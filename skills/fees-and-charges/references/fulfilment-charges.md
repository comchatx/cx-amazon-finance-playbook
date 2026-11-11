# FBA fulfilment, storage, inbound and removal charges

## Fulfilment fee

- The FBA fulfilment fee is charged per unit when the unit leaves the fulfilment centre, at the rate in force on the ship date, so peak rates apply by ship date. (P-ful-1)
- What the per-unit fulfilment fee covers, and its price bands, are stated per store; CA, MX and JP state that it covers picking, packing, shipping, customer service and returns. (P-ful-25)
- A price threshold changes the fulfilment rate in the US, CA, AU, JP and MX; the thresholds and bands are on the store's page, and the fee a SKU gets at a given price is returned by `getMyFeesEstimateForSKU`. (P-ful-25)
- The weight that sets the fee differs by store: the EU and IN use the greater of unit weight and dimensional weight for parcels and oversize, AU uses a different dimensional divisor, CA uses the greater of actual and dimensional weight, and JP sizes items by the sum of the three sides. (P-ful-26)
- Envelopes, low-price FBA and special oversize use unit weight in the EU, and envelopes do in AU. (P-ful-26)
- The weight rule and divisor are on the store's page (EU/UK: the *Rate Card Europe Fees* in force, "Calculating your FBA fees"), and a SKU's Amazon-measured dimensions and tier are in `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`. (P-ful-26)
- Amazon's own measurement sets every size-tier-based fee: fulfilment, storage, aged, removal, disposal, MCF and placement. (P-ful-2)
- A dimension-based fee reimbursement must be requested within a window from the charge, stated on Seller Central help *FBA fees reimbursement policy: Weight and dimensions*; the date a fee was charged is its `postedDate` in `listTransactions`. (P-ful-2)
- Remeasurement happens only through Seller Central, with per-FNSKU and per-account limits. (P-ful-2)
- Whether a fee figure includes tax differs by store: JP fulfilment fees include consumption tax, MX fees include IVA, IN fees exclude GST, which is added, AU fees exclude GST, and EU manual processing fees have VAT assessed in addition where applicable. (P-ful-27)
- Fee figures from two stores can therefore sit on different tax bases; the tax on each estimated fee is `TaxAmount` in `getMyFeesEstimateForSKU`. (P-ful-27)
- India's FBA charge set is its own: weight handling by distance (local, regional, national) in weight steps, pick and pack per unit, storage per cubic foot per month, per-unit FC removal, and a closing fee by price band and channel, all on *sell.amazon.in fees and pricing*. (P-ful-28)

## Surcharges on the fulfilment fee

- The US low-inventory-level fee is a per-unit surcharge within the fulfilment fee family, applied at shipment from the weekly FNSKU-level days of supply, with listed exemptions. (P-ful-7)
- Amazon's help page states automatic reimbursement of the low-inventory-level fee when Amazon delayed the inbound. (P-ful-7)
- From 2027-02-01 the US low-inventory-level fee is based on actual shipments around the assessment instead of days of supply; the window is on Seller Central help *Low-inventory-level fee*, and how the fee is posted under the new rule is open. (P-ful-7)
- The days-of-supply threshold, windows and exemptions are on Seller Central help *Low-inventory-level fee*; the seller's own days of supply and weekly fee flag are in `GET_FBA_INVENTORY_PLANNING_DATA` (Amazon Fulfillment role), and the fee ahead in Data Kiosk `economicsPreview` as `LOW_INVENTORY_LEVEL_FEE`. (P-ful-7)
- Pan-EU has the analogous low-inventory cost coverage fee, for DE, FR, IT and ES. (P-ful-7)
- The fuel and logistics surcharge is a percentage of the FBA fulfilment fee, not of the price. (P-ful-8)
- The fuel and logistics surcharge started on 2026-04-17 in the US/CA and the EU/UK stores at different percentages, and rose in the EU/UK on 2026-11-02. (P-ful-8)
- The fuel surcharge percentage for the store is on Seller Central help *2026 US FBA fulfillment fee changes* (US, CA) or the *Rate Card Europe Fees* in force (EU/UK). (P-ful-8)

