# Other marketplaces

## India

- Amazon deducts GST TCS and section 194-O TDS from the seller's proceeds. (P-tax-23)
- The Finances v0 model names the TCS lines `TCS-CGST`, `TCS-SGST`, `TCS-IGST` and `TCS-UTGST`; how they show in the seller's Finances events and V2 settlement is read in Amazon's model, not yet seen on a live account. (P-tax-23)
- The seller claims TCS through the GST portal ledger. (P-tax-23)
- The Finances v0 model names `TDSReimbursementEvent` for TDS reimbursements; this is read in Amazon's model, not yet seen on a live account. (P-tax-23)
- On Amazon Fulfillment, `GET_GST_STR_ADHOC` is India's tax read; India's MTRs need Tax Invoicing or Tax Remittance (Restricted). (P-tax-10, P-tax-11)

## Mexico

- Amazon withholds IVA and ISR from the seller's sales. (P-tax-24)
- The share withheld depends on whether a valid RFC is on the account, and the rates changed at the start of 2026. (P-tax-24)
- No operation or page gives the rates; research/areas/tax-and-invoices.md, P-tax-24, holds the value as read. (P-tax-24)
- The retention CFDIs sit in the Tax Document Library. (P-tax-24)

## Brazil

- In Brazil the seller issues the NF-e. (P-tax-25)
- Amazon's Invoices API v2024-06-19 reads only Brazilian FBA invoices; Shipment Invoicing v0 submits FBA Onsite invoices. (P-tax-25)
- An invoice cancelled at Sefaz after Amazon's own cancel window is not reflected; the window is read on Amazon's page "Invoices API FAQ". (P-tax-25)

## Japan

- Amazon issues qualified invoices to buyers on the seller's behalf only once the seller's T-number is in Tax Settings. (P-tax-26)
- Japan's platform taxation, from April 2025, covers consumer digital services. (P-tax-26)
- An enacted extension covers foreign businesses' goods sold in Japan and low-value mail-order sales from abroad, from April 2028, through platforms the NTA designates. (P-tax-26)
- No Amazon statement on designation was found; the value limit and the designation are read on the NTA page "国境を越えた電子商取引に係る消費税の課税関係について". (P-tax-26)

## Singapore, Australia and Canada

- Singapore law makes the marketplace "charge and account for GST" on low-value goods; the limit is read on the IRAS page on GST on imports of low-value goods. (P-tax-27)
- Amazon.com's page "Tax on Low Value Imported Goods (LVIG)" says the relevant Amazon entity collects tax on Amazon.com orders delivered to Australia, Singapore and other listed countries. (P-tax-27)
- That page covers Amazon.com cross-border orders; for Australia only a snippet of the ATO's page was read. (P-tax-27)
- In Canada Amazon collects GST/HST for sellers who have not registered a number with it, and some provincial taxes. (P-tax-27)
- Per order, collection is read from Orders v2026-01-01 `getOrder` or `searchOrders` with `includedData=TAX` (`taxCollections[]`); that it returns on the roles sellers tick today, without a restricted role, is read in Amazon's documents, not yet seen on a live account. (P-tax-27)
