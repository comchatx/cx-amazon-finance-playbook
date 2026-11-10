---
name: money-reads
description: "Which SP-API read carries each figure of a seller's Amazon money, and that read's role, window, lag, history reach and pitfalls: Finances listTransactions, listBalances and listSummary, the v0 financial event groups, Transfers listPayouts and listExpectedPayouts, the settlement V2 and Deferred Transaction reports, the FBA fee, storage and reimbursement reports, Product Fees estimates, Orders proceeds, Data Kiosk Economics and the tax reports. For any question about which SP-API operation or report holds a money figure, which role it needs, how far back it reaches, or why a money read came back empty, refused or short."
---

## Three finance views

- Finances 2024-06-19 `listTransactions`, under Finance and Accounting, is the current per-transaction read, with `DEFERRED`, `RELEASED` and `DEFERRED_RELEASED` transactions (P-api-1).
- Finances v0 omits deferred events until release; the Deprecation Schedule removes its event reads, not `listFinancialEventGroups` (P-api-9).
- `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`, under Finance and Accounting, is the settlement report that remains; Amazon schedules it, and it cannot be requested (P-api-15).

## Pitfalls

- `listTransactions` bounds over 180 days apart answer empty, not in error; empty pages can carry a `nextToken`; the last 48 hours may be missing (P-api-2).
- Money sits in `totalAmount` and nested `breakdowns[]`, whose `breakdownType` is an open string with no closed list (P-api-4).
- `getReports` lists only reports of the last 90 days, so through the API alone an older settlement report is not retrievable (P-api-30).

## Payouts and balances

- `listBalances` returns current or `asOfDate` balances by `balanceType`, `DEFERRED` and `ACCOUNT_LEVEL_RESERVE` among them; whether it answers in NA and FE for an ordinary seller is not yet seen on a live account (P-api-7).
- `listSummary` returns `netProceeds` with `breakdowns` for a date period or one `SETTLEMENT_ID` (P-api-8).
- Transfers `listPayouts` and `listExpectedPayouts` return past and expected payouts with status, trace id and settlement id; Role Mappings give them NA, EU and FE, the Transfers model an EU marketplace list; read in Amazon's documents, not yet seen on a live account (P-api-11).

## Products and fees

- Orders v2026-01-01 carries proceeds and the tax collection model, but no Amazon fee (P-api-20).
- Data Kiosk Economics returns per-product sales, fees by type, ads, entered costs and `netProceeds`, two years back (P-api-22).
- Its role differs by page: Brand Analytics per Role Mappings, Selling Partner Insights per Amazon's correction; a live `createQuery` decides; read in Amazon's documents, not yet seen on a live account (P-api-23).

## References

- references/questions.md: money questions, their reads, sibling skills.
- references/finances.md: Finances reads, filters, `marketplaceId`, v0.
- references/payouts.md: Transfers, `PAID`, on-demand payouts.
- references/reports.md: money report types and roles.
- references/products.md: fee estimates, orders, sales metrics, Economics.
- references/history.md: how far back each read reaches.
- references/roles-and-tools.md: roles, notifications, tools, clients.
- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
