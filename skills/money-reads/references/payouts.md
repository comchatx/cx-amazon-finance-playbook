# Payout reads: Transfers, `PAID`, on-demand payouts and other money APIs

## Payouts and expected payouts

- Transfers `listPayouts` returns past payouts and `listExpectedPayouts` the next expected one; Role Mappings name Finance and Accounting for both (P-api-11).
- A payout carries one of the status values Amazon defines, from `STARTED` to `NO_PAYOUT`, its trace id and its settlement id (P-api-11).
- An expected payout's status is `SCHEDULED`, `DISABLED`, `AT_RISK` or `NO_PAYOUT_EXPECTED` (P-api-11).
- Amazon's texts disagree on where Transfers answers: Role Mappings give Regions NA, EU and FE, while the Transfers model and the live `listPayouts` and `listExpectedPayouts` references name a list of EU marketplaces; read in Amazon's documents, not yet seen on a live account (P-api-11).
- Where Transfers answers for a seller is read from a `listPayouts` or `listExpectedPayouts` call for that seller's marketplace, with Amazon's current text on the Transfers API page and Role Mappings for SP-API Operations (P-api-11).

## What `PAID` means

- The Transfers model defines `PAID` as "successfully deposited in the bank"; Amazon's month-end skill says it "does not prove the deposit reached the bank"; read in Amazon's documents, not yet seen on a live account (P-api-12).
- Amazon's blog page How Amazon seller payments work gives how long funds can take to appear in a US bank account; no operation or page read gives it for another marketplace, and research/method/finance-surface.md, P-api-12, holds the value as read (P-api-12).

## On-demand payouts

- `initiatePayout` moves money (P-api-13).
- Amazon limits on-demand payouts per marketplace and account type; the marketplaces and the limit are read from `initiatePayout`'s description in the Transfers model and its reply for the seller's marketplace and account type, with the Transfers API page and Role Mappings for SP-API Operations (P-api-13).
- Role Mappings give `initiatePayout` Regions EU and "Required roles (need at least one)": Finance and Accounting, or Payment Initiation Service Provider, so Finance and Accounting alone is enough (P-api-13).

## Money APIs that are not the seller's disbursement

- Seller Wallet (Account Information and Payment Initiation Service Provider roles), Finance Remittance (vendors), Invoices v2026-06-25 (vendors) and Invoices v2024-06-19 (Brazil FBA invoices, Tax Invoicing) are not the ordinary seller disbursement (P-api-14).

## Amazon's month-end skill

- Amazon's `finance-month-end-closer` 1.3.1, in `amzn/selling-partner-agentic-toolkit`, runs on a private tool, `finances_monthEndClosing`, that no public model has (P-api-26).
- It classes settlements against a month as `inside`, `straddles_start`, `open_at_end` or `spans_month` (P-api-26).
- It states that a negative settlement counts as zero and carries forward; read in Amazon's documents, not yet seen on a live account (P-api-26).
- It states that the payout amount equals the settlement's net proceeds; read in Amazon's documents, not yet seen on a live account (P-api-26).
- It states that an open balance is not a guaranteed payout (P-api-26).
