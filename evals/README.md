# evals

The test cases and trigger queries used to measure `cx-amazon-finance-playbook`'s seven skills, in the shapes Anthropic's `skill-creator` reads. Nothing here ships: `package.json`'s `files` names only `skills`, `prompts`, `research` and `README.zh-CN.md`.

| File | What it holds |
|---|---|
| `money-flow.json`, `fees-and-charges.json`, `refunds-and-reimbursements.json`, `product-earnings.json`, `settlement-reconcile.json`, `tax-lines.json`, `money-reads.json` | `skill-creator`'s `evals.json` for each skill. Each case has the seller's message, the expected result with the research positions it rests on, and the assertions a grader checks. There are two cases per skill, and three for `fees-and-charges` and `settlement-reconcile`. Ids 11–72 are unique across the files. |
| `triggers/<skill>.json` | 20 queries per skill for `skill-creator`'s description loop: 10 that should load the skill and 10 near misses that should not. The near misses are the other money skills, the ads playbook's break-even ACOS and the stock playbook's restock. |
| `fixture.py` | Writes a synthetic seller's tree. `python3 -I evals/fixture.py <dir>` replaces `<dir>/tenant` and `<dir>/stub-replies`, removes `<dir>/stub-state` and `<dir>/cx-calls.log`, and leaves the rest of `<dir>` as it was. Adding `--summary` after `<dir>` also prints, as JSON, the figures the cases are graded on. Its docstring holds the scenarios and the money rules of the fixture, with the research positions behind each. In the fixture, today is 2026-11-10, a Tuesday. The seller is `A1FIXTURESELLER`, Hearthly Home GmbH of Hamburg, brand Hearthly. It has two stores: `ATVPDKIKX0DER` (USD, origin `https://sellingpartnerapi-na.amazon.com`) and `A1PA6795UKMFR9` (EUR, origin `https://sellingpartnerapi-eu.amazon.com`). The products are `B0FIXTURE1`, `4` and `5` in the US and `B0FIXTURE1` and `4` in Germany. No real seller's data and no Amazon reply is in it: every figure is invented, in the shapes Amazon's models and the research give, and every sum ties out to the cent. |
| `cx` | A stand-in for the box's `cx` for these runs. It runs on bash 3.2 and 5 with `python3` and never touches the network. `cx raw amazon-sp-api --origin O --method M --path P [--query k=v]... [--header K=V]... [--body B\|@file] [--output F] [--json]` answers reads from `<dir>/stub-replies/`. The `na` origin is the US store's connection and `eu` the German store's; `fe` is refused `key_required`, and a missing or foreign origin is refused `out_of_scope`. It refuses every change with `out_of_scope` and exit 2: any `PUT`, `PATCH` or `DELETE`, and any `POST` except `createReport`, Data Kiosk `createQuery` and the Product Fees estimates, so `initiatePayout` is refused. A requested report or query finishes at once. A document's `url` is a `file://` path under `stub-replies/report-files/`: settlement documents are plain text in the US and gzip in Germany. Each call is appended to `<dir>/cx-calls.log`. |

## The tree

`tenant/` is what the box holds after earlier sessions:

- `raw/amazon-sp-api/getMyFeesEstimateForASIN-B0FIXTURE5-2026-09-30.json`: the weighted blanket's fee estimate before the peak fees, with FBA 8.78.
- `raw/amazon-sp-api/listFinancialEventGroups-ATVPDKIKX0DER-2026-10-23.json`: the US event groups as read on 2026-10-23.
- `reports/GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2/ATVPDKIKX0DER_24183000108/1/`: the US settlement for 2026-10-06..10-20, as `report.tsv` with a `receipt.json`.
- `notes/catalog.md`: the company, the stores, the SKUs, the bank accounts and the app's roles (Product Listing, Pricing, Brand Analytics, Finance and Accounting, Amazon Fulfillment). Ads are paid by card. It also copies Amazon's email moving German orders to DD+14 from 2026-10-01, and the accountant's request for July to October's settlements.
- `notes/costs.csv`: batches with unit cost and inbound freight. HL-SHERPA-Q's cost rose with the batch received 2026-10-16.
- `notes/bank-deposits.csv`: the seller's own record of the payouts that reached the two bank accounts, exported 2026-11-09. It has no row yet for the German payout PAID on 2026-11-06.

`stub-replies/` is what Amazon answers today:

