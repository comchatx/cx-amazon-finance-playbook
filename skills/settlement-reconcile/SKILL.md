---
name: settlement-reconcile
description: "Reconciling Amazon's money to the bank deposit and the books: the V2 settlement report (GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2) and its amount-type and amount-description rows, financial event groups and listTransactions by FINANCIAL_EVENT_GROUP_ID, listSummary by SETTLEMENT_ID, the Date Range and Deferred Transaction reports, reserve, deferred and card-charge lines as they explain a deposit or month that does not tie out, UTC against local dates, month-end splits, charges billed outside the settlement (ads on card, Lending, AGL, Amazon Shipping, Transparency), and how A2X, Link My Books, Taxomate, Sellerboard, Lingxing, 积加, 赛狐, 金蝶 and 用友 book a settlement into Xero, QuickBooks or a Chinese ledger (对账, 做账). For any question on why a deposit, statement or month's Amazon figures do not tie to each other or to the books, or how a settlement is reconciled or booked."
---

## Settlement report

- Amazon generates settlement reports, found with `getReports` (`GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`), not requested. (P-rec-1)
- The API lists settlements back about 90 days; older ones are in Seller Central. (P-rec-6)
- Per practitioners, account-level rows (storage, subscription, reserve, reimbursement) have empty `sku` and `order-id`; a SKU filter drops them. (P-rec-29)

## Payout to bank

- A closed financial event group's `OriginalTotal` is the payout or a charge, and `ConvertedTotal` the disbursed-currency total, read in Amazon's model, not yet seen on a live account. (P-rec-10, P-rec-24)
- A payment's lines are `listTransactions` by `FINANCIAL_EVENT_GROUP_ID` with `transactionStatus=RELEASED`; whether they sum to the settlement V2 total, or only with `DEFERRED_RELEASED`, is read in Amazon's documents, not yet seen on a live account. (P-rec-11)

## Why figures differ

- A settlement holds released money; deferred ones enter on release. (P-rec-8)
- `listBalances` returns `DEFERRED` and reserve balances now or as of a past date (`asOfDate`), such as a month end; the Deferred Transaction Report lists only current deferrals. (P-rec-14, P-rec-20)
- Settlement `posted-date-time` is UTC; Date Range reports and `listSummary` use local time. (P-rec-15)
- Date Range reports count posted transactions, deferred included, since 2026, for periods from 2025-01-01; Business Reports count by order date. (P-rec-31, P-rec-18)
- Card- or invoice-paid ads and, per search snippets of Amazon's page, AGL paid by wire sit outside the settlement; Amazon Shipping bills in Shipper Central, and whether each also posts as an Adjustment is read in Amazon's documents, not yet seen on a live account. (P-rec-42, P-rec-44, P-rec-45)

## Booking

- A settlement crossing month end is booked whole on its period or split by each line's posting month, as the seller chooses. (P-rec-32)
- Practitioners describe a clearing account, gross or net, reserves as a current asset and a deferral accrual: seller's choices changing the P&L or balance sheet, none Amazon's rule. (P-rec-33)

## References

- references/settlement-report.md: V2 columns, rows, archive.
- references/payouts-and-transactions.md: groups, transactions, balances, payouts.
- references/timing-and-deferral.md: clocks, deferral, reserves.
- references/outside-the-settlement.md: charges billed elsewhere.
- references/accounts-and-stores.md: regions, stores.
- references/completeness.md: shipped against settled, horizons.
- references/books-and-tools.md: choices, connectors, ledgers.
- ../money-flow/SKILL.md: sale to bank.
- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
