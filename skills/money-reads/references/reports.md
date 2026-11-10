# Money report types

## Settlement report

- `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` is the settlement report that remains, and Role Mappings for Types name Finance and Accounting for it (P-api-15, P-tool-26).
- The SP-API Deprecation Schedule, as read on 2026-11-09, lists the v1 and XML settlement reports for removal on 2026-11-11; the current state is read on that page (P-api-15).
- The V2 columns are the 24 Amazon lists; amounts sit in one `amount` column, described by `amount-type` and `amount-description` (P-api-16).
- Through the API alone a settlement report is reachable only within the 90 days `getReports` lists (P-api-30).

## Deferred Transaction Report

- `GET_DATE_RANGE_FINANCIAL_HOLDS_DATA` is Amazon's Deferred Transaction Report; Amazon states it is requested in Seller Central's Payments Reports Repository before the Reports API retrieves it; read in Amazon's documents, not yet seen on a live account (P-api-17).
- It is point-in-time and covers up to 10 years of data (P-api-17, P-api-35).
- It lists what is deferred when it is generated: "When a transaction is updated from deferred to released, it will no longer be included" (P-api-35).
- No report type matches Seller Central's Date Range Reports (P-api-17).

## Fee, storage, reimbursement and FBA report types

- Role Mappings for Types list Amazon Fulfillment or Pricing, either one, for `GET_FBA_STORAGE_FEE_CHARGES_DATA`, `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA`, `GET_FBA_REIMBURSEMENTS_DATA` and `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`; read in Amazon's documents, not yet seen on a live account (P-tool-26, P-api-18).
- Role Mappings for Types list Pricing or Amazon Fulfillment for the returns and removal report types too; read in Amazon's documents, not yet seen on a live account (P-api-18).
- The overage fee, customer shipment sales and ledger report types need Amazon Fulfillment (P-api-18, P-tool-26).
- The referral fee preview (`GET_REFERRAL_FEE_PREVIEW_REPORT`) and the settlement report need Finance and Accounting (P-api-18, P-sell-33).

## Tax report types

- The US sales tax report needs Tax Remittance (Restricted), and the EU VAT reports need Tax Invoicing (Restricted) (P-api-18).
- The US sales tax report is generated in Seller Central's Tax Document Library and then found with `getReports` (P-api-37).
- The VAT transaction report needs Tax Invoicing (Restricted); its `dataEndTime` rule and the window of India's On Demand GST MTR B2C report are read on Amazon's Tax Reports page (P-api-36).

## Other report types

- A report type other than settlement whose report was not downloaded in time can be generated again, and order reports are kept 30 days (P-api-30).
