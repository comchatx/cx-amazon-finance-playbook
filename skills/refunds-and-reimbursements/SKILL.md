---
name: refunds-and-reimbursements
description: "What refunds, returns, claims and reimbursements do to an Amazon seller's money: customer refunds and which part of the referral fee and the FBA fee comes back (less the refund administration fee), returnless and partial refunds, restocking fees and return labels, A-to-z Guarantee claims, chargebacks and SAFE-T claims, FBA inventory reimbursements for lost or damaged inventory, missing inbound, customer returns and removals (IDR portal, Manage Your Sourcing Cost valuation, reversals, claim windows), the Reimbursements report GET_FBA_REIMBURSEMENTS_DATA, refund, chargeback and reimbursement lines in Finances and the settlement report, and Grade and Resell, donations, liquidation defaults and Amazon Resale. For any seller question about what a refund or return cost, what Amazon reimbursed or did not, a reversed reimbursement, lost inventory, an A-to-z claim or chargeback, or where refunds and reimbursements show in their Amazon money."
---

## Refunds

- A refund reverses the sale's charge lines and promotions (`ItemChargeAdjustmentList`, `PromotionAdjustmentList`). (P-ref-1)
- The referral fee comes back minus a refund administration fee per line item, capped per store. (P-ref-2)
- Practitioners report the FBA fulfilment fee does not come back; no Amazon page read says so. (P-ref-3)
- On seller-fulfilled orders Amazon also refunds for the seller: at first scan, by the seller's returnless rule, automatically after the seller's deadline, and on A-to-z claims, chargebacks and customer service. (P-ref-4)
- Returnless and partial FBA refunds are seller-funded; no reimbursement follows. (P-ref-8)

## Claims

- An assigned A-to-z claim debits the seller or cancels a future payment. (P-ref-9)
- Amazon carries fraud chargebacks, the seller service-related ones. (P-ref-10)
- SAFE-T reimburses seller-fulfilled refunds the seller did not cause. (P-ref-11)

## FBA reimbursements

- Covered: fulfilment-centre loss or damage, missing from inbound, lost or damaged removals, customer returns not returned or returned unsellable through Amazon's fault; not customer-damaged returns. (P-ref-12)
- Amazon pays most warehouse-lost, warehouse-damaged and customer-return cases without a claim; removal claims are filed manually. (P-ref-13)
- Since 2025-03-31 pre-order losses pay sourcing cost (Amazon's estimate unless the seller enters one), post-order losses sale price minus fees: read in Amazon's documents, not yet seen on a live account. (P-ref-14)
- Amazon reverses one paid in error or for a found unit; `original-reimbursement-id` links back. (P-ref-18)
- Amazon's posts state different claim windows; which the claim forms enforce is read in Amazon's documents, not yet seen on a live account. (P-ref-16)

## Reads

- `GET_FBA_REIMBURSEMENTS_DATA` carries a `reason`, cash and inventory quantities, and reversal links; Amazon publishes no list of `reason` values. (P-ref-19, P-ref-17)
- `listTransactions` by `ORDER_ID` finds refunds and adjustments posted days to months later. (P-ref-23)
- No SP-API operation issues a refund, files a claim or enters a sourcing cost. (P-ref-29)

## References

- references/refunds.md: refund lines, fees and where rates are read, triggers, dates.
- references/claims.md: A-to-z, chargebacks, SAFE-T, reserve.
- references/reimbursements.md: scope, valuation, claim windows, the report.
- references/lines-and-reads.md: Finances, settlement, roles.
- references/value-recovery.md: Grade and Resell, donations, Resale.
- references/tools.md: recovery services, tools.
- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
