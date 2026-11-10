# United States

## Marketplace facilitator sales tax

- Amazon collects US sales tax as marketplace facilitator in every US jurisdiction with a statewide sales tax, plus DC and Puerto Rico. (P-tax-6)
- Amazon's page names exceptions: Colorado home-rule cities, Alaska non-adopting localities, Alabama rentals, and New York non-tangible goods. (P-tax-6)
- The current list of jurisdictions is read on Amazon's page "Marketplace Tax Collection"; eComEngine's list is stale against it. (P-tax-6)
- Per item, collection is read from Orders v2026-01-01 `getOrder` or `searchOrders` with `includedData=TAX` (`taxCollections[]`); that it returns on the roles sellers tick today, without a restricted role, is read in Amazon's documents, not yet seen on a live account. (P-tax-6)
- Amazon's facilitator collection covers sales tax and named regulatory fees only. (P-tax-30)

## Form 1099-K

- The 1099-K reports "unadjusted gross sales", which include tax and shipping and are not reduced by fees or refunds. (P-tax-7)
- It is issued to US persons only, in the Tax Document Library; its issue date is stated on Amazon's page "IRS Form 1099-K FAQs". (P-tax-7)
- A2X holds that book gross "shouldn't match" the 1099-K. (P-tax-7)
- The 1099-K threshold changed by law within 2024–2025: Notice 2024-85's stepped path was replaced retroactively by P.L. 119-21. (P-tax-8)
- The threshold for a tax year is read on the IRS page "Form 1099-K FAQs: General information"; research/areas/tax-and-invoices.md, P-tax-8, holds the value as read. (P-tax-8)

## The US sales tax report

- `GET_FLAT_FILE_SALES_TAX_DATA` "cannot be requested or scheduled"; the seller generates it in the Tax Document Library, `getReports` then finds it, and it needs Tax Remittance (Restricted). (P-tax-9)
- It states who remits each line in `Tax_Collection_Model` and `Tax_Collection_Responsible_Party`. (P-tax-4)

## State taxes Amazon does not collect

- Washington counts "a stock of inventory … held by a marketplace facilitator" as physical presence, from which the seller must "register to report B&O tax" with no sales threshold, "even if sales … are only made through marketplace facilitator(s)". (P-tax-30)
- Avalara and Elliott Davis report that California's Office of Tax Appeals has held FBA inventory to create franchise and income-tax nexus. (P-tax-30)
- Other states differ; each state's own page for the year concerned is read at run time, Washington's being WA DOR "Marketplace sellers". (P-tax-30)
- State taxes measured on gross receipts or margin are filed by the seller, not collected by Amazon: Washington B&O, Ohio CAT and Texas franchise tax. (P-tax-31)
- Each has its own nexus test: physical presence, or a receipts, property or payroll threshold. (P-tax-31)
- Their thresholds and rates are read on each state's page for the year: WA DOR "Marketplace sellers", Texas Comptroller "Franchise Tax", and the Ohio Department of Taxation's CAT pages on tax.ohio.gov, which refused every direct read during the research. (P-tax-31)

## Where FBA stock sat

- Where FBA stock sat is read from the Inventory Ledger: `GET_LEDGER_DETAIL_VIEW_DATA` rows carry `Fulfillment Center` and `Country`, and the summary aggregates by `FC`. (P-tax-32)
- The ledger is on the Amazon Fulfillment role; how far back it reaches is read on Amazon's page "Fulfillment by Amazon (FBA) Reports", the `GET_LEDGER_DETAIL_VIEW_DATA` row. (P-tax-32)
- Amazon publishes no FC-to-state map; TaxJar describes FC codes as named for the nearest airport. (P-tax-32)
