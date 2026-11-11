# Deferral: from the order to the available balance

## The path

- In Amazon's words, a sale's money is added to the deferred amount when shipped, enters the reserve period when delivered, moves into the account balance when that period ends, becomes available, is disbursed by the settlement cycle or an on-demand request, and then reaches the bank. (P-flow-1)
- Each transaction's release day is `maturityDate` in its `listTransactions` entry (`DeferredContext`). (P-flow-1)
- A payout's time to the bank shows in its `statusHistory` in `listPayouts`, from `IN_TRANSIT` to `PAID`; whether `listPayouts` answers in NA and FE, and what `PAID` marks, are read in Amazon's documents, not yet seen on a live account. (P-flow-1)
- Amazon states the bank leg's length on its payment pages; research/areas/money-flow.md, P-flow-1, holds the value as read. (P-flow-1)

## The delivery-date reserve policy

- The reserve period runs from the delivery date, for FBA and FBM orders alike. (P-flow-2)
- The delivery date is the actual one where there is an integrated carrier or valid tracking, and otherwise the latest estimated delivery date. (P-flow-2)
- Amazon may extend the period "following an assessment of your overall risk and historical performance". (P-flow-2)
- Amazon names no exemption from the policy. (P-flow-2)
- Amazon staff describe a range of periods, and one Amazon email (EU, 2024) set a longer period for all orders "while we are reviewing your account"; research/areas/money-flow.md, P-flow-2, holds the periods as read. (P-flow-2)
- The period applied to each sale is its `maturityDate` in `listTransactions`; the account's reserve period as a setting is shown only on Seller Central's Statement View. (P-flow-2)
- Amazon's English worked examples and Amazon China's explainer do not agree on which calendar day after delivery a sale is released, and Amazon China's own two examples count differently from each other. (P-flow-3)
- Any one transaction's release date is the `maturityDate` Amazon returns for it ("The release date of the transaction"). (P-flow-3)

## The policy's dates

- Amazon calls the Delivery Date Based Reserve its "worldwide standard … since 2016". (P-flow-14)
- EU and UK base reserves moved to it from 2023-08-03; UK transitions were postponed, and extensions ended in September 2025. (P-flow-14)
- The remaining accounts were emailed on 2025-09-29/30: a US email gives 2026-03-12, and UK and EU sellers report emails giving 2026-03-05, 2026-03-12 or 2026-03-19. (P-flow-14)
- These migration dates are known only from emails sellers pasted in Seller Forums; no Amazon page states them. (P-flow-14)
- Brazil applies the policy (2025-06-27); Amazon published no other per-store dates in the pages read. (P-flow-14)
- During the 2026 transition, Amazon says delivery-date amounts "may temporarily" appear inside Account Level Reserve instead of as deferred transactions, and that this does not change when funds release. (P-flow-10)

## Deferred transactions

- Amazon defers a transaction "while an order is awaiting delivery or pending buyer payment". (P-flow-5)
- `deferralReason` examples are `DD7` (delivery date policy) and `B2B` (invoiced orders); the list is not closed. (P-flow-5)
- Only released transactions are paid in a settlement period. (P-flow-4)
- Settlement reports carry only disbursed transactions. (P-flow-4)
- `listTransactions` returns `DEFERRED`, `RELEASED` and `DEFERRED_RELEASED` transactions unless filtered. (P-flow-19)
- The v0 event operations do not show deferred events until they are released. (P-flow-19)

## Invoiced orders

- Amazon Business invoiced orders are credited when the buyer pays the invoice, or at the latest a set time past its due date, and sellers cannot opt out. (P-flow-6)
- In the US they appear as an "Invoiced Orders" row and may be paid by Amazon Services LLC, separately from standard orders paid by Amazon Payments, Inc. (P-flow-6)
- An invoiced order's release day is `maturityDate` on its `listTransactions` entry with `deferralReason` `B2B`. (P-flow-6)
- Amazon's terms for the US store are on How Amazon Business invoices work for sellers (https://sell.amazon.com/blog/amazon-business-invoice). (P-flow-6)
