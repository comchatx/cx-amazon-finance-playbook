---
name: product-earnings
description: "What one Amazon product earned after Amazon's charges and the seller's own costs: Amazon's net proceeds per ASIN, parent or SKU (Data Kiosk Economics and economicsPreview, SKU Economics, Profit Analytics, the Revenue Calculator), sales from getOrderMetrics and Sales and Traffic, per-order product charges in listTransactions, cost of goods entered in SKU Central, landed cost (freight, duty, tariffs and de minimis, IEEPA refunds, whether import VAT is a cost), Inventory Ledger units joined to the seller's cost for month-end stock value, and the counting choices profit tools make (order or settlement date, refund dating, FIFO or average cost, shared fee and ad allocation, exchange rate, VAT, what gross profit holds). For any question about a product's or SKU's profit, margin, ROI, net proceeds, COGS, unit economics or inventory value, or why SKU Economics and a profit tool show different profits."
---

## Amazon's figures

- Economics' net proceeds: ordered minus refunded sales (refunds by request time), minus Amazon fees, ads and unit cost times net units sold; no reimbursement term. (P-prof-1, P-prof-2, P-ref-26)
- In Economics a refunded unit carries no cost, returned or not; read in Amazon's model, not yet seen on a live account. (P-prof-3)
- Seller costs reach the API only as Economics `cost`: five per-unit fields from SKU Central or Revenue Calculator, null if unset. (P-prof-8)
- That cost is undated; whether a change rewrites past ranges is read in Amazon's documents, not yet seen on a live account. (P-prof-9)
- Economics' role: Selling Partner Insights per Amazon's 2024-07-02 correction, Brand Analytics per Role Mappings; read in Amazon's documents, not yet seen on a live account. (P-prof-12)

## Account-level charges

- Monthly storage has no order and is collected the following month; Amazon's per-product storage report estimates it. (P-ful-3)
- A period's storage and placement lines cover earlier stock; booking by posting date or covered period is a choice. (P-ful-21, P-prof-32)
- Tools keep account-level charges off product rows or spread them by sales, units, storage share or days; each key shifts products' shares. (P-prof-31, P-tool-9)

## Tool choices

- Most tools keep an order-date profit, estimated until charges post, and a settlement- or release-date one. (P-prof-27, P-tool-27)
- Tools date refunds by refund, original order or settlement. (P-prof-28)
- Cost: FIFO, average, dated periods or fixed; some tools recalculate past orders on a change. (P-prof-29, P-tool-11)
- Settlement-built cost of goods relieves sold units, and refunded ones where the tool supports it; A2X leaves unrestocked refunds to manual adjustment. (P-prof-46)
- The Inventory Ledger gives customer returns per disposition. (P-prof-41)
- ConnectBooks books a reimbursement as a recovery against the lost unit's write-off. (P-prof-47)

## References

- references/economics-dataset.md: Economics fields, charges, preview, role.
- references/amazon-views.md: SKU Economics, Profit Analytics, sales, per-order charges.
- references/profit-choices.md: each counting choice, tools per option.
- references/stock-and-landed-cost.md: landed cost, duty, stock ledger.
- references/import-tax.md: import VAT as cost, by country.
- references/research.md: published studies.
- ../fees-and-charges/SKILL.md: each Amazon charge.
- ../settlement-reconcile/SKILL.md: settlement dates.
- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
