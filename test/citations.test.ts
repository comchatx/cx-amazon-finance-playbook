import { readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { expect, it } from "vitest";
import { body } from "./pi.js";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const PREFIX = "(?:flow|sell|ful|ref|prof|rec|tax|api|tool)";
const ID = new RegExp(`P-${PREFIX}-\\d+`, "g");
const GROUP = new RegExp(`\\((P-${PREFIX}-\\d+(?:\\s*[,;]\\s*P-${PREFIX}-\\d+)*)\\)`, "g");

/** The seven positions that are the writing seats' own reasoning: they enter no skill. */
export const SEAT = ["P-api-29", "P-flow-35", "P-rec-37", "P-ref-30", "P-ref-51", "P-sell-41", "P-sell-52"] as const;

const markdown = (directory: string): string[] =>
  readdirSync(directory, { recursive: true, encoding: "utf8" }).filter((file) => file.endsWith(".md")).map((file) => join(directory, file));

/** Each research file's `## Positions` section, as far as its `## Verification`. */
const sections = markdown(join(ROOT, "research"))
  .filter((file) => !file.endsWith("README.md"))
  .map((file) => {
    const text = readFileSync(file, "utf8");
    const start = text.indexOf("\n## Positions");
    const end = text.indexOf("\n## Verification", start);
    return { file, text: text.slice(start, end < 0 ? undefined : end) };
  });

/** Every position, as a research file opens it: `**P-<area>-<n>.**` (or `**P-<area>-<n> [seat].**`) at the head of a line or a list entry, with the opening of its text. */
const positions = new Map(
  sections.flatMap(({ text }) =>
    [...text.matchAll(new RegExp(`^(?:\\s*(?:\\d+\\.|-)\\s*)?\\*\\*(P-${PREFIX}-\\d+)( \\[seat\\])?\\.\\*\\*(.*)$`, "gm"))].map((match) => [match[1]!, `${match[2] ?? ""}${match[3]!}`] as const),
  ),
);

/** A line that only points: to a reference, another skill, the door's skill or the research. */
const pointer = (line: string) => /references\/[\w-]+\.md|\.\.\/[\w-]+\/SKILL\.md|research\/|amazon-sp-api/.test(line);

/** Each text line of the skills and their references, with the ids its citation groups name. */
const lines = markdown(join(ROOT, "skills")).flatMap((file) =>
  body(readFileSync(file, "utf8"))
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line !== "" && !line.startsWith("#") && !/^\|?[-:| ]+\|?$/.test(line))
    .map((line) => ({ file, line, ids: [...line.matchAll(GROUP)].flatMap((group) => group[1]!.match(ID) ?? []) })),
);

it("the research holds 430 positions, seven of them the seats' own, each marked [seat] where it opens or saying it enters no skill", () => {
  expect(positions.size).toBe(430);
  const marked = [...positions].filter(([, opening]) => /^\s*\[seat\b|enters no skill/.test(opening)).map(([id]) => id).sort();
  expect(marked).toEqual([...SEAT]);
});

it("every line of the skills and their references cites a position that exists, except a line that only points", () => {
  expect(lines.length).toBeGreaterThan(0);
  for (const { file, line, ids } of lines) {
    if (ids.length === 0) expect(pointer(line), `${file}: ${line}`).toBe(true);
    for (const id of ids) expect(positions.has(id), `${file}: ${id}`).toBe(true);
  }
});

it("no [seat] position is cited", () => {
  const seat = new Set<string>(SEAT);
  for (const { file, ids } of lines) for (const id of ids) expect(seat.has(id), `${file}: ${id}`).toBe(false);
});

it("each of the 423 positions that are not the seats' own is cited somewhere in the skills", () => {
  const cited = new Set(lines.flatMap(({ ids }) => ids));
  const entering = [...positions.keys()].filter((id) => !(SEAT as readonly string[]).includes(id));
  expect(entering).toHaveLength(423);
  expect(entering.filter((id) => !cited.has(id)).sort()).toEqual([]);
});

it("P-tool-34 and P-tool-35 enter without their last clauses, which are the seat's own", () => {
  for (const { file, line, ids } of lines) {
    if (ids.includes("P-tool-34")) expect(line, file).not.toMatch(/net profit/i);
    if (ids.includes("P-tool-35")) expect(line, file).not.toMatch(/monetary item/i);
  }
});

/** Every skill file whole, its frontmatter and headings included. */
const files = markdown(join(ROOT, "skills")).map((file) => ({ file, text: readFileSync(file, "utf8") }));

/** The lines of a file's whole text that a check finds. */
const caught = (text: string, check: (line: string) => boolean): string[] => text.split("\n").filter(check);

const CURRENCY = "USD|EUR|GBP|JPY|CAD|MXN|BRL|INR|AUD|SGD|AED|SAR|EGP|TRY|SEK|PLN|CNY|RMB|ZAR|NZD|CHF|IEP";
/** A rate: a percentage. */
const PERCENT = /\d\s*%|\d\s*percent\b|\bper ?cent\b/i;
/** An amount of money: a currency sign or code beside a figure. */
const MONEY = new RegExp(`[$€£¥₹]\\s?\\d|\\b\\d[\\d,.]*\\s?(?:${CURRENCY})\\b|\\b(?:${CURRENCY})\\s?\\d|\\d\\s?(?:元|美元|欧元|英镑|日元)`);
/** A schedule by its count: a delivery-date policy's days, or a span of days, weeks or months beside a word of money's timing, a claim or a filing. */
const SPAN = /\b\d+\s*(?:-|–|to)?\s*\d*\s*(?:calendar |business )?(?:day|days|week|weeks|month|months|hours)\b/i;
const TIMING = /\b(?:reserve\w*|payout\w*|disburse\w*|deferr\w*|release\w*|matur\w*|claim\w*|deadline\w*|due|fil(?:e|es|ed|ing)|threshold\w*|regist\w*|eligib\w*|reimburs\w*|refund\w*|return\w*|settlement periods?|cycles?)\b/i;
const SCHEDULE = (line: string) => /\bDD\s*\+\s*\d/i.test(line) || (SPAN.test(line) && TIMING.test(line));
/** A calendar date beside a word of tax, a threshold or a deadline: the year's date of a tax rule. */
const CALENDAR = /\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.? \d{1,2}\b|\b\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December)\b|\b(?:19|20)\d{2}-\d{2}-\d{2}\b/;
const TAXWORD = /\b(?:tax|VAT|GST|HST|PST|QST|1099|deadline|due|threshold|regist\w*|fil(?:e|es|ed|ing))\b/i;
/** A count of transactions or a sum beside a word of threshold or tax reporting. */
const COUNT = /\b\d[\d,]*\s+(?:transactions|orders|sales|units)\b/i;
const changing = (line: string) =>
  PERCENT.test(line) || MONEY.test(line) || SCHEDULE(line) || (CALENDAR.test(line) && TAXWORD.test(line)) || (COUNT.test(line) && TAXWORD.test(line));

