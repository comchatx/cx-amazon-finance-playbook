---
name: tax-lines
description: "The tax inside an Amazon seller's money: sales tax, VAT and GST lines in settlements, Finances events and the Date Range report; tax Amazon collects as marketplace facilitator or deemed supplier (`MarketplaceFacilitatorTax`, `marketplace-withheld-tax`, OSS/IOSS); tax Amazon deducts (India TCS and TDS, Mexico IVA and ISR); VAT on Amazon's fees; the 1099-K, AVTR, VCS, VIDR, DAC7, Brazil NF-e and Japan qualified invoices; Pan-EU and EFN VAT numbers; import VAT; China's platform tax report, 9810 export VAT refund and offshore income. For questions on which tax line is the seller's and which is Amazon's, whether a tax is Amazon's to collect or the seller's to file, why a 1099-K or a China tax report differs from payouts, or where a tax document or report is read."
---

## Tax lines

- A tax line is buyer tax the seller keeps and owes, buyer tax Amazon withholds and remits, tax Amazon deducts from the seller, or tax on Amazon's fee. (P-tax-1)
- `MarketplaceFacilitatorTax-*` and `MarketplaceFacilitatorVAT-*` withheld lines offset the buyer-side tax on the same item, so that tax does not reach the payout (Finances v0; A2X: "results in a total of 0"). (P-tax-2)
- `Standard`-model tax is "paid to the seller and not remitted … by Amazon": in the payout, the seller's to remit. (P-tax-3)
- Who remits is stated per item in Orders `taxCollections[]`, the sales tax report, VCS and the AVTR; Orders returning it without a restricted role is read in Amazon's documents, not yet seen on a live account. (P-tax-4)
- An Economics fee total includes tax on the fee: `totalAmount = amount - promotionAmount + taxAmount`. (P-tax-14)
- A2X, Link My Books and Lingxing describe booking Amazon-collected tax excluded or as gross revenue plus a liability, fee VAT as cost or recoverable, profit VAT-inclusive or exclusive; each changes revenue and margin, not the payout. (P-tax-29)

## Documents

- The US 1099-K is "unadjusted gross sales": tax and shipping in, fees and refunds not deducted; its threshold is read on the IRS page "Form 1099-K FAQs: General information". (P-tax-7, P-tax-8)
- The US sales tax report, EU/UK VAT reports, India's MTRs and Brazil's invoice APIs need Tax Invoicing or Tax Remittance (Restricted), roles sellers do not tick today. (P-tax-9, P-tax-10)

## Beyond Amazon's collection

- Amazon does not collect Washington B&O, Ohio CAT or Texas franchise tax; the seller files each where its nexus test (physical presence, or a receipts, property or payroll threshold) is met. (P-tax-31)
- By STA 2025 No. 15 a platform reports income gross of VAT and of its fees; Amazon's quarterly China tax report, as China Daily, Zhonglun and AMZ123 relay it, follows this: not the payout. (P-tax-34, P-tax-35, P-tax-36)

## References

- references/lines.md: line kinds, columns, counting choices.
- references/reads.md: reads per role, fee invoices.
- references/us.md: facilitator tax, 1099-K, state taxes.
- references/eu-uk.md: deemed supplier, fee VAT, AVTR, Pan-EU.
- references/other-marketplaces.md: India, Mexico, Brazil, Japan, others.
- references/china.md: China tax report, exports.
- references/imports.md: importer of record, import VAT.
