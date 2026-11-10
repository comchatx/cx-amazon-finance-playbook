---
name: money-flow
description: "Where an Amazon seller's money is between the order and the bank: deferred transactions and the delivery-date reserve policy, the Account Level Reserve, the available balance, settlement periods, scheduled and on-demand payouts (Disburse on Demand, Disburse Now, Express Payout, `initiatePayout`), a negative balance charged to the card, ad charges deducted from the balance, funds withheld under the Funds Disbursement Eligibility policy, deactivation holds, frozen funds and TROs, Payability-style advances, the newer ZA, EG, TR, IE and BE stores, and currency conversion through ACCS, ACCS CNY, Seller Wallet or a PSP under SAFE conversion rules and its CNY conversion quota, as `listBalances`, `listTransactions`, `listFinancialEventGroups`, `listPayouts` and `listExpectedPayouts` show them. For any question on where the money is, when it is released or paid, why a payout is missing, held or frozen, or how proceeds are converted and received in CNY."
---

## From order to bank

- In Amazon's words, a sale's money is deferred when shipped, reserved from delivery, released into the balance, disbursed by cycle or on request and sent to the bank. (P-flow-1)
- The reserve period runs from the delivery date, FBA and FBM alike; Amazon may extend it on risk and performance. (P-flow-2)
- A transaction's release date is `maturityDate` in `listTransactions`, beside `deferralReason` (`DD7`, `B2B`; open list). (P-flow-3, P-flow-5)
- Only released transactions are paid in a settlement period, and settlement reports carry only disbursed ones. (P-flow-4)

## Balance and reserve

- `listBalances` returns `AVAILABLE`, `DEFERRED`, `ACCOUNT_LEVEL_RESERVE`, `RESERVED` and `TOTAL`. (P-flow-21, P-flow-40)
- Amazon describes the Account Level Reserve as per-order holds by reason (delivery date, open A-to-z claims, chargebacks, performance below benchmarks, account review, local income-tax withholding); no current Amazon page reached publishes a formula. (P-flow-7, P-flow-8)
- Each reserve's reason is shown on Statement View; `listBalances` has no reason field. (P-flow-9)

## Payouts

- Settlement periods are `FinancialEventGroupStart`/`End` in `listFinancialEventGroups`, the next payout `scheduledDate` in `listExpectedPayouts`, which can read `DISABLED`, `AT_RISK` or `NO_PAYOUT_EXPECTED`; `listPayouts` gives status history and `failureReason`; their regions, on which Role Mappings and the model disagree, are read in Amazon's documents, not yet seen on a live account. (P-flow-11, P-flow-22, P-flow-40)
- No Finances or Transfers type, status or field names funds withheld under the contract or the Funds Disbursement Eligibility policy, or their reason. (P-flow-40)
- A negative period-end balance is charged to the payment method on file. (P-flow-15)
- `initiatePayout`, a money-moving write, covers the EU stores the transfers_2024-06-01 model lists. (P-flow-12, P-flow-13)

## Currency

- `OriginalTotal` is in the store's currency, `ConvertedTotal` in the disbursed one; ACCS converts at its provider's rate on the transfer-initiation day. (P-flow-17, P-flow-26)

## References

- references/deferral.md: the path, the reserve policy's dates, invoiced orders.
- references/reserves.md: reserve composition, circulated rules, balance types.
- references/payouts.md: cycle, on-demand payouts, negative balance, bank changes, newer stores.
- references/holds.md: withholding, deactivation, reviews, court freezes.
- references/reads.md: operations, reports, notifications.
- references/currency.md: ACCS, Seller Wallet, CNY, FX differences.
- references/booking.md: how tools book deferred money.
- ../settlement-reconcile/SKILL.md: matching settlements.
- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
