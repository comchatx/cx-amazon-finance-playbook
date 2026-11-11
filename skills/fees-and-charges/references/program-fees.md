# Program, promotion and account-level charges

## Coupons and deals

- Coupon fees are separate from the coupon budget that funds the customer discount. (P-sell-15)
- Since 2025-06-02 (US, UK) coupon fees are an upfront fee per coupon plus a percentage of coupon sales. (P-sell-15)
- Coupons created from 2025-11-05 carry a capped variable fee in the UK and CA, by Amazon's posts, and in the US by Amazon's 2026 summary page as read on 2026-10-14, which no public Amazon page re-read since carries. (P-sell-15)
- Which coupon fee regime applies follows the coupon's creation date. (P-sell-15)
- The regime for the seller's marketplace is in Amazon's News posts: *Amazon is making it easier to try using deals and coupons…* (US), *Reduced voucher fees starting November 5, 2025* (UK) and *2026 Updates to Canada referral and FBA fees* (CA). (P-sell-15)
- Deal fees since 2025-06-02 (US, UK, non-peak) are a per-day upfront fee plus a capped percentage of deal sales. (P-sell-16)
- The daily deal fee is charged "even if your Deal does not produce any sales". (P-sell-16)
- Peak events carry their own announced fee per event, stated in that event's own post. (P-sell-16)
- A promotion's fee rates are locked at creation and returned by `getPromotion` in `feeSnapshot.previewedFeeRates`: `upfrontFee` with a frequency of `ONE_TIME` or `DAILY`, `variableFee.salesPercentage` and `variableFee.feeCapAmount`; this is read in Amazon's model, not yet seen on a live account. (P-sell-15, P-sell-16, P-sell-17)
- An empty `feeSnapshot` means that promotion type or marketplace records no fee. (P-sell-17)
- The Promotions API takes the Pricing or the Product Listing role. (P-sell-17)
- Practitioners (AMALYTIX; a seller thread with a staff reply) report coupon and deal lines moving to participation and performance-based names such as `CouponParticipationFee`, `DealPerformanceFee` and `VineFee`, and the model's `RunLightningDealFee` not seen in a year; these names are reported by practitioners, not yet seen on a live account. (P-sell-27)

## Vine, Transparency and brand programs

- Vine is charged per parent product by enrolled units. (P-sell-18)
- Vine is charged only after a first Vine review is published, and not if no review comes within the period Amazon states. (P-sell-18)
- Amazon's two Vine pages differ on how long after the first review the charge falls. (P-sell-18)
- The Vine tiers and charging terms are on *Amazon Vine*, and the charge itself is in `listTransactions`, among transactions without an order. (P-sell-18)
- Brand Registry and Manage Your Experiments carry no fee. (P-sell-19)
- Transparency has no enrolment cost but a per-code charge by annual volume, with the rates by volume and geography on *Amazon Transparency*. (P-sell-19)
- The Brand Referral Bonus is a credit applied against referral fees on later sales, after a wait; the rate and the wait are on *Brand Referral Bonus*. (P-sell-20)
- New Seller Incentives give automatic referral-fee waivers and program credits; the US amounts are on Amazon's selling home page and pricing page. (P-sell-20)
- Amazon does not document the line on which Brand Referral Bonus and New Seller Incentive credits post. (P-sell-20)

## Advertising

- Advertising reaches the seller's finances only when it is deducted from the selling balance, which is the default. (P-sell-23)
- A balance-deducted ad charge posts as an invoice-level `ProductAdsPaymentEvent` (`charge` or `refund`, `invoiceId`, base plus tax) or as the settlement "Cost of Advertising" line, never per ASIN. (P-sell-23)
- Ads paid by card or invoice do not appear in the finances. (P-sell-23)
- Data Kiosk economics names a per-product `SPONSORED_PRODUCTS_CHARGES` fee type, read in Amazon's model, not yet seen on a live account; the finance events carry ad charges only per invoice. (P-sell-31, P-sell-23)

## EPR Pay on Behalf