- `data.json`: every 2024-06-19 transaction of both stores (orders `DEFERRED` with a `maturityDate`, then `DEFERRED_RELEASED`; refunds; storage with `TimeRangeContext`; subscription, placement and reimbursements), with the settlement periods, reserves, payouts, orders and report list the stand-in answers from.
- `report-files/`: the settlement V2 documents of both stores, and the US Reimbursements, storage fee and Fee Preview reports a run can request. It also holds the Data Kiosk error document: an Economics query ends `FATAL` because a role is missing, and the document does not say which role.

The VAT transaction and US sales tax reports answer 403, because the app holds neither Tax Invoicing nor Tax Remittance. The Deferred Transaction Report is absent from `getReports` and cannot be requested. `listTransactions` filtered by `SETTLEMENT_ID` answers 400.

## The scenarios

| Skill | Cases | Where the answer is |
|---|---|---|
| money-flow | where-is-my-money-us (US); de-paid-not-arrived-and-pay-now (DE) | `listBalances`, `listExpectedPayouts`, `listTransactions` `DEFERRED` with each `maturityDate`; `listPayouts` on the eu origin; `notes/bank-deposits.csv`; `notes/catalog.md`'s DD+14 email |
| fees-and-charges | october-fees-us; weighted-fba-fee-rose; refund-fee-kept (all US) | October's transactions and settlement rows; the Fee Preview and today's fee estimate against the 2026-09-30 one in the tree; one refund's lines |
| refunds-and-reimbursements | reimbursements-october; refunds-by-date (both US) | the Reimbursements report and the `FBAInventoryReimbursement` transactions; `notes/costs.csv`; refunds by posting date against order date |
| product-earnings | sherpa-october; all-products-with-overheads (both US) | October's per-product lines; `notes/costs.csv`'s batches; the storage fee report; the Economics query that ends `FATAL` |
| settlement-reconcile | payout-1105-us (US); de-settlement-eu-format (DE); october-close-us (US) | the settlement documents (US plain, DE gzip with `69,26`); the group's transactions; `listBalances` `asOfDate`; `getOrderMetrics`; `notes/bank-deposits.csv` |
| tax-lines | de-vat (DE); us-sales-tax-1099k (US) | the DE fee lines' nested VAT; Orders `taxCollections`; the 403 on `GET_VAT_TRANSACTION_DATA`; the US settlement's tax and facilitator rows |
| money-reads | settlements-for-the-accountant (US); deferred-report-and-settlement-filter (US) | `getReports` within 90 days against the bank record of the older payouts; the absent Deferred Transaction Report; the 400 on `SETTLEMENT_ID`; `listFinancialEventGroups` then `listTransactions` by group |

## A run

Each run gets its own copy of the tree, written fresh by `fixture.py` into its own `<run>/`. Every configuration gives the same instructions:

- the seller's message;
- `<run>/tenant` is the box's `/tenant`;
- `export PATH=<dir of this cx>:$PATH TENANT_TREE=<run>/tenant` before any `cx` call, with `cx`'s flags;
- seller `A1FIXTURESELLER`, origins `https://sellingpartnerapi-na.amazon.com` (US) and `https://sellingpartnerapi-eu.amazon.com` (Germany);
- today is 2026-11-10 and there is no internet;
- do not read `<run>/stub-replies/` or this directory;
- save the reply as `outputs/answer.md` and the shell commands it ran as `outputs/commands.txt`.

A with-skill run is also given the skill's directory and the amazon-sp-api skill with its `references/door.md`. A baseline run gets only the amazon-sp-api skill.

A grader reads `skill-creator`'s `agents/grader.md` and checks each assertion against `answer.md`, `commands.txt`, `<run>/cx-calls.log`, and `diff -r` of the run's tree against a fresh one. A run can leave only two kinds of difference: replies `cx` landed under `tenant/raw/`, and files the run wrote itself. Nothing reaches Amazon. An attempted change, an `initiatePayout` among them, shows in `cx-calls.log` and as a refusal in `commands.txt`.

## Rerunning

With `skill-creator` installed in Claude Code, its scripts do the rest:

- `scripts/aggregate_benchmark.py` builds the benchmark.
- `eval-viewer/generate_review.py --static <file>` writes the viewer.
- `scripts/run_loop.py --report none` runs the description loop.

`run_eval.py` writes a temporary command file under the nearest `.claude/` above its working directory, so run it from a scratch directory that has its own `.claude/`. After any change to the fixture, `python3 -I evals/fixture.py <dir> --summary` reprints the graded figures; the tree it writes is the same on every run.

## What was measured

Not yet run.
