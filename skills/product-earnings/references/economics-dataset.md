# The Economics dataset: Amazon's own per-product net proceeds

## Net proceeds

- The Data Kiosk Economics dataset (`analytics_economics_2024_03_15`) defines a product's net proceeds as net product sales, minus the sum of Amazon fees charged, minus the sum of ad charges, minus the seller's entered per-unit cost times net units sold. (P-prof-1)
- Its per-unit net proceeds is that total divided by net units sold. (P-prof-1)
- Net product sales are ordered product sales minus refunded product sales, and refunded sales are counted by refund request time. (P-prof-2)
- Net units sold are units ordered minus units refunded. (P-prof-2)
- Because the seller's unit cost is multiplied by net units sold, a refunded unit carries no cost in Amazon's net proceeds, whether it came back sellable, damaged or not at all; this is read in Amazon's model, not yet seen on a live account. (P-prof-3)
- The `netProceeds` formula subtracts fees, ads and cost from net product sales and has no reimbursement term. (P-ref-26)

## Charges

- Each Amazon charge in the dataset totals the rate-card amount, minus its promotion amount, plus its tax amount. (P-prof-4)
- A charge's per-unit figure is its total over the charged quantity, which can be null or fractional for charges not made per unit. (P-prof-4)
- When a requested range crosses an Amazon fee-change date, the dataset returns that fee in two date ranges split at the change, with the per-unit change in `amountPerUnitDelta`. (P-prof-5)
- Amazon's release notes state that deal, coupon, removal, disposal and fuel fees were added to the dataset on 2026-09-30; their presence in a seller's results is read in Amazon's documents, not yet seen on a live account. (P-prof-13)
- Fee type names arrive as strings (`feeTypeName`), so names outside the schema's enums can appear in results; which names a seller's data carries is read in Amazon's documents, not yet seen on a live account. (P-prof-13)
- The dataset places fees such as storage, inbound placement and low-inventory fees on the SKU row as Amazon charged them; this is read in Amazon's model, not yet seen on a live account. (P-prof-31)

## Sales figures and what they net

- Amazon's sales figures differ by what they net: ad-attributed sales deduct only payment failures and quick cancellations, Economics nets refunds by refund request time, and Sales and Traffic gives ordered and shipped sales with refunds as units. (P-prof-20)

## Granularity, dates and retention

- The dataset aggregates by child ASIN, parent ASIN or SKU, and by day, week (Sunday start), month or whole range, in marketplace local time. (P-prof-6)
- Week and month ranges snap to whole weeks and months. (P-prof-6)
- A query's start can be at most two years back. (P-prof-6)
- FNSKU aggregation was removed on 2025-12-22 (SP-API Release Notes). (P-prof-6)
- Results are kept 30 days: every field carries `@resultRetention` P30D. (P-prof-7)

## The seller's costs

- The seller's own costs reach the API only as the dataset's `cost` field, all per unit: cost of goods, FBA shipping to Amazon, MFN fulfilment cost, MFN monthly storage per unit, and miscellaneous cost. (P-prof-8)
- The seller enters these costs in SKU Central or the Revenue Calculator, and each field is null when not entered. (P-prof-8)
- No SP-API operation writes the seller's costs. (P-prof-8)
- The schema gives one value per cost field per product and states no effective date or batch. (P-prof-9)
- The schema states no effective date, so whether a cost change rewrites past ranges is open: read in Amazon's documents, not yet seen on a live account. (P-prof-9)
- Costs typed into the Revenue Calculator are not saved; it recalculates net profit each time a field changes. (P-prof-10)
- A seller on Seller Forums reports that cost of goods reached SKU Economics only once entered in SKU settings. (P-prof-10)

## Forward and simulated

- `economicsPreview` previews fees per SKU for a range starting today and ending at most 120 days ahead. (P-prof-11)
- `economicsSimulation` simulates only AWD and Ships in Product Packaging, for up to 100 products and 90 days ahead. (P-prof-11)
- Its stated defaults are the past 90 days' weekly sales, 12 weeks of sales sent to AWD, a 1-week lead time, 20 units per carton, and the listing's own price and shipping. (P-prof-11)

## Role

- Amazon's correction of 2024-07-02 says the Economics dataset requires the Selling Partner Insights role, while Role Mappings and the Data Kiosk API page list Brand Analytics as the one required role for every Data Kiosk operation; this is read in Amazon's documents, not yet seen on a live account. (P-prof-12)
- The Data Kiosk API page says Data Kiosk checks the requester's roles for each field when the query is created, so the `createQuery` reply shows which role applies to a seller's app. (P-prof-12)
