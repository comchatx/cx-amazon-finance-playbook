# Selling fees, the subscription and the fees on a refund

## Referral fee

- The referral fee is the greater of the category percentage of the total sales price and the per-item minimum. (P-sell-1)
- The total sales price includes the item price, delivery and gift-wrap charges. (P-sell-1)
- Per-item minimums differ by marketplace; media and some grocery categories carry none. (P-sell-4)
- Amazon.com.au states "There is no minimum or maximum referral fee." (P-sell-4)
- The rates and minimums for the seller's marketplace and category are on Amazon's pricing page, *How much does it cost to sell on Amazon?*, or its counterpart for the store. (P-sell-4, P-sell-39)
- A listing's referral fee at a given price is returned by `getMyFeesEstimateForSKU` / `getMyFeesEstimates`. (P-sell-4, P-sell-39)
- The tax treatment of the referral base differs by marketplace: the US excludes taxes Amazon calculates, JP includes taxes the buyer paid, and MX includes IVA, in the minimum too. (P-sell-2)
- The UK and EU pricing pages state the base both ways, so there the base is read from a charged order: the posted `Commission` against the order's principal and tax in `listTransactions`. (P-sell-2)
- Price-dependent rates come in two kinds: a whole-price threshold changes the rate on the whole price when the price crosses the line, and a portion-of-price tier charges the second rate only on the part above the line. (P-sell-3)
- A price change near a threshold changes the fee differently under each kind. (P-sell-3)
- The referral fee category is Amazon's assignment and "may not be the same as the category that appears to customers". (P-sell-5)
- A seller who believes a wrong fee category was applied can request a review per charge in Seller Central; "only one claim per charge is allowed". (P-sell-5)
- No Amazon page read states whether the referral fee is computed before or after a seller-funded coupon or promotion, and practitioners (A2X, SellerView.ai) disagree. (P-sell-6)
- The order's own posted `Commission` against its principal and promotion lines is the record of the base Amazon used. (P-sell-6)
- Amazon Business orders pay the normal referral schedule. (P-sell-21)
- Since 2025-10-01 (US), high-value business orders that carry a business discount can qualify for a reduced referral rate. (P-sell-21)
- The qualifying discount and the reduced rates are in Amazon's News post on the Amazon Business bulk order referral fee discount and on *Business discount insights* (US); the tier table itself sits on a help page that was not readable. (P-sell-21)
- Amazon Handmade's referral fee has its own rate and minimum, and the Professional subscription is waived after a period; the rate, minimum and waiver are on Amazon's Handmade page (US). (P-sell-22)
- Subscribe & Save adds no selling fee; its seller-funded discount is a price reduction, and coupon fees apply to S&S coupons. (P-sell-22)

## Refund administration fee

- On a refund Amazon credits back the referral fee minus a refund administration fee. (P-sell-7)
- The refund administration fee is the lesser of a fixed amount and a percentage of the referral fee; both differ by marketplace. (P-sell-7)
- The fixed amount and the percentage are on *Selling on Amazon fee schedule* (US) or the pricing page for the seller's marketplace; the amount retained on a refund is in `listTransactions`. (P-sell-7)
- Practitioners (A2X, AMALYTIX, SellingPilot) read a refund as two fee lines: the referral fee credited back (`Commission`) and the retained administration fee (`RefundCommission`, "Adjustment Item Fees Refund Commission"); Amazon names neither, and these labels are reported by practitioners, not yet seen on a live account. (P-sell-8)
- Practitioners report the same pair on A-to-z Guarantee and chargeback debits. (P-sell-8)
- Amazon's v0 model states that `ItemFeeAdjustmentList` is "only returned for refunds, guarantee claims, and chargeback events". (P-sell-8)
- A-to-z Guarantee claims and chargebacks are debits recorded as `ShipmentEvent`s in `GuaranteeClaimEventList` and `ChargebackEventList`, with their fee adjustments in the item fee adjustment list. (P-sell-38)
- SAFE-T reimbursements are a separate inbound event. (P-sell-38)

## Closing and per-item fees

- `FixedClosingFee` is the Individual-plan per-item fee ("Per-item Selling Fees, also know as Fixed Closing Fee"). (P-sell-9)
- `VariableClosingFee` / `CLOSING_FEES` is the media closing fee ("also know as Variable Closing Fees"), even where Amazon now charges it as a flat amount per media item. (P-sell-9)
- India's "closing fee" is a broad fixed fee by price band and fulfilment channel (FBA, Easy Ship, Self Ship, Seller Flex), not a media fee. (P-sell-10)
- India's closing fee changed on 2026-09-07; its bands per channel are on *sell.amazon.in fees and pricing*, and the fee charged on an order is in `listTransactions`. (P-sell-10)

