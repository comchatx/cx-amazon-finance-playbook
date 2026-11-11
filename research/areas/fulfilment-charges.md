# Fulfilment, logistics and storage charges as money: how each is computed, when it posts, where it is recorded

Read 2026-11-09 by the research seat. Tags: **[official]** Amazon's own page, model, report page or rate card (title + URL + date read); **[opinion]** a named practitioner or vendor; **[research]** published study; **[seat]** this seat's own reasoning, never a position; **[command-verified]** a command run here over a clone of Amazon's models repository (https://github.com/amzn/selling-partner-api-models, commit db2936aa, 2026-10-29) or over a file downloaded today.

## What this covers

Scope: every charge Amazon takes for fulfilment, inbound logistics, storage, removal and related FBA/AWD/MCF services, treated as **money lines**. For each: Amazon's definition and computation basis, when it is assessed and when it posts, and every place it is recorded (Finances v2024-06-19, Finances v0, settlement V2, the FBA reports, Data Kiosk economics, Product Fees, Fulfillment Inbound/Outbound, AWD). The stock playbook (brief 307) owns the stock states behind storage, aged, low-inventory and capacity charges, and the decisions they drive. The selling/program fees seat owns referral, closing, subscription, coupon, deal and ads charges. Reimbursement *claims* are a later plugin; here a reimbursement or fee correction is read only as money received.

Skills it feeds: the pack's **fees** skill (where each charge lives, its timing, the open-ended type names), **profit** (what a product's fulfilment and storage cost was in a period, and why period totals and per-product totals differ), and **payouts / reconciliation** (why a settlement carries charges for stock sold months earlier, or for no sale at all).

Why a senior operator cares. Fulfilment and storage are, for most FBA sellers, the largest Amazon cost after referral fees, and most of them are **not on the order**. Monthly storage posts in the following month. The aged surcharge is a monthly snapshot charge. Inbound placement posts about 45 days after receipt. The high-return-rate fee posts in the third month after shipment. Removal and disposal post unit by unit as they are processed. A profit figure built from order lines alone leaves all of these out. A figure built from a settlement puts them in the period they posted, not the period of the stock or the sale they belong to. Amazon gives no closed list of the names these lines carry. The rates change every January (US) or February (EU), and also mid-year (the fuel surcharge in April 2026, the EU fuel rise in November 2026).

