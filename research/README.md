# Research for the money playbook (working name `@comchatx/cx-money-playbook`)

This directory is the research base for a pi skill pack over `cx-amazon-sp-api`, ComChatX's open door to Amazon's Selling Partner API (`cx raw amazon-sp-api`). The pack covers where a seller's Amazon money is and what each product earned. Brief 2026-11-03-306 asked for the research first; its correction 1 governs every value that changes by marketplace or by year.

## How the files were made

- Nine research files were written by nine seats on 2026-11-09/10. Each file was then checked by an adversarial verifier, who re-read quotes from raw pages and the models clone and corrected the file in place.
- Two completeness critics then named 24 gaps, which were filled with sources: a US/EU controller of an eight-figure seller, and a 财务总监 of a large Chinese cross-border seller.
- Correction 1 was then applied. Every position whose substance is a value that differs by marketplace or year says where cx reads it ("Read at run time: …"). Where no operation or page gives the value, the position says so and keeps the value with its marketplace and date.

## Rules of the files

**Source order:**
1. Amazon's own words, tagged **[official]**: Seller Forums News and staff posts, sell.amazon.*, globalselling.amazon.com, sellingpartners.aboutamazon.com, developer-docs, the SP-API models, rate-card PDFs;
2. named practitioners and tools, tagged **[opinion]**, English and Chinese alike;
3. published research, tagged **[research]**.

**A [seat] line** is the writing seat's own reasoning and enters no skill.

**Kept out:**
- no Amazon API host was called;
- no Seller Central help-hub content call was made (plain GET of a help page returns a JavaScript shell, so each file names the route it used instead);
- no seller data is held here.

**Positions** are facts and discipline under decision D233. Each is a definition, a rule of Amazon's, a dated deadline, a pitfall of the data, a measured effect, or a fact about a named tool or practitioner. None says when to ask the seller, imposes an order of work, sets a threshold of ours, or puts a ceiling on what cx may read or change.

**Values that move** (rates, bands, caps, windows, schedules, tax rates) are kept in a position only as evidence, with the marketplace, the date read and the citation; the position names where the value is read.

## Files

| File | Covers | Positions |
|---|---|---|
| `areas/money-flow.md` | order to bank: deferred, reserve, available, disbursed, on-demand payouts, negative balances, currencies and the CNY leg, held funds, per-store schedules | P-flow-1…51 |
| `areas/selling-fees.md` | selling, programme and service fees: computation, posting, names; promotions, Vine, ads in finances, Haul, EPR, ACCS | P-sell-1…52 |
| `areas/fulfilment-charges.md` | FBA, storage, inbound, removal, returns, capacity, MCF, AGL and freight charges as money | P-ful-1…40 |
| `areas/refunds-reimbursements-adjustments.md` | refunds, A-to-z, chargebacks, SAFE-T, reimbursements and their value and windows, reversals, adjustments, value recovery | P-ref-1…51 |
| `areas/product-profit.md` | per-product earnings: Amazon's definition and surfaces, the seller's costs, the counting choices, stock as an asset, import VAT | P-prof-1…55 |
| `areas/reconciliation.md` | settlement V2, the documents' clocks, Date Range and deferred reports, payout-to-transactions, money outside the settlement, multi-account layout, retention | P-rec-1…59 |
| `areas/tax-and-invoices.md` | the four kinds of tax in a money line, tax documents and their roles, US nexus, the China side, import VAT | P-tax-1…47 |
| `method/finance-surface.md` | every money read with path, rate, role and deprecation; the role grid; pitfalls; borrow-first; the door | P-api-1…38 |
| `beyond/sellers-tools-and-research.md` | sellers' paid tools and practice (English and Chinese), where they disagree, practitioners, published research | P-tool-1…37 |

Each file has the same layout:
1. what it covers;
2. Amazon's rules;
3. the SP-API and report faces;
4. practitioners;
5. published research;
6. stable enough for a skill;
7. read at run time;
8. what only Seller Central shows;
9. facts for human readers only;
10. pages read;
11. open questions;
12. positions;
13. verification.

## What the pack would hold (proposed; Jack's word pending)

- **Skills:** `money-flow`, `fees-and-charges`, `refunds-and-reimbursements`, `product-earnings`, `settlement-reconcile`, `tax-lines`, `money-reads`.
- **Templates:** `/money-where`, `/fees-review`, `/product-earnings`, `/settlement-check`, `/refunds-review`.
- **Packages named:**
  - `cx-amazon-sp-api` is required;
  - `cx-amazon-ads` is optional, for ad spend per product.
- **Script:** none.
