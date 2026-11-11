# The settlement report (V2)

## Found, not requested

- Amazon states that settlement reports cannot be requested or scheduled: Amazon schedules them itself. (P-rec-1)
- The settlement report's type is `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`; Amazon generates each one, and it is found among existing reports with `getReports` rather than requested. (P-rec-1)
- `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE` and `GET_V2_SETTLEMENT_REPORT_DATA_XML` were deprecated on 2025-03-17 and are removed on 2026-11-11; the removal date had moved from 2026-03-25. (P-rec-2)
- Amazon states that calls to the removed types fail from the removal date. (P-rec-2)
- `…_FLAT_FILE_V2` is the only settlement report type left, and Amazon states there is no XML replacement. (P-rec-2)
- Settlement reports require the Finance and Accounting role. (P-rec-7)

## Columns and amounts

- V2 is tab-delimited with 24 named columns: `settlement-id`, `settlement-start-date`, `settlement-end-date`, `deposit-date`, `total-amount`, `currency`, `transaction-type`, `order-id`, `merchant-order-id`, `adjustment-id`, `shipment-id`, `marketplace-name`, `amount-type`, `amount-description`, `amount`, `fulfillment-id`, `posted-date`, `posted-date-time`, `order-item-code`, `merchant-order-item-id`, `merchant-adjustment-item-id`, `sku`, `quantity-purchased`, `promotion-id`. (P-rec-3)
- Amazon publishes the column names but no per-column or per-transaction-type definition. (P-rec-3)
- An Amazon-side acknowledgement of this on GitHub #5353 is an opinion, not an Amazon page. (P-rec-3)
- Every amount sits in the one `amount` column, classified by `amount-type` and `amount-description`. (P-rec-4)
- New fee types arrive as new values of `amount-type` and `amount-description`, not as new columns, and Amazon publishes no closed list of either. (P-rec-4)
- Amounts are written in the marketplace's local number format; Amazon's example is `95,00` for EU instead of `95.00`; how the EU and JP stores write them is read in Amazon's documents, not yet seen on a live account. (P-rec-5)
- Amazon's changelog gives `posted-date` as MM/DD/YY and `posted-date-time` as "YYYY-MM-DD HH:MM:SS UTC"; how V2 writes `posted-date` in the EU and JP stores is read in Amazon's documents, not yet seen on a live account. (P-rec-5)

## Rows that carry no order

- Per practitioners (Nova; GitHub #5291), storage, subscription, service-fee, reserve and reimbursement rows have an empty `sku`, `order-id` and `marketplace-name`. (P-rec-29)
- Per the same practitioners, filtering a settlement by SKU or by order drops those rows. (P-rec-29)
- A developer on GitHub #5353 reports FBA fee rows that carry an FBA shipment id in `order-id`. (P-rec-29)
- Practitioners report that settlement identifier columns do not always hold what their names say. (P-rec-56)
- Practitioners (Intentwise, wimoor, A2X) name the reserve rows "Current Reserve Amount" and "Previous Reserve Amount Balance". (P-rec-22)

## How far back

- Amazon retains report documents for at most 90 days, and `getReports` looks back 90 days by default, so the API cannot list a settlement report older than about 90 days; Improvado (a connector) says the same. (P-rec-6)
- Older settlements are downloadable only in Seller Central. (P-rec-6)
- Seller Central archives older settlements, and a "Request Report" click (Finance > Finance Reports > Understand Payout) regenerates one; Amazon states no archive age. (P-rec-59)
- A2X and Link My Books say the API reaches a regenerated settlement after that click, a practitioners' report not yet seen on a live account. (P-rec-59)
- Connectors cap history on their side: Link My Books 24 months for Amazon, ConnectBooks two years, A2X about 10 settlements before a history request. (P-rec-59)

## Where Seller Central shows it now

- Practitioners date the new Seller Central Finance workspace at 2026-09-21. (P-rec-35)
- Sellers report the Statement view under Finance → Manage payments, and settlement downloads as .txt or .xml under Finance → Reports Hub. (P-rec-35)
- A seller following an older path guide may not find the page. (P-rec-35)
