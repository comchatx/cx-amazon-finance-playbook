# The seller's costs: landed cost, duty and stock as money

## What purchase cost and customs value include

- Under US tax rules the cost of purchased goods includes transportation and other charges of acquiring them, and inventory costing methods include FIFO, LIFO, specific identification and lower of cost or market (IRS *Publication 538*). (P-prof-23)
- No operation or page read gives another country's tax rule on the cost of purchased goods. (P-prof-23)
- US customs value, on which ad valorem duty is charged, excludes international freight and insurance (CBP *What Every Member of the Trade Community Should Know About: Customs Value*); no page read gives another import country's valuation rule. (P-prof-24)
- Under IAS 2, inventory cost includes purchase, conversion and the costs of bringing it to its present location and condition. (P-prof-45)
- China's Accounting Standard for Business Enterprises No. 1, Inventories (企业会计准则第1号), Article 6, states the same for purchase cost. (P-prof-45)

## Duty

- Tariff rates on a product change by instrument and date and are published by CBP, USTR and the Federal Register. (P-prof-26)
- The US duty-free de minimis status and its limit are on CBP's page *CBP modernizes low-value shipment processing*; research/areas/product-profit.md, P-prof-26, holds the dated suspensions (EO 14324, EO 14388, CBP's June 2026 rules) as read. (P-prof-26)
- IEEPA duty refunds go only to the importer of record or notify party, with interest, through a CAPE declaration (CBP *IEEPA Duty Refunds*). (P-prof-25)
- A seller who was not the importer of record receives no IEEPA duty refund from CBP. (P-prof-25)

## Inventory in accounting standards

- Under IAS 2 inventory is carried at the lower of cost and net realisable value. (P-prof-45)
- Under IAS 2 the carrying amount of sold inventory is expensed when the related revenue is recognised, and "all losses of inventories" and write-downs are expensed in the period they occur. (P-prof-45)
- China's standard No. 1 states lower of cost and net realisable value (Article 15) and charges damage (毁损) and count-shortage (盘亏) losses to the period's profit (Article 21). (P-prof-45)

## Amazon's units: the Inventory Ledger

- Amazon's Inventory Ledger summary (`GET_LEDGER_SUMMARY_VIEW_DATA`) is, in Amazon's words, "like a bank statement of your inventory". (P-prof-41)
- The summary gives, per FNSKU, MSKU, ASIN and disposition, by country or fulfilment centre and by day, week or month: starting warehouse balance, in transit between warehouses, receipts, customer shipments, customer returns, vendor returns, warehouse transfers, found, lost, damaged, disposed, other events, unknown events and ending warehouse balance. (P-prof-41)
- The summary is by month by default, and a monthly view needs a first-to-last-day range. (P-prof-41)
- The summary is in units only, with no cost or value column, and needs the Amazon Fulfillment role. (P-prof-41)
- The Inventory Ledger detail (`GET_LEDGER_DETAIL_VIEW_DATA`) lists each movement with event type, reference ID, quantity, fulfilment centre, disposition, reason, country, reconciled and unreconciled quantity and time, filterable by event type. (P-prof-42)
- The detail view covers 18 months of movements. (P-prof-42)
- Amazon's page does not define the reconciled and unreconciled quantities. (P-prof-42)
- The ledger replaced six inventory reports discontinued on 2022-09-30. (P-prof-42)
- Amazon does not state whether "In Transit Between Warehouses" is inside "Ending Warehouse Balance"; a seller's question on Seller Forums got only a referral to Seller Support from Amazon staff. (P-prof-43)
- A seller reply and ConnectBooks add ending balance and in-transit units for a total. (P-prof-43)
- Summary rows are split by disposition, so a sellable-only figure leaves out unsellable units. (P-prof-43)

## Units the ledger does not hold

- Units outside the ledger are counted elsewhere by Amazon, in units only and for the present moment. (P-prof-44)
- Inbound working, shipped and receiving, reserved, researching and unfulfillable units are in `getInventorySummaries` (Amazon Fulfillment or Product Listing) and the Manage Inventory reports (Pricing or Amazon Fulfillment). (P-prof-44)
- Removal units requested, in process, disposed and shipped are in the removal order and removal shipment reports (Pricing or Amazon Fulfillment). (P-prof-44)
- AWD on-hand, inbound-to-AWD and AWD-to-FBA units are in AWD `listInventory` (Amazon Warehousing and Distribution role, NA only). (P-prof-44)
- None of these carries a value, and stock at a 3PL or with the seller has no Amazon source. (P-prof-44)

## The inventory asset in practice

- A2X builds its cost-of-goods posting by multiplying "the SKUs and quantities in the settlement" by cost, moving that from the inventory asset to cost of goods sold. (P-prof-46)
- A2X has posted refunds by refund date since October 2025, with unrestocked refunds left to a manual adjustment. (P-prof-46)
- Lost, damaged, disposed and removed units are in no settlement's units. (P-prof-46)
- ConnectBooks names the result of relieving stock on financial events: "Lost or damaged items weren't removed from inventory until Amazon reimbursed you", and "Disposals and removals weren't tracked at all". (P-prof-46)
- ConnectBooks now relieves stock from the ledger on the date of the movement, and "Reimbursements no longer affect inventory counts". (P-prof-46)
- Practitioners value month-end inventory across every place the seller's units are: Amazon fulfilment centres, in transit to Amazon ("yours the moment it ships"), at a 3PL or the seller's warehouse, and lost or damaged units not yet written off or reimbursed (ConnectBooks). (P-prof-47)
- ConnectBooks writes a lost unit off once confirmed and books the reimbursement as a recovery against that loss, not as sales. (P-prof-47)
- 领星's FBA stock report takes opening stock as last month's closing stock, then adds or takes away ledger Receipts, Fulfilled Shipments, the Returns report, adjustments grouped by ledger reason, VendorReturns as removals, and WhseTransfers. (P-prof-48)
- 领星 groups adjustments by ledger reason: damaged (残损) 6/7/E/H/K/U, found (找到) F/N, lost (丢失) 5/M, disposed (弃置) D/G, other (其他) 3/4/O/P/Q. (P-prof-48)
- 领星 takes closing stock as the ledger summary's Ending Warehouse Balance, shows In Transit Between Warehouses as a separate in-transit-between-warehouses line (移仓在途), puts whatever the movements do not explain on an inventory-difference line (库存差异), and values both at the average closing cost. (P-prof-48)
- 领星 books non-sale stock movements to profit when they happen, "unrelated to settlement" (与结算无关), each switchable in its gross-profit formula: count gains and losses, ledger-vs-ERP differences, shipment shortfalls and their later receipt, over-receipts, and removals. (P-prof-49)
- 领星 moves sold units to goods shipped (发出商品) at shipment and to cost of goods sold (主营业务成本) at settlement, so its stock report's sold units and its profit report's units differ by shipped-but-unsettled orders. (P-prof-49)
- 优麦云's FIFO batches likewise take FBA count adjustments and unexplained ledger events. (P-prof-49)
