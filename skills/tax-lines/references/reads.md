# Where tax is read

## On the roles sellers tick today

- On Finance and Accounting, tax is read from the Finances v0 charge and withholding lists and the Flat File V2 settlement lines. (P-tax-11)
- The Deferred Transaction Report is also a Finance and Accounting face for tax; whether `getReports` finds it once the seller has requested it in Seller Central is read in Amazon's documents, not yet seen on a live account. (P-tax-11)

## Data Kiosk economics

- Data Kiosk economics `taxAmount` is a further tax face; Role Mappings name Brand Analytics for it and Amazon's correction names Selling Partner Insights, read in Amazon's documents, not yet seen on a live account. (P-tax-11)

## On Amazon Fulfillment

- On Amazon Fulfillment, tax is read from India's `GET_GST_STR_ADHOC` and the `TAX_INVOICE_*` notifications. (P-tax-11)
- Where FBA stock sat, by fulfilment center and country, is read from the Inventory Ledger on Amazon Fulfillment. (P-tax-32)

## Restricted roles

- Every EU/UK VAT report (`GET_VAT_TRANSACTION_DATA`, `SC_VAT_TAX_REPORT`, both VIDRs), India's MTRs, the Brazil Invoices and Shipment Invoicing APIs and Orders `taxRegistrations[]` need Tax Invoicing or Tax Remittance (Restricted). (P-tax-10)
- Report documents that carry PII also need a Restricted Data Token. (P-tax-10)
- None of these roles is on the roles sellers tick today. (P-tax-10)

## The Tax Document Library

- `GET_FLAT_FILE_SALES_TAX_DATA` "cannot be requested or scheduled"; the seller generates it in Seller Central's Tax Document Library, and `getReports` then finds it. (P-tax-9)
- That report needs Tax Remittance (Restricted). (P-tax-9)
- The US 1099-K is issued in the Tax Document Library. (P-tax-7)
- Mexico's retention CFDIs sit in the Tax Document Library. (P-tax-24)

## Amazon's invoices for its fees

- The Invoices API v2026-06-25 is "Vendors only". (P-tax-12)
- No SP-API operation found returns the invoices Amazon issues to sellers for selling, FBA or other fees; those sit in Seller Central. (P-tax-12)
- The tax on each estimated fee is `TaxAmount` in `getMyFeesEstimateForSKU`, `getMyFeesEstimateForASIN` and `getMyFeesEstimates`; Product Fees accept Pricing. (P-sell-14, P-sell-33)
- Whether VAT was charged on each fee is read from Data Kiosk `createQuery` on `analytics_economics_2024_03_15` (`taxAmount`); which role the Economics dataset needs, and whether Finances v0 EU/UK fee lines are net or gross of that VAT, are read in Amazon's documents, not yet seen on a live account. (P-tax-13)

## How a read is made

- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
- Each read's role, window and lag: ../money-reads/SKILL.md.
