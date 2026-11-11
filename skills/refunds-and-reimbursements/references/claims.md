# A-to-z claims, chargebacks and SAFE-T as money

## A-to-z Guarantee claims

- For an assigned A-to-z claim, Amazon refunds the buyer and debits the seller or cancels a future payment. (P-ref-9)
- A request for information left unanswered past Amazon's response time grants the claim, and a granted claim can be appealed within Amazon's appeal window. (P-ref-9)
- The response time and the appeal window are read from Amazon's pages A-to-z Guarantee claims (G27951) and Appeal an A-to-z Guarantee claim (G202041210) as the seller's own store shows them; no SP-API operation gives them. (P-ref-9)
- An order with an A-to-z claim is not eligible for SAFE-T. (P-ref-9)
- These A-to-z rules are read from search snippets of Amazon's pages G27951, G202041210 and G202188810, which render only in a browser. (P-ref-9)
- A granted A-to-z claim posts in Finances v0 as its own event list, `GuaranteeClaimEventList`, with the same item shape as a refund and an `OrderAdjustmentItemId`. (P-ref-41)
- In the settlement report it is the transaction type `A-to-z Guarantee Refund`, read from public files; Amazon publishes no list of transaction types. (P-ref-41)
- No public v2024-06-19 sample of an A-to-z transaction was found. (P-ref-41)

## Chargebacks

- Amazon carries fraud-related chargebacks. (P-ref-10)
- The seller carries service-related ones, such as non-receipt, and can refund or represent within Amazon's reply window. (P-ref-10)
- The customer's bank decides the outcome. (P-ref-10)
- The reply window and how long the outcome can take are read from Amazon's US page "How to manage Amazon chargebacks" (sell.amazon.com); no SP-API operation gives the reply window. (P-ref-10)
- A chargeback posts in Finances v0 as `ChargebackEventList`, with the refund item shape and an `OrderAdjustmentItemId`. (P-ref-41)
- In the settlement report it is the transaction type `Chargeback Refund`, read from public files. (P-ref-41)
- The model names no event for a chargeback won back by the seller. (P-ref-41)

## SAFE-T

- SAFE-T reimburses seller-fulfilled refunds the seller did not cause. (P-ref-11)
- In Finances v0 it posts as `SAFETReimbursementEvent`, with `SAFETClaimId` and `ReasonCode`, and the `SAFE-TReimbursement` charge. (P-ref-11, P-ref-41)
- No public v2024-06-19 sample of a SAFE-T transaction was found. (P-ref-41)
- The seller-fulfilled returns report carries the SAFE-T claim id, state and reimbursement amount. (P-ref-11)
- The US window is counted from the later of the return delivery scan and the refund date, or from the last scan for a lost shipment. (P-ref-11)
- Amazon changed the US window from 2026-02-16, in a Seller Forums News post. (P-ref-11)
- The window is read from Amazon's page Reimbursement for seller-fulfilled orders (G202188810) as the seller's own store shows it, and from that News post; no SP-API operation gives it. (P-ref-11)
- India has excluded packaging damage and broken seals from SAFE-T since 2025-08-01. (P-ref-11)
- An automatic refund issued because the seller did not refund a seller-fulfilled return in time cannot be recovered through SAFE-T, except when the item was lost in transit or the delivery confirmation was wrong. (P-ref-5)

## The reserve against refunds and claims

- `listBalances` reports an `ACCOUNT_LEVEL_RESERVE` "to cover potential liabilities such as refunds, chargebacks, or other claims". (P-ref-27)
- Finances v0 `ReserveEvent` is "generated at the time a settlement period closes" when money is held back. (P-ref-27)
- The settlement report carries the reserve as `Current Reserve Amount` and `Previous Reserve Amount Balance`. (P-ref-33)
- ../money-flow/SKILL.md: how the reserve moves between sale and payout.
