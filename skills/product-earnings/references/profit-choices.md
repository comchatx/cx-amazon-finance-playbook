# The counting choices inside a product's profit

## Two profits

- Seller profit tools keep two profits: an order-date operational profit, estimated until Amazon posts the charges, and a settlement- or release-date financial profit that matches statements. (P-prof-27)
- Vendors document that the two differ by data source, date basis, non-sale transactions (returns, counts, removals), ad source and custom fees. (P-prof-27)
- Most tools' order-time "sales/order profit" includes unshipped orders, and their settlement-time "financial profit" includes only shipped, settled orders; 赛狐 states this as the cause of their disagreement. (P-tool-27)
- Sellerboard separates Profit from a Cashflow module: "Profit shows performance; Cashflow shows liquidity and timing". (P-tool-27)
- Sellers have publicly reported large gaps between SKU Economics and their tool's profit for the same ASIN; the documented causes are basis, refund dating, which charges sit on the product, cost method, currency and VAT. (P-prof-40)

## Date basis

- 领星 dates its order profit (订单利润) by order time; its profit report offers settlement time (the default), settlement time with pre-settlement (预结算), and ship time (new on 2026-08-13, read from the Transaction report's Date/Time). (P-tool-3)
- 赛狐 offers settlement, expected settlement, transfer and order time, with a settlement or ship basis in its order view. (P-tool-3)
- 积加 keeps settlement time for its financial profit and API real time for its sales profit. (P-tool-3)
- SellerLogic offers order creation date or transaction date. (P-tool-3)

## Refund dating

- Tools date refunds by refund or posting date (积加, My Real Profit, Nova), by the original order (a 领星 setting; A2X says Sellerboard), or by the settlement that processes them (A2X). (P-prof-28)
- Amazon's Economics dataset counts refunds by refund request time. (P-prof-28)

## Cost method

- Tools offer FIFO batches (Sellerboard, InventoryLab, Nova, 领星, 赛狐), moving weighted average (领星), average or blended cost (A2X, Finaloop, Sellerboard), dated cost periods (Jungle Scout, Sellerboard) and fixed values (领星, 赛狐). (P-prof-29)
- Some tools recalculate past orders when a cost changes (Sellerboard, 领星); others apply a change only forward (SellerApp). (P-prof-29)
- 领星 offers moving weighted average or FIFO, and switching "requires recalculating all months" (需要将所有月份重算). (P-tool-11)
- 积加 offers FIFO or custom cost, and 赛狐 FIFO or fixed. (P-tool-11)
- Sellerboard offers FIFO, weighted average or by period: "Historical orders are recalculated accordingly". (P-tool-11)
- Finaloop runs FIFO from purchase orders with landed cost; Jungle Scout takes "Effective From" dated costs. (P-tool-11)
- Amazon's own SKU Central cost is one value per field per product, with no effective date or batch. (P-prof-9)

## Inbound freight and landed cost

- Practitioners spread inbound freight by volume or by actual, volumetric, chargeable or carton weight, keep duty on the SKU it was assessed on, spread insurance by value, and divide by the batch's actual units. (P-prof-30)
- ConnectBooks names spreading by unit count as the commonest importing error. (P-prof-30)
- 领星 allocates inbound freight (头程) per shipment by chargeable weight, actual weight, volumetric weight, quantity or custom (计费重，实重，体积重，数量，自定义), including logistics, taxes, port and clearance fees. (P-tool-10)
- 易仓 added equal allocation by quantity (2025-07). (P-tool-10)
- Sellerboard lets inbound shipping be imported and distributed, or folded into cost of goods. (P-tool-10)

## Shared Amazon charges

- Tools differ on account-level charges: kept off product rows (Helium 10), or spread by sales share (领星 default, Nova for subscription, 易仓), units (领星 option, ManageByStats), storage share (易仓), equally or by product or brand (ManageByStats), or over the month's days (Sellerboard, 赛狐). (P-prof-31)
- Sales share is the default key in 领星 (base FBA sales plus FBM sales, "FBA销售额+FBM销售额") and 积加, which does not spread on a day with no sales or units. (P-tool-9)
- 赛狐 offers FBA sales share, FBA+FBM sales share, monthly-storage-report share, long-term-storage share and custom ASINs. (P-tool-9)
- 店小秘 offers units, sales, volume or weight share. (P-tool-9)
- Sellerboard can spread storage "evenly across each day of the month", and 积加 spreads last month's storage daily over this month. (P-tool-9)
- Helium 10 leaves storage and Sponsored Brands at account or campaign level (snippet). (P-tool-9)

## Storage timing

- Storage can be booked in the month Amazon bills it or in the month it was incurred (领星 offers both), and the two place the same charge in different months. (P-prof-32)

## Ads not tied to one product

- In the tools read, Sponsored Products spend maps to the advertised SKU. (P-prof-33)
- Sponsored Brands and Display spend is kept at account or brand level (Helium 10, ConnectBooks), split equally across the creative's ASINs (My Real Profit, SellerSpace), split by sales share (Tool4seller, Eightx fallback) or assigned to the campaign's ASINs (领星). (P-prof-33)
- ConnectBooks notes that the ad report and the charge Amazon bills can differ, and that ad charges are billed both inside settlements and on cards. (P-prof-33)

## Currency

- Tools convert currency at different rates: the period's last day (Sellerboard), a monthly custom rate inherited when not edited (领星), or the live rate with costs at their last recalculation (积加). (P-prof-34)
- Amazon's own conversion is at payout. (P-prof-34)

## VAT

- Tools show sales excluding VAT with a tax-inclusive option (领星, 赛狐, Sellerboard "net sales"). (P-prof-35)
- Sellerboard can treat VAT on fees as recoverable and add VAT to ad costs. (P-prof-35)
- Profit Analytics includes tax "when selected", and Economics adds each charge's tax into its total. (P-prof-35)

## What "gross profit" holds

- Names of profit lines differ by tool: 积加 puts storage and ads below sales gross profit (销售毛利) in sales net gross profit (销售净毛利); Eightx's CM1/CM2/CM3 separate landed cost of goods, variable fulfilment and marketing. (P-prof-36)
- Sellerboard's P&L runs gross profit → Amazon fees → advertising → contribution margin → net profit, and every field of 领星's gross profit (毛利润) is switchable. (P-prof-36)
- Sellerboard's Gross Profit already subtracts advertising and Amazon fees; Webgility's gross profit is revenue minus cost of goods only, with fees and advertising in a separate "cost of sales". (P-tool-12)
- Jungle Scout's gross profit subtracts order fees but not company-level seller fees (snippet). (P-tool-12)
- ROI denominators differ: SellerApp uses cost of goods; 领星 uses purchase cost plus first-leg cost. (P-tool-12)

## What relieves inventory

- A cost-of-goods posting built from the units in a settlement relieves inventory only for sold units, and refunded units where the tool supports it. (P-prof-46)
- Lost, damaged, disposed and removed units are in no settlement's units. (P-prof-46)
- Details by tool are in references/stock-and-landed-cost.md.

## Import tax in landed cost

- Practitioners keep import VAT, GST and import consumption tax out of landed cost for a registered importer who recovers it, and in it for a seller who cannot recover it, while customs duty stays in cost. (P-prof-50)
- Details by country are in references/import-tax.md.