## Storage

- Monthly storage is assessed on the daily average volume over a calendar month and collected in the following month. (P-ful-3)
- Monthly storage is an account-level charge with no order. (P-ful-3)
- Amazon's per-product view of storage is the estimated `GET_FBA_STORAGE_FEE_CHARGES_DATA`. (P-ful-3)
- The storage utilization surcharge is part of the monthly storage fee, driven by the ratio of average daily volume stored to average daily volume shipped, above a ratio threshold, with exempt categories. (P-ful-4)
- In the US the storage utilization surcharge ends on 2027-02-01. (P-ful-4)
- The ratio threshold, window and exempt categories are on the store's page, and the seller's own ratio and surcharge rate per ASIN are `storage_utilization_ratio` and `utilization_surcharge_rate` in `GET_FBA_STORAGE_FEE_CHARGES_DATA`. (P-ful-4)
- The aged inventory surcharge, formerly long-term storage, is a monthly charge on top of storage, by age band. (P-ful-5)
- The age where the aged surcharge starts differs by store and changes by announcement; the starting age, bands and assessment day are on the store's page (US: *Amazon FBA (Fulfillment by Amazon)*; EU/UK: the *Rate Card Europe Fees* in force). (P-ful-5)
- The report carrying the aged surcharge keeps the "long-term storage" name, `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` (`surcharge-age-tier`, `snapshot-date`), and needs a one-month request window. (P-ful-5)
- The bands applied to the seller's stock are in `GET_FBA_INVENTORY_PLANNING_DATA` (`quantity-to-be-charged-ais-<band>`, `Inventory age snapshot date`; Amazon Fulfillment role). (P-ful-5)
- In the US the aged surcharge folds into a single age-based storage rate from 2027-02-01. (P-ful-5)
- In `listTransactions`, `TimeRangeContext` (`startTime`, `endTime`) is the field in Amazon's model that can date a charge to the period it covers, as distinct from `postedDate`; which charges carry it is open, not yet seen on a live account. (P-ful-16)

## Inbound

- The inbound placement fee is fixed when a placement option is confirmed, which is irreversible, and charged some weeks after the shipment is received. (P-ful-6)
- The placement charge timing is on Seller Central help *FBA inbound placement service fee* (US). (P-ful-6)
- The placement fee before confirmation is quoted in `listPlacementOptions` (`fees`, `discounts`; Amazon Fulfillment role), and the posted line is in `listTransactions`. (P-ful-6)
- No SP-API report itemises the placement charge. (P-ful-6)
- AWD-replenished stock carries no separate placement fee. (P-ful-6)
- Partnered-carrier inbound transport is quoted per shipment in `listTransportationOptions` (Amazon Fulfillment role). (P-ful-13)
- Cancelling a partnered-carrier shipment outside its void window can incur charges; each quote's void deadline is `quote.voidableUntil`. (P-ful-13)
- Content changes after confirmation carry a cost preview. (P-ful-13)
- Unplanned prep and label services and inbound-defect fees are itemised per shipment, carton and FNSKU, with `fee-type` and `fee-total`, in the Inbound Performance report. (P-ful-24)
- US prep by Amazon ended on 2026-01-01, and the 2026 schedule replaced the double inbound charge with a single inbound defect fee. (P-ful-24)

## Returns, removal and liquidation

