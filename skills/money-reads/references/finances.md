# Finances reads: transactions, balances, summary and v0 events

## Transactions

- Finances v2024-06-19 `listTransactions` is the current per-transaction money read; its transactions carry the status `DEFERRED`, `RELEASED` or `DEFERRED_RELEASED`, and Role Mappings name Finance and Accounting for it (P-api-1).
- The model's Usage Plan states only the default rate of `listTransactions` (P-api-1).
- `listTransactions` needs `postedAfter` unless a related identifier is given (P-api-2).
- Each date bound of `listTransactions` must be more than two minutes in the past (P-api-2).
- Bounds more than 180 days apart answer with an empty response, not an error (P-api-2).
- Pages can be empty while `nextToken` continues (P-api-2).
- Transactions of the last 48 hours may be missing (P-api-2).
- Amazon's model states that for US MFN orders `listTransactions` is called without `marketplaceId` (P-api-5).

## Filters

- The filters Amazon's model supports are `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`, "the only `relatedIdentifier` with filtering capabilities at the moment" (P-api-3).
- The release note of 2026-07-29 announced a `SETTLEMENT_ID` filter; the model carried it only from 2026-10-28 (df7c6298) to the rollback of 2026-10-29 (db2936aa), and the live reference never listed it; read in Amazon's documents, not yet seen on a live account (P-api-3).
- `SETTLEMENT_ID` remains an identifier in a transaction's reply (P-api-3).

## Shape of the money

- A transaction's money is in `totalAmount` and in nested `breakdowns[]`, each of which can hold further `breakdowns[]` (P-api-4).
- `breakdownType` is an open string; Amazon publishes no closed list of its values (P-api-4).
- Amounts are signed decimals (P-api-4).

## Balances and summary

- `listBalances` returns the current balance, or the balance at a past `asOfDate`, by type: `AVAILABLE`, `RESERVED`, `TOTAL`, `DEFERRED`, `ACCOUNT_LEVEL_RESERVE` (P-api-7).
- Its sub-balances are by account type and marketplace, and `lastUpdatedTime` is in the marketplace's local time (P-api-7).
- `listBalances` with `asOfDate` and `balanceType=DEFERRED` gives the deferred amount at a past date (P-api-35).
- `listSummary` returns `netProceeds` with the `breakdowns` behind it, for a date period or for one `SETTLEMENT_ID` (P-api-8).

## The transactions of one payout

- Amazon's guide "Determine which transactions make up a payment" takes the payment's `FinancialEventGroupId` from v0 `listFinancialEventGroups`, then reads `listTransactions` with `FINANCIAL_EVENT_GROUP_ID` and `RELEASED`; read in Amazon's documents, not yet seen on a live account (P-api-6).

## Finances v0

- Amazon's Deprecation Schedule removes v0 `listFinancialEvents`, `listFinancialEventsByGroupId` and `listFinancialEventsByOrderId` on 2027-08-27, and does not schedule `listFinancialEventGroups` for removal; the dates are read on the SP-API Deprecation Schedule page (P-api-9).
- v0 omits deferred events until they are released (P-api-9).
- v0 `listFinancialEventsByGroupId` covers only the past two years (P-api-9).
- A v0 `FinancialEventGroup` carries the settlement period's open or closed status, its beginning balance, its total ("For an open financial event group, this is the current balance"), its fund transfer date (closed groups only) and its trace id (P-api-10).
