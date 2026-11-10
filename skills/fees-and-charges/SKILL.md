---
name: fees-and-charges
description: "What each charge Amazon takes from a seller is, how it is worked out, when it posts and under which label: referral, closing and per-item fees, the subscription, refund administration, digital services and ACCS fees, coupon, deal, Vine, Transparency, EPR, advertising, Buy Shipping and Haul charges, and FBA fulfilment, storage, aged-inventory, low-inventory, inbound placement and defect, returns, removal and disposal, capacity, MCF, AGL and Amazon Freight charges, size tiers and yearly fee changes, with what `getMyFeesEstimateForSKU`, the Fee Preview report and `economicsPreview` leave out. For any question about why an Amazon fee was taken, how it is worked out, what it is called on a statement, when it posts, why it changed, or why an estimate and a posted fee differ."
---

## Selling fees

- The referral fee is the greater of a category percentage of the total sales price (item, delivery, gift wrap) and any per-item minimum (none for media, some grocery categories and Amazon.com.au), both on the marketplace's pricing page. (P-sell-1, P-sell-4, P-sell-39)
- On a refund the referral fee is credited back minus a refund administration fee. (P-sell-7)
- `Commission` is the referral fee, `FixedClosingFee` the Individual per-item fee, `VariableClosingFee` the media closing fee. (P-sell-9)
- The digital services fee is a percentage of Selling on Amazon fees, and in stated cases FBA fees, not of sales. (P-sell-13)
- Coupon fees are separate from the coupon budget funding the discount. (P-sell-15)
- Advertising reaches the finance events only if deducted from the selling balance (the default), as invoice-level `ProductAdsPaymentEvent` or the settlement "Cost of Advertising" line, neither per ASIN. (P-sell-23)

## Fulfilment and storage

- The FBA fulfilment fee is charged per unit at shipment, at the ship date's rate. (P-ful-1)
- Monthly storage is collected the following month as an account-level line; `GET_FBA_STORAGE_FEE_CHARGES_DATA` estimates it per product. (P-ful-3)
- The inbound placement fee is fixed on confirming a placement option, quoted in `listPlacementOptions`, and posted in `listTransactions` weeks after receipt; no SP-API report itemises it. (P-ful-6)
- A period's fulfilment and storage total holds earlier periods' charges, so it is not the fulfilment cost of that period's sales; booking them by posting date, covered period, amortisation or share is the seller's choice. (P-ful-21)

## Labels and estimates

- Amazon publishes no closed list of `breakdownType`, `FeeType` or `amount-description` values. (P-sell-26, P-ful-15)
- A fee estimate (Product Fees, Fee Preview, `economicsPreview`) is per unit at one price, without program fees, subscription, high-volume listing fee, refund administration or advertising. (P-sell-29)
- Product Fees estimates are "not guaranteed" and leave out storage, placement, removal and returns fees. (P-sell-30, P-ful-19)

## References

- references/selling-fees.md: referral, refunds, closing, subscription, digital services, tax on fees, fee changes.
- references/program-fees.md: coupons, deals, Vine, ads, EPR, Haul.
- references/fulfilment-charges.md: fulfilment, surcharges, storage, placement, returns, removal, capacity, timing.
- references/inbound-freight.md: AGL, SEND, Freight, GWD.
- references/where-fees-land.md: event lists, labels, economics, estimates, roles.
- ../product-earnings/SKILL.md: spreading charges over products.
- ../refunds-and-reimbursements/SKILL.md: refunds as money.
- ../tax-lines/SKILL.md: tax lines.
