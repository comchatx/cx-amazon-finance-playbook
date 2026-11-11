# Tax lines in the money data

## The four kinds

- Every tax amount in a money line is one of four kinds: buyer tax the seller keeps and owes, buyer tax Amazon withholds and remits, tax Amazon deducts from the seller, or tax on Amazon's own fee. Each is named by its own line. (P-tax-1)
- In the Finances v0 model, tax the seller collects is a `ChargeComponent`, tax Amazon withholds a `TaxWithheldComponent`, and tax Amazon deducts a `TaxWithholdingEvent` or India's `TCS-*` charges. (P-tax-1)
- What a `TaxWithholdingEvent` holds is read in Amazon's model, not yet seen on a live account. (P-tax-1)
- Tax on Amazon's own fee is the Data Kiosk economics `taxAmount`. (P-tax-1, P-tax-14)
- Lingxing separates 销售税 (sales tax kept by the seller) from 市场税 (marketplace tax withheld). (P-tax-1)

## Facilitator tax

- `MarketplaceFacilitatorTax-*` (US) and `MarketplaceFacilitatorVAT-*` (EU/UK) withheld lines offset the buyer-side tax on the same item, so that tax does not reach the payout; how it is booked is a choice (see Counting choices). (P-tax-2)
- The Finances v0 model describes the `MarketplaceFacilitator` model as "Tax is withheld and remitted … by Amazon on behalf of the seller". (P-tax-2)
- A2X describes the withheld lines as offsetting the tax charged to the customer so that it "results in a total of 0". (P-tax-2)
- Amazon, as quoted by ChannelX, told UK sellers: "You will not receive the UK VAT amount in your disbursements". (P-tax-2)

## Tax the seller keeps

- Tax with collection model `Standard` is "paid to the seller and not remitted … by Amazon": it sits in the seller's payout and remains the seller's to remit. (P-tax-3)

## Who remits

- Who remits is stated per item in Orders v2026-01-01 `taxCollections[]` (`model`, `responsibleParty`), in the US sales tax report's `Tax_Collection_Model` and `Tax_Collection_Responsible_Party`, and in the VCS and AVTR `tax_collection_responsibility`; that Orders returns `taxCollections[]` on the roles sellers tick today, without a restricted role, is read in Amazon's documents, not yet seen on a live account. (P-tax-4)
- Amazon, as relayed by ChannelX, tells sellers not to report VAT where the AVTR reads MARKETPLACE. (P-tax-4)

## Date Range and Deferred Transaction columns

- The Date Range transaction view and the Deferred Transaction Report carry `product-sales-tax`, `shipping-credits-tax`, `gift-wrap-credits-tax`, `tax-on-regulatory-fee`, `promotional-rebate-tax`, `marketplace-withheld-tax` and `tax-collection-model`. (P-tax-5)
- Their "Product sales" column excludes those tax columns. (P-tax-5)

## Tax on Amazon's fees

- Data Kiosk economics fee amounts carry `taxAmount`, and `totalAmount = amount - promotionAmount + taxAmount`, so a fee total there includes tax on the fee. (P-tax-14)
- In the EU and UK the VAT on a fee depends on where the seller is established, and Ads are invoiced separately; references/eu-uk.md holds the rule. (P-tax-13)
- VAT Services on Amazon ended in October 2024, so its fee lines `VatAmazonTechnologyFee`, `VatFiscalRepFee` and `VatPartnerFee` belong to older periods only; the names are Lingxing's mapping. (P-tax-21)

## Description strings

- Tax-description strings in settlements have no published Amazon dictionary; the `listTransactions` `breakdownType` is open. (P-tax-28)
- The practitioner mappings of A2X and Lingxing are a guide; the strings in the seller's own file decide. (P-tax-28)

## Counting choices

- A2X, Link My Books and Lingxing describe Amazon-collected tax booked either excluded from revenue or as gross revenue with an offsetting liability. (P-tax-29)
- A2X, Link My Books and Lingxing describe VAT on Amazon's fees booked either as a cost or as recoverable. (P-tax-29)
- A2X, Link My Books and Lingxing describe profit shown either VAT-inclusive or VAT-exclusive; Lingxing's pricing convention is one source for it. (P-tax-29)
- By the same practitioners, each of these conventions changes the revenue line and the margin, not the payout. (P-tax-29)
