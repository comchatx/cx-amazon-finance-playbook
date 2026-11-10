# The SP-API surface for money, and what already exists to borrow

Read 2026-11-09 by the research seat. Tags: **[official]** Amazon's own page or model (title, URL, date read); **[opinion]** a named practitioner, vendor or open-source author; **[research]** published study; **[seat]** this seat's reasoning, never a position; **[command-verified]** a command run over a local or public read-only source. Local model clone: `~/ComChatX_Project/scratch/sp-api-plugins/models`, commit `db2936aa` (2026-10-29, "SPAPI October Release Finance API Rollback"). Scripts used: `/tmp/fsurf/ops.py`, `desc.py`, `defs.py`, `roles.py` (they print each model's paths, parameters, Usage Plan tables, definitions, and the Role Mappings rows).

## What this covers

This is the one table every skill of the money pack reads from. It lists every SP-API operation, report type, Data Kiosk field and notification that carries money, with:

- its path and model file;
- its rate and burst from the model's Usage Plan;
- the role Amazon's Role Mappings give it;
- its deprecation dates and the pitfalls Amazon names;
- how far back it reaches, for audit and year-end (§J, added 2026-11-10).

It then covers what already exists before cx writes anything: Amazon's own Claude plugin and MCP connector, Seller Assistant, open-source clients and pi packages. It also covers what our door `cx-amazon-sp-api` already gives a money question, and what only Seller Central shows.

It feeds every skill of the pack:

- Payouts and balances: Finances 2024-06-19, Transfers, v0 groups.
- Fees per order and per product: transactions, settlement, economics.
- Product earnings: Data Kiosk economics, Product Fees, Orders proceeds.
- The reference file on sources and roles.

Deep treatment of each area belongs to the other seats. This file gives the surface and the borrow-first answer.

**Why a senior operator cares.** Amazon has three overlapping finance generations, and each counts money differently:

- **Finances v0 events:** no deferred events, removal 2027-08-27.
- **Finances 2024-06-19 transactions:** deferred events included.
- **The settlement report:** released money only, one file per settlement.

Data Kiosk economics adds a fourth view, per product, with refunds dated "by refund request time". The Orders API adds a fifth, proceeds at order time. Someone who has done this job knows which view answers which question, which role opens each, and which dates move under them. This year the dates did move:

- the old settlement reports go on 2026-11-11, two days from today;
- the `SETTLEMENT_ID` filter was announced and then rolled back in the model.

**Dated changes since 2025-01-01** (each sourced in the sections below):

- 2025-02-26: Transfers API v2024-06-01 "now generally available".
- 2025-03-17: `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE` and `_XML` deprecated. **Removal 2026-11-11.**
- 2025-04-30: `DEFERRED_RELEASED` transaction status added. Seller Wallet API launched.
- 2025-05-28: Sales `getOrderMetrics` takes `amazonProgram=AmazonHaul`.
- 2025-06-25: `listTransactions` can filter by `transactionStatus`.
- 2025-07-21: Finances v0 `listFinancialEvents`, `…ByGroupId` and `…ByOrderId` deprecated. **Removal 2027-08-27.** `listFinancialEventGroups` is not on the schedule.
- 2025-08-27:
  - Seller Wallet API public in NA and EU.
  - Product Fees `previewContext.itemPrice` removed.
  - Data Kiosk `analytics_salesAndTraffic_2023_11_15` deprecated, removal 2026-03-27.
- 2025-12-03: `listTransactions` filter `FINANCIAL_EVENT_GROUP_ID`. Seller Wallet `payeeContactInformation` is required for `THIRD_PARTY` payees.
- 2025-12-22: Economics `FNSKU` aggregation removed.
- 2026-01-28:
  - `listTransactions` filter `ORDER_ID`.
  - v0 `EBTRefundReimbursementOnlyEventList`.
  - Orders API v2026-01-01 launched. Orders v0 deprecated, **removal 2027-03-27**.
- 2026-01-28 / 2026-02-23: Sales and Traffic dataset gains B2B refund and claim metrics.
- 2026-04-29: Orders 2026-01-01 adds `TAX` and `PAYMENT` data.
- 2026-05-27: Orders 2026-01-01 adds the proceeds `breakdowns` (incl. delivery tip). Notifications `createSubscription` takes a `filterExpression`.
- 2026-06-11 (modified 2026-07-01): Amazon cancels the planned SP-API usage and annual fees.
- 2026-07-29:
  - Finances `listSummary` and `listBalances` added.
  - The `SETTLEMENT_ID` filter on `listTransactions` announced.
  - Transfers `listPayouts` and `listExpectedPayouts` added.
  - Invoices API v2026-06-25 launched (vendors only).
- 2026-09-23: Amazon's "Amazon Selling Partner" connector and plugin for Claude, in beta, US stores.
- 2026-09-30:
  - Finance Remittance API v2026-03-17 (vendors only).
  - The Economics dataset is "updated … with deal, coupon, removal, disposal, and fuel fees" (not in the schema clone).
  - Seller Analytics dataset added.
  - Orders `purchasePrice` added.
- 2026-10-08: Amazon commits a `finance-month-end-closer` skill (version 1.3.1) to its toolkit repository `amzn/selling-partner-agentic-toolkit` (commit 11d828ad). It was merged to `main` on 2026-10-12 (PR #7, 8d90d3b7).
- 2026-10-28: the October models release (df7c6298) adds the `SETTLEMENT_ID` filter text and the `AMAZON_FBA_FROM_ORIGIN` store name to `finances_2024-06-19.json`. Neither had been in the model before.
- 2026-10-29: the models commit "Finance API Rollback" (db2936aa) removes both, the day after.

## Amazon's own rules

### A. Finances API v2024-06-19 (current; "Sellers only")

A1. `listTransactions`, `GET /finances/2024-06-19/transactions`.

- **Description:** "Returns transactions for the given parameters. Financial events might not include orders from the last 48 hours. **Note:** If you want to retrieve MFN orders in the US store, do not supply the `marketplaceId` parameter."
- **`postedAfter`:** "must be more than two minutes before the time of the request. This field is required if you do not specify a related identifier."
- **`postedBefore`:**
  - "before (but not on) this date … more than two minutes before the request was submitted."
  - "If `PostedAfter` and `PostedBefore` are more than 180 days apart, the response is empty."
  - "**Default:** Two minutes before the time of the request."
- **`nextToken`:** "Note that this operation can return empty pages."

[official] (finances_2024-06-19.json at db2936aa [command-verified]; listTransactions reference, https://developer-docs.amazon/sp-api/reference/listtransactions, updatedAt 2026-09-10, read 2026-11-09)

A2. Filters.

- `transactionStatus`: `DEFERRED` ("currently deferred"), `RELEASED`, and `DEFERRED_RELEASED`: "the transaction was deferred in the past, but is now released. The status of a deferred transaction is updated to `DEFERRED_RELEASED` when the transaction is released."
- `relatedIdentifierName` (model at db2936aa and the live reference): "`FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID` are the only `relatedIdentifier` with filtering capabilities at the moment. While other `relatedIdentifier` values will be included in the response when available, they cannot be used for filtering purposes."

[official] (same; live reference read 2026-11-09)

A3. **`SETTLEMENT_ID` as a filter: announced, then rolled back.**

- The release note of 2026-07-29 reads "Added the `SETTLEMENT_ID` value for the `relatedIdentifierName` query parameter … You can use this value to filter transactions by their settlement ID".
- The models commit `db2936aa` (2026-10-29, "SPAPI October Release Finance API Rollback") changed only `finances_2024-06-19.json`, in two ways:
  - It deleted `SETTLEMENT_ID` from the filter's list.
  - It deleted the `BusinessContext.storeName` value `AMAZON_FBA_FROM_ORIGIN` ("Transactions associated with FBA from origin"), leaving `AMAZON_HAUL`.
- The live reference agrees with the rolled-back model.
- The model never carried the filter between July and October. The July release (dcb0ef91, 2026-07-29) added only `listSummary`'s `SETTLEMENT_ID`. The filter text ("`SETTLEMENT_ID`: the settlement group ID associated with the transaction") and `AMAZON_FBA_FROM_ORIGIN` arrived in the October release (df7c6298, 2026-10-28), one day before the rollback [command-verified, patches of dcb0ef91, 4be88722, af0be99a, df7c6298 and db2936aa].
- The changelog of 2026-10-21 still announces `AMAZON_FBA_FROM_ORIGIN` "Starting 6 November 2026". The model and the reference no longer list it.
- `SETTLEMENT_ID` stays a *response* value of `RelatedIdentifier`, along with `ORDER_ID`, `SHIPMENT_ID`, `FINANCIAL_EVENT_GROUP_ID`, `REFUND_ID`, `INVOICE_ID`, `DISBURSEMENT_ID`, `TRANSFER_ID`, `DEFERRED_TRANSACTION_ID` and `RELEASE_TRANSACTION_ID`.

[official] (SP-API Release Notes, https://developer-docs.amazon/sp-api/docs/sp-api-release-notes.md, updatedAt 2026-11-04, read 2026-11-09). [command-verified] (`gh api repos/amzn/selling-partner-api-models/commits/db2936aa…` → one file changed, +2 −13; the patch was read)

A4. The `Transaction` shape [command-verified, `defs.py` over the model]:

- **`sellingPartnerMetadata`:** `sellingPartnerId`, `accountType`, `marketplaceId`.
- **`relatedIdentifiers[]`:** `relatedIdentifierName` takes the ten values in A3.
- **`transactionType`:** "**Possible value:** `Shipment`". This is the only value the model states.
- **`transactionId`.**
- **`transactionStatus`:** the three values in A2.
- **`description`:** "Describes the reasons for the transaction. **Example:** `Order Payment`, `Refund Order`".
- **`postedDate`.**
- **`totalAmount`:** a `Currency`, made of `currencyCode` and `currencyAmount`, and `BigDecimal` is "A signed decimal number".
- **`marketplaceDetails`:** `marketplaceId` and `marketplaceName`, e.g. `Amazon.com`.
- **`items[]`:**
  - `description`;
  - `relatedIdentifiers`, whose `itemRelatedIdentifierName` is `ORDER_ADJUSTMENT_ITEM_ID`, `COUPON_ID`, `REMOVAL_SHIPMENT_ITEM_ID` or `TRANSACTION_ID`;
  - `totalAmount`, `breakdowns`, `contexts`.
- **`contexts[]`:** a `contextType` plus one of the following.
  - `AmazonPayContext`: `storeName`, `orderType`, `channel`.
  - `ProductContext`: `asin`, `sku`, `quantityShipped`, `fulfillmentNetwork`.
  - `PaymentsContext`: `paymentType`, `paymentMethod`, `paymentReference`, `paymentDate`.
  - `DeferredContext`: `deferralReason`, whose "**Examples:** `B2B` (invoiced orders), `DD7` (delivery date policy)", and `maturityDate`, "The release date of the transaction".
  - `BusinessContext`: `storeName` enum `AMAZON_HAUL`.
  - `TimeRangeContext`: `startTime`, `endTime`.
- **`breakdowns[]`:** each has a `breakdownType` ("The type of charge"), a `breakdownAmount`, and a nested `breakdowns[]` of the same shape, to any depth.

A5. "breakdownType is an open-ended string; Amazon does not publish a closed list of values." The guide's table of common values is:

- `CSBAFee` ("Customer Service by Amazon fee");
- `MPFRegulatoryFee`;
- `MarketplaceFacilitatorRegulatoryFee-Principal`;
- `OurPriceRegulatoryFee`.

The page also says "The response will include transactions with statuses RELEASED, DEFERRED, and DEFERRED_RELEASED."

[official] (Get the latest transactions, https://developer-docs.amazon/sp-api/docs/get-latest-transactions.md, updatedAt 2026-09-24, read 2026-11-09)

A6. `listBalances`, `GET /finances/2024-06-19/balances`.

- **Description:** "Retrieve a balance. This balance can be a past balances at a specified date, or a current balance. Sub-balances are listed by account type and marketplace."
- **`balanceType`:** `AVAILABLE`, `RESERVED`, `TOTAL`, `DEFERRED`, `ACCOUNT_LEVEL_RESERVE`.
- **`asOfDate`:** "If provided, the response includes historical balances at the specified date … If omitted, the point in time balance is provided."
- **`lastUpdatedTime`:** "in the marketplace's local time zone".
- **`nextToken`:** given "When there are more than 500 results available".
- **Nesting:** each `Balance` nests `balances[]`, "A list of balances that comprise this balance".

[official] (model; listBalances reference, updatedAt 2026-09-10)

A7. `listSummary`, `GET /finances/2024-06-19/summary`.

- **Description:** "Retrieve the financial summary for the specified time period or settlement period."
- **`relatedIdentifierName`:** "The only possible value is `SETTLEMENT_ID`".
- **`periodStart` / `periodEnd`:** ISO dates; the summary "will only include summaries with transactions that occurred on or after / on or before the specified date".
- **`Summary` fields:** `partnerMetadata`, `netProceeds` ("The net proceeds for the summary period"), `relatedIdentifiers`, `breakdowns` ("how the net proceeds are calculated"), `periodStart`, `periodEnd`.

[official] (model; listSummary reference)

A8. Use case "Determine which transactions make up a payment":

1. Call `listFinancialEventGroups` (v0), "up to 100 financial event groups at a time".
2. Take the payment's `FinancialEventGroupId`.
3. Call `listTransactions` with `relatedIdentifierName=FINANCIAL_EVENT_GROUP_ID`, the id, and `transactionStatus=RELEASED`: "The response includes up to 500 released transactions associated with the specified financial event group."

[official] (https://developer-docs.amazon/sp-api/docs/determine-payment-transactions.md, updatedAt 2026-09-09, read 2026-11-09)

### B. Finances API v0 (legacy; three of four operations on the removal schedule)

B1. Four operations, each at 0.5 a second, burst 30 [command-verified]:

| Operation | Path | Window and paging (model) |
|---|---|---|
| `listFinancialEventGroups` | `GET /finances/v0/financialEventGroups` | `MaxResultsPerPage` 1–100, default 10. `FinancialEventGroupStartedAfter/Before` "more than 180 days apart, no financial event groups are returned". |
| `listFinancialEventsByGroupId` | `GET /finances/v0/financialEventGroups/{eventGroupId}/financialEvents` | "only retrieves a group's data for the past two years. A request for data spanning more than two years produces an empty response." Deferred events are absent "until they are released". |
| `listFinancialEventsByOrderId` | `GET /finances/v0/orders/{orderId}/financialEvents` | Deferred events are absent until released. |
| `listFinancialEvents` | `GET /finances/v0/financialEvents` | `PostedAfter/Before`: 180 days or the response is empty; "If you include the `PostedBefore` parameter … you must also specify the `PostedAfter` parameter." Deferred events are absent until released. |

- All four: "Orders from the last 48 hours might not be included in financial events." "If the response exceeds the maximum number of transactions or 10 MB, the response is `InvalidInput`." "this operation can return empty pages."
- Deprecation: `listfinancialevents`, `listFinancialEventsByGroupId` and `listFinancialEventsByOrderId` were deprecated on July 21, 2025, with removal on August 27, 2027. `listFinancialEventGroups` is not listed. None of the four carries `deprecated: true` in the model [command-verified].

[official] (financesV0.json; SP-API Deprecation Schedule, https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md, updatedAt 2026-09-09, read 2026-11-09)

B2. `FinancialEventGroup` (one per settlement period):

- `FinancialEventGroupId`.
- `ProcessingStatus`: `Open` or `Closed`.
- `FundTransferStatus`.
- `OriginalTotal`: "For a closed financial group, this is the total amount of a disbursement or a charge amount. For an open financial event group, this is the current balance".
- `ConvertedTotal`: the amount "in the currency of the marketplace in which the funds were disbursed".
- `FundTransferDate`: "Only present for closed settlements".
- `TraceId`: "used by sellers to look up transactions externally".
- `AccountTail`.
- `BeginningBalance`.
- `FinancialEventGroupStart` and `FinancialEventGroupEnd`.

[official, command-verified]

B3. The model's 34 event lists [command-verified, `len(FinancialEvents.properties) = 34`]: Shipment, ShipmentSettle, Refund, GuaranteeClaim, EBTRefundReimbursementOnly, Chargeback, PayWithAmazon, ServiceProviderCredit, Retrocharge, RentalTransaction, ProductAdsPayment, ServiceFee, SellerDealPayment, DebtRecovery, LoanServicing, Adjustment, SAFETReimbursement, SellerReviewEnrollmentPayment, FBALiquidation, CouponPayment, ImagingServicesFee, NetworkComminglingTransaction, AffordabilityExpense, AffordabilityExpenseReversal, RemovalShipment, RemovalShipmentAdjustment, TrialShipment, TDSReimbursement, AdhocDisbursement, TaxWithholding, ChargeRefund, FailedAdhocDisbursement, ValueAddedServiceCharge, CapacityReservationBilling.

B4. Value lists the model states.

- **`ChargeType`:** Principal ("selling price … multiplied by the quantity ordered"), Tax ("collected by the seller"), MarketplaceFacilitatorTax-Principal/-Shipping/-Giftwrap/-Other ("withheld"), Discount, TaxDiscount, the COD family, ShippingCharge, ShippingTax, Goodwill, Giftwrap, GiftwrapTax, RestockingFee, ReturnShipping, PointsFee, GenericDeduction ("A generic bad debt deduction"), FreeReplacementReturnShipping, PaymentMethodFee, ExportCharge, SAFE-TReimbursement, TCS-CGST/SGST/IGST/UTGST and PaidthroughEBT.
- **`AdjustmentType`:**
  - `FBAInventoryReimbursement`: "This occurs if a seller's inventory is damaged."
  - `ReserveEvent`: "generated at the time a settlement period closes. This occurs when some money from a seller's account is held back."
  - `PostageBilling` and `PostageRefund`.
  - `LostOrDamagedReimbursement` (Easy Ship).
  - India-only: `CanceledButPickedUpReimbursement`, `ReimbursementClawback`, `SellerRewards`.
- **`FeeType`:** a free string. The model sends the reader to the fee schedules G200336920 and G201074400.
- **`ProductAdsPaymentEvent`:** `transactionType` `charge`/`refund`, `invoiceId`, `baseValue`, `taxValue`, and `transactionValue` "Equal to `baseValue` + `taxValue`".
- **`ShipmentItem` adjustment lists:** `ItemChargeAdjustmentList`, `ItemFeeAdjustmentList` and `PromotionAdjustmentList` are "only returned for refunds, guarantee claims, and chargeback events".
- **`OrderFeeList`:** "applicable to Multi-Channel Fulfillment orders".

[official, command-verified]

### C. Payout-side APIs

C1. **Transfers v2024-06-01** ("Sellers only"). The model's `info.description` reads: "This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE."

| Operation | Path | Rate/burst | Region and role (Transfers API page, Role Mappings 2026-10-28) |
|---|---|---|---|
| `listPayouts` | `GET /finances/transfers/2024-06-01/payouts` | 0.5 / 10 | NA, EU, FE; Finance and Accounting |
| `listExpectedPayouts` | `GET /finances/transfers/2024-06-01/payouts/expected` | 0.5 / 10 | NA, EU, FE; Finance and Accounting |
| `getPaymentMethods` | `GET /finances/transfers/2024-06-01/paymentMethods` | .5 / 30 | EU; AISP, Finance and Accounting or PISP |
| `initiatePayout` (POST, moves money) | `POST /finances/transfers/2024-06-01/payouts` | 0.017 / 2 | EU; Finance and Accounting or Payment Initiation Service Provider |

- **`initiatePayout`:** "Initiates an on-demand payout to the seller's default deposit method in Seller Central … if eligible. You can only initiate one on-demand payout for each marketplace and account type within a 24-hour period." "For supported EU marketplaces, the only account type is `Standard Orders`." It answers `payoutReferenceId`, "The financial event group ID for a successfully initiated payout."
- **`Payout`:**
  - `id`, `currentStatus`, `statusHistory[]` (with `failureReason`);
  - `type`: `SCHEDULED`, or `ON_DEMAND` ("Ad hoc payouts initiated by the selling partner");
  - `amount`, `accountTail`, `paymentMethod` (`BANK_ACCOUNT`, `DEBIT_CARD`), `creationDate`, `paymentRail`;
  - `traceId`: "The banking network's unique identifier for a fund transfer request";
  - `period`, and `relatedIdentifiers` (`SETTLEMENT_ID` only).
- **`PayoutStatusName`:** `STARTED`, `IN_TRANSIT` ("sent to the bank for disbursal"), `PAID` ("successfully deposited in the bank"), `FAILED`, `CANCELLED`, `NO_PAYOUT` ("No payout is made for this settlement period").
- **`ExpectedPayout`:**
  - `amount`: "Can be null when no payout is expected";
  - `status`: `SCHEDULED`, `DISABLED`, `AT_RISK` ("may fail because of an invalid deposit instrument") or `NO_PAYOUT_EXPECTED` ("The expected balance is negative");
  - `period`, `scheduledDate`, `accountTail`, `paymentMethod`, `relatedIdentifiers`.
- **Release notes:** "The Transfers API v2024-06-01 is now generally available", with the roles PISP, AISP and Finance and Accounting (2025-02-26). `listPayouts` "enables you to retrieve payouts by date or settlement" (2026-07-29).

[official] (transfers_2024-06-01.json [command-verified]; Transfers API, https://developer-docs.amazon/sp-api/docs/transfers-api.md, updatedAt 2026-09-09, read 2026-11-09; Role Mappings for SP-API Operations, https://developer-docs.amazon/sp-api/docs/role-mappings.md, updatedAt 2026-10-28, saved copy `web01/role-mappings.md`)

C2. **Amazon's words disagree on what `PAID` means.** The Transfers model defines `PAID` as "The payout is successfully deposited in the bank". Amazon's own `finance-month-end-closer` skill says "`PAID` (**Amazon processed the payout — this does NOT prove the deposit reached the bank**)" and, in its checklist, "Amazon `PAID` ≠ received". Amazon's seller blog says "it can take up to five business days for the funds to appear in your bank account". [official] (Transfers model; `amzn/selling-partner-agentic-toolkit` `skills/finance-month-end-closer/references/reconciliation-notes.md`, commit 11d828ad 2026-10-08, read via `gh api` 2026-11-09; How Amazon seller payments work, https://sell.amazon.com/blog/amazon-seller-payments, 2025-07-30, read 2026-11-09)

C3. **Seller Wallet v2024-03-01** ("Sellers only"; model title "Amazon Seller Wallet Open Banking API").

- Twelve operations under `/finances/transfers/wallet/2024-03-01/`. Reads: `listAccounts`, `getAccount`, `listAccountBalances`, `getTransferPreview`, `listAccountTransactions`, `getTransaction`, `listTransferSchedules`, `getTransferSchedule`. Writes: `createTransaction`, `createTransferSchedule`, `updateTransferSchedule` (PUT), `deleteScheduleTransaction` (DELETE). The writes need `destAccountDigitalSignature` and `amountDigitalSignature` headers.
- The model carries **no Usage Plan table** [command-verified].
- Roles: reads Account Information Service Provider; writes AISP or Payment Initiation Service Provider. Regions NA, EU, FE.
- Release notes: "now publicly available in the NA and EU regions" (2025-08-27).
- It covers the Seller Wallet account (Amazon's own account product), not the ordinary Seller Central disbursement. aboutamazon's sidebar: "Amazon Seller Wallet gives selling partners more control over their funds—now available in USD, EUR, and GBP."

[official] (sellerWallet_2024-03-01.json; Seller Wallet API, updatedAt 2026-09-09; Role Mappings; aboutamazon, 2026-09-23)

C4. **Finance Remittance v2026-03-17.** It is "Vendors only": "programmatic access to vendor payment remittance data … the same data available on the **Payments** > **Remittance** view in Vendor Central".

- `getRemittanceHeaders` takes `startDate` ("minimum start date is one year ago") and `endDate` ("maximum date range … is 90 days"; default 30 days). The guide "Reconcile payments to invoices" says instead "remittance data is available from 1 January 2024 onward". The model and the guide disagree on the earliest date; vendors only either way.
- `getRemittance` returns the line items.
- No Usage Plan table in the model.
- Role Finance and Accounting.
- **Out of scope** (Vendor).

[official] (financeRemittance-2026-03-17.json; Finance Remittance API, saved `web01/api/finance-remittance-api.md`)

C5. **Invoices v2026-06-25** (`/finances/invoices/2026-06-25/invoices[/{invoiceIdentifier}]`). The page says "Vendors only" and "The Selling Partner API for Invoices is available for vendors."

- `fromIssueDate`/`toIssueDate`: "must not exceed 90 days".
- Page sizes: 100 headers, 600 line items.
- No Usage Plan table.
- **Not in Role Mappings** (2026-10-28) [command-verified, grep].
- The model's `partnerType` enum does include `SELLER`, and `serviceChargeType` includes `FBA_INVENTORY_STORAGE_FEE`, but Amazon's page settles the audience as vendors.
- **Out of scope.**

[official] (financesInvoices_2026-06-25.json; Invoices API page, saved `web01/api/invoice-api.md`, updatedAt 2026-09-09)

C6. **Invoices v2024-06-19** (`/tax/invoices/…`): "This API is only able to retrieve **Brazilian FBA invoices**." Role Tax Invoicing (Restricted), NA. Not a money read for this pack. [official] (Invoices API (Brazil Only), saved `web01/api/invoicing-2026.md`, updatedAt 2026-09-09)

### D. Fees before the fact: Product Fees API v0 ("Sellers only")

| Operation | Path | Rate/burst | Role (Role Mappings) |
|---|---|---|---|
| `getMyFeesEstimateForSKU` | `POST /products/fees/v0/listings/{SellerSKU}/feesEstimate` | 1 / 2 | Any of AF, Buyer Communication, Buyer Solicitation, F&A, IOT, Pricing, PL, Professional Services (R), SPI, DTCS (R), Tax Invoicing (R), Tax Remittance (R) |
| `getMyFeesEstimateForASIN` | `POST /products/fees/v0/items/{Asin}/feesEstimate` | 1 / 2 | Same list (DTCS: EU, FE only) |
| `getMyFeesEstimates` (batch) | `POST /products/fees/v0/feesEstimate` | 0.5 / 1 | **Pricing; Product Listing** only |

- "The estimated fees returned by this API are not guaranteed. Actual fees can vary."
- SKU: "accurate fees based on real item measurements, but only after they've sent their items to Amazon".
- ASIN: "these estimates use the item's catalog size, which might not always match the actual size".
- Batch: "allows up to 20 product requests in a single batch". The body is an array of `FeesEstimateByIdRequest`. The model states no `maxItems` [command-verified].
- Request: `MarketplaceId`, `IsAmazonFulfilled`, `PriceToEstimateFees` (`ListingPrice`, `Shipping`, `Points`), `Identifier` and `OptionalFulfillmentProgram` (`FBA_CORE`, `FBA_SNL`, `FBA_EFN`).
- Each `FeeDetail` carries `FeeType` (free string), `FeeAmount`, `FeePromotion`, `TaxAmount`, `FinalFee` and `IncludedFeeDetailList`.

[official] (productFeesV0.json [command-verified]; Product Fees API, saved, updatedAt 2026-09-09; Get product fees for a batch, https://developer-docs.amazon/sp-api/docs/get-product-fees-batch.md, updatedAt 2026-09-09, read 2026-11-09). The listing playbook's `price-position.md` §H holds the fee rules for price decisions (read 2026-10-14).

### E. Sales and orders: money at order time

E1. **Sales v1 `getOrderMetrics`**, `GET /sales/v1/orderMetrics`, rate .5 / burst 15.

- Required: `marketplaceIds` ("Only one marketplace can be specified"), `interval` ("first date is inclusive; second date is exclusive") and `granularity` (`Hour`/`Day`/`Week`/`Month`/`Year`/`Total`; Hour "only … less than or equal to 30 days from now", others "less or equal to 2 years").
- Optional: `granularityTimeZone`, `buyerType` (`B2B`/`B2C`/`All`), `fulfillmentNetwork` (MFN/AFN), `firstDayOfWeek`, `asin` or `sku` ("Specifying both … returns an error") and `amazonProgram` (`AmazonHaul`).
- Returns `unitCount`, `orderItemCount`, `orderCount`, `averageUnitPrice` ("totalSales/unitCount") and `totalSales`, "The total ordered product sales".
- Role: Inventory and Order Tracking or **Product Listing** in all regions. In FE, F&A, Pricing, AF and the others also work.

[official] (sales.json [command-verified]; Sales API, updatedAt 2026-09-09; Role Mappings)

E2. **Orders v2026-01-01.** `searchOrders` is `GET /orders/2026-01-01/orders`, rate 0.0056 / 20. `getOrder` is `GET /orders/2026-01-01/orders/{orderId}`, rate 0.5 / 30.

- `includedData` takes `BUYER`, `RECIPIENT`, `PROCEEDS` ("The revenue and financial breakdown for the order and order items"), `EXPENSE` ("The cost information"), `PROMOTION`, `CANCELLATION`, `FULFILLMENT`, `PACKAGES`, `TAX`, `PAYMENT` and `FULFILLMENT_ORDERS`.
- Money fields [command-verified]:
  - `Order.proceeds.grandTotal`: "The total amount that the seller receives from the sale of the order".
  - Order proceeds `breakdowns[].type`: `ITEM`, `SHIPPING`, `GIFT_WRAP`, `COD_FEE`, `TAX`, `DISCOUNT`, `DELIVERY_TIP`, `OTHER`. `status` is `PENDING`/`FINALIZED` "Only present for categories processed separately after checkout, such as `DELIVERY_TIP`".
  - `OrderItem.proceeds.proceedsTotal`, with `breakdowns` and `detailedBreakdowns`.
  - `ItemPrice.unitPrice`.
  - `AssociatedOrderItem.purchasePrice` ("excluding shipping, tax, gift wrap, and promotions"; added 2026-09-30).
  - `ItemExpense.pointsCost` (the only expense field).
  - `ItemTax.taxCollections[].model` `MARKETPLACE_FACILITATOR`: "Tax is withheld and remitted … by Amazon on behalf of the seller".
  - `OrderPayment.paymentExecutions`.
- **No Amazon fee is on an order** in this model; fees live in Finances [command-verified by absence of a fee field].
- Roles: AF, Buyer Communication, Buyer Solicitation, DTCS (R), F&A, IOT, Pricing, PL, Professional Services (R), SPI, Tax Invoicing (R), Tax Remittance (R).
- Orders v0 is deprecated as of 2026-01-28, **removal 2027-03-27**.

[official] (orders_2026-01-01.json; Role Mappings; Deprecation Schedule)

### F. Reports API (2021-06-30): report types that carry money

The operations carry many roles (AF, Buyer Communication, Buyer Solicitation, F&A, IOT, Pricing, PL, Professional Services (R), SPI, DTCS (R), Tax Invoicing (R), Tax Remittance (R)). The **report type's** own role governs. Rates are in the brief-305 door.md: `createReport` 0.0167/15, `getReport` 2/15, `getReportDocument` 0.0167/15, `getReports` 0.0222/10. "If an explicit retention is not specified for a report type, then the report will be retained for 90 days." Order reports are retained 30 days.

The roles below come from Role Mappings for SP-API Types (updatedAt 2026-09-09, saved `web01/role-mappings-for-types.md`) [command-verified, parsed]. The columns and timing come from Amazon's report pages as read by the surface survey (`02-surface-reports-datakiosk-notifications.md`, 2026-11-09) and the settlement and payment pages read today.

| Report type | What it carries | Request | Role |
|---|---|---|---|
| `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` | Settlement lines. Columns: settlement-id, settlement-start-date, settlement-end-date, deposit-date, total-amount, currency, transaction-type, order-id, merchant-order-id, adjustment-id, shipment-id, marketplace-name, amount-type, amount-description, amount, fulfillment-id, posted-date, posted-date-time, order-item-code, merchant-order-item-id, merchant-adjustment-item-id, sku, quantity-purchased, promotion-id. "Amount values always populate in a single amount column." | "Settlement reports cannot be requested or scheduled. They are automatically scheduled by Amazon." Found with `getReports`. | **F&A** |
| `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE`, `…_XML` | v1 settlement | Deprecated 2025-03-17; **removed 2026-11-11** | AF or F&A / F&A |
| `GET_DATE_RANGE_FINANCIAL_HOLDS_DATA` ("Deferred Transaction Report") | "A point-in-time report that contains a list of deferred transactions. A single report can provide up to 10 years of data." CSV. | "You must request the Deferred Transaction Report through the Payments Reports Repository on Seller Central" before Reports retrieves it | F&A (payment page); **absent from Role Mappings for Types** [command-verified] |
| `GET_REFERRAL_FEE_PREVIEW_REPORT` | Referral fee preview per listing | Request; "up to 24 hours old … not more than once per 24-hour period" (listing playbook; another page says 72 h) | F&A |
| `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` | FBA fee preview per SKU | "once per day per seller", data up to 72 h old | AF, Pricing |
| `FEE_DISCOUNTS_REPORT` ("Referral Fee Discounts Report") | "a summary of the seller's fee discounts". `.xlsx`. "Amazon Business sellers". | "can be requested or scheduled"; "up to 24 hours old" | PL |
| `GET_FBA_REIMBURSEMENTS_DATA` | Reimbursements: approval-date, reimbursement-id, case-id, amazon-order-id, reason, sku, fnsku, asin, amount-per-unit, amount-total, quantity-reimbursed-cash/-inventory/-total, original-reimbursement-id/-type | Request; daily | AF, Pricing |
| `GET_FBA_STORAGE_FEE_CHARGES_DATA` | Monthly storage estimate per ASIN and FC | Request or schedule | AF, Pricing |
| `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` | Aged-inventory surcharge charges | Request; range "should be equal to one month" | AF, Pricing |
| `GET_FBA_OVERAGE_FEE_CHARGES_DATA` | Capacity overage fee | Request | **AF only** |
| `GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA` / `…_SHIPMENT_DETAIL_DATA` | Removal fees, quantities | Request | AF, Pricing |
| `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` | FBA returns and dispositions | Request; daily | AF, Pricing |
| `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA` | Shipped FBA units with `item-price-per-unit` | Request; 1–3 h lag | **AF only** |
| `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_PROMOTION_DATA` | `item-promotion-discount` on FBA orders | Request; daily | AF, Pricing |
| `GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL` (and `…BY_LAST_UPDATE_GENERAL`, XML twins) | All orders with `item-price`, promotions, `quantity`, `is-business-order` | Request; 30-day range | AF, DTCS (R), IOT, **Pricing** (+PL for last-update) |
| `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL` | FBA shipments (prices, tax, shipping columns) | Request; at most 12 requests per 8 hours per seller account (listing playbook) | AF, IOT, Pricing |
| `GET_LEDGER_DETAIL_VIEW_DATA` / `GET_LEDGER_SUMMARY_VIEW_DATA` | Inventory movements (units, not money; feeds reimbursement reads) | Request | AF only |
| `GET_COUPON_PERFORMANCE_REPORT` / `GET_PROMOTION_PERFORMANCE_REPORT` | Promotion spend and sales | Request | BA / BA, SPI (sellers need SPI per Amazon's Performance Reports page, listing playbook) |
| `GET_SALES_AND_TRAFFIC_REPORT` | Ordered product sales, refunds | Request | BA |
| `GET_FBA_FULFILLMENT_CUSTOMER_TAXES_DATA` | FBA tax lines | Request | **AF** or Tax Remittance (R) |
| `GET_FLAT_FILE_SALES_TAX_DATA` (US) | Sales tax report | "cannot be requested or scheduled"; the seller generates it in the Tax Document Library | Tax Remittance (R) |
| `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_TAX`, `GET_FLAT_FILE_ORDER_REPORT_DATA_TAX`, `GET_FLAT_FILE_ORDERS_RECONCILIATION_DATA_TAX`, `GET_ORDER_REPORT_DATA_TAX` (NA) | Tax order data | Request | Tax Remittance (R) |
| `GET_VAT_TRANSACTION_DATA`, `SC_VAT_TAX_REPORT_INVOICE`, `GET_FLAT_FILE_VAT_INVOICE_DATA_REPORT`, `GET_XML_VAT_INVOICE_DATA_REPORT`, `FBA_BULK_INVOICE`, `GET_FLAT_FILE_ORDER_REPORT_DATA_INVOICING` (EU) | VAT | Request; VAT transaction `dataEndTime` "no later than three days before the request date" | Tax Invoicing (R) |
| `GET_GST_MTR_B2B_CUSTOM`, `GET_GST_MTR_B2C_CUSTOM`, `GST_MTR_B2B`, `GST_MTR_B2C`, `GST_MTR_STOCK_TRANSFER_REPORT` (India) | GST | Request | Tax Invoicing (R) / Tax Remittance (R) |
| `GET_EPR_MONTHLY/QUARTERLY/ANNUAL_REPORTS` | EPR declarations (EU); fee lines not read here | Request | PL |

**No SP-API report type corresponds to Seller Central's Date Range Reports** (summary or transaction). Report Type Values lists only the Deferred Transaction Report under "Payment". [official] (Report Type Values, https://developer-docs.amazon/sp-api/docs/report-type-values.md, updatedAt 2026-09-10; Payment reports, …/report-type-values-payment.md, updatedAt 2026-09-09; Settlement reports, …/report-type-values-settlement.md, updatedAt 2026-10-14; Amazon Business reports, …/report-type-values-amazon-business.md; all read 2026-11-09)

### G. Data Kiosk (2023-11-15)

G1. Operations [command-verified]:

- `createQuery` (`POST /dataKiosk/2023-11-15/queries`): 0.0167/15. The query is "at most 8000 characters after unnecessary whitespace is removed".
- `getQuery`: 2.0/15.
- `getQueries` and `cancelQuery`: 0.0222/10.
- `getDocument`: 0.0167/15.

Limits:

- "Data Kiosk only allows one request per query / selling partner / application combination."
- "does not support query scheduling."
- "does not support query backlogging. Data Kiosk limits the number of concurrent non-terminal queries per selling partner and per GraphQL query."
- Retention: "the shortest (minimum) retention is applied". Every field in the economics and sales-and-traffic schemas is `P30D` [command-verified: 112 `P30D` directives in sales-and-traffic; economics likewise].

[official] (dataKiosk_2023-11-15.json; Data Kiosk API, updatedAt 2026-10-20, saved)

G2. **Role: Amazon's pages disagree.**

- Role Mappings (2026-10-28) gives **Brand Analytics** as the only role for all five operations.
- The Data Kiosk page says: "Each field available with Data Kiosk requires a certain role. Data Kiosk determines whether the requester has the required roles for each field in the query upon query creation."
- "Correction: Data Kiosk role requirements" says: "The Economics dataset requires the Selling Partner Insights role. The Vendor Analytics and Sales and Traffic datasets require the Brand Analytics role." The correction shows no date; it refers back to the 2024-06-19 GA.
- Seller Analytics fields carry PAAM rights rather than a role name (`analytics_sales_and_traffic_view_pa`, `analytics_sales_and_lending_view`) [command-verified].

[official] (https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements.md, read 2026-11-09)

G3. **`analytics_economics_2024_03_15`** [command-verified, schema read in full at db2936aa].

`economics(startDate, endDate, aggregateBy, includeComponentsForFeeTypes, marketplaceIds)`:

- "The start date must be no more than two years ago." Mid-week and mid-month dates snap to week or month boundaries in UTC+0.
- Aggregation: `MSKU`/`CHILD_ASIN`/`PARENT_ASIN` × `DAY`/`WEEK`/`MONTH`/`RANGE`, in "marketplace local time"; the week starts Sunday.
- "The data sets are refreshed daily."
- "The supported fee types and advertisement charge types can be found [here](…/GZ8Y22NL2FSRY8M5)."

Row fields:

- **`sales`:** `orderedProductSales`, `refundedProductSales`, `netProductSales`, `unitsOrdered`, `unitsRefunded`, `netUnitsSold`, `averageSellingPrice`.
- **`fees[]`:** a `FeeSummary` (`feeTypeName`, `charges[]`; `charge` is deprecated). Each `Fee` has `aggregatedDetail` (`amount`, `amountPerUnit`, `amountPerUnitDelta`, `promotionAmount`, `quantity`, `taxAmount`, `totalAmount`), `components[]` (only for `FBA_FULFILLMENT_FEE` and `FBA_STORAGE_FEE`), `properties[]` (e.g. size tier), and its own `startDate`/`endDate`. "when the request date range includes the Amazon fee change date … the response will split the request date range and display the fee separately".
- **`ads[]`:** an `AdSummary`, `adTypeName`.
- **`cost`:** the seller-provided `costOfGoodsSold`, `fbaCost.shippingToAmazonCost`, `mfnCost.fulfillmentCost`/`storageCost`, `miscellaneousCost`. "Fields in this type will be null if not provided by the seller."
- **`netProceeds.total` / `perUnit`:** "calculated as sales.netProductSales - sum of fees.charge.totalAmount - sum of ads.charge.totalAmount - (cost of … MFN products or cost of … FBA products) * sales.netUnitsSold".

`economicsPreview`: from today to at most 120 days ahead, MSKU × RANGE. `feeTypes` is required, from `PreviewFeeType`: `AGED_INVENTORY_SURCHARGE`, `BASE_FBA_FULFILLMENT_FEE`, `BASE_MONTHLY_STORAGE_FEE`, `CLOSING_FEES`, `DIGITAL_SERVICES_FEE_FBA`, `DIGITAL_SERVICES_FEE_SOA`, `FBA_FULFILLMENT_FEES`, `FBA_INBOUND_PLACEMENT_SERVICE_FEE`, `HIGH_RETURN_RATE_FEE`, `LOW_INVENTORY_LEVEL_FEE`, `MONTHLY_INVENTORY_STORAGE_FEES`, `PAN_EU_OVERSIZE_FEE`, `PER_ITEM_SELLING_FEES`, `REFERRAL_FEES`, `RETURN_PROCESSING_FEE`, `SPONSORED_PRODUCTS_CHARGES`, `STORAGE_UTILIZATION_SURCHARGE`.

`economicsSimulation`: `actionTypes` `AWD` or `SIPP`, at most 100 products, up to 90 days ahead.

The release note of 2026-09-30 ("deal, coupon, removal, disposal, and fuel fees") is **not reflected** in the schema clone. Fee types in `economics` come back by name (`feeTypeName`), not as an enum, so new types may appear in results without a schema change [seat].

G4. **`analytics_salesAndTraffic_2024_04_24`.** Money fields: `orderedProductSales`, `shippedProductSales`, `averageSalesPerOrderItem`, `averageSellingPrice`, `claimsAmount`, `claimsGranted`, `refundRate`, `unitsRefunded` [command-verified]. B2B refund and claim metrics were added 2026-01-28 and 2026-02-23. The v2023_11_15 dataset was removed 2026-03-27.

G5. **`analytics_sellerAnalytics_2025_03_31`** (added per the 2026-09-30 release note). Money fields [command-verified]:

- A `Lending` group: `disbursements` ("Total monetary amount disbursed to the seller from Amazon for sales and other transactions"), `totalBalanceByStandardOrders`, `primaryProductCategoryNetGMS`, `totalFbaInventoryValue` ("based on 15-day average selling price").
- `totalRefundAmount`: "Refund data is computed with a delay of about 45 days, so the most recent ~45 days may be empty or incomplete".
- `promotionDiscountAmt`, `orderedProductSales`.
- "If not provided, amounts are returned in USD" (the `currencyCode` argument).
- Access is by PAAM rights.

### H. Notifications carrying money

| Type | What Amazon says | Role (Role Mappings for Types) |
|---|---|---|
| `TRANSACTION_UPDATE` | "sent whenever there is a new transaction posted to the seller's account". The payload holds SellingPartnerMetadata (incl. `AccountType`), RelatedIdentifiers, TransactionType, PostedDate, TotalAmount. Its example writes `"RelatedIdentifierName": "OrderId"`, not the API's `ORDER_ID`. SQS. Added 2024-10-14. | **Not listed** in Role Mappings for Types (updatedAt 2026-09-09) [command-verified]. The notification page says "Sellers can subscribe to this notification." |
| `FEE_PROMOTION` | Time-limited fee promotions. On subscribing, "the seller receives all currently active promotions"; "Each promotion is sent as a single message". `FeePromotionType` is `Pricing`, `SelectionASIN` or `SelectionCategory`. | F&A; PL |
| `REPORT_PROCESSING_FINISHED` | A report ended | AF, BA, IOT, Pricing, PL, DTCS (R), TI (R), TR (R). **F&A is not listed.** |
| `DATA_KIOSK_QUERY_PROCESSING_FINISHED` | A query ended | AWD; BA |

The destination and subscription operations are grantless (`sellingpartnerapi::notifications`); `createSubscription` takes "the role that is associated with the notification type". Delivery is to Amazon SQS or EventBridge. [official] (Notification Type Values, https://developer-docs.amazon/sp-api/docs/notification-type-values.md, updatedAt 2026-10-28, read 2026-11-09; schemas `TransactionUpdateNotification.json`, `FeePromotionNotification.json` [command-verified]; Role Mappings)

### I. The SP-API fee cancellation

"After careful consideration, we have decided that we will not move forward with the SP-API usage and annual fees at this time." "In the coming weeks, we will be making updates to the Solution Provider Portal (SPP) to reflect this decision, such as removing the fee preview dashboard." [official] (Cancellation of Third-Party Developer Selling Partner API (SP-API) Fees, https://developer.amazonservices.com/cancellation-of-sp-api-fees, datePublished 2026-06-11, dateModified 2026-07-01, saved `web01/fees/cancellation-of-sp-api-fees.html`, read 2026-11-09). For money reads this means the high-volume `listTransactions` and `getReportDocument` pulls carry no Amazon charge today.

### J. How far back each money document reaches (added 2026-11-10)

Auditors and tax inspections ask for several years of settlements and transaction detail. Amazon states each horizon in a different place, and some views state none. The table below gathers them. "Stated" means Amazon's words; "none stated" means the model or page was read and carries no earliest date [command-verified, grep over the models at db2936aa for "years", "past", "ago", "retain", "180"].

| Document or read | Where | How far back (Amazon's words) | After that | Source |
|---|---|---|---|---|
| Settlement report V2 through the API | `getReports` (`reportTypes=GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`) | `createdSince`: "The default is 90 days ago. Reports are retained for a maximum of 90 days." | Not listable; "Settlement reports cannot be requested or scheduled." | [official] reports_2021-06-30.json [command-verified]; Settlement Reports page (updatedAt 2026-10-14) |
| Any other generated report | `getReport` / `getReportDocument` | "If an explicit retention is not specified for a report type, then the report will be retained for 90 days." Order reports: "retained for 30 days". | "If the generated report is not downloaded within the retention period, you can generate the report again." (Order reports: "you can generate them again.") | [official] Report Type Values (updatedAt 2026-09-10); Order Reports (updatedAt 2026-10-28) |
| Settlements in Seller Central (Payments → All Statements; in the 2026 Finance workspace, Finance Reports → "Understand Payout") | Seller Central only | Amazon's own page not readable (JS shell). See the practitioners: archived after a period, re-requestable. | — | §What practitioners add |
| `listTransactions` (2024-06-19) | API | **None stated.** Only the 180-day span per call and the two-minute and 48-hour edges. | — | [command-verified] finances_2024-06-19.json |
| `listBalances` `asOfDate`; `listSummary` `periodStart`/`periodEnd` | API | **None stated** ("If provided, the response includes historical balances at the specified date"). | — | [command-verified] same model |
| `listPayouts` | API | **None stated**: `createdAfter` "If omitted, no start date filter is applied." | — | [command-verified] transfers_2024-06-01.json |
| `listFinancialEventGroups` (v0) | API | **None stated** beyond the 180-day span per call. | Not on the removal schedule | [command-verified] financesV0.json |
| `listFinancialEventsByGroupId` (v0) | API | "This operation only retrieves a group's data for the past two years. A request for data spanning more than two years produces an empty response." | Removal 2027-08-27 | [official] financesV0.json |
| `listFinancialEvents`, `listFinancialEventsByOrderId` (v0) | API | **None stated** beyond the 180-day span (`listFinancialEvents`). | Removal 2027-08-27 | [command-verified] financesV0.json |
| Transaction view | Seller Central | "Only transactions from the last 24 months are available to review." | — | [official, Amazon staff] Quick Tip: Payments Dashboard – Transaction View (Jessica_Amazon_, 2024-01-16) |
| Date Range reports (Summary PDF, Transaction CSV) | Seller Central; no SP-API report type | "you can generate reports for up to 365 days at a time, going back as far as 2012." "This process can take up to three hours". | Reports "for periods before January 1, 2025, will continue to follow the prior format" (the 2026 posted-date change; reconciliation.md §C). | [official, Amazon staff] Where to find your Amazon selling reports (KJ_Amazon, 2024-10-31); Updated payment reports … (News_Amazon, 2026-03-18) |
| Deferred Transaction Report (`GET_DATE_RANGE_FINANCIAL_HOLDS_DATA`) | Requested in Seller Central, then `getReports` | "A point-in-time report that contains a list of deferred transactions. A single report can provide up to 10 years of data." | "When a transaction is updated from deferred to released, it will no longer be included on the Deferred Transaction report." | [official] Payment Reports (updatedAt 2026-09-09); News_Amazon UK 2024-10-04 (as read in reconciliation.md C) |
| Data Kiosk Economics | API | "The start date must be no more than two years ago." | Results kept 30 days (`P30D`) | [official] analytics_economics_2024_03_15.graphql |
| Data Kiosk Sales and Traffic; Seller Analytics | API | "no more than two years ago" (both schemas) | P30D | [official] analytics_salesAndTraffic_2024_04_24, analytics_sellerAnalytics_2025_03_31 |
| `GET_SALES_AND_TRAFFIC_REPORT` | API | "`dataStartTime` … must not be more than two years before the date of the request. If you fail this condition, the request will be cancelled." | — | [official] Analytics Reports (updatedAt 2026-10-28) |
| `getOrderMetrics` | API | `granularity=Hour` "less than or equal to 30 days from now"; others "less or equal to 2 years from now". | — | [official] sales.json |
| Orders API (2026-01-01 and v0) | API | "This API does not display order data that is more than two years old, except in the JP, AU, and SG marketplaces, for which data from 2016 and after is available." | — | [official] orders_2026-01-01.json; ordersV0.json |
| Order reports (all-orders and others) | API | "Order reports only support orders that are less than two years old." | Retained 30 days | [official] Order Reports |
| Inventory Ledger detail (`GET_LEDGER_DETAIL_VIEW_DATA`, units) | API | "You can view all historical movements of your inventory for 18 months in this report." | — | [official] FBA Reports (updatedAt 2026-10-13) |
| Reimbursements, storage, returns and removal reports | API | **None stated** on the FBA Reports page. | — | [command-verified] grep of the page |
| VAT transaction report (`GET_VAT_TRANSACTION_DATA`, Tax Invoicing (R)) | API | No earliest date stated; `dataEndTime` "no later than three days before the request date". "If you request the same date range again, the report can return updated records." | — | [official] Tax Reports (updatedAt 2026-11-03) |
| India On Demand GST MTR B2C (`GET_GST_MTR_B2C_CUSTOM`, Tax Invoicing (R)) | API | "The report only provides data for the last 45 days." | — | [official] Tax Reports |
| US sales tax report (`GET_FLAT_FILE_SALES_TAX_DATA`) | Generated in the Tax Document Library, then `getReports` | Years not stated. | — | [official] Tax Reports |
| Tax Document Library forms (1099-K) | Seller Central | Years not stated. Amazon Pay's FAQ: "Select the appropriate year"; "You must be signed in as the primary user to access forms in the Tax Document Library." | — | [official, Amazon Pay] IRS Form 1099-K FAQs, https://pay.amazon.com/help/200831230 (via WebFetch; the Seller Central copy is a JS shell) |
| Profit Analytics | Seller Central | "the past two years through the next 90 days" | — | [official] as read in product-profit.md (2025-11-13 announcement) |
| Amazon's `finance-month-end-closer` 1.3.1 | Amazon's toolkit | States **no** look-back window; it takes any `year` + `month`. | — | [official] SKILL.md, reconciliation-notes.md, evals.json via `gh api` [command-verified, grep] |

What the table shows, in facts:

- The settlement report is the only money document Amazon generates on its own schedule and the API can neither request nor list after about 90 days [official, the two quotes above]. Every other API report can be generated again within its data's own horizon.
- The transaction-level views reach back unevenly: Transaction view 24 months, v0 by group two years, Date Range reports to 2012 in 365-day pieces, `listTransactions` with no stated earliest date.
- Per-product views (Economics, Sales and Traffic, Orders, order reports) stop at two years. Data Kiosk results themselves are kept 30 days.
- The Deferred Transaction Report lists what is deferred at the moment it is generated; a released line leaves it. A list of what was deferred on a past date is therefore not a report Amazon regenerates; `listBalances` with `asOfDate` and `balanceType=DEFERRED` gives the past deferred **amount** [official, the quotes above; the "not regenerated" reading is [seat]].
- A regenerated VAT transaction report can differ from one generated earlier for the same range (Amazon's note above). A copy kept at the time is not the same as a copy generated later [official; the comparison is [seat]].

## The SP-API and report faces

### The one table: every money read

Key to the role abbreviations:

- **Ticked today:** PL Product Listing, Pr Pricing, BA Brand Analytics, F&A Finance and Accounting.
- **Being added:** AF Amazon Fulfillment.
- **Others:** SPI Selling Partner Insights, IOT Inventory and Order Tracking, AISP Account Information Service Provider, PISP Payment Initiation Service Provider, TI Tax Invoicing (Restricted), TR Tax Remittance (Restricted), DTCS Direct to Consumer Shipping (Restricted).

Rates are the model's default: rate in requests per second, then burst. Amazon: "Selling partners whose business demands require higher throughput may have higher rate and burst values".

| Read | Path | Model file | Rate/burst | Role (Role Mappings, 2026-10-28) | Deprecation |
|---|---|---|---|---|---|
| `listTransactions` | GET /finances/2024-06-19/transactions | finances_2024-06-19.json | 0.5/10 | F&A | — |
| `listBalances` | GET /finances/2024-06-19/balances | same | 0.5/10 | F&A | — |
| `listSummary` | GET /finances/2024-06-19/summary | same | 0.5/10 | F&A | — |
| `listFinancialEventGroups` | GET /finances/v0/financialEventGroups | financesV0.json | 0.5/30 | F&A; AISP (EU only) | not scheduled |
| `listFinancialEventsByGroupId` | GET /finances/v0/financialEventGroups/{id}/financialEvents | same | 0.5/30 | F&A; AISP (EU only) | removal 2027-08-27 |
| `listFinancialEventsByOrderId` | GET /finances/v0/orders/{orderId}/financialEvents | same | 0.5/30 | F&A | removal 2027-08-27 |
| `listFinancialEvents` | GET /finances/v0/financialEvents | same | 0.5/30 | F&A; AF (NA, FE only); AISP (EU only) | removal 2027-08-27 |
| `listPayouts` | GET /finances/transfers/2024-06-01/payouts | transfers_2024-06-01.json | 0.5/10 | F&A (NA, EU, FE) | — |
| `listExpectedPayouts` | GET …/payouts/expected | same | 0.5/10 | F&A (NA, EU, FE) | — |
| `getPaymentMethods` | GET …/paymentMethods | same | .5/30 | AISP or F&A or PISP, any one (EU) | — |
| `initiatePayout` (write) | POST …/payouts | same | 0.017/2 | F&A or PISP, any one (EU) | — |
| Seller Wallet reads (8) / writes (4) | /finances/transfers/wallet/2024-03-01/… | sellerWallet_2024-03-01.json | none stated | AISP / AISP; PISP | — |
| `getMyFeesEstimateForSKU` / `ForASIN` | POST /products/fees/v0/listings/{SellerSKU}/feesEstimate; …/items/{Asin}/feesEstimate | productFeesV0.json | 1/2 | any of 12 incl. F&A, Pr, PL, AF | — |
| `getMyFeesEstimates` | POST /products/fees/v0/feesEstimate | same | 0.5/1 | Pr; PL | — |
| `getOrderMetrics` | GET /sales/v1/orderMetrics | sales.json | .5/15 | PL; IOT (others FE only) | — |
| `searchOrders` / `getOrder` | GET /orders/2026-01-01/orders[/{orderId}] | orders_2026-01-01.json | 0.0056/20; 0.5/30 | any of 12 incl. F&A, Pr, PL, AF | v0 reads removal 2027-03-27 |
| Data Kiosk `createQuery` … | /dataKiosk/2023-11-15/… | dataKiosk_2023-11-15.json | 0.0167/15 etc. | BA (op); Economics: SPI (correction) | — |
| Reports `createReport` … | /reports/2021-06-30/… | reports_2021-06-30.json | 0.0167/15 etc. | per report type (§F) | v1 settlement removal 2026-11-11 |
| `getRemittanceHeaders` / `getRemittance` | /finances/remittances/2026-03-17/… | financeRemittance-2026-03-17.json | none stated | F&A | vendors only |
| `getInvoiceHeaders` / `getInvoice` | /finances/invoices/2026-06-25/… | financesInvoices_2026-06-25.json | none stated | not in Role Mappings | vendors only |
| Support `listCases` / `getCase` | /support/2025-02-01/… | support model | 0.1/10 | Selling Partner Support (R) | — |

[command-verified] (rates: `ops.py` over each model; roles: `roles.py` over `web01/role-mappings.md` and `role-mappings-for-types.md`, with the `[block:parameters]` rows read by hand)

### Roles against the five a seller ticks

| Money read | PL | Pr | BA | F&A | AF | Needs something else |
|---|---|---|---|---|---|---|
| Transactions, balances, summary (2024-06-19) | | | | ✓ | | — |
| v0 event groups / by group / by order | | | | ✓ | (listFinancialEvents NA/FE) | — |
| Payouts, expected payouts | | | | ✓ | | — |
| On-demand payout, payment methods (EU) | | | | ✓ | | or PISP / AISP |
| Settlement V2; Deferred Transaction Report; referral fee preview | | | | ✓ | | — |
| Fee estimate (single) | ✓ | ✓ | | ✓ | ✓ | — |
| Fee estimate (batch of 20) | ✓ | ✓ | | | | — |
| Orders 2026-01-01 proceeds | ✓ | ✓ | | ✓ | ✓ | buyer/address fields need an RDT + DTCS |
| `getOrderMetrics` | ✓ | | | | | (IOT also) |
| All-orders reports (`item-price`) | | ✓ | | | ✓ | — |
| FBA fee preview, reimbursements, storage, LTSF, returns, removal, shipment promotions | | ✓ | | | ✓ | — |
| Overage fee, customer shipment sales, ledger, inventory planning | | | | | ✓ | — |
| FBA customer taxes | | | | | ✓ | or TR |
| Sales and Traffic report / dataset; coupon performance | | | ✓ | | | — |
| Promotion performance report | | | ✓ | | | sellers: SPI (Performance Reports page) |
| Data Kiosk Economics (per-product fees, ads, COGS, net proceeds) | | | ✓ (per Role Mappings) | | | **SPI (per the correction)**: unresolved until a live `createQuery` |
| Seller Analytics `Lending` (disbursements) | | | ? | | | PAAM right `analytics_sales_and_lending_view` |
| Fee-discount report (Amazon Business) | ✓ | | | | | — |
| `FEE_PROMOTION` notification | ✓ | | | ✓ | | an SQS/EventBridge destination |
| `TRANSACTION_UPDATE` notification | | | | ? | | role not mapped; SQS destination |

**Reads that need roles outside the five. Nothing is built on any of them:**

- **Selling Partner Insights.** It would open the Economics dataset, if the correction holds. It also opens the promotion performance report for sellers, seller performance reports and `ACCOUNT_STATUS_CHANGED`.
- **Tax Remittance (Restricted).** It would open the US sales-tax report, the `_TAX` order reports and the India GST reports. Each needs an RDT as well.
- **Tax Invoicing (Restricted).** It would open the EU VAT transaction and VAT invoice reports, `FBA_BULK_INVOICE`, the Brazil invoices API and the India GST MTR reports.
- **Account Information Service Provider.** It would open Seller Wallet reads and the EU alternative for v0 groups and `getPaymentMethods`.
- **Payment Initiation Service Provider.** It would open Seller Wallet money moves and the alternative role for `initiatePayout`.
- **Selling Partner Support (Restricted).** It would open reading a reimbursement or fee case's status.
- **Inventory and Order Tracking.** It would open `getOrderMetrics` (already open under PL) and `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE` (MFN returns).

### Pitfalls Amazon names (collected)

- Finances can lack "orders from the last 48 hours" (both versions).
- Windows over 180 days return an empty answer, not an error (v2024-06-19 and v0 events and groups).
- Pages can be empty while `nextToken` continues. `postedBefore` must be more than 2 minutes in the past.
- v0 hides deferred events "until they are released"; v2024-06-19 returns them as `DEFERRED`.
- v0 by-group covers only "the past two years".
- For US MFN orders, `listTransactions` must be called without `marketplaceId`.
- `breakdownType` and `FeeType` are open strings.
- Settlement reports cannot be requested. The Deferred Transaction Report must first be requested in Seller Central.
- The v1 settlement reports end 2026-11-11.
- Economics is P30D and splits ranges at fee-change dates.
- Seller Analytics refunds lag about 45 days.
- Seller Wallet, Remittance and Invoices 2026 models state no rate.

## What practitioners add

**Open-source clients (read-only check, 2026-11-09)** [command-verified, `gh api` / `npm view`]:

- **`saleweaver/python-amazon-sp-api`** (692★, MIT, pushed 2026-11-10). It has `finances_v0`, `finances_2024_06_19`, `finances_2024_06_01` (Transfers), `seller_wallet` and `product_fees` modules.
  - Its `FinancesV20240619` class maps v0 operations to paths **that are not in Amazon's model**, e.g. `/finances/2024-06-19/orders/{}/financialEvents` and `/finances/2024-06-19/financialEventGroups`.
  - Only `list_transactions` there matches a real path.
  - Its Transfers class has `initiate_payout` and `get_payment_methods`, but no `listPayouts` or `listExpectedPayouts`.
  - [opinion: code author] "Finance helpers" amount to paging wrappers; no fee mapping, reconciliation or settlement parsing ships in it.
- **`amz-tools/amazon-sp-api`** (npm `amazon-sp-api` 1.2.1, 265★, MIT, last change 2026-03-30). `finances_2024-06-19` lists only `listTransactions`; Transfers lists only `initiatePayout` and `getPaymentMethods`. It predates `listBalances`, `listSummary` and `listPayouts`.
- **Settlement and profit tools on GitHub** are single-author and near zero stars: `prathamk11/amazon-settlement-reviewer` (2026-08), `xieyi138-star/amazon-settlement-parser` (V2 flat file in the browser, CC-BY-4.0), `Puntoos/amazon-settlement-analyzer`, and a dozen "FBA profit calculator" repos. No open A2X-like accounting tool of standing was found. A cx pack borrows nothing from them.
- **pi packages:** `npm search keywords:pi-package` with "amazon", "finance", "accounting" and "ecommerce" finds no Amazon money package except ours. The finance ones are personal-portfolio tools (`@pi-stef/finance`, `@e9n/pi-myfinance`, Yahoo tickers). `pi-mcp-adapter` 7.0.1 exists, so pi could in principle mount an MCP server, but see Amazon's connector below.
- The surface survey (`07-reuse.md`, 2026-11-09) lists about 15–20 SP-API MCP wrappers (ailumia, jhrendon, haloshin and others). They have finances tools but no seller money knowledge. Hosted paid MCPs sell profit "from settlement line items": AgentXray, DataDoe ($97/month), Novadata ("40+ fee types"), Sellerboard (read-only MCP), Helium 10 (Diamond+). So do the Chinese ERPs: 领星 Lingxing official MCP (MSKU and order profit, settlements, reimbursement report), 赛狐 Sellfox (profit, reimbursement report, read/write), 船长BI Captain BI (finance/profit), 积加 Gerpgo (finance). [opinion: those vendors, as read by that seat]

**Amazon's own Claude plugin, "Amazon Selling Partner" 1.0.0** (local zip; Apache-2.0) [command-verified, grep over every file]:

- **No skill or command is about money.**
- `seller-analytics` reads `analytics_getMetricData`. Its only money metric is `TOTAL_ORDERED_PROD_SALES_AMT` (revenue, `Threep_Sales`), and "include the `currency` field for financial metrics". Its description excludes "tax/GST/financial-settlement reports". Its eval expects the agent to say a per-unit "profit-margin metric isn't available".
- `fba-inbound-management` shows the inbound placement fee before `fbaInbound_confirmPlacementOption`: "permanent and charges the placement fee".
- `stockout-prevention` notes running lean "can trigger the **low-inventory-level fee**" and uses `sales_getOrderMetrics` because "there is **no `reports` tool** exposed".
- The commands (`/sp-stockout-check`, `/sp-fix-listing`, `/sp-sales-drop`) carry no money read.

**Amazon's toolkit repository** (`amzn/selling-partner-agentic-toolkit`, not in our zip):

- A 12th skill, **`finance-month-end-closer` 1.3.1**, sits at `skills/finance-month-end-closer/` in https://github.com/amzn/selling-partner-agentic-toolkit. Its files are `SKILL.md`, `references/reconciliation-notes.md`, `references/seller-central-urls.md` and `eval/evals.json`. It was committed 2026-10-08 (11d828ad) and merged 2026-10-12 (PR #7).
  - Frontmatter: `license: Apache-2.0`, `author: SP-AI Skill Authoring Pipeline`, `persona: Maya (non-technical FBA seller / bookkeeper)`, `platforms: [claude-desktop, aws-quick]`, `apis: [finances]`. GitHub reports the repository licence as NOASSERTION.
  - It describes itself as "Read-and-explain only: it posts no entries, changes no accounting records, and never files, submits, pays, or moves money".
- It calls one tool, **`finances_monthEndClosing`** ("gateway tool `monthEndClosing`"). Params: `year`, `month` and `entityId` are required; `accountType` and `toolVersion` are optional. `entityId` is "supplied by the SP-AI host/runtime context". It returns per account `lhsMonthNetProceeds`, `rhsSettlementSum`, `difference`, `beginningBalance`, `endingBalance` and `settlements[]` (`settlementId`, `periodStart`, `periodEnd`, `classification`, `netProceeds`, `contribution`, `payoutId`, `payoutStatus`, `payoutCreationDate`, `payoutStatusHistory[]`).
- Facts it states:
  - "`difference` = LHS − RHS … A difference that parses to a non-zero value … means some transactions for the period are still being processed".
  - Settlement classes: `inside`, `straddles_start`, `open_at_end`, `spans_month`.
  - "Negative closed-settlement net proceeds are treated as 0 (a negative settlement produces no payout and carries into the next settlement)".
  - "The payout amount **always equals the settlement's `netProceeds`** (confirmed invariant)".
  - "`PAID` (**Amazon processed the payout — this does NOT prove the deposit reached the bank**)".
  - "The open month-end balance is **not** a guaranteed payout"; elsewhere "it is **not a guaranteed future payout** (fees, refunds, reserves, adjustments may …)".
  - The reconciliation trail: settlements closed in the month − `beginningBalance` + `endingBalance` = month net proceeds (`lhsMonthNetProceeds`). "A month's payouts can total *more* than its net proceeds without any error — settlements cross calendar months."
  - "All monetary amounts are **decimal strings**".
  - The Seller Central Payments link is `<marketplace host>/amazonsell/payments`.
- `finances_monthEndClosing` is **in no public model** [command-verified: 0 hits in `ops.tsv` (394 ops) and `models/`].
- Its rules (the completed-month gate, the six-check checklist, the fixed wording, "never show the raw classification labels") are rules of behaviour, which the zen forbids.

[official] (Amazon's repo files via `gh api`, read 2026-11-09)

**Amazon's MCP connector** (`https://sellingpartner-ai.amazon.com/mcp`; not called):

- The Claude marketplace listing shows 8 tools: `accounts_getMerchants`, `call_read_only_tool`, `call_write_tool`, `functional_feedback`, `get_tool_schema`, `search_tools`, `sellerAssistant_sellerAssistantCreate`, `sellerAssistant_sellerAssistantGet`. Categories include "Financial services"; it was "Added September 2026" and is "Currently in beta".
- The SP-API operations, `finances_monthEndClosing` among them, sit behind `search_tools` / `call_*_tool`.
- [official] (Claude marketplace, https://claude.com/marketplace/connectors/amazon-selling-partner, saved `web01/claude-connector.html`; aboutamazon, "Published: September 23, 2026": "now available in beta for sellers in Amazon's U.S. stores, with international expansion to follow")
- No public program lets a self-hosted agent like cx register as its client (surface survey §1) [seat]. So it is **not installable in pi as is**, even though `pi-mcp-adapter` could mount an HTTP MCP.

**Seller Assistant (Amazon's AI in Seller Central):**

- The plugin announcement names "listing contributions, real-time performance metrics, inventory levels" and lets sellers bring Amazon data "alongside the rest of their operations, such as financial, marketing, and manufacturing". No Amazon page read says Seller Assistant answers payments, fees, profit, settlement or reimbursement questions. [official, by absence] (aboutamazon 2026-09-23)
- The Seller Assistant help page GLYJTRGQCYNYAZS9 is a JS shell to a plain GET. `sell.amazon.com/seller-assistant` and `/tools/seller-assistant` return 404.

**Borrow-first verdict per source:**

| Source | Installable in pi as is? | Money it covers | What a cx money pack adds |
|---|---|---|---|
| Amazon plugin 1.0.0 (zip) | Skills are markdown and could be copied (Apache-2.0); its MCP is not reachable from cx | Revenue metric only; placement fee shown | Everything about money |
| Amazon `finance-month-end-closer` (repo) | No: it needs the private `finances_monthEndClosing` | Month close against settlements, payout statuses | The same identity rebuilt from public `listSummary` (month and settlement), `listBalances` (`asOfDate`), `listPayouts`, v0 groups, stated as facts without the gates; plus fees, products, deferrals |
| Amazon connector (MCP) | No (US beta, Seller Central OAuth, no third-party client program) | Through private tools | cx's door reaches the public operations directly |
| Seller Assistant | No (in Seller Central) | No money job found | — |
| python-amazon-sp-api / amazon-sp-api npm | Libraries, not pi packages; the door is HTTP, so neither is needed | Paging wrappers; stale or wrong finance paths | Correct paths, windows, field meanings |
| GitHub settlement parsers, profit calculators | No | One author's parsing | — |
| Paid MCPs and ERPs (Sellerboard, Lingxing, Sellfox, AgentXray …) | A seller who pays may connect them as another source | Profit, fees, reimbursements, with the vendor's method | Facts in the seller's own box, no method imposed, at no data charge |

**Settlement history: archived, then re-requested (added 2026-11-10).** Amazon's own help page on this is a JS shell to a plain GET. These are the accounting connectors' words, all read 2026-11-10 [opinion]:

- **A2X** (Why are some of my settlement files missing in A2X?, dateModified 2026-10-13): "Amazon archives older settlement reports after a certain period, which prevents A2X from importing them via the API. You must manually un-archive these reports in Seller Central". Its path is the 2026 Finance workspace: "Finance > Finance Reports", the "Understand Payout" tab, "Click the Request Report button next to the settlement … you should see a Download flat file V2 button". Standard Orders and Invoiced Orders are separate account types to select. "Once the Download flat file V2 button appears, A2X can access the data via th[e API]". https://support.a2xaccounting.com/faqs/why-are-some-of-my-settlement-files-missing
- **A2X** (How far back in time can A2X import Settlements from Amazon?, 2025-10-22): "A2X can import Settlements going back to the beginning of opening your marketplace with Amazon … they need to be unarchived and available for download in Amazon Seller Central." https://support.a2xaccounting.com/en/articles/1137038-how-far-back-in-time-can-a2x-import-settlements-from-amazon
- **Link My Books** (Some of my Amazon settlements are missing, Donna Walker, 2026-10-01): "Amazon archives settlement reports after 90 days." "On the All Statements tab you will see a list of all your past settlements. Older settlements will show a Request Report button — click it to ask Amazon to generate a Flat File V2 report for that settlement period." A row still "In progress more than about 24 hours" after the request means "Amazon hasn't released that settlement's data yet". https://help.linkmybooks.com/en/articles/2817909-some-of-my-amazon-settlements-are-missing
- **Dext Commerce (Greenback)**: "By default, Amazon archives statements after 90 days." "settlement reports may have beginning dates before the dates you request, those reports will need to be unarchived as well." In Europe the other stores' statements and the "Account type" dropdown (invoiced sales) need the same check. "Amazon will archive them again in 90 days". https://commerce.app.dext.com/help/how-do-i-unarchive-amazon-statements/469
- **Blue Onion** (2025-03-05) and **ConnectBooks** (dateModified 2026-10-14) give the same All Statements → Request Report step. ConnectBooks: "When a report is archived, ConnectBooks cannot get its data from the Amazon API." https://intercom.help/blue-onion-labs/en/articles/10714779-how-to-unarchive-amazon-settlements-data-for-historical-data-pulls ; https://help.connectbooks.com/en/articles/8155506-how-to-request-a-settlement-report-from-amazon
- **Webgility** (2025-06-18) puts the line at 120 days: "settlement reports older than 120 days are not automatically available". https://helpcenter.webgility.com/en/why-manual-import-of-amazon-settlement-reports-is-needed-for-periods-over-120-days
- **Improvado** (September 2026): "older settlements are no longer retrievable from the API at all" (re-read 2026-11-10; already in reconciliation.md). The connectors above say an un-archived settlement becomes fetchable again. The two readings disagree on whether a Seller Central request restores API access.
- **Nova** gives figures that disagree with Amazon's own staff posts: "Settlement Report … 3 years", "Date Range Reports … 2 years", "All Statements … 3 years", "Transaction View … 18 months" (Amazon Seller Central Reports: All 50+ Report Types, Antoine, updated 2026-10-14, https://novadata.io/resources/blog/amazon-seller-central-reports-guide), and "Amazon keeps 3 years of history" (Amazon Settlement Report guide, 2026-07-20, https://novadata.io/resources/blog/amazon-settlement-report-guide). Amazon's staff say 24 months for Transaction view and back to 2012 for Date Range reports (§J); A2X says settlements reach back to the account's start.
- **领星 Lingxing** (结算中心 help, https://www.lingxing.com/help/article/SettlementCenter): 「受到SP订单接口和亚马逊settelment report保存时间影响，目前结算中心仅同步最近3个月数据」 ("because of the SP orders interface and how long Amazon keeps the settlement report, the settlement center syncs only the last 3 months"). The same page takes uploads of Seller Central transaction and summary reports and compares them with the API data (「S代表summary，T代表API数据」).
- **ManageByStats** (Getting Older Data): for older history it has the seller generate Seller Central Date Range Transaction reports in blocks of at most six months, which its overnight process then picks up. The six-month block is the vendor's own practice; Amazon's staff post gives 365 days per report. https://managebystats.com/knowledge-base/getting-older-data
- Paid tools cap history by plan, not by Amazon: Link My Books 3 to 24 months by plan tier; Nova "24 months of order and settlement data on paid plans (3 months on a trial)" (How do I export my full Amazon transaction history?, 2026-07-26, https://novadata.io/resources/answers/how-to-export-full-transaction-history).

## Published research

None found on the SP-API finance surface itself. Published accounting research on marketplace settlement is outside this file's scope.

## Stable enough for a skill

1. Amazon keeps three finance views: v0 events, 2024-06-19 transactions, and the settlement report. v0 omits deferred events, 2024-06-19 includes them, and settlement holds released money. Each has a fixed window: 180 days, 180 days, and per settlement period.
2. The 48-hour lag, the 2-minute `postedBefore` floor, empty pages, and the empty answer past 180 days.
3. The `Transaction` shape, the nested breakdowns, and the open `breakdownType`.
4. `FinancialEventGroup` fields, and that `listFinancialEventGroups` survives the v0 removal.
5. (Moved to What cx must read at run time: the removal dates.)
6. Payout and expected-payout status values and meanings, with Amazon's conflicting wording on `PAID`.
7. `initiatePayout` is a money move. Role Mappings: Finance and Accounting or Payment Initiation Service Provider (need at least one), so F&A alone suffices. Its marketplaces and its on-demand limit moved to What cx must read at run time.
8. Settlement reports cannot be requested. The Deferred Transaction Report is requested in Seller Central and then found by `getReports`.
9. The Economics `netProceeds` formula, its seller-entered costs, its fee-change split, P30D, the 2-year look-back and the 120-day preview.
10. The role per read, and the five-role map above.
11. Orders 2026-01-01 carries proceeds and tax collection, but no Amazon fee.
12. The horizons Amazon states (§J): settlement reports listable by `getReports` for about 90 days and never requestable by API; other reports kept 90 days (order reports 30) and generated again on request; v0 by group two years; Deferred Transaction Report up to 10 years, current deferrals only; Economics, Sales and Traffic, Seller Analytics, Orders, order reports and `getOrderMetrics` two years; ledger detail 18 months; `listTransactions`, `listBalances`, `listSummary`, `listPayouts` and `listFinancialEventGroups` state no earliest date.

## What cx must read at run time

| Moves | Where |
|---|---|
| Current, past, deferred and reserved balances | `listBalances` (`balanceType`, `asOfDate`) |
| Next payout, its date and whether it is at risk | `listExpectedPayouts` |
| Past payouts and trace ids | `listPayouts`; v0 `listFinancialEventGroups` (`TraceId`) |
| Each charge and fee on an order or period | `listTransactions` (by `ORDER_ID`, `FINANCIAL_EVENT_GROUP_ID`, date) |
| Whether the `SETTLEMENT_ID` filter works | A live call; the model and the reference say no, the release note says yes |
| Fee amounts and rates | Product Fees estimates; Economics preview; the fee schedules (Seller Central help) |
| Which `breakdownType` / `FeeType` / `feeTypeName` values appear | The replies themselves |
| Seller's own COGS in Amazon | Economics `cost` (null if not entered) |
| Rate actually granted | `x-amzn-RateLimit-Limit` reply header |
| Which roles the app holds, and whether Economics opens under BA | The `403`, or a `createQuery` result |
| Deprecation and removal dates (as read 2026-11-09: settlement v1 2026-11-11, v0 events 2027-08-27, Orders v0 2027-03-27) | SP-API Deprecation Schedule, https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md (the page was last updated 2026-09-09) |
| Which marketplaces the Transfers reads and `initiatePayout` answer in, and the on-demand payout limit (as read 2026-11-09/10: model and references DE, FR, IT, ES, SE, NL, PL, BE; Role Mappings NA, EU, FE for `listPayouts`/`listExpectedPayouts`, EU for `initiatePayout`; one on-demand payout per marketplace and account type per 24 hours) | The call itself for the seller's marketplace; Transfers API, https://developer-docs.amazon/sp-api/docs/transfers-api.md; Role Mappings for SP-API Operations, https://developer-docs.amazon/sp-api/docs/role-mappings.md |
| Seller Central's Transaction view and Date Range report horizons (as read 2026-11-10 in 2024 staff posts: 24 months; 365 days per report, back to 2012) | Quick Tip: Payments Dashboard – Transaction View, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/69b45838-78ce-4403-bfa9-e895f4b89ab4; Where to find your Amazon selling reports, https://sellercentral.amazon.com/seller-forums/discussions/t/5a7d44ff-358e-4c39-a6de-e67aff1a2770 |
| Which marketplaces' order data reaches back past two years (as read 2026-11-10: JP, AU, SG from 2016) | The Orders API 2026-01-01 description in orders_2026-01-01.json (`searchOrders`, `getOrder`) |
| How far back `listTransactions`, `listSummary`, `listBalances` (`asOfDate`) and `listPayouts` answer | A call for an old window; the models state no earliest date |
| Which settlements are archived, and whether an un-archived one appears in `getReports` | `getReports` for `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`; the archive state shows only in Seller Central (All Statements / Understand Payout) |

## What only Seller Central shows

| Seller Central view | Does an API reach it? |
|---|---|
| Payments dashboard, Statement view (balances, recent payouts, next disbursement) | Mostly: `listBalances`, `listSummary`, `listExpectedPayouts`, v0 groups (`BeginningBalance`, `OriginalTotal`). The page layout and its "Other" grouping are not reproduced [seat] |
| Transaction view (24 months, filters) | Yes: `listTransactions`, in 180-day windows |
| Disbursements tab, trace ID | Yes: `listPayouts.traceId`, `FinancialEventGroup.TraceId` |
| Deferred transactions page | Yes: `listTransactions?transactionStatus=DEFERRED` with `DeferredContext.maturityDate`; `listBalances` `DEFERRED`; the Deferred Transaction Report once requested in Seller Central |
| Date Range Reports (summary / transaction, CSV/PDF) | **No report type.** `listSummary` with `periodStart`/`periodEnd` gives a period summary; whether it matches the Date Range summary line for line is unverified |
| Account level reserve: why and for how long | The amount only (`ACCOUNT_LEVEL_RESERVE`, v0 `ReserveEvent`). Not the reason |
| Request Transfer / Express Payout | EU-8 only, via `initiatePayout`. Elsewhere, Seller Central only |
| Deposit method changes | No (EU `getPaymentMethods` reads only) |
| Tax Document Library (US sales-tax report generation, tax forms) | The generated sales-tax report is reachable by `getReports` under Tax Remittance (R). Generation is Seller Central only |
| Fee schedule pages (G200336920, G201074400, GZ8Y22NL2FSRY8M5) | No; JS shells to a plain GET today. Figures come from estimates or the Economics preview |
| COGS entry (SKU Central, Revenue Calculator); manufacturing cost (IDR portal) | Read only (Economics `cost`); no write operation |
| Seller Central Payments page link | `<host>/amazonsell/payments` (Amazon's skill) |
| All Statements / Finance Reports "Understand Payout": settlement list, archive state, "Request Report" for an archived settlement | No operation lists or un-archives a settlement older than `getReports`' 90 days. Connectors say an un-archived settlement is then fetchable by API (§What practitioners add) |
| Date Range reports older than any API window (back to 2012, 365 days per report) | No report type; `listTransactions` states no earliest date, untested |
| Tax Document Library: which tax years it keeps (1099-K and others) | No; Amazon states no number of years on a readable page |

## Facts for human readers only

- 2026-11-09: the v1 settlement reports end in two days (2026-11-11).
- Amazon's fee figures quoted elsewhere in the pack's research (referral percentages, FBA rate cards, the 2026 fuel surcharge) are not repeated here; read them at run time.
- gs.amazon.cn homepage, read 2026-11-09: "按销售额8%-15%收取" (referral fee) and "$39.99即可开通19大站点". sell.amazon.com/pricing: "A Professional selling account is $39.99/month + selling fees."
- 2026-11-10, settlement archiving as practitioners give it (not Amazon's words): 90 days (Link My Books, Dext), 120 days (Webgility); history reachable to the account's start (A2X) or 3 years (Nova). Amazon's own page was not readable.
- 2026-11-10, Seller Central horizons in Amazon staff posts: Transaction view 24 months (2024-01-16); Date Range reports 365 days per report, back to 2012 (2024-10-31). Both posts predate the 2026 Finance workspace; whether the new screens keep them is unverified.

## Pages read

| Title | URL | Date read | Tag |
|---|---|---|---|
| Models clone: finances_2024-06-19, financesV0, transfers_2024-06-01, financesInvoices_2026-06-25, financeRemittance-2026-03-17, sellerWallet_2024-03-01, productFeesV0, sales, orders_2026-01-01, dataKiosk_2023-11-15, notifications schemas, Data Kiosk GraphQL schemas | `~/…/sp-api-plugins/models` @ db2936aa | 2026-11-09 | [command-verified] |
| selling-partner-api-models commits db2936aa, df7c6298 | https://github.com/amzn/selling-partner-api-models | 2026-11-09 | [command-verified] |
| Role Mappings for SP-API Operations | https://developer-docs.amazon/sp-api/docs/role-mappings.md (saved, updatedAt 2026-10-28) | 2026-11-09 | [official] |
| Role Mappings for SP-API Types | …/role-mappings-for-types.md (saved, updatedAt 2026-09-09) | 2026-11-09 | [official] |
| SP-API Deprecation Schedule | https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md (live and saved, updatedAt 2026-09-09) | 2026-11-09 | [official] |
| SP-API Release Notes; changelog RSS | …/sp-api-release-notes.md (updatedAt 2026-11-04); saved `changelog.rss` (to 2026-11-04) | 2026-11-09 | [official] |
| Finances API; Transfers API; Seller Wallet API; Sales API; Product Fees API; Data Kiosk API; Finance Remittance API; Invoices API (2026-06-25); Invoices API (Brazil Only) | developer-docs.amazon/sp-api/docs/… (saved `web01/api/`; Transfers live) | 2026-11-09 | [official] |
| listTransactions / listBalances / listSummary references | https://developer-docs.amazon/sp-api/reference/listtransactions (…/listbalances, …/listsummary), updatedAt 2026-09-10 | 2026-11-09 | [official] |
| Get the latest transactions | …/docs/get-latest-transactions.md, updatedAt 2026-09-24 | 2026-11-09 | [official] |
| Determine which transactions make up a payment | …/docs/determine-payment-transactions.md, updatedAt 2026-09-09 | 2026-11-09 | [official] |
| Settlement reports; Report Type Values; Payment reports; Amazon Business reports | …/report-type-values-settlement.md (2026-10-14); …/report-type-values.md (2026-09-10); …/report-type-values-payment.md (2026-09-09); …/report-type-values-amazon-business.md (2026-09-09) | 2026-11-09 | [official] |
| Notification Type Values | …/notification-type-values.md, updatedAt 2026-10-28 | 2026-11-09 | [official] |
| Get product fees for a batch | …/get-product-fees-batch.md, updatedAt 2026-09-09 | 2026-11-09 | [official] |
| Correction: Data Kiosk role requirements | https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements.md | 2026-11-09 | [official] |
| Cancellation of Third-Party Developer SP-API Fees | https://developer.amazonservices.com/cancellation-of-sp-api-fees (2026-06-11 / 2026-07-01) | 2026-11-09 | [official] |
| Amazon Selling Partner connector | https://claude.com/marketplace/connectors/amazon-selling-partner (saved) | 2026-11-09 | [official] |
| Amazon gives sellers an even smarter Seller Assistant and a new plugin … | https://www.aboutamazon.com/news/innovation-at-amazon/seller-assistant-plugin-amazon-quick-claude (2026-09-23) | 2026-11-09 | [official] |
| Amazon plugin 1.0.0 zip | `~/…/sp-api-plugins/amazon-plugin-zip/` | 2026-11-09 | [command-verified] |
| amzn/selling-partner-agentic-toolkit (README; finance-month-end-closer SKILL.md, reconciliation-notes.md) | https://github.com/amzn/selling-partner-agentic-toolkit | 2026-11-09 | [official] |
| How Amazon seller payments work | https://sell.amazon.com/blog/amazon-seller-payments (2025-07-30) | 2026-11-09 | [official] |
| Seller Central help G200336920, G201074400, GZ8Y22NL2FSRY8M5, GQNVDV46U9JQ25HY, G201355540, G201062540, G202102230, GLYJTRGQCYNYAZS9 | https://sellercentral.amazon.com/gp/help/external/<id> (and .co.uk copies) | 2026-11-09 | JS shell, unreadable |
| sell.amazon.com/seller-assistant; /tools/seller-assistant | — | 2026-11-09 | 404 |
| gs.amazon.cn homepage | https://gs.amazon.cn/ | 2026-11-09 | [official]; no settlement wording |
| saleweaver/python-amazon-sp-api; amz-tools/amazon-sp-api; GitHub search results; npm `keywords:pi-package` searches | github.com / npm | 2026-11-09 | [command-verified] |
| cx-amazon-sp-api origin/main (README, SKILL.md, door.md, prompts); brief-305 work tree `fix/305-door-roles-reports` @ 9b6ad9c | local git | 2026-11-09 | [command-verified] |
| Surface survey notes 01, 02, 04, 07 | `~/…/sp-api-plugins/` | 2026-11-09 | secondary |
| cx-listing-playbook research (sp-api-access, report-lifecycle, seller-central-only-tools) | origin/main | 2026-11-09 (their reads 2026-10-14) | reused |
| ads-playbook `beyond/goals-and-economics.md` | local | 2026-11-09 | overlap (§C–D fees; Economics `netProductSales`) |
| Report Type Values (retention note); Order Reports; FBA Reports; Analytics Reports; Tax Reports; Payment Reports; Settlement Reports (re-read for §J) | https://developer-docs.amazon/sp-api/docs/report-type-values.md (updatedAt 2026-09-10); …/report-type-values-order.md (2026-10-28); …/report-type-values-fba.md (2026-10-13); …/report-type-values-analytics.md (2026-10-28); …/report-type-values-tax.md (2026-11-03); …/report-type-values-payment.md (2026-09-09); …/report-type-values-settlement.md (2026-10-14) | 2026-11-10 | [official] |
| Models: reports_2021-06-30, finances_2024-06-19, financesV0, transfers_2024-06-01, sales, orders_2026-01-01, ordersV0; Data Kiosk schemas (economics, salesAndTraffic, sellerAnalytics), grep for horizons | `~/…/sp-api-plugins/models` @ db2936aa | 2026-11-10 | [command-verified] |
| Quick Tip: Payments Dashboard – Transaction View (Jessica_Amazon_, 2024-01-16) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/69b45838-78ce-4403-bfa9-e895f4b89ab4 | 2026-11-10 | [official, Amazon staff] |
| Quick Tip: Date Range reports (Jessica_Amazon_, 2024-04-17) | https://sellercentral.amazon.com/seller-forums/discussions/t/a53226d8-554a-427d-a0d9-31c52420377d | 2026-11-10 | [official, Amazon staff] |
| Where to find your Amazon selling reports (KJ_Amazon, 2024-10-31) | https://sellercentral.amazon.com/seller-forums/discussions/t/5a7d44ff-358e-4c39-a6de-e67aff1a2770 | 2026-11-10 | [official, Amazon staff] |
| IRS Form 1099-K FAQs (Amazon Pay) | https://pay.amazon.com/help/200831230 (JS shell to curl; read through WebFetch) | 2026-11-10 | [official, Amazon Pay] |
| amzn/selling-partner-agentic-toolkit `finance-month-end-closer` SKILL.md, references, evals.json (grep for windows) | https://github.com/amzn/selling-partner-agentic-toolkit (`gh api` GET) | 2026-11-10 | [official] [command-verified] |
| A2X: Why are some of my settlement files missing; How far back in time can A2X import Settlements | https://support.a2xaccounting.com/faqs/why-are-some-of-my-settlement-files-missing ; https://support.a2xaccounting.com/en/articles/1137038-how-far-back-in-time-can-a2x-import-settlements-from-amazon | 2026-11-10 | [opinion] |
| Link My Books: Some of my Amazon settlements are missing | https://help.linkmybooks.com/en/articles/2817909-some-of-my-amazon-settlements-are-missing | 2026-11-10 | [opinion] |
| Dext Commerce: How do I Unarchive Amazon Statements? | https://commerce.app.dext.com/help/how-do-i-unarchive-amazon-statements/469 | 2026-11-10 | [opinion] |
| Blue Onion; ConnectBooks; Webgility; ManageByStats (settlement and Date Range history) | intercom.help/blue-onion-labs …/10714779; help.connectbooks.com …/8155506; helpcenter.webgility.com …/why-manual-import…-120-days; managebystats.com/knowledge-base/getting-older-data | 2026-11-10 | [opinion] |
| Improvado settlement sunset notice (re-read) | https://improvado.io/product-updates/connectors/amazon-seller-central-settlement-report-sunset | 2026-11-10 | [opinion] |
| Nova: Seller Central reports guide; settlement report guide; export full transaction history | https://novadata.io/resources/blog/amazon-seller-central-reports-guide ; …/blog/amazon-settlement-report-guide ; …/answers/how-to-export-full-transaction-history | 2026-11-10 | [opinion] |
| 领星 help: SettlementCenter (结算中心, FAQ Q2) | https://www.lingxing.com/help/article/SettlementCenter | 2026-11-10 | [opinion] |

## Open questions

These are for a first run on a real account.

1. Does `listTransactions` accept `relatedIdentifierName=SETTLEMENT_ID`? The note says yes; the model and the reference say no after the rollback.
2. Does a Data Kiosk Economics `createQuery` succeed under Brand Analytics, or does it need Selling Partner Insights?
3. Does `TRANSACTION_UPDATE` subscribe under Finance and Accounting? It is unmapped.
4. Do `listBalances` and `listExpectedPayouts` answer in NA and FE for an ordinary seller? Do `accountType` values look like the v0 examples (`Standard Orders`, `Invoiced Orders`)?
5. Does `listSummary` by `SETTLEMENT_ID` equal the settlement report's `total-amount` and the payout amount? And does `listSummary` by month equal Amazon's `lhsMonthNetProceeds`?
6. Which `breakdownType` values appear on this seller's transactions, and do they nest the way v0 charge and fee lists did?
7. Does the Economics dataset return the 2026-09-30 deal, coupon, removal, disposal and fuel fee types by name?
8. Is `getMyFeesEstimates` (batch) refused under F&A alone? Role Mappings lists only Pricing and PL.
9. Is `initiatePayout` eligible for this seller (EU only)?
10. How far back does `listTransactions` answer for this account (a 180-day window two, three and five years back)? The model states no earliest date. The same for `listSummary`, `listBalances` with `asOfDate`, and `listPayouts`.
11. After a settlement is un-archived in Seller Central (All Statements or Finance Reports → Understand Payout → Request Report), does `getReports` list it, with which `createdTime`, and for how long? Connectors say yes; Improvado says no.
12. How far back does this account's All Statements list reach, and does a re-requested old settlement come back as Flat File V2 with the same `total-amount` as the payout of the time?
13. Does the Date Range Transaction report still reach back to 2012 in the 2026 Finance workspace, and does a pre-2025 period come out in the prior format?
14. Which tax years does this account's Tax Document Library list (1099-K, other forms, US sales tax report)?

## Positions

- **P-api-1.** Finances 2024-06-19 `listTransactions` is the current per-transaction money read. It needs Finance and Accounting, is rated 0.5/s with burst 10, and returns transactions whose status is `DEFERRED`, `RELEASED` or `DEFERRED_RELEASED`. (finances_2024-06-19.json; Get the latest transactions; Role Mappings) Read at run time: the `x-amzn-RateLimit-Limit` response header of `listTransactions` gives the rate granted to this seller, the model's Usage Plan only the default.
- **P-api-2.** `listTransactions` needs `postedAfter` unless a related identifier is given. Each bound must be more than two minutes in the past. Bounds more than 180 days apart return an empty response, not an error. Pages can be empty while `nextToken` continues, and the last 48 hours may be missing. (model; listTransactions reference)
- **P-api-3.** The filters Amazon's model supports are `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`, "the only `relatedIdentifier` with filtering capabilities at the moment". The release note of 2026-07-29 announced a `SETTLEMENT_ID` filter. The model carried it only from 2026-10-28 (df7c6298) to the rollback of 2026-10-29 (db2936aa), and the live reference never listed it. `SETTLEMENT_ID` remains a response identifier. (Release Notes; models commits df7c6298, db2936aa; live reference)
- **P-api-4.** A transaction's money is in `totalAmount` and in nested `breakdowns[]`, each of which can hold further `breakdowns[]`. `breakdownType` is an open string with no closed list from Amazon, and amounts are signed decimals. (model; Get the latest transactions)
- **P-api-5.** For US MFN orders, `listTransactions` is called without `marketplaceId`. (model)
- **P-api-6.** The transactions of one payout come from v0 `listFinancialEventGroups` (its `FinancialEventGroupId`), then `listTransactions` with `FINANCIAL_EVENT_GROUP_ID` and `RELEASED`. (Determine which transactions make up a payment)
- **P-api-7.** `listBalances` gives current or past (`asOfDate`) balances by type: `AVAILABLE`, `RESERVED`, `TOTAL`, `DEFERRED`, `ACCOUNT_LEVEL_RESERVE`. Sub-balances are by account type and marketplace, and `lastUpdatedTime` is in marketplace local time. (model; listBalances reference)
- **P-api-8.** `listSummary` gives `netProceeds` with `breakdowns` for a date period or for one `SETTLEMENT_ID`. (model; listSummary reference)
- **P-api-9.** Finances v0 `listFinancialEvents`, `ByGroupId` and `ByOrderId` are removed on 2027-08-27. `listFinancialEventGroups` is not scheduled for removal. v0 omits deferred events until release, and by-group covers only the past two years. (Deprecation Schedule; financesV0.json) Read at run time: SP-API Deprecation Schedule, https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md.
- **P-api-10.** A v0 `FinancialEventGroup` carries the settlement period's open or closed status, beginning balance, total ("For an open financial event group, this is the current balance"), fund transfer date (closed only), and trace id. (financesV0.json)
- **P-api-11.** Transfers `listPayouts` and `listExpectedPayouts` (Finance and Accounting) give past payouts and the next expected one. Role Mappings (2026-10-28) give them "Regions NA, EU, FE"; the Transfers model text and the live `listPayouts` / `listExpectedPayouts` references (updatedAt 2026-09-10) say "This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE." The two Amazon texts disagree. They carry the status values Amazon defines (`STARTED`…`NO_PAYOUT`; `SCHEDULED`, `DISABLED`, `AT_RISK`, `NO_PAYOUT_EXPECTED`), the trace id and the settlement id. (transfers model; Transfers API page; Role Mappings 2026-10-28; listPayouts and listExpectedPayouts references as read in money-flow.md, 2026-11-10) Read at run time: a `listPayouts` or `listExpectedPayouts` call for the seller's own marketplace, with Amazon's current text in Transfers API, https://developer-docs.amazon/sp-api/docs/transfers-api.md, and Role Mappings for SP-API Operations, https://developer-docs.amazon/sp-api/docs/role-mappings.md.
- **P-api-12.** Amazon's words on `PAID` disagree. The Transfers model says "successfully deposited in the bank"; Amazon's month-end skill says it "does not prove the deposit reached the bank". Amazon's blog says funds can take up to five business days to appear. (transfers model; amzn toolkit; sell.amazon.com blog) Read at run time: How Amazon seller payments work, https://sell.amazon.com/blog/amazon-seller-payments, for the US store; for another marketplace no operation or page read gives it, and the value stands as read on 2026-11-09, US.
- **P-api-13.** `initiatePayout` moves money. It is available in DE, FR, IT, ES, SE, NL, PL and BE, with "one on-demand payout for each marketplace and account type within a 24-hour period". Role Mappings give Regions "EU" and "Required roles (need at least one)": Finance and Accounting, or Payment Initiation Service Provider. Finance and Accounting alone is therefore enough. (transfers model; Role Mappings 2026-10-28) Read at run time: the `initiatePayout` operation (its description in transfers_2024-06-01.json and its reply for the seller's marketplace and account type), with the marketplaces in Transfers API, https://developer-docs.amazon/sp-api/docs/transfers-api.md, and Role Mappings for SP-API Operations, https://developer-docs.amazon/sp-api/docs/role-mappings.md.
- **P-api-14.** Seller Wallet (AISP/PISP), Finance Remittance (vendors), Invoices v2026-06-25 (vendors) and Invoices v2024-06-19 (Brazil FBA invoices, Tax Invoicing) are not the ordinary seller disbursement. (their API pages and models)
- **P-api-15.** `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` is the settlement report that remains (Finance and Accounting). Amazon schedules it; it cannot be requested and is found with `getReports`. The flat-file v1 and XML reports are removed on 2026-11-11. (Settlement reports; Deprecation Schedule; Role Mappings for Types) Read at run time: SP-API Deprecation Schedule, https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md.
- **P-api-16.** The settlement V2 columns are the 24 Amazon lists. Amounts sit in one `amount` column, described by `amount-type` and `amount-description`. (Settlement reports)
- **P-api-17.** `GET_DATE_RANGE_FINANCIAL_HOLDS_DATA` is Amazon's Deferred Transaction Report. It is point-in-time, covers up to 10 years, and must first be requested in Seller Central's Payments Reports Repository before the Reports API retrieves it. No report type matches Seller Central's Date Range Reports. (Payment reports; Report Type Values)
- **P-api-18.** The role for each money report type is the one Role Mappings for Types gives. Overage fee, customer shipment sales and the ledger need Amazon Fulfillment. Reimbursements, storage, aged-inventory surcharge, returns, removal and FBA fee preview accept Pricing or Amazon Fulfillment. Referral fee preview and settlement need Finance and Accounting. US sales tax needs Tax Remittance (Restricted), and EU VAT needs Tax Invoicing (Restricted). (Role Mappings for Types)
- **P-api-19.** Product Fees estimates are "not guaranteed". A SKU estimate uses measured dimensions once the item is at Amazon; an ASIN estimate uses catalog size. A batch takes up to 20 items and accepts only Pricing or Product Listing. (productFeesV0.json; Product Fees API; batch guide; Role Mappings)
- **P-api-20.** Orders v2026-01-01 carries proceeds (`grandTotal`, item `proceedsTotal`, breakdowns by `ITEM`, `SHIPPING`, `GIFT_WRAP`, `COD_FEE`, `TAX`, `DISCOUNT`, `DELIVERY_TIP`, `OTHER`), tax collection model and payment executions, but no Amazon fee. Orders v0 reads are removed on 2027-03-27. (orders_2026-01-01.json; Deprecation Schedule) Read at run time: SP-API Deprecation Schedule, https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md.
- **P-api-21.** Sales `getOrderMetrics` gives ordered `totalSales`, units and orders per interval, for one marketplace, with `asin` or `sku` but not both. It is open under Product Listing. (sales.json; Role Mappings)
- **P-api-22.** Data Kiosk Economics gives per-product sales, fees by type, ads, the seller's own entered costs and `netProceeds`, by Amazon's stated formula. It is refreshed daily, reaches two years back, splits at fee-change dates and is retained 30 days. Its preview reaches 120 days ahead. (analytics_economics_2024_03_15.graphql)
- **P-api-23.** Amazon's pages disagree on the role for Economics: Brand Analytics (Role Mappings, the Data Kiosk page) or Selling Partner Insights (the correction). The live `createQuery` result decides it. (Role Mappings; correction page)
- **P-api-24.** `TRANSACTION_UPDATE` is sent "whenever there is a new transaction posted"; Role Mappings for Types does not list it. `FEE_PROMOTION` needs Finance and Accounting or Product Listing. Both deliver to SQS or EventBridge destinations. (Notification Type Values; Role Mappings for Types)
- **P-api-25.** Amazon cancelled the planned SP-API usage and annual fees: "we will not move forward with the SP-API usage and annual fees at this time". (Cancellation of SP-API Fees, 2026-06-11)
- **P-api-26.** Amazon's own Claude plugin 1.0.0 carries no money skill. Its month-end reconciliation skill (`finance-month-end-closer` 1.3.1, `skills/finance-month-end-closer/` in `amzn/selling-partner-agentic-toolkit`, committed 2026-10-08, merged 2026-10-12) runs on a private tool, `finances_monthEndClosing`, that no public model has. Its stated facts are borrowable as facts: the settlement classes, negative settlements counting as zero and carrying forward, the payout amount equal to settlement net proceeds, and that an open balance is not a guaranteed payout. (amzn toolkit; plugin zip; ops.tsv)
- **P-api-27.** No pi package for Amazon money exists, and the public SP-API clients lag the finance models. One maps 2024-06-19 calls to paths that are not in Amazon's model. (npm and GitHub reads) [command-verified]
- **P-api-28.** The door `cx-amazon-sp-api` already carries every money operation above under the roles the seller ticked. Its reference names Finance and Accounting for `listTransactions`. The brief-305 work adds the reports lifecycle, the settlement facts and Amazon Fulfillment. (door.md at origin/main and 9b6ad9c)
- **P-api-29 [seat].** For a money question, the door alone gives the raw calls. A money pack adds:
  - which of the five views answers which question;
  - the windows and lags;
  - the field meanings;
  - the role map;
  - the reconciliation identities Amazon states.

  It enters no skill as a rule.

- **P-api-30.** `getReports` lists reports created in the last 90 days: "The default is 90 days ago. Reports are retained for a maximum of 90 days." Settlement reports "cannot be requested or scheduled", so through the API alone a settlement report is retrievable only inside that window. Other report types not downloaded in time can be generated again ("If the generated report is not downloaded within the retention period, you can generate the report again"); order reports are kept 30 days. (reports_2021-06-30.json; Settlement Reports; Report Type Values; Order Reports)
- **P-api-31.** Accounting connectors state that Amazon archives older settlement reports: after 90 days (Link My Books, Dext), 120 days (Webgility). A "Request Report" click in Seller Central (Payments → All Statements; in the 2026 Finance workspace, Finance Reports → "Understand Payout") regenerates a Flat File V2 for that period, after which their API imports work (A2X, Link My Books, ConnectBooks, Blue Onion). Dext says the report is archived again after 90 days, and A2X says history reaches back to the account's start. Improvado says older settlements are "no longer retrievable from the API at all". Amazon's own page was not readable. [opinion] (pages in §What practitioners add) No operation or page gives this; the value stands as read on 2026-11-10, marketplace not stated by the connectors.
- **P-api-32.** Seller Central's transaction-level horizons in Amazon staff words: Transaction view, "Only transactions from the last 24 months are available to review"; Date Range reports, "up to 365 days at a time, going back as far as 2012", each taking "up to three hours". Date Range reports for periods before 2025-01-01 keep the prior format. Nova's figures (Transaction view 18 months, Date Range 2 years, settlements 3 years) disagree with these. (Quick Tip: Transaction View, 2024-01-16; Where to find your Amazon selling reports, 2024-10-31; News_Amazon 2026-03-18; Nova [opinion]) Read at run time: Quick Tip: Payments Dashboard – Transaction View, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/69b45838-78ce-4403-bfa9-e895f4b89ab4, and Where to find your Amazon selling reports, https://sellercentral.amazon.com/seller-forums/discussions/t/5a7d44ff-358e-4c39-a6de-e67aff1a2770.
- **P-api-33.** Of the API finance reads, only v0 `listFinancialEventsByGroupId` states a history limit: "the past two years", with an empty response past it. `listTransactions`, `listFinancialEvents`, `listFinancialEventsByOrderId`, `listFinancialEventGroups`, `listBalances` (`asOfDate`), `listSummary` and `listPayouts` state no earliest date; where stated, the limit is a 180-day span per call. (financesV0.json; finances_2024-06-19.json; transfers_2024-06-01.json) [command-verified]
- **P-api-34.** Per-product and order data stops at two years: the Economics, Sales and Traffic and Seller Analytics datasets ("no more than two years ago"), `GET_SALES_AND_TRAFFIC_REPORT`, `getOrderMetrics` (30 days at hourly granularity), the Orders API (JP, AU and SG from 2016) and order reports ("less than two years old"). Data Kiosk results are kept 30 days. The Inventory Ledger detail holds 18 months of unit movements. (Data Kiosk schemas; sales.json; orders models; Analytics, Order and FBA Reports pages) Read at run time: the Orders API 2026-01-01 description in orders_2026-01-01.json, which `searchOrders` and `getOrder` carry, names the marketplaces whose order data reaches back further.
- **P-api-35.** The Deferred Transaction Report covers "up to 10 years of data" but is "point-in-time": it lists what is deferred when it is generated, and "When a transaction is updated from deferred to released, it will no longer be included". `listBalances` with `asOfDate` and `balanceType=DEFERRED` gives the deferred amount at a past date. (Payment Reports; News_Amazon UK 2024-10-04; finances_2024-06-19.json)
- **P-api-36.** A VAT transaction report generated again for the same range "can return updated records" (marked by `transaction_update_date`). Its `dataEndTime` must be at least three days before the request, and it needs Tax Invoicing (Restricted). India's On Demand GST MTR B2C report "only provides data for the last 45 days". (Tax Reports, updatedAt 2026-11-03) Read at run time: Tax Reports, https://developer-docs.amazon/sp-api/docs/report-type-values-tax.md.
- **P-api-37.** Amazon states no number of years for the Tax Document Library. The US sales tax report is generated there and then found with `getReports`. 1099-K forms are found by year ("Select the appropriate year"), by the primary user only (Amazon Pay's 1099-K FAQ). Amazon's `finance-month-end-closer` states no look-back window. (Tax Reports; IRS Form 1099-K FAQs, pay.amazon.com; amzn toolkit)
- **P-api-38.** 领星 Lingxing's settlement center syncs only the last three months, which it puts down to the SP orders interface and Amazon's settlement report retention. It accepts uploaded Seller Central transaction and summary reports and compares them with its API data. ManageByStats rebuilds older history from Date Range Transaction reports the seller generates. Paid tools cap history by plan (Link My Books 3 to 24 months; Nova 24 months on paid plans). [opinion] (Lingxing SettlementCenter; ManageByStats; Link My Books; Nova)

### Our door: what it gives, what a pack adds, what it lacks (follow-ups; nothing changed)

- **origin/main** (`7409b41`):
  - README line 1: "cx … breaks down each transaction's fees". The example ask is "Which fees did Amazon take from last month's sales?".
  - `door.md`: four roles; reports by `createReport`/`DONE`; no money report type named; Finance and Accounting tied to `listTransactions`.
  - Prompts: `/listing-check`, `/low-stock`, `/orders-today` (order totals in each currency); none is a money prompt.
- **Brief 305** (`fix/305-door-roles-reports`, head `9b6ad9c`, +60 −8 over six files):
  - adds Amazon Fulfillment as the fifth role and lists what it opens (incl. `GET_FBA_OVERAGE_FEE_CHARGES_DATA`, `…CUSTOMER_SHIPMENT_SALES_DATA`);
  - moves the example to `searchOrders`;
  - adds the Reports lifecycle, 90-day retention, and the settlement facts with the 2026-11-11 removal;
  - adds Data Kiosk limits.
- **The door alone already gives a money question:** any Finances, Transfers, Product Fees, Orders, Reports or Data Kiosk call under the seller's roles, and Amazon's reply as given.
- **A money pack adds past that:** the facts in this file (views, windows, pitfalls, statuses, formulas, roles), plus the fee, payout and earnings facts of the sibling seats.
- **What the door lacks for money** (follow-ups for the door's owner):
  1. `door.md` (305) says "Amazon's Data Kiosk guide lists Brand Analytics for each dataset". Amazon's correction gives Economics to Selling Partner Insights, so the conflict could be named.
  2. The door names no money report type beyond settlement: not the Deferred Transaction Report's Seller-Central-first request, nor the restricted tax reports' roles.
  3. The door's README promise "breaks down each transaction's fees" rests on `listTransactions` breakdowns, whose types Amazon leaves open. That is a pack fact, not a door fact.
  4. `initiatePayout` moves money in the EU under Finance and Accounting, which the door holds. The door has no write switch, so the reference could state that fact (no rule).
  5. Notifications need an SQS or EventBridge destination; the door has none to offer. `TRANSACTION_UPDATE` is therefore not a live feed for cx today [seat].

## Verification

Verified 2026-11-09/10 by the verifier seat (brief 306, `_verify.md`).

**What was checked**
- The `SETTLEMENT_ID` rollback, against the clone (db2936aa) and the commit history of `finances_2024-06-19.json` through `gh api` (read-only GET). Commits read: dcb0ef91 (2026-07-29), 4be88722 and af0be99a (2026-07-30), df7c6298 (2026-10-28), db2936aa (2026-10-29).
- The live listTransactions reference (updatedAt 2026-09-10): filter text with two values; `storeName` enum `AMAZON_HAUL` only. Release Notes (updatedAt 2026-11-04) and the 2026-10-21 changelog: the `AMAZON_FBA_FROM_ORIGIN` text was quoted from the page.
- Transfers rates and `info.description` from the model. Every Transfers, Finances and v0 role row in `web01/role-mappings.md`; the live Role Mappings page is identical in the Transfers block (updatedAt 2026-10-28). Notification roles in `role-mappings-for-types.md`.
- Amazon's `finance-month-end-closer`, read-only through `gh api`: `SKILL.md`, `references/reconciliation-notes.md`, `references/seller-central-urls.md`, the commit list and the repository metadata. Nothing was run. The local plugin zip has no copy (0 grep hits).
- Invoices API page ("Availability … Vendors only"; "The Selling Partner API for Invoices is available for vendors."; roles: Finance and Accounting). Finance Remittance API page ("Vendors only"; "programmatic access to vendor payment remittance data"). The Data Kiosk role correction ("The Economics dataset requires the Selling Partner Insights role").

**Changes made (old → new, why, source)**
1. Dated changes: "2026-10-08: Amazon adds a skill" → committed 2026-10-08 (11d828ad), merged 2026-10-12 (PR #7). Added a 2026-10-28 entry: the October release introduced the filter and the store name. Source: `gh api` commit lists.
2. A3: added that the model never carried the filter from July to October, and that the October changelog still announces `AMAZON_FBA_FROM_ORIGIN`.
3. C2 and the toolkit bullets: the `PAID` quote was a paraphrase ("Amazon `PAID` means Amazon processed the payout — it does **not** prove …"). Replaced with the file's words: "`PAID` (**Amazon processed the payout — this does NOT prove the deposit reached the bank**)" and "Amazon `PAID` ≠ received". The "not a guaranteed future payout" quote was replaced with both of the file's wordings.
4. Toolkit: location, files, frontmatter and the optional `toolVersion` parameter added (the old text listed only `accountType`). Added the reconciliation-trail identity and "decimal strings".
5. One table and Stable 7: "F&A; PISP (EU)" and "F&A suffices" → "F&A or PISP, any one (EU)", quoting Role Mappings' "need at least one". The same change applies to `getPaymentMethods`.
6. **P-api-3**, **P-api-13**, **P-api-26** reworded as above. No meaning reversed. P-api-3 now dates the filter's one day in the model.
7. C4: added the Remittance start-date conflict between the model (one year back) and the guide (from 2024-01-01).

**Positions checked:** 29. Changed: 3 (P-api-3, 13, 26). Made [seat]: 0 (P-api-29 already was). Removed: 0. D233 check: P-api-26 states the toolkit's facts and calls its gates rules of behaviour, which are not borrowed. No position imposes a sequence or threshold. P-api-6 is Amazon's documented recipe, stated as a fact about Amazon's guide.

**Could not verify**
- What `finances_monthEndClosing` computes internally beyond the skill's description, including "confirmed invariant" (payout = settlement `netProceeds`). That is Amazon's claim in a skill file, not a model. Its eval file was not read.
- Whether `listPayouts`/`listExpectedPayouts` answer in NA/FE. The model's `info.description` names EU8; Role Mappings say NA, EU, FE.

**Gaps left**
- The Seller Assistant's money answers: help page GLYJTRGQCYNYAZS9 is a JS shell.
- No live check of `x-amzn-RateLimit-Limit` on finance operations (limits forbid API calls).
- The 2026-06-29 Finances release-note link is still unresolved (reconciliation open question 11).

### Gap fill (2026-11-10)

Filled by the research seat against the completeness critics' gap "how far back each Amazon money document reaches". The file did not hold this in one place before: the 90-day, two-year and 10-year horizons were in §B, §F and §G, and the Seller Central horizons were not sourced here.

**Added**
- §J, a table of every money document's horizon, with Amazon's words, and five facts drawn from it.
- What this covers: a line pointing to §J.
- What practitioners add: settlement archiving and re-requesting (A2X, Link My Books, Dext, Blue Onion, ConnectBooks, Webgility, Improvado), Nova's conflicting figures, 领星's three-month sync, ManageByStats' Date Range rebuild.
- Stable enough for a skill: item 12.
- What cx must read at run time: two rows (earliest date each API read answers; archived settlements in `getReports`).
- What only Seller Central shows: three rows (All Statements un-archive, Date Range history, Tax Document Library years).
- Facts for human readers only: the practitioners' archive days and the staff-post dates.
- Pages read: 14 rows. Open questions: 10–14. Positions: P-api-30 to P-api-38.

**Corrections to sibling files (not edited here)**
- reconciliation.md P-rec-6 says older settlements are "downloadable only in Seller Central". The connectors say an un-archived settlement becomes fetchable through the API again (P-api-31); Improvado says the opposite. Open question 11.
- The survey note `04-job-money.md` §1 already gave Transaction view 24 months; the staff post was re-read and agrees (2024-01-16).
- Nova's retention table (Transaction view 18 months, Date Range 2 years) disagrees with Amazon's staff posts; it is recorded as opinion only.

**Gaps left**
- How far back Seller Central's All Statements lists settlements: no readable Amazon page. Practitioners differ (A2X: the account's start; Nova: 3 years).
- The archive threshold for settlements (90 or 120 days) in Amazon's own words: the help page is a JS shell.
- Tax Document Library: how many tax years of 1099-K and other forms it keeps, and how long EU VAT invoices (VCS) stay downloadable. No Amazon page read states either.
- Whether `listTransactions`, `listSummary`, `listBalances` (`asOfDate`) and `listPayouts` answer for windows older than two years. The models state no limit; only a live call tells.
- Statutory record-keeping periods (tax and accounting law per country) are outside this file and were not researched.

### Correction 1 (2026-11-10)

Applied by the research seat under brief 306 correction 1 and the plugin zen's item 4 (a value that differs by marketplace or changes from year to year is read where Amazon gives it, not carried). Nothing was re-researched; no Amazon API host and no help-hub page was called. Names were checked against the models clone at db2936aa: `x-amzn-RateLimit-Limit` on every Finances, Transfers and Orders operation; the Transfers `info.description` and the `initiatePayout` 24-hour sentence; the Orders 2026-01-01 `info.description` (JP, AU, SG from 2016) [command-verified].

**Positions changed** (each keeps its value as evidence and ends with where it is read, or with "No operation or page gives this"):
- P-api-1: the rate (0.5/10) is read from the `x-amzn-RateLimit-Limit` header of `listTransactions`.
- P-api-9, P-api-15, P-api-20: the removal dates are read from the SP-API Deprecation Schedule.
- P-api-11: aligned with money-flow.md (P-flow-22 and its Transfers section). It now states both texts: Role Mappings (2026-10-28) "Regions NA, EU, FE" for `listPayouts`/`listExpectedPayouts`, and the Transfers model and live references "This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE." Where they answer is read by the call for the seller's marketplace, the Transfers API page and Role Mappings.
- P-api-12: the five business days to the bank are read from How Amazon seller payments work for the US store; for other marketplaces no page read gives it.
- P-api-13: the marketplaces and the 24-hour on-demand limit are read from `initiatePayout`, the Transfers API page and Role Mappings.
- P-api-31: the settlement archive threshold (90 or 120 days) has no readable Amazon page; it stands as read on 2026-11-10.
- P-api-32: the Transaction view and Date Range horizons are read from the two Amazon staff posts.
- P-api-34: the marketplaces whose order data reaches past two years are read from the Orders API 2026-01-01 description.
- P-api-36: the EU VAT and India GST report windows are read from Tax Reports.

**Stable enough for a skill → What cx must read at run time**: item 5 (removal dates) moved whole; item 7 lost the EU-8 marketplaces and the 24-hour limit; item 12 lost the Transaction view and Date Range horizons and the JP/AU/SG exception. Three run-time rows added and the Deprecation row widened, each with the value as read.

**Left untouched, and why**: P-api-3, P-api-25 and P-api-26 carry facts of history (an announcement, a rollback, a cancellation, commit dates). The windows, page sizes and retention stated in an operation's own model or developer page as its contract (180 days, two minutes, 48 hours, 90-day `getReports`, 30-day order reports, 10-year Deferred Transaction Report, the 20-item fee batch, Economics' two years and 120 days) were judged API facts, not marketplace or yearly values (P-api-2, 17, 19, 22, 30, 33, 35). P-api-38's limits are vendors' plan caps, not Amazon values.
