---
name: fees-and-charges
description: "What each charge Amazon takes from a seller is, how it is worked out, when it posts and under which label: referral, closing and per-item fees, the subscription, refund administration, digital services and ACCS fees, coupon, deal, Vine, Transparency, EPR, advertising, Buy Shipping and Haul charges, and FBA fulfilment, storage, aged-inventory, low-inventory, inbound placement and defect, returns, removal and disposal, capacity, MCF, AGL and Amazon Freight charges, size tiers and yearly fee changes, with what `getMyFeesEstimateForSKU`, the Fee Preview report and `economicsPreview` leave out. For any question about why an Amazon fee was taken, how it is worked out, what it is called on a statement, when it posts, why it changed, or why an estimate and a posted fee differ."
---

## Selling fees

- The referral fee is the greater of a category percentage of the total sales price and any per-item minimum, on the marketplace's pricing page. (P-sell-1, P-sell-4, P-sell-39)
- On a refund the referral fee is credited back minus a refund administration fee, the lesser of a fixed amount and a percentage of the referral fee, by marketplace; research/areas/selling-fees.md, P-sell-7, holds the percentages as read. (P-sell-7)
- Advertising posts only when deducted from the selling balance, invoice-level, not per ASIN. (P-sell-23)

## Fulfilment, storage and account charges

- The FBA fulfilment fee is charged per unit at the ship date's rate. (P-ful-1)
- Monthly storage is an account-level charge with no order, collected the following month; `GET_FBA_STORAGE_FEE_CHARGES_DATA` estimates it per product. (P-ful-3)
- The subscription is a monthly account fee, not per unit. (P-sell-11)
- The inbound placement fee posts in `listTransactions` weeks after receipt; `listPlacementOptions` quotes it, and no SP-API report itemises it. (P-ful-6)
- `ServiceFeeEvent` has an order id and SKU; whether storage, placement or capacity charges reach order-scoped reads is read in Amazon's model, not yet seen on a live account. (P-ful-17)
- A period's fulfilment and storage total holds earlier periods' charges; booking them by posting date, covered period or amortisation, or by volume, units or sales share, is the seller's choice. (P-ful-21)

## Dates and estimates

- Amazon's Date Range reports date transactions by posting, which "may not correspond to the order date or the shipment date"; vendors document order-date and settlement-date profits differing by date basis. (P-rec-17, P-prof-27)
- A fee estimate (Product Fees, Fee Preview, `economicsPreview`) is per unit at one price, without program fees, subscription, high-volume listing, refund administration or advertising. (P-sell-29)
- Product Fees estimates are "not guaranteed" and omit storage, placement, removal and returns fees. (P-sell-30, P-ful-19)

## References

- references/selling-fees.md: referral, refund administration, closing, subscription, digital services, tax on fees, fee changes.
- references/program-fees.md: coupons, deals, Vine, ads, EPR, Haul.
- references/fulfilment-charges.md: fulfilment, measured size tiers, dimension claims, peak window, storage, placement, returns, removal, capacity.
- references/inbound-freight.md: AGL, SEND, Freight, GWD.
- references/where-fees-land.md: event lists, labels, economics, estimates, roles.
- ../product-earnings/SKILL.md: spreading charges over products.
- ../refunds-and-reimbursements/SKILL.md: refunds as money.
- ../tax-lines/SKILL.md: tax lines.
