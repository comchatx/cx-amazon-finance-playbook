---
name: product-earnings
description: "What one Amazon product earned after Amazon's charges and the seller's own costs: Amazon's net proceeds per ASIN, parent or SKU (Data Kiosk Economics and economicsPreview, SKU Economics, Profit Analytics, the Revenue Calculator), sales from getOrderMetrics and Sales and Traffic, per-order product charges in listTransactions, cost of goods entered in SKU Central, landed cost (freight, duty, tariffs and de minimis, IEEPA refunds, whether import VAT is a cost), Inventory Ledger units joined to the seller's cost for month-end stock value, and the counting choices profit tools make (order or settlement date, refund dating, FIFO or average cost, shared fee and ad allocation, exchange rate, VAT, what gross profit holds). For any question about a product's or SKU's profit, margin, ROI, net proceeds, COGS, unit economics or inventory value, or why SKU Economics and a profit tool show different profits."
---

## Amazon's figures

- Economics' net proceeds: net product sales minus Amazon fees, ads and unit cost times net units sold. (P-prof-1)
- Net product sales: ordered minus refunded sales, refunds by request time. (P-prof-2)
- So a refunded unit carries no cost in Amazon's net proceeds, returned or not; read in Amazon's model, not yet seen on a live account. (P-prof-3)
- In Economics a charge is rate card minus promotion plus tax, split at a mid-range fee change. (P-prof-4, P-prof-5)
- Seller costs reach the API only as Economics `cost`: five per-unit fields set in SKU Central or Revenue Calculator, null if unset. (P-prof-8)
- The schema's cost is undated and silent on whether changing it rewrites past ranges; read in Amazon's documents, not yet seen on a live account. (P-prof-9)
- Economics' role: Selling Partner Insights per Amazon's 2024-07-02 correction, Brand Analytics per Role Mappings; read in Amazon's documents, not yet seen on a live account. (P-prof-12)
- SKU Economics shows the dataset's net proceeds; its per-unit fee is period fees over period net units, which Amazon staff note can differ from units charged. (P-prof-15)
- No operation serves Profit Analytics. (P-prof-14)
- A `listTransactions` transaction names its product in a `ProductContext`. (P-prof-18)

## Tool choices

- Most tools keep an order-date profit, estimated until charges post, and a settlement- or release-date one; differing, per vendors, by data source, date basis, non-sale transactions, ad source and custom fees. (P-prof-27, P-tool-27)
- Tools date refunds by refund, original order or settlement. (P-prof-28)
- Cost: FIFO, average, dated periods or fixed; on a change some tools recalculate past orders, others go forward only. (P-prof-29, P-tool-11)
- Account-level charges: off product rows, or spread by sales, units, storage or days. (P-prof-31, P-tool-9)
- Practitioners keep recoverable import VAT out of landed cost, duty in. (P-prof-50)

## References

- references/economics-dataset.md: Economics fields, preview, role.
- references/amazon-views.md: other Amazon views, currency, VAT.
- references/profit-choices.md: each choice, tools per option.
- references/stock-and-landed-cost.md: landed cost, duty, stock ledger.
- references/import-tax.md: import tax by country.
- references/research.md: published studies.
- ../fees-and-charges/SKILL.md: each Amazon charge.
- ../settlement-reconcile/SKILL.md: settlement dates.
- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
