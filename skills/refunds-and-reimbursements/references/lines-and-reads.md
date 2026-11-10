# Refund, claim and reimbursement lines and the reads that carry them

## Finances v2024-06-19 `listTransactions`

- `listTransactions` needs the Finance and Accounting role. (P-ref-23)
- It answers empty for a date range wider than 180 days and may leave out the last 48 hours. (P-ref-23)
- It includes deferred transactions unless filtered. (P-ref-23)
- Its `transactionType` is documented only as `Shipment`, and its `breakdownType` is an open string. (P-ref-23)
- It filters only by `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`. (P-ref-23)
- `SETTLEMENT_ID` is not a filter on it: a release note of 2026-07-29 announced it, the model added it on 2026-10-28 and the "Finance API Rollback" of 2026-10-29 removed it; it filters `listSummary` and still appears as a related identifier in responses. (P-ref-23)
- Listing by `ORDER_ID` finds refunds, chargebacks and adjustments that post days to months after the order. (P-ref-23)
- Public pulls show `transactionType` values beyond the model, such as `Refund`, `Retrocharge`, `ServiceFee`, `Adjustment`, `Compensation`, `Chargeback` and `FBAInventoryReimbursement`. (P-ref-34)
- Amazon answered one developer that a reimbursement's breakdown tree "does not appear to be documented as expected behavior". (P-ref-34)

## Finances v0

- `listFinancialEvents`, `listFinancialEventsByOrderId` and `listFinancialEventsByGroupId` were deprecated on 2025-07-21 and are removed on 2027-08-27; `listFinancialEventGroups` is not on that schedule. (P-ref-24)
- In v0, deferred events appear only once released. (P-ref-24)
- The model's `AdjustmentType` list has eight values; the four that are not India- or Easy Ship-only are `FBAInventoryReimbursement`, `ReserveEvent`, `PostageBilling` and `PostageRefund`. (P-ref-21)
- Practitioners' responses and settlement files show further names, such as `ReserveDebit`, `ReserveCredit`, `WAREHOUSE_DAMAGE` and `REVERSAL_REIMBURSEMENT`, that appear nowhere in the model, so the list is open in practice. (P-ref-21)
- The `PostageBilling_*`, `PostageRefund_*` and `ReturnPostageBilling_*` families seen in responses are reported to carry no order id or SKU. (P-ref-34)

## Joins from a refund to its order

- Refunds, guarantee claims and chargebacks carry `OrderAdjustmentItemId` in v0. (P-ref-22)
- In v2024-06-19 they carry `ORDER_ID` / `REFUND_ID` related identifiers and an `ORDER_ADJUSTMENT_ITEM_ID` item identifier. (P-ref-22)
- The settlement V2 report carries `adjustment-id` and `merchant-adjustment-item-id`. (P-ref-22)

## Settlement V2 values

- In public mapping files and vendor glossaries, settlement refund rows carry `ItemPrice`, `ItemFees`, `Promotion` and `ItemWithheldTax` parts under `amount-type`. (P-ref-33)
- In the same public files, reimbursements arrive as `other-transaction` / `FBA Inventory Reimbursement` with a reason in `amount-description`. (P-ref-33)
- Amazon publishes no list of `amount-type` or `amount-description` values, so the values are read from the seller's file. (P-ref-33)

## Data Kiosk

- Data Kiosk economics `netProceeds` subtracts fees, ads and cost from net product sales; its formula has no reimbursement term. (P-ref-26)
- Data Kiosk economics counts `refundedProductSales` "by refund request time". (P-ref-25)

## Roles

- Through the door's roles: Finances and the settlement V2 report (Finance and Accounting only), the reimbursements, FBA returns and removal reports (Pricing or Amazon Fulfillment), the Prime returns and flat return-attribute reports (Pricing), and Data Kiosk Sales and Traffic and seller analytics (Brand Analytics). (P-ref-28)
- That the reimbursements, FBA returns and removal reports answer on Pricing without Amazon Fulfillment is read in Amazon's documents, not yet seen on a live account. (P-ref-28)
- The role for Data Kiosk Economics is open: Role Mappings and the Data Kiosk page say Brand Analytics, while Amazon's correction page (2024-07-02) says "The Economics dataset requires the Selling Partner Insights role"; read in Amazon's documents, not yet seen on a live account. (P-ref-28)
- The ledger and FBA replacements reports need Amazon Fulfillment. (P-ref-28)
- Seller-fulfilled returns by return date need Inventory and Order Tracking or Direct-to-Consumer Shipping (restricted roles), and the Support API needs Selling Partner Support (restricted). (P-ref-28)

## What no operation does

- No SP-API operation issues a refund, files a reimbursement, SAFE-T or A-to-z claim, represents a chargeback, sets returnless or partial-refund rules, or enters a sourcing cost; those happen only in Seller Central. (P-ref-29)
- The Support API reads cases and creates none. (P-ref-29)
- Amazon's own plugin skill `support-case-helper` calls no SP-API tool and points to the Help Center. (P-ref-29)
- ../money-reads/SKILL.md: each read's role, window and lag across the package.
