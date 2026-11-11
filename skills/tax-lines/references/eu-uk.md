# EU and UK

## Deemed supplier

- In the EU, Amazon is deemed supplier for B2C goods in the EU sold by sellers established outside the EU, and for low-value imports under IOSS. (P-tax-19)
- In the UK, the marketplace is liable for VAT on low-value consignments and on overseas sellers' UK-stocked goods. (P-tax-19)
- Per order, Orders v2026-01-01 `getOrder` or `searchOrders` with `includedData=TAX` returns `taxCollections[]`, and `taxCalculationBreakdowns[].reportingScheme` marks UOSS or IOSS; that it returns on the roles sellers tick today, without a restricted role, is read in Amazon's documents, not yet seen on a live account. (P-tax-19)
- The value limits are read on the EC page "One Stop Shop" and GOV.UK "VAT and overseas goods sold to customers in the UK using online marketplaces". (P-tax-19)

## VAT on Amazon's fees

- Amazon EU S.à r.l. supplies EU and UK seller services from August 2024. (P-tax-13)
- Sellers established in some countries are invoiced by the local branch with local VAT; others are invoiced by the Luxembourg head office. (P-tax-13)
- Which establishments are invoiced with local VAT is read in News_Amazon's "Update to Amazon UK and EU agreements and VAT treatment". (P-tax-13)
- The tax on each estimated fee is `TaxAmount` in `getMyFeesEstimateForSKU`, `getMyFeesEstimateForASIN` and `getMyFeesEstimates`, and ads and deal events carry their own tax field. (P-sell-14)
- The tax actually charged on each fee is read from Data Kiosk `createQuery` on `analytics_economics_2024_03_15` (`taxAmount`); which role the Economics dataset needs, and whether Finances v0 EU/UK fee lines are net or gross of that VAT, are read in Amazon's documents, not yet seen on a live account. (P-tax-13, P-tax-14)
- Amazon Ads are invoiced separately from selling fees. (P-tax-13)
- VAT Services on Amazon ended in October 2024; `VatAmazonTechnologyFee`, `VatFiscalRepFee` and `VatPartnerFee` lines are a closed history. (P-tax-21)

## VAT Calculation Service

- VCS works in the stores Amazon's page "VAT Calculation Service" lists. (P-tax-16)
- VCS keeps VAT-inclusive prices in the price feed. (P-tax-16)
- Since June 2026 VCS calculates VAT per shipment by rate, not per unit. (P-tax-16)
- Sellers who invoice themselves upload within the limit stated on Amazon's page "VCS Best Practices". (P-tax-16)
- Amazon calculates no VAT on a shipment from a country where the seller's VAT number is missing; the seller computes it and uploads the invoice, and Amazon does not validate that invoice's `TotalAmount` and `TotalVATAmount` fields. (P-tax-15)

## Amazon VAT Transactions Report

- The AVTR (`GET_VAT_TRANSACTION_DATA`) covers sales, returns, refunds, cross-border inbound and FC transfers. (P-tax-17)
- It "ignores the `marketplaceId` parameter and returns data for all available stores". (P-tax-17)
- Its `dataEndTime` must lie some days before the request; the lag is read on Amazon's page "Tax Reports", the `GET_VAT_TRANSACTION_DATA` row. (P-tax-17)
- A re-pulled range can return changed rows, marked by `transaction_update_date`. (P-tax-17)

## VAT Invoice Data Report

- The VIDR exists only for VCS sellers who upload their own invoices. (P-tax-18)
- Its default and `all=true` windows and Amazon's recommended pull frequency are read on Amazon's page "Invoice Data Reports". (P-tax-18)
- Corrections arrive as `CorrectionReversal:` REFUND and `Correction::` SHIPMENT pairs with unchanged amounts. (P-tax-18)

## Pan-EU and own-goods moves

- Pan-European FBA needs a VAT number in every storage country. (P-tax-20)
- The UK left Pan-European FBA in January 2021. (P-tax-20)
- Amazon verifies EU, UK, NO and CH VAT registrations from 2025, and a failed check can restrict selling or FBA. (P-tax-20)
- A Pan-EU or EFN move of the seller's own stock across a border is, for VAT, a supply in the departure country and an acquisition in the arrival country, needing VAT numbers in both. (P-tax-47)
- The AVTR records "cross border inbound, and cross border fulfillment center transfers" with departure and arrival country and the seller's VAT number in each. (P-tax-47)
- The name `FC_TRANSFER` for these AVTR rows is Taxually's and Eurofiscalis'; the rows themselves are read in Amazon's documents, not yet seen on a live account. (P-tax-47)
- ViDA adds a transfer-of-own-goods scheme under Single VAT Registration, from 2028. (P-tax-47)

## DAC7 and UK platform reporting

- Under DAC7 and the UK platform rules, Amazon reports seller identity and transaction data to tax authorities and must give the seller a copy. (P-tax-22)
- A seller who does not supply TIN and registration data in time faces deactivation and withheld funds; the windows are read in News_Amazon's DAC7 collection notice. (P-tax-22)

## Roles

- The AVTR, `SC_VAT_TAX_REPORT` and both VIDRs need Tax Invoicing or Tax Remittance (Restricted), with a Restricted Data Token for PII report documents. (P-tax-10)
