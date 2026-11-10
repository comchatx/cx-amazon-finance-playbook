# Amazon's other profit, sales and fee views

## Profit Analytics

- Amazon's own profit view in Seller Central is Profit Analytics, reached at Reports → Selling Economics and Fees. (P-prof-14, P-tool-2)
- It shows ASIN-, SKU- and parent-level profitability over the past two years and the next 90 days, with off-Amazon costs and price simulation. (P-prof-14)
- It counts selling, fulfilment, storage, return processing, removal and disposal fees, Sponsored Products, deals and coupons, and tax when selected. (P-prof-14)
- Amazon's US 2027 fee letter (2026-11-05) names a Fee Change Comparison dashboard in Profit Analytics. (P-prof-14)
- Amazon announced it on 2025-09-17 as "introduced … this year" and reachable then; the News post naming the Reports path is dated 2025-11-13. (P-prof-14, P-tool-2)
- No SP-API operation serves the Profit Analytics dashboard. (P-prof-14)
- Trade press (PPC Land, 2025-09-20) dates it 2025-09-18 and reports that it combines sales, returns, fees, advertising and seller-provided costs into "Net Proceeds". (P-tool-2)
- The same trade press reports that it runs "1-2 days behind", with some fee data "up to 7 days". (P-tool-2)
- The same trade press reports that it accepts seller inputs for cost of goods, per-unit storage, shipping, packing, LTL freight and off-Amazon ad spend. (P-tool-2)

## SKU Economics

- SKU Economics on SKU Central "collects fees, sales, ads, off-Amazon costs, and net proceeds in a single view", at the FNSKU, MSKU, ASIN and parent-ASIN level (Amazon News post). (P-tool-1)
- SKU Economics shows the same net proceeds as the Economics dataset. (P-prof-15)
- Its per-unit fee divides fees charged in the period by net units sold in the period. (P-prof-15)
- Amazon staff note that the units charged a fee in a period can differ from the net units sold in it: an item sold in one month and shipped in the next is "charged FBA fees" in the next. (P-prof-15)
- Amazon staff note that the SKU Economics card "may not include taxes on some fees, while other reports do". (P-prof-15)

## Sales without fees or costs

- `getOrderMetrics` gives units, order items, orders, ordered product sales and average unit price per interval, for one marketplace. (P-prof-16)
- `getOrderMetrics` filters by ASIN or SKU (not both), fulfilment network, buyer type and Amazon program, and carries no fees, refunds or costs; its role is Product Listing (NA, EU). (P-prof-16)
- Sales and Traffic (Data Kiosk 2024-04-24 and `GET_SALES_AND_TRAFFIC_REPORT`, role Brand Analytics) gives ordered and shipped product sales, units refunded and refund rate per ASIN or date, with no fees or costs. (P-prof-17)

## Per-transaction product charges

- A Finances 2024-06-19 transaction names its product in `items[].contexts` as a `ProductContext` (ASIN, SKU, quantity shipped, fulfilment network). (P-prof-18)
- Since 2026-01-28 `listTransactions` can list one order's transactions by order id; its role is Finance and Accounting. (P-prof-18)

## Fee estimates at a price

- Amazon's fee estimate at a price (Product Fees API) is "not guaranteed" and uses catalog dimensions when asked by ASIN. (P-prof-19)
- The estimate takes no coupon input and carries no storage, placement, returns processing or aged-inventory share. (P-prof-19)

## Dates in Seller Central reports

- In the stores named on Amazon's page *Payment reports update* (News_Amazon), the Date/Time column of Seller Central's Transaction reports shows the posted date, not the release date, with a deferred/released column; the stores and the start date are read on that page. (P-prof-38)
- For other stores no operation or page read gives this; research/areas/product-profit.md, P-prof-38, holds the value as read. (P-prof-38)
- Seller Central's Date Range reports have no API. (P-prof-38)

## Currency and VAT in Amazon's words

- Amazon Currency Converter for Sellers converts at its provider's rate on the day the transfer to the bank is initiated, not at the order's date. (P-prof-21)
- The rule is on Amazon's page *Amazon Currency Converter for Sellers (ACCS)*, and the conversion applied to each of the seller's payouts is in Finances v0 `listFinancialEventGroups` (`OriginalTotal`, `ConvertedTotal`, `FundTransferDate`). (P-prof-21)
- Amazon's EU prices are VAT-inclusive, with the VAT-exclusive price derived from them (*VAT Calculation Service guide*). (P-prof-22)
- Under the marketplace deemed-supplier rules (EU and UK, 2021), Amazon is liable for VAT on some sales and the seller on others (the UK rule per GOV.UK; the EU rule seen only in summaries and an Amazon staff reply, as snippets). (P-prof-22)
- ../tax-lines/SKILL.md: deemed-supplier VAT Amazon withholds.
- Per sold item, Orders v2026-01-01 `getOrder` and `searchOrders` carry `taxCollections[]` (`model`, `responsibleParty`) and `taxCalculationBreakdowns[].reportingScheme`, which show whether Amazon withheld and remitted the tax; the UK rule is on GOV.UK *VAT and overseas goods sold to customers in the UK using online marketplaces*. (P-prof-22)

## Amazon's agents

- Amazon's own Claude plugin (1.0.0) has no profit skill, and its eval expects the answer that a per-unit margin metric is not available. (P-prof-37)
- Amazon's Seller Assistant pages read show no profit-per-ASIN job. (P-prof-37)
- Profit on a stated basis is what paid MCP servers and ERPs sell (Sellerboard, Helium 10, 领星, 赛狐, 船长BI, AgentXray, DataDoe, Novadata). (P-prof-37)
