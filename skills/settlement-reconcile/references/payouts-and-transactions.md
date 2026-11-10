# Payouts, financial event groups and transactions

## Financial event groups (Finances v0)

- A financial event group is a settlement period. (P-rec-10)
- A group's `ProcessingStatus` is `Open`, with `OriginalTotal` the current balance, or `Closed`, with `OriginalTotal` the disbursement or the charge amount. (P-rec-10)
- A group carries `FundTransferDate` (closed groups only), `TraceId`, `AccountTail`, `BeginningBalance` and `ConvertedTotal`, the total in the disbursed currency. (P-rec-10)
- The seller's own settlement periods are read from `listFinancialEventGroups` (`FinancialEventGroupStart`, `FinancialEventGroupEnd`). (P-rec-38)
- The v0 event operations `listFinancialEvents`, `listFinancialEventsByGroupId` and `listFinancialEventsByOrderId` do not show deferred events until they are released. (P-rec-9)
- `listFinancialEventGroups` and `listFinancialEventsByGroupId` take Finance and Accounting or, in the EU only, Account Information Service Provider. (P-rec-7)

## Transactions (Finances 2024-06-19)

- `listTransactions` returns `DEFERRED`, `RELEASED` and `DEFERRED_RELEASED` transactions unless `transactionStatus` filters them. (P-rec-9)
- Amazon's documented way to list the transactions behind a payment: take the payment's `FinancialEventGroupId` from `listFinancialEventGroups`, then call `listTransactions` with `relatedIdentifierName=FINANCIAL_EVENT_GROUP_ID` and `transactionStatus=RELEASED`. (P-rec-11)
- Whether those released transactions sum to the settlement V2 `total-amount`, or only with `DEFERRED_RELEASED` added, is read in Amazon's documents, not yet seen on a live account. (P-rec-11)
- The model and the live reference state that `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID` are "the only `relatedIdentifier` with filtering capabilities at the moment". (P-rec-12)
- The 2026-07-29 release note announces a `SETTLEMENT_ID` filter on `listTransactions`; it was in the model for one day (2026-10-28) and removed by the 2026-10-29 "Finance API Rollback"; whether a live call accepts it is read in Amazon's documents, not yet seen on a live account. (P-rec-12)
- `SETTLEMENT_ID` is returned in `listTransactions` responses and filters `listSummary`. (P-rec-12)
- A `listTransactions` or `listFinancialEventGroups` window over 180 days yields an empty result, not an error. (P-rec-16)
- `postedBefore` must be at least two minutes in the past. (P-rec-16)
- Amazon states that `listTransactions` events from the last 48 hours may be missing. (P-rec-16)
- Pages may come back empty while `nextToken` continues. (P-rec-16)
- `listFinancialEventsByGroupId` covers only the last two years. (P-rec-16)
- Amazon's changelog announced a `BusinessContext.storeName` value `AMAZON_FBA_FROM_ORIGIN` from 2026-11-06 beside `AMAZON_HAUL`, and told integrations to handle unknown enum values gracefully. (P-rec-36)
- The model added `AMAZON_FBA_FROM_ORIGIN` on 2026-10-28 and removed it in the 2026-10-29 rollback, and the live reference lists only `AMAZON_HAUL`, so `storeName` values in replies may go beyond the model's enum. (P-rec-36)

## Summary and balances

- `listSummary` returns `netProceeds` and nested `breakdowns`, for a date range given as ISO dates or for one settlement (`relatedIdentifierName=SETTLEMENT_ID`). (P-rec-13)
- Amazon's `listSummary` reference example uses the Statement view's categories (Sales, Product Charges, Expenses, FBA fees, Refunds); which `breakdownType` values a seller's data carries, and whether a settlement summary reproduces the Statement view's lines, is read in Amazon's documents, not yet seen on a live account. (P-rec-13)
- `listBalances` returns `AVAILABLE`, `RESERVED`, `TOTAL`, `DEFERRED` and `ACCOUNT_LEVEL_RESERVE`, by account type and marketplace, now or as of a past date (`asOfDate`). (P-rec-14)
- `listTransactions`, `listSummary`, `listBalances`, `listFinancialEventsByOrderId`, `listPayouts` and `listExpectedPayouts` require Finance and Accounting. (P-rec-7)

## Payouts (Transfers 2024-06-01)

- `listPayouts` returns payouts with a status history (`STARTED`, `IN_TRANSIT`, `PAID`, `FAILED`, `CANCELLED`, `NO_PAYOUT`), a type (`SCHEDULED` or `ON_DEMAND`), `traceId` ("The banking network's unique identifier"), `paymentRail`, `period`, the account tail and a `SETTLEMENT_ID`. (P-rec-25)
- `listExpectedPayouts` returns the next payout's `scheduledDate` and status (`SCHEDULED`, `DISABLED`, `AT_RISK`, `NO_PAYOUT_EXPECTED`). (P-rec-25)
- The next payout's period and date are read from `listExpectedPayouts` (`period`, `scheduledDate`). (P-rec-38)
- The Transfers model names the EU8 marketplaces while Role Mappings list NA, EU and FE; whether `listPayouts` answers in NA and FE, and whether `PAID` means the deposit or Amazon's processing, is read in Amazon's documents, not yet seen on a live account. (P-rec-25)
- `initiatePayout` is the only payout-moving write; Role Mappings give it the EU region, with Finance and Accounting or Payment Initiation Service Provider, either one sufficing. (P-rec-26)
- `initiatePayout`'s own description states its marketplaces and its limit on on-demand payouts per marketplace and account type, and it returns `payoutReferenceId`, "The financial event group ID for a successfully initiated payout". (P-rec-26)
- An on-demand payout already made shows in `listPayouts` with `type` `ON_DEMAND` and its `creationDate`. (P-rec-26)

## Identifiers

- In Amazon's examples a financial event group id is a long opaque string while a settlement id is numeric, and the example payout's `id` equals its `SETTLEMENT_ID`. (P-rec-28)
- The two identifiers are not interchangeable without a lookup; whether a report's `settlement-id` equals the APIs' `SETTLEMENT_ID` is read in Amazon's documents, not yet seen on a live account. (P-rec-28)
- Lingxing (a vendor) says the settlement id exists only once the settlement report is issued. (P-rec-28)

## Negative balances and currency

- When a settlement's balance is negative, Amazon recovers the debt from the seller's charge instrument or from later proceeds, as read in Amazon's model, not yet seen on a live account. (P-rec-23)
- v0 records the recovery as `DebtRecoveryEvent` (`DebtPayment`, `DebtPaymentFailure`, `DebtAdjustment`), with the charge instrument's tail and amount and the begin and end of the group where the debt arose. (P-rec-23)
- A closed group's `OriginalTotal` can be a charge to the seller, not only a payout, read in Amazon's model, not yet seen on a live account. (P-rec-23)
- A2X, beancount and Lingxing describe the negative balance and its card charge as a "pending balance", a "Successful Charge" or 信用卡扣款. (P-rec-23)
- A payout can arrive in a currency other than the marketplace's: `OriginalTotal` is in the transactions' currency and `ConvertedTotal` in the disbursed currency; how a multi-currency payout shows is read in Amazon's model, not yet seen on a live account. (P-rec-24)
- Lingxing (a vendor) attributes the difference to a bank account bound in another currency. (P-rec-24)

## Vendor-only APIs

- The Finance Remittance API (v2026-03-17) and the Invoices API (v2026-06-25) are documented "Vendors only". (P-rec-27)
- Remittance mirrors Vendor Central's Remittance view, and neither API carries a seller's settlement or bank-payment detail. (P-rec-27)
