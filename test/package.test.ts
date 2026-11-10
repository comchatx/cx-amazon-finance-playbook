import { execFileSync } from "node:child_process";
import { cpSync, existsSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { expect, it } from "vitest";
import { loadPackage, scratch, typed } from "./pi.js";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const SKILLS = ["fees-and-charges", "money-flow", "money-reads", "product-earnings", "refunds-and-reimbursements", "settlement-reconcile", "tax-lines"] as const;
const PROMPTS = ["fees-review", "money-where", "product-earnings", "refunds-review", "settlement-check"] as const;
const skillFile = (name: string) => join(ROOT, "skills", name, "SKILL.md");
const manifest = () => JSON.parse(readFileSync(join(ROOT, "package.json"), "utf8")) as Record<string, unknown>;

// The Plugins page lists a skill or template only when its description is English: no letter, mark or punctuation of another script.
const NOT_LATIN = /[^\p{Script=Latin}\p{Script=Common}\p{Script=Inherited}]|[\u3000-\u303F\uFF00-\uFFEF]/u;

it("the pinned pi loads seven skills and five templates from the package, and nothing else, each described in Latin script", async () => {
  const { loader } = await loadPackage(ROOT);
  const skills = loader.getSkills();
  const prompts = loader.getPrompts();
  expect(skills.diagnostics).toEqual([]);
  expect(prompts.diagnostics).toEqual([]);
  for (const one of [...skills.skills, ...prompts.prompts]) expect(one.description, one.name).not.toMatch(NOT_LATIN);
  expect(skills.skills.map((skill) => skill.name).sort()).toEqual([...SKILLS]);
  expect(skills.skills.map((skill) => skill.filePath).sort()).toEqual(SKILLS.map(skillFile));
  expect(prompts.prompts.map((prompt) => prompt.name).sort()).toEqual([...PROMPTS]);
  expect(loader.getExtensions().extensions).toEqual([]);
});

it("every directory under skills/ holds a SKILL.md and no script: the call is the door's", () => {
  const directories = readdirSync(join(ROOT, "skills"), { withFileTypes: true }).filter((entry) => entry.isDirectory()).map((entry) => entry.name).sort();
  expect(directories).toEqual([...SKILLS]);
  for (const name of directories) {
    expect(existsSync(skillFile(name)), `skills/${name}/SKILL.md`).toBe(true);
    expect(existsSync(join(ROOT, "skills", name, "scripts")), `skills/${name}/scripts`).toBe(false);
  }
});

it("each template expands in a pi session: its arguments and the seller's own words reach the model, no placeholder does", async () => {
  const expected: Record<(typeof PROMPTS)[number], [string, string]> = {
    "money-where": ["/money-where 只看欧洲站", "Tell me where my Amazon money is now: how much is available, how much is deferred and how much is held in reserve, and when my next payout reaches my bank. 只看欧洲站"],
    "fees-review": ["/fees-review 2026-10 SKU-1", "Show me which fees Amazon took from me last month, how each one was worked out, and what changed against the months before. 2026-10 SKU-1"],
    "product-earnings": ["/product-earnings", "Work out what each of my products earned on Amazon last month, after all of Amazon's fees and my own costs."],
    "settlement-check": ["/settlement-check DE 到账少了", "Match my latest Amazon settlement to the money that reached my bank, and explain where each difference comes from. DE 到账少了"],
    "refunds-review": ["/refunds-review 2026-10", "Show me last month's refunds, reimbursements and adjustments, how much each came to, and which orders or shipments each ties back to. 2026-10"],
  };
  for (const [name, [input, text]] of Object.entries(expected)) {
    const received = await typed(ROOT, input);
    expect(received.trim(), name).toBe(text);
    expect(received, name).not.toMatch(/\$\{?[@0-9A]/);
  }
}, 120_000);

it("the package carries no dependency, no install script and no extension", () => {
  const pkg = manifest();
  for (const field of ["dependencies", "peerDependencies", "optionalDependencies", "bundleDependencies", "bundledDependencies"]) expect(pkg[field], field).toBeUndefined();
  expect(pkg["scripts"]).toEqual({ typecheck: "tsc --noEmit", test: "vitest run" });
  expect(pkg["keywords"]).toEqual(["pi-package"]);
  expect(pkg["pi"]).toEqual({ skills: ["./skills"], prompts: ["./prompts"] });
  expect(readdirSync(ROOT)).not.toContain("extensions");
});

it("the package's name lives in package.json: its repository fields and every file that names it follow that one line", () => {
  const pkg = manifest() as { name: string; homepage: string; bugs: string; repository: { url: string } };
  expect(pkg.name).toMatch(/^@comchatx\/cx-amazon-/);
  const repo = pkg.name.replace(/^@comchatx\//, "");
  expect(pkg.homepage).toBe(`https://github.com/comchatx/${repo}#readme`);
  expect(pkg.bugs).toBe(`https://github.com/comchatx/${repo}/issues`);
  expect(pkg.repository.url).toBe(`git+https://github.com/comchatx/${repo}.git`);
  for (const file of ["README.md", "README.zh-CN.md", "DEVELOPING.md", "CHANGELOG.md", "evals/README.md", "research/README.md"]) {
    const text = readFileSync(join(ROOT, file), "utf8");
    for (const named of text.match(/(?:@comchatx\/)?cx-(?:amazon-)?(?:finance|money)-playbook\b/g) ?? []) expect(named.replace(/^@comchatx\//, ""), file).toBe(repo);
  }
});

it("the Plugins page's field names every skill and template in both languages, and what the skills read", () => {
  const { comchatx } = manifest() as { comchatx: { skills: Record<string, { about: { en: string; zh: string } }>; prompts: Record<string, { zh: string }>; builds: unknown } };
  expect(Object.keys(comchatx.skills).sort()).toEqual([...SKILLS]);
  for (const [name, words] of Object.entries(comchatx.skills)) {
    expect(words.about.zh, name).toMatch(/[一-鿿]/);
    expect(words.about.en, name).not.toMatch(/[一-鿿]/);
  }
  expect(Object.keys(comchatx.prompts).sort()).toEqual([...PROMPTS]);
  for (const [name, words] of Object.entries(comchatx.prompts)) expect(words.zh, name).toMatch(/[一-鿿]/);
  expect(comchatx.builds).toEqual([
    { on: "cx-amazon-sp-api", need: "required" },
    { on: "@comchatx/cx-amazon-ads", need: "optional" },
  ]);
});

it("money-reads points to the door's own skill for how a call is made and a report is landed", () => {
  const reads = readFileSync(skillFile("money-reads"), "utf8");
  expect(reads).toContain("amazon-sp-api");
  expect(reads).toContain("references/door.md");
});

const walk = (directory: string): string[] =>
  readdirSync(directory, { withFileTypes: true }).flatMap((entry) => (entry.isDirectory() ? walk(join(directory, entry.name)) : [join(directory, entry.name)]));

it("ships its skills, its templates, its research, its README in English and in Chinese and its license, and nothing else", () => {
  // npm 12 keys its answer by the package's name; earlier ones answer a list.
  const answer = JSON.parse(execFileSync("npm", ["pack", "--dry-run", "--json", "--ignore-scripts"], { cwd: ROOT, encoding: "utf8" })) as { files: { path: string }[] }[] | Record<string, { files: { path: string }[] }>;
  const packed = Array.isArray(answer) ? answer : Object.values(answer);
  const shipped = ["skills", "prompts", "research"].flatMap((directory) => walk(join(ROOT, directory)).map((path) => relative(ROOT, path)));
  expect(packed[0]!.files.map((file) => file.path).sort()).toEqual(["LICENSE", "README.md", "README.zh-CN.md", "package.json", ...shipped].sort());
  expect(manifest()["files"]).toEqual(["skills", "prompts", "research", "README.zh-CN.md"]);
});

/** What the pinned pi loads from a package root: its skills, its templates and any diagnostic. */
const shelf = async (root: string) => {
  const { loader } = await loadPackage(root);
  const skills = loader.getSkills();
  const prompts = loader.getPrompts();
  return {
    skills: skills.skills.map((skill) => skill.name).sort(),
    prompts: prompts.prompts.map((prompt) => prompt.name).sort(),
    diagnostics: [...skills.diagnostics, ...prompts.diagnostics],
  };
};

/** The tarball npm would publish, unpacked: the package as a seller's pi installs it. */
const packed = (from: string): string => {
  const out = scratch();
  const reply = JSON.parse(execFileSync("npm", ["pack", "--json", "--ignore-scripts", "--pack-destination", out], { cwd: from, encoding: "utf8" })) as
    | { filename: string }[]
    | Record<string, { filename: string }>;
  // npm 10 answers a list; npm 11 answers an object keyed by the package's name.
  const [result] = Array.isArray(reply) ? reply : Object.values(reply);
  execFileSync("tar", ["xzf", join(out, result!.filename), "-C", out]);
  return join(out, "package");
};

it("the published tarball loads seven skills and five templates under the pinned pi, with no diagnostic, and ships no evals or tests", async () => {
  const root = packed(ROOT);
  expect(await shelf(root)).toEqual({ skills: [...SKILLS], prompts: [...PROMPTS], diagnostics: [] });
  for (const left of ["evals", "test"]) expect(existsSync(join(root, left)), left).toBe(false);
  expect(existsSync(join(root, "research", "README.md"))).toBe(true);
}, 120_000);

it("the same check fails a copy whose money-flow description is emptied", async () => {
  const copy = join(scratch(), "copy");
  cpSync(packed(ROOT), copy, { recursive: true });
  const file = join(copy, "skills", "money-flow", "SKILL.md");
  writeFileSync(file, readFileSync(file, "utf8").replace(/^description: .*$/m, 'description: ""'));
  const loaded = await shelf(copy);
  expect(loaded.skills).not.toContain("money-flow");
  expect(loaded.diagnostics.map((one) => [one.message, one.path])).toEqual([["description is required", file]]);
}, 120_000);