**Dated changes since 2025-01-01** (each with its source in section 3):
- 2025-02-01 (EU): high-return-rate returns processing fee introduced in Europe.
- 2025-03-31 (EU, US posts): lost/damaged reimbursement valued at manufacturing cost. First announced for 2025-03-10; Amazon's News post of 2025-02-28 ("New effective date for FBA inventory reimbursement policy") moved it to 2025-03-31. This is money received, owned by the reimbursements seat; listed because it changes what a "fee correction" line can be worth.
- 2025-10-15 (US): reimbursement claim windows revised (reimbursements seat).
- 2025-12-22: Data Kiosk economics loses `FNSKU` granularity.
- 2026-01-01 (US): FBA prep and item labelling services by Amazon end.
- 2026-01-15 (US): 2026 schedule. Fulfilment fee price bands; the low-inventory-level fee moves to FNSKU level and applies to Small and Large Bulky; Grocery is exempt; placement fees rise; a single inbound defect fee replaces the double charge; an aged tier over 15 months is added; the Bulky tiers are split.
- 2026-02-01 (EU): the 2026 European rate card (announced reductions brought forward to 2026-01-05 per practitioners).
- 2026-03-01 (US): removal and disposal fees charged per unit as each unit is processed (revised from 2026-02-15).
- 2026-04-17: fuel and logistics surcharge, 3.5% of FBA fulfilment fees in the US and CA and on Remote Fulfillment from the US. 1.5% in the EU/UK stores from the same date. MCF from 2026-05-02 [opinion].
- 2025-11-05 (CA): FBA Liquidations launched in Canada, with a 15% referral fee plus a per-item processing fee (News_Amazon CA, a9383e96). 2026: "no increases to Canada referral and Fulfilment by Amazon fees" (same post).
- 2026-04-01 (JP): FBA fulfilment fees cut for standard-size items of 20–80 cm and up to 5 kg. 2026-04-15 (JP): aged-inventory surcharge revised, with a minimum of ¥20 per unit per month on non-media stock aged 365 days or more; first charge 2026-04-22, on the 2026-04-15 assessment (gs.amazon.cn news-notices-251202, 2025-12-02).
- 2026-06-04 (MX): fulfilment fee table updated ("Tarifas actualizadas el 4 de junio de 2026", vender.amazon.com.mx/precios).
- 2026-07-01 (CA): prep and labelling by Amazon end [opinion/snippet]. (EU): prep ends per one vendor [opinion], but the EU rate card of 2026-11-02 still lists FBA Prep Services: a conflict.
- 2026-07-29: Finances `listSummary`, `listBalances`, Transfers `listPayouts`; a `SETTLEMENT_ID` filter on `listTransactions` announced in the release note. Amazon added it to the model on 2026-10-28 (commit df7c6298) and removed it on 2026-10-29 (db2936aa, "Finance API Rollback"). The live reference page, read 2026-11-10, lists only `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`, so it is not a filter today.
- 2026-09-30: economics dataset "updated … with deal, coupon, removal, disposal, and fuel fees".
- 2026-10-15 → 2027-01-14: holiday peak fulfilment fees (US, CA, EU/UK).
- 2026-11-02 (EU/UK): fuel and logistics surcharge rises from 1.5% to 2%.
- Announced 2026-11-05 for 2027 (US): fulfilment fees from 2027-01-15. From **2027-02-01**: storage utilization surcharge eliminated; aged surcharge folded into "a single, age-based rate"; low-inventory-level fee re-based on actual shipments four weeks either side of the assessment date. AWD age-based storage from 2027-03-01 [opinion: ppc.land's reading].
- 2026-11-11: removal of settlement V1 (`GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE`) and XML. 2027-08-27: removal of three Finances v0 operations.
- Amazon-sold inbound transport (section Q; added in the 2026-11-10 gap fill):
  - 2025-06-01 (US): partnered-carrier lines in the Payments transaction report renamed from "FBA Amazon-Partnered Carrier Shipment Fee" to "Inbound Transportation Fee", now with the FBA shipment ID in the order-id column [opinion: a seller on sellersasksellers.com, 2026-03-24].
  - 2026-01-14: current Amazon Global Logistics (AGL) Freight Service Terms dated.
  - 2026-02-20 onwards: IEEPA tariffs struck down. Refunds go to the importer of record (`product-profit.md`); AGL entries keep the seller as importer (Q4).
  - 2026-04-09: Global Warehousing and Distribution (GWD) opens in Shenzhen, storing stock in China for replenishment to US FBA. 2026-07-16: Shanghai, with the FOB incoterm. Amazon announced seven more destination countries by the end of 2026 [opinion relaying Amazon: FreightWaves, 2026-09-27].
  - 2026-08-05: Tracking API v2026-01-30 (US, grantless) and the `SHIPMENT_TRACKING_MILESTONE_CHANGED` notification launched. They carry customs and delivery milestones, not amounts.
  - 2026-10-28 → 2026-10-29: Finances `BusinessContext.storeName` value `AMAZON_FBA_FROM_ORIGIN` ("Transactions associated with FBA from origin.") added, then removed by the rollback commit db2936aa.

## Amazon's own rules

### A. The fee family and the measurement that drives most of it

A1. RULE (which fees depend on size tier). "The product size tier of an item is used to calculate certain fees": FBA fulfilment, monthly storage, the aged inventory surcharge, removal, disposal, MCF and inbound placement. The 2024 tier table ended 2026-01-14. The 2026 table starts 2026-01-15, adds Small Bulky and defines Overmax. Amazon points to the Fee Preview report: "View the product size tier in the product-size-tier field." [official] (Product size tiers, https://sellercentral.amazon.com/help/hub/reference/external/GG5KW835AHDJCH8W, v7, read 2026-10-14 by the listing seat: `cx-listing-playbook` research/angles/inventory-and-fulfillment.md G9)

A2. RULE (Amazon's measurement governs). "Amazon may verify the weight and dimensions of a product using representative samples. Amazon's information … will be used to calculate fees if there is a difference …. Fees … are calculated using Amazon's information … at the time the fee is calculated." [official] (Product dimensions and volume, G37G73BJXHF75ACH v5, read 2026-10-14, inventory-and-fulfillment.md G10.) "When the weight or dimensions that the seller provides vary from our verified measurement, our measurement will govern", and a fee reimbursement request is due "within 90 days of the date on which the fee was charged". [official] (FBA fees reimbursement policy: Weight and dimensions, GL7U4JFSDXUTQAJ v14, same source.) The EU rate card says the same of storage volume: "Amazon will be entitled to make its own measurement … and in the event of any conflict … Amazon's measurement will govern." [official] (Rate Card Europe Fees, effective 2 November 2026, FAQ Q2, https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf, read 2026-11-09 [command-verified: text extracted with macOS PDFKit])

A3. RULE (re-measurement). Sensors measure "edge-to-edge, including loose material". A remeasurement "typically takes 10 days". Updated dimensions "apply across all stores within the region". Each FNSKU "can only be remeasured twice within the preceding 60 days". There are account-level monthly limits "based on the number of offers with inventory in your account". The route is the "Remeasure FBA products and confirm fees widget". [official] (Understanding item package weight and dimensions, G6WAEPTECPT2JUH3 v11, read 2026-10-14, inventory-and-fulfillment.md G11.) No SP-API operation requests a remeasurement [command-verified: no remeasure/dimension-dispute operation in ops.tsv or the models].

A4. RULE (shipping weight, EU wording). "Envelopes, Special oversize products and products fulfilled via Low-Price FBA are charged as per the actual unit weight … Parcel and oversize tiers (excluding Special oversize) are charged as per the greater of the unit weight or the dimensional weight. The dimensional weight in kilograms is calculated as (length x width x height cm³) divided by 5000." [official] (EU rate card 2026-11-02, "Calculating your FBA fees")

A5. RULE (the total). "Simply add together your fulfilment and storage fees and any optional services you require to calculate your total FBA Fee." [official] (EU rate card 2026-11-02.) In the US the FBA fees overview lists placement as reflecting "the cost of distributing inventory to fulfillment centers close to customers". [official] (FBA features, services, and fees, G201074400 v41, read 2026-10-14, inventory-and-fulfillment.md F1)

### B. FBA fulfilment fee (and surcharges on it)

B1. RULE (what it is, when it is charged). The fee is "based on the product's price, weight, and dimensions". [official] (Amazon FBA, https://sell.amazon.com/fulfillment-by-amazon, read 2026-11-09.) "FBA fulfillment fees are calculated and charged when shipments leave fulfillment centers. If a product is ordered before October 15, 2026, but is shipped on or after that date, the peak fulfillment fees … will apply." [official] (2026 US FBA fulfillment fee changes, GABBX6GZPA8MSZGW v58, read 2026-10-14, inventory-and-fulfillment.md G3.) So the rate that applies is the one in force on the **ship date**, and the fee rides on the order's shipment line.

B2. RULE (US price bands, 2026). The 2026 rate cards are split "<$10", "$10-$50", ">$50". "Products priced under $10 will automatically receive Low-Price FBA rates". A price change across $10 or $50 changes the fulfilment fee per unit. [official] (GABBX6GZPA8MSZGW v58, inventory-and-fulfillment.md G2)

B3. RULE (US 2027). "On average, FBA fulfillment fees will increase by $0.19 per unit sold". "most changes take effect on January 15, 2027". "The impact will vary by product, size, and price. Fees for some products will increase, and others will decrease." "The FBA fuel and logistics surcharge remains unchanged." [official] (Update to US Referral and Fulfillment by Amazon fees for 2027, Amazon Selling Partners, dated 2026-11-05, https://sellingpartners.aboutamazon.com/update-to-us-referral-and-fulfillment-by-amazon-fees-for-2027, read 2026-11-09; the same text as a Seller Central news article copied in https://sellersasksellers.com/t/fba-rate-increases/7699.) The detail pages, as reproduced by a practitioner, say that from 2027-01-15 Low-Price FBA rates are "restricted to a narrower set of fee categories". Five categories (Automotive and Powersports, Compact Appliances, Musical Instruments and AV Production, Media, Computers) "will be charged the same rates as products priced from $10 to $50", and the Overmax handling fee "no longer applies". [opinion relaying Amazon text: ppc.land, Luís Rijo, 2026-11-06, https://ppc.land/amazon-sellers-face-average-0-19-fba-fee-rise-from-january-15-2027/; the summary page G201411300 itself was not readable by plain GET]

B4. RULE (fuel and logistics surcharge). US/CA: "Starting April 17, 2026, a 3.5% fuel and logistics-related surcharge will be applied to fulfillment fees across Fulfillment by Amazon (FBA) in the US and Canada". It applies to peak fees too. [official] (GABBX6GZPA8MSZGW v58, inventory-and-fulfillment.md G3.) EU/UK: "Starting from April 17, 2026, a 1.5% fuel and logistics-related surcharge will be applied to fulfilment fees across Fulfilment by Amazon (FBA) in the UK, France, Germany, Italy, Spain, Poland, Sweden, Netherlands, Ireland and Belgium stores." [official] (Rate Card Europe Fees, effective 1 July 2026, https://m.media-amazon.com/images/G/02/sell/images/260630-FBA-Rate-Card-EN1.pdf, read 2026-11-09.) "Starting November 2, 2026, the fuel and logistics-related surcharge will increase from 1.5% to 2%" in the same ten stores. [official] (EU rate card 2026-11-02.) It is a percentage **of the fulfilment fee**, not of the price. Practitioners stress that point [opinion: 跨境小侠醉千丝, AMZ123, 2026-09-10, https://www.amz123.com/t/BA1qW9jV: "这个3.5%不是按照售价收，而是按照FBA配送费"].

B5. RULE (holiday peak). US: "holiday peak fulfillment fees will apply from October 15, 2026 to January 14, 2027", and the surcharge applies to them. [official] (GABBX6GZPA8MSZGW v58.) EU/UK: "The festive peak fulfillment fee for FBA (excluding apparel) will apply from October 15, 2026, through January 14, 2027. On January 15, 2027, fulfillment fees will revert back to the non-peak period rates, which are unchanged from the 2026 non-peak rates." [official] (EU rate card 2026-11-02, p. 7.) **Today (2026-11-09) is inside the peak window** in both regions.

B6. RULE (EU low-price FBA). It covers fast-moving small light products priced at or under £20 / €20 (DE, NL, FR, IT, ES, BE, IE) / 230 SEK / 85 PLN incl. VAT, with lower caps (£10, €11 DE, €12 others, 140 SEK, 55 PLN) in Beauty, Health & Personal Care, Business/Industrial/Scientific, Office, Grocery, Books, Amazon Device Accessories and Kitchen. [official] (EU rate card 2026-11-02, p. 5) **(figures; read at run time)**

B7. RULE (EU network variants on the fulfilment fee). The card has separate fee tables for local/Pan-European, EFN and Remote Fulfilment UK-EU, Ireland, parcel-size products in selected categories, and SIPP discounts. Pan-EU sellers "will benefit from local FBA fulfilment fees". [official] (EU rate card 2026-11-02, contents and p. 5.) The **Pan-EU Oversize Surcharge** "applies on top of Pan-EU FBA fulfilment fees if the country in which you ship your oversize inventory to us is different from the country in which your inventory is sold". It is "based on the historical inbound minus sales quantity metric", computed "at the seller-FNSKU and the Pan-EU store level … over both the long-term (last 150 days) and short-term (last 30 days) periods", and applies "only … when both its long-term and short-term historical days of supply are below zero (<0)". [official] (EU rate card 2026-11-02, p. 10 and FAQ Q3.) The surcharge rides on the fulfilment fee line [seat].

B8. RULE (multi-unit and per-order components). The Fee Preview report carries per-unit and per-order fields by store: `expected-fulfillment-fee-per-unit` (US, CA), `estimated-order-handling-fee-per-order` (US, UK), `estimated-pick-pack-fee-per-unit` and `estimated-weight-handling-fee-per-unit` (MX), and EFN per-destination fees in the EU (`expected-efn-fulfilment-fee-per-unit-uk/de/fr/it/es/se`). [official] (FBA Reports, https://developer-docs.amazon/sp-api/docs/report-type-values-fba.md, updatedAt 2026-10-13, read 2026-11-09 [command-verified by curl].) Amazon's fee is per unit shipped. Per-order components appear only where those fields say so [seat].

### C. Inbound placement service fee

C1. RULE. Three options. "Minimal shipment splits": "generally to a single location, for a fee". "Amazon-optimized shipment splits": "multiple inbound locations yourself for no fee", which requires "at least five identical cartons or pallets per item". "Partial shipment splits": Bulky only. Availability depends on "product types and quantities …, your existing inventory levels …, location of customer demand, and capacity availability". The fee is "charged … 45 days after your shipment is received", "may be adjusted periodically within the ranges listed", and "doesn't apply to Extra-Large products". [official] (FBA inbound placement service fee, GC3Q44PBK8BXQW3Z v16, read 2026-10-14, inventory-and-fulfillment.md F1)

C2. RULE (2026 / 2027). 2026: standard-size placement fees on minimal splits rose about $0.05 per unit from 2026-01-15. [official] (2026 US Referral and FBA fee changes summary, G201411300 v47, read 2026-10-14, inventory-and-fulfillment.md G1.) 2027: "no changes to the inbound placement service fee rate card", and central inbound regions go "from three to two (East and West)". [opinion relaying Amazon text: ppc.land 2026-11-06; in the part of the page summarised by the fetch tool, so lower confidence]

C3. RULE (AWD and placement). "AWD pricing covers FBA inbound placement, so there is no separate charge for this service." [official] (Amazon Warehousing and Distribution, https://sell.amazon.com/programs/warehousing, read 2026-11-09.) The Supply Chain Portal fee policy defines it as a "Per unit fee applicable to small standard, large standard and large bulky units if inbound shipment split is less than 4 locations". [official] (Supply Chain Portal fees overview, https://supplychain.amazon.com/pricing/fees-policy, read 2026-11-09.) That is a different threshold wording ("less than 4 locations") from the Seller Central page's "five identical cartons". The two apply to different programmes [seat].

C4. RULE (the price is shown before it is committed). In Fulfillment Inbound v2024-03-20, each `PlacementOption` carries `fees` and `discounts`, each an `Incentive` with `type` `FEE` or `DISCOUNT`, `target` 'Placement Services' or 'Fulfillment Fee Discount', `description` and `value`. `confirmPlacementOption`: "Once confirmed, it cannot be changed for the Inbound Plan." [official, command-verified] (fulfillmentInbound_2024-03-20.json.) The fee charged 45 days after receipt is the money line; the option's `fees` is the quote [seat].

C5. RULE (EU). The EU rate card of 2026-11-02 has **no inbound placement service fee** section. Its inbound charge is the manual processing fee for missing box content ("If you do not provide box content information, we will manually process your boxes … and a fee will apply"). [official, absence] (EU rate card 2026-11-02, pp. 2, 24.) The absence was re-checked by the verifier on 2026-11-10 across the cards effective 2026-02-01, 2026-07-01 and 2026-11-02: none has an inbound placement section. The card's phrase "In the countries enabled for placement, Selling Partners will benefit from local FBA fulfilment fees" is about where Pan-EU stock may be stored, not a fee. An EU forum thread title, "FBA Inventory Placement Fee charged on Shipment without placement service" (sellercentral-europe, a58fad97…), shows a placement-type line can appear in EU accounts. [opinion, seen only as a search title; not read]

### D. Low-inventory-level fee (US) and low-inventory cost coverage fee (Pan-EU)

D1. RULE (US, 2026 method). "We'll only charge a low-inventory-level fee when both the long-term historical days of supply (last 90 days) and short-term historical days of supply (last 30 days) are below 28 days (4 weeks)." From 2026-01-15 it is computed "at the seller-FNSKU level instead of the parent-ASIN level". It is charged **per unit when the order ships**, by size tier, shipping weight and days-of-supply band (0–14, 14–21, 21–28). The metric is "updated weekly, and the latest available historical days of supply will determine the fee rate for units shipped that week." Exemptions: new Professional sellers (365 days from first receipt), New-to-FBA parents in FBA New Selection (180 days), SKUs with 70%+ auto-replenished via AWD over 90 days, "Products that have sold less than 20 units in the past 7 days", and Grocery. On Amazon-caused inbound delays: "we'll automatically reimburse you if the low-inventory-level fees are charged". [official] (Low-inventory-level fee, GV43F6S76Y9DHYRH v29, read 2026-10-14, inventory-and-fulfillment.md E1–E3.) Economics names it "Fulfillment by Amazon (FBA) Fulfillment Fee Low Level Inventory Surcharge". It is a component of the fulfilment fee family, not a separate event [official, command-verified: `PreviewFeeType.LOW_INVENTORY_LEVEL_FEE` in analytics_economics_2024_03_15.graphql]. The Fee and Economics Preview report includes it only if the seller selects "fulfillment base rate and surcharges". [official] (G4, GQNVDV46U9JQ25HY v3)

D2. RULE (US, from 2027-02-01). "Today, the fee is assessed using trailing 30- and 90-day sales." "Effective February 1, the fee will apply only when your inventory falls below 28 days of supply, based on actual shipments in both the four weeks before and after the assessment date." [official] (2027 announcement, 2026-11-05.) [seat] Under that wording, the rate for a unit shipped in a given week depends on shipments after that week. So a charge's final amount may be known only some weeks after the ship date. How Amazon posts it (at shipment, then adjusted; or later) is not stated: open question.

D3. RULE (Pan-EU). "A low-inventory cost coverage fee (Pan-EU) applies to standard-size products fulfilled through the Pan-European FBA (Pan-EU) programme when inventory units are less than 28 days relative to shipped units across Germany, France, Italy and Spain." Both the 90-day and 30-day historical days of supply must be below 28. It is computed "at the seller-FNSKU level … across Pan-EU stores". It "Does not apply to the Netherlands, Poland, Sweden, Belgium and Ireland." Bands are 0–14, 14–21, 21–28 days. [official] (EU rate card 2026-11-02, p. 10, FAQ Q6)

D4. RULE (where to see the flags). `GET_FBA_INVENTORY_PLANNING_DATA` carries `historical-days-of-supply`, `Short term historical days of supply`, `Long term historical days of supply`, `Last updated date for Historical Days of Supply`, `Exempted from Low-Inventory-Level fee?` and `Low-Inventory-Level fee applied in current week?`. Role: Amazon Fulfillment only. [official] (FBA Reports page)

### E. Monthly storage fee, storage utilization surcharge (to 2027-01-31)

E1. RULE (US). "Charged monthly based on the space your inventory occupies in Amazon's fulfillment network (calculated based on your daily average volume in cubic feet)." "Storage costs vary seasonally, with potentially higher rates during holiday months." [official] (sell.amazon.com/fulfillment-by-amazon; A guide to Amazon FBA fees, https://sell.amazon.com/blog/fba-fees-guide, dated 2026-07-24; both read 2026-11-09.) Collection: "Monthly, typically between the 7th and 15th day of the month, in the month following when the fees were incurred". [official, via search snippet only: Monthly inventory storage fees, https://sellercentral.amazon.com/gp/help/external/53921. A plain GET returned only the JS shell.]

E2. RULE (EU). "Monthly storage fees are charged for all units stored in an Amazon fulfilment centre based on calendar month and your daily average volume (measured in cubic feet for the United Kingdom and cubic metres for the other European stores)." The base fee "is determined by product size and time of year". Seasons are **Jan–Sep and Oct–Dec**, with separate columns for clothing/accessories/eyewear/footwear/rucksacks/handbags, all other standard-size, oversize, and dangerous goods. [official] (EU rate card 2026-11-02, p. 21)

E3. RULE (storage utilization surcharge, EU wording; the US one is the same mechanism). "this surcharge is based on storage utilisation ratio, which is the ratio of your average daily inventory volume stored divided by the average daily shipped volume during the past 13 weeks." It "Applies for professional sellers with a storage utilisation ratio above 22 weeks and for products outside of clothing, eyewear, shoes and bags". It is calculated per product size tier, "on the last day of a given month". It "does not apply to new sellers, sellers with Individual selling accounts and sellers with less than 25 cubic feet of daily volume", where new means first shipment under 52 weeks ago. [official] (EU rate card 2026-11-02, pp. 4, 21.) Supply Chain Portal: "Professional sellers with a storage utilization ratio above 22 weeks", with inventory aged 0–30 days excluded. [official] (Supply Chain Portal fees overview)

E4. RULE (storage is one fee type with components). Economics: `FBA_STORAGE_FEE` is "Monthly Inventory Storage Fee, including base rate and surcharges". `includeComponentsForFeeTypes` can break it into components. `PreviewFeeType` lists `BASE_MONTHLY_STORAGE_FEE`, `STORAGE_UTILIZATION_SURCHARGE` and `MONTHLY_INVENTORY_STORAGE_FEES`. [official, command-verified] (analytics_economics_2024_03_15.graphql)

E5. RULE (2027, US). "Effective February 1, 2027, we'll eliminate the storage utilization surcharge, which will make it easier to stock up ahead of high-demand events. We'll also remove the aged inventory surcharge and combine it with monthly storage fees into a single, age-based rate." "These changes will result in flat or lower fees for inventory that turns in under six months" and "higher fees for aged inventory". [official] (2027 announcement, 2026-11-05.) No 2027 age bands or rates were readable on 2026-11-09.

### F. Aged inventory surcharge (replaced long-term storage)

F1. RULE (US). "Charged monthly for all items stored in a fulfillment center for more than 181 days." [official] (sell.amazon.com/fulfillment-by-amazon.) Economics: "Aged Inventory Surcharge, previously known as the Long-term Storage Fee" (help GJQNPA23YWVA4SBD). [official, command-verified.] 2026 added a tier for items over 15 months. [official] (G201411300 v47, inventory-and-fulfillment.md G1.) The age bands the US uses are visible as Planning-report columns: `quantity-to-be-charged-ais-181-210-days` … `-331-365-days`, `-366-455-days`, `-456-plus-days`, each with `estimated-ais-…`. [official] (FBA Reports page)

F2. RULE (EU). "Aged Inventory Surcharge - Applies to inventory stored for: More than 241 days." Bands: 241–270, 271–300, 301–330, 331–365, 365–455, 455+. Some rates are "per cubic foot or … per unit, whichever is greater". Footnote 1 sits on the **241–270** column only: "Excluding items listed under Clothing and Accessories, Footwear, Rucksacks and Handbags, Luggage, Jewellery and Watches." So those categories pay nothing in the 241–270 band and are charged from 271 days (verified on the rendered p. 21, 2026-11-10). [official] (EU rate card 2026-11-02, pp. 4, 21; unchanged in the cards of 2026-02-01 and 2026-07-01 [command-verified: grep across the three extracted cards])

F3. RULE (assessment date). Two Amazon pages state an assessment on the 15th, for their own stores:
- AU: the aged-surcharge table has a column "Inventory assessment date" reading "15th of the month" on every band. [official] (sell.amazon.com.au/pricing, read 2026-11-10)
- JP: the 2026 change was first charged on "2026年4月22日（基于2026年4月15日库存评估结果）" (22 April 2026, based on the 15 April 2026 inventory assessment). [official] (gs.amazon.cn news-notices-251202, 2025-12-02, read 2026-11-10)

For the US and EU, practitioners say the age snapshot is on the 15th [opinion: AMALYTIX, https://www.amalytix.com/en/knowledge/controlling/amazon-seller-fees/, updated 2026-10-20; several US blogs]. One says it is billed between the 18th and 22nd [opinion, unverified]. No US or EU Amazon page read states the date. The Planning report carries `Inventory age snapshot date` [official].

F4. RULE (the report name lags). The report `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` ("Contains the charge data for long-term storage") now carries `surcharge-age-tier` and `rate-surcharge`. The request range "should be equal to one month". [official] (FBA Reports page.) The Recommended Removal report still speaks of the "next Long-Term Storage cleanup event" and "365 days". [official] Both are older vocabulary on live reports [seat].

### G. Returns processing fees

G1. RULE (US, two fees). High return rate: "A returns processing fee is charged on all products (except apparel and shoes) with a high return rate … The fee will only apply to products that have return rates above a threshold specific to each product". The return rate is "the percentage of the product's shipped units in a given month that are physically returned during that month and the subsequent two calendar months". It is charged "for each returned unit above the product's return rate threshold", "between the 7th and 15th day of the third subsequent month". Exempt "if it shipped fewer than 25 units in a month". New Selection waives "the first 20 units of each eligible parent ASIN". Thresholds are "audited quarterly". Apparel and shoes: "a returns processing fee is applied for each customer-returned unit. No thresholds are applied, and fees are charged as returns are made." It shows in "Manage Your Payments", "a report from Amazon Fulfillment reports", and "SKU Economics". [official] (2026 returns processing fee changes, GZGEQLTM3RZXUV6T v17, read 2026-10-14; `cx-listing-playbook` research/angles/returns.md.) "The high return rate fee is not charged for returns that are successfully given to customers through FBA Returnless Resolutions." [official] (G3RZC8DVQCDTCQ3B v8, same source.) Introduced 2024-06-01 (announced 2023-12-05). [official, same source]

G2. RULE (EU). "Starting on February 1, 2025, we'll introduce a returns processing fee for high-return-rate products in all categories, excluding clothing and, shoes". Same three-month return-rate window. "For products in the clothing and shoes categories, the returns processing fee is equal to 50% of the total fulfilment fee for a given product", local and EFN. [official] (EU rate card 2026-11-02, FAQ Q4, p. 25)

G3. 2027 (US). The 2027 summary reportedly changes returns processing for apparel and shoes from 2027-01-15 and outside apparel and shoes from 2027-02-01. [opinion: ppc.land 2026-11-06, summarised part]. Not confirmed on an Amazon page read today.

### H. Removal, disposal, return-to-seller, liquidation

H1. RULE (per-item). "You can have Amazon return, dispose of, or liquidate your inventory in a fulfillment center for a per-item charge." [official] (sell.amazon.com/fulfillment-by-amazon)

H2. RULE (per-unit billing from 2026-03-01, US). Removal and disposal fees "will be charged on a per-unit basis at the time each unit is removed or disposed of". Previously "these fees were charged all at once when the entire removal or disposal order was completed." "This is a charge timeline change only. The fee rates for removal and disposal fees remain unchanged." "This change will apply automatically to new orders created on or after March 1." "The effective date for these fee changes has been revised to March 1, 2026." "Previously, it was listed as February 15, 2026." "To review your shipment level charges and when units are removed, go to Payments and click Transaction view." [official] (FBA removal and disposal fees to be charged as units are processed, News_Amazon, https://sellercentral.amazon.com/seller-forums/discussions/t/2f4edad8-31d4-443b-8b22-12776c4f685a, article published 2026-01-29, read 2026-11-09)

H3. RULE (EU). Return-to-seller (local and cross-border, Zone 1/Zone 2), disposal and liquidation are per-unit "optional services". "Fees are charged in the currency of the country where your inventory is stored." "Amazon applies two separate fees to each item that you liquidate: A 15% liquidations referral fee, based on the item's gross recovery value. A liquidation processing fee, based on the item's size and weight." "Cross-border returns from the UK are currently disabled." [official] (EU rate card 2026-11-02, p. 23)

H4. RULE (liquidation as money, US model). `FBALiquidationEvent`: "A payment event for Fulfillment by Amazon (FBA) inventory liquidation. This event is used only in the US marketplace." `LiquidationProceedsAmount`: "The amount paid by the liquidator for the seller's inventory. The seller receives this amount minus `LiquidationFeeAmount`." `RemovalShipmentEvent` (TransactionType `WHOLESALE_LIQUIDATION`) carries per item `Revenue` ("The total amount paid to the seller for the removed item"), `FeeAmount` ("The fee that Amazon charged to the seller for the removal of the item. The amount is a negative number."), `TaxAmount`, `TaxWithheld`. `RemovalShipmentAdjustmentEvent` carries later adjustments: "A positive value indicates money owed to Amazon by the buyer … A negative value indicates a full or partial refund owed to the buyer". [official, command-verified] (financesV0.json)

### I. Prep, labelling, unplanned services, manual processing

I1. RULE (US/CA prep end). US prep and item labelling by Amazon ended 2026-01-01. [official, via the listing seat's G1 and many vendors; the US 2024-03-20 model says of `prepOwner`: "`AMAZON` is not an accepted value in the US marketplace" [command-verified].] Canada ends 2026-07-01 [opinion/snippet: practitioners citing the SP-API changelog].

I2. RULE (EU still lists prep). "FBA Prep Service helps you to properly package and prepare your shipments … If you use the FBA Prep Service, we'll prep your products for a per-unit fee." Lines are label service, bagging, opaque bagging and bubble wrap by size class. [official] (EU rate card 2026-11-02, p. 24.) One vendor says Amazon stopped EU prep from 2026-07-01 [opinion: AMALYTIX, 2026-10-20]. **Conflict**, unresolved; the rate card is the later Amazon document.

I3. RULE (unplanned services). The help page "Unplanned services" (https://sellercentral.amazon.com/gp/help/external/201000230) returned only navigation to a plain GET. Search snippets say fees for missing labels, taping, bagging and bubble wrap are "scaled by coaching level", "apply only when Amazon supplies an image of the problem", with disputes "within 30 days". [opinion: summaries of that page; not read]. The Inbound Performance report carries per problem `problem-type`, `problem-quantity`, `coaching-level`, `fee-type`, `currency`, `fee-total`. [official] (FBA Reports page, `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA`)

I4. RULE (manual processing). EU: missing box content → "we will manually process your boxes … and a fee will apply". [official] (EU rate card 2026-11-02)

### J. Inbound defect fee

J1. RULE. 2026: "A single inbound defect fee replaced the double charge". [official] (G201411300 v47, inventory-and-fulfillment.md G1.) Supply Chain Portal names one trigger: "domestic shipments that don't arrive within 45 days of shipment creation". [official] (Supply Chain Portal fees overview.) Practitioners list misrouted, deleted or abandoned shipments, quantity mismatches, and late arrival (45 days domestic, 75 days international) [opinion: CC站外推广, AMZ123, 2025-11-09, https://www.amz123.com/t/3PEcbbvv]. Rates are for human readers (section 10).

### K. Capacity: limits, reservation fee, performance credits, overage fee

K1. RULE. Capacity Manager lets a seller "request an increase … at a reservation fee that you specify". Requests are granted from "the highest reservation fee per cubic foot first". There is "a $0.15 performance credit for every dollar of sales that you generate using additional capacity". [official] (FBA capacity limits, GAFNWEYTJUV2GBFC v22, read 2026-10-14, inventory-and-fulfillment.md D2.) "Performance credits are designed to offset up to 100% of the reservation fee, so sellers don't pay for the additional capacity as long as their products sell through." [official] (Amazon announces new streamlined FBA capacity management system, https://sell.amazon.com/blog/announcements/fba-capacity, 2023-01-17, read 2026-11-09)

K2. RULE (overage). "overage fees will apply if your on-hand inventory in Amazon's fulfillment centers, not including open shipments, exceeds your capacity limit." "Overage fees are calculated based on the highest estimated or confirmed limit that we provided for the given period." [official] (Ask Amazon: Simplified FBA capacity limits Q&A, Kelly_Amazon, 2023-03-14, https://sellercentral.amazon.com/seller-forums/discussions/t/3c9cef3c-530b-4846-a3b3-a855ed62f241, read 2026-11-09.) The overage report carries `charged_date`, `storage_type`, `charge_rate`, `storage_usage_volume`, `storage_limit_volume`, `overage_volume`, `charged_fee_amount`. [official] (FBA Reports page)

K3. RULE (how the reservation charge is recorded). Finances v0 has `CapacityReservationBillingEventList` / `CapacityReservationBillingEvent`: "An event related to a capacity reservation billing charge", with `TransactionType` ("For example, FBA Inventory Fee"), `PostedDate`, `Description`, `TransactionAmount`. [official, command-verified] (financesV0.json.) How credits appear (a netted line, or a separate credit) is not stated by any page read: open question.

### L. Amazon Partnered Carrier and inbound transportation

L1. RULE. In v2024-03-20, `TransportationOption.shippingSolution` is `AMAZON_PARTNERED_CARRIER` or `USE_YOUR_OWN_CARRIER`, with a `quote` (`cost`, `expiration`, `voidableUntil`). `cancelInboundPlan`: "Charges may apply if the cancellation is performed outside of a void window. The window for Amazon Partnered Carriers is 24 hours for Small Parcel Delivery (SPD) and one hour for Less-Than-Truckload (LTL) carrier shipments." Content updates after carrier confirmation have previews "with the updated costs" (`generateShipmentContentUpdatePreviews`, `confirmShipmentContentUpdatePreview`: "accept the changes in transportation cost"). [official, command-verified] (fulfillmentInbound_2024-03-20.json.) The v0 transport operations (`estimateTransport`, `getTransportDetails`, `confirmTransport`, `voidTransport` …) were removed 2025-01-21. [official] (SP-API Deprecation Schedule, https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md, updatedAt 2026-09-09, read 2026-11-09)

L2. RULE (delivery windows can carry discounts). `DeliveryWindowOption.availabilityType` `AVAILABLE`, `BLOCKED`, `CONGESTED`, `DISCOUNTED`. "A `DISCOUNTED` delivery window has an incentive for choosing it." `discounts` were added to `listDeliveryWindowOptions` on 2026-07-29. [official] (release notes 2025-12-03 and 2026-07-29; model)

### M. AWD (Amazon Warehousing and Distribution)

M1. RULE. AWD charges storage per cubic foot per month (by region and tier: base, "smart storage", "Amazon managed"), inbound processing per box, outbound processing per box, and transportation per cubic foot. "there are no fees for enrolling in AWD". "AWD has simple, pay-as-you-go pricing with no additional costs for the holiday season." "Pay as you go, with available discounts and no seasonal surcharges." An inbound processing promotion runs "for eligible shipments received through December 31, 2026". [official] (sell.amazon.com/programs/warehousing, read 2026-11-09.) AWD from 2027-03-01: storage "vary based on inventory age, with inventory stored for more than 12 months charged at 2.5 times the standard rate" [opinion relaying Amazon: ppc.land 2026-11-06]. The 2027 Amazon letter says only that the full summary covers "Multichannel Fulfillment, and Amazon Warehousing and Distribution". [official]

M2. RULE (API). The AWD API v2024-05-09 carries no fee or cost field [command-verified: no `fee`/`cost`/`charge` property in awd_2024-05-09.json]. Role: Amazon Warehousing and Distribution (not on the door). [official] (Role Mappings for SP-API Operations, updatedAt 2026-10-28, local copy web01/role-mappings.md)

### N. Multi-Channel Fulfillment (as a charge)

N1. RULE (preview). MCF 2020-07-01 `getFulfillmentPreview` returns `estimatedFees` with `Fee.name` enum: `FBAPerUnitFulfillmentFee` ("Estimated fee for each unit in the fulfillment order"), `FBAPerOrderFulfillmentFee` ("Estimated order-level fee"), `FBATransportationFee` ("Estimated shipping fee"), `FBAFulfillmentCODFee` ("Estimated COD … fee"). In MCF 2026-07-04, price components have an open `type` (example `MCFTransportationFee`), and the preview has `excludeEstimatedFees` ("for latency optimization"). [official, command-verified] (fulfillmentOutbound_2020-07-01.json, fulfillmentOutbound_2026-07-04.json)

N2. RULE (where MCF fees are charged). Finances v0 `ShipmentEvent.OrderFeeList`: "A list of order-level fees. These charges are applicable to Multi-Channel Fulfillment orders." `OrderChargeList`: "applicable to Multi-Channel Fulfillment COD orders." [official, command-verified] (financesV0.json)

### O. FBA New Selection and new-seller credits (negative charges)

O1. RULE. "New Professional sellers can reduce their FBA costs through the FBA New Selection program, which offers free monthly storage, referral discounts, and fee waivers on eligible new-to-FBA products." Credits listed: "$400 credit for inbound placement costs", "$100 off shipments … using the Amazon Partnered Carrier program", "$200 credit towards fulfillment costs when you use Amazon Global Logistics", "Free storage and customer returns with auto-enrollment in the FBA New Selection program". [official] (sell.amazon.com/fulfillment-by-amazon, read 2026-11-09.) The Storage Fees report carries `eligible_for_inventory_discount`, `qualifies_for_inventory_discount`, `total_incentive_fee_amount`, `breakdown_incentive_fee_amount`. [official] (FBA Reports page.) Economics' `AggregatedDetail.promotionAmount`: "The promotion amount associated with this transaction type. This value is deducted from amount when computing totalAmount." [official, command-verified]

### P. Other marketplaces

P1. CA. The verifier read these on 2026-11-10 (sell.amazon.ca/pricing; News_Amazon CA a9383e96).
- The US 3.5% surcharge and the peak window apply ("in the US and Canada"). [official] (GABBX6GZPA8MSZGW v58, via the listing seat)
- What the fee covers and its basis: "Fee per unit includes picking and packing your orders, shipping and handling, customer service, and product returns. Fees are based on the weights and dimensions of your product." [official]
- A price band: "Products priced under CAD $14 receive rates CAD $0.80 less than standard FBA rates." [official]
- Shipping weight: "Shipping weight is the greater of the product's actual weight and its dimensional weight." Tiers are envelope, standard and oversize, by weight steps. [official]
- Storage: "charged monthly based on the daily average volume (measured in cubic metres)". It has January–September and October–December rates, standard vs oversize. "Additional fees apply for aged inventory (over 180 days), and high storage utilization." [official]
- Dangerous goods: "Lithium batteries … as well as dangerous goods … will incur a CAD $0.11 per-unit surcharge, in addition to the FBA fulfilment fee." [official]
- 2026: "there will be no increases to Canada referral and Fulfilment by Amazon fees". From 2025-11-05, FBA Liquidations: "Liquidations fees will include a 15% referral fee plus a per-item processing fee based on size and weight." [official] (News_Amazon, *2026 Updates to Canada referral and Fulfilment by Amazon fees*, https://sellercentral.amazon.ca/seller-forums/discussions/t/a9383e96-87ef-484e-bbe7-cc07584331bb)

P2. MX. The verifier read these on 2026-11-10 (vender.amazon.com.mx/precios).
- What the fee covers: "La tarifa por unidad incluye la recepción y empaque, envío y gestión, servicio de atención al cliente y devoluciones de productos de tus pedidos. Las tarifas se basan en el peso y dimensiones del producto … e incluyen IVA." (The per-unit fee covers picking and packing, shipping and handling, customer service and returns. Fees are based on weight and dimensions and include VAT.) [official]
- Four price bands. The table applies "a todas las categorías de producto excepto Salud y Cuidado personal, Alimentación y Comida gourmet, y Bebidas alcohólicas" (to every category except Health and Personal Care, Grocery and Gourmet, and Alcoholic Beverages), which have their own table. The bands are "Productos menores a MXN 150", 150–299, 299–499, and "en y mayor a MXN 499". The table is dated "Tarifas actualizadas el 4 de junio de 2026". [official]
- Storage: "Se mide en decímetros cúbicos (dm3), se calcula un promedio diario y se cobra de forma mensual" (measured in cubic decimetres, averaged daily and charged monthly). It has January–September and October–December rates, standard vs large. [official]
- Aged storage: "Aplica únicamente a inventario que ha permanecido en centros de distribución de Amazon por 181 días o más" (applies only to stock held 181 days or more), in bands 181–210 … 331–365 and "366 días o más" (366 days or more, the greater of a per-dm³ rate or a per-unit rate). [official]
  - The same page, further down, still says "por más de 271 días" (for more than 271 days). The page contradicts itself. The banded table is the more detailed text, and the charged line is the record.
- Removal and disposal are per unit, with average rates; all figures include IVA. [official]
- Fee Preview splits MX fees into `estimated-pick-pack-fee-per-unit` and `estimated-weight-handling-fee-per-unit`. [official] (FBA Reports page.) Remote Fulfillment from the US into CA, MX and BR carries the surcharge [opinion].
P3. EU/UK: sections B–H above, from the three 2026 rate cards. `PAN_EU_OVERSIZE_FEE` exists in economics preview. [official]
P4. BR, IN, TR, SA, AE, EG, SG: Fee Preview carries `estimated-fixed-closing-fee`. [official.] IN uses `NetCo` network commingling transactions (`NetworkComminglingTransactionEvent`, "Available only in the India marketplace"). [official, command-verified]
P5. JP. The verifier read these on 2026-11-10 (sell.amazon.co.jp/pricing; gs.amazon.cn news-notices-251202).
- What the fee covers: 「1点あたりの料金は、注文商品のピッキング・梱包・配送・カスタマーサービス・返品の料金を含みます。」 (The per-unit fee covers picking, packing, delivery, customer service and returns.) [official]
- A price band at ¥1,000: separate columns 「価格が1,000円を超える商品」 (items priced above ¥1,000) and 「価格が1,000円以下の商品」 (items priced at ¥1,000 or less). [official]
- Size by the sum of the three sides: 「寸法＝梱包済み商品の長さ、幅、高さの合計です。」 (Dimension = the sum of the packed item's length, width and height.) Tiers are 小型 (small), 標準 (standard), 大型 (large) and 特大型 (extra-large). [official]
- Tax included: 「上記の手数料には10％の消費税が含まれます。」 (The fees above include 10% consumption tax.) [official]
- Storage is a formula: rate × (item volume in cm³ ÷ 1,000 cm³) × days stored ÷ days in the month, at January–September and October–December rates. Small/standard and large/extra-large differ, and apparel, shoes and bags have their own rates. 「フルフィルメントセンターでの保管期間が365日を超えた在庫については、長期在庫保管手数料が追加発生します。」 (Stock held more than 365 days incurs an additional long-term storage fee.) [official]
- The 2026 notice: FBA fees cut from 2026-04-01 for standard-size items of 20–80 cm and up to 5 kg. From 2026-04-15, 「所有非媒介类商品中，存储365天及以上的库存，每月每件收取最低20日元附加费」 (non-media stock stored 365 days or more pays a minimum surcharge of ¥20 per unit per month), and the media minimum rises from ¥10 to ¥20. First charge 2026-04-22, on the 2026-04-15 assessment. [official] (gs.amazon.cn, *2026亚马逊日本站销售佣金与亚马逊物流费用变更* (2026 Amazon Japan referral fee and FBA fee changes), 2025-12-02; the source help pages GRH54FUTD3C5LWWW and GMXDT9ELPWWDMDTY are linked but were not read)

P7. AU. The verifier read these on 2026-11-10 (sell.amazon.com.au/pricing).
- A price band at $13: "Fulfilment fee (for products with an item price equal to or greater than $13)" and "(… less than $13)". [official]
- Shipping weight: "For all Envelope-sized products: the product's unit weight; and For all Parcel and Oversize products: the greater of the product's unit weight or its dimensional weight in kg. To calculate dimensional weight, multiply the product's overall length, width and height in cm, then divide by 4,000." "The shipping weight for each unit will be rounded up to the nearest gram". [official]
- Storage: monthly on "the daily average volume (measured in cubic metres)", with January–September and October–December rates, standard vs oversize. [official]
- Aged surcharge: "The Aged Inventory Surcharge is separate from Inventory storage fees". Bands are 271–300, 301–330, 331–365 and "366 days or more" (the greater of a per-m³ or a per-unit rate), each with "Inventory assessment date: 15th of the month". [official]
- MCF has its own table, with standard, expedited and priority rates by size tier. [official]

P8. IN. The verifier read these on 2026-11-10 (sell.amazon.in/fees-and-pricing).
- The fee structure differs from other stores. "Most Amazon orders are subject to the above 3 fees": referral, closing and weight handling. [official]
- Weight handling (shipping) fees apply under FBA ("FC") and Easy Ship. They depend on weight and distance: "Local rate", "Regional rate" (same one of four regions) and "National rate". [official]
- Weight steps: "For standard-size items, the minimum chargeable weight is 500 gms", charged in 500 g multiples, "computed on volumetric or actual weight, whichever is higher", with "Volumetric Weight (kg) = (Length x Breadth x Height)/5000". [official]
- FC only: "Pick & Pack Fee (FC Only) This fee is charged per unit sold"; "Storage Fee (FC Only) … per cubic foot per month"; "FC Removal fee is charged per unit". Heavy & Bulky has its own criteria and rates. [official]
- Tax: "All fees above are displayed excluding taxes. We will apply Goods and Services Tax (GST)". [official]
- Closing fees vary by price band and fulfilment channel and rose on 2026-09-07 (selling-fees file B3). India also has `NetworkComminglingTransactionEvent` (P4).
P6. Finances v0 `listFinancialEvents` accepts Amazon Fulfillment in NA and FE only. AISP is EU only. [official] (Finances API, https://developer-docs.amazon/sp-api/docs/finances-api.md, updatedAt 2026-09-09)

### Q. Amazon-sold inbound transport and the duties passed through it: AGL, SEND, GWD, Amazon Freight

Added in the gap fill of 2026-11-10. Section L covers the domestic partnered carrier quoted in Fulfillment Inbound.

Q1. RULE (what AGL is and what its price covers).
- "With Amazon Global Logistics, you can ship ocean cargo or air freight from China directly to the Amazon fulfillment network in the US, UK, EU, and Japan, as well as ocean freight from Vietnam to the US."
- "Our pricing includes services for each step of the supply chain journey, including pickup at origin, export declaration, cross-border ocean and air freight transportation, destination customs clearance, and delivery to Amazon fulfillment centers or warehousing facilities. Plus, conveniently book, pay, and track shipments right in Seller Central."
- Onboarding is "Set up a payment method, provide your importer of record (IOR) details, and upload the required documents". Booking is through "the Send/replenish inventory workflow".
- FAQ: "We currently ship from mainland China, Hong Kong, and Vietnam to the US, UK, France, Germany, Italy, Spain, and Japan."

[official] (Amazon Global Logistics, https://sell.amazon.com/programs/amazon-global-logistics, read 2026-11-10 by curl.)

Customs brokerage is part of the price: "For FBA Sellers using Amazon Global Logistics, brokerage services are included in the price." Amazon Customs & Trade imports "in the United States, United Kingdom, European Union and Japan" and also provides bonds ("Yes, we provide bonds"). [official] (Amazon Customs & Trade, https://spcentral.amazon.com/nlp/customs-and-trade, read 2026-11-10)

Q2. RULE (who bills, and when). AGL Freight Service Terms, "Dated: January 14, 2026":
- §Preamble: Amazon "may engage its Affiliate(s) … including Beijing Century Joyo Courier Co., Limited, a Chinese company ("BCJ"). For China origin, domestic, and international outbound Services, "us" or "we" will mean BCJ. For international ocean carriage originating in China, "us" or "we" will mean BCJ."
- §9.5: "We, or an Affiliate as indicated on your invoice, will bill you for your shipment upon its delivery to Destination or as the fees, costs or expenses are incurred. You will receive statements of fees and any additional costs or expenses incurred".
- §7.9 (US ocean lanes): "Bills of Lading, Booking Orders, statement records and debit notes, and amendments thereof will be maintained by Amazon Logistics, Inc. for five (5) years. This information may be retrieved on Our Site."
- §9.6: if fees are unpaid, Amazon may assert a lien on the cargo, or withhold the bill of lading and other documents.

[official] (Amazon Global Logistics Freight Service Terms, https://supplychain.amazon.com/legal/service-terms/global-logistics-freight, read 2026-11-10 by curl)

Q3. RULE (what the seller pays, and how the quote differs from the charge). Same terms:
- §1.2: "You are responsible for all costs to ship your Cargo using the AGL Freight Program, including freight charges for ocean carriage and domestic transshipment as applicable, insurance, export, customs, duties, taxes, and any other fees and charges, regardless of the source."
- §9.1: "You will pay all fees and costs for your shipments at Destination, regardless of whether you are the IOR."
- §9.2: Amazon gives a "Preliminary Estimate" of "the end-to-end freight fee, customs clearance fee, and, if elected, palletization, loading, or other optional services fees", and a "Collection Fee Estimate" for pickup "within 48 hours of accepting a Booking Order". "Neither the Preliminary Estimate nor the Collection Fee Estimate include export and import duties and taxes, accessorial charges, and any fees for other services, such as MCF." The actual charge may differ "if the weight, size, or dimensions of your Cargo, as determined by us or the carrier, differs", or "if a different rate is in effect on the cargo ready date … the terminal or container freight station gate-in date".
- §9.3: accessorial charges per tariffs and rate cards, plus costs "arising due to any force majeure event".
- §2.5: changes and cancellations can carry "liquidated damages in the form of a cancellation fee".
- §7.2, §7.4, §7.6: the seller bears demurrage, detention, storage, re-export and disposal costs. Cargo not accepted "within 21 days of the date of the notice of delivery" is "deemed abandoned".
- §11.2: notice of "overcharges, duplicate payment, or overcollection" is due "within 180 days of receipt of the invoice". §11.3: an accepted claim may be met by a credit "to your account".

[official] (same page.) The search snippet of help page "Claims and reimbursements through Amazon Global Logistics" (GR384ESWC8HH8667) adds: "If you believe you have been incorrectly charged a fee, contact us to submit a claim"; the claim should identify the shipment and the fee. [official, via search snippet only; the page is a JS shell to a plain GET]

Amazon's Chinese course adds of duty: 「税金（Duty）是否包含在 AGL 下单时的报价中？不包含在报价中，清关行基于进口商提交的箱单发票信息生成税金单」 (duty is not in the AGL booking quote; the customs broker generates a duty bill from the importer's commercial invoice and packing list). Inspection costs: 「进口商将承担相关的检查费和额外仓储费。查验费用将在查验结束后才能确认」 (the importer bears exam and extra storage fees, which are known only after the exam). [official] (物流仓储：跨境物流 – 进口清关准备 (Logistics: cross-border logistics, import clearance), Amazon Global Selling course PDF, © 2026, https://m.media-amazon.com/images/G/28/AS/AGS/SU/CN_GS_CB_Logistics_Basics_Customs_Clearance.pdf, pp. 24–25, read 2026-11-10 [command-verified: text extracted with macOS PDFKit])

Q4. RULE (importer of record). §4.4: "You may designate yourself or any party (other than us) as the EOR or importer of record ("IOR") … The EOR and IOR retain sole responsibility for importing and exporting your Cargo. If you fail to designate any EOR or IOR, you will be listed as the EOR or IOR." §4.5: the EOR and IOR sign "a Power of Attorney" for "our designated customs broker". §4.3: Amazon engages "the customs broker of our choice … unless you elected during the Booking Order process to perform self-clearance". [official] (AGL Freight Service Terms.)

The Chinese course adds:
- An account needs an approved IOR for each import country: 「您的账户需要有对应进口国的、通过审核的海关登记进口商（Importer of Record，IOR）」.
- In the US a bond is required (「确保进口商履行其向美国海关支付所有进口商品关税、税费及相关费用的义务」, which guarantees the importer pays all duties, taxes and related fees on imported goods).
- In the EU and UK the importer needs an EORI and a VAT number, a POA, and a PVA signature for the UK.
- In Japan, non-resident importers clear through an ACP (Japan's customs agent for non-residents).

[official] (same PDF, pp. 9–10, 26–28, 39–40.) So Amazon is the customs broker on an AGL entry, not the importer [seat, from §4.4 and the Customs & Trade page]. A practitioner states it outright: "AGL only makes Amazon Customs and Trade your broker, not your IOR." [opinion: Andrew Erickson, Inventory Hero, 2026-05-27]

Q5. RULE (how AGL is paid and where it is recorded). Help page *Paying for Amazon Global Logistics* (GZJ4B4HXDUEWP4PC). The page is a JS shell to a plain GET; the text below is from search snippets.
- "You can pay for Amazon Global Logistics shipments in two ways: With a disbursement account through Seller Central, or via wire transfer through Shipper Central."
- CNY: pay "in Chinese yuan (CNY) or renminbi (RMB) via wire transfer" through Shipper Central.
- USD from the disbursement account: "Fees are charged against the account within 48 hours after a shipment is received at a fulfillment center. If inventory is being distributed to multiple fulfillment centers, fees are charged 7 days after delivery to the first fulfillment center. If there are additional fees, they will typically be charged seven days after the shipment has been received and, if necessary, charged again 14 days later."
- "Be sure to have a sufficient balance in your Seller Central account when making payment." Otherwise Amazon may collect by other means the agreement allows.
- "Amazon Global Logistics freight charges will appear as FBA International Freight Shipping Charge and FBA International Freight Duties and Taxes Charge". They are found in the payments dashboard → Transaction View, filtered by Service Fees.

[official, via search snippets of https://sellercentral.amazon.com/gp/help/external/GZJ4B4HXDUEWP4PC, 2026-11-10]

Copies of Amazon's EU/UK onboarding guide, seen only as search snippets, say EU shippers pay in EUR, UK shippers in GBP, and "Non-CN based entities cannot pay in CNY". A CNY payer receives "a Chinese tax bureau invoice". [opinion/snippet: manuals.plus reproductions of Amazon guides; a plain GET returned a bot check, so not read]

[seat] Under that wording, a wire-paid AGL shipment is billed in Shipper Central and does not appear among the seller-balance charges. A balance-paid one appears there as two kinds of line: freight, then duties and taxes. "Additional fees" can follow 7 and 14 days later.

Q6. RULE (when US duty is fixed, and how it is corrected). Amazon's Chinese course, US section:
- Deadlines: ISF 24 hours before sailing; pre-clearance documents by ATD + 3 days; entry within 15 days of arrival.
- 「AGL 提交清关申报后，请在收到税金单3天内确认或提出争议」 (after AGL files the entry, confirm or dispute the duty bill within three days). 「如卖家未提出争议或确认税金单，72小时内系统会自动确认税金单」 (unconfirmed bills auto-confirm within 72 hours).
- Payment: 「清算前 完成税金支付」 (duty is paid before liquidation). Either 「若选择 AGL 服务，清关行可为进口商先行支付税金」 (with AGL the broker can advance the duty for the importer), or the importer pays CBP directly through an ACH account (「一般是6位数字的"PUN"账号」, usually a six-digit PUN account).
- Changes after auto-confirmation: before the preliminary statement date, email the broker. After it and until 15 days before liquidation, a Post Summary Correction (PSC). Within 180 days after liquidation, a Protest, the "last chance".

[official] (CN_GS_CB_Logistics_Basics_Customs_Clearance.pdf, pp. 8, 19–24.)
- EU/UK: 「税金单收到后3天内：确认税金单或提出争议」 (confirm or dispute the duty bill within three days of receipt). [official] (p. 27.)
- Japan: the duty bill auto-confirms after 24 hours, and 「税金支付后，海关才可放行」 (customs releases only after duty is paid). A non-resident importer's customs value is computed by a deductive method from the Amazon sales price, less FBA outbound fee, referral fee and local transport. The FBA cost report (FCR) is 「海关唯一认可的税基扣减凭证」 (the only document customs accepts for the deduction). [official] (pp. 43, 48)

[seat] So the duty line on an AGL shipment can be revised after its first posting, by PSC or protest, months after the goods were sold. Whether a revision posts back to the seller balance, or is settled between the IOR, the broker and CBP, is not stated (open question 14).

Q7. RULE (AGL placement options change which FBA inbound charges apply). From the AGL page:
- Amazon Managed Placement: "It's a flat, all-inclusive, per-shipment rate solution that includes other destination charges required for placement. That means you won't be charged for the FBA inbound placement service separately."
- Seller Managed Placement: "eliminating inbound placement service costs". It requires "at least five identical box quantities per item".
- "Minimal shipment splits incur FBA inbound placement service costs."
- Ship to AWD: "AWD pricing covers FBA inbound placement, so there is no separate charge for this service."

[official] (sell.amazon.com/programs/amazon-global-logistics.) [seat] So, for an AGL shipment, whether a separate placement line (section C) follows about 45 days after receipt depends on the placement option booked.

Q8. RULE (Amazon SEND, the cross-border partnered carrier). US page:
- "You will be billed in US dollars. Costs are posted to your Seller Central account, similar to FBA and other Amazon services." Charges are under Reports → Payments → Transaction View.
- "Freight charges are posted to your Seller Central account within 24 hours of booking and appear as "FBA international shipping charge.""
- "If your shipment incurs customs duties at the destination, the costs will be charged to your account after delivery based on the actual duty charged to the carrier by customs. Customs duty charges appear as "FBA international shipping customers charge.""
- "The carrier does not provide any invoices for shipping costs."
- Charges can be voided within a 24-hour cancellation period ("Void Charges").

[official] (Amazon SEND (Seller Export & Delivery), https://sell.amazon.com/programs/seller-export-and-delivery, read 2026-11-10.) The Chinese copy names the lines 「亚马逊物流国际运费」 and 「亚马逊物流国际运输买家费用」. [official] (https://sell.amazon.com/zh/programs/seller-export-and-delivery, read 2026-11-10.) Australia differs: "you are required to enter a contract directly with an external carrier and manage payments with them directly offline". "If customs duty is charged on the shipment by destination Customs, the partnered carrier will pay the customs duty, and the same will be charged to the seller by the partnered carrier." [official] (Amazon SEND, https://sell.amazon.com.au/amazon-send, read 2026-11-10.) SEND destinations: "the US, the UK, Germany, Japan, the UAE, Saudi Arabia, and Australia". [official, US page]

Q9. RULE (Global Warehousing and Distribution, GWD).
- "Starting April 9, 2026, you can store your inventory in bulk … in our new Global Warehousing & Distribution (GWD) facility in Shenzhen, China, and seamlessly replenish to our US fulfillment network". It includes "shipping, customs clearance, and delivery to our fulfillment centers all through a single, integrated solution". New users are onboarded "to AGL if you haven't used AGL services previously". [official] (News post *Introducing Global Warehousing & Distribution — now available in Shenzhen, China*, https://sellercentral.amazon.com/seller-forums/discussions/t/91f2bda1-ff49-456e-9319-9b61058c7c03, 2026-04-09, read 2026-11-10)
- "30 days of free storage … for every shipment received at an active GWD distribution center between July 1 and December 31, 2026"; Shanghai from 2026-07-16. "With the FOB incoterm, you can obtain separate invoices for export declaration and origin port handling charges to support your export tax rebate process." [official] (News post *Send to Global Warehousing and Distribution and get 30 days of free storage*, https://sellercentral.amazon.com/seller-forums/discussions/t/20c69db3-7a11-459a-b265-6d7e0eb434fa, 2026-07-07, read 2026-11-10)
- Sellers asked in both threads for the GWD fee schedule; no Amazon reply in the thread text gives one. [official absence, as read]

Q10. RULE (Amazon Freight, domestic truckload). Amazon Freight bills through its own shipper account: "Log in to your shipper account to manage all your Amazon Freight invoices in one place … Use the 'Actions' column of the Billing & Payments table to download an invoice, view BOLs, and even file a claim". [official] (*How to use Amazon Freight's online tools to your advantage*, https://freight.amazon.com/newsroom/shipper-tips/26-use-af-portal, 2026-02-09, read 2026-11-10.) "We review shippers' payment history and the orders placed with Amazon Freight, along with financial and credit history to determine the credit limit." "Credit limits can be reviewed on a monthly basis." [official] (Amazon Freight UK, *Streamlined credit approval*, https://freight.amazon.co.uk/newsroom/streamline-credit-limit-approval, 2024-06-25, read 2026-11-10.) The Amazon Freight terms page (https://freight.amazon.com/terms) requires sign-in, so it was not read.

Q11. RULE (partnered-carrier inbound transport as a posted charge). An Amazon reply in the EU forums says: "You can access FBA inbound charges by date through the payment reports. First navigate to reports and then payments. After selecting payments change the transaction to service fees. You will then be able to see the cost for FBA Inbound Transportation Charges." [official, forum reply by Dominic_Amazon] (*Inbound transportation fee Report*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2583156f-b480-44d3-8271-bbeb752c0df8, thread 2023-02-02, read 2026-11-10)

## The SP-API and report faces

Rates are the model's default usage plans [command-verified]. Roles come from Role Mappings for SP-API Operations (updatedAt 2026-10-28) and Role Mappings for SP-API Types (updatedAt 2026-09-09), local copies in web01/ [official]. "AF" = Amazon Fulfillment. The door holds Product Listing, Pricing, Brand Analytics, Finance and Accounting (F&A).

### Money records (charges as posted)

| Read | Path / type | Model | Rate (rps / burst) | Role | What carries fulfilment & storage charges | Pitfalls Amazon names |
|---|---|---|---|---|---|---|
| `listTransactions` | `GET /finances/2024-06-19/transactions` | finances_2024-06-19.json | 0.5 / 10 | F&A | Every posted transaction; `breakdowns[]` nested `breakdownType`/`breakdownAmount`; `items[].contexts` incl. `ProductContext` (asin, sku, quantityShipped, fulfillmentNetwork) and **`TimeRangeContext` (`startTime`/`endTime`, the period a charge covers)**; `ItemRelatedIdentifier` includes `REMOVAL_SHIPMENT_ITEM_ID` | "Financial events might not include orders from the last 48 hours." >180 days apart → empty. Empty pages with `nextToken`. "`breakdownType` is an open-ended string; Amazon does not publish a closed list of values" (Get the latest transactions, read 2026-11-09). `transactionType` lists only `Shipment`. |
| `listSummary` | `GET /finances/2024-06-19/summary` | same | 0.5 / 10 | F&A | `breakdowns` by `Sales` / `Expenses` / `Refunds` per settlement or period (model example) | Added 2026-07-29 |
| `listBalances` | `GET /finances/2024-06-19/balances` | same | 0.5 / 10 | F&A | Balances, not charges | — |
| `listFinancialEvents` | `GET /finances/v0/financialEvents` | financesV0.json | 0.5 / 30 | F&A, AF (NA, FE), AISP (EU) | `ShipmentEventList` (`ItemFeeList` per unit: FBA fees ride here; `ShipmentFeeList`; `OrderFeeList` for MCF), `RefundEventList` (`ItemFeeAdjustmentList`), `ServiceFeeEventList` (`FeeReason`, `FeeList`, `SellerSKU`, `FnSKU`, `ASIN`, `FeeDescription`), `AdjustmentEventList`, `RemovalShipmentEventList`, `RemovalShipmentAdjustmentEventList`, `FBALiquidationEventList` (US), `CapacityReservationBillingEventList`, `ValueAddedServiceChargeEventList` ("For example, 'Other Support Service fees'"), `TrialShipmentEventList`, `NetworkComminglingTransactionEventList` | Deprecated 2025-07-21, **removal 2027-08-27**. Deferred events hidden until released. `FeeType` is a free string pointing to G200336920 / G201074400. |
| `listFinancialEventsByGroupId` | `…/financialEventGroups/{id}/financialEvents` | same | 0.5 / 30 | F&A, AISP (EU) | Same lists, one settlement group | Removal 2027-08-27; two years back only |
| `listFinancialEventsByOrderId` | `…/orders/{orderId}/financialEvents` | same | 0.5 / 30 | F&A | Order-scoped only: account-level storage, placement, capacity never appear here [seat] | Removal 2027-08-27 |
| `listFinancialEventGroups` | `GET /finances/v0/financialEventGroups` | same | 0.5 / 30 | F&A, AISP (EU) | Settlement groups | Not on the removal schedule |
| Settlement V2 | `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` via `getReports` | reports_2021-06-30 | getReports 0.0222 / 10; getReportDocument 0.0167 / 15 | F&A | `transaction-type`, `amount-type`, `amount-description`, `amount`, `sku`, `order-id`, `posted-date`: one row per charge | "Settlement reports cannot be requested or scheduled." "Price columns are condensed into three general-purpose columns". "amounts are displayed in local currency formats (for example, `95,00` for EU)". V1 flat file and XML removal **2026-11-11**. |
| Transfers `listPayouts` | `/finances/transfers/2024-06-01/payouts` | transfers_2024-06-01.json | 0.5 / 10 | F&A | Payouts only | — |

### Itemising reports (what a charge was for)

| Report type | Roles | Requested / scheduled | Money columns | Notes Amazon gives |
|---|---|---|---|---|
| `GET_FBA_STORAGE_FEE_CHARGES_DATA` (FBA Storage Fees) | Pricing, AF | requested or scheduled | per ASIN/FNSKU × FC × `month_of_charge`: `product_size_tier`, `average_quantity_on_hand`, `average_quantity_pending_removal`, `estimated_total_item_volume`, `storage_rate`, `storage_utilization_ratio`, `base_rate`, `utilization_surcharge_rate`, `avg_qty_for_sus`, `est_vol_for_sus`, `est_base_msf`, `est_sus`, `estimated_monthly_storage_fee`, `dangerous_goods_storage_type`, discount/incentive columns, `average_quantity_customer_orders` | "Contains **estimated** monthly inventory storage fees for each ASIN". This is the only per-product split of storage Amazon gives. |
| `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` | Pricing, AF | requested | `snapshot-date`, sku, fnsku, asin, `per-unit-volume`, `qty-charged`, `amount-charged`, `surcharge-age-tier`, `rate-surcharge`, `country` | "the time between the `dataStartTime` and the `dateEndTime` … should be equal to one month" |
| `GET_FBA_INVENTORY_PLANNING_DATA` | **AF only** | requested | `estimated-storage-cost-next-month`, `quantity-to-be-charged-ais-<band>` + `estimated-ais-<band>`, LIL flags, `qty-to-be-charged-ltsf-6-mo/12-mo`, `estimated-ltsf-next-charge` | Forward estimates, not charges. "Attributes vary by store." |
| `GET_FBA_OVERAGE_FEE_CHARGES_DATA` | **AF only** | requested | `charged_date`, `charge_rate`, `overage_volume`, `charged_fee_amount` | "Estimated inventory storage overage fees" |
| `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` (Fee Preview) | Pricing, AF | requested, "once per day per seller" | per SKU dims, `product-size-tier` (US), `expected-fulfillment-fee-per-unit` (US, CA), future-fee columns (US, MX), EU EFN per-destination fees, `estimated-fee-total` | "updated at least once every 72 hours"; `dataStartTime` ≥ 72 h before now |
| `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA` (Inbound Performance) | Pricing, AF | requested | `problem-type`, `coaching-level`, `fee-type`, `fee-total`, per shipment/carton/FNSKU | "Content updated daily." The only report that itemises unplanned-service/defect fees. |
| `GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA` | Pricing, AF | requested | `order-type`, `order-status`, `requested/cancelled/disposed/shipped/in-process-quantity`, **`removal-fee`**, `currency` | "near real-time" |
| `GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA` | Pricing, AF | requested | none (tracking) | "will not include canceled returns or disposed items" |
| `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` | Pricing, AF | requested | none (returns detail for joining to returns fees) | — |
| `GET_FBA_REIMBURSEMENTS_DATA` | Pricing, AF | requested | `amount-per-unit`, `amount-total`, `reason`, `original-reimbursement-id/type` | Money received; reimbursements seat |
| Inbound placement fee report | — | — | — | **No SP-API report type exists** for the placement fee or the low-inventory-level fee [command-verified: not on report-type-values-fba.md or report-type-values.md]. Seller Central has a download under Reports → Payments, "亚马逊物流入库配置服务费用" [opinion: 优麦云 SellerSpace help, 2024-10-10, https://www.sellerspace.com/help/storage-configuration-fee-use-guide]. |
| Returns-processing breakdown | — | — | — | Amazon names "a report from Amazon Fulfillment reports" breaking down shipped, returned, over-threshold and charged units (GZGEQLTM3RZXUV6T). **No matching SP-API report type found** [command-verified]. |
| AWD reports | — | — | — | No AWD report type in the FBA or main report lists [command-verified]. |

Report generation limits: near real-time FBA reports "no more than once every 30 minutes", daily ones "no more than once every four hours". [official] (FBA Reports page.) Reports API: `createReport` 0.0167 / 15 [command-verified].

### Estimates and previews (not charges)

| Read | Path | Model / rate | Role | Fulfilment content |
|---|---|---|---|---|
| `getMyFeesEstimateForSKU` / `…ForASIN` | `POST /products/fees/v0/listings/{SellerSKU}/feesEstimate`, `…/items/{Asin}/feesEstimate` | productFeesV0.json, 1 / 2 | long list incl. F&A, Pricing, Product Listing, AF | `FeeDetailList` (`FeeType` free string, `FeeAmount`, `FeePromotion`, `TaxAmount`, `FinalFee`); `IsAmazonFulfilled`; `OptionalFulfillmentProgram` `FBA_CORE` / `FBA_SNL` / `FBA_EFN`. SKU uses measured dims, ASIN uses catalog size. "not guaranteed". It estimates per-sale fees (referral, closing, FBA fulfilment), not storage, placement or removal [seat, from FeeDetail semantics; no storage input exists]. |
| `getMyFeesEstimates` | `POST /products/fees/v0/feesEstimate` | 0.5 / 1, ≤ 20 items | Pricing, Product Listing | same |
| Data Kiosk `economics` | `POST /dataKiosk/2023-11-15/queries` (0.0167 / 15), `getQuery` (2 / 15), `getDocument` (0.0167 / 15) | analytics_economics_2024_03_15 | Role Mappings (2026-10-28) and the Data Kiosk API page (updatedAt 2026-10-20): Brand Analytics on all five operations. Amazon's changelog *Correction: Data Kiosk role requirements* (timestamp 2024-07-02; https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements): "The initial version of that announcement stated that all datasets require the Brand Analytics role. This is not correct. The Vendor Analytics and Sales and Traffic datasets require the Brand Analytics role. The Economics dataset requires the Selling Partner Insights role." The Data Kiosk page also says "Each field available with Data Kiosk requires a certain role", checked "upon query creation". (**conflict, unresolved**; the `createQuery` reply settles it) | **Charged** fees per product and date: `fees[].feeTypeName`, `charges[]` with `aggregatedDetail` (`amount` "calculated by rate card", `promotionAmount`, `taxAmount`, `totalAmount`, `quantity` "may be null or may not be an integer" when not per unit, `amountPerUnitDelta` across a fee change), `components` for `FBA_FULFILLMENT_FEE` / `FBA_STORAGE_FEE`, `properties` (e.g. size tier). Ranges split at a fee-change date. P30D retention. Two years back. Daily refresh. |
| Data Kiosk `economicsPreview` | same | same | same | ≤ 120 days ahead, MSKU × RANGE, `feeTypes` incl. `LOW_INVENTORY_LEVEL_FEE`, `FBA_INBOUND_PLACEMENT_SERVICE_FEE`, `AGED_INVENTORY_SURCHARGE`, `STORAGE_UTILIZATION_SURCHARGE`, `HIGH_RETURN_RATE_FEE`, `RETURN_PROCESSING_FEE`, `PAN_EU_OVERSIZE_FEE`, `BASE_FBA_FULFILLMENT_FEE`, `FBA_FULFILLMENT_FEES`, `BASE_MONTHLY_STORAGE_FEE`, `MONTHLY_INVENTORY_STORAGE_FEES` |
| Inbound `listPlacementOptions` / `listTransportationOptions` / `listDeliveryWindowOptions` / `getShipment` | `/inbound/fba/2024-03-20/…` | 2 / 6 (`listDeliveryWindowOptions` 2 / 30) | **AF only** | Placement `fees`/`discounts` (Incentive), transport `quote.cost`, window `discounts` |
| MCF `getFulfillmentPreview` | `POST /fba/outbound/2020-07-01/fulfillmentOrders/preview` | 2 / 30 | AF | `estimatedFees` (four named fee types) |
| Notification `FEE_PROMOTION` | — | FeePromotionNotification.json | F&A, Product Listing | `FeePromotionType`, `FeeType`, `FeeDiscountType`/`Value`, `PromotionActiveTimeRange`; needs SQS/EventBridge |

### Amazon-sold inbound transport (AGL, SEND, GWD, Amazon Freight): what the API carries

Added in the 2026-11-10 gap fill.

| Read | Path / model | Rate | Role | What it carries for this charge | Limits |
|---|---|---|---|---|---|
| `listTransactions` | `GET /finances/2024-06-19/transactions`, finances_2024-06-19.json | 0.5 / 10 | F&A | Balance-paid AGL and SEND lines, under whatever `transactionType` / `breakdownType` / `description` Amazon gives them. `relatedIdentifiers[]` can name `SHIPMENT_ID` ("The `ShipmentId` that is associated with the transaction") and `INVOICE_ID`. `PaymentsContext` has `paymentMethod` and `paymentReference`. | Filters are `ORDER_ID` and `FINANCIAL_EVENT_GROUP_ID` only. The model does not say whether an AGL line's `SHIPMENT_ID` is the FBA inbound shipment ID (open question 15). Wire-paid AGL is not a balance transaction [seat, Q5]. |
| `listFinancialEvents…` (v0) | financesV0.json | 0.5 / 30 | F&A (+AF NA/FE) | `ServiceFeeEvent` has `AmazonOrderId`, `FeeReason`, `FeeList` (`FeeType` free string), `SellerSKU`, `FnSKU`, `ASIN` and `FeeDescription`. It has **no inbound-shipment field** [command-verified]. Practitioners put the AGL codes `FBAInternationalInboundFreightFee` / `…TaxAndDuty` here (section 5). | Removal 2027-08-27 |
| Settlement V2 | `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` | (as above) | F&A | One row per line, with `amount-description` and `order-id`. A practitioner reports that partnered-carrier transport rows carry the FBA shipment ID in `order-id` from 2025-06-01; whether AGL rows do is open (question 15). | — |
| Fulfillment Inbound v2024-03-20 | `listTransportationOptions`, fulfillmentInbound_2024-03-20.json | 2 / 6 | AF | `shippingMode` includes `OCEAN_LCL`, `OCEAN_FCL`, `AIR_SMALL_PARCEL` and `AIR_SMALL_PARCEL_EXPRESS`. `shippingSolution` is only `AMAZON_PARTNERED_CARRIER` or `USE_YOUR_OWN_CARRIER`. `quote.cost` is the partnered-carrier quote [command-verified]. | No AGL or SEND solution value, and no duty field. Gerpgo lists AGL among what "亚马逊未提供API" (Amazon provides no API for) [opinion, 03-job-stock.md]. |
| Tracking API `getShipmentTracking` | `GET /tracking/2026-01-30/shipments/track`, tracking_2026-01-30.json | — (not in model text) | **grantless**, NA (US only) (Role Mappings 2026-10-28) | Look-up by `containerNumber`, `houseBillOfLadingNumber`, `aftn`, `acsin`, `proNumber` or carrier tracking. Milestones include `CUSTOMS_CLEARED`, `CUSTOMS_HOLD`, `CUSTOMS_PAYMENT_REQUIRED`, `DELIVERED`, and `occurredAt` dates. Also pushed as `SHIPMENT_TRACKING_MILESTONE_CHANGED`. | Launched 2026-08-05. No amounts [command-verified]. |
| Invoices API v2026-06-25 | `getInvoiceHeaders` / `getInvoice`, financesInvoices_2026-06-25.json | — | not in the local Role Mappings copy | `invoiceType` is `AP_INVENTORY` or `OTHER`. Related identifiers are vendor-side (PO, ASN, vendor code). `serviceChargeType` is `DAMAGE_ALLOWANCE`, `PRICE_PROTECTION`, `FBA_INVENTORY_STORAGE_FEE` or `OTHER`. | No freight, AGL or duty field [command-verified]. Not shown to carry AGL debit notes. |
| Data Kiosk `economics` | `FbaPerUnitCost.shippingToAmazonCost` | (as above) | (conflict, see above) | "Cost of shipping the … (FBA) item to an Amazon fulfillment center. This value is provided by the seller" [official, command-verified] | The seller's own figure, not Amazon's charge |
| AGL booking, Preliminary Estimate, Shipper Central statements, debit notes, broker duty bills | — | — | — | — | **No SP-API operation** [command-verified: "Global Logistics" and "AGL" appear nowhere in the models clone or ops.tsv] |

Model history: `BusinessContext.storeName` gained `AMAZON_FBA_FROM_ORIGIN` ("Transactions associated with FBA from origin.") on 2026-10-28, and the rollback db2936aa (2026-10-29) removed it. The live model has only `AMAZON_HAUL`. [command-verified: GitHub commit diff.] Whether "FBA from origin" names GWD or AGL lines is not stated (open question 16).

**Deprecation dates that touch this area.** Settlement V1 flat file and XML: removal 2026-11-11. Finances v0 `listFinancialEvents`, `…ByGroupId`, `…ByOrderId`: removal 2027-08-27. Inbound v0 transport ops: removed 2025-01-21. FBA Small and Light: removed 2023-09-26 (NA/EU) and 2024-03-27 (JP), so `FBA_SNL` is dead there. Economics `FNSKU` granularity: removed 2025-12-22. [official] (Deprecation Schedule; release notes, updatedAt 2026-11-04)

**Model vs release notes (re-checked 2026-11-10).**
- The release note of 2026-07-29 says: "Added the `SETTLEMENT_ID` value for the `relatedIdentifierName` query parameter for the `listTransactions` operation."
- On GitHub, commit df7c6298 (2026-10-28) put it into the model's filter text. The next commit, db2936aa (2026-10-29, "SPAPI October Release Finance API Rollback"), took it out again. Its diff replaces "`FINANCIAL_EVENT_GROUP_ID`, `ORDER_ID`, and `SETTLEMENT_ID` are the only `relatedIdentifier` with filtering capabilities at the moment" with "`FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID` are the only `relatedIdentifier` with filtering capabilities at the moment". The same commit also removed the `AMAZON_FBA_FROM_ORIGIN` store name. [command-verified: GitHub commit API, db2936aa]
- The live reference page (https://developer-docs.amazon/sp-api/reference/listtransactions.md, read 2026-11-10) has the two-value text.
- So the filters are `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`. `SETTLEMENT_ID` filters `listSummary` ("The only possible value is `SETTLEMENT_ID`"), and it appears in `listTransactions` only as a response `relatedIdentifiers` value.
- The release note still carries the claim (updatedAt 2026-11-04).

**Economics fee types.** The release note of 2026-09-30 adds deal, coupon, removal, disposal and fuel fees to economics. The schema's `PreviewFeeType` enum has none of them [command-verified]. The change may be in `fees[].feeTypeName`, which is a free string, rather than in an enum [seat].

## What practitioners add

**Names on the money lines (none of this is an Amazon list).** Amazon "does not publish permitted values for transaction-type, amount-type or amount-description" [opinion: xieyi138-star/amazon-settlement-parser README, GitHub, 2026, data file updated 2026-08-12]. Names vendors report, with the field they put them in:
- Fulfilment: `FBAPerUnitFulfillmentFee` (ItemFees), `FBAPerOrderFulfillmentFee` (Shipment-Fees in one source, ItemFees in another), `FBAWeightBasedFee` (ItemFees), `FBATransportationFee` (MCF shipping; Intentwise ties it to MCF, not inbound), "Multi-Channel Fulfillment Brand-Neutral Box Fee". [opinion: Webgility help 2025-10-26; Intentwise mapping guide; the GitHub parser]
- Storage: `Storage Fee` and `StorageRenewalBilling` under other-transaction (Webgility, parser); `FBAStorageFee`, `FBALongTermStorageFee` as v0 FeeType codes (AMALYTIX 2026-10-20, which says the long-term name now carries the monthly aged surcharge). AMALYTIX says the storage utilization surcharge, the low-inventory fee and the fuel surcharge have **no fee type of their own** in the SP-API financial data. MyProfit (2026-10-03) groups "FBA Inventory Storage Fee", "FBA Long Term Storage Fee", "Removal Order Disposal / Return Fee", "FBA Inbound Placement Service Fee" and "Inbound Transportation Fee" under a `FBAFees` transaction type.
- Inbound: `FBAInboundTransportationFee`, `FBAInboundTransportationProgramFee` (AMALYTIX: about 7% of the transport fee in its data), `FBAInboundDefectFee`, `FBAInboundShipmentCartonLevelInfoFee` (manual processing), AGL `FBAInternationalInboundFreightFee` / `…TaxAndDuty` [opinion: AMALYTIX].
- Removal/disposal: `RemovalComplete`, `DisposalComplete` (other-transaction); `FBARemovalFee`, `FBADisposalFee` (FeeType) [opinion: Webgility, parser, AMALYTIX].
- Returns: `FBACustomerReturnPerUnitFee`, `…PerOrderFee`, `…WeightBasedFee`; `CustomerReturnHRRUnitFee` (high return rate, monthly) [opinion: Webgility, AMALYTIX].
- Rare: `StorageReservationFee`, `STARStorageFee`, AWD `AmazonUpstreamStorageTransportationFee`, `AmazonUpstreamProcessingFee` [opinion: AMALYTIX, "rarely seen", no descriptions].
- Fee corrections and reimbursements of fees: `NonSubscriptionFeeAdj`, `INCORRECT_FEES_ITEMS`, `INCORRECT_FEES_NON_ITEMIZED`, `RE_EVALUATION` (no description) [opinion: AMALYTIX, Webgility].
- Sign: positive = credit, negative = fee [opinion: AMALYTIX, MyProfit; neither cites Amazon]. Amazon's own wording appears only for removal `FeeAmount`, "a negative number" [official].

**The charges sellers say are most often wrong.**
- Size-tier and dimension errors. A seller example of two same-weight colour variants charged US$1.37 apart [opinion: AMZ123 Q&A, 2024-12-19, https://www.amz123.com/ask/6VGZb5c9]. A seller reports losing US$10,000+ to a mis-measurement, with a step-by-step remeasure route. The same seller claims "亚马逊每月只给 20 次重测机会" (20 remeasurements a month) [opinion: Regan跨境, AMZ123, 2025-11-27, https://www.amz123.com/t/2kIZ4A7n; the 20 figure is unverified; Amazon says the limit is "based on the number of offers with inventory"]. Recovery vendors list "Pick & Pack overcharge" / "Incorrect weights and dimensions" as claim types [opinion: GETIDA, Seller Investigators, via 04-job-money.md §3].
- Ghost or unexpected inbound fees: EU threads "FBA Inventory Placement Fee charged on Shipment without placement service" and "Amazon is rediculously charging inbound placement fees and defect fees" [opinion: Seller Forums EU, titles only]. AWD threads "Incorrect AWD auto-replenishment charges" [opinion: title only].
- Billing timing as a cause of confusion: placement 45 days after receipt; removals now trickle in per unit; storage in the following month. Sellers misread these as duplicate or orphan charges [seat, from the rules above].
- Dispute route the Chinese community names for a wrong charge: open a case as "账单计算错误" (billing calculation error), with no known success rate [opinion: 双木@AMZ123 via 白鲸出海, 2026-09-11, https://www.baijing.cn/article/56666].

**How tools and sellers allocate account-level charges to products** (methods, not facts about Amazon):
- **Sellerboard**: "daily amortization for multiple Amazon fee categories — not just FBA storage fees". The categories are storage; removal and disposal; AWD storage, transport and processing; inbound transportation; international freight/duty/tax; "placement and convenience fees". It is set at Settings → General → Calculation logic. It "allocates storage and aged-inventory charges to individual products automatically"; the key is not stated [opinion: blog.sellerboard.com 2026-05-18 and 2026-07-14]. Note the name "convenience fees": the old v0 name `FBAInboundConvenienceFee` for placement survives in tools.
- **优麦云 SellerSpace**: placement fee imported from the Seller Central placement-fee CSV or synced by plugin and booked as an expense **per ASIN and date** (not spread). It warns of double counting for stores that had it auto-booked as 店铺其他成本 before 2024-08-16, and of a date mismatch ("Seller Central uses zero-timezone dates; the tool uses site-local dates"). "其他-FBA库存和入库服务费" can be allocated "只支持手动分摊" (manually only). Store rent, deals and Vine are allocated by last month's unit or sales share from the Payment report [opinion: sellerspace.com help, 2024-10-10 and 2024-09-04].
- **领星 Lingxing**: "店铺费用支持自定义分摊到产品维度" (store expenses custom-allocated to product level); basis not stated; returns, adjustments, removals and discrepancies booked to profit in one step [opinion: AMZ123 encyclopaedia entry supplied by the vendor, 2025-09-22, https://www.amz123.com/b/ygSxkvSd]. Earlier survey: profit from 结算中心 settlement data; 头程 allocated "按计费重、实重、体积重" [opinion, 04-job-money.md §3].
- **积加 Gerpgo**: "抓取相应亚马逊后台FBA库容统计" (pulls capacity statistics from Seller Central back office) four times a day; it lists "亚马逊未提供API" for partnered carrier [opinion, 03-job-stock.md]. Its fee-allocation pages were not reached.
- **赛狐 SellFox**: "解析1000+平台费用" (parses 1000+ platform fees) [opinion, 04-job-money.md]. Allocation method not found.
- **Seller practice**: storage as units × cubic feet × rate; peak and deal fees "平摊下来" (spread per unit) [opinion: AMZ123 2026-09-10]. Sellerboard's own manual model: cubic feet × months held × rate, with dwell time from days of cover [opinion].
- Common allocation keys named across vendors: volume (cubic feet), units, sales share, weight (for freight), or none (left as an account-level line) [opinion: the vendors above; beancount.io guides].

**AGL and other Amazon-sold freight as money lines** (added in the 2026-11-10 gap fill):
- **Names.**
  - AMALYTIX (updated 2026-10-20): `FBAInternationalInboundFreightFee` ("If your goods come from abroad with Amazon Global Logistics (AGL), this line holds the freight costs"), `FBAInternationalInboundFreightTaxAndDuty` ("Amazon charges taxes and duties for international shipments through … AGL"), and `GlobalInboundTransportationFreight` / `GlobalInboundTransportationDuty` ("If Amazon handles the import of goods for you … Amazon passes this amount on").
  - MyRealProfit's glossary maps `FBAInternationalInboundFreightFee` to "FBA International Freight Shipping Charge" and `FBAInternationalInboundFreightTaxAndDuty` to "FBA International Freight Duties and Taxes Charge", which are Amazon's display names (Q5).
  - Synder lists a separate "FBA International Freight Shipping Charge Adjustments".

  [opinion: amalytix.com; intercom.help/myrealprofit; synder.com, all read 2026-11-10.] None is an Amazon list.
- **A contradiction to note.** Synder writes that for "FBA International Freight Duties and Taxes Charge", "Amazon, as the receiver, pays all the duties and taxes when your shipment arrives". Amazon's own terms make the seller (or its designee) the importer, and Amazon's broker can only advance the duty (Q4, Q6). [opinion vs official]
- **Timing and payment.** Threecolts (2025-11-24): "USD payment via your Seller Central disbursement account charges your balance within 48 hours after delivery. CNY payment through wire transfer via Shipper Central gives you local currency options." Its "hidden costs" are pickup fees "provided 48 hours after booking", "Customs duties and taxes (excluded from base quotes)", "Amendment fees" and "Defect fees". [opinion: https://www.threecolts.com/blog/?p=9447]
- **Importer and refunds.** Inventory Hero (Andrew Erickson, 2026-05-27): "Amazon Global Logistics users are still the IOR (Amazon is only the broker)". "Entries starting with the prefix INL were brokered by Amazon Customs and Trade". Amazon Customs and Trade "emailed this list automatically in April 2026" (IEEPA duties per entry). CBP refunds "by ACH to an account at a bank with a US branch", outside Amazon. [opinion: https://www.inventoryhero.ai/blog/how-to-get-trump-tariff-refund]
- **Joining charges to shipments.** A seller reports that from 2025-06-01 the partnered-carrier line is "Inbound Transportation Fee" with "an associated order (shipment) id in the order id column", and that earlier lines carry only the settlement ID. [opinion: sellersasksellers.com, 2026-03-24, https://sellersasksellers.com/t/reconciling-fba-inbound-shipment-fee-on-2025-transaction-report/7053.] No practitioner page read says whether AGL lines carry the shipment ID.
- **Chinese ERPs.** 积加 (Gerpgo) lists AGL among the things for which "亚马逊未提供API" (Amazon provides no API) [opinion, 03-job-stock.md]. 领星 and 赛狐 help on matching AGL charges to a 货件 (FBA shipment) was searched for and **not found**. Their documented 头程 (first-leg freight) method is a seller-entered cost on a 发货单 (shipping order), spread by weight or volume (`product-profit.md`), not an import of Amazon's AGL lines.
- **Other AGL charges named in a Chinese Q&A.** Per-ticket handling and document fees, storage, continuation-sheet and fumigation fees, value-added services, and extra costs from port congestion or FC overflow [opinion/snippet: AMZ123 Q&A pages, seen only as search summaries, not read].

## Published research

None found on FBA fulfilment or storage charge accuracy, allocation or timing. Vendor "studies" (AMALYTIX's 7% partnered-carrier programme fee ratio, Sellerboard's storage figures) are vendor data, tagged [opinion] above.

## Stable enough for a skill

1. The FBA fulfilment fee is charged per unit **at shipment from the FC**, at the rate in force on the ship date, and posts with the order's shipment transaction. Peak rates follow the ship date, not the order date.
2. Monthly storage is assessed on the daily average volume over a calendar month and collected in the **following** month (the collection days are read at run time). It is an account-level line with no order. Amazon's only per-product split is the **estimated** Storage Fees report.
3. The aged inventory surcharge (formerly long-term storage) is a monthly age-snapshot charge, separate from base storage. The age where it starts, and the assessment day, differ by store and are read at run time. The report that itemises it still has the old "long-term storage" name.
4. The inbound placement fee is chosen when the placement option is confirmed (permanent) and charged **some weeks after the shipment is received** (the lag is read at run time). The quote is in `listPlacementOptions`; no SP-API report itemises the charge.
5. The US low-inventory-level fee is a per-unit surcharge on the fulfilment fee at shipment, using the weekly days-of-supply value. Pan-EU has the analogous "low-inventory cost coverage fee" (DE, FR, IT, ES only).
6. The high-return-rate returns fee is computed per ship month over that month plus two, and charged in a later month. Apparel and shoes pay per return as it happens (US) or a share of the fulfilment fee (EU). The charge month and the share are read at run time.
7. US removal and disposal fees post per unit as each unit is processed (orders created on or after 2026-03-01). Rates are unchanged by that switch.
8. Liquidation pays gross proceeds minus a liquidation fee (US `FBALiquidationEvent`). The EU charges a liquidations referral fee on gross recovery value plus a processing fee per unit (the rate is read at run time).
9. The capacity reservation fee is a bid that performance credits from sales can offset. It is recorded in v0 as `CapacityReservationBillingEvent`. Overage fees apply to on-hand stock over the limit; the overage report (AF only) carries the charge and the limit.
10. Partnered-carrier charges are quoted per shipment in `listTransportationOptions`; cancellation charges apply outside the void window, which each quote dates (`quote.voidableUntil`).
11. MCF fees ride on the MCF order (v0 `OrderFeeList`). The preview names per-unit, per-order, transportation and COD fees.
12. Amazon's measurement governs fees. A dimension-based fee reimbursement must be requested within a window from the charge (read at run time). Remeasurement is a Seller Central widget with per-FNSKU and per-account limits.
13. **No closed list exists** for `breakdownType` (v2024-06-19), `FeeType` (v0, Product Fees), MCF 2026 price `type`, or settlement `amount-description`. Some charges (storage utilization surcharge, low-inventory fee, fuel surcharge) may not have a type of their own and may be inside another line [opinion, AMALYTIX].
14. Economics `fees[]` holds **charged** fees per product and date with size-tier properties, and splits ranges at fee-change dates. `economicsPreview` previews the named fee types up to 120 days ahead. Retention is 30 days.
15. Storage, aged, removal, returns, fee-preview, inbound-performance and reimbursement reports open with **Pricing**. Planning, overage and ledger need **Amazon Fulfillment**. Inbound (placement/transport quotes) and MCF need AF. AWD needs the AWD role.
16. A settlement mixes current sales with charges for past months' storage, placement on receipts from about 45 days earlier, and returns fees for shipments from three months earlier. A settlement's fulfilment-and-storage total is not the cost of the period's sales [seat, derived from 2, 4, 6; stated as a timing fact].
17. Fulfilment fee rates change at announced dates every year and also mid-year (fuel surcharge). Each rate figure has an effective date; the dates are read at run time.
18. AGL is paid either from the Seller Central balance or by wire through Shipper Central. Balance-paid AGL posts as freight and as duties-and-taxes lines, after FC receipt, and "additional fees" can follow later. The currencies and the lags are read at run time. The booking estimate excludes duties, taxes and accessorials.
19. On AGL the seller, or a party it names, is the importer of record. Amazon's broker clears and can advance duty, but the duty is the importer's, and the duty bill can be corrected by PSC or protest after the first charge.
20. Amazon SEND (US) posts freight after booking (the lag is read at run time) and destination duty after delivery, both to the Seller Central account, and issues no carrier invoice. SEND in Australia is paid to the carrier directly.
21. Amazon Freight invoices through its own shipper account on credit.
22. No SP-API operation reads AGL bookings, quotes, Shipper Central statements, debit notes or duty bills.

## What cx must read at run time

| Figure or state | Where it is read |
|---|---|
| Any fee rate (fulfilment by tier/band, storage by season, aged by band, placement, LIL, returns, removal, disposal, liquidation, prep, overage, AWD, MCF) | Seller Central rate pages and rate cards (human); per SKU: Product Fees API, Fee Preview report, `economicsPreview` |
| A SKU's current size tier and Amazon-measured dimensions | Fee Preview `product-size-tier`, dims columns (US tier column); Storage Fees `product_size_tier`; economics `properties` |
| What was charged per product and day | `economics` (role conflict), else Finances lines joined by SKU/order |
| Every charge posted, with its name | `listTransactions` (`breakdownType`, `TimeRangeContext`), v0 events until 2027-08-27, settlement V2 `amount-description` |
| The month a storage line covers | `TimeRangeContext` on the transaction; `month_of_charge` in the Storage Fees report |
| This month's storage estimate per FNSKU × FC | `GET_FBA_STORAGE_FEE_CHARGES_DATA` |
| Aged surcharge charged / next estimate | `…LONGTERM_STORAGE_FEE_CHARGES_DATA` (one-month window); Planning `estimated-ais-*` (AF) |
| LIL status this week, exemption | Planning report (AF); `economicsPreview LOW_INVENTORY_LEVEL_FEE` |
| Placement quote before confirming; option chosen | `listPlacementOptions`, `getInboundPlan`/`getShipment` (AF) |
| Partnered-carrier cost, void window | `listTransportationOptions` `quote` (AF) |
| Removal fee per order line | Removal Order Detail `removal-fee` |
| Unplanned/defect fees per shipment | Inbound Performance `fee-type`, `fee-total` |
| Overage charge and capacity limit | Overage report (AF) |
| Current peak window, fuel surcharge rate, next fee-change date (as read 2026-11-09/10: US changes mid-January; EU 2026-02-01, with the 2027 non-peak rates from 2027-01-15) | Amazon fee-change pages and rate cards; economics fee-range splits |
| Which roles the seller's app actually holds | Amazon's reply (403/Unauthorized) on the first call |
| Balance-paid AGL / SEND freight and duty lines, their names and dates | `listTransactions` (and v0 `ServiceFeeEvent` until 2027-08-27), settlement V2 `amount-description`; Seller Central Transaction View → Service Fees |
| Whether a seller pays AGL from the balance or by wire, and the IOR on each lane | The seller; Seller Central AGL profile (not in the API) |
| AGL booking estimate, statements, debit notes; broker duty bill (税金单) and its corrections | Shipper Central / AGL pages and the broker's emails (human); not in the API |
| Arrival, customs-cleared and delivered dates for an inbound shipment (to date a duty or freight line) | Tracking API `getShipmentTracking` (US, grantless) or the `SHIPMENT_TRACKING_MILESTONE_CHANGED` notification |
| AGL, SEND, GWD rates and promotions | Seller Central booking quote; sell.amazon.com pages (human) |
| Storage collection days (US, as read 2026-11-09 via search snippet: "typically between the 7th and 15th day of the month, in the month following") | Seller Central help *Monthly inventory storage fees* (53921, https://sellercentral.amazon.com/gp/help/external/53921); the posted line's date in `listTransactions` |
| Aged surcharge starting age and assessment day per store (as read 2026-11-10: US 181 days, CA "over 180 days", MX 181 days (its page also says 271), EU 241 days (271 for clothing, footwear, bags, luggage, jewellery and watches), AU 271 days, JP 365 days; AU and JP assess on the 15th) | US: *Amazon FBA (Fulfillment by Amazon)* (https://sell.amazon.com/fulfillment-by-amazon); EU/UK: the *Rate Card Europe Fees* in force (https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf); https://sell.amazon.ca/pricing?lang=en-CA; https://vender.amazon.com.mx/precios; https://sell.amazon.com.au/pricing; https://sell.amazon.co.jp/pricing; the seller's bands in Planning `quantity-to-be-charged-ais-<band>` and `Inventory age snapshot date` (AF) |
| Placement charge lag (US, GC3Q44PBK8BXQW3Z v16 via the listing seat, 2026-10-14: "45 days after your shipment is received") | Seller Central help *FBA inbound placement service fee* (https://sellercentral.amazon.com/help/hub/reference/external/GC3Q44PBK8BXQW3Z); the posted line in `listTransactions` |
| High-return-rate charge month and the EU apparel and shoes share (US: "between the 7th and 15th day of the third subsequent month", GZGEQLTM3RZXUV6T v17, 2026-10-14; EU: "50% of the total fulfilment fee", card of 2026-11-02) | Seller Central help *2026 returns processing fee changes* (https://sellercentral.amazon.com/help/hub/reference/external/GZGEQLTM3RZXUV6T); the *Rate Card Europe Fees* in force (https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf), FAQ Q4 |
| Liquidations referral rate (EU card of 2026-11-02 and CA News a9383e96, read 2026-11-09/10: 15% of gross recovery value) | The *Rate Card Europe Fees* in force (https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf), p. 23; *2026 Updates to Canada referral and Fulfilment by Amazon fees* (https://sellercentral.amazon.ca/seller-forums/discussions/t/a9383e96-87ef-484e-bbe7-cc07584331bb) |
| Partnered-carrier void window (model text, db2936aa: 24 h SPD, 1 h LTL) | `listTransportationOptions` `quote.voidableUntil` (AF) |
| Dimension-based fee reimbursement window (GL7U4JFSDXUTQAJ v14 via the listing seat, 2026-10-14: "within 90 days of the date on which the fee was charged") | Seller Central help *FBA fees reimbursement policy: Weight and dimensions* (https://sellercentral.amazon.com/help/hub/reference/external/GL7U4JFSDXUTQAJ) |
| AGL payment currency and charge lags (US help, snippets 2026-11-10: USD from the balance or CNY by wire; within 48 hours after FC receipt, 7 days after the first FC when split; additional fees 7 days after receipt and again 14 days later) | Seller Central help *Paying for Amazon Global Logistics* (https://sellercentral.amazon.com/gp/help/external/GZJ4B4HXDUEWP4PC); posted dates in `listTransactions` |
| SEND billing currency and freight posting lag (US page, 2026-11-10: USD, "within 24 hours of booking") | *Amazon SEND (Seller Export & Delivery)* (https://sell.amazon.com/programs/seller-export-and-delivery); *Amazon SEND* AU (https://sell.amazon.com.au/amazon-send) |

## What only Seller Central shows

- **Capacity Monitor / Capacity Manager**: limits, estimates, reservation bids and credits. No API returns the limit except as `storage_limit_volume` on an overage charge row (AF). [official absence, command-verified]
- **Inbound placement fee download** (Reports → Payments) and the **returns processing fee breakdown report** ("a report from Amazon Fulfillment reports"): no SP-API report type [command-verified].
- **Remeasure FBA products and confirm fees widget**: no API.
- **Revenue Calculator, Profit Analytics, Fee Change Comparison** (`scenario-modeling?id=2027_ANNUAL_FEE_CHANGE`): Amazon's previews. The API equivalents are `economicsPreview` and Product Fees.
- **Return Insights / FBA Returns page** (return rate vs threshold, "updated three times a week"): no API for the threshold.
- **Transaction view** (shipment-level removal charges per Amazon's post): Finances `listTransactions` carries the same postings.
- **Rate cards and help pages** (US help pages are JavaScript shells to a plain GET; EU rate cards are public PDFs). No API returns a rate table.
- **AWD fee invoices / statements**: no AWD fee field in the AWD API. Whether AWD charges land in Finances is open.
- **Fee disputes / cases** (incorrect fee, inbound defect, unplanned service, 30-day window): no create-case API. The Support API reads cases behind a restricted role.
- **AGL and GWD.** Booking, the Preliminary Estimate, the IOR profile, Shipper Central (wire payers' statements and debit notes), AGL claims, and the GWD fee schedule. No API reaches them. Balance-paid AGL lines alone reach Finances.
- **Broker duty bills (税金单) and their corrections** (email, PSC, protest): with the broker and CBP. No Amazon API.
- **Amazon Freight shipper portal** (Billing & Payments invoices, credit limit): a separate account. No SP-API.

## Facts for human readers only

All dated; never stated by a skill.

- US 2026: FBA fees "+$0.08 per unit sold" on average from 2026-01-15; Low-Price FBA "$0.86 less" on average; placement +~$0.05/unit (minimal splits) [official, G201411300 v47 / GABBX6GZPA8MSZGW v58, via listing seat 2026-10-14]. Peak 2026: about +US$0.32/unit on average [opinion: AMZ123/白鲸出海 2026-09-11]. Inbound defect for ≤16 oz: US$0.04 → US$0.32 from 2026-01-15 [opinion: AMZ123 2025-11-09]. Storage (standard, non-hazmat) about US$0.78/cu ft Jan–Sep and US$2.40 Oct–Dec [opinion: sellerboard 2026-07-14; AMZ123 2026-09-10]. Aged 12–15 months: min US$0.30/unit or US$6.90/cu ft; 15+ months: US$0.35/unit or US$7.90/cu ft [opinion: AMZ123 2025-11-27].
- US 2027 (announced 2026-11-05): fulfilment "+$0.19 per unit" on average, "approximately 0.8% of the average item's selling price" [official]. Band averages per ppc.land: small standard >$50 +$0.70, large standard >$50 +$0.47, small standard $10–$50 +$0.40 [opinion].
- Fuel and logistics surcharge: 3.5% US/CA from 2026-04-17 [official]; EU/UK 1.5% from 2026-04-17, 2% from 2026-11-02 [official, EU rate cards].
- Capacity: performance credit "$0.15 … for every dollar of sales" [official, GAFNWEYTJUV2GBFC v22]; overage "$10 per cubic foot" [opinion, 03-job-stock.md].
- AWD (sell.amazon.com, read 2026-11-09): storage West Coast $0.57 / smart $0.51 / managed $0.46 per cu ft per month; East/South-East/South-Central $0.48 / $0.43 / $0.38; inbound processing $1.40/box ($1.05 West Coast Palletizable); outbound $1.40/box; transportation $1.40/cu ft ($1.26 managed); $0.35/box promotional discount through 2026-12-31 [official]. AWD >12 months at 2.5× from 2027-03-01 [opinion].
- New-seller credits: $400 placement, $100 partnered carrier, $200 AGL [official, sell.amazon.com].
- EU (rate card 2026-11-02, read from the rendered p. 21 on 2026-11-10): monthly storage, Jan–Sep / Oct–Dec. Standard size, non-apparel: UK £0.76 / £1.51 per ft³; DE/FR/IT/ES/NL/PL/BE/IE €27.54 / €52.20 per m³. Standard size, apparel, shoes and bags: £0.62 / £0.82; €19.99 / €29.23. Oversize: £0.55 / £0.87; €21.78 / €34.49 [official]. (The writing seat's "0.62 / 0.82" was the UK apparel column, and AMALYTIX's €27.54 / €52.20 matches the card.) Aged surcharge DE/FR/IT/ES/IE €47.99 (241–270) up to €261.97/m³ or €0.25/unit (455+); UK £1.18 up to £6.14/ft³ or £0.25/unit [official]. Storage utilisation surcharge DE/FR/IT/ES standard size €14.85 (22–28 weeks) to €76.87/m³ (>52 weeks) [official]. Pan-EU low-inventory cost coverage fee: €0.16–0.67 per unit by tier and band [official]. Manual processing €0.15–0.18; label service from €0.38; Pan-EU oversize surcharge from €1.40–€2.98 by tier and country; Sweden flat SEK 20 oversize; liquidation referral 15% [official]. DE removal €0.50 and disposal €0.74 (standard ≤200 g) [opinion: AMALYTIX].
- Liquidation CA: 15% referral plus processing CAD 0.25–1.90 (0–5 kg), plus CAD 0.20/kg over 5 kg, from 2025-11-05 [official: News_Amazon CA a9383e96, read 2026-11-10].
- CA (sell.amazon.ca/pricing, 2026-11-10): envelope from CAD 4.46 for the first 100 g; standard from CAD 5.92; CAD 0.80 less below CAD 14; storage CAD 40 / 77 per m³ standard and CAD 28 / 49 oversize (Jan–Sep / Oct–Dec); dangerous goods +CAD 0.11 per unit [official].
- MX (vender.amazon.com.mx/precios, 2026-11-10, IVA included): envelope 0–0.10 kg MXN 27.00 / 33.00 / 49.00 / 60.00 across the four price bands; storage MXN 0.36 / 0.53 per dm³ standard and 0.19 / 0.43 large; aged MXN 0.30 per dm³ (181–210 days) up to MXN 4.76 per dm³ or 2.32 per unit (366+); removal about MXN 10.70 and disposal about MXN 13.00 per unit [official].
- JP (sell.amazon.co.jp/pricing, 2026-11-10, consumption tax included): 小型 ¥288 (above ¥1,000) / ¥222 (¥1,000 or less); 標準 from ¥318 / ¥252; storage ¥5.676 / ¥10.087 per 1,000 cm³ per month for small/standard non-apparel (Jan–Sep / Oct–Dec); aged minimum ¥20 per unit at 365+ days from 2026-04-15 [official].
- AU (sell.amazon.com.au/pricing, 2026-11-10, excl. GST): storage A$37.00 / 51.80 per m³ standard and A$34.20 / 48.00 oversize; aged A$155 (271–300) up to A$370 per m³ or A$0.12 per unit (366+) [official].
- IN (sell.amazon.in/fees-and-pricing, 2026-11-10, excl. 18% GST): pick & pack ₹17 for standard items up to 1 kg, +₹5/kg to 5 kg; heavy & bulky ₹26; storage ₹50 per ft³ per month; FC removal ₹10 (standard, standard shipping) [official].
- Returns processing US apparel/shoes $1.65–$3.89+ per unit [opinion; unverified].
- AGL (read 2026-11-10):
  - "8% discount on base ocean freight rates for 60 days after onboarding" for new FBA sellers [official, sell.amazon.com AGL page].
  - Amazon Managed Placement caps: "no more than 2,000 cartons … per 40-foot container, and no more than 1,000 cartons … per 20-foot container" [official, same page].
  - Liability, from the AGL Freight Service Terms of 2026-01-14 [official]:
    - US ocean bill of lading "500 USD per shipment" unless a higher value is agreed.
    - Warehouseman or transloading "$0.25 per pound".
    - Cumulative "80,000 USD in any 12-month period".
  - AGL peak seasons in the same terms [official]: ocean "June 1 to October 31 and one month prior to the official Chinese New Year"; air "September 1 to November 30".
- GWD: 30 days of free storage for shipments received 2026-07-01 to 2026-12-31; storage "up to 45% lower than US Amazon Warehousing and Distribution" [official, News 2026-07-07]. Reported per-carton and export-declaration fees [opinion, vendor blogs; not on an Amazon page read].

## Pages read

| Title | URL | Date read | Tag |
|---|---|---|---|
| FBA Reports (report type values) | https://developer-docs.amazon/sp-api/docs/report-type-values-fba.md (updatedAt 2026-10-13) | 2026-11-09 | [official] [command-verified] |
| Settlement Reports | https://developer-docs.amazon/sp-api/docs/report-type-values-settlement.md (updatedAt 2026-10-14) | 2026-11-09 | [official] |
| Report Type Values | https://developer-docs.amazon/sp-api/docs/report-type-values.md (updatedAt 2026-09-10) | 2026-11-09 | [official] |
| Finances API | https://developer-docs.amazon/sp-api/docs/finances-api.md (updatedAt 2026-09-09) | 2026-11-09 | [official] |
| Get the latest transactions | https://developer-docs.amazon/sp-api/docs/get-latest-transactions.md | 2026-11-09 | [official] |
| Determine payment transactions | https://developer-docs.amazon/sp-api/docs/determine-payment-transactions.md (updatedAt 2026-09-09) | 2026-11-09 | [official] |
| Finances transaction types / v2024-06-19 use case guide | https://developer-docs.amazon/sp-api/docs/finances-api-transaction-types.md, …/finances-api-v2024-06-19-use-case-guide.md | 2026-11-09: **Page Not Found** | [official, absent] |
| Product Fees API | https://developer-docs.amazon/sp-api/docs/product-fees-api.md (updatedAt 2026-09-09) | 2026-11-09 | [official] |
| SP-API Release Notes | https://developer-docs.amazon/sp-api/docs/sp-api-release-notes.md (updatedAt 2026-11-04) | 2026-11-09 | [official] [command-verified] |
| SP-API Deprecation Schedule | https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md (updatedAt 2026-09-09) | 2026-11-09 | [official] |
| Role Mappings for SP-API Operations / Types | local web01/role-mappings.md, role-mappings-for-types.md (updatedAt 2026-10-28) | 2026-11-09 | [official] [command-verified] |
| Models: financesV0, finances_2024-06-19, fulfillmentInbound_2024-03-20, fulfillmentInboundV0, fulfillmentOutbound_2020-07-01 / _2026-07-04, awd_2024-05-09, productFeesV0, reports_2021-06-30, dataKiosk_2023-11-15; schemas analytics_economics_2024_03_15.graphql, FeePromotionNotification.json | local clone db2936aa | 2026-11-09 | [official] [command-verified] |
| Rate Card Europe Fees, effective 2 November 2026 | https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf | 2026-11-09 | [official] [command-verified] |
| Rate Card Europe Fees, effective 1 July 2026 | https://m.media-amazon.com/images/G/02/sell/images/260630-FBA-Rate-Card-EN1.pdf | 2026-11-09 | [official] [command-verified] |
| Rate Card Europe Fees, effective 1 February 2026 | https://m.media-amazon.com/images/G/02/sell/images/260114-FBA-Rate-Card-EN.pdf | 2026-11-09 | [official] [command-verified] |
| Update to US Referral and Fulfillment by Amazon fees for 2027 (2026-11-05) | https://sellingpartners.aboutamazon.com/update-to-us-referral-and-fulfillment-by-amazon-fees-for-2027 | 2026-11-09 | [official] |
| 2027 Amazon FBA Rate Increases (forum copy of Amazon's news article) | https://sellersasksellers.com/t/fba-rate-increases/7699 | 2026-11-09 | [official, relayed] |
| Amazon FBA (Fulfillment by Amazon) | https://sell.amazon.com/fulfillment-by-amazon | 2026-11-09 (first ~40k chars verbatim) | [official] |
| A guide to Amazon FBA fees (2026-07-24) | https://sell.amazon.com/blog/fba-fees-guide | 2026-11-09 (partial) | [official] |
| Sell on Amazon pricing | https://sell.amazon.com/pricing | 2026-11-09 (no FBA content) | [official] |
| Amazon Warehousing and Distribution | https://sell.amazon.com/programs/warehousing | 2026-11-09 | [official] |
| Amazon announces new streamlined FBA capacity management system (2023-01-17) | https://sell.amazon.com/blog/announcements/fba-capacity | 2026-11-09 | [official] |
| Ask Amazon: Simplified FBA capacity limits Q&A (2023-03-14) | https://sellercentral.amazon.com/seller-forums/discussions/t/3c9cef3c-530b-4846-a3b3-a855ed62f241 | 2026-11-09 (partial) | [official] |
| FBA removal and disposal fees to be charged as units are processed (News_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/2f4edad8-31d4-443b-8b22-12776c4f685a | 2026-11-09 | [official] |
| Supply Chain Portal fees overview for MCF | https://supplychain.amazon.com/pricing/fees-policy | 2026-11-09 | [official] |
| Unplanned services (help 201000230) | https://sellercentral.amazon.com/gp/help/external/201000230 | 2026-11-09: JS shell, no text | [official, unreachable] |
| Monthly inventory storage fees (help 53921) | https://sellercentral.amazon.com/gp/help/external/53921 | 2026-11-09: JS shell; cited via search snippet | [official, snippet] |
| MWS Finances Fee Types / Datatypes | https://docs.developer.amazonservices.com/en_ES/finances/Finances_FeeTypes.html | 2026-11-09: **DNS failure** (host gone) | [official, unreachable] |
| Listing playbook research (fee pages read 2026-10-14: G201074400, GC3Q44PBK8BXQW3Z, GV43F6S76Y9DHYRH, GABBX6GZPA8MSZGW, G201411300, GG5KW835AHDJCH8W, G37G73BJXHF75ACH, GL7U4JFSDXUTQAJ, G6WAEPTECPT2JUH3, GAFNWEYTJUV2GBFC, G200680700, GQNVDV46U9JQ25HY, GZGEQLTM3RZXUV6T, G3RZC8DVQCDTCQ3B) | `cx-listing-playbook` origin/main research/angles/inventory-and-fulfillment.md, returns.md | 2026-11-09 (re-read) | [official, reused] |
| Survey notes 03-job-stock.md, 04-job-money.md, report-full.md | the sp-api-plugins seat's survey of SP-API for brief 306 (not published) | 2026-11-09 | (survey; re-checked where load-bearing) |
| ppc.land: per-unit removal billing (Luís Rijo, 2026-02-01) | https://ppc.land/amazon-changes-how-sellers-pay-for-fba-removals-with-per-unit-billing/ | 2026-11-09 | [opinion] |
| ppc.land: $0.19 rise from 2027-01-15 (2026-11-06) | https://ppc.land/amazon-sellers-face-average-0-19-fba-fee-rise-from-january-15-2027/ | 2026-11-09 (first 40% verbatim) | [opinion] |
| Nova Analytics: 2027 FBA fee changes (2026-11-06) | https://novadata.io/resources/news/amazon-2027-fba-fee-changes-us | 2026-11-09 | [opinion] |
| EcomCrew: 2027 fee math (2026-11-05) | https://www.ecomcrew.com/amazons-2027-fee-math-doesnt-stop-at-19-cents/ | 2026-11-09 | [opinion] |
| EcommerceBytes 2026-01-30 | https://www.ecommercebytes.com/2026/01/30/amazon-changes-how-it-charges-fba-removal-and-disposal-fees/ | 2026-11-09: closure notice only | [opinion, unreachable] |
| Seller Forums CA disposal-fee thread | https://sellercentral.amazon.ca/seller-forums/discussions/t/ef3a5062-d4ca-4487-b159-4687fb032d18 | 2026-11-09 (off-topic) | [opinion] |
| sellerboard: amortize Amazon fees (2026-05) | https://blog.sellerboard.com/2026/05/18/new-in-sellerboard-amortize-amazon-fees-for-a-clearer-view-of-your-real-profits/ | 2026-11-09 | [opinion] |
| sellerboard: FBA storage fees per SKU (2026-07) | https://blog.sellerboard.com/2026/07/14/fba-storage-fees-the-silent-margin-killer-and-how-to-model-them-per-sku/ | 2026-11-09 | [opinion] |
| Seller Assistant: FBA inbound placement service fee (2026-10-09) | https://help.sellerassistant.app/en/articles/9154405-fba-inbound-placement-service-fee | 2026-11-09 | [opinion] |
| scanpower placement fee update | https://scanpower.com/inbound-inventory-placement-fees-update/ | 2026-11-09: 404 | — |
| amazon-settlement-parser (GitHub) | https://github.com/xieyi138-star/amazon-settlement-parser | 2026-11-09 (data file partial) | [opinion] |
| Webgility: settlement fee groups and names (2025-10-26) | https://helpcenter.webgility.com/en/articles/6257546-amazon-settlement-report-fee-groups-and-fee-names | 2026-11-09 | [opinion] |
| MyProfit: settlement report explained (2026-10-03) | https://www.myprofit.co/guides/amazon-settlement-report-explained | 2026-11-09 | [opinion] |
| Intentwise: settlement V1→V2 mapping | https://help.intentwise.com/amazon-settlement-report-v1-to-v2-mapping-guide | 2026-11-09 | [opinion] |
| Seller Forums: amount-description help thread | https://sellercentral.amazon.com/seller-forums/discussions/t/328bfeed-9007-478e-bea8-20b370db2cde | 2026-11-09 (user posts) | [opinion] |
| AMALYTIX: Amazon seller fees 2026 (2026-10-20) | https://www.amalytix.com/en/knowledge/controlling/amazon-seller-fees/ | 2026-11-09 | [opinion] |
| AMZ123 articles (5KOnjjlQ 2026-04-30; BA1qW9jV 2026-09-10; 2kIZ4A7n 2025-11-27; 3PEcbbvv 2025-11-09; ask/kpCwMYnb 2024-12-09; ask/6VGZb5c9 2024-12-19; ask/7BnRHjCk 2025-05-13; b/ygSxkvSd 2025-09-22) | https://www.amz123.com/… | 2026-11-09 | [opinion] |
| 白鲸出海 reprint of 双木@AMZ123 (2026-09-11) | https://www.baijing.cn/article/56666 | 2026-11-09 | [opinion] |
| 优麦云 SellerSpace: 入库配置费报告; 费用分摊 | https://www.sellerspace.com/help/storage-configuration-fee-use-guide; …/method-of-the-cost-sharing-use-guide | 2026-11-09 | [opinion] |
| sell.amazon.ca pricing (FBA section) | https://sell.amazon.ca/pricing?lang=en-CA | 2026-11-10 (verifier) | [official] |
| 2026 Updates to Canada referral and Fulfilment by Amazon fees (News_Amazon) | https://sellercentral.amazon.ca/seller-forums/discussions/t/a9383e96-87ef-484e-bbe7-cc07584331bb | 2026-11-10 (verifier) | [official] |
| vender.amazon.com.mx precios (FBA section) | https://vender.amazon.com.mx/precios | 2026-11-10 (verifier) | [official] |
| sell.amazon.co.jp pricing (FBA section) | https://sell.amazon.co.jp/pricing | 2026-11-10 (verifier) | [official] |
| 2026亚马逊日本站销售佣金与亚马逊物流费用变更 (2026 Amazon Japan referral fee and FBA fee changes, 2025-12-02) | https://gs.amazon.cn/news/news-notices-251202 | 2026-11-10 (verifier) | [official] |
| sell.amazon.com.au pricing (FBA section) | https://sell.amazon.com.au/pricing | 2026-11-10 (verifier) | [official] |
| sell.amazon.in fees and pricing (FBA section) | https://sell.amazon.in/fees-and-pricing | 2026-11-10 (verifier) | [official] |
| Correction: Data Kiosk role requirements (page timestamp 2024-07-02) | https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements | 2026-11-10 (verifier) | [official] |
| Data Kiosk API (updatedAt 2026-10-20) | https://developer-docs.amazon/sp-api/docs/data-kiosk-api.md | 2026-11-10 (verifier) | [official] |
| listTransactions reference | https://developer-docs.amazon/sp-api/reference/listtransactions.md | 2026-11-10 (verifier) | [official] |
| GitHub commits db2936aa (2026-10-29) and df7c6298 (2026-10-28), amzn/selling-partner-api-models | https://api.github.com/repos/amzn/selling-partner-api-models/commits/db2936aa19f4b48185173c385c51ab115166f221 | 2026-11-10 (verifier) | [official] [command-verified] |
| Web search snippets (prep end, inbound defect, capacity 2026, returns, liquidation, CA/MX, JP, Chinese ERPs) | (search result pages) | 2026-11-09 | [opinion, snippet] |
| Amazon Global Logistics (program page) | https://sell.amazon.com/programs/amazon-global-logistics | 2026-11-10 (curl, full text) | [official] |
| Amazon Global Logistics (UK program page) | https://sell.amazon.co.uk/amazon-global-logistics | 2026-11-10 (curl, grep only) | [official] |
| Amazon Global Logistics Freight Service Terms (dated 2026-01-14) | https://supplychain.amazon.com/legal/service-terms/global-logistics-freight | 2026-11-10 (curl, full text) | [official] |
| Amazon Customs & Trade | https://spcentral.amazon.com/nlp/customs-and-trade | 2026-11-10 | [official] |
| 物流仓储：跨境物流 – 进口清关准备 (Amazon Global Selling course PDF, © 2026) | https://m.media-amazon.com/images/G/28/AS/AGS/SU/CN_GS_CB_Logistics_Basics_Customs_Clearance.pdf | 2026-11-10 | [official] [command-verified: PDFKit text] |
| Paying for Amazon Global Logistics (GZJ4B4HXDUEWP4PC) | https://sellercentral.amazon.com/gp/help/external/GZJ4B4HXDUEWP4PC | 2026-11-10: JS shell; cited via search snippets | [official, snippet] |
| Amazon Global Logistics (202187670; EU G202187670), Booking transportation with AGL (G5NQMLZ7E6UBPVNE), AGL importer setup (ASFW4BD897LNTNN), Claims and reimbursements through AGL (GR384ESWC8HH8667) | https://sellercentral.amazon.com/gp/help/external/… | 2026-11-10: JS shells; GR384ESWC8HH8667 cited via snippet only | [official, unreachable / snippet] |
| Amazon SEND (Seller Export & Delivery), EN and ZH | https://sell.amazon.com/programs/seller-export-and-delivery ; https://sell.amazon.com/zh/programs/seller-export-and-delivery | 2026-11-10 | [official] |
| Amazon SEND (Australia) | https://sell.amazon.com.au/amazon-send | 2026-11-10 | [official] |
| Introducing Global Warehousing & Distribution (News, 2026-04-09) | https://sellercentral.amazon.com/seller-forums/discussions/t/91f2bda1-ff49-456e-9319-9b61058c7c03 | 2026-11-10 | [official] |
| Send to GWD and get 30 days of free storage (News, 2026-07-07) | https://sellercentral.amazon.com/seller-forums/discussions/t/20c69db3-7a11-459a-b265-6d7e0eb434fa | 2026-11-10 | [official] |
| Amazon offers one inbound shipment to reach eight countries (FreightWaves, 2026-09-27) | https://www.freightwaves.com/news/amazon-global-warehousing-distribution-eight-countries | 2026-11-10 | [opinion, relaying Amazon] |
| How to use Amazon Freight's online tools (2026-02-09) | https://freight.amazon.com/newsroom/shipper-tips/26-use-af-portal | 2026-11-10 | [official] |
| Amazon Freight terms all shippers should know | https://freight.amazon.com/newsroom/2024-amazon-freight-terms | 2026-11-10 | [official] |
| Streamlined credit approval (Amazon Freight UK, 2024-06-25) | https://freight.amazon.co.uk/newsroom/streamline-credit-limit-approval | 2026-11-10 | [official] |
| Amazon Freight terms | https://freight.amazon.com/terms | 2026-11-10: sign-in wall | [official, unreachable] |
| Inbound transportation fee Report (EU forum, Amazon reply; thread 2023-02-02) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2583156f-b480-44d3-8271-bbeb752c0df8 | 2026-11-10 | [official, forum reply] |
| Ask Amazon: Amazon Global Logistics (EU forum event) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/e9d0ff76-865f-462f-970f-c848f0b6998d | 2026-11-10 (seller questions only in the static text) | [opinion] |
| Tracking API v2026-01-30 model; financesInvoices_2026-06-25 model; finances_2024-06-19 `RelatedIdentifier`; financesV0 `ServiceFeeEvent`; analytics_economics `FbaPerUnitCost`; ShipmentTrackingMilestoneChangedNotification schema | local clone db2936aa | 2026-11-10 | [official] [command-verified] |
| GitHub commit db2936aa diff (`AMAZON_FBA_FROM_ORIGIN` removal) | https://api.github.com/repos/amzn/selling-partner-api-models/commits/db2936aa19f4b48185173c385c51ab115166f221 | 2026-11-10 | [official] [command-verified] |
| Threecolts: How Amazon Global Logistics works (2025-11-24) | https://www.threecolts.com/blog/?p=9447 | 2026-11-10 | [opinion] |
| Inventory Hero: IEEPA CAPE guide (Andrew Erickson, 2026-05-27) | https://www.inventoryhero.ai/blog/how-to-get-trump-tariff-refund | 2026-11-10 | [opinion] |
| Synder: FBA International Freight Shipping Charge / …Adjustments / …Duties and Taxes Charge | https://synder.com/fees-amazon/fba-international-freight-shipping-charge/ (and two siblings) | 2026-11-10 | [opinion] |
| MyRealProfit: Amazon fees glossary | https://intercom.help/myrealprofit/en/articles/14116503-amazon-fees-glossary-every-fee-type-explained | 2026-11-10 | [opinion] |
| AMALYTIX: Amazon seller fees 2026 (re-read for AGL lines) | https://www.amalytix.com/en/knowledge/controlling/amazon-seller-fees/ | 2026-11-10 | [opinion] |
| Sellers Ask Sellers: Reconciling FBA inbound shipment fee (2026-03-24) | https://sellersasksellers.com/t/reconciling-fba-inbound-shipment-fee-on-2025-transaction-report/7053 | 2026-11-10 | [opinion] |
| My Amazon Guy: AGL tips (Steven Pope, 2026-03-16) | https://myamazonguy.com/logistics/amazon-global-logistics-tips/ | 2026-11-10 (via fetch tool) | [opinion] |
| manuals.plus copies of Amazon AGL onboarding guides | https://manuals.plus/amazon/using-amazon-global-logistics-in-seller-central-guide (and others) | 2026-11-10: bot check; snippets only | [opinion, snippet] |
| Web search snippets (AGL payment, AGL claims, AGL in 领星/赛狐/积加, AMZ123 AGL Q&A, Amazon Freight billing, GWD fees) | (search result pages) | 2026-11-10 | [opinion, snippet] |

## Open questions

For a first run on a real account:
1. Which `breakdownType` values `listTransactions` returns for: storage, aged surcharge, storage utilization surcharge, placement, LIL (separate, or inside the fulfilment fee), fuel surcharge (separate, or inside), returns processing (HRR and apparel), removal/disposal per unit, liquidation, capacity reservation and credits, overage, inbound defect, unplanned service, manual processing, partnered carrier, AWD, MCF. Also which `transactionType` / `description` each carries, and whether `TimeRangeContext` is present on storage lines.
2. The same for v0 (`ServiceFeeEvent.FeeReason`/`FeeType`, `FeeDescription`; whether storage and placement come with `SellerSKU`/`FnSKU`/`ASIN`) and for settlement V2 `amount-description`.
3. Whether account-level storage and placement lines carry a SKU or ASIN in any record, or only at account level.
4. Whether AWD charges post in Finances / settlement at all, and under what name; whether a separate AWD invoice exists.
5. How the capacity reservation fee and performance credits post (gross and credit, or net) and when.
6. How the 2027 LIL rule (shipments in the four weeks after) is posted: at shipment with a later adjustment, or deferred.
7. (Settled from Amazon's documents on 2026-11-10: `listTransactions` does not take a `SETTLEMENT_ID` filter. It was added to the model on 2026-10-28 and rolled back on 2026-10-29, and the live reference page lists only `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`. A live call only confirms this.)
8. Which role the economics dataset accepts on this seller's app (Brand Analytics vs Selling Partner Insights), and whether the 2026-09-30 removal/disposal/fuel additions show in `fees[].feeTypeName`.
9. Whether the Storage Fees report's `estimated_monthly_storage_fee` sums to the posted storage line for the same month (estimate vs charge gap).
10. Whether the EU account still sees prep fees after 2026-07-01 (rate card vs vendor conflict).
11. Rate structures for JP, AU, IN, MX and CA are now read (section P). Still open: the 2027 notices for those stores; whether MX's aged storage starts at 181 or 271 days (its page says both); and how IN's weight-handling, pick-and-pack and storage fees are named on the money lines.
12. Whether a fee correction after a remeasurement posts as a reversal of the original fee lines or as one adjustment (`NonSubscriptionFeeAdj`, `INCORRECT_FEES_*`, `RE_EVALUATION`?), and with what reference to the orders.
13. The `transactionType`, `breakdownType` and `description` that `listTransactions` gives balance-paid AGL freight, AGL duties and taxes, AGL "additional fees", SEND freight and SEND duty. Also whether settlement V2 shows "FBA International Freight Shipping Charge" / "…Duties and Taxes Charge" or the codes `FBAInternationalInboundFreightFee` / `…TaxAndDuty`, and whether `GlobalInboundTransportationFreight` / `…Duty` appear.
14. Whether a US duty correction on an AGL entry (broker re-issue, PSC, protest, IEEPA refund) ever posts back to the Seller Central balance, or is settled only between the IOR, Amazon Customs & Trade and CBP. And whether a duty advanced by the broker for a wire-paying seller is billed in Shipper Central.
15. Whether AGL lines carry the FBA shipment ID (`relatedIdentifiers` `SHIPMENT_ID`, or settlement `order-id`) the way partnered-carrier lines have since 2025-06-01, or only the AGL booking reference, or nothing.
16. What `AMAZON_FBA_FROM_ORIGIN` ("FBA from origin") names, and whether GWD storage, processing, export and transport charges post to the seller balance and under which names.
17. In which currency balance-paid AGL lines post on EU, UK and JP accounts (EUR/GBP/JPY, or USD as on the US page), and whether VAT or JCT on AGL services is shown on the line or on a separate invoice.
18. Whether an AGL shipment booked with minimal splits also produces the ~45-day inbound placement line (section C) on top of the AGL lines, and whether Amazon Managed Placement shows any placement line at all.

## Positions

- **P-ful-1.** The FBA fulfilment fee is charged per unit when the unit leaves the fulfilment centre, at the rate in force on the ship date, so peak rates apply by ship date. Sources: GABBX6GZPA8MSZGW v58 ("calculated and charged when shipments leave fulfillment centers"); EU rate card 2026-11-02 (peak window).
- **P-ful-2.** Amazon's own measurement sets every size-tier-based fee (fulfilment, storage, aged, removal, disposal, MCF, placement). A dimension-based fee reimbursement must be requested within 90 days of the charge, and remeasurement happens only through Seller Central, with per-FNSKU and per-account limits. Sources: GG5KW835AHDJCH8W v7; GL7U4JFSDXUTQAJ v14; G6WAEPTECPT2JUH3 v11; EU rate card FAQ Q2; ops.tsv (no API). Read at run time: the claim window from Seller Central help *FBA fees reimbursement policy: Weight and dimensions* (GL7U4JFSDXUTQAJ, https://sellercentral.amazon.com/help/hub/reference/external/GL7U4JFSDXUTQAJ, on the seller's own Seller Central), and the date a fee was charged from `listTransactions` (`postedDate`).
- **P-ful-3.** Monthly storage is assessed on the daily average volume over a calendar month and collected in the following month. It is an account-level charge with no order. Amazon's per-product view of it is the estimated `GET_FBA_STORAGE_FEE_CHARGES_DATA` (Pricing or AF). Sources: help 53921 (snippet); EU rate card p. 21; FBA Reports page.
- **P-ful-4.** The storage utilization surcharge is part of the monthly storage fee, driven by the ratio of average daily volume stored to average daily volume shipped over 13 weeks, above 22 weeks, outside apparel/eyewear/shoes/bags. In the US it ends on 2027-02-01. Sources: EU rate card pp. 4, 21; Supply Chain Portal fees overview; 2027 announcement. Read at run time: the ratio threshold, the window and the exempt categories from the seller's store's page (EU/UK: the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf); US: *Supply Chain Portal fees overview for MCF*, https://supplychain.amazon.com/pricing/fees-policy), and the seller's own ratio and surcharge rate per ASIN from `GET_FBA_STORAGE_FEE_CHARGES_DATA` (`storage_utilization_ratio`, `utilization_surcharge_rate`).
- **P-ful-5.** The aged inventory surcharge (formerly long-term storage) is a monthly charge on top of storage, by age band. The starting age differs by store and changes by announcement. As read 2026-11-10: US 181 days; CA "over 180 days"; MX 181 days, though its page also says 271; EU 241 days, with clothing, footwear, bags, luggage, jewellery and watches exempt from the 241–270 band; AU 271 days; JP 365 days. AU and JP state the assessment on the 15th of the month. The report carrying it still has the "long-term storage" name, needs a one-month request window, and opens with Pricing. In the US it folds into a single age-based storage rate from 2027-02-01. Sources: sell.amazon.com/fulfillment-by-amazon; EU rate card p. 21; sell.amazon.ca/pricing; vender.amazon.com.mx/precios; sell.amazon.com.au/pricing; sell.amazon.co.jp/pricing; gs.amazon.cn news-notices-251202; FBA Reports page; 2027 announcement. Read at run time: the starting age, the bands and the assessment day from the seller's store's page (US: *Amazon FBA (Fulfillment by Amazon)*, https://sell.amazon.com/fulfillment-by-amazon; EU/UK: the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf); CA: https://sell.amazon.ca/pricing?lang=en-CA; MX: https://vender.amazon.com.mx/precios; AU: https://sell.amazon.com.au/pricing; JP: https://sell.amazon.co.jp/pricing), the bands applied to the seller's stock from `GET_FBA_INVENTORY_PLANNING_DATA` (`quantity-to-be-charged-ais-<band>`, `Inventory age snapshot date`; AF), and the tier charged from `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` (`surcharge-age-tier`, `snapshot-date`).
- **P-ful-6.** The inbound placement fee is fixed when a placement option is confirmed (irreversible) and charged about 45 days after the shipment is received. The quote is readable in `listPlacementOptions` (AF). No SP-API report itemises the charge. AWD-replenished stock carries no separate placement fee. Sources: GC3Q44PBK8BXQW3Z v16; fulfillmentInbound_2024-03-20.json; report-type-values pages; sell.amazon.com/programs/warehousing. Read at run time: the charge timing from Seller Central help *FBA inbound placement service fee* (GC3Q44PBK8BXQW3Z, https://sellercentral.amazon.com/help/hub/reference/external/GC3Q44PBK8BXQW3Z; US), the fee before confirmation from `listPlacementOptions` (`fees`, `discounts`), and the posted line from `listTransactions`.
- **P-ful-7.** The US low-inventory-level fee is a per-unit surcharge within the fulfilment fee family, applied at shipment from the weekly FNSKU-level days of supply (both 30- and 90-day below 28, to 2027-01-31; actual shipments four weeks either side from 2027-02-01), with listed exemptions and automatic reimbursement when Amazon delayed the inbound. Pan-EU has the analogous low-inventory cost coverage fee for DE/FR/IT/ES. Sources: GV43F6S76Y9DHYRH v29; 2027 announcement; EU rate card p. 10; economics schema. Read at run time: the days-of-supply threshold, the windows and the exemptions from Seller Central help *Low-inventory-level fee* (GV43F6S76Y9DHYRH, https://sellercentral.amazon.com/help/hub/reference/external/GV43F6S76Y9DHYRH; US) or the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf) (Pan-EU), the seller's own days of supply, exemption and weekly fee flag from `GET_FBA_INVENTORY_PLANNING_DATA` (AF), and the fee ahead from Data Kiosk `createQuery` on `economicsPreview` (`LOW_INVENTORY_LEVEL_FEE`).
- **P-ful-8.** The fuel and logistics surcharge is a percentage of the FBA fulfilment fee, not of the price. It started 2026-04-17 (US/CA and the EU/UK stores at different percentages) and rose in the EU/UK on 2026-11-02. Its percentage is read from Amazon's page at run time. Sources: GABBX6GZPA8MSZGW v58; EU rate cards 2026-07-01 and 2026-11-02; 2027 announcement ("remains unchanged"). Read at run time: the percentage for the seller's store from Seller Central help *2026 US FBA fulfillment fee changes* (GABBX6GZPA8MSZGW, https://sellercentral.amazon.com/help/hub/reference/external/GABBX6GZPA8MSZGW; US and CA) or the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf) (EU/UK).
- **P-ful-9.** The high-return-rate returns fee is computed per ship month over that month and the next two, on returned units above the product's category threshold, and charged in the third subsequent month (US: 7th–15th). Apparel and shoes are charged per return as it occurs (US) or at 50% of the fulfilment fee (EU). Sources: GZGEQLTM3RZXUV6T v17; EU rate card FAQ Q4. Read at run time: the thresholds, the charge month and days, and the apparel and shoes rate from Seller Central help *2026 returns processing fee changes* (GZGEQLTM3RZXUV6T, https://sellercentral.amazon.com/help/hub/reference/external/GZGEQLTM3RZXUV6T; US) or the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf) (FAQ Q4; EU/UK), and the fee ahead per SKU from Data Kiosk `createQuery` on `economicsPreview` (`HIGH_RETURN_RATE_FEE`, `RETURN_PROCESSING_FEE`).
- **P-ful-10.** US removal and disposal fees post per unit as each unit is removed or disposed of, for orders created on or after 2026-03-01, at unchanged rates. The Removal Order Detail report carries `removal-fee` per line. Sources: News_Amazon 2f4edad8…; FBA Reports page.
- **P-ful-11.** Liquidation is money in and money out on one event: in the US, `FBALiquidationEvent` gives gross proceeds and the liquidation fee, and the seller receives the difference. In the EU and in CA (from 2025-11-05), a 15% liquidations referral fee on gross recovery value plus a per-unit processing fee. Sources: financesV0.json; EU rate card p. 23; News_Amazon CA a9383e96. Read at run time: the liquidations referral rate and processing fee from the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf) (p. 23; EU/UK) or *2026 Updates to Canada referral and Fulfilment by Amazon fees* (https://sellercentral.amazon.ca/seller-forums/discussions/t/a9383e96-87ef-484e-bbe7-cc07584331bb; CA), and the fee taken on a US liquidation from `listFinancialEvents` (`FBALiquidationEvent.LiquidationFeeAmount`).
- **P-ful-12.** The capacity reservation fee is a seller-set bid, granted highest bid first, that performance credits earned on sales from the extra capacity can offset up to 100%. It is recorded in Finances v0 as `CapacityReservationBillingEvent`. Overage fees apply to on-hand stock (not open shipments) above the highest limit given for the period, and are itemised only in the AF-only overage report. Sources: GAFNWEYTJUV2GBFC v22; sell.amazon.com/blog/announcements/fba-capacity; Ask Amazon Q&A 2023-03-14; financesV0.json; FBA Reports page.
- **P-ful-13.** Partnered-carrier inbound transport is quoted per shipment in `listTransportationOptions` (AF). Cancelling outside the void window (24 h SPD, 1 h LTL) can incur charges, and post-confirmation content changes carry a cost preview. Sources: fulfillmentInbound_2024-03-20.json; Deprecation Schedule (v0 transport removed 2025-01-21). Read at run time: the void deadline of each quote from `listTransportationOptions` (`quote.voidableUntil`).
- **P-ful-14.** MCF fees ride on the MCF order (v0 `OrderFeeList`). The 2020-07-01 preview names per-unit, per-order, transportation and COD fees; the 2026-07-04 preview uses an open price `type`. Sources: financesV0.json; fulfillmentOutbound_2020-07-01.json; fulfillmentOutbound_2026-07-04.json.
- **P-ful-15.** Amazon publishes no closed list of the names fulfilment and storage charges carry: `breakdownType`, v0 `FeeType`, Product Fees `FeeType` and settlement `amount-description` are open strings, and new names appear. Some surcharges may have no type of their own. Sources: Get the latest transactions; financesV0.json; productFeesV0.json; Settlement Reports page; practitioner: AMALYTIX (no own type for SUS/LIL/fuel), amazon-settlement-parser README.
- **P-ful-16.** In `listTransactions`, `TimeRangeContext` (`startTime`, `endTime`) is the field that can date a charge to the period it covers, as distinct from `postedDate`. Source: finances_2024-06-19.json. (Which charges carry it: open question 1.)
- **P-ful-17.** In Amazon's v0 model, `ServiceFeeEvent` carries `AmazonOrderId`, `SellerSKU`, `FnSKU` and `ASIN`, and `CapacityReservationBillingEvent` carries none of them. Whether storage, placement, capacity or overage charges come back on an order-scoped read (`listFinancialEventsByOrderId`, order-level transactions) is not yet seen on a live account (open question 3); date-range and group-scoped reads and settlements carry account-level charges. Sources: financesV0.json `ServiceFeeEvent` and `CapacityReservationBillingEvent` definitions [official, command-verified 2026-11-10].
- **P-ful-18.** Data Kiosk `economics` holds charged fees per product and date with the properties (such as size tier) that set them, splits ranges at Amazon fee-change dates, and keeps results 30 days. `economicsPreview` previews the named fulfilment, storage, aged, LIL, placement, returns and Pan-EU oversize fees up to 120 days ahead. The role it needs is in conflict between Amazon's pages: Role Mappings and the Data Kiosk API page give Brand Analytics, while the changelog *Correction: Data Kiosk role requirements* (2024-07-02) says "The Economics dataset requires the Selling Partner Insights role". Sources: analytics_economics_2024_03_15.graphql; Role Mappings (2026-10-28); Data Kiosk API page (2026-10-20); https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements.
- **P-ful-19.** Product Fees estimates per-sale fees (referral, closing, FBA fulfilment) for a price. SKU estimates use Amazon's measured dimensions once stock is received; ASIN estimates use catalog size. It does not estimate storage, placement, removal or returns fees, and is "not guaranteed". Sources: productFeesV0.json; Product Fees API page; inventory-and-fulfillment.md G5–G6.
- **P-ful-20.** Roles: the storage, aged, fee-preview, inbound-performance, removal, returns and reimbursement reports open with Pricing (or AF). The planning and overage reports, Fulfillment Inbound and MCF need Amazon Fulfillment. AWD needs the AWD role. Settlement V2 and Finances v2024-06-19 need Finance and Accounting. Sources: Role Mappings for SP-API Operations and Types (2026-10-28); FBA Reports page.
- **P-ful-21.** A settlement or period total of fulfilment and storage charges includes charges for earlier periods: storage for the previous month, placement for receipts from about 45 days earlier, HRR returns fees for shipments three months earlier, and per-unit removal charges spread over processing. It is not the fulfilment cost of that period's sales. How a seller assigns these to periods or products (by posting date, by covered period, amortised, or by volume, units or sales share) is the seller's choice. Sources: P-ful-3, -6, -9, -10 sources; practitioners: sellerboard amortisation, SellerSpace per-ASIN booking, Lingxing custom allocation.
- **P-ful-22.** Fee rates and their effective dates change on announced dates (US mid-January, EU early in the year) and also mid-year (fuel surcharge 2026-04-17, EU rise 2026-11-02, peak 2026-10-15 to 2027-01-14). A rate figure is meaningful only with its effective date and marketplace. Sources: 2027 announcement; GABBX6GZPA8MSZGW v58; EU rate cards 2026-02-01, 2026-07-01, 2026-11-02. Read at run time: the peak window and the next fee-change dates for the seller's store from Seller Central help *2026 US FBA fulfillment fee changes* (GABBX6GZPA8MSZGW, https://sellercentral.amazon.com/help/hub/reference/external/GABBX6GZPA8MSZGW) and *Update to US Referral and Fulfillment by Amazon fees for 2027* (https://sellingpartners.aboutamazon.com/update-to-us-referral-and-fulfillment-by-amazon-fees-for-2027) in the US, or the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf) in the EU/UK, and the dates a product's fees actually changed from Data Kiosk `createQuery` on `economics` (date ranges split at fee changes).
- **P-ful-23.** New-to-FBA programmes reduce fulfilment-family charges (free storage, returns waivers, placement and partnered-carrier credits). These appear as promotion or incentive amounts (economics `promotionAmount`; Storage Fees report incentive columns) rather than as missing charges. Sources: sell.amazon.com/fulfillment-by-amazon; FBA Reports page; economics schema; GZGEQLTM3RZXUV6T (20 units waived).
- **P-ful-24.** Unplanned prep/label services and inbound-defect fees are itemised per shipment, carton and FNSKU, with `fee-type` and `fee-total`, in the Inbound Performance report (Pricing or AF). US prep by Amazon ended 2026-01-01; the 2026 schedule replaced the double inbound charge with a single inbound defect fee. Sources: FBA Reports page; G201411300 v47; fulfillmentInbound_2024-03-20.json (`prepOwner`).
- **P-ful-25.** What the per-unit FBA fulfilment fee covers, and its price bands, are stated per store. CA, MX and JP state that it covers picking, packing, shipping, customer service and returns. A price threshold changes the rate: US $10 and $50, CA CAD 14, AU $13, JP ¥1,000, MX four bands (MXN 150/299/499). The thresholds are read from the store's page at run time. Sources: GABBX6GZPA8MSZGW v58 (US, via listing seat); sell.amazon.ca/pricing; sell.amazon.com.au/pricing; sell.amazon.co.jp/pricing; vender.amazon.com.mx/precios. Read at run time: the price thresholds from the seller's store's page (US: Seller Central help *2026 US FBA fulfillment fee changes*, GABBX6GZPA8MSZGW, https://sellercentral.amazon.com/help/hub/reference/external/GABBX6GZPA8MSZGW; CA: https://sell.amazon.ca/pricing?lang=en-CA; AU: https://sell.amazon.com.au/pricing; JP: https://sell.amazon.co.jp/pricing; MX: https://vender.amazon.com.mx/precios; EU/UK low-price FBA caps: the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf)), and the fee a SKU gets at a given price from `getMyFeesEstimateForSKU`.
- **P-ful-26.** The weight that sets the fee differs by store. EU and IN use the greater of unit weight and dimensional weight (L×W×H cm ÷ 5,000) for parcels and oversize; AU divides by 4,000; CA uses the greater of actual and dimensional weight. Envelopes, low-price FBA and special oversize use unit weight in the EU, and envelopes do in AU. JP sizes items by the sum of the three sides. Sources: EU rate card 2026-11-02; sell.amazon.in/fees-and-pricing; sell.amazon.com.au/pricing; sell.amazon.ca/pricing; sell.amazon.co.jp/pricing. Read at run time: the weight rule and the divisor from the seller's store's page (EU/UK: the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf), "Calculating your FBA fees"; IN: https://sell.amazon.in/fees-and-pricing; AU: https://sell.amazon.com.au/pricing; CA: https://sell.amazon.ca/pricing?lang=en-CA; JP: https://sell.amazon.co.jp/pricing), and a SKU's Amazon-measured dimensions and tier from `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`.
- **P-ful-27.** Whether a fee figure includes tax differs by store. JP fulfilment fees include 10% consumption tax, and MX fees include IVA. IN fees exclude GST, which is added. AU fees exclude GST. EU manual processing fees have VAT assessed in addition where applicable. So fee figures from two stores can sit on different tax bases. Sources: sell.amazon.co.jp/pricing; vender.amazon.com.mx/precios; sell.amazon.in/fees-and-pricing; sell.amazon.com.au/pricing; EU rate card 2026-11-02 p. 24 footnote. Read at run time: the tax basis from the seller's store's page (JP: https://sell.amazon.co.jp/pricing; MX: https://vender.amazon.com.mx/precios; IN: https://sell.amazon.in/fees-and-pricing; AU: https://sell.amazon.com.au/pricing; EU/UK: the *Rate Card Europe Fees* in force (effective 2 November 2026: https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf)), and the tax on each estimated fee from `getMyFeesEstimateForSKU` (`TaxAmount`).
- **P-ful-28.** India's FBA charge set is its own: weight handling by distance (local, regional, national; 500 g steps; volumetric ÷ 5,000), pick & pack per unit, storage per cubic foot per month, per-unit FC removal, and a closing fee by price band and channel. Sources: sell.amazon.in/fees-and-pricing (read 2026-11-10). Read at run time: the weight steps, the divisor, the distance bands and the rates from *sell.amazon.in fees and pricing* (https://sell.amazon.in/fees-and-pricing), and a SKU's estimated fees from `getMyFeesEstimateForSKU`.
- **P-ful-29.** Who bills AGL, and when.
  - Amazon or the affiliate named on the invoice bills AGL. For China-origin services and ocean carriage from China that is Beijing Century Joyo Courier Co., Limited.
  - It bills on delivery to the destination, or as costs are incurred.
  - The seller pays every cost at the destination (freight, insurance, export, customs, duties, taxes, accessorials) "regardless of whether you are the IOR".

  Sources: AGL Freight Service Terms (dated 2026-01-14) §§Preamble, 1.2, 9.1, 9.5.
- **P-ful-30.** How AGL is paid and where it is recorded.
  - Payment is either USD from the Seller Central disbursement balance or a wire (CNY) through Shipper Central.
  - Balance-paid AGL appears in Transaction View under Service Fees as "FBA International Freight Shipping Charge" and "FBA International Freight Duties and Taxes Charge".
  - Timing: within 48 hours after FC receipt, or 7 days after delivery to the first FC when the stock is split. Any "additional fees" are typically charged 7 days after receipt and again 14 days later.

  Sources: Seller Central help *Paying for Amazon Global Logistics* (GZJ4B4HXDUEWP4PC, via search snippets); sell.amazon.com AGL page ("book, pay, and track shipments right in Seller Central"). Read at run time: the payment currencies and the charge timing from Seller Central help *Paying for Amazon Global Logistics* (GZJ4B4HXDUEWP4PC, https://sellercentral.amazon.com/gp/help/external/GZJ4B4HXDUEWP4PC, on the seller's own Seller Central), and the dates a balance-paid line actually posted from `listTransactions` (`postedDate`).
- **P-ful-31.** The AGL booking estimate is not the charge.
  - The Preliminary Estimate and the Collection Fee Estimate exclude import and export duties and taxes, accessorial charges and other services.
  - The charge moves with Amazon's or the carrier's measured weight and dimensions, and with the rate in effect on the cargo-ready or gate-in date.
  - Cancellation fees, demurrage, detention, storage, exam fees and abandonment costs fall on the seller.
  - Overcharge notices are due within 180 days of receipt of the invoice, and accepted claims may be credited to the account.

  Sources: AGL Freight Service Terms §§2.5, 7.2, 7.4, 7.6, 9.2, 9.3, 11.2, 11.3; Amazon course PDF *进口清关准备* (Import clearance preparation) pp. 24–25. Read at run time: the overcharge notice window and the estimate terms from *Amazon Global Logistics Freight Service Terms* (https://supplychain.amazon.com/legal/service-terms/global-logistics-freight), in the version in force for the booking.
- **P-ful-32.** Amazon is the broker on an AGL entry, not the importer of record.
  - The seller names the IOR (by default the seller), signs a power of attorney for Amazon's broker, and in the US holds a customs bond. Brokerage is included in the AGL price.
  - Duty refunds from customs, such as IEEPA refunds after 2026-02-20, go from CBP to the IOR, outside the seller's Amazon balance.

  Sources: AGL Freight Service Terms §§4.3–4.5; Amazon Customs & Trade page; Amazon course PDF pp. 9–10, 26–28, 39–40; CBP via `product-profit.md` P-prof-25; practitioner: Inventory Hero (2026-05-27).
- **P-ful-33.** The duty on a US AGL entry is set by a duty bill, and it can change later.
  - The broker builds the bill (税金单) from the commercial invoice and packing list. The importer has 3 days to confirm or dispute, and the bill auto-confirms within 72 hours.
  - Duty is paid before liquidation, either advanced by the broker or paid by the importer through its own ACH account.
  - It can be corrected later: by the broker before the preliminary statement date, by Post Summary Correction until 15 days before liquidation, and by protest within 180 days after liquidation.
  - So the duty first charged on a shipment can change months later. EU/UK duty bills also have a 3-day confirmation; JP bills auto-confirm after 24 hours.

  Source: Amazon course PDF pp. 8, 19–24, 27, 48. Read at run time: the confirmation, auto-confirmation and correction windows for the import country from Amazon's course *物流仓储：跨境物流 – 进口清关准备* (Logistics: cross-border logistics, import clearance; https://m.media-amazon.com/images/G/28/AS/AGS/SU/CN_GS_CB_Logistics_Basics_Customs_Clearance.pdf).
- **P-ful-34.** The AGL placement option decides whether a separate inbound placement fee follows.
  - Amazon Managed Placement is a flat per-shipment rate that includes destination charges and no separate placement fee.
  - Seller Managed Placement eliminates placement costs (at least five identical boxes per item).
  - Minimal shipment splits incur the inbound placement fee.
  - Ship to AWD carries no separate placement fee.

  Source: sell.amazon.com AGL page.
- **P-ful-35.** How Amazon SEND is billed.
  - US: in USD, to the Seller Central account. Freight posts within 24 hours of booking as "FBA international shipping charge" (亚马逊物流国际运费). Destination duty posts after delivery, at the actual duty customs charged the carrier, as "FBA international shipping customers charge" (亚马逊物流国际运输买家费用).
  - Carriers issue no invoices.
  - In Australia SEND is contracted and paid with the carrier directly, offline, and the carrier passes on any duty.

  Sources: sell.amazon.com SEND page (EN, ZH); sell.amazon.com.au/amazon-send. Read at run time: the billing currency and the posting times for the seller's store from *Amazon SEND (Seller Export & Delivery)* (https://sell.amazon.com/programs/seller-export-and-delivery; US) or *Amazon SEND* (https://sell.amazon.com.au/amazon-send; AU), and the posted lines and their dates from `listTransactions`.
- **P-ful-36.** Amazon Freight bills in its own shipper account: invoices are in the portal's Billing & Payments table, on a credit limit set from payment and credit history and reviewable monthly. Sources: freight.amazon.com newsroom (2026-02-09); freight.amazon.co.uk newsroom (2024-06-25).
- **P-ful-37.** No SP-API operation reads AGL bookings, estimates, Shipper Central statements, debit notes or broker duty bills.
  - Fulfillment Inbound v2024-03-20 lists ocean and air `shippingMode` values but only partnered-carrier and own-carrier `shippingSolution` values.
  - Balance-paid AGL and SEND lines reach Finances (F&A) under open-ended names. Finances v0 `ServiceFeeEvent` has no inbound-shipment field.
  - The Tracking API (grantless, US, from 2026-08-05) gives customs and delivery milestones without amounts.
  - The Invoices API v2026-06-25 has no freight or duty field.

  Sources: ops.tsv and models clone (no "Global Logistics"/"AGL"); fulfillmentInbound_2024-03-20.json; financesV0.json; finances_2024-06-19.json; tracking_2026-01-30.json; financesInvoices_2026-06-25.json; Role Mappings (2026-10-28); practitioner: 积加 ("亚马逊未提供API", Amazon provides no API).
- **P-ful-38.** Names practitioners report on AGL money lines (not an Amazon list):
  - `FBAInternationalInboundFreightFee` and `FBAInternationalInboundFreightTaxAndDuty`, shown as "FBA International Freight Shipping Charge" and "FBA International Freight Duties and Taxes Charge".
  - "FBA International Freight Shipping Charge Adjustments".
  - `GlobalInboundTransportationFreight` and `GlobalInboundTransportationDuty`.

  Sources: GZJ4B4HXDUEWP4PC (display names, via snippet); practitioners: AMALYTIX (2026-10-20), MyRealProfit glossary, Synder.
- **P-ful-39.** Global Warehousing and Distribution (from 2026-04-09) stores stock in China (Shenzhen; Shanghai from 2026-07-16) and replenishes US FBA through AGL, which a user must onboard.
  - Under FOB, export declaration and origin port handling are invoiced separately.
  - Its fee schedule was not public on any Amazon page read on 2026-11-10.

  Sources: News posts 91f2bda1… (2026-04-09) and 20c69db3… (2026-07-07).
- **P-ful-40.** One AGL shipment's cost is recorded in several places:
  - the booking's Preliminary Estimate;
  - balance lines, posted in stages (freight, then duties and taxes, then "additional fees" up to about three weeks after receipt);
  - for wire payers, Shipper Central statements and debit notes;
  - the broker's duty bill, which can be corrected later;
  - any placement line, depending on the option booked.

  A settlement-built cost and the seller's own freight records can each hold part or all of it. Which record a seller treats as the cost, and how it avoids counting a shipment twice, is the seller's choice. Sources: AGL Freight Service Terms §§7.9, 9.2, 9.5; GZJ4B4HXDUEWP4PC (snippet); Amazon course PDF pp. 19–24; sell.amazon.com AGL page.

## Verification

The verifier checked this file on 2026-11-09/10, by plain GET of public pages, greps and `python3 -I` over the models clone (db2936aa), the GitHub commit API (read-only) and macOS PDFKit text extraction. Rate-card page 21 was also rendered and read as an image.

**What was checked.**
- **EU rate cards.** All three 2026 EU rate cards were downloaded fresh: effective 2026-02-01, 2026-07-01 and 2026-11-02. Checked on them: every quote in A2, A4, A5, B4–B7, C5, D3, E2, E3, F2, G2, H3 and I2.
- **The 2027 US letter**, word for word (B3, D2, E5).
- **Other Amazon pages:** sell.amazon.com/fulfillment-by-amazon, the AWD page, the capacity blog, the Supply Chain Portal fees page, and the removal post 2f4edad8.
- **The model, against the clone:** every model quote in D1, E4, F1, H4, K3, N1, N2 and O1, and every rate in the tables.
- **Roles:** every role against Role Mappings (operations, 2026-10-28) and Role Mappings for Types (2026-09-09).
- **Dates:** the release-note and deprecation dates.

**Changes made** (old → new; why; source):
1. **`SETTLEMENT_ID`** (dated changes; *Model vs release notes*; open question 7).
   - Old: "announced… the binding answer is Amazon's reply on a live account".
   - New: settled from Amazon's documents. It is not a `listTransactions` filter: it was added in df7c6298 (2026-10-28) and removed in db2936aa (2026-10-29), whose diff is quoted. The live reference page (2026-11-10) lists only `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`. It filters `listSummary`.
   - Source: GitHub commit API; the listtransactions reference page.
2. **Data Kiosk role** (Data Kiosk row; P-ful-18).
   - Old: one clause of the correction, with no date or URL.
   - New: the correction's full words, its URL and its page timestamp (2024-07-02). Also that the Data Kiosk API page (updatedAt 2026-10-20) still lists only Brand Analytics.
   - Still unresolved; the `createQuery` reply settles it.
3. **Roles header.**
   - Old: "both updatedAt 2026-10-28".
   - New: operations 2026-10-28, types 2026-09-09 (the local copies' front matter).
4. **Inbound rate.**
   - Old: "2 / 6 (reads)".
   - New: `listDeliveryWindowOptions` is 2 / 30.
   - Source: fulfillmentInbound_2024-03-20.json.
5. **F2, the EU aged-surcharge exclusion.**
   - Old: "excludes … (footnote placement as extracted)".
   - New: footnote 1 sits on the 241–270 column only, so those categories start at 271 days.
   - Source: rendered p. 21.
6. **F3, the assessment date.**
   - Old: "No Amazon page read today states the assessment date."
   - New: AU's page states "15th of the month", and the JP notice states the 2026-04-15 assessment. US and EU remain practitioner-only.
7. **C5.** Placement absence re-checked on all three cards. The card's "countries enabled for placement" phrase is not a fee.
8. **Section P.**
   - Old: "CA rest not read", "MX rate card not read", "JP, AU, IN … not read. Open."
   - New: P1 (CA), P2 (MX), P5 (JP), P7 (AU) and P8 (IN), filled from Amazon's own pages read 2026-11-10.
9. **CA liquidation.**
   - Old: [opinion, snippet].
   - New: [official], from News_Amazon CA a9383e96. Added to P-ful-11 and to section 10.
10. **Section 10, EU storage figures.**
   - Old: "extraction gave 0.62 / 0.82 for one column; another vendor quotes €27.54 / €52.20".
   - New: the card's own columns. The 0.62/0.82 is UK £/ft³ for apparel, and €27.54/€52.20 is the official EU standard non-apparel rate.
   - Added: dated CA, MX, JP, AU and IN figures.
11. **Stable fact 3 and P-ful-5.**
   - Old: "US 181, EU 241".
   - New: the starting age per store, the EU apparel exemption from the first band, and the 15th-of-month assessment where stated.
12. **New positions P-ful-25 to P-ful-28** (sourced: price bands; weight basis; tax basis; India's charge set). Rewritten while adding: P-ful-27's "is compared on the same tax basis" became the fact behind it.
13. **Dated changes added:** CA 2025-11-05 (liquidations; no 2026 increases), JP 2026-04-01 and 2026-04-15, MX 2026-06-04.
14. **Manufacturing-cost reimbursement date** (dated changes; edited by the refunds verifier, 2026-11-10). Old: "2025-03-10". New: "2025-03-31", moved from 2025-03-10. Source: News_Amazon "New effective date for FBA inventory reimbursement policy", https://sellercentral.amazon.com/seller-forums/discussions/t/ed8abc33-a1d5-417d-b2e2-03b789099833, posted 2025-02-28, read 2026-11-10: "will now go into effect on March 31, 2025, instead of March 10, 2025".

**Figures the brief named, re-checked and holding:**
- EU aged surcharge "More than 241 days": in all three 2026 cards.
- No inbound placement fee section in any EU card.
- Pan-EU low-inventory cost coverage fee "across Germany, France, Italy and Spain", "Does not apply to the Netherlands, Poland, Sweden, Belgium and Ireland", with both 90- and 30-day days of supply below 28.
- EU fuel surcharge 1.5% from 2026-04-17 (July card) and 2% from 2026-11-02 (November card).
- EU peak window 2026-10-15 to 2027-01-14.

**Positions checked:** 24 original. Changed: 3 (P-ful-5, -11 and -18). Made [seat]: 0. Removed: 0. Added: 4 (P-ful-25 to -28). None of the 28 states a behaviour rule. P-ful-17's "never" stays marked [seat] pending open question 3. (Corrected 2026-11-10 after review: Amazon's model gives `ServiceFeeEvent` an order id and a SKU, so P-ful-17 now states the model's fields and leaves the order-scoped question open.)

**Not verified.**
- Help-page quotes taken from the listing seat's 2026-10-14 reads: G201074400, GC3Q44PBK8BXQW3Z, GV43F6S76Y9DHYRH, GABBX6GZPA8MSZGW, G201411300, GG5KW835AHDJCH8W, G37G73BJXHF75ACH, GL7U4JFSDXUTQAJ, G6WAEPTECPT2JUH3, GAFNWEYTJUV2GBFC, GZGEQLTM3RZXUV6T and G3RZC8DVQCDTCQ3B. They are JS shells to a plain GET and stay attributed to that reading. Their quotes exist in the listing playbook's files.
- Of those, two are corroborated elsewhere:
  - The capacity performance credit, by sell.amazon.com/blog/announcements/fba-capacity.
  - The 3.5% US/CA surcharge, by the EU card's parallel wording and practitioners.
- Practitioner readings of the 2027 detail pages (ppc.land): Low-Price FBA categories, central inbound regions, AWD 2.5× after 12 months, returns 2027.
- The unplanned-services snippet (I3).
- US help 53921 ("7th and 15th"), which is a snippet only.

**Gaps a long-time operator would name.**
- The 2027 rate tables (G201411300 is a shell).
- The EU 2027 card (not yet published as of 2026-11-10).
- UK low-inventory fee: the card applies the coverage fee to DE/FR/IT/ES only. Whether the UK has its own was not found.
- The names of JP, CA, MX, AU and IN charges on money lines.
- AWD and Partnered Carrier posting names.
- Multi-unit (Amazon Business) fulfilment discount (listing seat GMZ5WFTZHCM4Q4C5).
- SIPP discount rules (EU card p. 5 tables not transcribed).
- Remote Fulfilment and EFN cross-border fee rules beyond the table names.

### Gap fill (2026-11-10): Amazon-sold inbound transport and China-origin charges

Two completeness critics asked for this: a US/EU controller (AGL, Amazon Freight and other Amazon-sold inbound transport as money) and a Chinese finance director (AGL and China-origin inbound charges: freight, duties and taxes, posting and later true-ups). Before this fill the file named AGL only as two practitioner fee codes, a $200 credit and a prep note. Both gaps were open; neither was already covered. The work used plain GETs and curl of public pages, search snippets where help pages are JS shells, `python3 -I` greps over the models clone (db2936aa), the GitHub commit diff (read-only), and PDFKit text extraction of Amazon's Chinese course PDF.

**Added.**
- Dated changes: 2025-06-01 (partnered-carrier line rename, practitioner), 2026-01-14 (AGL terms), the IEEPA pointer, 2026-04-09 / 07-16 / 09-27 (GWD), 2026-08-05 (Tracking API), 2026-10-28/29 (`AMAZON_FBA_FROM_ORIGIN`).
- Section 3, new **Q1–Q11**: AGL scope and the inclusion of brokerage; the billing entity and timing (BCJ, Amazon Logistics, Inc. records); what the seller pays, with estimate vs charge, accessorials and the 180-day overcharge notice; the importer of record; the two payment routes, timing and display names; US duty-bill timing and its correction path (3-day confirmation, PSC, protest), with EU/UK and JP notes; how the placement option interacts with the placement fee; SEND billing (US vs AU); GWD; Amazon Freight invoicing; the partnered-carrier line in Payments.
- Section 4: a new table, *Amazon-sold inbound transport: what the API carries*, and the `AMAZON_FBA_FROM_ORIGIN` model history.
- Section 5: AGL line names (AMALYTIX, MyRealProfit, Synder) and the Synder-vs-Amazon contradiction on who pays duty; Threecolts; Inventory Hero; the shipment-ID join for partnered-carrier lines; the absence of Chinese ERP AGL documentation.
- Sections 7–10: stable facts 18–22; five run-time rows; three Seller-Central-only items; dated AGL and GWD figures.
- Pages read: 29 rows. Open questions 13–18.
- **Positions P-ful-29 to P-ful-40** (12 new; none renumbered). Each is a fact with Amazon's source first; P-ful-40 leaves the choice of cost record to the seller. None states a behaviour rule or a threshold.

**Gaps left.**
- The full text of Seller Central help pages GZJ4B4HXDUEWP4PC (paying for AGL), GR384ESWC8HH8667 (AGL claims), 202187670 / G202187670, G5NQMLZ7E6UBPVNE and ASFW4BD897LNTNN. They are JS shells to a plain GET, and their words here rest on search snippets.
- AGL fee tables (freight rates, accessorial schedule, cancellation-fee standard). They sit behind the AGL portal, and the rules tariff at dpiusa.com was not read.
- The gs.amazon.cn AGL / 亚马逊全球物流 notice pages. No gs.amazon.cn AGL page surfaced in search, and the Chinese course PDF was used instead.
- Which entity bills EU/UK/JP AGL, in which currency, and with what VAT/JCT invoice. Only snippet copies of Amazon's EU/UK guide say EUR/GBP and "Non-CN based entities cannot pay in CNY".
- Whether AGL duty true-ups (PSC, protest, IEEPA refunds) ever post to the seller balance (open question 14).
- How AGL lines join to the FBA shipment ID (open question 15).
- 领星 and 赛狐 documentation on matching AGL charges to a 货件: not found.
- Amazon Freight's payment terms (due days, card or ACH). The terms page requires sign-in.
- The GWD fee schedule, and whether GWD charges post to the balance.
- How Amazon SEND posts outside the US and AU (UK, DE, JP, AE, SA).

### Correction 1 (2026-11-10)

Applied correction 1 of brief 306 and the plugin zen's item 4: a value that differs by marketplace or changes from year to year is read at run time, not carried. Nothing was re-researched; operation and field names were checked against the models clone (db2936aa: `listTransportationOptions` `quote.voidableUntil`, `listPlacementOptions`, `listTransactions`, `listFinancialEvents` `FBALiquidationEvent.LiquidationFeeAmount`, `getMyFeesEstimateForSKU`, Data Kiosk `createQuery` with `economics` / `economicsPreview` and the `LOW_INVENTORY_LEVEL_FEE`, `HIGH_RETURN_RATE_FEE` and `RETURN_PROCESSING_FEE` enum values) and the report columns against this file's SP-API section. Page titles and addresses come from the Pages read table and the help IDs already cited; no page was fetched.

- **Positions changed** (one "Read at run time:" sentence added at the end; the value, its marketplace, date and citation kept as evidence; no other wording changed): P-ful-2 (dimension-fee claim window), P-ful-4 (storage utilisation threshold and window), P-ful-5 (aged surcharge starting age and assessment day by store), P-ful-6 (placement charge lag), P-ful-7 (low-inventory thresholds and windows), P-ful-8 (fuel surcharge percentage), P-ful-9 (return-rate thresholds, charge month, EU apparel share), P-ful-11 (liquidations referral rate), P-ful-13 (partnered-carrier void window), P-ful-22 (peak window and fee-change dates), P-ful-25 (price-band edges), P-ful-26 (dimensional-weight rule and divisor), P-ful-27 (tax basis of fee figures), P-ful-28 (India weight steps, divisor and bands), P-ful-30 (AGL payment currency and charge lags), P-ful-31 (AGL overcharge notice window), P-ful-33 (duty-bill confirmation and correction windows), P-ful-35 (SEND billing currency and posting lag).
- **Left as they are:** the other 22 positions. Their substance is a mechanism, a record or a fact of history (when a rule took effect, an operation's removal date, GWD's opening), not a varying value.
- **Stable enough for a skill:** items 2, 3, 4, 6, 8, 10, 12, 17, 18 and 20 lost their varying values (US storage collection days; aged starting ages and assessment day; the 45-day placement lag; the return-fee charge month and EU 50% share; the 15% liquidations rate; the 24 h / 1 h void window; the 90-day claim window; the annual change dates; AGL currencies and lags; SEND's 24-hour lag). Each value moved, with its date and source, to a row of *What cx must read at run time* naming where it is read; the fee-change dates joined the existing peak-window row.
- **No value was left without a place to read it.** Several places are Seller Central help pages that are JS shells to a plain GET; they are named by title, help ID and US address, and are read on the seller's own Seller Central.
