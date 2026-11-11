# FBA inventory reimbursements

## What is covered

- FBA inventory reimbursement covers units lost or damaged in a fulfilment centre, shipments missing from inbound, and removals lost or damaged. (P-ref-12)
- It covers customer returns that were refunded but not returned, or returned unsellable through Amazon's fault. (P-ref-12)
- Returns damaged by the customer are not reimbursed. (P-ref-12)
- Accounts in blocked, terminated or fraud status are not reimbursed. (P-ref-12)
- In the US, units in shipments created from 2026-01-01 that arrive without proper prep and labelling and are then damaged or untraceable are not reimbursed. (P-ref-12)
- From 2026-03-31, when commingling ends, stock that is not correctly labelled may be untraceable and not eligible for reimbursement (Amazon's Chinese pages). (P-ref-38)

## Paid without a claim

- Amazon reimburses most warehouse-lost, warehouse-damaged and customer-return cases without a claim, and records them in the Reimbursements report. (P-ref-13)
- Every removal claim is still filed manually. (P-ref-13)
- The IDR portal leaves out missing-from-inbound, removals and warehouse disposals. (P-ref-13)
- Amazon states the start of this automation twice, 2024-11-01 (News post of 2024-07-24) and 2025-01-15 (News post of 2024-10-10), and no page says which store each addresses: read in Amazon's documents, not yet seen on a live account. (P-ref-13)
- Amazon's Chinese pages say the IDR portal covers warehouse lost, warehouse damaged and customer-return defects, with three statuses: eligible to file, resolved, and in review. (P-ref-37)
- The Chinese FBA FAQ says warehouse-damaged units cannot be removed and are reimbursed automatically and written off. (P-ref-37)

## Valuation

- Since 2025-03-31, a unit lost or damaged before a customer order is reimbursed at the seller's sourcing ("manufacturing") cost: the cost of sourcing or making the item, excluding shipping, handling, customs duties and other costs. (P-ref-14)
- Amazon applies its own estimate unless the seller enters a cost on Manage Your Sourcing Cost. (P-ref-14)
- A unit lost or damaged after a customer order is reimbursed at the order's sale price minus applicable fees. (P-ref-14)
- A unit that was unsellable when lost is reimbursed at "a reduced estimated cost". (P-ref-14)
- These valuation rules are read in Amazon's documents, not yet seen on a live account. (P-ref-14)
- The 2025-03-31 date replaced the announced 2025-03-10. (P-ref-15)
- The page Amazon first called Manage Your Manufacturing Cost is now Manage Your Sourcing Cost. (P-ref-15)
- No SP-API operation enters a sourcing cost. (P-ref-29)

## The policy text

- Amazon's redlined US policy PDF (created 2024-12-18) says Amazon may replace a lost or damaged unit "with a new item of the same FNSKU" instead of paying. (P-ref-40)
- It says Amazon may reverse a reimbursement made in error or for a unit later found. (P-ref-40)
- It says found reimbursed units may be sold through Amazon Warehouse or other channels. (P-ref-40)
- It values a customer-return claim at "the refund amount or the sales price of the replacement item on the original order minus applicable fees". (P-ref-40)
- It defines post-order estimated proceeds as an estimated sale price, built from median prices and current list prices, "minus referral fees and fulfillment fees". (P-ref-40)
- It states a per-unit reimbursement cap, a window for disputing a valuation after the reimbursement is issued, and that a repeat cost dispute within a stated period with no new information may be declined. (P-ref-40)
- The cap and the dispute windows are read from Amazon's page FBA inventory reimbursement policy (G200213130) as the seller's own store shows it; no SP-API operation gives them. (P-ref-40)
- The PDF predates the move of the effective date to 2025-03-31. (P-ref-40)

## Cash or units

- A reimbursement is paid in cash, as units put back in stock, or both, in the report's `quantity-reimbursed-cash`, `quantity-reimbursed-inventory` and `quantity-reimbursed-total`. (P-ref-17)

## Reversals

- Amazon reverses a reimbursement when it was paid in error or when the lost unit is found and returned to stock. (P-ref-18)
- A reversal row links to what it reverses through `original-reimbursement-id` and `original-reimbursement-type`. (P-ref-18)
- Sellers report reversals more than a year after payment, with no matching found unit in the ledger. (P-ref-18)
- Amazon's reimbursement policy text says reimbursed units, including units found after reimbursement, may be sold "on Amazon warehouse or other channels"; Amazon Warehouse was renamed Amazon Resale in August 2024. (P-ref-50)

## Claim windows, page by page

- A claim window is a dated fact, and Amazon's pages state different windows. (P-ref-16)
- News posts of 2024-07-24 and 2024-10-10 and an EU post of 2025-01-15 give one set: fulfilment-centre lost or damaged, counted from the loss report; customer returns, a band after the customer refund or replacement date; removals lost in transit, counted from shipment creation; other removals, counted from delivery back to the seller. (P-ref-16)
- A News post of 2025-08-14, effective 2025-10-15, gives another set, adds removal grading and re-evaluation windows, and names no missing-from-inbound window. (P-ref-16)
- An Amazon staff post of 2026-08-13 gives a third set, with a missing-from-inbound window that opens once the shipment is closed. (P-ref-16)
- Policy text relayed by a seller on 2025-04-14 says a unit not returned within a stated period after the refund is reimbursed. (P-ref-16)
- Amazon's policy PDF of 2024-12-18 counts the valuation-dispute window from the issue of the reimbursement. (P-ref-16)
- Amazon's Chinese pages (gs.amazon.cn, 2025-03 and 2025-08) state a US missing-from-inbound window counted from delivery to the fulfilment centre. (P-ref-37)
- The Chinese FBA FAQ says the original unit of a free replacement order must reach the warehouse within a stated period, or Amazon reimburses under the policy. (P-ref-37)
- Which of these windows Amazon's claim forms enforce is read in Amazon's documents, not yet seen on a live account. (P-ref-16)
- The windows are read from Amazon's page FBA inventory reimbursement policy (G200213130) as the seller's own store shows it and from the latest Seller Forums News post on claim windows; no SP-API operation gives a window. (P-ref-16, P-tool-22)
- research/areas/refunds-reimbursements-adjustments.md, P-ref-16, holds each page's figures as read.
- Helium 10's 2024 blog gives a customer-returns window that differs from Amazon's US notices; the blog predates the windows taking effect, and whether Amazon's wording changed in between was not established. (P-tool-22)
- GETIDA and Helium 10 MRS still advertise long audit look-backs after Amazon shortened the windows (2024-10-23; revised 2025-10-15). (P-tool-22)

## The Reimbursements report

- `GET_FBA_REIMBURSEMENTS_DATA` can only be requested and is updated daily. (P-ref-19)
- Its columns: `approval-date`, `reimbursement-id`, `case-id`, `amazon-order-id`, `reason`, `sku`, `fnsku`, `asin`, `product-name`, `condition`, `currency-unit`, `amount-per-unit`, `amount-total`, `quantity-reimbursed-cash`, `quantity-reimbursed-inventory`, `quantity-reimbursed-total`, `original-reimbursement-id`, `original-reimbursement-type`. (P-ref-19)
- It needs the Pricing or Amazon Fulfillment role; that it answers on Pricing without Amazon Fulfillment is read in Amazon's documents, not yet seen on a live account. (P-ref-19, P-ref-28)
- Amazon publishes no list of its `reason` values. (P-ref-19)
- Values seen in one public India report and in audit code are `CustomerReturn`, `CustomerServiceIssue`, `Lost_Warehouse`, `Damaged_Warehouse`, `Lost_Inbound`, `Damaged_Inbound`, `Lost_Outbound`, `Damaged_Outbound`, `ReturnAdjustment` and `Reimbursement_Reversal`. (P-ref-35)
- On reversal rows, `original-reimbursement-type` names the reason being reversed. (P-ref-35)
- A reimbursement ties back to its cause through `amazon-order-id` (customer-return and post-order cases), `case-id` (manual claims), `fnsku` / `sku` / `asin` (the unit), and `reimbursement-id` with `original-reimbursement-id` (reversals). (P-ref-20)

## The same reimbursement in other reads

- Practitioners' sources (wording not confirmed against Amazon) show the ledger naming a loss by a one-letter `Reason`, the Reimbursements report by a CamelCase `reason`, and the settlement report and Finances by UPPER_SNAKE descriptions. (P-ref-36)
- Practitioners match ledger `M` (misplaced) to `Lost_Warehouse` and `E` / `H` to `Damaged_Warehouse` by FNSKU and currency, and say no event id links them. (P-ref-36)
- Ledger `F` / `N` (found) and the reconciliation outcome "Reimbursed" are the ledger side of a reimbursement or its reversal, in practitioners' reading. (P-ref-36)
- In the settlement report, reimbursements arrive as `other-transaction` / `FBA Inventory Reimbursement` with a reason in `amount-description` (`WAREHOUSE_LOST`, `WAREHOUSE_DAMAGE`, `MISSING_FROM_INBOUND`, `REVERSAL_REIMBURSEMENT`, `COMPENSATED_CLAWBACK`, `FREE_REPLACEMENT_REFUND_ITEMS`, …), values seen in public files. (P-ref-33)
- In Finances v0 the model's reimbursement type is the `AdjustmentType` `FBAInventoryReimbursement`. (P-ref-21)
- In Finances v2024-06-19 public pulls show `FBAInventoryReimbursement` as a `transactionType`, with the reason in `description`. (P-ref-34)
