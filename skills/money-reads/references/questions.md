# Money questions and the reads that answer them

## Balances and payouts

- What the account holds now or held on a past date, available, reserved, deferred or held as an account-level reserve: `listBalances` by `balanceType`, with `asOfDate` for a past date; whether it answers in NA and FE for an ordinary seller is not yet seen on a live account (P-api-7).
- The net proceeds of a date period or of one settlement: `listSummary` (P-api-8).
- The next payout and whether it is at risk: `listExpectedPayouts`, read in Amazon's documents, not yet seen on a live account (P-api-11).
- Past payouts, their status and trace ids: `listPayouts`, read in Amazon's documents, not yet seen on a live account; v0 `listFinancialEventGroups` carries the trace id too (P-api-11, P-api-10).
- A settlement period's open or closed status, beginning balance and fund transfer date: the v0 `FinancialEventGroup` (P-api-10).
- The transactions that make up one payout: Amazon's guide reads them from `listTransactions` by `FINANCIAL_EVENT_GROUP_ID` with `RELEASED`, read in Amazon's documents, not yet seen on a live account (P-api-6).
- Money deferred now: `listTransactions` returns it with the status `DEFERRED`, and v0 omits it until release (P-api-1, P-api-9).
- An on-demand payout: `initiatePayout`, which moves money, in the marketplaces its description in the Transfers model names (Role Mappings: Region EU); see references/payouts.md (P-api-13).
- ../money-flow/SKILL.md: how money moves from an order to the bank, and what each balance means.

## Fees and charges

- Each charge and fee on an order, a payout group or a date range: `listTransactions` by `ORDER_ID`, `FINANCIAL_EVENT_GROUP_ID` or posted dates, in its nested `breakdowns[]`, whose `breakdownType` values are open strings; which appear on a seller's data is read in Amazon's documents, not yet seen on a live account (P-api-3, P-api-4).
- A fee before the sale: the Product Fees estimates, which Amazon calls "not guaranteed" (P-api-19).
- The referral fee preview and the FBA fee preview: `GET_REFERRAL_FEE_PREVIEW_REPORT` and `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` (P-sell-33, P-tool-26).
- Storage and aged-inventory surcharge charges: `GET_FBA_STORAGE_FEE_CHARGES_DATA` and `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` (P-tool-26, P-api-18).
- The overage fee: its report type, under Amazon Fulfillment (P-api-18).
- Fees per product over a range: Data Kiosk Economics, fees by type (P-api-22).
- ../fees-and-charges/SKILL.md: what each fee is and how it is computed and posted.

## Refunds and reimbursements

- Refund lines of one order: `listTransactions` filtered by `ORDER_ID` (P-api-1, P-api-3).
- FBA reimbursements: `GET_FBA_REIMBURSEMENTS_DATA` (P-tool-26).
- FBA customer returns and removals: the returns and removal report types (P-api-18).
- Inventory unit movements: the ledger reports, under Amazon Fulfillment (P-api-18).
- ../refunds-and-reimbursements/SKILL.md: refunds, claims, reimbursements and adjustments as money.

## Product earnings

- Per-product sales, fees, ads, entered costs and net proceeds: Data Kiosk Economics (P-api-22).
- Ordered sales, units and orders per interval: Sales `getOrderMetrics` (P-api-21).
- An order's proceeds and its tax collection model: Orders v2026-01-01, which carries no Amazon fee (P-api-20).
- ../product-earnings/SKILL.md: what each product earned and the counting choices behind it.

## Settlements and deferrals

- A settlement's lines: `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`, reachable through the API only within the 90 days `getReports` lists; older ones in references/history.md (P-api-15, P-api-16, P-api-30).
- What is deferred at the moment of asking: the Deferred Transaction Report, which Amazon states is requested in Seller Central before the Reports API retrieves it, read in Amazon's documents, not yet seen on a live account; `listBalances` with `DEFERRED` gives the amount (P-api-17, P-api-35, P-api-7).
- ../settlement-reconcile/SKILL.md: settlement lines, the documents' clocks and how they tie to payouts.

## Tax

- US sales tax lines: the US sales tax report, under Tax Remittance (Restricted); EU VAT lines: the VAT reports, under Tax Invoicing (Restricted) (P-api-18).
- Tax forms and the US sales tax report's generation: Seller Central's Tax Document Library (P-api-37).
- ../tax-lines/SKILL.md: the kinds of tax in a money line and the documents that carry them.

## History

- How far back each read reaches: references/history.md.
