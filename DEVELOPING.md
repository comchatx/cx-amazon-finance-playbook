# Developing cx-amazon-finance-playbook

The README is written for a seller, in English (`README.md`) and Chinese (`README.zh-CN.md`); the Plugins page draws it. These are the notes for whoever works on the package.

A [pi](https://pi.dev) package for a seller's Amazon money, read through SP-API: where the money is between an order and the bank, every fee and charge, refunds and reimbursements, what each product earned, settlements against the bank and the books, the taxes in a money line, and which read holds each money fact. It is written for the assistant in a [ComChatX](https://comchatx.com) seller's box, and reads the seller's account through the box's `cx` command and the [`cx-amazon-sp-api`](https://github.com/comchatx/cx-amazon-sp-api) package.

It is text only: no script, no extension, no dependency. Its changes are in [CHANGELOG.md](CHANGELOG.md). Every line of the skills ends with the position it rests on, as `(P-flow-8)` or `(P-rec-4, P-tool-7)`, and the positions are in the nine files under [`research/`](research/README.md); a line without one only points to another file.

## What it holds

| | What the model reads | Positions |
|---|---|---|
| `skills/money-flow` | Where the money is between an order and the bank: deferred, reserved, available, disbursed; payouts, negative balances, currencies | P-flow, P-tool |
| `skills/fees-and-charges` | Selling, programme, FBA, storage, inbound, removal and service fees: how each is worked out, when it posts, which line it is on | P-sell, P-ful, P-tool |
| `skills/refunds-and-reimbursements` | Refunds, A-to-z and chargebacks, SAFE-T, reimbursements and their reversals, adjustments | P-ref, P-tool |
| `skills/product-earnings` | Amazon's per-product net proceeds and its surfaces, the seller's own costs, and the counting choices and what each changes | P-prof, P-tool |
| `skills/settlement-reconcile` | Settlement V2, the documents' clocks, payouts against transactions, money outside the settlement, the ledger side | P-rec, P-tool |
| `skills/tax-lines` | The kinds of tax in a money line, who owes or has paid each, and the tax documents | P-tax |
| `skills/money-reads` | Which operation or report holds each money fact, with its role, window, lag and pitfalls | P-api, P-tool |
| `prompts/*.md` | `/money-where`, `/fees-review`, `/product-earnings`, `/settlement-check`, `/refunds-review`: each hands the seller's words to cx | |

Each template's `description:` is one English sentence; its Chinese is `comchatx.prompts.<name>.zh` in `package.json`, beside each skill's words in `comchatx.skills`, as the Plugins page reads them.

How a call is made and how a report is asked for and landed is the `amazon-sp-api` skill's (`references/door.md`), never this package's. `@comchatx/cx-amazon-ads` is optional: where the seller has it, it reads each product's ad spend. What an ad sale earns against its cost is `@comchatx/cx-sponsored-ads-playbook`'s, and stock and restocking are `@comchatx/cx-amazon-stock-playbook`'s; nothing of theirs is written here.

Seven positions are the writing seats' own reasoning and no skill cites them: P-api-29, P-flow-35, P-rec-37, P-ref-30, P-ref-51, P-sell-41 and P-sell-52. P-tool-34 and P-tool-35 enter without their last clauses, which are the seat's own.

A value that differs by marketplace or year (a fee rate, a reserve or payout schedule, a tax rate, a threshold or a filing date) is in no line of a skill: the line says where it is read, and the research keeps the value as it was read, with its marketplace and date.

## Install

```bash
pi install npm:@comchatx/cx-amazon-finance-playbook
```

On ComChatX, a seller installs it from the Plugins page.

## Develop

```bash
npm ci
npm run typecheck
npm test               # pi at the pin loads the package and its tarball and expands every template;
                       # every line of the skills cites a position that exists, none of the seven [seat] ones,
                       # and each of the 423 others is cited; each SKILL.md body is at most 371 words;
                       # no line of a skill file, frontmatter and headings included, names a request route
                       # or states a rate, an amount, a threshold, a filing date or a reserve or payout schedule
```

The skills were measured with Anthropic's `skill-creator`; the cases, the fixture and the stand-in `cx` are in [`evals/`](evals/README.md), and nothing there ships.

## Release

A tag `v<version>` on `main`, the version in `package.json`, runs `.github/workflows/release.yml`, which publishes through npm trusted publishing. WRITING-A-PACKAGE.md, "Shipping it", gives the steps before the first release.
