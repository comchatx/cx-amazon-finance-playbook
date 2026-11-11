# Roles, notifications and the tools around the money reads

## Roles

- Role Mappings name Finance and Accounting for `listTransactions` (P-api-1).
- Role Mappings name Finance and Accounting for Transfers `listPayouts` and `listExpectedPayouts` (P-api-11).
- `initiatePayout` takes Finance and Accounting or Payment Initiation Service Provider, any one (P-api-13).
- Role Mappings list only Pricing or Product Listing for the batch fee estimate `getMyFeesEstimates`; whether a call under Finance and Accounting alone is refused is not yet seen on a live account (P-api-19).
- `getOrderMetrics` is open under Product Listing (P-api-21).
- Amazon's pages disagree on the role for Data Kiosk Economics: Brand Analytics per Role Mappings, Selling Partner Insights per Amazon's correction; the live `createQuery` result decides it; read in Amazon's documents, not yet seen on a live account (P-api-23).
- The role for each money report type is the one Role Mappings for Types gives (P-api-18).
- Storage, aged-inventory surcharge, reimbursements and FBA fee preview take Amazon Fulfillment or Pricing; the ledger reports take Amazon Fulfillment only; settlement V2 takes Finance and Accounting; read in Amazon's documents, not yet seen on a live account (P-tool-26, P-api-18).
- Seller Wallet sits under the Account Information and Payment Initiation Service Provider roles (AISP/PISP), and is not the ordinary seller disbursement (P-api-14).

## Notifications

- `TRANSACTION_UPDATE` is sent "whenever there is a new transaction posted", and Role Mappings for Types do not list it; read in Amazon's documents, not yet seen on a live account (P-api-24).
- `FEE_PROMOTION` needs Finance and Accounting or Product Listing (P-api-24).
- Both notifications deliver to Amazon SQS or EventBridge destinations (P-api-24).

## SP-API fees

- Amazon cancelled the planned SP-API usage and annual fees: "we will not move forward with the SP-API usage and annual fees at this time" (P-api-25).

## Amazon's own tools

- Amazon's own Claude plugin 1.0.0 carries no money skill (P-api-26).
- Amazon's month-end skill and the facts it states: references/payouts.md.

## Clients

- No pi package for Amazon money was found on npm or GitHub, and the public SP-API clients lag the finance models (P-api-27).
- One public client maps Finances 2024-06-19 calls to paths that are not in Amazon's model (P-api-27).
- The door `cx-amazon-sp-api` carries the money operations under the roles the seller ticked, and its reference names Finance and Accounting for `listTransactions` (P-api-28).