- The high-return-rate returns fee is computed per ship month over that month and the next two, on returned units above the product's category threshold, and charged in a later month. (P-ful-9)
- Apparel and shoes are charged a returns fee per return as it occurs in the US, and as a share of the fulfilment fee in the EU. (P-ful-9)
- The thresholds, charge month and days, and the apparel and shoes rate are on Seller Central help *2026 returns processing fee changes* (US) or the *Rate Card Europe Fees* in force (EU/UK). (P-ful-9)
- Data Kiosk `economicsPreview` previews the fee ahead per SKU as `HIGH_RETURN_RATE_FEE` and `RETURN_PROCESSING_FEE`. (P-ful-9)
- US removal and disposal fees post per unit as each unit is removed or disposed of, for orders created on or after 2026-03-01, at unchanged rates. (P-ful-10)
- The Removal Order Detail report carries `removal-fee` per line. (P-ful-10)
- In the US, `FBALiquidationEvent` gives a liquidation's gross proceeds and the liquidation fee (`LiquidationFeeAmount`), and the seller receives the difference. (P-ful-11)
- In the EU and in CA (from 2025-11-05), liquidation carries a liquidations referral fee on gross recovery value plus a per-unit processing fee, on the *Rate Card Europe Fees* in force and in *2026 Updates to Canada referral and Fulfilment by Amazon fees*. (P-ful-11)

## Capacity, MCF and new-seller programs

- The capacity reservation fee is a seller-set bid, granted highest bid first, that performance credits earned on sales from the extra capacity can offset up to the whole fee. (P-ful-12)
- The capacity reservation fee is recorded in Finances v0 as `CapacityReservationBillingEvent`. (P-ful-12)
- Overage fees apply to on-hand stock, not open shipments, above the highest limit given for the period, and are itemised only in the overage report, which needs the Amazon Fulfillment role. (P-ful-12)
- MCF fees ride on the MCF order, in v0 `OrderFeeList`. (P-ful-14)
- The 2020-07-01 MCF preview names per-unit, per-order, transportation and COD fees; the 2026-07-04 preview uses an open price `type`. (P-ful-14)
- New-to-FBA programmes reduce fulfilment-family charges (free storage, returns waivers, placement and partnered-carrier credits). (P-ful-23)
- These reductions appear as promotion or incentive amounts, such as economics `promotionAmount` and the Storage Fees report's incentive columns, rather than as missing charges. (P-ful-23)

## Timing

- A settlement or period total of fulfilment and storage charges includes storage for the previous month, placement for receipts from weeks earlier, high-return-rate fees for shipments months earlier, and per-unit removal charges spread over processing. (P-ful-21)
- Such a total is therefore not the fulfilment cost of that period's sales. (P-ful-21)
- Assigning these charges to periods or products can follow the posting date, the covered period, amortisation, or a volume, unit or sales share, each a seller's choice; sellerboard amortises, SellerSpace books per ASIN, and Lingxing allows a custom allocation. (P-ful-21)
- Fulfilment fee rates change on announced dates (US mid-January, EU early in the year) and also mid-year, as with the fuel surcharge. (P-ful-22)
- A fulfilment rate figure is meaningful only with its effective date and marketplace. (P-ful-22)
- The peak window and the next fee-change dates are on Seller Central help *2026 US FBA fulfillment fee changes* and *Update to US Referral and Fulfillment by Amazon fees for 2027* (US) or the *Rate Card Europe Fees* in force (EU/UK); the dates a product's fees actually changed show as range splits in Data Kiosk `economics`. (P-ful-22)

## Competition cases about fulfilment and pricing

- FTC et al. v. Amazon (W.D. Wash. 2:23-cv-01495) alleges anti-discounting punishment of sellers and conditioning Prime eligibility on Amazon's fulfilment; no court has found these allegations true. (P-tool-25)
- Trial in the FTC case is set for 2027-03-29, a date a 2026-10-09 ruling kept as reported by PYMNTS citing Law360 and MLex, and California v. Amazon is set for trial on 2027-01-19. (P-tool-25)
- The EU commitments (2022-12-20) and the UK CMA commitments (2023-11-03) let Prime sellers choose and negotiate their own carriers. (P-tool-25)
- As reported by Cuatrecasas, GRC Report and beck-aktuell (the Bundeskartellamt's own page not read), the Bundeskartellamt's decision of 2026-02-04 bars Amazon's price-control mechanisms on amazon.de, with a disgorgement, and is under appeal. (P-tool-25)
