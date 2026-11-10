# The reads that carry each state

- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
- ../money-reads/SKILL.md: the finance reads across this package, by role, window and lag.

## Transactions

- `listTransactions` returns `DEFERRED`, `RELEASED` and `DEFERRED_RELEASED` transactions unless filtered. (P-flow-19)
- The v0 event operations do not show deferred events until they are released. (P-flow-19)
- A transaction's `DeferredContext` carries `deferralReason` and `maturityDate`, "The release date of the transaction". (P-flow-3, P-flow-5)
- Amazon's documented way to list a payout's transactions is to take the `FinancialEventGroupId` from `listFinancialEventGroups` and call `listTransactions` with `relatedIdentifierName=FINANCIAL_EVENT_GROUP_ID`. (P-flow-18)
- `listSummary` gives a settlement's `netProceeds` and breakdowns by `SETTLEMENT_ID`. (P-flow-18)
- `listTransactions` has no `SETTLEMENT_ID` filter: the 2026-07-29 release note announced one, and the model's one-day addition was rolled back on 2026-10-29. (P-flow-18)

## Limits of both Finances versions

- ../money-reads/SKILL.md: the Finances reads' posting lag, date-window, history and paging limits.
- `listFinancialEventGroups` shares the date-window limit of `listTransactions`; the values are in the parameter and operation descriptions of `listTransactions` (finances_2024-06-19.json) and of `listFinancialEventGroups` and `listFinancialEventsByGroupId` (financesV0.json). (P-flow-20)

## Settlement groups

- Each financial event group is a settlement period or payout. (P-flow-17)
- A group with `ProcessingStatus` `Open` holds the current balance in `OriginalTotal`; a `Closed` one holds the disbursed or charged amount. (P-flow-17)
- `OriginalTotal` is in the store's currency and `ConvertedTotal` in the disbursed currency. (P-flow-17)
- `FundTransferDate` is set only once a group is closed. (P-flow-17)
- `TraceId` is the bank-side lookup id. (P-flow-17)
- In the v0 model, a negative balance's recovery is a `DebtRecoveryEvent`, and a period-close reserve is an `AdjustmentEvent` of type `ReserveEvent`. (P-flow-16)

## Balances and payouts

- `listBalances` returns `AVAILABLE`, `RESERVED`, `ACCOUNT_LEVEL_RESERVE`, `DEFERRED` and `TOTAL` balances by account type and store, current or as of a date; `lastUpdatedTime` is in the store's local time zone. (P-flow-21)
- `listExpectedPayouts` returns the next payout's amount and `scheduledDate`, with status `SCHEDULED`, `DISABLED`, `AT_RISK` ("may fail because of an invalid deposit instrument") or `NO_PAYOUT_EXPECTED`. (P-flow-22)
- `listPayouts` returns each payout's status history (`STARTED`, `IN_TRANSIT`, `PAID`, `FAILED`, `CANCELLED`, `NO_PAYOUT`), failure reason, type (`SCHEDULED` or `ON_DEMAND`), rail, trace id and settlement id. (P-flow-22)
- `listPayouts` and `listExpectedPayouts` both need Finance and Accounting. (P-flow-22)
- Role Mappings list `listPayouts` and `listExpectedPayouts` for "NA, EU, FE", while the model and the live references say "This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE"; which regions answer is read in Amazon's documents, not yet seen on a live account. (P-flow-22)

## Reports

- Settlement reports cannot be requested or scheduled: Amazon generates them, and `getReports` finds them. (P-flow-23)
- Settlement reports are kept for a limited time, stated in the `createdSince` description of `getReports` (reports_2021-06-30.json). (P-flow-23)
- Only `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` survives 2026-11-11. (P-flow-23)
- The settlement V2 report has one row per `amount-type` / `amount-description` / `amount`. (P-flow-23)
- Amazon documents settlement V2 amounts in local number formats, with a decimal comma in EU stores; this is read in Amazon's documents, not yet seen on a live account. (P-flow-23)
- The Deferred Transaction Report (`GET_DATE_RANGE_FINANCIAL_HOLDS_DATA`, Finance and Accounting) lists deferred transactions over a date range whose maximum Amazon's Payment Reports page states. (P-flow-24)
- Amazon states the Deferred Transaction Report must first be requested in Seller Central's Payments Reports Repository before the Reports API can fetch it; this is read in Amazon's documents, not yet seen on a live account. (P-flow-24)

## Notifications

- `TRANSACTION_UPDATE` is sent when a new transaction is posted. (P-flow-25)
- `TRANSACTION_UPDATE` carries type, posted date, total amount and identifiers, but no deferral status or balance. (P-flow-25)
- `TRANSACTION_UPDATE` is delivered through Amazon SQS. (P-flow-25)

## What no seller read covers

- The Finance Remittance API (2026-03-17) and the Invoices API (2026-06-25) are vendor APIs ("Vendors only"). (P-flow-29)
- A seller's payouts are read through Finances and Transfers. (P-flow-29)
- Seller Wallet's API needs the AISP or PISP open-banking roles, so a seller's own Finance and Accounting app cannot read it. (P-flow-28)
- Only Seller Central shows the reserve reason and the account's reserve period. (P-flow-31)
- Only Seller Central offers Request Payment or Disburse on Demand outside the stores `initiatePayout` covers (listed in the transfers_2024-06-01 model). (P-flow-31)
- Only Seller Central handles Express Payout enrolment, changes to deposit methods or the card, requests for the Deferred Transaction Report, and Seller Wallet enrolment. (P-flow-31)
