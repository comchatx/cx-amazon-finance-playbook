# Product and order reads: fee estimates, orders, sales metrics, Economics

## Product Fees estimates

- Amazon states that Product Fees estimates are "not guaranteed" (P-api-19).
- A SKU estimate (`getMyFeesEstimateForSKU`) uses measured dimensions once the item is at Amazon; an ASIN estimate (`getMyFeesEstimateForASIN`) uses the catalog size (P-api-19).
- The batch `getMyFeesEstimates` takes up to 20 items, and Role Mappings list only Pricing or Product Listing for it; whether a call under Finance and Accounting alone is refused is not yet seen on a live account (P-api-19).

## Orders

- Orders v2026-01-01 carries proceeds: the order's `grandTotal`, each item's `proceedsTotal`, and breakdowns by `ITEM`, `SHIPPING`, `GIFT_WRAP`, `COD_FEE`, `TAX`, `DISCOUNT`, `DELIVERY_TIP` and `OTHER` (P-api-20).
- Orders v2026-01-01 carries the tax collection model and payment executions, and no Amazon fee (P-api-20).
- Amazon's Deprecation Schedule removes the Orders v0 reads on 2027-03-27; the date is read on the SP-API Deprecation Schedule page (P-api-20).

## Sales metrics

- Sales `getOrderMetrics` returns ordered `totalSales`, units and orders per interval, for one marketplace, with `asin` or `sku` but not both (P-api-21).
- `getOrderMetrics` is open under Product Listing (P-api-21).
- `getOrderMetrics` stops at two years, and at hourly granularity at 30 days (P-api-34).

## Data Kiosk Economics

- Economics returns per-product sales, fees by type, ads, the seller's own entered costs and `netProceeds`, by Amazon's stated formula (P-api-22).
- Economics is refreshed daily, reaches two years back, splits a date range at fee-change dates, and its results are kept 30 days (P-api-22).
- The Economics preview reaches 120 days ahead (P-api-22).
- Amazon's pages disagree on the role for Economics: Brand Analytics per Role Mappings and the Data Kiosk page, Selling Partner Insights per Amazon's correction; the live `createQuery` result decides it; read in Amazon's documents, not yet seen on a live account (P-api-23).
