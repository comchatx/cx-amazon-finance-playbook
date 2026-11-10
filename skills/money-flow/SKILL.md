---
name: money-flow
description: "Where an Amazon seller's money is between the order and the bank: deferred transactions and the delivery-date reserve policy, the Account Level Reserve, the available balance, settlement periods, scheduled and on-demand payouts (Disburse on Demand, Disburse Now, Express Payout, `initiatePayout`), a negative balance charged to the card, ad charges deducted from the balance, funds withheld under the Funds Disbursement Eligibility policy, deactivation holds, frozen funds and TROs, Payability-style advances, the newer ZA, EG, TR, IE and BE stores, and currency conversion through ACCS, ACCS CNY, Seller Wallet or a PSP under SAFE conversion rules and its CNY conversion quota, as `listBalances`, `listTransactions`, `listFinancialEventGroups`, `listPayouts` and `listExpectedPayouts` show them. For any question on where the money is, when it is released or paid, why a payout is missing, held or frozen, or how proceeds are converted and received in CNY."
---

## Release

- The reserve period runs from the delivery date, FBA and FBM alike; Amazon may extend it on risk and performance, and one Amazon email set a longer period for all orders under account review. (P-flow-2)
- The period applied to each sale is its `maturityDate` in `listTransactions`, beside `deferralReason` (`DD7`, `B2B`; open list); the account's setting shows only on Statement View. (P-flow-2, P-flow-3, P-flow-5)
- `listTransactions` returns `DEFERRED`, `RELEASED` and `DEFERRED_RELEASED` lines unless filtered. (P-flow-19)
- Only released transactions are paid in a settlement period. (P-flow-4)

## Balance

- `listBalances` returns `AVAILABLE`, `DEFERRED`, `ACCOUNT_LEVEL_RESERVE`, `RESERVED` and `TOTAL`, with no reason field; Statement View shows each reserve's reason. (P-flow-21, P-flow-40, P-flow-9)
- An `Open` group in `listFinancialEventGroups` holds the current balance in `OriginalTotal`; Amazon lists a payout's transactions by `listTransactions` with its `FinancialEventGroupId`. (P-flow-17, P-flow-18)
- Monthly storage is an account-level charge with no order, collected the month after it accrues; the order-scoped reads examined carry no such charge, group-scoped reads do. (P-ful-3, P-ful-17)

## Payouts

- Periods are `FinancialEventGroupStart`/`End`; the next payout is `scheduledDate` in `listExpectedPayouts` (`SCHEDULED`, `DISABLED`, `AT_RISK`, `NO_PAYOUT_EXPECTED`). (P-flow-11, P-flow-22, P-flow-40)
- `listPayouts` gives status history (`STARTED`, `IN_TRANSIT`, `PAID`), trace id and settlement id; whether it answers in NA and FE, and whether `PAID` marks the bank deposit or Amazon's processing, are read in Amazon's documents, not yet seen on a live account. (P-flow-1, P-flow-22)
- Amazon states a time from payout to bank on the US, CA, AE, SA, AU and IN pages read. (P-flow-1, P-flow-36)
- `initiatePayout`, a money-moving write, covers the EU stores the transfers_2024-06-01 model lists, one per store and account type per interval stated there. (P-flow-12, P-flow-13)

## References

- references/deferral.md: the path from order to bank, the reserve policy and its dates, invoiced orders.
- references/reserves.md: the Account Level Reserve's reasons, circulated formulas, balance types.
- references/payouts.md: cycle, on-demand payouts, negative balance, bank changes, newer stores.
- references/holds.md: funds withheld, deactivation, reviews, court freezes.
- references/reads.md: operations, reports, notifications.
- references/currency.md: ACCS, Seller Wallet, CNY.
- references/booking.md: how tools book deferred money.
- ../fees-and-charges/SKILL.md: account-level charges.
- ../settlement-reconcile/SKILL.md: matching settlements.
- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
