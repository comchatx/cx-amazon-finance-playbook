# Where each fee is recorded, and what estimates hold

## Finances v0 and v2024-06-19

- v0 places selling fees in `ShipmentEvent` item fee lists. (P-sell-25)
- v0 keeps account and program fees in their own lists: `ServiceFeeEventList`, `CouponPaymentEventList`, `SellerDealPaymentEventList`, `ProductAdsPaymentEventList`, `ImagingServicesFeeEventList`, `ValueAddedServiceChargeEventList`, and `ChargeRefundEventList` for corrections. (P-sell-25)
- v0 `SellerReviewEnrollmentPaymentEventList` serves the retired Early Reviewer Program. (P-sell-25)
- In v0 `ChargeType` is an enumerated list, while `FeeType` is a free string pointing to the fee schedule. (P-sell-26)
- In v2024-06-19 `breakdownType` is "an open-ended string; Amazon does not publish a closed list". (P-sell-26)
- The settlement `amount-description` values are published nowhere, and fee labels are read from the account. (P-sell-26)
- Fee labels change over time without a version change. (P-sell-27)
- The model's sandbox `breakdownType` strings ("Product Charges", "Principle", "FBA fees") differ from the camel-case strings vendors (Trellis, Openbridge) report from production (`ProductCharges`, `AmazonFees`, `Commission`), so example payloads are not a label source. (P-sell-28)
- Amazon publishes no closed list of the names fulfilment and storage charges carry: `breakdownType`, v0 `FeeType`, Product Fees `FeeType` and settlement `amount-description` are open strings, and new names appear. (P-ful-15)
- AMALYTIX reports that some surcharges (storage utilization, low-inventory, fuel) may have no type of their own and sit inside another line. (P-ful-15)
- In the v0 model, `ServiceFeeEvent` carries `AmazonOrderId`, `SellerSKU`, `FnSKU` and `ASIN`, and `CapacityReservationBillingEvent` carries none of them; whether storage, placement, capacity or overage charges come back on `listFinancialEventsByOrderId` or order-level transactions is read in Amazon's model, not yet seen on a live account. (P-ful-17)

## Data Kiosk economics

- Data Kiosk economics' schema itemises selling fees per product under Amazon's own type names: `REFERRAL_FEES`, `CLOSING_FEES`, `PER_ITEM_SELLING_FEES`, `DIGITAL_SERVICES_FEE_SOA` / `_FBA` and `SPONSORED_PRODUCTS_CHARGES`; read in Amazon's model, not yet seen on a live account. (P-sell-31)
- Economics splits a date range at an Amazon fee-change date, and its schema can lag Amazon's release notes on new fee types. (P-sell-31)
- Economics `fees[]` holds charged fees per product and date with the properties, such as size tier, that set them, and keeps query results 30 days. (P-ful-18)
- `economicsPreview` previews the named fulfilment, storage, aged, low-inventory, placement and Pan-EU oversize fees, among others, up to 120 days ahead. (P-ful-18)
- The role economics needs conflicts between Amazon's pages: Role Mappings and the Data Kiosk API page give Brand Analytics, while the changelog *Correction: Data Kiosk role requirements* says "The Economics dataset requires the Selling Partner Insights role"; read in Amazon's documents, not yet seen on a live account. (P-ful-18)

## Estimates

- A fee estimate (Product Fees, Fee Preview, Referral Fee Preview, `economicsPreview`) is per unit at one price. (P-sell-29)
- Product Fees takes no coupon, promotion, business or establishment input. (P-sell-29)
- Program fees, the subscription, the high-volume listing fee, the refund administration fee and advertising cannot be in a fee estimate. (P-sell-29)
- Product Fees estimates "are not guaranteed"; an ASIN estimate uses catalog size, while a SKU estimate uses measured size once the item is at Amazon. (P-sell-30, P-ful-19)
- Product Fees estimates per-sale fees (referral, closing, FBA fulfilment) for a price, and does not estimate storage, placement, removal or returns fees. (P-ful-19)
- Amazon states the Revenue Calculator includes referral, FBA fulfilment, inbound placement, storage and variable closing fees, and excludes the subscription, per-item, removal, returns processing, refund administration and high-volume listing fees. (P-sell-40)
- The Revenue Calculator's public page loads without sign-in. (P-sell-40)

## Roles

- The finance reads take Finance and Accounting: `listTransactions`, `listSummary`, v0 events, settlement V2, `GET_REFERRAL_FEE_PREVIEW_REPORT`, and Transfers `listPayouts` / `listExpectedPayouts`. (P-sell-33)
- Product Fees and `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` accept Pricing, and the Promotions API takes Pricing or Product Listing. (P-sell-33)
- `GET_COUPON_PERFORMANCE_REPORT` takes Brand Analytics, and `GET_PROMOTION_PERFORMANCE_REPORT` takes Brand Analytics or Selling Partner Insights. (P-sell-33)
- By Role Mappings, the storage, aged, fee-preview, inbound-performance, removal, returns and reimbursement reports open with Pricing (or Amazon Fulfillment); read in Amazon's documents, not yet seen on a live account. (P-ful-20)
- The planning and overage reports, Fulfillment Inbound and MCF need Amazon Fulfillment, and AWD needs the AWD role. (P-ful-20)

## Dated removals

- The settlement V1 report, in both its flat and XML forms, is removed on 2026-11-11. (P-sell-34)
- Finances v0 `listFinancialEvents`, `…ByGroupId` and `…ByOrderId` are removed on 2027-08-27, deprecated since 2025-07-21. (P-sell-34)

## Calls

- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
- ../money-reads/SKILL.md: each finance read with its window, lag and pitfalls.