- A seller who sells EPR-subject products in a country where Amazon offers Pay on Behalf, without a valid EPR registration number for that category, is enrolled automatically. (P-sell-42)
- Amazon reports to the PROs, pays the eco-contributions for each reporting period, and debits them plus a service fee from the selling account. (P-sell-42)
- Eco-contributions are computed per category from sales volume or weight at the PRO's rates. (P-sell-42)
- By Amazon's notices, Pay on Behalf covers France, UK packaging for sellers not established in the UK, Spain and Italy. (P-sell-43)
- For UK packaging, eco-contributions run from 2024-04-01 and an annual per-category service fee from 2025-04-01. (P-sell-43)
- Italy's automatic enrolment runs from 2024-11-15. (P-sell-43)
- Amazon's notice for Germany states listing suspension for packaging and electrical equipment without a valid registration number (LUCID for packaging), not payment on behalf. (P-sell-43)
- Since 2025-08-27 one Pay on Behalf policy covers the UK, Spain and France. (P-sell-44)
- Under that policy Amazon "may hold EPR eco-contribution and service fees in reserve" and "may charge additional EPR eco-contribution and service fees at times that may differ from the applicable reporting cycle, including additional charges due to regulatory recalculations". (P-sell-44)
- From 2025-11 some sellers' FR and ES service runs as an account-level reserve (some UK sellers' earlier), which charges nothing extra but lowers the withdrawable balance. (P-sell-44)
- The amount held is read in Amazon's documents to sit in the reserve rows of `listSummary` and of `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`, not yet seen on a live account; whether `listSummary` shows it and whether EPR has its own reserve line are open. (P-sell-44)
- An EPR charge is an account-level debit for a past reporting period, not a line on the order whose sale caused it, and no fee estimate or preview carries it. (P-sell-45)
- The EPR service fee is annual per category. (P-sell-45)
- No operation or page gives the reporting cycle by category and PRO, and Amazon points to the Seller Central dashboard; research/areas/selling-fees.md, P-sell-45, holds the value as read. (P-sell-45)
- Amazon names no EPR line in any finance face; practitioners (AMALYTIX, My Real Profit) see `EPRChargebackServiceFee` and `EPRChargebackEcoFee` in settlements since April 2026, names reported by practitioners, not yet seen on a live account. (P-sell-46)
- `GET_EPR_MONTHLY_REPORTS`, `GET_EPR_QUARTERLY_REPORTS` and `GET_EPR_ANNUAL_REPORTS` are request-only CSV reports under the Product Listing role. (P-sell-47)
- The EPR reports carry per-ASIN units, EPR category and subcategories, registration number, ship-to country, item and package weights and packaging material weights, and no fee amount. (P-sell-47)

## Amazon Haul, the FBA-from-origin value and FFO

- Amazon Haul is a separate ultra-low-price shopping experience with its own listings (`is_value_stores_item` true, offer `audience` `BZR`). (P-sell-48)
- Haul launched in the US in 2024-11 and in the UK on 2025-05-06; by 2025-11 it served 25 locations, as Amazon Bazaar in MX, SA and AE and through a Bazaar app in 14 more, and Amazon removed its "beta" label. (P-sell-48)
- Haul money is marked apart in Amazon's model: `listTransactions` `BusinessContext.storeName` `AMAZON_HAUL` (from 2025-06-25; the context "only appears for program-specific transactions"), Sales `getOrderMetrics` with `amazonProgram=AmazonHaul`, and Orders v2026-01-01 `Order.programs` `AMAZON_HAUL` / `AMAZON_BAZAAR`; read in Amazon's model, not yet seen on a live account. (P-sell-49)
- `getOrderMetrics` with `amazonProgram=AmazonHaul` takes the Product Listing or the Inventory and Order Tracking role. (P-sell-49)
- No public Amazon page read states Haul's referral or fulfilment fees, and practitioners disagree on them. (P-sell-50)
- The fees actually charged on a Haul order are in the `listTransactions` transactions whose `BusinessContext.storeName` is `AMAZON_HAUL`. (P-sell-50)
- Practitioners relaying Amazon's notice report that Haul returns are not sent back to the seller but liquidated, donated or disposed of, with fees, and that the refund administration fee is the main store's. (P-sell-50)
- Amazon's changelog announces `storeName` `AMAZON_FBA_FROM_ORIGIN` "Starting 6 November 2026", "representing FBA from origin transactions", for "all Amazon stores", only on new such transactions. (P-sell-51)
- The model rolled the `AMAZON_FBA_FROM_ORIGIN` value back on 2026-10-29, and no Amazon page read defines FBA from origin or its fees. (P-sell-51)
- As reported in Chinese media, Amazon's 2025-12 China summit announced Fulfill From Origin (FFO): the seller inbounds at an origin-country warehouse, lists on international stores, and Amazon delivers each order cross-border; it ran first on Haul and widens in 2026. (P-sell-51)
- No Amazon page read ties FFO to the `AMAZON_FBA_FROM_ORIGIN` value. (P-sell-51)