## Account fees

- The Professional subscription is a monthly account fee, not a per-unit fee, and can be prorated on a plan switch. (P-sell-11)
- Subscription corrections post as `ChargeRefundEvent` with a `ReasonCode` such as `SubscriptionFeeCorrection`. (P-sell-11)
- Whether the subscription is charged in a month with no active listings is stated only for AU ("when you have active listings"). (P-sell-11)
- The high-volume listing fee is a monthly per-SKU fee above a SKU threshold. (P-sell-12)
- It counts all SKUs "irrespective of creation date or sales history", at the month's highest count over the counting days Amazon states. (P-sell-12)
- The per-SKU rate, the SKU threshold and the counting days are on *Selling on Amazon fee schedule* (US) or the Canadian pricing page; the fee charged is in `listTransactions`, among transactions without an order. (P-sell-12)

## Digital services fee

- The digital services fee is a percentage of Amazon's Selling on Amazon fees, and in stated cases FBA fees, not of sales. (P-sell-13)
- It has been a separate line since 2024-10-01. (P-sell-13)
- From 2026-03-20 it is based on the DST rate of the country of sale, and it depends on the seller's country of establishment. (P-sell-13)
- The rate by country of establishment and store is in News_Amazon *2026 digital services fee changes*. (P-sell-13)
- The fee charged is in `listTransactions` per order, and in Data Kiosk `analytics_economics_2024_03_15` per product as `DIGITAL_SERVICES_FEE_SOA` and `DIGITAL_SERVICES_FEE_FBA`. (P-sell-13)
- A CESifo working paper (Langenmayr and Muddasani, read as a snippet) reports that Amazon raised fees by about each country's digital services tax. (P-tool-24)

## Tax on Amazon's fees

- Amazon's fees carry their own tax, by marketplace. (P-sell-14)
- EU-established sellers in the countries listed in News_Amazon *Update to Amazon UK and EU agreements and VAT treatment* are invoiced by the AEU branch in their country, with local VAT on the fees. (P-sell-14)
- India adds GST to its fees; AE, AU and JP state their own treatment, and JP's page is internally inconsistent. (P-sell-14)
- The tax on each fee is a separate field: `TaxAmount` in `getMyFeesEstimateForSKU` / `getMyFeesEstimateForASIN` / `getMyFeesEstimates`, `taxAmount` in Data Kiosk `analytics_economics_2024_03_15`, and its own amount in the deal and ads events. (P-sell-14)
- The stated treatment is on the pricing page for the seller's marketplace and, for EU-established sellers, in News_Amazon *Update to Amazon UK and EU agreements and VAT treatment*. (P-sell-14)
- The Invoices API v2026-06-25 is "Vendors only", and no SP-API operation returns Amazon's fee invoices to a seller. (P-sell-32)

## Currency conversion and shipping labels

- The Amazon Currency Converter for Sellers (ACCS) charges a conversion fee tiered by the seller's cross-currency net proceeds over the trailing twelve months, with flat rates for some currencies and for JPY. (P-sell-37)
- The ACCS fee is not documented as a separate statement line; its tiers and flat rates are on *Amazon Currency Converter for Sellers*. (P-sell-37)
- Buy Shipping label costs post as `PostageBilling`, and label refunds as `PostageRefund`. (P-sell-24)
- Carrier-audited label adjustments pass through later, because the label price "is an estimate". (P-sell-24)

## Fee changes

- Amazon announces selling-fee changes in dated letters and posts per marketplace, usually effective mid-January in the US and on other dates elsewhere. (P-sell-35)
- A fee on a transaction is the rate in force on its date. (P-sell-35)
- The effective date and the changes for the seller's marketplace are in that year's letter or post (US: *Update to US Referral and FBA fees for 2027*). (P-sell-35)
- Data Kiosk `economicsPreview` returns a product's fees across a coming change date. (P-sell-35)
- Amazon's 2027 US letter (2026-11-05) states FBA, storage and low-inventory changes, names "Buy X, Get Y" promotions, MCF and AWD among the summary's further updates, and does not mention referral rates. (P-sell-36)
- sell.amazon.com/pricing shows 3D Printers as a portion-of-price tier without a start date. (P-sell-36)
- Practitioner reports of a Renewed promotional rate, a "Buy X, Get Y" fee and monthly promotion billing are unconfirmed on the Amazon pages read. (P-sell-36)
- Category rates, minimums, plan prices and program rates are read from Amazon's pages at the date in question. (P-sell-39)
- The Seller Central help pages behind the fee rules are not reachable by plain GET; sell.amazon.* pages and News_Amazon posts are. (P-sell-39)
