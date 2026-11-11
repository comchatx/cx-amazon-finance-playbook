# Grade and Resell, donations and Amazon Resale as money

## FBA Grade and Resell

- FBA Grade and Resell grades eligible unfulfillable customer returns and relists them as Used ("Like New", "Very Good", "Good", "Acceptable") under the parent ASIN, "with you as the seller on record". (P-ref-42)
- Each graded listing gets an Amazon-generated SKU beginning `amzn.gr`. (P-ref-42)
- The 2021 UK help text says at most five such SKUs are generated per used listing under the parent ASIN (four used conditions and one unsellable); practitioners' files show `amzn.gr` SKUs with differing random keys for one product. (P-ref-42, P-ref-45)
- A unit graded unsellable stays in unfulfillable inventory under a new FNSKU beginning `amzn.gr`. (P-ref-42)
- Payments for graded sales appear in the seller's Payments dashboard. (P-ref-42)

## Its fees

- The 2021 UK help text, relayed by a seller, says a graded unit's sale carries the referral fee and the FBA fulfilment fee, plus a processing fee charged at relisting. (P-ref-43)
- The same 2021 UK text says no processing fee is charged on a unit graded unsellable. (P-ref-43)
- The same 2021 UK text says standard removal fees do not apply to units submitted to the programme. (P-ref-43)
- The same 2021 UK text says storage stops accruing on submission and restarts once a used unit is listed. (P-ref-43)
- The US News post of 2024-08-07 calls the programme "an optional fee-based service". (P-ref-43)
- The EU post of 2025-02-24 (UK, FR, DE, IT, ES, CZ, PL) says it runs "without any programme fees", with notice promised before any. (P-ref-43)
- The processing fee is read from Amazon's page FBA Grade and Resell (GUA6RV6UA4DR2MFK) as the seller's own store shows it, and from the fee as it posts on the seller's settlement V2 and `listTransactions` rows; no SP-API operation gives the rate. (P-ref-43)
- The fee's label on those rows is not published by Amazon. (P-ref-43)
- Whether a processing fee is charged in the US today is not established by any Amazon page read; research/areas/refunds-reimbursements-adjustments.md, P-ref-43, holds what was read. (P-ref-43)

## Its prices and enrolment

- The used price of a graded unit is set by the seller as a discount per condition on the new price at relisting. (P-ref-44)
- Since 2026-02-03, used prices follow changes to the new price and to the discounts automatically, until the seller prices a used SKU by hand. (P-ref-44)
- Since 2026-02-03 the seller can include chosen ASINs, up to a limit, or the whole catalogue less exclusions, and watches, jewelry, luggage, shoes and apparel are eligible. (P-ref-44)
- The ASIN limit is read from Amazon's page FBA Grade and Resell (GUA6RV6UA4DR2MFK) as the seller's own store shows it; no SP-API operation gives it. (P-ref-44)
- Enrolment sits in FBA settings → Automated unfulfillable settings. (P-ref-44)

## Where a graded sale's money lands

- Proceeds of a graded resale land under the `amzn.gr` SKU, not under the SKU whose refund produced the unit: read in Amazon's documents, not yet seen on a live account. (P-ref-45)
- The only links back are the parent ASIN and the SKU string; practitioners see `amzn.gr.<seller SKU>-<random key>-<two-character code>` (codes such as `LN`, `VG`, `PO`). (P-ref-45)
- One tool reports that in about one case in five Amazon shortened the seller SKU so that the string no longer matches. (P-ref-45)
- Amazon publishes neither the format nor a linking field. (P-ref-45)
- One US seller's live Data Kiosk `economics` pull (July 2026) returned `amzn.gr` MSKUs with FBA fulfilment-fee and fuel-surcharge components, and ledger tools separate `amzn.gr` rows from new stock. (P-ref-47)
- Orders v0 order items carry `ConditionId` (`New`, `Used`, …) and `ConditionSubtypeId` (`Very Good`, `Good`, `Acceptable`, …), which tell a used sale from a new one: for graded sales, read in Amazon's model, not yet seen on a live account. (P-ref-47)
- No SP-API operation or report names Grade and Resell. (P-ref-47)

## How a graded resale is costed

- How a graded resale is costed is an accounting choice, and tools differ. (P-ref-46)
- sellerboard detects `amzn.gr` SKUs and excludes the original SKU's COGS from their profit, because the cost was booked when the original unit sold. (P-ref-46)
- ConnectBooks maps them to a non-inventory item at zero cost, with Amazon fees kept. (P-ref-46)
- A German DATEV exporter values unmatched graded units at a fixed share of the purchase cost; research/areas/refunds-reimbursements-adjustments.md, P-ref-46, holds the share as read. (P-ref-46)
- A US dashboard leaves `amzn.` SKUs out of its fee analysis. (P-ref-46)
- Which treatment applies is the seller's choice. (P-ref-46)

## FBA Donations

- A donated FBA unit costs the seller the usual disposal fee and returns no proceeds. (P-ref-48)
- US sellers are enrolled in FBA Donations by default, and returned units ineligible for resale may be donated automatically. (P-ref-48)
- In Seller Central donating appears as "Dispose" or "Donate/Recycle". (P-ref-48)
- Donations show in the Removal Order Detail report: read in Amazon's documents, not yet seen on a live account. (P-ref-48)
- A yearly donation certificate on the Donations page lists the quantity and description of units donated the previous year. (P-ref-48)
- Amazon says the certificate "can be used to receive a tax benefit"; how a seller treats it for tax is the seller's. (P-ref-48)
- The programme started in the US and UK in 2019 and in France in 2020. (P-ref-48)

## Dated enrolment changes

- Amazon's News post of 2025-08-22 announced, for 2025-09-30 in the US and Canada, FBA Liquidations as the default for unsold inventory where no automated settings are configured (opt-out kept). (P-ref-49)
- The same post announced FBA Donations as mandatory, with opted-out sellers re-enrolled, and "no changes to the fees". (P-ref-49)
- Amazon's correction, relayed by a seller on 2025-09-30, limits both changes to the US, leaves Canada unchanged, and moves the Donations change to 2025-10-30, applying "if you select Dispose". (P-ref-49)
- The News post itself still reads US and Canada, 2025-09-30. (P-ref-49)
- ../fees-and-charges/SKILL.md: liquidation proceeds and removal and disposal fees.

## Amazon Resale

- Amazon's reimbursement policy text says reimbursed units, including units found after reimbursement, may be sold "on Amazon warehouse or other channels". (P-ref-50)
- Amazon Warehouse was renamed Amazon Resale in August 2024. (P-ref-50)
- Grade and Resell uses the same grading process as Amazon Warehouse. (P-ref-50)