/** A skill file with one line placed in its frontmatter, its heading or its body. */
const control = (where: "frontmatter" | "heading" | "body", line: string) =>
  [
    "---",
    "name: money-example",
    where === "frontmatter" ? `description: "${line}"` : 'description: "An example."',
    "---",
    "",
    where === "heading" ? `## ${line}` : "## Example",
    "",
    where === "body" ? `- ${line} (P-flow-1)` : "- A line (P-flow-1).",
  ].join("\n");

it("no line of any skill file, frontmatter and headings included, states a tax rate, a threshold, a filing deadline, a fee rate, an amount, or a reserve or payout schedule: each differs by marketplace or year, and is read where Amazon or the authority gives it", () => {
  expect(files.length).toBeGreaterThan(0);
  for (const { file, text } of files) expect(caught(text, changing), file).toEqual([]);
});

it("the changing-value check catches a rate, an amount, a schedule, a threshold and a deadline in a body line, a heading and the frontmatter", () => {
  for (const line of [
    "The referral fee is 15% for most categories",
    "The FBA fee for a small standard unit is $3.06",
    "Funds are held under DD+7",
    "The reserve releases 7 days after delivery",
    "A reimbursement claim is filed within 60 days",
    "The 1099-K threshold is 200 transactions",
    "UK VAT registration applies above £90,000",
    "The VAT return is due 2027-01-31",
    "Payouts run every 14 days",
    "A unit costs 25 元",
  ]) {
    for (const where of ["frontmatter", "heading", "body"] as const) expect(caught(control(where, line), changing), `${where}: ${line}`).toHaveLength(1);
  }
  for (const line of [
    "The referral fee's rate is read from getMyFeesEstimateForSKU for the seller's own marketplace",
    "The delivery-date policy's release day is the transaction's maturityDate",
    "Settlement V1 and the XML report are removed on 2026-11-11",
    "Finances v0's event operations are removed on 2027-08-27",
    "A settlement period's dates are the report's settlement-start-date and settlement-end-date",
  ]) {
    for (const where of ["frontmatter", "heading", "body"] as const) expect(caught(control(where, line), changing), `${where}: ${line}`).toEqual([]);
  }
});

/** An SP-API request route as a request names it: a method and a path, or a path of Amazon's from its root. */
const ROUTE =
  /\b(?:GET|POST|PUT|PATCH|DELETE)\s+`?\/|`\/[A-Za-z]|(?<![\w.~/])\/(?:finances|reports|transfers|products|dataKiosk|sellers|orders|fba|tokens|notifications|catalog|listings|externalFulfillment|feeds|finance|tax|invoices|vendor|sellerWallet|inbound|easyShip|shipping|replenishment|aplus|authorization|solicitations|messaging)\//;
const mechanics = (line: string) => ROUTE.test(line);

it("no line of any skill file names an SP-API request route: how a call is made is the amazon-sp-api skill's", () => {
  for (const { file, text } of files) expect(caught(text, mechanics), file).toEqual([]);
});

it("the route check catches a route in a body line, a heading and the frontmatter, and passes an operation's name", () => {
  for (const line of ["`GET /finances/2024-06-19/transactions` lists transactions", "Payouts come from /finances/transfers/2024-06-01/payouts"]) {
    for (const where of ["frontmatter", "heading", "body"] as const) expect(caught(control(where, line), mechanics), `${where}: ${line}`).toHaveLength(1);
  }
  for (const line of ["`listTransactions` returns posted transactions", "deferred/released and SP/MCF"]) {
    for (const where of ["frontmatter", "heading", "body"] as const) expect(caught(control(where, line), mechanics), `${where}: ${line}`).toEqual([]);
  }
});

it("each SKILL.md body is at most 371 words", () => {
  for (const name of readdirSync(join(ROOT, "skills"))) {
    const words = body(readFileSync(join(ROOT, "skills", name, "SKILL.md"), "utf8")).split(/\s+/).filter(Boolean).length;
    expect(words, name).toBeLessThanOrEqual(371);
  }
});
