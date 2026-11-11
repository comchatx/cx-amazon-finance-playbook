# Clocks, posting dates, deferral and reserves

## What each document counts

- A settlement covers released money in one payout period, and only disbursed transactions enter settlement reports. (P-rec-8)
- Deferred transactions are not in a settlement until they are released; A2X says the same. (P-rec-8)
- The settlement counts released transactions by payout period. (P-rec-31)
- The Date Range reports count posted transactions by local posted date, deferred ones included from 2026. (P-rec-31)
- Business Reports and the economics dataset count ordered sales by order date. (P-rec-31)
- `listTransactions` counts every posted transaction by UTC posted date. (P-rec-31)
- A month's figure from one of these does not equal another's; Nova (a vendor) puts the month-boundary gap at 2 to 4 days. (P-rec-31)
- Amazon's staff give the cross-reference route: find an order's posted date in Transaction view, then find the payment in the Settlement or Date Range report by that date. (P-rec-30)

## Clocks

- Settlement `posted-date-time` is UTC. (P-rec-15)
- Date Range reports run from 12:00 a.m. to 11:59 p.m. local time. (P-rec-15)
- Amazon states that `listSummary` "is calculated based on the marketplace timezone of the seller, not UTC". (P-rec-15)
- `listBalances.lastUpdatedTime` is in the marketplace's local time. (P-rec-15)
- A transaction near midnight can fall on different dates in each of these. (P-rec-15)

## Date Range reports

- Date Range Transaction (CSV) and Summary (PDF) reports are requested in Seller Central's Payments or Finance Reports Repository. (P-rec-17)
- They cover transactions by the date posted to the account, which Amazon says "may not correspond to the order date or the shipment date". (P-rec-17)
- Amazon's staff say they can take up to three hours to generate. (P-rec-17)
- From 2026, for periods from 2025-01-01, the Date Range Transaction and Summary reports include deferred and released transactions, with Date/Time as the posted date. (P-rec-18)
- The Transaction report gained a deferred/released status column and a Transaction Release Date, blank while a transaction stays deferred. (P-rec-18)
- The rollout was US/CA/MX/BR by 2026-04-30, BE/FR/DE/IE/IT/NL/PL/ES/SE/IN/EG/SA/TR/AE/UK from 2026-03-23 to 2026-05-31, and other stores by 2026-06-30. (P-rec-18)
- Periods before 2025-01-01 keep the old format. (P-rec-18)
- Amazon's Report Type Values page lists no SP-API report type for the Date Range Transaction or Summary report; under Payment it lists only `GET_DATE_RANGE_FINANCIAL_HOLDS_DATA`. (P-rec-19)

## The Deferred Transaction report

- `GET_DATE_RANGE_FINANCIAL_HOLDS_DATA` is a point-in-time CSV of currently deferred transactions; its reach is stated on Payment Reports. (P-rec-20)
- A transaction that moves from deferred to released leaves the report. (P-rec-20)
- Amazon states the API can retrieve it only after the seller requests it in Seller Central's Payments Reports Repository; whether `getReports` then finds it is read in Amazon's documents, not yet seen on a live account. (P-rec-20)
- Amazon's reply on GitHub #4830 says the same behaviour holds for other reports and that its team is looking into improving it. (P-rec-20)
- The Payment Reports page gives the report Finance and Accounting, and Role Mappings for Types does not list it. (P-rec-7)

## Report timing changed twice

- From late October 2024, deferred sales entered the Transaction and Summary reports on release; from 2026, by posted date with status columns. (P-rec-34)
- Amazon did not restate past reports, so a comparison across these dates carries the shift. (P-rec-34)
- Per practitioners (Finaloop, Bookkeep), the US 1099-K follows the deferred/posted timing. (P-rec-34)

## The delivery-date reserve

- Under the delivery-date reserve policy, funds are deferred at shipment, become reserves on delivery, and move to the balance when the policy's period ends. (P-rec-21)
- The delivery date is the tracked delivery (at least one physical carrier scan) or, without valid tracking, the latest estimated delivery date (handling plus transit time). (P-rec-21)
- Amazon's English and Chinese worked examples disagree on the day count; a transaction's own release date is its `maturityDate`. (P-rec-21)
- Invoiced (B2B) orders are also deferred, and `DeferredContext.deferralReason` names the delivery-date reserve or B2B, with enum values as in the model (for example `B2B`). (P-rec-21)
- The reserve period for the seller's own marketplace is read per transaction from `listTransactions` (`DeferredContext.deferralReason` and `maturityDate`, against `postedDate`), and the deferred total from `listBalances` (`DEFERRED`). (P-rec-21)
- Amazon moved the remaining accounts to the policy on the date each account's e-mail gave; no Amazon page gives those dates, which are known only from e-mails sellers pasted in Seller Forums. (P-rec-21)
- Reserves of this policy held in the account-level reserve before an account's switch were not moved into deferred transactions, so both can carry such money in the transition (Amazon's Chinese explainer; Sellfox). (P-rec-39)

## Account-level reserve

- An account-level reserve is distinct from a deferred transaction, and can remain for a claim, a chargeback or an account review. (P-rec-22)
- Amazon reports it as `ReserveEvent` at settlement close in v0 and as `ACCOUNT_LEVEL_RESERVE` in `listBalances`. (P-rec-22)

## Settlement period length

- Amazon's Chinese explainer states that the automatic settlement cycle keeps its length under the delivery-date policy, but that each Disburse on Demand truncates the current settlement period and restarts the cycle; this is read in Amazon's documents, not yet seen on a live account. (P-rec-38)
- Sellfox (a vendor) says a Disburse on Demand does not truncate the period. (P-rec-38)
- On the Payments dashboard the payment-request button works on the Standard Orders or Invoiced Orders row, not on the Deferred transactions row. (P-rec-38)
