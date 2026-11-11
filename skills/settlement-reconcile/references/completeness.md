# Shipped against settled, and how far back each face reaches

## The faces

- Amazon Fulfilled Shipments (`GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL`) takes Amazon Fulfillment, Inventory and Order Tracking or Pricing; its request cap, span per report and lag are stated on Amazon's FBA Reports page. (P-rec-55)
- Amazon's FBA Reports page states the shipments report's request cap counts requests made in Seller Central too. (P-rec-55)
- The All Orders reports cover all order statuses and fulfilment channels, take any start date, and are reached with Pricing or Product Listing; their span per report is stated on Order Reports. (P-rec-55)
- FBA Returns (`GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`) takes Amazon Fulfillment or Pricing and is updated daily. (P-rec-55)
- That the shipments and FBA Returns reports answer on Pricing without Amazon Fulfillment is read in Amazon's documents, not yet seen on a live account. (P-rec-55)
- `searchOrders` filters by `fulfillmentStatuses`, including `PARTIALLY_SHIPPED` and `CANCELLED`. (P-rec-55)
- `listTransactions` filtered by `ORDER_ID` returns the posted money of one order. (P-rec-55)
- Seller-fulfilled returns by return date (`GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE`) need Inventory and Order Tracking or Direct to Consumer Shipping (Restricted); their span per report is stated on Returns Reports. (P-rec-55)

## Identifiers that meet

- The shipments report carries `amazon-order-id`, `shipment-id`, `shipment-item-id`, `amazon-order-item-id`, `merchant-order-item-id` and `sku`. (P-rec-56)
- Settlement V2 carries `order-id`, `shipment-id`, `order-item-code`, `merchant-order-item-id`, `adjustment-id` and `sku`. (P-rec-56)
- v0 `ShipmentEvent` carries `AmazonOrderId`, with item `OrderItemId` and, for refunds, guarantee claims and chargebacks, `OrderAdjustmentItemId`. (P-rec-56)
- `listTransactions` carries `ORDER_ID`, `SHIPMENT_ID` and `ORDER_ADJUSTMENT_ITEM_ID`. (P-rec-56)
- The returns reports carry an order id and a SKU only. (P-rec-56)
- Whether a settlement's `order-item-code` equals the shipments report's `amazon-order-item-id`, and whether a split shipment posts one event per `shipment-id`, is read in Amazon's documents, not yet seen on a live account. (P-rec-56)

## A practitioner shape

- Lingxing's 发货与结算差异报告 (a vendor's report) traces each order through ship, settle and transfer. (P-rec-57)
- It carries a 发出商品 (goods shipped, not settled) balance, rolled forward as opening + shipped − shipped-and-settled − earlier-shipped-settled-now. (P-rec-57)
- It separates shipped-not-settled, settled-not-transferred and settled-not-shipped, the last rare (for example try-before-you-buy). (P-rec-57)
- Lingxing notes its shipment-report feed runs about three days late. (P-rec-57)
- A UK seller thread says cancelled orders remain in sales reports though they never complete. (P-rec-57)

## How far back each face reaches

- Report documents through the Reports API: at most 90 days (reports_2021-06-30.json). (P-rec-58)
- Date Range reports: the span per report and the earliest date are stated by Amazon staff in Where to find your Amazon selling reports. (P-rec-58)
- The Deferred Transaction report: its reach is stated on Payment Reports. (P-rec-58)
- `listFinancialEventsByGroupId`: two years (financesV0.json). (P-rec-58)
- `listTransactions` and `listFinancialEventGroups`: 180 days per call, with no earliest date stated in the models. (P-rec-58)
- Orders API: two years, with JP, AU and SG from 2016 (orders_2026-01-01.json). (P-rec-58)
- Data Kiosk: start dates up to two years back, results kept for each field's `@resultRetention`. (P-rec-58)
- Amazon Ads invoices: the consolidated statement's window is on Sponsored ads consolidated invoice statement download is now global. (P-rec-58)
- The Transaction view's horizon is given by no operation or page read; research/areas/reconciliation.md, P-rec-58, holds the value as read.
