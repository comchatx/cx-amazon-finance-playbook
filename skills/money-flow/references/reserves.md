# Account Level Reserve and the balance types

## What Amazon says the reserve holds

- Amazon describes the Account Level Reserve as a sum of per-order holds by reason. (P-flow-7)
- The reasons Amazon names are delivery-date reserves (and, during the 2026 transition, delivery-date policy amounts), open A-to-z claims, recent chargebacks, performance below benchmarks, an account under review, and local income-tax withholding. (P-flow-7)
- The chargebacks counted fall within a window Amazon states; research/areas/money-flow.md, P-flow-7, holds the value as read. (P-flow-7)
- An account under review includes a new seller whose delivery times exceed the settlement period. (P-flow-7)
- Amazon publishes no percentage and no timeframe for the Account Level Reserve, and every seller is subject to it. (P-flow-7)
- During the 2026 transition, Amazon says delivery-date amounts "may temporarily" sit inside Account Level Reserve instead of showing as deferred transactions. (P-flow-10)

## Rules in circulation

- The percentage-of-sales reserve rules practitioners circulate are not in any current Amazon page reached. (P-flow-8)
- One such rule is reproduced by AMZ123 (2022) as text of Amazon's old payments FAQ, second-hand; the tier rules are vendors' claims (Payability, SellersFi). research/areas/money-flow.md, P-flow-8, holds the rules as read. (P-flow-8)
- No current Amazon page publishes an Account Level Reserve formula. (P-flow-8)
- Lingxing describes Amazon's reserve as a share of the store's recent sales, says the reserve amount cannot be predicted, and says Amazon gives no real-time reserve amount; research/beyond/sellers-tools-and-research.md, P-tool-21, holds its figure as read. (P-tool-21)
- Lingxing's description is a vendor's, not Amazon's rule, and no operation or page read gives the rule behind the amount. (P-tool-21)
- The amount held on the seller's account is read from `listBalances` (`ACCOUNT_LEVEL_RESERVE`, `RESERVED`, `DEFERRED`) and from the `Current Reserve Amount` and `Previous Reserve Amount Balance` lines of `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`; these `amount-description` names are read in Amazon's documents, not yet seen on a live account. (P-tool-21)

## Where the reason is

- The reason for each reserve amount is shown on Statement View in Seller Central. (P-flow-9)
- `listBalances` returns the reserve amount with no reason field. (P-flow-9)

## Balance types

- `listBalances` returns `AVAILABLE`, `RESERVED`, `ACCOUNT_LEVEL_RESERVE`, `DEFERRED` and `TOTAL` balances by account type and store, current or as of a date. (P-flow-21)
- `lastUpdatedTime` in `listBalances` is in the store's local time zone. (P-flow-21)
- Amazon defines `ACCOUNT_LEVEL_RESERVE` as "Based on sales volume, product category, and account history" and `RESERVED` as the sum of Deferred and Account Level Reserve. (P-flow-40)
- In the v0 model, a reserve taken when a settlement period closes is an `AdjustmentEvent` of type `ReserveEvent`. (P-flow-16)
- The withheld reserve becomes the next period's beginning balance, and the beginning balance includes reserves and failed disbursements. (P-flow-11)
