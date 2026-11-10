# How far back each money read reaches

## Finance reads

- Of the API finance reads, only v0 `listFinancialEventsByGroupId` states a history limit, "the past two years", with an empty response past it (P-api-33).
- `listTransactions`, `listFinancialEvents`, `listFinancialEventsByOrderId`, `listFinancialEventGroups`, `listBalances` (`asOfDate`), `listSummary` and `listPayouts` state no earliest date; where a limit is stated, it is a 180-day span per call; read in Amazon's documents, not yet seen on a live account (P-api-33).
- Amazon states that settlement reports "cannot be requested or scheduled" and that `getReports` lists reports of the last 90 days, so through the API alone a settlement report is retrievable only inside that window (P-api-30).
- The Deferred Transaction Report covers up to 10 years but lists only what is deferred when it is generated; `listBalances` with `asOfDate` and `balanceType=DEFERRED` gives the deferred amount at a past date (P-api-35).

## Product and order reads

- The Economics, Sales and Traffic and Seller Analytics datasets take a start "no more than two years ago" (P-api-34).
- `GET_SALES_AND_TRAFFIC_REPORT`, the Orders API and the order reports ("less than two years old") stop at two years (P-api-34).
- The Orders API v2026-01-01 description in its model, which `searchOrders` and `getOrder` carry, names the marketplaces whose order data reaches back further (P-api-34).
- Data Kiosk results are kept 30 days (P-api-34).
- The Inventory Ledger detail holds 18 months of unit movements (P-api-34).

## Seller Central views

- Amazon staff posts of 2024 give how far back the Transaction view reaches, and how long a span, how early a start and how long a wait a Date Range report takes; the values are read in Quick Tip: Payments Dashboard – Transaction View and Where to find your Amazon selling reports, and are not yet seen on a live account in the 2026 Finance workspace (P-api-32).
- Amazon states that Date Range reports for periods before 2025-01-01 keep the prior format; read in Amazon's documents, not yet seen on a live account (P-api-32).
- Nova's figures for the Transaction view, Date Range reports and settlements disagree with Amazon's staff posts (P-api-32).

## Archived settlements

- Accounting connectors state that Amazon archives older settlement reports after a period, which Link My Books and Dext give one way and Webgility another; no Amazon page read gives it, and research/method/finance-surface.md, P-api-31, holds the values as read (P-api-31).
- A2X, Link My Books, ConnectBooks and Blue Onion state that a "Request Report" click in Seller Central (Payments, All Statements; in the 2026 Finance workspace, Finance Reports, "Understand Payout") regenerates a Flat File V2 for that period, after which their API imports work (P-api-31).
- Dext says the report is archived again later, and A2X says settlement history reaches back to the account's start (P-api-31).
- Improvado says older settlements are "no longer retrievable from the API at all", against the connectors above (P-api-31).
- Lingxing's settlement center syncs only the last three months, which Lingxing puts down to the SP orders interface and Amazon's settlement report retention (P-api-38).
- Lingxing accepts uploaded Seller Central transaction and summary reports and compares them with its API data (P-api-38).
- ManageByStats rebuilds older history from Date Range Transaction reports the seller generates (P-api-38).
- Paid tools cap history by plan tier, Link My Books and Nova among them (P-api-38).

## Tax documents

- Amazon states no number of years for the Tax Document Library (P-api-37).
- Amazon Pay's 1099-K FAQ states that 1099-K forms are found by year ("Select the appropriate year"), by the primary user only (P-api-37).
- Amazon's `finance-month-end-closer` states no look-back window (P-api-37).
- A VAT transaction report generated again for the same range "can return updated records", marked by `transaction_update_date` (P-api-36).
