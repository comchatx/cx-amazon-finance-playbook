---
name: tax-lines
description: "The tax inside an Amazon seller's money: sales tax, VAT and GST lines in settlements, Finances events and the Date Range report; tax Amazon collects as marketplace facilitator or deemed supplier (`MarketplaceFacilitatorTax`, `marketplace-withheld-tax`, OSS/IOSS); tax Amazon deducts (India TCS and TDS, Mexico IVA and ISR); VAT on Amazon's fees; the 1099-K, AVTR, VCS, VIDR, DAC7, Brazil NF-e and Japan qualified invoices; Pan-EU and EFN VAT numbers; import VAT; China's platform tax report, 9810 export VAT refund and offshore income. For questions on which tax line is the seller's and which is Amazon's, whether a tax is Amazon's to collect or the seller's to file, why a 1099-K or a China tax report differs from payouts, or where a tax document or report is read."
---

## Tax lines

- `MarketplaceFacilitatorTax-*` and `MarketplaceFacilitatorVAT-*` withheld lines offset the buyer-side tax on the same item, so that tax does not reach the payout. (P-tax-2)
- `Standard`-model tax is "paid to the seller and not remitted … by Amazon": the seller's to remit. (P-tax-3)
- Who remits is stated per item in Orders `taxCollections[]`, the sales tax report, VCS and the AVTR; Orders returning it without a restricted role is read in Amazon's documents, not yet seen on a live account. (P-tax-4)
- A2X, Link My Books and Lingxing describe collected tax and fee VAT booked either way (excluded or revenue plus liability; cost or recoverable): margin changes, the payout does not. (P-tax-29)

## Tax on Amazon's fees

- EU/UK sellers established in a country News_Amazon's "Update to Amazon UK and EU agreements and VAT treatment" lists are invoiced by Amazon's local branch with local VAT; others by its Luxembourg head office. (P-tax-13)
- Each fee's tax is its own field: `TaxAmount` in `getMyFeesEstimateForSKU`, Data Kiosk economics `taxAmount`, deal and ads events. (P-sell-14, P-tax-14)

## Documents

- The US 1099-K is "unadjusted gross sales": tax and shipping in, fees and refunds not deducted; US persons only; threshold on the IRS page "Form 1099-K FAQs: General information". (P-tax-7, P-tax-8)
- The US sales tax report "cannot be requested or scheduled": generated in the Tax Document Library, it needs Tax Remittance (Restricted). (P-tax-9)
- EU/UK VAT reports, India's MTRs and Brazil's invoice APIs need Tax Invoicing or Tax Remittance (Restricted), roles sellers do not tick today. (P-tax-10)

## Beyond Amazon's collection

- The seller, not Amazon, files Washington B&O, Ohio CAT and Texas franchise tax; each has its own nexus test. (P-tax-31)
- Amazon's quarterly China tax report, as China Daily, Zhonglun and AMZ123 relay it, follows STA 2025 No. 15: income gross of VAT and of fees, not the payout. (P-tax-34, P-tax-35, P-tax-36)

## References

- references/lines.md: line kinds, columns, counting choices.
- references/reads.md: reads per role, Tax Document Library, fee invoices.
- references/us.md: facilitator tax, 1099-K, state taxes, stock location.
- references/eu-uk.md: deemed supplier, fee VAT, VCS, AVTR, Pan-EU.
- references/other-marketplaces.md: India, Mexico, Brazil, Japan, others.
- references/china.md: China tax report, exports.
- references/imports.md: importer of record, import VAT.
