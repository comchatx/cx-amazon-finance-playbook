# Where a sale's money is, from order to bank

Read 2026-11-09 by the research seat. Tags:
- **[official]** Amazon's own page, model, contract, staff post or email (title + URL + date read).
- **[opinion]** A named practitioner or vendor.
- **[research]** A published study.
- **[seat]** This seat's own reasoning. It is never a position for a skill.
- **[command-verified]** A command run by this seat over the local models clone (`~/ComChatX_Project/scratch/sp-api-plugins/models`, commit db2936aa, 2026-10-29) or over saved pages.

How the pages were read:
- Seller Central help pages are a JavaScript shell to a plain GET in every marketplace tried (.com, .co.uk, -europe, .ca, -japan, .com.au, .in, .ae, .sg, .com.mx, .com.br). Their rules are therefore cited from Amazon staff posts on Seller Forums (server-rendered), Amazon emails that sellers pasted into the forums (labelled as such), sell.amazon.* pages, Amazon-hosted contracts, and the SP-API docs (`developer-docs.amazon/sp-api/docs/<page>.md`, fetched by `curl`).
- Help-page ids given here come from links on Amazon pages that name them. The pages behind them were not read.
- Three helper seats read the web pages through a fetch tool that summarises. Every Amazon quote that a position leans on was re-read by this seat with `curl` plus a text dump; those are marked ✓.

## What this covers

**Scope.** The money of one sale, from the buyer's order to the seller's bank, in every major marketplace:
- posting;
- deferral (Delivery Date Policy, DD+7; invoiced orders);
- reserves (Account Level Reserve);
- the balance buckets on the Payments dashboard;
- settlement periods and on-demand payouts;
- disbursement, currency conversion (Amazon Currency Converter for Sellers, Seller Wallet, third-party payment service providers);
- negative balances and the card on file;
- the SP-API operations, reports and notifications that carry each state.

**What it does not cover.** Fee definitions and what each fee does to a product's earnings belong to other files in this pack. Stock charges as stock states belong to the stock playbook. Reimbursement claims belong to the later recovery plugin.

**Skills it would feed.** The pack's payouts/cash skill: "where is my money and when does it reach my bank". It also feeds the reconciliation side of any accounting or earnings skill: why a settlement is not a period's sales, and why the deposit is not the settlement in the marketplace currency.

**Why a senior operator cares.** Cash, not profit, is what runs out:
- A seller's balance is split three ways: deferred, reserved and available. Each bucket moves on its own clock.
- The split changed in 2026 for long-tenured North American accounts.
- The SP-API now exposes most of the split (`listBalances`, `transactionStatus`, `listExpectedPayouts`). Before 2024–2026 only Seller Central showed it, so older tools and older advice are wrong about what an API can see.

**Dated changes since 2025-01-01** (details and sources in §A–H and §SP-API):
- 2025-01-31: Amazon staff state that delivery-date reserves, formerly a lump sum under "Account-Level Reserves", are now shown as deferred transactions. The US display switch was "By November 1" (News_Amazon post created 2024-10-04, so 2024-11-01).
- 2025-03-17: settlement reports `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE` and `…_XML` deprecated. **Removal 2026-11-11**, two days from today.
- 2025-03-18: Amazon.ie opened (press date; Amazon's own pages say "in 2025"). It sells from the European Seller Central account, where Ireland was added as a country option on 2024-12-10 (§E).
- 2025-04-30: `transactionStatus` value `DEFERRED_RELEASED` added (Finances 2024-06-19). The Seller Wallet API launched as a private beta.
- 2025-05-23: Amazon explains that Amazon Business invoiced orders stay deferred until the buyer pays, or at the latest seven days past the invoice due date (US).
- 2025-06-25: `listTransactions` gained the `transactionStatus` filter.
- About 2025-06: 亚马逊卖家钱包 (Seller Wallet) was presented to China-based sellers (trade press).
- 2025-06-27: Amazon staff state that DD+7 applies in Brazil, and that a bank change triggers a 3-day reserve.
- 2025-07-21: Finances v0 `listFinancialEvents`, `…ByGroupId` and `…ByOrderId` deprecated, with **removal 2027-08-27**. `listFinancialEventGroups` is not on the schedule.
- 2025-08-27: the Seller Wallet API became "publicly available in the NA and EU regions".
- 2025-09-29/30: Amazon emailed the remaining accounts not yet on DD+7 (US sellers and UK/EU sellers whose extension ran to 2025-09-30) that their reserve moves to DD+7. Route: every date here is known only as sellers pasted the emails in Seller Forums, not from an Amazon page. A US seller pasted an email giving **2026-03-12** ("DD+7 March 12, 2026", created 2025-09-29T22:33Z, https://sellercentral.amazon.com/seller-forums/discussions/t/cd0dfc4d-fbc5-4ded-a0b1-4c7ed989c107). On the EU forum ("DD+7 Deferred Again", created 2025-09-30, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/7d30d954-dd74-4c46-b01e-48a7cc7f5c45), UK/EU sellers report an email at 1:33 giving "19th March 2026", a second at 1:42–1:43 giving "5th March 2026", and another seller "allocated March 12th". So the dates seen are 2026-03-05, 2026-03-12 and 2026-03-19, by account.
- 2025-09-01 (Roberto_Amazon, EU forum): the UK/EU DD+7 transition extensions to 2025-09-30 end ("no further extensions will be provided").
- 2025-12-03: `listTransactions` gained the filter `relatedIdentifierName=FINANCIAL_EVENT_GROUP_ID`. Seller Wallet `createTransaction` now needs `payeeContactInformation` for `THIRD_PARTY` payees.
- 2026-01-08: Amazon updated its Express Payout page (US; "currently free"; "there may be a 50 cent per transaction cost").
- 2026-01-28: `listTransactions` gained the `ORDER_ID` filter.
- 2026-03-02 / 2026-03-09 vs "2025": Seller Wallet EUR for DE, FR, IT, ES, BE, IE and NL. Trade press of Amazon's release is dated 2026-03-02 (Ecommerce News) and 2026-03-03 (ChannelX); Amazon's own EU forum post (Roberto_Amazon, "Announcing Amazon Seller Wallet EU", created 2026-03-09T16:46Z, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/d852cc31-987a-48cb-b58e-d4db422c5055) reads "We're excited to introduce Amazon Seller Wallet for European stores!". aboutamazon ("It's now easier for sellers to manage their money on Amazon", published 2022-07-25, page "Updated: November 04", dateModified 2026-11-05, https://www.aboutamazon.com/news/small-business/its-now-easier-for-sellers-to-manage-their-money-on-amazon) reads "In 2025, Amazon Seller Wallet EUR expanded to seven European stores". Both are Amazon's (re-read 2026-11-10 with `curl`); the file picks neither.
- 2026-03-04: the Business Solutions Agreement was updated. Mexico got its own BSA, a new Agent Policy was added, and a new Section 20 sets out the arbitrator's power (News_Amazon, created 2026-02-17). The withholding clause in §2 is not named among the changes. Two earlier changes still govern held funds (§I): from 2024-07-12 (EU notice) the BSA allows permanent withholding, and from 2024-10-09 (US; 2024-10-04 EU) the Funds Withholding policy became the Funds Disbursement Eligibility policy, with the appeal wait cut from 90 to 60 days.
- 2026-03-05 / 2026-03-12 / 2026-03-19: the DD+7 migration dates given to the remaining accounts (dates from emails as sellers pasted them; see 2025-09-29/30). A UK seller on 2026-03-09 wrote "DD+7 starts this week".
- 2026-04-01 (KJ_Amazon reply in a thread created 2026-03-24): Amazon staff say DD+7 amounts "may temporarily" show inside Account Level Reserve while transaction-level visibility rolls out.
- 2026-04-14: Amazon Ads deferred to **2026-08-01** the move of "a small number of advertisers" from card to balance deduction or Pay by Invoice (Amazon Ads page, re-read 2026-11-10).
- 2026-06-05: Amazon China's DD+7 explainer (globalselling.amazon.com) gives worked examples, Disburse on Demand for "所有卖家" ("all sellers"), the Express Payout conditions, and states that DD+7 reserves already in the account-level reserve are not moved into deferred transactions.
- About 2026-05-04: Amazon emailed that **Disburse on Demand** (once every 24 hours) had rolled out to sellers who completed the DD+7 migration (US).
- 2026-07-29: Finances `listBalances` and `listSummary` added. Transfers `listPayouts` and `listExpectedPayouts` added. The release note also announced `SETTLEMENT_ID` as a `listTransactions` filter; that filter is **rolled back**: the July model left it out, Amazon's models repo added it on 2026-10-28 (commit df7c6298) and removed it on 2026-10-29 (commit db2936aa, "SPAPI October Release Finance API Rollback"), and the live `listTransactions` reference (updatedAt 2026-09-10) names only `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`. The release note still carries the July sentence (updatedAt 2026-11-04).
- 2026-09-21: Seller Central "Finance Workspace" (agency report, no Amazon text).
- 2026-09-30: the Finance Remittance API launched. It is **vendors only**.
- About 2026-11-03/06: Seller Wallet GBP launched (UK).

## Amazon's own rules

### A. The life of a sale's money (the states, in order)

A1. **Shipment starts the clock; delivery plus seven days frees the money.** Amazon's email to sellers migrating to DD+7, pasted in "DD+7 March 12, 2026" (posted 2025-09-29) ✓:
> "When you ship an order, funds are collected and added to your deferred transaction amount. Upon delivery, funds become reserves to allow Amazon customers to receive and review orders and you to accrue fees and costs. After seven days, the funds are moved into your account balance, which can be disbursed automatically through your choice of the automatic settlement cycle or a once daily disburse-on-demand request."

[official, Amazon email as posted] https://sellercentral.amazon.com/seller-forums/discussions/t/cd0dfc4d-fbc5-4ded-a0b1-4c7ed989c107 (read 2026-11-09)

A2. **The policy and its default.** Micah_Amazon, "Understanding Account Level Reserves" (2024-08-06), reproducing help text ✓:
- "We typically reserve your funds until a specific number of days after your shipments are delivered. This is recognized as payments based on delivery date."
- "Funds are reserved until a shipment is delivered, plus a reserve period. The default standard setting reserve period is 7 days after delivery date ("DD+7" reserve policy). For example, if you sell something on January 1, and it is delivered on January 6, then under the DD+7 policy, your funds will become available for disbursement starting on January 14."
- "Your reserve period may be extended following an assessment of your overall risk and historical performance."
- "When you use an integrated shipping provider, we will use the actual delivery date of the order. In the absence of valid tracking data, we will use the latest estimated delivery date (EDD)."
- "If you have recently had a delivery date reserve policy applied to your account, or if you just started selling, it is normal to observe that all of your funds are held in reserve."

[official, staff post] https://sellercentral.amazon.com/seller-forums/discussions/t/aac4b8e9-c776-418e-8373-9484fbf8baa1 (also on the .ca forum; read 2026-11-09). The help page "Payments based on delivery date" is G202124090 (id from staff links; JS shell, not read).

A3. **Amazon's worked examples do not agree on the day count.**
- English examples ✓:
  - Jan 1 sold, Jan 6 delivered → "available for disbursement starting on January 14" (A2; also Brazil's "Entrega (06/01) → Liberação (14/01)").
  - Jan 1 sold, Jan 3 delivered → "available for disbursement on January 11" (A1's email).
  - UK email (pasted 2024-05-30): "if you ship an item on 1 June, and the delivery date is 4 June, the funds will be available for disbursement from 12 June" (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a5b93d1e-913f-4ac4-9f80-b1cce9f3347e).
  - All three land on the 8th calendar day after delivery.
- Amazon China's explainer, "详解｜亚马逊DD+7预留金政策：底层逻辑、新旧变化和实操建议" (2026-06-05, https://globalselling.amazon.com/news/news-notices-260605, re-read 2026-11-10 ✓):
  - 「假设你的货件5月1日发货，买家5月3日签收…送达7日后，5月10日资金即被释放」 ("shipped May 1, signed for May 3 … seven days after delivery, on May 10 the funds are released"): the 7th day.
  - 「假设你5月1日发货，买家5月5日实际签收：有效追踪 → 5月6日起算7天 → 5月13日资金释放」 ("delivered May 5: with valid tracking, the 7 days count from May 6 → released May 13"): the 8th day.
- The authority for any one transaction is the `maturityDate` Amazon returns in its `DeferredContext` ("The release date of the transaction"). [official; the day counts are seat arithmetic over Amazon's examples]

A4. **FBA and FBM alike.** Glenn_Amazon, reply dated 2025-10-01 in "DD+7 - does this apply to both FBM & FBA" (thread created 2025-09-30) ✓: "The DD+7 reserve policy applies to both seller-fulfilled (FBM) and FBA orders. For shipments with tracking, the funds will be released 7 days after the delivery date. For shipments without tracking, the funds will be released 7 days after the latest estimated delivery date." [official, staff post] https://sellercentral.amazon.com/seller-forums/discussions/t/7d00779e-3f21-42ae-adfe-8ac36b203ddd (read 2026-11-09). An earlier reply in the same thread that says "in different contexts" is not by Glenn and is not used here.

A5. **The hold can be longer than seven days.**
- Danny_Amazon, "Where's My Money? — Navigating Deferred Transactions" (2025-08-05) ✓: "we withhold the sales proceeds until a specified number of days after the order is delivered (usually 7-14 days)." https://sellercentral.amazon.com/seller-forums/discussions/t/a64e7047-1fdc-4ddd-8491-ce7f686b77b2
- CR_Amazon (AU forum, thread created 2024-04-30) ✓: "Payments are based on delivery dates and can range from 7 to 14 days." https://sellercentral.amazon.com.au/seller-forums/discussions/t/25026327-b395-4d48-b913-8d68b9de09c6
- An extension, as Amazon words it (email pasted on the EU forum 2024-07-19, "Your Reserve Policy – Delivery Date + 14 Days (DD+14)") ✓: "Your sales proceeds will be delayed while we are reviewing your account. Starting today, the reserve period for all of your orders will be 14 days after the delivery date. For example, if you ship an item on January 1, and the actual delivery date is January 4, then the sales proceeds will be available for disbursement starting on January 19." https://sellercentral-europe.amazon.com/seller-forums/discussions/t/19fe1365-987e-42d7-9dc2-a33187fd78a7 [official, email as posted]
- [official, staff posts; read 2026-11-09, re-read 2026-11-10]
- No Amazon text read names an exemption from delivery-date reserves, whether for FBA, for tenure or for good history. The only stated flex is the extension in A2.

A6. **What a deferred transaction is, and what a settlement pays.** Micah_Amazon, "What is a deferred transaction?" (2025-01-31) ✓:
- "Note that only released transactions are included for payout in a settlement period."
- "A transaction is deferred while an order is awaiting delivery or pending buyer payment."
- The deferral reasons "you may see on the Transaction view page" begin with "Delivery date policy (Orders are awaiting delivery)": "Sales proceeds are reserved until we know the buyer received the order in the promised condition, and to ensure that you have enough funds to fulfill any returns, claims, or chargebacks."
- "Previously, sales proceeds withheld through Delivery Date-Based Reserves appeared as a lump sum amount "Account-Level Reserves" on your Payments Dashboard. This is now shown as deferred transactions so that you can know exactly which orders are subject to these policies and for how long they will be res[erved]."
- Invoiced orders: "These transactions will be released after the customer completes their invoice payment, which typically occurs within 30-45 days after the order date. Note that these orders are also subject to delivery date policies, but in most cases, the invoice due date will be later than the reserve period."

[official, staff post] https://sellercentral.amazon.com/seller-forums/discussions/t/3fe1fff3-f924-42bc-aa45-69244e8d6f83 (read 2026-11-09). Help page "What is a deferred transaction?" = GLRNLZDAKHDBBVBY (id from link).

A7. **During the 2026 transition, DD+7 money may sit in the reserve line.** KJ_Amazon (reply dated 2026-04-01, thread created 2026-03-24) ✓: "Some sellers may see their transactions displayed at an account-level reserve, rather than as individual deferred transactions, while we complete rollout of transaction-level visibility to deferrals. Account Level Reserve (ALR) traditionally holds funds for refunds, claims, and chargebacks, but may temporarily include DD+7 transactions as we transition our system. This means sellers may see an increase in account-level reserve balances without corresponding transaction-level visibility. This does not impact when funds are released." [official, staff post] https://sellercentral.amazon.com/seller-forums/discussions/t/6c017ac3-9f3d-45a5-bc89-14f877ddf6cc (read 2026-11-09)

A8. **Settlement, reserve carry-over and time to bank.** "How Amazon seller payments work", sell.amazon.com blog (Mickey Toogood, 2025-07-30):
- "Amazon pays sellers via Automated Clearing House or electronic funds transfer. When you have a positive balance, Amazon initiates a transfer on a scheduled payout date and sends the funds in a single disbursement to the bank account on file".
- "In general, Amazon settles seller accounts every two weeks. We take your beginning balance, add your sales, subtract expenses, and adjust for any refunds, then transfer payment to you after withholding an amount in reserve. The reserved amount becomes the beginning balance for your next settlement period."
- "after Amazon initiates a payment, it can take up to five business days for the funds to appear in your bank account."
- "If it has been longer than five business days, you can track a payment with the trace ID listed on the Disbursements section."
- "The funds available in an account are the portion of your total balance set aside for transfer to you."
- Why a payout may not start: "If your bank account information is missing or invalid, Amazon won't initiate a payment." "Mismatches in card information, expiring cards, and other issues can cause payment delays." "If your selling account has a negative or zero balance due to expenses or product refunds, Amazon may not initiate payment." "If your account has a performance issue or suspicious activity, this could cause payment delays."

[official] https://sell.amazon.com/blog/amazon-seller-payments (read 2026-11-09; every quote above re-read 2026-11-10 ✓)

A9. **The contract (North America Business Solutions Agreement).** Amazon CDN redline PDF, no visible date. It is a redline, so verify against the live G1791 before treating a clause as current. [official]
- S-5: "we will remit to you your available balance on a bi-weekly (14 day) (or at our option, more frequent) basis, which may vary for each Elected Country."
- S-5: "Net Sales Proceeds from non-invoiced orders will be credited to your available balance when they are received by us or our Affiliates." Invoiced orders are credited "(a) if you have elected in advance to pay a fee to accelerate remittance … on the day all of Your Products included in an invoiced orders are shipped; or (b) otherwise, no later than the seventh day following the date that an invoiced order becomes due."
- S-5: "When you either initially provide or later change Your Bank Account information, the Remittance Calculation Date may be deferred by up to 14 days."
- https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/legal/BSA_NA_English_redlined.pdf (read 2026-11-09, by a helper seat; stdlib text extraction)

The AU agreement (Amazon CDN, file dated October 2023) adds: "If your account is subject to a reserve or withholding requirement, the time period for remittance of sales proceed to you may be longer than 14 days." https://m.media-amazon.com/images/G/35/01/Amazon_Services_Business_Solutions_Agreement_October_2023_LIVE.pdf [official]

### B. Account Level Reserve

B1. **Definition.**
- "Your Amazon account level reserve is a portion of your balance that we hold in reserve for a period of time to cover potential circumstances like refunds or chargebacks. It's a normal part of selling in the Amazon store" (A8 blog, which links help page G200136810, "What is an account level reserve"; JS shell, not read).
- Statement View definition (Jessica_Amazon_, EU, 2024-01-11): "Account Level Reserves: The amount of money that is reserved to ensure that you have enough funds to fulfil any claims or chargebacks." https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a64bdf02-d6bd-461e-b952-0e2492ba3cfe
- [official]

B2. **Amazon states the reserve as a sum of per-order holds by reason. It publishes no percentage.** Micah_Amazon, "Account Level Reserve for New Sellers" (2023-09-06) ✓:
- Reasons listed:
  - delivery-date reserves;
  - "When an A-to-z Guarantee claim is filed, the claim amount will be reserved until the claim is resolved. Some claims can take up to 14 days or longer to resolve";
  - "Money might be reserved if your account has any chargebacks from transactions in the last 90 days. The reserve will be released after the chargebacks are processed.";
  - "Your seller performance has fallen below our benchmarks";
  - account under review: "We might reserve funds if we notice an unexpected change in your sales or account activity, or if you are a new seller with estimated delivery times that are longer than your settlement period.";
  - "Local regulations require us to withhold income tax from you (varies by store)".
- "Multiple reasons for account level reserves can be applied at the same time. For example, if an order for $40 has incurred a chargeback and an order for $20 has an open A-to-z Guarantee claim, the total account level reserve from those two orders would be $60. Since there are many factors, we do not have a specific timeframe".

[official, staff post] https://sellercentral.amazon.com/seller-forums/discussions/t/8a25cfdc-51f9-44ff-960b-251997c476ef (read 2026-11-09)

B3. **The reserve's reason is shown in Seller Central.** Danny_Amazon (2025-07-24) points sellers to the "Statement View" tab, "which will show the reserve amount and the reason for the hold." [official, staff post] https://sellercentral.amazon.com/seller-forums/discussions/t/f42225d6-79c0-4549-b9aa-9ed92439d4b6 (read by a helper seat)

B4. **Every seller has one.** CR_Amazon (AU, about 2023): "All sellers, regardless are subject to account level reserves… This is applied to all sellers and is not something some sellers are omitted from." [official, staff post] (AU thread in A5)

B5. **Contract discretion.**
- NA BSA §2: "If we determine that your actions or performance may result in returns, chargebacks, claims, disputes, violations of our terms or policies, or other risks to Amazon or third parties, then we may in our sole discretion withhold any payments to you for as long as we determine any related risks to Amazon or third parties persist."
- NA BSA S-5: "We may establish a reserve on your account based on our assessment of risks to Amazon or third parties posed by your actions or performance, and we may modify the amount of the reserve from time to time at our sole discretion."
- AU §2.5 is the same "by notice to you".
- [official] (PDFs in A9)

B6. **What Amazon does not publish.** No Amazon text read gives:
- a reserve percentage;
- a "7 days of sales or 5% of 28 days" rule;
- "Tier I / Tier II";
- a fixed "first payout 14 days after first sale" rule for Seller Central.

The tier rules circulate among practitioners (see What practitioners add). The "7 days or 5% of 28 days" rule does have an Amazon origin, second-hand: AMZ123 ("关于亚马逊回款和收款你真的真的真的清楚吗？", 2022-01-18, https://www.amz123.com/t/K0djSBnw, re-read 2026-11-10) reproduces as Amazon's old payments FAQ: 「②资深卖家…(亚马逊以较高金额为准收取预留金)：a.过去7天的所有销售额将会被保留在亚马逊账户里…b.亚马逊将保留您在过去28天销售总额5%的金额」 ("established sellers … Amazon takes the higher amount: a. all sales of the past 7 days are held … b. Amazon holds 5% of the past 28 days' total sales"), and for new sellers 「预留金额为账户内所有余额」 ("the reserve is the whole balance"). [opinion, second-hand reproduction of an old Amazon text] No current Amazon page reached on 2026-11-10 (sell.amazon.com payments blog, Seller Forums staff posts above, Amazon China's 2026 DD+7 explainer, the BSAs) carries it or any other Account Level Reserve formula; the help pages that might (G200136810, G69122) are JS shells to a plain GET. The closest Amazon statements:
- The BSA's 14-day deferral after a bank change (A9).
- For sellers registered after 2011-10-30 on the Individual plan, "the remittance amount will not include Sales Proceeds from the 14-day period before the date of remittance" (NA BSA S-5).
- India's "first settles your account balance 14 days after you register" (G4).

[official, absence across the pages read]

### C. The balance buckets on the Payments dashboard

C1. **Statement View lines** (Jessica_Amazon_, EU, 2024-01-11, B1 URL):
- "Beginning Balance: The amount carried over from the previous settlement period including account level reserves and failed disbursements (if any)."
- "Beneath the tabs 3 sections detail your total balance, funds available and recent payments."
- The next disbursement date and estimated amount are "at the bottom of the Statement View page of the Payments Dashboard"; past payouts are on the "Disbursements tab" (A8 blog).
- [official]

C2. **Deferred transactions moved into the Total balance box.** News_Amazon: "By November 1, your delivery date reserve amounts will display as Deferred transactions in the Total balance box". Until then "they may still display under the account-level reserve field". "Only new transactions posted after this change will show as deferred." The year 2024 comes from Finaloop's dating ("In late October 2024…"). [official] https://sellercentral.amazon.com/seller-forums/discussions/t/3535e9f1-cea7-4037-9163-351eb91b2318 and https://sellercentral-europe.amazon.com/seller-forums/discussions/t/5eb04dd2-c1e7-47bb-9bf4-57049bc7d1fe (read by a helper seat)

C3. **Standard and invoiced orders are separate rows and separate payer entities (US).** "How Amazon Business invoices work for sellers" (2025-05-23):
- The Statement View has "Standard Orders", "Invoiced Orders", "Deferred Transactions" and "All Accounts" rows.
- "Your bank statement might show payments from Amazon Services LLC for invoiced orders, and you might receive separate payments for standard orders from Amazon Payments, Inc."
- "Amazon guarantees payment to the seller no later than seven days past the invoice due date—whether the customer pays their invoice or not."
- "the invoice due date is usually 30 days after the purchase date (net 30), though in some cases the invoice terms could give the customer 45 days or longer."
- "No, Amazon sellers cannot opt out of Pay by Invoice."

[official] https://sell.amazon.com/blog/amazon-business-invoice (read by a helper seat)

C4. **The Deferred transactions page (2021).**
- News_Amazon EU (2021-09-23): "Starting September 23, the new Deferred transactions page will be live under Payments reports… If you receive invoiced orders, these will also appear on this page… With the launch of deferred transactions, only transactions which have been disbursed will be included in the Settlement reports." https://sellercentral-europe.amazon.com/seller-forums/discussions/t/531c1ec69cedea0b00f7fdf94aaa23d4
- The US post says "starting September 20" and adds "If Delivery date reserve policies do not apply to you, you will not see any transactions". https://sellercentral.amazon.com/seller-forums/discussions/t/fa4dc3e343d8205930d783e0cf035427
- [official]

C5. **Named Seller Central pages** (ids from Amazon links, not read): Statement View G200378770; Payments report G200913190; Getting Paid G19301; Payment FAQs G69122; Linked global accounts G201841950; Currency Converter supported currencies G200497780. [official, ids only]

### D. Getting paid: the schedule, on-demand payouts and holds

D1. **The schedule.** It is 14 days by contract, "or at our option, more frequent", and "may vary for each Elected Country" (A9). A seller quotes Seller Support saying "Amazon sellers cannot change their payout frequency or schedule". No Amazon page read offers a daily, 7-day or 14-day schedule setting. [official contract; the support quote is a seller report]

D2. **Disburse on Demand (US, 2026).** Amazon email pasted 2026-05-04 ✓:
- "We've rolled out Disburse on Demand to sellers who have completed their migration to the standard reserve period of seven days after delivery date (DD+7)… you can begin using this feature to withdraw funds daily from your available balance."
- It allows "a disbursement of your available balance, up to once every 24 hours". The three conditions: positive available balance, active disbursement instrument, and "At least 24 hours have passed since your last disbursement request". "Requests that don't meet all three conditions won't be processed."
- "go to your Payments Dashboard in Seller Central, confirm your available balance in the Funds Available column, and then select Request Payment."

[official, Amazon email as posted] https://sellercentral.amazon.com/seller-forums/discussions/t/70a0e49b-096d-49fb-b4d7-19b6c3a8432b (read 2026-11-09; re-read 2026-11-10 ✓, created 2026-05-04)

Amazon China's DD+7 explainer (2026-06-05) ✓ adds:
- the request button works on the 「"标准订单"或"发票支付订单"行」 ("Standard Orders" or "Invoiced Orders" row); 「"延迟交易"行的"请求付款"按钮不可用」 ("the Deferred transactions row's Request Payment button is unavailable"); 3–5 business days to the bank; 「所有卖家均可使用」 ("available to all sellers");
- 「自动结算的14天周期不变…每次通过按需提现提款后，当前结算周期会被"截断"并重新开始计算14天」 ("the 14-day automatic settlement cycle is unchanged … each Disburse on Demand withdrawal 'truncates' the current settlement period and restarts the 14 days");
- greyed-out button causes: no released funds, 「退款、费用、拒付、索赔等超过可用资金」 ("refunds, fees, chargebacks, claims exceed available funds"), or under 24 hours since the last request.

D3. **"Disburse Now" in Europe predates this.** The 2023 EU notice (E2) says the change "will not affect your disbursement frequency, your ability to 'Disburse Now' or the total amount of funds received." In the API, `initiatePayout` is the EU8 counterpart (SP-API faces). [official]

D4. **Express Payout (US only).** "Get paid faster with Express Payout" (2026-01-08):
- "Express Payout makes this possible for US sellers who use Amazon Pay… receive deposits in 24 hours (including weekends)".
- Eligibility: "in-network US bank"; "valid business address in the US (US territories are excluded)"; "transactions of $1 million or less at the time of the payout initiation… Payouts over $1 million will be disbursed through the standard ACH process."
- Payouts can go to "a valid, seller-designated Visa debit card account".
- "Express Payout is currently free… In the future, there may be a 50 cent per transaction cost".
- The payments blog (A8) says "Eligible sellers in Amazon's US store can get paid faster with Amazon Express Payout."
- "you can opt-in to Express Payout through the click of a button on the Deposit Methods page in Seller Central … switching from the Standard Payout setting to Express Payout".
- [official] https://sell.amazon.com/blog/express-payout (Priya Padmanabhan, 2026-01-08; re-read 2026-11-10 ✓).
- Amazon China's DD+7 explainer (2026-06-05) ✓ lists it as a Seller Central deposit-method choice: 「在账户信息 → 付款信息 → 存款方式中选择标准付款 (3 至 5 个工作日) 或快捷支付（24小时到账）」 ("in Account Info → Payment Information → Deposit Methods choose Standard Payout (3 to 5 business days) or Express Payout (24 hours)"). Conditions: 「仅限美国站，要求专业销售账户且状态良好、关联美国银行账户、Visa或Mastercard借记卡（符合条件的美国银行发行）、账户活跃90天以上、无活跃的政策违规或账户冻结。快捷支付单笔不超过100万美元，且不支持部分提款」 ("US store only; a Professional account in good standing, a linked US bank account, a Visa or Mastercard debit card issued by an eligible US bank, active over 90 days, no active policy violation or account hold; at most USD 1 million per payout; no partial withdrawals"). So Express Payout covers Seller Central store proceeds (closes the earlier open question).

D5. **Holds after a bank change.**
- NA BSA: "may be deferred by up to 14 days" (A9).
- Brazil, Angie_Amazon (2025-06-27): "Alterações bancárias geram 3 dias de reserva!" ("bank changes cause a 3-day reserve"). https://sellercentral.amazon.com.br/seller-forums/discussions/t/ed3efbf6-2c5f-4106-863e-db75969a303f
- [official]

D6. **Deactivated accounts.** The wait is no longer 90 days. In 2022 sellers quoted the older "Funds withholding policy" in the forums: "after 90 days from when your account was deactivated, you may separately request funds disbursement by contacting disbursement-appeals@amazon.com". The JP PDF says "アカウント停止措置の解除ができない場合は90日後に支払い対象となります" ("if the suspension cannot be lifted, funds become payable after 90 days"). From 2024-10-09 (US) and 2024-10-04 (EU), Amazon cut the appeal wait to 60 days and renamed the policy. The rules, contract clauses and API faces are in §I. [official; read 2026-11-10]

D7. **Lending repayments.**
- UK Amazon Lending: "Repayments are fixed amounts (principal and interest) across the term, and collected monthly directly via Direct Debit." https://sell.amazon.co.uk/programmes/amazon-lending
- The US page lists partner lenders (Lendistry, Parafin, QuickBooks Capital, Uncapped, iBusiness Funding, Slope). It does not say whether repayment comes from the balance. https://sell.amazon.com/programs/amazon-lending
- In the Finances v0 model, `LoanServicingEvent` carries `LoanAdvance`, `LoanPayment` and `LoanRefund` [command-verified].
- [official]

### E. Rules by marketplace (where they differ)

| Marketplace | What Amazon's own words show | Source |
|---|---|---|
| **US** | Remaining accounts were emailed a DD+7 date of 2026-03-12 (as pasted; the 2026-03-05 and 2026-03-19 dates were reported by UK/EU sellers). "Most Amazon sellers worldwide already use DD+7." Disburse on Demand once a day after migration (D2). Express Payout (D4). Seller Wallet USD. Invoiced orders deferred and paid by a separate entity (C3). For US MFN orders, `listTransactions` is called without `marketplaceId` (model). | A1 email; D2; D4; C3; finances_2024-06-19.json |
| **CA, MX** | Part of the "North America and Brazil unified account" (sell.amazon.com/global-selling). No Amazon text read gives a CA or MX DD+7 date. sell.amazon.ca/learn ✓: "It can take up to five business days for the money to appear in your bank account after Amazon initiates a payment"; CA/US/MX sellers "can use your existing bank account to receive disbursements in your local currency with the Amazon Currency Converter for Sellers". No sell.amazon.com.mx payments page was found. ACCS for MXN is a flat rate. The CA ACCS page differs from the US one: it says "19 Amazon stores and 44 payout currencies", and "Volume-based fee does not apply to seller disbursements processed through Hyperwallet". | https://sell.amazon.ca/cad-usd-currency-converter ; https://sell.amazon.ca/learn |
| **BR** | DD+7: "Fundos liberados 7 dias após a entrega. Exemplo: Venda (01/01) → Entrega (06/01) → Liberação (14/01)" ("funds released 7 days after delivery"). A bank change causes a 3-day reserve. "pode levar até 5 dias úteis" ("can take up to 5 business days"). ACCS volume pricing excludes Amazon.com.br. | Angie_Amazon 2025-06-27 (D5 URL); ACCS page |
| **UK, EU** | Notice: "Starting August 3, 2023, in order to unify base reserve policies for all selling partners, your base reserve policy will change to a 'Delivery Date Based Reserve.'" "Delivery Date Based Reserve is our worldwide standard for selling partner accounts since 2016". Before the change, "your current base reserve policy uses the shipment confirmation date". UK transitions were postponed to 2024-01-31, then 2024-08-07, with "a transition extension to 30 September 2025". Then "no further extensions will be provided" (Roberto_Amazon, thread created 2025-09-01 ✓). The remaining UK/EU accounts were emailed DD+7 dates of 2026-03-05, 2026-03-12 or 2026-03-19 (as sellers pasted them, EU thread 7d30d954, 2025-09-30). EU8 on-demand payout in the API (`initiatePayout`). Seller Wallet EUR (DE FR IT ES NL IE BE) and GBP (UK, 2026-11). AISP/PISP roles exist in ES, UK, FR, BE, NL, DE, IT, SE, PL. | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a3106511f780c0ef74b7d8e2360163f7 ; …/a5b93d1e-913f-4ac4-9f80-b1cce9f3347e ; …/b701f3a6-8280-40bb-9097-e6ae9644aeb4 ; tpp-registration.md |
| **JP** | Deferred transactions (留保中トランザクション) with reason お届け日ポリシー ("delivery date policy") appear in JP forum threads from about 2021. Help text as quoted by a seller: "購入者が注文した商品を約束されたコンディションで受け取ったことが確認されるまで、留保中トランザクションとして留保されます。" ("held as a deferred transaction until it is confirmed that the buyer received the item in the promised condition"). No JP day count was found. Cadence ✓: 「Amazonがお客様から支払いを回収し、売上金を原則2週間おきに出品者様にお支払いします」 ("Amazon collects payment from customers and in principle pays sellers every two weeks", sell.amazon.co.jp/learn/beginners-guide) and 「売上は2週間ごとに銀行口座に振り込みます」 ("sales are transferred to the bank account every two weeks", sell.amazon.co.jp/pricing). "If sales exceeding the monthly subscription fee are accrued, the disbursement will be offset" (sell.amazon.co.jp/en/sell/account-registration). ACCS for JPY is a flat rate. | https://sellercentral-japan.amazon.com/seller-forums/discussions/t/907903cef08702409ce5168d288738ee (2021-11-30) ; https://sell.amazon.co.jp/learn/beginners-guide ; https://sell.amazon.co.jp/pricing |
| **AU** | "can range from 7 to 14 days" (CR_Amazon, 2024). The AU BSA allows remittance "longer than 14 days" under a reserve. "it can take up to five business days for your money to appear in your bank account after we initiate payment" (sell.amazon.com.au/new-seller-guide ✓). | A5; A9; https://sell.amazon.com.au/new-seller-guide |
| **IN** | "Generally, Amazon first settles your account balance 14 days after you register your seller account… Subsequently, the settlement process repeats every 7 days." "It usually takes 2 to 3 working days". Payouts go to an Indian bank account "even in the case of pay on delivery". India-only v0 adjustment types (`CanceledButPickedUpReimbursement`, `ReimbursementClawback`, `SellerRewards`) and TCS-GST charge types. The page is by Swati Bucha, dated 15/06/2017 (footer © 2024) ✓; no newer Amazon.in page on reserve or DD+7 was found. | https://sell.amazon.in/seller-blog/how-payments-work-for-online-selling ; financesV0.json |
| **AE, SA** | Country-specific MENA accounts. ACCS for AED is a flat rate. sell.amazon.ae/learn and sell.amazon.sa/en/learn ✓ carry the same text: "When your seller account is settled and you have a positive balance, Amazon sends the money to your bank account using an Automated Clearing House (ACH) or electronic funds transfer. It can take up to five business days…"; "We cannot make payments to a credit card or online payment system, such as PayPal." No reserve period or cadence is given. | sell.amazon.com/global-selling; ACCS page; https://sell.amazon.ae/learn ; https://sell.amazon.sa/en/learn |
| **SG** | Nothing payment-specific found in Amazon's words (sell.amazon.sg/learn carries no payment text, 2026-11-10). | — |
| **ZA** (Amazon.co.za; marketplace ID `AE08WJ6YKNBMC`, EU endpoint group) | Opened 2024-05-07 (press; Amazon announced it on 2023-10-17 and opened seller registration that day). ✓ "Do I need a South African bank account? No, however your bank account needs to be chargeable in ZAR. You can use the Amazon Currency Converter in Seller Central to receive your sales proceeds in a bank account outside of South Africa, converting to the relevant currency." The bank account "must be in your name or the name of your business". Fees: "Unless otherwise stated, all fees are in South African Rand (ZAR) and do not include applicable taxes, such as VAT"; "VAT is additonal [sic] to all fees displayed". "Amazon will charge the credit card to cover your fees, and proceeds from any sales will be deposited into your bank account." No reserve period, DD+7 date or payout cadence is given. | https://sellercentral.amazon.co.za/welcome/sell-online/how-to-register-as-a-seller ; …/welcome/sell-online/fees ; …/the-beginners-guide ; aboutamazon 2023-10-17 |
| **EG** (Amazon.eg; `ARBP9OOSHTCHU`) | ✓ Payout text matches AE and SA: "When your seller account is settled and you have a positive balance, Amazon sends the money to your bank account using an Automated Clearing House (ACH) or electronic funds transfer. It can take up to five business days…"; "We cannot make payments to a credit card or online payment system, such as PayPal." Fees are in EGP: "All listed fees are displayed excluding applicable VAT. We will additionally apply VAT to all fees displayed above." "Amazon proceeds from any sales will be deposited into your bank account (pre-deducting the fees). Any additional charges not covered by seller balance will be charge on the credit card." Registration asks for a "National Egyptian ID". No reserve period or cadence is given, and the page does not say whether the bank account must be Egyptian or in EGP. | https://sell.amazon.eg/learn?mons_sel_locale=en_EG ; https://sell.amazon.eg/pricing?mons_sel_locale=en_EG |
| **TR** (Amazon.com.tr; `A33AVAJ2PDY3EV`) | ✓ Cadence: 「Amazon Türkiye hesabınıza ilk ödeme, kayıt olduktan 14 gün sonra yapılır. Takip eden süreçte ödemelerinizi 14 günlük periyotlar halinde alırsınız. Transfer gerçekleştikten sonra 5 iş günü içinde para hesabınıza geçer.」 ("the first payment to your Amazon Türkiye account is made 14 days after registration; after that you are paid in 14-day periods; the money reaches your account within 5 business days of the transfer"). A payout needs a balance that is not below zero. Sellers: 「Geçerli bir şirket sicil numarası, Türkiye vergi numarası… kullanan herhangi bir şirket」 ("any company with a valid company registration number and a Turkish tax number"). 「Satış komisyonları, varsa KDV'ye tabidir.」 ("referral fees are subject to VAT where applicable"). The card is used 「hesap bakiyeniz yeterli olmadığında」 ("when your account balance is not enough"). The CA ACCS page excludes .com.tr from volume pricing (§F1). | https://satis.amazon.com.tr/satis ; https://satis.amazon.com.tr/satis/baslangic-kilavuzu |
| **IE** (Amazon.ie; `A28R8C7NBKEWEA`) | Opened 2025-03-18 (press; Amazon: "in 2025"). News_Amazon (EU forum, 2024-12-10) ✓: "Ireland is now available as a new country option in your European Seller Central account. Your professional selling plan will include the Ireland store." So IE uses the European unified account and EUR. It is covered by Seller Wallet EUR (F3), but not by `initiatePayout` (S4, whose list is DE FR IT ES SE NL PL BE). No IE-specific payout, reserve or fee-VAT text was found. | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/96cbb8c1-c899-4cd7-bfbf-3715fc0d05de ; https://sellercentral.amazon.ie/ |
| **BE** (Amazon.com.be; `AMEN7PMS3EDWL`) | European unified account, EUR. Covered by Seller Wallet EUR (F3) and by `initiatePayout` (S4). sell.amazon.com.be/en ✓ gives the monthly plan "excl. VAT" (figure in Facts for human readers only). No BE-specific payout or reserve text. | https://sell.amazon.com.be/en ; transfers_2024-06-01.json |

### F. Currency, deposit methods and payment service providers

F1. **Amazon Currency Converter for Sellers (ACCS)**, US page ✓:
- "Convert and transfer funds for 20 Amazon stores and 20+ payout currencies."
- Pricing "is based on your total cross-currency net proceeds during the past 12 months", tiered, with "Total cross-currency net proceeds across all Amazon stores".
- "Volume-based pricing is available for all global Amazon stores supported by Amazon Currency Converter for Sellers, with the exception of Amazon.com.br. Sellers who receive funds in AED, CHF, MXN, KRW, and TWD pay a flat rate of 1.5% regardless of tier. Sellers who receive funds in JPY pay a flat rate of 2.0%."
- Linked global accounts pool the volume ("Is my volume based on all my global accounts? Yes, as long as yo[u…]").
- "Amazon Currency Converter for Sellers uses the exchange rate applied by our third-party service provider on the day the transfer to your bank account is initiated. For failed disbursements, this is the exchange rate of the day the transfer is re-initiated."
- "Funds generally arrive in your local bank account in 1 to 5 business days."

[official] https://sell.amazon.com/programs/amazon-currency-converter (read 2026-11-09). The rates themselves are in Facts for human readers only.

F2. **For China-based sellers (亚马逊全球收款).** globalselling.amazon.com, "How should you choose a payment method?" (2023-07-07) gives three deposit options:
- a domestic CNY account via ACCS;
- an "Overseas or Hong Kong bank account";
- "a bank account provided to sellers by a payment service provider participating in the Payment Service Provider Program".

ACCS CNY was then "available in 10 Amazon marketplaces". https://globalselling.amazon.com/en/news/news-product-230810-2 [official]. Amazon's Chinese ACCS guidebook PDF has its own tier table (snippet only; see Facts for human readers only). gs.amazon.cn now redirects to globalselling.amazon.com.

F3. **Seller Wallet** (sell.amazon.com/tools/seller-wallet) ✓:
- "Seller Wallet USD supports the US store. A separate Seller Wallet EUR is available for Germany, France, Spain, Italy, the Netherlands, Ireland, and Belgium. Other stores are not currently supported."
- The same page also says: "Currently, you can use Amazon Seller Wallet to manage funds earned from selling in the US store only." The page contradicts itself, and it predates GBP.
- Eligibility: "a seller account in the US store that is in good account health" and "proof of your business establishment in one of the supported countries and regions."
- "You will see your US sales proceeds in Amazon Seller Wallet within minutes of your disbursement. Transfers can take 1 to 5 business days".

Trade press dates the Seller Wallet EUR launch 2026-03-02; Amazon's EU forum announcement is dated 2026-03-09 and aboutamazon says "In 2025" (see dated changes). Amazon's release via press: "Only one fee applies to international transfers, which decreases as your business with Amazon grows." "Sellers can enroll directly within Seller Central with no upfront costs or minimum requirements." (https://pubt.io/view/9E930FD9350039B1ED87DB93C0539F7A27416338; aboutamazon says "In 2025"). Seller Wallet GBP: "giving sellers more choice and control over how they manage their UK proceeds" (Manasi Kudtarkar, GM Seller Wallet; Retail Times 2026-11-06). [official]

F4. **The Payment Service Provider (PSP) Program.** News_Amazon, 2021-02-01:
- "Sellers that choose to use a payment service provider (PSP) to receive their Amazon store sales proceeds will be required to use a PSP that is participating in this program."
- First list: "LianLian Pay, NetEase Global Pay, Payoneer, PingPong, WorldFirst, AirWallex, OFX Global Currency Account, iPaylinks, Skyee, Zhejiang Chouzhou Commercial Bank, and Onerway".
- Non-participating PSPs got "a longer disbursement reserve period of up to 21 days after the latest estimated delivery date"; "Beginning on July 15, 2021, we will stop disbursement to sellers using non-participating PSPs altogether."
- https://sellercentral.amazon.com/seller-forums/discussions/t/b5b926382ab10beb898b7bedbf93b837 ; EU version …/29eb22801d8df04049acacc7a55cfc0b. Help page GHP8M87Z5W6XTSTL (id from link).
- Amazon's KYC email to a China-based seller (pasted 2023-12-21): "请在收到此邮件后的 45 天内完成以下步骤，以便继续接收向通过 PSP 开立的银行账户的付款" ("complete these steps within 45 days of this email to keep receiving payments to a bank account opened through a PSP"). https://www.wearesellers.com/question/86012
- [official]. No 2025–26 rule change was found; new members were (TransferMate, BRISKPE; snippets). The only current list read is KDP's, and KDP's 2026-08-01 stop is KDP only.

F5. **Each marketplace settles in its own currency; the deposit may be converted.** In the v0 model, `OriginalTotal` is "The total amount in the currency of the marketplace in which the transactions occurred" and `ConvertedTotal` is "The total amount in the currency of the marketplace in which the funds were disbursed" [official, financesV0.json, command-verified]. No Amazon sentence read says outright that "each store settles separately", but the BSA ("may vary for each Elected Country") and deposit methods assigned per store point that way. The SP-API's `listPayouts` "Results are grouped by the seller's account groups". [official; the per-store reading is seat]

### G. Negative balances and the card on file

G1. **The card is required.** Amazon email pasted by a seller: "For billing and security purposes, all Amazon sellers must provide valid credit card information from a credit card acceptable to Amazon." [official, email as posted] https://sellercentral.amazon.com/seller-forums/discussions/t/4cdd800c-e93b-46a5-b1b8-095b974476e8

G2. **The charge.** Billy_Amazon (about 2026-07-27), quoting the Payment FAQs (G69122) ✓: "when your account carries a negative balance at the end of a settlement period, Amazon charges your on-file payment method to settle the debt. If your bank imposes a credit limit, Amazon may retry the charge every 24 hours until the balance is paid in full." [official, staff post] https://sellercentral.amazon.com/seller-forums/discussions/t/4e9c95d9-81ab-436b-8492-80d42bde9804

G3. **The contract's collection means.** NA BSA §2: "For any amounts that we determine you owe us, we may (a) charge Your Credit Card or any other payment instrument…; (b) offset…; (c) invoice you…; (d) reverse any credits to Your Bank Account; or (e) collect payment… by any other lawful means." [official]

G4. **Ads billing (2026).** Amazon Ads, "Update on advertiser payments" (2026-04-14):
- Amazon "let a small number of advertisers know" it would update "their available payment methods to pay with their seller or vendor account balance or Pay by Invoice… deferring this change until August 1, 2026."
- "With account balance payments, debits and credits are handled automatically. This is the payment method used by the overwhelming majority of our advertisers."
- "If an advertiser doesn't select a preference… we'll automatically update their default payment method to deduction from available seller or vendor account balance. The existing payment method (such as a credit or debit card) will be retained as a backup".

- "With Pay by Invoice, we send an invoice at the end of each month, and payment is due 30 days later." "This update applies only to the small group of advertisers who have been contacted directly."

[official, re-read 2026-11-10 ✓] https://advertising.amazon.com/library/news/update-on-advertiser-payments (JP copy reads 「本変更を2026年8月1日まで延期いたします。」, "this change is deferred to August 1, 2026"). Whether it took effect on 2026-08-01 was not found.

### H. Deferral reasons and types the API names

H1. In the Finances 2024-06-19 model, `DeferredContext.deferralReason` is "The deferral policy applied to the transaction. **Examples:** `B2B` (invoiced orders), `DD7` (delivery date policy)", and `maturityDate` is "The release date of the transaction." The list is examples, not a closed set. [official, command-verified]

### I. Funds held at deactivation, suspension, review or verification (资金冻结)

Added 2026-11-10 (gap fill). Every Amazon quote in this section was read with `curl` and a text dump on that day ✓.

I1. **The contract (NA BSA, General Terms §2, redline PDF as in A9).** The text was re-extracted 2026-11-10 with a stdlib PDF text dump.
- Withholding while risk lasts: "If we determine that your actions or performance may result in returns, chargebacks, claims, disputes, violations of our terms or policies, or other risks to Amazon or third parties, then we may in our sole discretion withhold any payments to you for as long as we determine any related risks to Amazon or third parties persist."
- Offset: "(b) offset any amounts that are payable by you to us (in reimbursement or otherwise) against any payments we may make to you or amounts we may owe you".
- Permanent withholding: "If we determine that your account has been used to engage in deceptive, fraudulent, or illegal activity, or to repeatedly violate our Program Policies, then we may in our sole discretion permanently withhold any payments to you."
- Security amounts: "we may require that you pay other amounts to secure the performance of your obligations under this Agreement … These amounts may be refundable or nonrefundable in the manner we determine, and failure to comply with terms of this Agreement, including any applicable Program Policies, may result in their forfeiture."
- Transaction limits: "we may, but are not required to, impose transaction limits on some or all customers and sellers relating to the value of any transaction or disbursement".
- §3: Amazon may suspend or terminate if "your account has been, or our controls identify that it may be used for deceptive or fraudulent, or illegal activity". On termination, Sections "2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15, and 18" survive. This is a redline, so both the struck and the new survival lists appear in the dump; §2 is in both.
- S-5: the available balance is net of "(e) any amounts we require you to maintain in your account balance pursuant to this Agreement (including payments withheld pursuant to Section 2 of the General Terms, Section S-1.4, and applicable Program Policies)". S-1.4: "We may in our sole discretion withhold for investigation, refuse to process, restrict shipping destinations for, stop, and/or cancel any of Your Transactions."
- [official] https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/legal/BSA_NA_English_redlined.pdf

I2. **The EU change of 2024-07-12.** News_Amazon (EU forum, created 2024-06-27) ✓:
- "Effective July 12, 2024 … if we determine that your actions or performance may result in returns, chargebacks, claims, disputes, violations of our terms, this Agreement, or Programme Policies, or other risks to Amazon or third-parties, then we may, in our sole discretion, withhold any payments that may be otherwise due to you until the aforementioned concerns with your actions or performance are resolved."
- "If we determine that your account (or any other account that you have operated) has been used to engage in deceptive, fraudulent or illegal activity (including the sale of counterfeit goods), or to repeatedly violate our Programme Policies, then we may, in our sole discretion, permanently withhold any payments due to you."
- [official] https://sellercentral-europe.amazon.com/seller-forums/discussions/t/08045a88-3f1b-452e-bdb7-0222868c7984

I3. **The Funds Disbursement Eligibility policy (renamed 2024-10).** News_Amazon ✓, US post (created 2024-09-24, effective October 9, 2024) and UK post (created 2024-09-20, effective October 4, 2024), same text:
- "Renaming the Funds Withholding policy to the "Funds Disbursement Eligibility policy.""
- "We have also reduced the time within which sellers may appeal for their disbursements from 90 days to 60 days from the date of deactivation."
- Both posts say the update complements "recent changes we released to Section 2 of the Amazon Services Business Solutions Agreement".
- https://sellercentral.amazon.com/seller-forums/discussions/t/e5457317-25d9-4562-9207-86a19b3d38e9 ; https://sellercentral.amazon.co.uk/seller-forums/discussions/t/c640ebd9-b93d-49ca-9aab-873987dbae5d [official]

The policy text itself: Amazon CDN PDF "Fund Disbursement Eligibility Policy" (EU version: it names the "Amazon Services Europe Business Solutions Agreement" and a .co.uk address; undated; read 2026-11-10 ✓):
- "If we deactivate your account under Section 3 of the Amazon Services Europe Business Solutions Agreement and determine that your actions may result in risks to Amazon or third parties, then we may withhold any funds that may be in your account. These funds may be used to cover liability from your conduct and offset amounts that you owe, such as product returns or refunds, A-to-z claims from customers, inventory removal costs, outstanding fees, or monetary and non-monetary damages inflicted on Amazon."
- "If your account is reinstated as a result of the appeal, funds will be released and disbursed according to your disbursement schedule."
- "Even if your appeal is not decided in your favor, or you choose not to appeal the deactivation, you can separately appeal to seek any withheld funds by contacting disbursement-appeals@amazon.co.uk at any point after 60 days from the date when your account was deactivated. We will release any remaining funds (less any amounts used to offset amounts you owe us) after evaluating your account for deceptive, fraudulent, or other illegal activity and confirming your identity."
- "we may request that you provide additional information or documentation regarding your identity, financial instruments, or supply chain … we may validate any information that you provide with third party services or government agencies."
- "If we find that you have engaged in deceptive, fraudulent, harmful, or illegal activity, have abused our systems, or repeatedly violated our policies, or if we cannot confirm your identity, we may be legally required to withhold any payments to you." Examples: "falsifying or misrepresenting your identity or activity in our store, or violating the Amazon anti-counterfeiting policy."
- https://m.media-amazon.com/images/G/02/Program_Policy/Fund_Disbursement_Eligibility_Policy.pdf [official]. Help page id 9RA9LYBJ3QP27M6 (from an Amazon email that a seller pasted on the .co.uk forum on 2024-11-30; JS shell, not read).
- Staff and addresses: a Canada forum staff reply (LeviDylan, thread created 2024-09-08) gives "disbursement-appeal@amazon.com 60 days after your deactivation". Charles_Amazon (US, thread created 2022-11-09) says the funds request is judged like a reinstatement appeal. The address differs by marketplace (.com, .co.uk) and by post. [official, staff posts]
- An Amazon reply to a funds appeal, pasted on the .co.uk forum (thread created 2024-11-30): "We have thoroughly reviewed your account and the information you provided, and confirmed that the actions taken were correct and in accordance with the Amazon Services Business Solutions Agreement and our Funds Disbursement Eligibility Policy." The seller notes "My balance is shown at -". [official, email as posted] https://sellercentral.amazon.co.uk/seller-forums/discussions/t/985bc0c6-9161-4918-9db9-75149613f2e0

I4. **Holds without deactivation.**
- *Account under review.* A notice that a seller pasted on the US forum (thread created 2025-04-05): "Your account is currently under review as per section 3 of the Amazon Services Business Solutions Agreement. During the review, FBA shipment creation ability will be disabled and your funds will be withheld in accordance with our "Funds Disbursement Eligibility Policy"". The review asked for supplier invoices "issued within the last 365 days". [official, notice as posted] https://sellercentral.amazon.com/seller-forums/discussions/t/94e0a55b-4554-4414-b701-58cac83553be
- *Identity verification (INFORM Consumers Act, US).* Sonny_Amazon (reply 2023-06-19, quoting the staff FAQ): "After you submit your information to verify your identity, we will aim to lift the hold on your disbursements within 24 hours. When the hold is removed, the banner on your Account Health page notifying you about the hold on your disbursements will disappear. You may also receive an email notification letting you know this has been lifted. The available balance will disburse on your next scheduled settlement date." The same reply adds: "if you change banks there may be a temporary hold on disbursements for security purposes". [official, staff post] https://sellercentral.amazon.ca/seller-forums/discussions/t/4e5eecd7-f728-46f3-956f-413dcee0ce7e
- *Re-verification (EU).* A seller described (EU forum, 2023-12-05) an Amazon email "in line with the Amazon Services Business Solutions Agreement", saying that "if I don't provide the required information within 10 days, disbursements for my Amazon selling account may be put on hold, or my account might be deactivated". This is the seller's paraphrase, not a pasted email. In the same thread, Micah_Amazon points to the Account Level Reserve on Statement View. https://sellercentral-europe.amazon.com/seller-forums/discussions/t/578deeb6-bc06-425c-8f7f-eb49953e5d04
- *Reserve reasons.* B2's list already includes "account under review". A bank change defers payout (D5).
- *ACCS CNY and verification.* Amazon China's ACCS page ✓: 「使用亚马逊全球收款不会触发额外的卖家身份验证（SIV）审核。欧洲站点相关审核将按照亚马逊KYC的具体政策执行。」 ("using ACCS does not trigger an extra seller identity verification (SIV) review; European-store reviews follow Amazon's KYC policy"). https://gs.amazon.cn/accs

I5. **How a held balance shows in the API** [official, command-verified over the models clone db2936aa].
- `listExpectedPayouts` status `DISABLED`: "Payouts have been disabled for this account." `AT_RISK`: "The payout may fail because of an invalid deposit instrument." `NO_PAYOUT_EXPECTED`: "The expected balance is negative, resulting in no payout." (transfers_2024-06-01.json `ExpectedPayoutStatusName`).
- `listPayouts` `statusHistory[]` carries a free-text `failureReason` (example "Insufficient funds") and status `NO_PAYOUT` ("No payout is made for this settlement period").
- `listBalances` balance types and Amazon's definitions (finances_2024-06-19.json `Balance`):
  - `AVAILABLE`: "The total balance currently available in the account."
  - `DEFERRED`: "a portion of sales revenue that is temporarily withheld before being transferred to the available balance after a specified period."
  - `ACCOUNT_LEVEL_RESERVE`: "Balance reserved as a safety measure to cover potential liabilities such as refunds, chargebacks, or other claims. Based on sales volume, product category, and account history."
  - `RESERVED`: "The reserved balance is sum of Deferred and Account Level Reserved."
  - `TOTAL`: "Overall sum of balances including available and reserved."
  - The model's example nests `DEFERRED` 9000 and `ACCOUNT_LEVEL_RESERVE` −2000 under `RESERVED` 7000, beside `AVAILABLE` 8000 and `TOTAL` 15000. In that example the reserve is a negative amount.
- No balance type, transaction status or field names funds withheld under §2 or the Funds Disbursement Eligibility policy, and none gives a reason. Where a withheld balance appears (available but not paid out, Account Level Reserve, or elsewhere) is not stated by Amazon. [command-verified: grep for withh/suspend/deactivat/hold/freeze over the finances and transfers models returns only tax-withholding text]

I6. **Court-ordered freezes (US).** No Amazon text read describes them, apart from the policy's "we may be legally required to withhold any payments to you" (I3). Practitioners' account is in What practitioners add (中伦 2026-10).

### J. After disbursement: the CNY leg for China-based sellers (结汇)

Added 2026-11-10 (gap fill). Amazon's own words first, then the PRC rules that bind the payment service provider (PSP) and bank leg. The PRC texts are tagged **[official: PRC regulator]**: they are not Amazon's.

J1. **ACCS CNY to a domestic bank account (亚马逊全球收款)**, Amazon China product page ✓ (gs.amazon.cn/accs, undated, read 2026-11-10):
- 「协助卖家们使用国内银行账户以人民币接收全球付款」 ("helps sellers receive global payments in CNY into a domestic bank account"); 「目前覆盖全球十大站点」 ("currently covers ten marketplaces"); 「直接存入国内银行账户，无需虚拟银行账户」 ("deposited directly to a domestic bank account, no virtual bank account needed"); 「自动转账换汇，无最低提款限额」 ("automatic transfer and conversion, no minimum withdrawal").
- Fee inside the rate: 「与使用亚马逊全球收款相关的所有费用和收费都包含在汇率中。在您收到账户转账时，您看到的【付款一览】页面上有货币兑换后金额，将鼠标悬停在该金额上便可查看汇率。」 ("all fees for ACCS are included in the exchange rate; the converted amount on the Payments overview page shows the rate when you hover over it").
- Tiering: 「阶梯定价根据卖家过去连续12个月区间内的净销售额所在阶梯，给予相应的优惠费率，并在每月自动更新」 ("tier pricing applies the rate for the seller's net sales over the past 12 consecutive months, updated monthly"). Linked NA, EU and JP accounts pool their volume, and 「卖家可以选择在北美/欧洲/日本的任何站点中使用获得的费率，而不一定必须要用于所有的站点」 ("the seller may use the earned rate on any NA/EU/JP store, not necessarily all"). The lowest rate is 「低至0.4%」 ("as low as 0.4%"; the table is in Facts for human readers only).
- Timing: 「款项将在亚马逊下发付款通知后自动打出，在1-3个工作日内转入您的国内账户」 ("paid out automatically after Amazon's payment notice, into the domestic account in 1–3 business days"). US-store sellers see 「预估银行到账日期与时间、付款状态、付款进度」 ("the estimated bank arrival date and time, payment status and progress") under Reports → Payments.
- Who pays in China: 「依照中国人民银行和国家外汇管理局有关规定，到中国的付款由持有牌照的中国服务商首信易支付或富友支付处理」 ("under PBOC and SAFE rules, payments to China are processed by the licensed Chinese providers PayEase (首信易支付) or Fuiou (富友支付)").
- Switching: 「卖家可随时转换收款方案」 ("sellers may switch payout solutions at any time") on the Deposit Methods page.
- [official] https://gs.amazon.cn/accs (gs.amazon.cn serves this page; other gs.amazon.cn paths redirect to globalselling.amazon.com)

J2. **Amazon China on double conversion through a PSP**, 「选择了「0费率」，但跨境收款真的是「0成本」吗？」 (article dated 「2025年2月」, read 2026-11-10 ✓):
- A seller with US, CA and MX stores who points CA and MX at a USD virtual account: 「部分第三方支付机构则可能会经过两次货币转换，存在两种累加费用」 ("some third-party providers may convert twice, with two stacked fees"); 「将「加拿大元、墨西哥比索等当地货币兑换美元」，会产生「货币转换费用」」 ("converting CAD, MXN etc. into USD incurs a conversion fee"); 「当您的资金从虚拟美金账户转账到国内人民币账户时，还会面临「二次汇损」」 ("moving funds from the virtual USD account to a domestic CNY account brings a 'second FX loss'"); 「您可能会误以为是正常的汇率损失」 ("you may mistake it for a normal exchange-rate loss").
- ACCS: 「只经过一次换汇，只收取一次费用」 ("one conversion, one fee").
- This is Amazon promoting its own product against PSPs. [official, promotional] https://globalselling.amazon.com/zhishi/article-250208-1

J3. **SAFE, 《支付机构外汇业务管理办法》 (汇发〔2019〕13号, issued 2019-04-29)**, State Council Gazette copy, read 2026-11-10 ✓. Effective "自发布之日起" ("from issue"); it replaced the 2015 pilot notice (汇发〔2015〕7号).
- PSPs need a SAFE registration (名录登记) and must verify identity and trade authenticity: 第四条 「支付机构应对交易的真实性、合法性及其与外汇业务的一致性进行审查」 ("the PSP shall review the authenticity and legality of transactions and their consistency with the FX business").
- 第二十一条 transaction information to collect: 「商品或服务名称及种类、数量、交易币种、金额、交易双方及国别、订单时间等」 ("name and type of goods or services, quantity, currency, amount, both parties and their countries, order time, etc.").
- 第二十二条 「应确保资金收付与交易在主体、项目、金额等方面一致」 ("receipts and payments must match the transaction in party, item and amount").
- 第二十三条 for higher-risk transactions the PSP 「应要求市场交易主体提供相关单证材料。不能确认交易真实合规的，应拒绝办理」 ("shall require documents; where authenticity cannot be confirmed, it shall refuse").
- 第二十四条 「单笔交易金额原则上不得超过等值5万美元」 ("a single transaction in principle may not exceed USD 50,000 equivalent"), unless the PSP's registration is varied.
- 第二十五条 结汇 goes through the partner bank, 「实现交易信息的逐笔还原，除退款外不得办理轧差结算」 ("transaction-by-transaction restoration; no netting except refunds"), and 「应在收到资金之日（T）后的第1个工作日（T+1）内完成结售汇业务办理」 ("must complete the conversion within the first business day after receiving funds (T+1)").
- 第二十七条 「支付机构应事前与市场交易主体就汇率标价、手续费、清算时间、汇兑损益等达成协议。支付机构应向市场交易主体明示合作银行提供的汇率标价，不得擅自调整汇率标价，不得利用汇率价差非法牟利」 ("the PSP shall agree in advance with the client on rate quotation, fees, clearing time and FX gains/losses; it shall show the client the partner bank's quoted rate, may not adjust it on its own, and may not profit illegally from rate spreads").
- 第三十八条 「支付机构外汇业务项下的个人结售汇不计入个人年度结售汇便利化额度」 ("individuals' conversions under PSP FX business do not count towards the individual annual facilitation quota").
- 第四十条 monthly large-value reporting: clients with more than USD 200,000 a month or more than USD 50,000 in one transaction.
- [official: PRC regulator] https://www.gov.cn/gongbao/content/2019/content_5428473.htm

J4. **SAFE, 《关于支持贸易新业态发展的通知》 (汇发〔2020〕11号, 2020-05-20)**, SAFE Xiamen branch copy (.docx), read 2026-11-10 ✓:
- 一: banks and PSPs may provide conversion 「凭交易电子信息」 ("on the basis of electronic transaction information") for cross-border e-commerce.
- 二: 「从事跨境电子商务的企业可将出口货物在境外发生的仓储、物流、税收等费用与出口货款轧差结算，并按规定办理实际收付数据和还原数据申报。跨境电子商务企业出口至海外仓销售的货物，汇回的实际销售收入可与相应货物的出口报关金额不一致。」 ("cross-border e-commerce firms may net overseas warehousing, logistics, tax and similar costs against export proceeds, and report actual and restored data; for goods exported to an overseas warehouse for sale, the actual sales income repatriated may differ from the export-declaration amount").
- 三: platform and logistics firms may advance overseas costs for clients, in principle for at most 12 months.
- 四: 「从事跨境电子商务的境内个人，可通过个人外汇账户办理跨境电子商务外汇结算。境内个人办理跨境电子商务项下结售汇，提供有交易额的证明材料或交易电子信息的，不占用个人年度便利化额度。」 ("domestic individuals in cross-border e-commerce may settle through a personal FX account; when they provide proof of transaction amounts or electronic transaction information, the conversion does not use the individual annual facilitation quota").
- 九: restored reporting at or below USD 5,000 a transaction may be aggregated in the bank's or PSP's own name; payments needing export tax rebate or financing may be aggregated in the firm's name by counterparty. Declarations carry the postscript 「跨境电商」 ("cross-border e-commerce").
- [official: PRC regulator] https://www.safe.gov.cn/xiamen/file/file/20201117/2e54c8a76703447baee7773d476b5d0a.docx
- The individual annual facilitation quota itself is "每人每年等值5万美元" ("USD 50,000 equivalent per person per year"), under 《个人外汇管理办法实施细则》 第二条 (汇发〔2007〕1号). Search snippet of a SAFE-hosted copy only; not read.

J5. **Customs export modes.** GACC 2020 No.75 (pilot from 2020-07-01) added 9710 「跨境电子商务企业对企业直接出口」 ("cross-border e-commerce B2B direct export") and 9810 「跨境电子商务出口海外仓」 ("cross-border e-commerce export to overseas warehouse"), beside 9610 「跨境贸易电子商务」 ("cross-border trade e-commerce"; for 「境内个人或电子商务企业通过电子商务交易平台实现交易」, "domestic individuals or e-commerce firms trading through an e-commerce platform"). Read through 汉坤 (Han Kun) law firm's article (2022-09-07), which quotes the announcements. GACC's own pages were not read, and a press report says the 9810 overseas-warehouse filing requirement ended from 2024-12-15 (not read). [opinion: law firm quoting GACC]

J6. **Chinese accounting standard on FX (CAS 19, 企业会计准则第19号——外币折算, effective 2007-01-01)**, read via the fadada.com mirror 2026-11-10:
- 第十条 「外币交易应当在初始确认时，采用交易发生日的即期汇率将外币金额折算为记账本位币金额；也可以采用按照系统合理的方法确定的、与交易发生日即期汇率近似的汇率折算。」 ("a foreign-currency transaction is first recorded at the spot rate on the transaction date, or at a rate approximating it, set by a systematic and rational method").
- 第十一条（一） 「外币货币性项目，采用资产负债表日即期汇率折算。因资产负债表日即期汇率与初始确认时或者前一资产负债表日即期汇率不同而产生的汇兑差额，计入当期损益。」 ("foreign-currency monetary items are translated at the balance-sheet-date spot rate; differences against the initial or previous rate go to profit or loss for the period").
- The application guide (search snippet; Deloitte-hosted copy, not read) says the spot rate is normally the PBOC's published central parity, and that conversions use the bank buying or selling rate actually applied.
- [official: PRC regulator, via mirror] https://www.fadada.com/article/detail-11190

## The SP-API and report faces

Roles are from Role Mappings for SP-API Operations (`web01/role-mappings.md`, updatedAt 2026-10-28) [official, command-verified by an awk condense of that file]. Rates are from the models (default usage plans; "Selling partners whose business demands require higher throughput may have higher rate and burst values"). Sellers' apps tick Product Listing, Pricing, Brand Analytics, and Finance and Accounting. Amazon Fulfillment is being added.

| Operation | Path | Model | Rate/burst | Role (Role Mappings) | Regions | Notes |
|---|---|---|---|---|---|---|
| `listTransactions` | GET `/finances/2024-06-19/transactions` | finances_2024-06-19.json | 0.5 / 10 | Finance and Accounting | NA, EU, FE | Includes DEFERRED |
| `listBalances` | GET `/finances/2024-06-19/balances` | same | 0.5 / 10 | Finance and Accounting | NA, EU, FE | Added 2026-07-29 |
| `listSummary` | GET `/finances/2024-06-19/summary` | same | 0.5 / 10 | Finance and Accounting | NA, EU, FE | Added 2026-07-29 |
| `listFinancialEventGroups` | GET `/finances/v0/financialEventGroups` | financesV0.json | 0.5 / 30 | Finance and Accounting; AISP (EU only) | NA, EU, FE | **Not** on the removal schedule |
| `listFinancialEventsByGroupId` | GET `/finances/v0/financialEventGroups/{eventGroupId}/financialEvents` | same | 0.5 / 30 | Finance and Accounting; AISP (EU only) | NA, EU, FE | Removal 2027-08-27 |
| `listFinancialEventsByOrderId` | GET `/finances/v0/orders/{orderId}/financialEvents` | same | 0.5 / 30 | Finance and Accounting | NA, EU, FE | Removal 2027-08-27 |
| `listFinancialEvents` | GET `/finances/v0/financialEvents` | same | 0.5 / 30 | Finance and Accounting; Amazon Fulfillment (NA, FE); AISP (EU) | NA, EU, FE | Removal 2027-08-27 |
| `listPayouts` | GET `/finances/transfers/2024-06-01/payouts` | transfers_2024-06-01.json | 0.5 / 10 | Finance and Accounting | NA, EU, FE | Added 2026-07-29 |
| `listExpectedPayouts` | GET `/finances/transfers/2024-06-01/payouts/expected` | same | 0.5 / 10 | Finance and Accounting | NA, EU, FE | Added 2026-07-29 |
| `getPaymentMethods` | GET `/finances/transfers/2024-06-01/paymentMethods` | same | .5 / 30 | Finance and Accounting; AISP; PISP | **EU** | — |
| `initiatePayout` (**write, moves money**) | POST `/finances/transfers/2024-06-01/payouts` | same | 0.017 / 2 | **Finance and Accounting**; PISP | **EU** | Rate changed 2024-11-11 from 0.5/30; GA 2024-12-18 |
| Seller Wallet (12 ops) | `/finances/transfers/wallet/2024-03-01/…` | sellerWallet_2024-03-01.json | no usage-plan table in model | Reads: AISP. Writes (`createTransaction`, `createTransferSchedule`, `updateTransferSchedule`, `deleteScheduleTransaction`): AISP or PISP | NA, EU, FE | Open-banking API |
| `getRemittanceHeaders`, `getRemittance` | `/finances/remittances/2026-03-17/remittances[/{uniquePaymentId}]` | financeRemittance-2026-03-17.json | no usage-plan table | Finance and Accounting | NA, EU, FE | **"Vendors only"** |
| `getReports` (settlement V2) | GET `/reports/2021-06-30/reports?reportTypes=GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` | reports_2021-06-30.json | 0.0222 / 10 | Finance and Accounting (report type) | NA, EU, FE | — |
| Deferred Transaction Report `GET_DATE_RANGE_FINANCIAL_HOLDS_DATA` | via Reports | — | — | Finance and Accounting (report page) | — | Not on the role-mappings types page |
| Notification `TRANSACTION_UPDATE` | Notifications API | TransactionUpdateNotification.json | — | not listed on the role-mappings types page | — | SQS workflow |

### S1. Finances 2024-06-19 `listTransactions`: the transaction-level view, deferred included [official, command-verified]

- "Returns transactions for the given parameters. Financial events might not include orders from the last 48 hours. **Note:** If you want to retrieve MFN orders in the US store, do not supply the `marketplaceId` parameter."
- `postedAfter` "must be more than two minutes before the time of the request" and is "required if you do not specify a related identifier". For `postedBefore`: "If `PostedAfter` and `PostedBefore` are more than 180 days apart, the response is empty."
- `transactionStatus`:
  - `DEFERRED`: "the transaction is currently deferred".
  - `RELEASED`: "the transaction is currently released".
  - `DEFERRED_RELEASED`: "the transaction was deferred in the past, but is now released. The status of a deferred transaction is updated to `DEFERRED_RELEASED` when the transaction is released."
  - The parameter is a free string in the model (no `enum`).
- `relatedIdentifierName` filter: the model's parameter text says "`FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID` are the only `relatedIdentifier` with filtering capabilities at the moment". The 2026-07-29 release note adds "the `SETTLEMENT_ID` value … You can use this value to filter transactions by their settlement ID". **There is no `SETTLEMENT_ID` filter.** Amazon's models repo added it on 2026-10-28 (commit df7c6298, "release:SPAPI-October-2026-Release": "`FINANCIAL_EVENT_GROUP_ID`, `ORDER_ID`, and `SETTLEMENT_ID` are the only `relatedIdentifier` with filtering capabilities", with a new store value `AMAZON_FBA_FROM_ORIGIN`) and removed both on 2026-10-29 (commit db2936aa, "SPAPI October Release Finance API Rollback"); the live `listTransactions` reference (updatedAt 2026-09-10) names only `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`; the release note (updatedAt 2026-11-04) still carries the July sentence. `SETTLEMENT_ID` is a filter of `listSummary` and an identifier on `listPayouts`. [command-verified: both commit patches read from github.com, the clone and the live reference, 2026-11-10] Response `RelatedIdentifier` names are `ORDER_ID, SHIPMENT_ID, FINANCIAL_EVENT_GROUP_ID, REFUND_ID, INVOICE_ID, DISBURSEMENT_ID, TRANSFER_ID, DEFERRED_TRANSACTION_ID, RELEASE_TRANSACTION_ID, SETTLEMENT_ID`.
- Transaction fields:
  - `sellingPartnerMetadata` (`sellingPartnerId`, `accountType`, `marketplaceId`);
  - `transactionType` ("**Possible value:** `Shipment`");
  - `transactionId`, `transactionStatus`;
  - `description` (examples `Order Payment`, `Refund Order`);
  - `postedDate`, `totalAmount` (signed decimal);
  - `marketplaceDetails`, `items[]`, `contexts`, nested `breakdowns[]`.
- Contexts:
  - `DeferredContext` (`deferralReason`, `maturityDate`);
  - `PaymentsContext` (`paymentType`, `paymentMethod`, `paymentReference`, `paymentDate`);
  - `ProductContext`, `AmazonPayContext`, `BusinessContext` (`storeName` = `AMAZON_HAUL`), `TimeRangeContext`.
- Item-level identifiers: `ORDER_ADJUSTMENT_ITEM_ID, COUPON_ID, REMOVAL_SHIPMENT_ITEM_ID, TRANSACTION_ID`.
- The page caution (Get the latest transactions, updatedAt 2026-09-24): "The response will include transactions with statuses `RELEASED`, `DEFERRED`, and `DEFERRED_RELEASED`." Also: "`breakdownType` is an open-ended string; Amazon does not publish a closed list of values, and new values are added as needed."
- `nextToken`: "Note that this operation can return empty pages."
- Pitfall Amazon's own guide raises: "Determine payment transactions" (updatedAt 2026-09-09) matches a payout's transactions with `relatedIdentifierName = FINANCIAL_EVENT_GROUP_ID`, the group id, and `transactionStatus = RELEASED`. The model says a once-deferred transaction carries `DEFERRED_RELEASED` after release, and the guide does not say whether `RELEASED` also matches those. [official; the gap is seat, an open question]

### S2. Finances 2024-06-19 `listBalances` and `listSummary`: the dashboard boxes and the settlement summary [official, command-verified]

- `listBalances`: "Retrieve a balance. This balance can be a past balances at a specified date, or a current balance. Sub-balances are listed by account type and marketplace."
  - `balanceType` values: `AVAILABLE`, `RESERVED`, `ACCOUNT_LEVEL_RESERVE`, `DEFERRED`, `TOTAL`.
  - `asOfDate` gives historical ending balances.
  - `lastUpdatedTime` is "in the marketplace's local time zone" and is null for `asOfDate` queries.
  - Nested `balances[]` make up a balance.
  - The model defines no reason field for a reserve.
- `listSummary`: "Retrieve the financial summary for the specified time period or settlement period." It returns `netProceeds`, `breakdowns`, `periodStart`, `periodEnd` and `relatedIdentifiers`. Filter `relatedIdentifierName`: "The only possible value is `SETTLEMENT_ID`."
- [seat] The five balance types line up with the Payments dashboard's Total balance box (Deferred, Account Level Reserve, Funds available; C1–C2).
- **Correction (gap fill 2026-11-10):** this line used to say the model does not define `RESERVED` vs `ACCOUNT_LEVEL_RESERVE`. It does, in its enum table: `RESERVED` "is sum of Deferred and Account Level Reserved", and `ACCOUNT_LEVEL_RESERVE` is "Based on sales volume, product category, and account history". The full definitions are in I5 [command-verified].

### S3. Finances v0 `listFinancialEventGroups`: one group per settlement period or payout [official, command-verified]

- "Returns financial event groups for a given date range. Orders from the last 48 hours might not be included in financial events."
- "If `FinancialEventGroupStartedAfter` and `FinancialEventGroupStartedBefore` are more than 180 days apart, no financial event groups are returned."
- Group fields, in Amazon's words:
  - `FinancialEventGroupId`.
  - `ProcessingStatus` "indicates whether the balance of the financial event group is settled", with values `Open` and `Closed`.
  - `FundTransferStatus`: "The status of the fund transfer." A free string with no enum.
  - `OriginalTotal`: "For a closed financial group, this is the total amount of a disbursement or a charge amount. For an open financial event group, this is the current balance."
  - `ConvertedTotal`: "in the currency of the marketplace in which the funds were disbursed".
  - `FundTransferDate`: "when the disbursement or charge was initiated. Only present for closed settlements."
  - `TraceId`: "used by sellers to look up transactions externally".
  - `AccountTail`: "The account tail of the payment instrument."
  - `BeginningBalance`: "The balance at the start of the settlement period."
  - `FinancialEventGroupStart` / `End`.
- Amazon's use-case guides (updatedAt 2026-09-09):
  - "Retrieve the amount and status of a payment" filters `ProcessingStatus = Closed`: "`OriginalTotal` … provides the total amount of disbursement or charge".
  - "Retrieve your current balance" filters `Open`.
- Deferred events in v0: "Deferred events don't appear in the `listFinancialEventsByGroupId` response until they are released" (same wording for `…ByOrderId` and `listFinancialEvents`). "This operation only retrieves a group's data for the past two years."
- Money-flow events in v0:
  - `AdjustmentEvent.AdjustmentType` `ReserveEvent`: "A reserve event that is generated at the time a settlement period closes. This occurs when some money from a seller's account is held back."
  - `DebtRecoveryEvent` ("A debt payment or debt adjustment"; `DebtPayment`, `DebtPaymentFailure`, `DebtAdjustment`; `RecoveryAmount`, `OverPaymentCredit`, `ChargeInstrumentList` with `Tail` and `Amount`, and `DebtRecoveryItem` with `OriginalAmount` and `GroupBeginDate`/`GroupEndDate` of the group that holds the debt).
  - `LoanServicingEvent` (`LoanAdvance`, `LoanPayment`, `LoanRefund`).
  - `AdhocDisbursementEvent` ("For example, "Disbursed to Amazon Gift Card balance"").
  - `FailedAdhocDisbursementEvent` (e.g. `HARD_DECLINED`).
  - `TaxWithholdingEvent` (`BaseAmount`, `WithheldAmount`, period).
  - `ChargeRefundEvent` (e.g. `SubscriptionFeeCorrection`).
  - `DirectPayment` types (stored value card, private-label credit card, COD).
- Deprecations (SP-API Deprecations, updatedAt 2026-09-09): `listfinancialevents`, `listFinancialEventsByGroupId` and `listFinancialEventsByOrderId` were deprecated July 21, 2025, with removal August 27, 2027. `listFinancialEventGroups` is not listed. None is flagged `deprecated` in the model [command-verified].

### S4. Transfers 2024-06-01: payouts, the expected payout, deposit methods, and the one payout write [official, command-verified]

- Model description: "This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE." Role Mappings, however, give `listPayouts` and `listExpectedPayouts` as **NA, EU, FE** under Finance and Accounting (Role Mappings rows: "Regions | NA, EU, FE"; "Required roles (need at least one) | Finance and Accounting"), and so does the Transfers API page's role table (updatedAt 2026-09-09). The live `listPayouts` / `listExpectedPayouts` references (updatedAt 2026-09-10) still carry the model's EU-only sentence, while their `marketplaceIds` example is `ATVPDKIKX0DER` (the US store). The two Amazon texts disagree; [seat] the EU-only sentence dates from the API's 2024 EU launch and was not updated when the reads were added. Which regions answer is an open question for a live account.
- `listPayouts`:
  - "Retrieve a list of payouts for the selling partner's account. You can filter results by `marketplaceIds`, `accountType`, date range (`createdAfter` and `createdBefore`), or a specific `payoutId`… Results are grouped by the seller's account groups."
  - `Payout` fields: `id`, `currentStatus`, `statusHistory[]` (status, `lastUpdatedDate`, `failureReason`), `type` (`SCHEDULED` / `ON_DEMAND`: "Ad hoc payouts initiated by the selling partner"), `amount`, `accountTail` ("May be omitted when the configured payment instrument is invalid"), `paymentMethod` (`BANK_ACCOUNT`, `DEBIT_CARD`), `creationDate`, `paymentRail` ("The underlying payment network or clearing system"), `traceId` ("The banking network's unique identifier for a fund transfer request"), `period`, and `relatedIdentifiers` (`SETTLEMENT_ID`).
  - Statuses: `STARTED`, `IN_TRANSIT` ("sent to the bank for disbursal"), `PAID` ("successfully deposited in the bank"), `FAILED`, `CANCELLED`, `NO_PAYOUT` ("No payout is made for this settlement period").
- `listExpectedPayouts`: "Returns the upcoming expected payouts from Amazon".
  - `amount` "Can be null when no payout is expected".
  - `scheduledDate`: "The expected date when the payout would be initiated in Amazon's system".
  - Statuses: `SCHEDULED`, `DISABLED` ("Payouts have been disabled for this account"), `AT_RISK` ("The payout may fail because of an invalid deposit instrument") and `NO_PAYOUT_EXPECTED` ("The expected balance is negative, resulting in no payout").
- `getPaymentMethods`: returns `accountHolderName`, `paymentMethodId`, `tail`, `expiryDate` (cards), `countryCode`, `paymentMethodType` (`BANK_ACCOUNT`, `CARD`, `SELLER_WALLET`) and `assignmentType` (`DEFAULT_DEPOSIT_METHOD`). EU only.
- `initiatePayout`:
  - "Initiates an on-demand payout to the seller's default deposit method in Seller Central for the given `marketplaceId` and `accountType`, if eligible. You can only initiate one on-demand payout for each marketplace and account type within a 24-hour period."
  - Body: `marketplaceId` (DE, FR, IT, ES, SE, NL, PL, BE) and `accountType` ("For supported EU marketplaces, the only account type is `Standard Orders`").
  - Response `payoutReferenceId`: "The financial event group ID for a successfully initiated payout."
  - Role: Finance and Accounting **or** PISP, EU.
  - Release note 2024-12-18: Transfers API "now generally available", roles PISP, AISP or Finance and Accounting, "This API is available in the EU region." Release note 2024-11-11: rate "from 0.5 to 0.017 and updated the burst rate from 30 to 2".
  - UK and IE are not in the list.

### S5. Seller Wallet 2024-03-01: Amazon's own multi-currency account, behind open-banking roles [official, command-verified]

- Title: "The Selling Partner API for Amazon Seller Wallet Open Banking API". It "provides financial information that is relevant to a seller's Seller Wallet account. You can obtain financial events, balances, and transfer schedules for Seller Wallet accounts. You can also schedule and initiate transactions."
- Balance types: `AVAILABLE`, `LOCKED_IN`, `LOCKED_OUT`, `TOTAL`.
- Transaction statuses: `EXPIRED`, `FAILED`, `FAILED_CREDITS_APPLIED`, `IN_PROGRESS`, `PENDING_USER_APPROVAL`, `SUCCESSFUL`.
- Schedules: `DAILY`, `WEEKLY`, `BIWEEKLY`, `MONTHLY`.
- Payees: `SELF` / `THIRD_PARTY`; `TAX_AUTHORITY` is a payee entity type.
- `getTransferPreview`: "Retrieve a list of potential fees on a transaction".
- Roles: reads need AISP; writes need AISP or PISP. There is **no Finance and Accounting route** to Seller Wallet.
- Third-Party Provider Registration (updatedAt 2026-09-09):
  - AISP and PISP are "two open banking roles that are are available to licensed TPPs", "compliant with the EU's revised Payment Services Directive (PSD2)".
  - The developer must give "your organization identifier (`orgID`), which is issued by the national competent authority". Open-banking calls need `x-amzn-psd2-certificate`, `x-amzn-content-digest`, `Signature-Input` and `Signature` headers.
  - "The AISP and PISP roles are available in the following Amazon stores: ES, UK, FR, BE, NL, DE, IT, SE, and PL."
  - https://developer-docs.amazon/sp-api/docs/tpp-registration.md
- Release notes: private beta 2025-04-30; "publicly available in the NA and EU regions" 2025-08-27; `payeeContactInformation` "required when the `bankAccountOwnershipType` … is set to `THIRD_PARTY`" (2025-12-03).

### S6. Finance Remittance 2026-03-17: vendor payments, not seller payouts [official]

- Finance Remittance API page (updatedAt 2026-09-30): "programmatic access to **vendor** payment remittance data … the same data available on the **Payments** > **Remittance** view in Vendor Central". Availability: "Vendors only".
- What a remittance is, in Amazon's terms: a payment Amazon made to a vendor ("payment date, total amount paid, unique payment ID, payment number, payment method, and payment status"), with line items per invoice ("the invoiced amount, the amount paid, the transaction type, any terms discount taken, and the net amount transferred per invoice").
- Filters: `startDate` minimum one year ago; maximum 90-day range; default 30 days.
- Role: Finance and Accounting (NA, EU, FE).
- A seller account has no remittances in this sense. [seat]
- The Invoices API v2026-06-25 (`/finances/invoices/…`) page also says "Vendors only" / "available for vendors" (updatedAt 2026-09-09).

### S7. Reports [official]

- **Settlement reports** (updatedAt 2026-10-14): "Settlement reports cannot be requested or scheduled. They are automatically scheduled by Amazon. You can search for these reports using the `getReports` operation."
  - `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` (Finance and Accounting) "replaces the Flat File Settlement Report and XML Settlement Report".
  - Columns: settlement-id, settlement-start-date, settlement-end-date, deposit-date, total-amount, currency, transaction-type, order-id, merchant-order-id, adjustment-id, shipment-id, marketplace-name, amount-type, amount-description, amount, fulfillment-id, posted-date, posted-date-time, order-item-code, merchant-order-item-id, merchant-adjustment-item-id, sku, quantity-purchased, promotion-id.
  - "amounts are displayed in local currency formats (for example, `95,00` for EU instead of `95.00`)."
  - The deprecated `…FLAT_FILE` (roles Amazon Fulfillment or Finance and Accounting; role-mappings-for-types, updatedAt 2026-09-09) and `…XML` are removed **2026-11-11** (SP-API Deprecations).
  - Retention: `getReports` `createdSince` "The default is 90 days ago. Reports are retained for a maximum of 90 days" (reports model, via listing playbook report-lifecycle.md D, read 2026-10-14).
  - Since 2021: "only transactions which have been disbursed will be included in the Settlement reports" (C4).
- **Deferred Transaction Report** `GET_DATE_RANGE_FINANCIAL_HOLDS_DATA` (Payment Reports, updatedAt 2026-09-09):
  - "A point-in-time report that contains a list of deferred transactions. A single report can provide up to 10 years of data."
  - "You must request the Deferred Transaction Report through the **Payments Reports Repository** on Seller Central before you can use the Reports v2021-06-30 API to retrieve the Deferred Transaction Report."
  - Columns: ReportType, date/time, settlement-id, type, order-id, sku, description, quantity, store, fulfillment, order-city, order-state, order-post-code, tax-collection-model, product-sales, product-sales-tax, shipping-credits, shipping-credits-tax, gift-wrap-credits, gift-wrap-credits-tax, regulatory-fee, tax-on-regulatory-fee, promotional-rebate, promotional-rebate-tax, marketplace-withheld-tax, selling-fees, fba-fees, other-transaction-fees, other, total, Tax Amount, Total Amount.
  - Role: Finance and Accounting. https://developer-docs.amazon/sp-api/docs/report-type-values-payment.md

### S8. Notifications [official, command-verified]

- `TRANSACTION_UPDATE`: "Sellers can subscribe to this notification." It "is sent whenever there is a new transaction posted to the seller's account". It supports `filterExpression`. Workflow: Amazon SQS.
  - Payload: `SellingPartnerMetadata` (`SellingPartnerId`, `AccountType`, e.g. `PAYABLE`; `MarketplaceId`), `RelatedIdentifiers`, `TransactionType`, `PostedDate`, `TotalAmount`.
  - The docs table types `CurrencyAmount` as **`int`**, while Finances amounts are signed decimals.
  - The type is **not** on the Role Mappings for SP-API Types page (updatedAt 2026-09-09) [command-verified].
  - It carries no status (deferred or released) and no balance. https://developer-docs.amazon/sp-api/docs/notification-type-values.md (updatedAt 2026-10-28)
- No other notification type in the docs or the models' `schemas/notifications` (26 files) carries a payout, balance, reserve or deferral event [command-verified, by listing].

### S9. Data Kiosk

- No Data Kiosk schema carries settlement, payout, reserve or deferral detail. The economics dataset counts sales and fees, not cash timing. **Correction:** `analytics_sellerAnalytics_2025_03_31.graphql` has a `Lending` metric group with `disbursements` ("Total monetary amount disbursed to the seller from Amazon for sales and other transactions") and `totalBalanceByStandardOrders` ("Total balance amount generated from standard order transactions"); the group is gated by the PAAM right `analytics_sales_and_lending_view`, which Role Mappings do not map to a seller role, so nothing is built on it. [command-verified: grep over `schemas/data-kiosk`, 2026-11-10; method/finance-surface.md agrees]
- The Economics dataset's role is open: Role Mappings and the Data Kiosk page say Brand Analytics for every operation, while Amazon's "Correction: Data Kiosk role requirements" (2024-07-02, https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements, re-read 2026-11-10) says "The Economics dataset requires the Selling Partner Insights role."

### S10. Borrowing

Amazon's own Claude plugin "Amazon Selling Partner" 1.0.0 has no payments or settlement skill. Its seller-analytics skill rules out "tax/financial-settlement reporting" [command-verified, `amazon-plugin-zip/skills/seller-analytics/SKILL.md`]. No pi package for this was found. The ERPs and accounting tools below compute this view, each by its own method.

## What practitioners add

**Accounting and reconciliation tools (English)** [opinion]

- **A2X.**
  - Reserves:
    - "The Current Reserve Amount should be allocated to the suspense account"; when released it appears as "Previous Reserve Amount Balance which you also code to the suspense account" (Denym Bird, 2016-12-12). https://www.a2xaccounting.com/blog/amazon-reserve-amounts-what-to-do-when-amazon-withholds-your-settlement-payment
    - Now mapped to an "'Amazon Reserved Balances' current asset account"; "You may have a reserve balance if there is a validation issue with your bank account" (Elspeth Cordray, updated 2025-02-28). https://a2xaccounting.com/ecommerce-accounting-hub/amazon-reserve-balances
  - Split-month settlements: "A2X uses a Carried Forward Balance to bridge the gap between split months". A negative settlement posts as a draft bill matched to the card charge (support, 2026-07-01). https://support.a2xaccounting.com/en/articles/959836-how-to-reconcile-amazon-settlements-in-xero
  - Currency: "a settlement from Amazon.fr will always be in EUROS". https://support.a2xaccounting.com/en/articles/2318063
  - DD+7:
    - 2024-11-07: "A2X does not include deferred transactions, as Amazon's API does not provide this deferred transaction data". That statement predates the `DEFERRED` status and filter (2025).
    - 2025-08-18 (Geoffrey Gualano): "Those 'Deferred Transactions' don't appear in the settlement file until the cash actually moves." The add-on "accrues Deferred Transactions during the period and reverses any Amazon orders released in the following period". The article puts the held-back share of revenue at 20–25% (vendor's figure).
    - https://www.a2xaccounting.com/ecommerce-accounting-hub/amazon-dd-7-deferred-transactions-accounting-challenges-and-a2x-workarounds
  - Name trap: "Payable to Amazon" and "Successful Charge" exist in **Amazon Pay** settlements (2023-05-09). Similar names appear in Seller Central.
- **Link My Books** (help pages 2026):
  - Reserve lines "Amazon Reserved Balances - Current Reserve Amount" / "Previous Reserve Amount Balance".
  - "If a settlement payout fails, Amazon rolls the same amount into the next settlement" ("Failed to transfer funds").
  - Small negative balances below roughly 20 GBP/USD/EUR tend to roll forward instead of being charged. The lines named are "Repayment of negative Amazon Balance", "Successful charge" and "Cross-debt adjustment" / "Cross-marketplace adjustment".
  - Seller Wallet: "Enrolling in Seller Wallet does not change your settlement cycle"; "Amazon no longer converts at the point of settlement".
  - Deferred add-on: "identifies orders placed this month but not yet settled, directly from Amazon's API data", booked to an "Amazon Deferred Balances" asset; "Real + Released = zero".
  - Account Level Reserve has no formula; record it "as a receivable asset" (Dan Little, 2026-07-14).
  - Pages: help.linkmybooks.com articles 4184943, 5738830, 4096645, 16553034; https://linkmybooks.com/amazon-deferred-payments
- **Synder** (2024-11-18, modified 2026-04-10): Amazon labels the same item "Account Level Reserve(s) / Unavailable Balance(s)/ Current/Previous Reserve Amount(s)". The current reserve is a negative amount in the report. Pitfall: "the sync of the balance reserve can fail, since the 'from' and 'to' accounts must be in the same currency." https://synder.com/help/per-transaction-sync-synchronizing-amazon-account-level-reserves/
- **Webgility** (Parag Mamnani, 2026-09-09): "Money Amazon is holding from you (reserves) never makes it into your books". Its toggle posts withheld reserves as an expense and released reserves as a deposit. That is an expense treatment; A2X, LMB and Synder use the balance sheet. https://www.webgility.com/blog/amazon-reconciliation-in-quickbooks
- **Bookkeep**: daily journals "book each sale when Amazon defers it, about a week earlier"; "The difference is the change in your Deferred Balance over the period"; the reserve line "represents the change to the reserve balance and not the current reserve balance". https://bookkeep.com/docs/apps/amazon/matching-your-amazon-seller-payouts-to-amazon-reporting
- **Taxomate** (Jon Hainstock, 2026-08-10): "Always reconcile to your actual bank deposit, not the expected amount from reports." https://taxomate.com/blog/amazon-seller-accounting
- **Elver** (Oliver Blackmore, 2026-05-27): when the clearing account does not zero, causes include "A reserve that was not coded as a receivable", "A currency conversion difference", and "A loan repayment deducted by Amazon but not recorded". https://www.elverecommerceaccountants.co.uk/?p=4966
- **Improvado** (connector notice, 2026-09): "Amazon is removing the flat file behind the Payment All Statements report on 11 November 2026". V2 is not a drop-in swap. https://improvado.io/product-updates/connectors/amazon-seller-central-settlement-report-sunset

**Advances and financing** [opinion]

- **Payability Instant Access**: "Each day we advance 80% of your previous day's payouts into your Payability account. The remaining 20% is made available once the marketplace payout is received." https://www.payability.com/instant-access/
  - Its blog (Peter Murray, 2022-03-10): "Tier II … holds 3% of their daily processed payments over a 28-day average". https://www.payability.com/blog/account-level-reserve-amazon/
- **SellersFi** (updated 2025-01-09): the same tiers ("3% of your daily processed payments averaged over the past 28 days"). https://sellersfi.com/resources/blog/account-level-reserve-amazon/
- **Caution on the tiers.** The tier rules above are the vendors' claims. No Seller Central text read states them, and Amazon staff give a sum of per-order holds by reason instead (B2). A helper seat reports that the tiers match Amazon Pay's published reserve tiers; this seat did not verify that. An Amazon forum representative wrote that the reserve "is placed on all accounts, regardless of their performance" and is "based on a number of factors, including your business, and your processing history". https://sellercentral-europe.amazon.com/seller-forums/discussions/t/23a8587a-a412-4190-a995-e74f29fe4c49
- **8fig** glossary: "Earnings accumulate for 14 days before being released". https://www.8fig.co/glossary/amazon-payouts
- **Amazon/Parafin cash advance** (deBanked, 2023-10-29, quoting Amazon): "Payment is deducted from your bank account based on your current Amazon disbursement schedule … a fixed percentage of monthly sales." https://debanked.com/?p=201072
- Clearco and Wayflyer: no primary page found.

**DD+7 practitioners (English)** [opinion]

- EcomCrew (Alexa Alix, updated 2026-05-24): 14–27 days from order to bank for FBA and 20–35 for FBM; $10k a day of sales means about $70k held. https://www.ecomcrew.com/amazon-dd7-payment-policy-update-leaves-sellers-waiting-longer/
- Riverbend Consulting (Christian Rodgers, 2026-03-19): DD+7 makes sellers "short-term lenders to Amazon". https://riverbendconsulting.com/blog/dd7-amazon-payout-policy/
- MyAmazonGuy (Steven Pope, 2026-05-25): changing bank details "can trigger a temporary security hold". https://myamazonguy.com/selling-on-amazon/amazon-seller-payment-schedule/
- MyAmazonGuy (2026-09-28) on the new "Finance Workspace": Statement View moved to "Manage payments", and the balance is split into Available, Deferred and Account Level Reserve. https://myamazonguy.com/news/amazon-finance-workspace/
- Seller forums: on migration day one seller saw the whole balance in ALR for about 48 hours. Others report ALR holds of months.

**Chinese sources** [opinion unless marked]

- **DD+7 2026 in trade press.**
  - AMZ123 (2026-01-28) says 「亚马逊官宣自2026年3月12日起，在全球所有站点对全量卖家统一执行DD+7」 ("Amazon announced that from 2026-03-12 it applies DD+7 to all sellers on all marketplaces"). Amazon's own email says "Most Amazon sellers worldwide already use DD+7", which reads as a migration of the remaining accounts, not a new worldwide rule.
  - Money path given: 「发货→暂扣（延迟交易金额）→妥投→转入储备金→妥投满 7 天→转为可用余额→自动结算 / 按需付款提现」 ("ship → held as deferred transactions → delivered → moved to reserve → 7 days after delivery → available balance → automatic settlement / on-demand withdrawal"). 「是延迟回款而非扣减货款」 ("a delay in payout, not a deduction"). https://www.amz123.com/t/5bJ2W1nh
  - AMZ123 (2026-03-10): 「自2026年3月5日起在全球范围内（德国站为3月12日）」 ("from 2026-03-05 worldwide; 2026-03-12 for Germany").
- **Statement change** (雨果网, 2026-04-23):
  - 「旧账单：只显示 已结算（Released）订单」 ("the old statement showed only Released orders").
  - 「新账单：显示所有出单（Posted），包含已释放 + 延迟两部分」 ("the new statement shows all Posted orders, Released plus Deferred").
  - FBM: 「物流时效 + 妥投 + 7 天 → 回款周期明显拉长」 ("transit time + delivery + 7 days; the payout cycle is clearly longer").
  - https://www.cifnews.com/article/185409
- **Pre-2026 rules** (雨果网, 2023-04-04): 「你可以每24小时使用一次请求转账回款功能」 ("you can request a transfer once every 24 hours"). Using it pushes the next scheduled payout 14 days later. https://www.cifnews.com/article/142821
- **Old reserve rule** (雨果网, 2022-01-19, author's account): new sellers 「预留金额为账户内所有余额」 ("the reserve is the whole balance"). Established sellers: the higher of 「过去7天的所有销售额」 ("all sales of the past 7 days") or 「过去28天销售总额5%」 ("5% of the past 28 days' sales"). Europe: 「可以选择每 24 小时获得一次款项」 ("can choose to be paid every 24 hours"). Not Amazon's words; old. https://www.cifnews.com/article/115583
- **Seller pitfalls (知无不言 wearesellers.com):**
  - The whole balance reserved, so ads go to the card daily; the reserve grew 「从一万二，变二万二了」 ("from 12k to 22k") (question 79865).
  - A residual UK ALR of £24.99 with no orders blocks closing the site (96384).
  - The request-transfer button disappeared, said to be 「系统判定的」 ("decided by the system") (30398).
  - EU deposit-method verification failed with both WorldFirst and LianLian (105791).
  - A claim that card payment of ads ends 2026-04-15 (118398). Amazon Ads' own text limits that change to a small contacted group and defers it to 2026-08-01 (G4).
- **Reconciliation identity** (跨境知道, written by 积加 Gerpgo, 2023-05-16): 「应收账款余额 = 账户预留余额 + 净收入额」 ("receivable balance = reserve balance + net proceeds"); 「卖家需要考虑到时区差因素」 ("sellers must account for the time-zone difference"). https://www.ikjzd.com/articles/1658378894475730945
- **领星 Lingxing**:
  - Settlement Center: 「接入亚马逊财务API接口」 ("connects to Amazon's finance API").
  - Formulas: 「本期结算=收入+退款+支出」 ("this period's settlement = income + refunds + expenses") and 「应收金额=期初余额+本期结算+信用卡扣款+预留退回+本期预留」 ("receivable = opening balance + this period's settlement + credit-card debits + reserve released + this period's reserve").
  - Statuses Open → 待结算 ("unsettled"), Close → 已结算 ("settled"), then 已转账 ("transferred"). Arrival matched by 「店铺＋收款账号后三位+金额」 ("store + last three digits of the receiving account + amount").
  - 「目前结算中心仅同步最近3个月数据」 ("the Settlement Center currently syncs only the last 3 months").
  - FX: 「结算汇总的汇率取值的是结算开始时间对应月份的月初汇率」 ("the settlement summary uses the month-start rate of the month in which the settlement began").
  - 「转账失败的亚马逊一般会在3~5天再次回款」 ("after a failed transfer Amazon usually pays again in 3–5 days").
  - Scheduled automatic withdrawal: 「每月、每周乃至每天定时自动提现」 ("scheduled automatic withdrawals monthly, weekly or even daily"). Note that this is an ERP clicking Seller Central's button, not an API in NA.
  - Profit report bases: by settlement time (default), settlement plus 「预结算」 ("pre-settlement", off by default), or by ship time. 「亚马逊发生延迟放款或 DD+7 等政策变化时，利润仍归属订单发货月份，但实际到账时间可能延后」 ("under delayed release or DD+7, profit stays in the ship month but the cash may arrive later").
  - Release V3.7.0 (2025-10-17): 「延迟结算预估结算时间接入亚马逊接口」 ("estimated release time for deferred settlement now comes from Amazon's API").
  - https://www.lingxing.com/help/article/SettlementCenter ; …/jiesuanzhongxin ; …/ProfitStatementnew ; …/Update264
- **积加 Gerpgo** (2022 press): syncs 「亚马逊卖家中心->数据报告->付款报告数据」 ("Seller Central → Reports → Payments report data") daily at about 03:00. Its 销售回款分析 ("sales payout analysis") panel shows settled and unsettled reserve amounts. https://news.pedaily.cn/20220316/31804.shtml
- **赛狐 SellFox**: 「预留资金会在下一个14天结算周期发放」 ("reserve funds are paid out in the next 14-day settlement cycle"); linked collection tools reconcile automatically. https://www.sellfox.com/help/solution/how-to-track-and-monito-payment-collection
- **易仓**: 「完成新版财务接口适配」 ("adapted to the new finance API") (2026-06-10). 马帮, 店小秘 and 通途: no payout documentation found. 紫鸟 is a browser, not a finance tool.
- **Amazon-credited promotion pieces** (雨果网 2025-07-17 and 2026-02-27, from the 亚马逊全球开店 account):
  - A Seller Wallet example pays a US supplier in USD 「不用换汇，连手续费都是0」 ("no currency conversion, and even the fee is zero").
  - Enterprise ACCS needs 中国对外贸易经营权 (China foreign-trade operating rights).
  - Sellers' pains: 「回款到账时效不确定」 ("unpredictable payout timing") and 「实际到账金额总与后台显示有偏差」 ("the amount that arrives always differs from what the dashboard shows").
  - https://www.cifnews.com/article/176665 ; …/183741

**Payment providers** [opinion; their fees are in Facts for human readers only]

- **Payoneer**: "local receiving account details in the currencies Amazon pays out in"; funds arrive "within one to two business days" after the marketplace sends them. https://www.payoneer.com/ecommerce-sellers/
- **WorldFirst**: "certified participant in Amazon's Payment Service Provider Program (PSPP)". A payee bank account in the seller's own name is required ("Amazon will stop the disbursement of your funds"). Amazon's verification comes "within 48 to 72 hours". https://www.worldfirst.com/global/user-guide/receiving-payments/amazon
- **PingPong** (2026-09/10): ACCS converts automatically on arrival, so the seller cannot choose when to convert. A collection provider cannot speed up DD+7 release. https://www.pingpongx.com/zh/news/articles/26091116571864
- **Airwallex**: a Chinese blog (2026-02-25) says sale to available funds 「往往会拉长到 10–12 天甚至更久」 ("often stretches to 10–12 days or more"); it cites no Amazon notice.
- **LianLian**: no Amazon rate published.
- Providers call themselves 亚马逊 SPN 认证服务商 ("Amazon SPN-certified provider"); Amazon's own term for the program is PSP.

**The CNY leg (gap fill 2026-11-10)** [opinion]
- **PingPong**, 「亚马逊收款方式哪种好？官方收款 vs 第三方平台全对比（2026）」 (page timestamp 2026-09-11; read ✓):
  - Reproduces ACCS CNY tiers on 「近 12 个月跨币种净收入」 ("cross-currency net proceeds over the past 12 months"), the same five steps as Amazon's guidebook snippet (figures in Facts for human readers only).
  - ACCS is 「强制自动换汇，资金到账时就完成币种转换，卖家无法持有外币、不能自主择时结汇」 ("forced automatic conversion on arrival; the seller cannot hold foreign currency or pick when to convert").
  - A PSP lets the seller hold USD/EUR/GBP/JPY and pay VAT, freight and suppliers from it, avoiding a convert-then-buy-back round trip. It offers 「对公结汇，贸易材料留存，适配 9810/0110 出口退税」 ("corporate conversion with trade records kept, suited to 9810/0110 export tax rebate").
  - "A collection provider cannot speed up DD+7 release" (already cited above).
  - A vendor comparing itself with ACCS. https://www.pingpongx.com/zh/news/articles/26091116571864
- **WorldFirst (万里汇) CN pricing page** (read ✓):
  - 「什么是人民币结汇额度？根据监管机构对于跨境交易的相关规定，贸易相关跨境收支均需要真实、合法的交易背景，人民币额度为经审核具有真实合法贸易背景的金额，您需先上传交易明细申请人民币额度才可完成人民币结汇。」 ("What is the CNY conversion quota? Under the regulators' rules every trade-related cross-border flow needs a genuine, lawful trade background; the CNY quota is the amount verified as having one; you must upload transaction details to apply for quota before converting to CNY").
  - 「对标市场汇率，真正实现 0 汇损」 ("benchmarked to the market rate, zero FX loss"; a vendor claim).
  - https://www.worldfirst.com.cn/cn/pricing/
- **PingPong help centre** lists 「为什么要提供店铺授权信息？」 ("why provide store authorisation?") and a 一般贸易提现 ("general-trade withdrawal") flow that needs customs declarations and logistics documents and pays only to a same-name corporate account. Both were seen as search snippets only; the help pages answer HTTP 412 to `curl`.
- AMZ123 Q&A pages (2024) repeat the PSP practice: a company may withdraw to its corporate account or to the legal representative's personal account; an individual registrant withdraws to their own account. These are community answers, not providers' terms. https://www.amz123.com/ask/6FRsSPbG (snippet)
- **Booking-rate practice.** An AMZ123 Q&A (2024-05-18) gives the common bookkeeping method: book at the PBOC rate of the 1st of the month, put the bank-conversion difference to exchange gain or loss at once, and revalue foreign-currency receivables and bank balances at month-end. It also notes the other method, the transaction-day rate. CAS 19 (J6) allows both: the spot rate or a systematic approximation. Lingxing's month-start rate (P-flow-33) is one such approximation. https://www.amz123.com/ask/VrFfga6p
- **Listed sellers' FX lines** (AMZ123 headline piece, 2026-11): 三态股份 (Santai) reports a CNY 30.98m exchange loss for the first three quarters of 2026; 乐歌 (Loctek) CNY 77.84m in H1; and 「人民币兑美元一度摸到6.6682」 ("CNY/USD touched 6.6682 at one point") on 2026-10-26. These show that the FX line can be the size of operating profit for China-based sellers. Figures as reported by the article, not checked against the filings. https://www.amz123.com/t/1WA9bAge

**Held funds (gap fill 2026-11-10)** [opinion / research]
- **Court-ordered freezes (TRO, Schedule A).** 中伦 (Zhong Lun law firm), 「从TRO到反向TRO：中国跨境电商的美国临时限制令应对与反制」 (中伦深度观察 2026-10, read ✓):
  - A TRO under FRCP 65 is ex parte. 「TRO一经签发，电商平台及支付机构必须立即配合执行下架产品、冻结账户」 ("once issued, platforms and payment providers must take down products and freeze accounts at once"). It lasts up to 14 days, extendable once, and is usually followed by a preliminary injunction that keeps the freeze until judgment.
  - Under Schedule A the defendant list is sealed, so the seller learns of the suit from the freeze.
  - Defaulting sellers' frozen funds 「最终被判归原告所有」 ("are finally awarded to the plaintiff").
  - The Second Circuit's 2025-12 "Baby Shark" ruling bars email-only service on defendants in China.
  - It cites 中国知识产权研究会 (2025-05) for the share of US cross-border e-commerce cases with a TRO (figure in Facts for human readers only).
  - https://www.zhonglun.com/research/articles/56066.html
- **Is permanent withholding enforceable?** Arbitrators have split on BSA §2 under Washington law. Some awards struck the permanent-withholding clause as an unenforceable penalty, and others upheld it. New York's Appellate Division, First Department (Matter of Mariana Trading Inc. v Amazon.com Servs., LLC, 2024) held that an arbitrator's rejection of the penalty argument was not a manifest disregard of the law. A seller-advocacy firm (AMZ Sellers Attorney) reports an AAA award of 2026-08-05 striking §2. [research: court records, read as search snippets only (justia.com and nycourts.gov refused `curl`); the 2026 award is unverified]
- **UK KYC holds.** ChannelX (Chris Dawson, 2026-02-01), "Are you impacted by Amazon KYC with disbursements held?": UK sellers report "All fund disbursements were withheld due to an ongoing business/KYC verification review (since September 2025)", with accounts "selling as normal" while no payout is made, for more than a quarter in some cases. https://channelx.world/2026/02/are-you-impacted-by-amazon-kyc-with-disbursements-held/
- **Seller reports.** Funds still held after the waiting period even with identity verified (EU forum); no reply to the appeals address (several threads); Chinese community pages describe a funds-appeal video interview with the legal representative showing original licence and ID. These are seller reports (AMZ123 search snippets 2024–2026; EU forum 64a7c91b, 2020).

## Published research

None found on Amazon seller payout timing, reserves or DD+7. The only quantitative statements are vendors' (the A2X 20–25% deferred share, the EcomCrew day ranges).

## Stable enough for a skill

1. The states of a sale's money, in Amazon's words: shipped → deferred → delivered → reserve period → released into the balance → available (net of Account Level Reserve) → disbursed (settlement cycle or on demand) → bank. The days each step takes are read at run time.
2. A reserve period runs from the delivery date, for FBA and FBM alike; its length is read at run time. Delivery date: actual, with an integrated carrier or tracking; latest EDD without. It can be extended on risk and performance, and Amazon names no exemption.
3. Only released transactions are paid in a settlement, and settlement reports carry only disbursed transactions.
4. The Account Level Reserve is, in Amazon's own description, a sum of per-order holds by reason: delivery-date reserve (transitional), open A-to-z claims, chargebacks in the last 90 days, performance below benchmarks, account under review, local income-tax withholding. Amazon gives no percentage and no timeframe. The reason shows on Statement View.
5. The schedule is set by contract, "or at our option, more frequent", and may vary by store; its length is read at run time. The reserve carries into the next period's beginning balance.
6. On-demand payouts go by different names and rules by store (Disburse on Demand, Disburse Now, `initiatePayout`, Express Payout); which apply to the seller's store, how often and with what limits is read at run time.
7. Invoiced (Amazon Business) orders are deferred until the buyer pays, at the latest a set time past due (read at run time). In the US they are a separate account row and are paid by a separate entity.
8. A negative balance at a period's end is charged to the card on file, retried as often as every 24 hours. In the API it is a `DebtRecoveryEvent` and an expected payout `NO_PAYOUT_EXPECTED`.
9. Each store settles in its own currency. `OriginalTotal` is in the store's currency and `ConvertedTotal` in the disbursed currency. ACCS converts at the provider's rate on the day the transfer is initiated (the re-initiation day for a failed one).
10. A third-party payment provider must be in Amazon's PSP Program (since 2021-07-15).
11. API facts: what each operation returns (S1–S8), the posting lag, date-window and two-minute limits the models state (their values read at run time), empty pages, v0 hiding deferred events, settlement reports cannot be requested and are kept for a limited time (read at run time), the Deferred Transaction Report must first be requested in Seller Central, and the removal dates (settlement V1 2026-11-11; v0 events 2027-08-27).
12. Roles: every read here is Finance and Accounting. Seller Wallet is AISP/PISP only, and those are licensed open-banking roles. Finance Remittance and Invoices v2026-06-25 are vendor APIs.
13. Held funds (§I):
    - Amazon's contract lets it withhold payments while it judges a risk persists, offset what it says is owed, and permanently withhold where it finds deceptive, fraudulent or illegal activity or repeated violations. In the EU this includes "any other account that you have operated", from 2024-07-12.
    - Under the Funds Disbursement Eligibility policy (renamed 2024-10), a deactivated seller can appeal for funds after a waiting period Amazon shortened in 2024-10 (its length read at run time). Amazon releases what remains less offsets after checking for fraud and confirming identity.
    - Reviews under §3 and identity verification also hold disbursements.
    - The API shows only the effect (`DISABLED`, no payout, balance types), never the reason.
14. The CNY leg (§J):
    - ACCS CNY puts the fee inside the exchange rate, converts on arrival, and pays a domestic account through a licensed Chinese processor.
    - A PSP route adds the PSP's own conversion under SAFE's rules: trade-authenticity checks on transaction data, a conversion deadline, a disclosed bank rate, a per-transaction ceiling in principle, and individuals' e-commerce conversions kept outside the annual quota when backed by transaction data (the deadline, ceiling and quota read at run time).
    - SAFE allows overseas costs to be netted against export proceeds, and overseas-warehouse sales income to differ from the declared export value.
15. Where an FX difference can arise, as rates are applied: the store-to-payout-currency conversion (ACCS, or a PSP's account currency); the PSP's conversion to CNY; and the gap between the rate a seller books (CAS 19: the spot or an approximate rate) and the rate actually received. Which rate is booked is the seller's choice.
16. ZA, EG and TR settle in ZAR, EGP and TRY; VAT on their fees is read at run time. IE and BE are EUR stores in the European unified account.

## What cx must read at run time

| Moving figure or state | Where it is read |
|---|---|
| Balance by bucket (available, reserved, ALR, deferred, total), per store and account type; history via `asOfDate` | `listBalances` |
| Which transactions are deferred, why (`deferralReason`) and when they release (`maturityDate`) | `listTransactions?transactionStatus=DEFERRED`; Deferred Transaction Report (after a Seller Central request) |
| What a payout contained | `listTransactions` by `FINANCIAL_EVENT_GROUP_ID` ; `listSummary` by `SETTLEMENT_ID`; `listPayouts` (its `relatedIdentifiers` carry `SETTLEMENT_ID`); settlement V2 via `getReports` |
| Settlement periods, payout amount, converted amount, trace id, account tail, beginning balance | `listFinancialEventGroups`; `listPayouts` |
| Next payout date and amount, at-risk or disabled state, negative expected balance | `listExpectedPayouts` |
| Payout status and failure reason | `listPayouts` `statusHistory` |
| Deposit methods and card expiry (EU only) | `getPaymentMethods` |
| Reserve events, debt recovery and card charges, loan repayments, tax withholding, ad hoc disbursements | v0 events by group (until 2027-08-27) or `listTransactions` descriptions and breakdowns |
| The seller's reserve period (DD+7 or extended), reserve reasons, Disburse on Demand / Express Payout eligibility | Seller Central only (Statement View); the API shows the effect, not the setting |
| ACCS rate actually applied | `OriginalTotal` vs `ConvertedTotal` per group; the seller's bank statement |
| Fees for currency conversion and payout services | The provider's or Amazon's page on the day; never a remembered figure |
| Whether payouts are disabled or at risk (held account, invalid deposit method) | `listExpectedPayouts` status (`DISABLED`, `AT_RISK`); `listPayouts` `statusHistory.failureReason` |
| Where a withheld balance sits (available, reserve, or elsewhere) and whether it changes over a hold | `listBalances` over time (`asOfDate`), compared with Seller Central's banner and notice; Amazon names no bucket for it |
| ACCS CNY rate applied to a payout, fee included | Seller Central Payments overview (hover on the converted amount); `OriginalTotal` vs `ConvertedTotal`; the bank's credit advice |
| A PSP's conversion rate, spread and CNY quota | The PSP's own statement or portal (outside Amazon); the partner bank's quoted rate it must disclose (SAFE 2019 No.13 art. 27) |
| PBOC central parity for a date (the usual "spot rate" for booking) | CFETS / PBOC publication on the day; never a remembered figure |
| Currency, VAT on fees and promotions for ZA, EG, TR, IE, BE | Each store's fee page and Seller Central fee schedule on the day |
| Which filters and values `listTransactions` accepts today | The model and live reference (`FINANCIAL_EVENT_GROUP_ID`, `ORDER_ID` only, 2026-11-10); the release note's `SETTLEMENT_ID` filter was rolled back |
| Reserve period applied to each sale (default DD+7, extended on risk; US, EU, BR, read 2026-11-10) | `maturityDate` in `listTransactions` (`DeferredContext`); the account setting on Seller Central's Statement View |
| Days from payout to bank (US, CA, AE, SA, AU pages "up to five business days"; IN 2–3 working days; ACCS CNY 1–3; read 2026-11-09/10) | `listPayouts` `statusHistory` (`IN_TRANSIT` to `PAID`) |
| Settlement cadence for the store (NA contract 14 days; JP every two weeks; IN every 7 days; TR every 14 days; read 2026-11-10) | `FinancialEventGroupStart` / `End` in `listFinancialEventGroups`; `scheduledDate` in `listExpectedPayouts` |
| On-demand payout availability, frequency and limits (US Disburse on Demand once per 24 hours; `initiatePayout` EU8, once per store and account type per 24 hours; Express Payout US, at most USD 1 million) | transfers_2024-06-01 model and Transfers API page (https://developer-docs.amazon/sp-api/docs/transfers-api.md); Get paid faster with Express Payout (https://sell.amazon.com/blog/express-payout); Seller Central for Disburse on Demand / Disburse Now |
| Invoiced-order release (on payment, at the latest seven days past due; US, 2025-05-23) | `maturityDate` with `deferralReason` `B2B` in `listTransactions`; How Amazon Business invoices work for sellers (https://sell.amazon.com/blog/amazon-business-invoice) |
| Finances API limits (48-hour lag, 180-day window, two-minute rule, two-year v0 coverage) and settlement-report retention (90 days), read 2026-11-10 | Parameter and operation descriptions in finances_2024-06-19.json, financesV0.json and reports_2021-06-30.json (`getReports` `createdSince`), and the live references |
| Waiting period before a deactivated seller's funds appeal (60 days since 2024-10, 90 before) | Fund Disbursement Eligibility Policy (EU PDF, https://m.media-amazon.com/images/G/02/Program_Policy/Fund_Disbursement_Eligibility_Policy.pdf); US: News_Amazon 2024-09-24 only |
| SAFE PSP rules (T+1 conversion; USD 50,000 per transaction in principle; individual annual quota USD 50,000), read 2026-11-10 | SAFE 汇发〔2019〕13号 (https://www.gov.cn/gongbao/content/2019/content_5428473.htm); SAFE 汇发〔2020〕11号; the annual quota from 个人外汇管理办法实施细则 art. 2, snippet only |

## What only Seller Central shows

| Item | Any API? |
|---|---|
| The reason for each Account Level Reserve amount (Statement View) | No. `listBalances` gives the amount only; there is no reason field [command-verified]. |
| The reserve period applied to the account (DD+7 or extended) | No. Only per-transaction `maturityDate` reveals it, in effect. |
| Request Payment / Disburse on Demand (US) and Disburse Now (EU, UK) | EU8 only: `initiatePayout` (Finance and Accounting or PISP). UK, IE, NA, FE: no. |
| Express Payout enrolment | No. |
| Adding or changing a deposit method or the card on file; Currency Conversion Payment Agreement; ACCS enrolment | No (`getPaymentMethods` reads, EU only). |
| Requesting the Deferred Transaction Report and Date Range reports | Request: no. The Deferred Transaction Report can then be fetched by `getReports` / `getReportDocument`. |
| Seller Wallet enrolment, wallet balance and transfers | API exists, but only for licensed open-banking TPPs (AISP/PISP). A seller's own app has no route. |
| The disbursement-appeals route for deactivated accounts | No. |
| Disbursement holds and their notices (verification, KYC, bank-change hold) | Partly: `listExpectedPayouts` `DISABLED` / `AT_RISK`; the reason text is Seller Central's. |
| The Account Health banner for a disbursement hold, the deactivation or §3 review notice, and the funds-appeal route (email after 60 days) | No. No API field names a hold reason, a deactivation or an appeal state [command-verified]. |
| ACCS enrolment for CNY and the per-payout rate (hover on Payments overview) | Enrolment: no. Rate: implied by `OriginalTotal` / `ConvertedTotal`. |
| A PSP's conversion to CNY, its CNY quota, and trade-authenticity checks | Not Amazon at all: the PSP's portal. Amazon's API shows only the payout to the PSP's receiving account. |

## Facts for human readers only

These figures were read 2026-11-09. A skill never states them; cx reads them at run time.
- **ACCS, US page:** cross-currency net proceeds over the past 12 months:
  - under $100k: 1.50%;
  - $100k–$500k: 1.50%;
  - $500k–$1M: 1.25%;
  - $1M–$10M: 1.00%;
  - $10M+: 0.75%.

  Flat 1.5% for AED, CHF, MXN, KRW and TWD; flat 2.0% for JPY; no volume pricing for Amazon.com.br. The CA page says volume pricing excludes .com.tr and .com.br, and that it "does not apply to seller disbursements processed through Hyperwallet".
- **亚马逊全球收款, Amazon's Chinese guidebook (search snippet only, undated):** 0.4% (USD 10M and above), 0.5%, 0.6%, 0.7%, and 0.9% (under USD 100k). Linked NA, EU and JP volume pools. AMZ123's mirror lists US, CA, MX, UK, DE, FR, IT, ES, NL and JP, and 1–3 business days to a domestic RMB account. This table differs from the US page's tiers.
- **Seller Wallet USD (sell.amazon.com):** USD to US banks free. To Hong Kong USD: 0.90% falling to 0.40% by tier. To 20+ non-CNY currencies: 1.50% falling to 0.75%. A 2024 promotion offered "up to 80% off" (0.3% / 0.6%) for registrations by 2024-09-06.
- **Express Payout:** "currently free"; "may be a 50 cent per transaction cost" (2026-01-08).
- **Invoiced-order "Get Paid Faster":** 1.5% of the invoiced amount (2025-05-23).
- **Provider figures (vendors' pages, dated as read):**
  - Payoneer (pricing "Last updated on 1 January 2026"): marketplace receipts "Varies by marketplace"; 1% for receipts in another currency; 29.95 USD annual fee under 6,000 USD received.
  - WorldFirst CN: 0.3% for new users.
  - PingPong CN (2026-10): 0.4%, negotiable.
  - Airwallex CN (2025-08): capped at 0.3%.
  - LianLian: 0.25% for newly linked Amazon stores, limited time (snippet).
- **Practitioner day counts (EcomCrew 2026):** FBA 14–27 days order-to-bank; FBM 20–35.
- **Added 2026-11-10 (gap fill), all read that day:**
  - ACCS CNY tiers, as reproduced by PingPong (2026-09) on 12 months' cross-currency net proceeds: under USD 100k 0.9%; 100k–500k 0.7%; 500k–1M 0.6%; 1M–10M 0.5%; 10M and above 0.4%. They match Amazon's guidebook snippet. Amazon's own page gives only "低至0.4%" ("as low as 0.4%").
  - PingPong's own claim: 0.3–0.4% "market benchmark rate". WorldFirst CN: 0.3% for new users, "远低于行业 1% 平均费率" ("well below the industry 1% average", vendor claim).
  - SAFE thresholds (regulatory, not fees): USD 50,000 per PSP transaction in principle; large-value reports above USD 200,000 a month; restored reporting may be aggregated at or below USD 5,000; individual annual facilitation quota USD 50,000.
  - ZA: Professional plan R1 a month until 2027-03-31 (regular R400); a 5% referral-fee promotion on all categories; fulfilment-fee waivers until 2027-03-31; Easy Ship fees from R20 a parcel. All exclude VAT.
  - EG: referral from 3% or a minimum EGP 5; shipping from EGP 42 a shipment; FBA fulfilment from EGP 15.5 a unit. All exclude VAT.
  - TR: Professional plan 99 TL + KDV a month, waived for sellers registered from 2018-01-15 until further notice (3 months' notice); new-seller 1% commission for 90 days or TL 2,000,000 of sales, until 2026-12-31.
  - BE: €39 (excl. VAT) a month plus referral fees. IE: incentives "€47.25K" (page banner).
  - TRO prevalence (中伦 citing 中国知识产权研究会, 2025-05): 1,302 US cross-border e-commerce cases against Chinese firms in 2024; a TRO was issued in 75.62% of the 931 closed cases.
  - CNY/USD onshore touched 6.6682 on 2026-10-26 (AMZ123 article).

## Pages read

All read 2026-11-09. "helper" = read by a helper seat through a summarising fetch tool; ✓ = re-read by this seat with `curl`.

| Title | URL | Tag | Note |
|---|---|---|---|
| Local models: finances_2024-06-19, financesV0, transfers_2024-06-01, sellerWallet_2024-03-01, financeRemittance-2026-03-17, reports_2021-06-30; schemas/notifications; schemas/data-kiosk | `~/ComChatX_Project/scratch/sp-api-plugins/models` (db2936aa) | [command-verified] | jq dumps |
| Role Mappings for SP-API Operations / Types | `web01/role-mappings.md` (2026-10-28), `role-mappings-for-types.md` | [official] [command-verified] | awk condense |
| SP-API Release Notes (local copy, updatedAt 2026-11-04); SP-API Deprecations (2026-09-09) | `web01/` | [official] | — |
| Finances API | https://developer-docs.amazon/sp-api/docs/finances-api.md | [official] | updatedAt 2026-09-09; lists a "June 29, 2026" note not in the local release notes |
| Get the latest transactions | https://developer-docs.amazon/sp-api/docs/get-latest-transactions.md | [official] | 2026-09-24 |
| Determine payment transactions; Retrieve the amount and status of a payment; Retrieve your current balance; Retrieve the financial events in a group | https://developer-docs.amazon/sp-api/docs/{determine-payment-transactions, retrieve-amount-status-payment, retrieve-your-current-balance, retrieve-financial-events-in-group}.md | [official] | 2026-09-09 |
| Transfers API; Retrieve payment method details and initiate a payout | https://developer-docs.amazon/sp-api/docs/transfers-api.md ; …/retrieve-payment-details-initiate-payout.md | [official] | 2026-09-09 |
| Seller Wallet API; Retrieve Seller Wallet account details; Preview fees and initiate a transaction | https://developer-docs.amazon/sp-api/docs/seller-wallet-api.md ; …/retrieve-seller-wallet-account-details.md ; …/initiate-seller-wallet-transaction.md | [official] | 2026-09-09 |
| Third-Party Provider Registration | https://developer-docs.amazon/sp-api/docs/tpp-registration.md | [official] | 2026-09-09 |
| Finance Remittance API | https://developer-docs.amazon/sp-api/docs/finance-remittance-api.md | [official] | 2026-09-30, Vendors only |
| Invoices API (v2026-06-25) | https://developer-docs.amazon/sp-api/docs/invoice-api.md | [official] | Vendors only |
| Settlement Reports; Payment Reports; Report Type Values | https://developer-docs.amazon/sp-api/docs/report-type-values-settlement.md ; …-payment.md ; report-type-values.md | [official] | 2026-10-14; 2026-09-09 |
| Notification Type Values (TRANSACTION_UPDATE) | https://developer-docs.amazon/sp-api/docs/notification-type-values.md | [official] | 2026-10-28 |
| Roles in the SP-API (AISP, PISP, Finance and Accounting) | `web01/roles-in-the-selling-partner-api.md` | [official] | — |
| DD+7 March 12, 2026 (Amazon email as posted) | https://sellercentral.amazon.com/seller-forums/discussions/t/cd0dfc4d-fbc5-4ded-a0b1-4c7ed989c107 | [official] | ✓ |
| DD+7 FBM & FBA (Glenn_Amazon) | …/t/7d00779e-3f21-42ae-adfe-8ac36b203ddd | [official] | ✓ |
| Account Level Reserve for New Sellers (Micah_Amazon) | …/t/8a25cfdc-51f9-44ff-960b-251997c476ef | [official] | ✓ |
| Disburse on Demand (Amazon email as posted) | …/t/70a0e49b-096d-49fb-b4d7-19b6c3a8432b | [official] | ✓ |
| What is a deferred transaction? (Micah_Amazon) | …/t/3fe1fff3-f924-42bc-aa45-69244e8d6f83 | [official] | ✓ |
| DD+7 in ALR during transition (KJ_Amazon) | …/t/6c017ac3-9f3d-45a5-bc89-14f877ddf6cc | [official] | ✓ |
| Negative balance, Payment FAQs quote (Billy_Amazon) | …/t/4e9c95d9-81ab-436b-8492-80d42bde9804 | [official] | ✓ |
| Where's My Money? (Danny_Amazon) | …/t/a64e7047-1fdc-4ddd-8491-ce7f686b77b2 | [official] | ✓ |
| Understanding Account Level Reserves (Micah_Amazon) | …/t/aac4b8e9-c776-418e-8373-9484fbf8baa1 | [official] | helper; survey note |
| ALR reason on Statement View (Danny_Amazon) | …/t/f42225d6-79c0-4549-b9aa-9ed92439d4b6 | [official] | helper |
| Deferred display "By November 1" (News_Amazon, US/EU) | …/t/3535e9f1-cea7-4037-9163-351eb91b2318 ; sellercentral-europe …/5eb04dd2-c1e7-47bb-9bf4-57049bc7d1fe | [official] | helper |
| Deferred transactions page (News_Amazon, US 2021 / EU 2021-09-23) | …/t/fa4dc3e343d8205930d783e0cf035427 ; europe …/531c1ec69cedea0b00f7fdf94aaa23d4 | [official] | helper |
| Delivery Date Based Reserve, EU 2023 notice | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a3106511f780c0ef74b7d8e2360163f7 | [official] | helper |
| UK transition postponements; extension end | europe …/a5b93d1e-913f-4ac4-9f80-b1cce9f3347e ; …/b701f3a6-8280-40bb-9097-e6ae9644aeb4 ; …/5e2536a8-bb44-4176-b8ed-e65e8c95b529 ; co.uk …/47398bdb-883a-4686-a932-eaa596f66ae2 | [official] | helper |
| Quick Tip: Statement View (Jessica_Amazon_) | europe …/a64bdf02-d6bd-461e-b952-0e2492ba3cfe | [official] | helper; survey note |
| BR DD+7 (Angie_Amazon) | https://sellercentral.amazon.com.br/seller-forums/discussions/t/ed3efbf6-2c5f-4106-863e-db75969a303f | [official] | helper |
| AU reserve range (CR_Amazon) | https://sellercentral.amazon.com.au/seller-forums/discussions/t/25026327-b395-4d48-b913-8d68b9de09c6 | [official] | ✓ 2026-11-10; thread 2024-04-30 |
| JP deferred thread | https://sellercentral-japan.amazon.com/seller-forums/discussions/t/907903cef08702409ce5168d288738ee | [official] | helper |
| PSP Program (News_Amazon 2021, US / EU) | https://sellercentral.amazon.com/seller-forums/discussions/t/b5b926382ab10beb898b7bedbf93b837 ; europe …/29eb22801d8df04049acacc7a55cfc0b | [official] | helper |
| Card required (email as posted) | …/t/4cdd800c-e93b-46a5-b1b8-095b974476e8 | [official] | helper |
| How Amazon seller payments work | https://sell.amazon.com/blog/amazon-seller-payments | [official] | helper; 2025-07-30 |
| How Amazon Business invoices work for sellers | https://sell.amazon.com/blog/amazon-business-invoice | [official] | helper; 2025-05-23 |
| Get paid faster with Express Payout | https://sell.amazon.com/blog/express-payout | [official] | helper; 2026-01-08 |
| Amazon Currency Converter for Sellers (US; CA) | https://sell.amazon.com/programs/amazon-currency-converter ; https://sell.amazon.ca/cad-usd-currency-converter | [official] | US ✓; CA helper |
| Seller Wallet | https://sell.amazon.com/tools/seller-wallet | [official] | ✓ |
| Amazon Lending (US; UK) | https://sell.amazon.com/programs/amazon-lending ; https://sell.amazon.co.uk/programmes/amazon-lending | [official] | helper |
| Global selling (unified accounts) | https://sell.amazon.com/global-selling | [official] | helper |
| How payments work (India) | https://sell.amazon.in/seller-blog/how-payments-work-for-online-selling | [official] | ✓ 2026-11-10; dated 2017-06-15 |
| How should you choose a payment method? (globalselling) | https://globalselling.amazon.com/en/news/news-product-230810-2 | [official] | helper; 2023-07-07 |
| Business Solutions Agreement NA (redline) / AU (Oct 2023) | https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/legal/BSA_NA_English_redlined.pdf ; https://m.media-amazon.com/images/G/35/01/Amazon_Services_Business_Solutions_Agreement_October_2023_LIVE.pdf | [official] | helper; text extraction |
| Update on advertiser payments (Amazon Ads, EN/JP) | https://advertising.amazon.com/library/news/update-on-advertiser-payments | [official] | helper; 2026-04-14 |
| Seller Wallet EUR release; GBP (press) | https://pubt.io/view/9E930FD9350039B1ED87DB93C0539F7A27416338 ; https://retailtimes.co.uk/amazon-seller-wallet-gbp-launches-giving-sellers-in-the-uk-store-more-control-over-their-money/ | [official via press] | helper |
| aboutamazon: easier to manage money (Seller Wallet) | aboutamazon.com (updated 2026-11-04) | [official] | helper |
| KDP PSP page | https://kdp.amazon.com/en_US/help/topic/G6GLVRHVQZY4V4FX | [official] | KDP only |
| Seller Central help pages G200136810, GLRNLZDAKHDBBVBY, GFLRKM5TG3LHNCV8, G202124090, G200497780, G201841950, GHP8M87Z5W6XTSTL, G69122, G1791 | sellercentral.*/gp/help/external/… | [official] | **unreachable** (JS shell, all marketplaces) |
| A2X (5 pages); Link My Books (6); Synder; Webgility; Bookkeep; Taxomate; Elver; Improvado | URLs in What practitioners add | [opinion] | helper |
| Payability; SellersFi (2); 8fig; deBanked; Payments Dive; EcomCrew; Riverbend; MyAmazonGuy (2); SellerSprite; Seller Labs; sellersasksellers.com (2) | URLs in What practitioners add | [opinion] | helper |
| Payoneer (2); WorldFirst (3); PingPong (3); Airwallex (2); LianLian | URLs in What practitioners add | [opinion] | helper |
| AMZ123 (5); 雨果网 (8); 白鲸出海; 知无不言 (7); 跨境知道; 领星 (4); 积加; 赛狐; 易仓 | URLs in What practitioners add | [opinion] | helper |
| Amazon ACCS guidebook PDF (CN) | m.media-amazon.com/images/G/28/AS/AGS/pdf/accs/accs_guidebook_261016.pdf | [official] | snippet only (PDF unparsed) |
| gs.amazon.cn | https://gs.amazon.cn/ | — | redirects to globalselling.amazon.com |
| EcommerceBytes; Reddit; Business Wire | — | — | unreachable (closed / refused / 403) |
| Amazon China: 详解｜亚马逊DD+7预留金政策 (2026-06-05) | https://globalselling.amazon.com/news/news-notices-260605 | [official] | ✓ 2026-11-10 (verifier) |
| DD+7 Deferred Again (EU forum, emails as posted, 2025-09-30) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/7d30d954-dd74-4c46-b01e-48a7cc7f5c45 | [official, emails as posted] | ✓ 2026-11-10 (verifier) |
| Your Reserve Policy – DD+14 (EU forum, email as posted, 2024-07-19) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/19fe1365-987e-42d7-9dc2-a33187fd78a7 | [official, email as posted] | ✓ 2026-11-10 (verifier) |
| UK postponement to 31 January 2024 (co.uk forum, 2023-09-13) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/47398bdb-883a-4686-a932-eaa596f66ae2 | [official, email as posted] | ✓ 2026-11-10 (verifier) |
| Announcing Amazon Seller Wallet EU (Roberto_Amazon, 2026-03-09) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/d852cc31-987a-48cb-b58e-d4db422c5055 | [official] | ✓ 2026-11-10 (verifier) |
| aboutamazon: It's now easier for sellers to manage their money | https://www.aboutamazon.com/news/small-business/its-now-easier-for-sellers-to-manage-their-money-on-amazon | [official] | ✓ 2026-11-10 (verifier) |
| AMZ123: 关于亚马逊回款和收款… (2022-01-18) | https://www.amz123.com/t/K0djSBnw | [opinion, reproduces an old Amazon FAQ] | ✓ 2026-11-10 (verifier) |
| sell.amazon.co.jp beginners-guide; pricing; account-registration (EN) | https://sell.amazon.co.jp/learn/beginners-guide ; https://sell.amazon.co.jp/pricing ; https://sell.amazon.co.jp/en/sell/account-registration | [official] | ✓ 2026-11-10 (verifier) |
| sell.amazon.ca/learn; sell.amazon.ae/learn; sell.amazon.sa/en/learn; sell.amazon.com.au/new-seller-guide; sell.amazon.sg/learn | as named | [official] | ✓ 2026-11-10 (verifier); SG has no payment text |
| Correction: Data Kiosk role requirements (2024-07-02) | https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements | [official] | ✓ 2026-11-10 (verifier) |
| listTransactions; listPayouts; listExpectedPayouts references | https://developer-docs.amazon/sp-api/reference/{listtransactions,listpayouts,listexpectedpayouts}.md | [official] | ✓ 2026-11-10 (verifier); updatedAt 2026-09-10 |
| Models commits df7c6298 (2026-10-28) and db2936aa (2026-10-29) | https://github.com/amzn/selling-partner-api-models/commit/df7c6298 ; …/db2936aa (`.patch`) | [official] [command-verified] | 2026-11-10 (verifier) |
| SP-API Release Notes (live, updatedAt 2026-11-04) | https://developer-docs.amazon/sp-api/docs/sp-api-release-notes.md | [official] | ✓ 2026-11-10 (verifier) |
| *Gap fill 2026-11-10 (all read that day by curl + text dump unless noted)* | | | |
| NA BSA redline: §2 withholding, offset, permanent withholding, security amounts; §3; S-1.4; S-5 | https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/legal/BSA_NA_English_redlined.pdf | [official] | ✓ stdlib PDF text dump |
| Fund Disbursement Eligibility Policy (EU PDF) | https://m.media-amazon.com/images/G/02/Program_Policy/Fund_Disbursement_Eligibility_Policy.pdf | [official] | ✓ |
| Funds Disbursement Eligibility policy rename, 90 → 60 days (News_Amazon US 2024-09-24; UK 2024-09-20) | https://sellercentral.amazon.com/seller-forums/discussions/t/e5457317-25d9-4562-9207-86a19b3d38e9 ; https://sellercentral.amazon.co.uk/seller-forums/discussions/t/c640ebd9-b93d-49ca-9aab-873987dbae5d | [official] | ✓ |
| BSA change effective 2024-07-12, permanent withholding (News_Amazon EU, 2024-06-27) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/08045a88-3f1b-452e-bdb7-0222868c7984 | [official] | ✓ |
| BSA change effective 2026-03-04 (News_Amazon US, 2026-02-17) | https://sellercentral.amazon.com/seller-forums/discussions/t/84e3f6b1-42f7-4cf3-a189-a5cc8d78d838 | [official] | ✓ |
| Funds held 90 days (policy text quoted; Charles_Amazon, 2022-11) | https://sellercentral.amazon.com/seller-forums/discussions/t/9c13c610bf1eb3a84e52942c40d755ad ; …/7c4758278ba8820fc8839d4c9d204624 | [official, staff + quoted policy] | ✓ |
| Old Funds withholding policy text (EU forum, 2020) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/64a7c91b34d3aa46b707b20957528961 | [official, quoted by a seller] | ✓ |
| 60 days, disbursement-appeal@ (CA forum staff, 2024-09) | https://sellercentral.amazon.ca/seller-forums/discussions/t/4fdc17ce-a45a-43f8-b91f-9a5b0f11cfc7 | [official, staff] | ✓ |
| Funds appeal decision email (co.uk forum, 2024-11-30) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/985bc0c6-9161-4918-9db9-75149613f2e0 | [official, email as posted] | ✓ |
| Section 3 review notice, funds withheld (US forum, 2025-04-05) | https://sellercentral.amazon.com/seller-forums/discussions/t/94e0a55b-4554-4414-b701-58cac83553be | [official, notice as posted] | ✓ |
| INFORM hold FAQ (Sonny_Amazon, 2023-06-19) | https://sellercentral.amazon.ca/seller-forums/discussions/t/4e5eecd7-f728-46f3-956f-413dcee0ce7e | [official, staff] | ✓ |
| Re-verification within 10 days (EU forum, 2023-12-05) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/578deeb6-bc06-425c-8f7f-eb49953e5d04 | [official, paraphrased by seller] | ✓ |
| Transfers / Finances 2024-06-19 models: `ExpectedPayoutStatusName`, `PayoutStatusEntry`, `Balance` | models clone db2936aa | [command-verified] | python3 -I |
| 亚马逊全球收款 product page | https://gs.amazon.cn/accs | [official] | ✓ |
| 选择了「0费率」，但跨境收款真的是「0成本」吗？ (2025-02) | https://globalselling.amazon.com/zhishi/article-250208-1 | [official, promotional] | ✓ |
| Amazon ACCS guidebook PDF (CN) | https://m.media-amazon.com/images/G/28/AS/AGS/pdf/accs/accs_guidebook_261016.pdf | [official] | downloaded; CJK text not extractable with the stdlib dump (still snippet only) |
| SAFE 汇发〔2019〕13号 (State Council Gazette) | https://www.gov.cn/gongbao/content/2019/content_5428473.htm | [official: PRC regulator] | ✓ |
| SAFE 汇发〔2020〕11号 (SAFE Xiamen copy) | https://www.safe.gov.cn/xiamen/file/file/20201117/2e54c8a76703447baee7773d476b5d0a.docx | [official: PRC regulator] | ✓ docx text |
| 个人外汇管理办法实施细则 第二条 | safe.gov.cn (Inner Mongolia branch PDF) | [official: PRC regulator] | search snippet only |
| CAS 19 外币折算 (mirror) | https://www.fadada.com/article/detail-11190 | [official: PRC regulator, mirror] | ✓; Deloitte and CICPA copies refused `curl` |
| 汉坤: 跨境电商出口监管方式 (2022-09-07) | https://hankunlaw.com/portal/article/index/cid/8/id/9616.html | [opinion] | WebFetch summary |
| PingPong: 亚马逊收款方式哪种好 (2026-09-11) | https://www.pingpongx.com/zh/news/articles/26091116571864 | [opinion] | ✓ |
| WorldFirst CN pricing / FAQ | https://www.worldfirst.com.cn/cn/pricing/ | [opinion] | ✓ |
| PingPong help centre | help.pingpongx.com | [opinion] | HTTP 412; snippets only |
| LianLian pricing | lianlianglobal.com/pricing | — | 404; not read |
| AMZ123: 记账汇率; 亚马逊结算; 多家上市公司…汇率 | https://www.amz123.com/ask/VrFfga6p ; …/ask/FssWvCKU ; …/t/1WA9bAge | [opinion] | ✓ |
| 中伦: 从TRO到反向TRO (2026-10) | https://www.zhonglun.com/research/articles/56066.html | [opinion] | ✓ |
| ChannelX: Amazon KYC with disbursements held (2026-02-01) | https://channelx.world/2026/02/are-you-impacted-by-amazon-kyc-with-disbursements-held/ | [opinion] | WebFetch summary |
| Mariana Trading v Amazon (NY App Div 2024); AMZ Sellers Attorney award report | law.justia.com ; amazonsellers.attorney | [research] | refused (403); search snippets only |
| Amazon.co.za seller pages: register, fees, beginners guide, new seller guide; sell.amazon.com/south-africa | https://sellercentral.amazon.co.za/welcome/sell-online/{how-to-register-as-a-seller,fees,the-beginners-guide,new-seller-guide} ; https://sell.amazon.com/south-africa | [official] | ✓ |
| aboutamazon: Amazon.co.za launch announcement (2023-10-17); Amazon.ie announcement (2024-05-09) | https://www.aboutamazon.com/news/retail/amazon-south-africa-store-launch ; …/amazon-ireland-store-launch | [official] | ✓ |
| aboutamazon.eu: Countdown to Amazon.ie | https://www.aboutamazon.eu/news/retail/countdown-to-amazon-ie-as-businesses-are-invited-to-register-and-new-country-manager-is-announced | [official] | ✓ |
| Amazon.ie in European Seller Central (News_Amazon, 2024-12-10) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/96cbb8c1-c899-4cd7-bfbf-3715fc0d05de | [official] | ✓ |
| sellercentral.amazon.ie; sell.amazon.com.be/en | as named | [official] | ✓; no payment text |
| sell.amazon.eg learn and pricing (en) | https://sell.amazon.eg/learn?mons_sel_locale=en_EG ; …/pricing?mons_sel_locale=en_EG | [official] | ✓ |
| satis.amazon.com.tr: satis; baslangic-kilavuzu | https://satis.amazon.com.tr/satis ; …/satis/baslangic-kilavuzu | [official] | ✓ |
| Store Identifiers (local copy, updatedAt 2026-10-23) | `web01/store-identifiers.md` | [official] | ZA, EG, TR, IE, BE in the Europe/Middle East/India/Africa group |
| sell.amazon.co.za, sell.amazon.ie, sell.amazon.com.tr | — | — | do not resolve (no such hosts); the stores use sellercentral.amazon.co.za, sellercentral.amazon.ie, satis.amazon.com.tr |
| Amazon disbursements to South Africa (EU forum, 2019) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/e489638b4b0d7168649b057a54734a44 | [opinion, seller reply quoting help text] | ✓ |

## Open questions

1. Does `transactionStatus=RELEASED` also return transactions that are `DEFERRED_RELEASED`? Amazon's "Determine payment transactions" guide filters on `RELEASED` only. Settles it: one payout's group read with and without the filter.
2. (Settled 2026-11-10: `listTransactions` has no `SETTLEMENT_ID` filter; the model added it 2026-10-28 and rolled it back 2026-10-29, and the live reference lists only `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`. A live account can still show whether Amazon's service ignores or rejects the value.)
3. (Partly settled 2026-11-10: the model defines `RESERVED` as the sum of Deferred and Account Level Reserve, I5.) What sign the reserve carries on a live account (the model's example shows it negative), and which `accountType` strings come back ("Standard Orders", "Invoiced Orders", `PAYABLE`)?
4. Are `listPayouts` and `listExpectedPayouts` live in NA and FE, as Role Mappings ("Regions | NA, EU, FE") and the reference's US `marketplaceIds` example say, despite the model's "This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE"? What is `paymentRail` for a CNY ACCS payout?
5. What are the values of `FundTransferStatus` (free string) and `ProcessingStatus` for a failed or retried disbursement, and how does a failed transfer look in groups vs `listPayouts`?
6. Does `listTransactions` return the reserve and debt-recovery lines that v0 carries (`ReserveEvent`, `DebtRecoveryEvent`, `LoanServicingEvent`, `TaxWithholdingEvent`), and under which `description`/`breakdownType`? This matters before v0 events are removed on 2027-08-27.
7. Which `deferralReason` values other than `DD7` and `B2B` appear (e.g. an extended reserve, a PSP reserve)?
8. Does `TRANSACTION_UPDATE` fire on release (deferred → released), or only on posting? Is its `CurrencyAmount` really an integer?
9. The reserve period on this account (DD+7 or extended), read as `maturityDate` minus the delivery date over a sample. Delivery dates come from another seat's reads.
10. (Settled 2026-11-10: Express Payout is a Seller Central deposit-method choice for US store proceeds, per sell.amazon.com's Express Payout page and Amazon China's DD+7 explainer.) Whether this account is eligible is read in Seller Central only.
11. JP, MX, CA, AU, IN, AE, SA and SG: the actual reserve period and on-demand payout availability. Amazon publishes nothing found per store; a live account's `maturityDate` and expected payouts show it.
12. Did the ads balance-deduction change take effect on 2026-08-01 for the affected group? If so, ad charges appear as balance lines rather than card charges.
13. Release-note entry "June 29, 2026" for Finances (linked from the Finances API page) is absent from the live release-notes page too (updatedAt 2026-11-04 has no June 2026 heading). Its content is unknown. The "Finance API Rollback" commit is explained: it removed the `SETTLEMENT_ID` filter and the `AMAZON_FBA_FROM_ORIGIN` store value added the day before.
14. (Gap fill.) On an account under a disbursement hold or deactivation: does the withheld money show as `AVAILABLE`, inside `ACCOUNT_LEVEL_RESERVE`, or elsewhere in `listBalances`? Does `listExpectedPayouts` read `DISABLED`? Does the seller's SP-API app keep working after deactivation at all?
15. (Gap fill.) After a funds appeal is granted, does the release come as an ordinary scheduled payout (`listPayouts` `SCHEDULED`) or an ad hoc one? What do the offsets (removal costs, claims, "damages") look like in `listTransactions` descriptions?
16. (Gap fill.) For an ACCS CNY payout: what are `paymentRail`, `ConvertedTotal`'s currency and the `accountTail` of a domestic account, and do the rate shown on hover and `ConvertedTotal`/`OriginalTotal` agree?
17. (Gap fill.) Which ten stores ACCS CNY covers today (the page says 「十大站点」 without listing them; AMZ123's mirror of Amazon's guidebook lists US, CA, MX, UK, DE, FR, IT, ES, NL, JP), and whether ZA, IE, BE, TR or EG are among them.
18. (Gap fill.) ZA, EG, TR, IE, BE: reserve period (DD+7 or other), Disburse on Demand, ACCS availability by currency, and whether an Egyptian account must be in EGP. Only a live account's `maturityDate`, expected payouts and Deposit Methods page show it.

## Positions

1. **P-flow-1.** A sale's money passes, in Amazon's words, through: shipped (added to the deferred amount) → delivered (reserves) → seven days later moved into the account balance → available → disbursed by the settlement cycle or an on-demand request → the bank, which can take up to five business days. — Amazon email "DD+7 March 12, 2026"; How Amazon seller payments work. Read at run time: each transaction's release day is `maturityDate` in `listTransactions` (`DeferredContext`), and a payout's days to the bank are its `statusHistory` in `listPayouts` (`IN_TRANSIT` to `PAID`).
2. **P-flow-2.** The default reserve period is seven days after the delivery date (DD+7), for FBA and FBM orders alike. The delivery date is the actual one with an integrated carrier or valid tracking, and otherwise the latest estimated delivery date. Amazon may extend the period "following an assessment of your overall risk and historical performance". Its staff also describe 7–14 days; one Amazon email (EU, 2024) set "14 days after the delivery date" (DD+14) for all orders "while we are reviewing your account". Amazon names no exemption. — Understanding Account Level Reserves (Micah_Amazon); Glenn_Amazon; Danny_Amazon; CR_Amazon; DD+14 email as posted. Read at run time: the period applied to each sale is `maturityDate` in `listTransactions` (`DeferredContext`); the account's reserve period as a setting is shown only on Seller Central's Statement View.
3. **P-flow-3.** Amazon's worked examples do not agree on the day a DD+7 sale is released. The English ones (delivered Jan 6 → available Jan 14; Jan 3 → Jan 11; UK 4 June → 12 June) land on the eighth calendar day after delivery. Amazon China's explainer gives May 3 → May 10 (the seventh) and May 5 → May 13 (the eighth, counting from May 6). Any one transaction's release date is the `maturityDate` Amazon returns for it ("The release date of the transaction"). — Micah_Amazon; Amazon email (US 2025-09-29; UK 2024-05-30); Amazon China DD+7 explainer (2026-06-05); finances_2024-06-19.json `DeferredContext`. Read at run time: `maturityDate` in `listTransactions` (`DeferredContext`), for each transaction.
4. **P-flow-4.** Only released transactions are paid in a settlement period, and settlement reports carry only disbursed transactions. A settlement's total is therefore not the period's sales. — What is a deferred transaction? (Micah_Amazon); News_Amazon 2021 deferred page; [seat] for the consequence, stated as arithmetic.
5. **P-flow-5.** A transaction is deferred "while an order is awaiting delivery or pending buyer payment". `deferralReason` examples are `DD7` (delivery date policy) and `B2B` (invoiced orders); the list is not closed. — Micah_Amazon; finances_2024-06-19.json.
6. **P-flow-6.** Amazon Business invoiced orders are credited when the buyer pays the invoice, or at the latest seven days past its due date (usually net 30, sometimes 45 or longer). Sellers cannot opt out. In the US they appear as an "Invoiced Orders" row and may be paid by Amazon Services LLC, separately from standard orders paid by Amazon Payments, Inc. — How Amazon Business invoices work for sellers; NA BSA S-5. Read at run time: an invoiced order's release day is `maturityDate` on its `listTransactions` entry with `deferralReason` `B2B`, and Amazon's terms for the US store are on How Amazon Business invoices work for sellers (https://sell.amazon.com/blog/amazon-business-invoice).
7. **P-flow-7.** Amazon describes the Account Level Reserve as a sum of per-order holds by reason:
   - delivery-date reserves (and, during the 2026 transition, DD+7 amounts);
   - open A-to-z claims;
   - chargebacks from the last 90 days;
   - performance below benchmarks;
   - an account under review (including a new seller whose delivery times exceed the settlement period);
   - local income-tax withholding.

   It publishes no percentage and no timeframe, and every seller is subject to it. — Account Level Reserve for New Sellers (Micah_Amazon); KJ_Amazon; CR_Amazon; NA/AU BSA reserve clauses.
8. **P-flow-8.** The percentage-of-sales reserve rules practitioners circulate ("Tier II … 3% … 28-day average"; "7 days of sales or 5% of 28 days") are not in any current Amazon page reached. The "higher of the past 7 days' sales or 5% of the past 28 days' sales" rule is reproduced by AMZ123 (2022) as text of Amazon's old payments FAQ, second-hand; the tier rules are vendors' claims. No current Amazon page publishes an Account Level Reserve formula. — Payability; SellersFi; 雨果网 2022; AMZ123 2022-01-18 (second-hand); absence in Amazon's pages read 2026-11-10.
9. **P-flow-9.** The reason for each reserve amount is shown on Statement View in Seller Central. `listBalances` returns the reserve amount with no reason field. — Danny_Amazon; finances_2024-06-19.json [command-verified].
10. **P-flow-10.** During the 2026 DD+7 transition, Amazon says DD+7 amounts "may temporarily" appear inside Account Level Reserve instead of as deferred transactions, and that this does not change when funds release. — KJ_Amazon (2026-04-01).
11. **P-flow-11.** Settlement is every 14 days by contract, "or at our option, more frequent", and may vary by store. The withheld reserve becomes the next period's beginning balance, and the beginning balance includes reserves and failed disbursements. — NA BSA S-5; How Amazon seller payments work; Statement View (Jessica_Amazon_). Read at run time: the store's settlement periods are each group's `FinancialEventGroupStart` and `FinancialEventGroupEnd` in `listFinancialEventGroups`, and the next payout's date is `scheduledDate` in `listExpectedPayouts`.
12. **P-flow-12.** On-demand payouts differ by store:
    - US: Disburse on Demand, once every 24 hours, for sellers who completed the DD+7 migration, needing a positive available balance, an active disbursement instrument and 24 hours since the last request.
    - Europe: Disburse Now.
    - API: `initiatePayout` only for DE, FR, IT, ES, SE, NL, PL and BE, once per store and account type per 24 hours, account type `Standard Orders`.
    - Express Payout (24 hours) is US only: a deposit-method choice in Seller Central, with eligibility conditions Amazon lists (US bank, US business address, at most USD 1 million per payout).
    - Amazon China's explainer says each Disburse on Demand withdrawal truncates the current settlement period and restarts the 14 days.

    — Amazon email (Disburse on Demand); EU 2023 notice; transfers_2024-06-01.json; Express Payout page; Amazon China DD+7 explainer (2026-06-05). Read at run time: `initiatePayout`'s stores and 24-hour limit are in the transfers_2024-06-01 model and on the Transfers API page (https://developer-docs.amazon/sp-api/docs/transfers-api.md), Express Payout's conditions on Get paid faster with Express Payout (https://sell.amazon.com/blog/express-payout), and Disburse on Demand or Disburse Now eligibility only in Seller Central, with past on-demand payouts shown as `type` `ON_DEMAND` in `listPayouts`.
13. **P-flow-13.** `initiatePayout` is a money-moving write. Its Role Mappings row reads "Regions | EU" and "Required roles (need at least one) | Finance and Accounting, Payment Initiation Service Provider", so Finance and Accounting alone suffices. A seller's app with that role can start a payout in the EU8. — Role Mappings (2026-10-28); Transfers API page (2026-09-09); release note 2024-12-18.
14. **P-flow-14.** The DD+7 timeline:
    - Amazon calls the Delivery Date Based Reserve its "worldwide standard … since 2016".
    - EU/UK base reserves moved to it from 2023-08-03, with UK transitions postponed and extensions ending September 2025.
    - The remaining accounts were emailed on 2025-09-29/30: a US email gives 2026-03-12; UK/EU sellers report emails giving 2026-03-05, 2026-03-12 or 2026-03-19. These dates are known only from emails sellers pasted in Seller Forums; no Amazon page states them.
    - Brazil applies DD+7 (2025-06-27).

    Amazon published no other per-store dates in the pages read. — EU notice 2023; UK forum notices (2023-09-13, 2024-05-30); Roberto_Amazon (2025-09-01); Amazon emails as posted (US 2025-09-29; EU thread 2025-09-30); Glenn_Amazon (2025-10-01); Angie_Amazon.
15. **P-flow-15.** A negative balance at the end of a settlement period is charged to the payment method on file. Where the bank imposes a credit limit, Amazon may retry every 24 hours until paid. A valid card is required of every seller. The contract also allows offset, invoicing and reversal of bank credits. — Payment FAQs as quoted by Billy_Amazon; Amazon email; NA BSA §2.
16. **P-flow-16.** In the v0 model, a negative balance's recovery is a `DebtRecoveryEvent` (`DebtPayment`, `DebtPaymentFailure`, `DebtAdjustment`; the card's tail and amount; the original debt's group dates). A period-close reserve is an `AdjustmentEvent` of type `ReserveEvent`. In Transfers, `NO_PAYOUT_EXPECTED` means "The expected balance is negative". — financesV0.json; transfers_2024-06-01.json.
17. **P-flow-17.** Each financial event group is a settlement period or payout:
    - `ProcessingStatus` `Open` holds the current balance in `OriginalTotal`; `Closed` holds the disbursed or charged amount.
    - `OriginalTotal` is in the store's currency and `ConvertedTotal` in the disbursed currency.
    - `FundTransferDate` is set only once closed.
    - `TraceId` is the bank-side lookup id.

    — financesV0.json; Retrieve the amount and status of a payment; Retrieve your current balance.
18. **P-flow-18.** Amazon's documented way to list a payout's transactions is to take the `FinancialEventGroupId` from `listFinancialEventGroups` and call `listTransactions` with `relatedIdentifierName=FINANCIAL_EVENT_GROUP_ID`. `listSummary` gives a settlement's `netProceeds` and breakdowns by `SETTLEMENT_ID`. `listTransactions` has no `SETTLEMENT_ID` filter: the 2026-07-29 release note announced one, and the model's one-day addition was rolled back on 2026-10-29. — Determine payment transactions; finances_2024-06-19.json; listTransactions reference (2026-09-10); release notes 2025-12-03, 2026-07-29; models commits df7c6298, db2936aa.
19. **P-flow-19.** `listTransactions` returns `DEFERRED`, `RELEASED` and `DEFERRED_RELEASED` transactions unless filtered. v0 event operations do not show deferred events until they are released. — Get the latest transactions; financesV0.json.
20. **P-flow-20.** Limits common to both Finances versions:
    - events may be missing for the last 48 hours;
    - date bounds must be more than two minutes in the past;
    - a window over 180 days returns nothing (`listTransactions` and `listFinancialEventGroups`);
    - pages can be empty while `nextToken` continues;
    - v0 by-group data covers two years.

    — finances_2024-06-19.json; financesV0.json. Read at run time: the parameter and operation descriptions of `listTransactions` (finances_2024-06-19.json) and of `listFinancialEventGroups` and `listFinancialEventsByGroupId` (financesV0.json) in the models, and the live reference listTransactions (https://developer-docs.amazon/sp-api/reference/listtransactions.md).
21. **P-flow-21.** `listBalances` returns `AVAILABLE`, `RESERVED`, `ACCOUNT_LEVEL_RESERVE`, `DEFERRED` and `TOTAL` balances by account type and store, current or as of a date. `lastUpdatedTime` is in the store's local time zone. — finances_2024-06-19.json.
22. **P-flow-22.** `listExpectedPayouts` returns the next payout's amount and `scheduledDate`, with status `SCHEDULED`, `DISABLED`, `AT_RISK` ("may fail because of an invalid deposit instrument") or `NO_PAYOUT_EXPECTED`. `listPayouts` returns each payout's status history (`STARTED`, `IN_TRANSIT`, `PAID`, `FAILED`, `CANCELLED`, `NO_PAYOUT`), failure reason, type (`SCHEDULED` / `ON_DEMAND`), rail, trace id and settlement id. Both need Finance and Accounting. Role Mappings list "NA, EU, FE"; the model and the live references say "This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE". The two Amazon texts disagree. — transfers_2024-06-01.json; Role Mappings; listPayouts reference.
23. **P-flow-23.** Settlement reports cannot be requested or scheduled. Amazon generates them, `getReports` finds them, and they are kept 90 days. Only `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` survives 2026-11-11. Its amounts are in local formats (`95,00` in EU), with one row per `amount-type` / `amount-description` / `amount`. — Settlement Reports; SP-API Deprecations; reports model. Read at run time: the retention is in the `createdSince` description of `getReports` (reports_2021-06-30.json), and the number format is that of the settlement report document `getReportDocument` returns for the seller's store.
24. **P-flow-24.** The Deferred Transaction Report (`GET_DATE_RANGE_FINANCIAL_HOLDS_DATA`, Finance and Accounting) lists deferred transactions, up to 10 years in one report. It must first be requested in Seller Central's Payments Reports Repository before the Reports API can fetch it. — Payment Reports.
25. **P-flow-25.** `TRANSACTION_UPDATE` is sent when a new transaction is posted. It carries type, posted date, total amount and identifiers, but no deferral status or balance. It is delivered through Amazon SQS. — Notification Type Values; TransactionUpdateNotification.json.
26. **P-flow-26.** Each store settles in its own currency. Amazon Currency Converter for Sellers converts at its third-party provider's rate on the day the transfer is initiated (for a failed disbursement, the re-initiation day). Funds generally arrive in 1–5 business days. The fee is tiered on the past 12 months' cross-currency net proceeds across linked accounts, with flat-rate exceptions by currency and none for Amazon.com.br (rates read at run time). — ACCS page (US, CA); financesV0.json `OriginalTotal`/`ConvertedTotal`; A2X support 2318063. Read at run time: the tiers and exceptions on Amazon Currency Converter for Sellers (US https://sell.amazon.com/programs/amazon-currency-converter; CA https://sell.amazon.ca/cad-usd-currency-converter), and the rate applied to a payout as `ConvertedTotal` against `OriginalTotal` in `listFinancialEventGroups`.
27. **P-flow-27.** Since 2021-07-15 a seller who receives proceeds through a third-party payment service provider must use one participating in Amazon's PSP Program. Amazon stops disbursement to non-participating providers, and providers' KYC requests carry deadlines (45 days in one Amazon email). — News_Amazon 2021-02-01; Amazon KYC email as posted.
28. **P-flow-28.** Seller Wallet is Amazon's own account for holding and moving store proceeds:
    - USD for the US store (2022); EUR for DE, FR, IT, ES, NL, IE and BE, dated two ways by Amazon (an EU forum announcement of 2026-03-09 and trade press of 2026-03-02, against aboutamazon's "In 2025"); GBP for the UK (2026-11, press).
    - Enrolling does not change the settlement cycle (Link My Books).
    - Its API needs the AISP or PISP open-banking roles, available only to PSD2-licensed third-party providers with certificate and signature headers, so a seller's own Finance and Accounting app cannot read it.

    — Seller Wallet page; press releases; Seller Wallet API; Third-Party Provider Registration; Role Mappings. Read at run time: which store currencies Seller Wallet covers is on Seller Wallet (https://sell.amazon.com/tools/seller-wallet) and, for the EU, Announcing Amazon Seller Wallet EU (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/d852cc31-987a-48cb-b58e-d4db422c5055); no operation a seller's own app can call gives it.
29. **P-flow-29.** The Finance Remittance API (2026-03-17) and the Invoices API (2026-06-25) are vendor APIs ("Vendors only"). A seller's payouts are read through Finances and Transfers. — Finance Remittance API page; Invoices API page.
30. **P-flow-30.** Changing or first adding a bank account can defer the remittance calculation by up to 14 days (NA contract). In Brazil it causes a 3-day reserve. A missing or invalid bank account stops a payout from starting. — NA BSA S-5; Angie_Amazon; How Amazon seller payments work. Read at run time: the deferral for a bank change is in the store's Business Solutions Agreement (NA: Business Solutions Agreement NA (redline), https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/legal/BSA_NA_English_redlined.pdf, S-5), Brazil's reserve on BR DD+7 (Angie_Amazon, https://sellercentral.amazon.com.br/seller-forums/discussions/t/ed3efbf6-2c5f-4106-863e-db75969a303f), and the effect on the next payout in `listExpectedPayouts`.
31. **P-flow-31.** What only Seller Central does here:
    - shows the reserve reason and the account's reserve period;
    - Request Payment / Disburse on Demand outside the EU8;
    - Express Payout enrolment;
    - changing deposit methods or the card;
    - requesting the Deferred Transaction Report;
    - Seller Wallet enrolment.

    — The operations in the 2026-10-29 models and Role Mappings [command-verified by absence]; Amazon pages above.
32. **P-flow-32.** How a seller books deferred and reserved money is the seller's choice. Practitioners use three treatments:
    - accrue deferred sales in the month earned and reverse on release (A2X, Link My Books, Bookkeep);
    - carry reserves as a current asset or receivable that nets to zero (A2X, Link My Books, Synder);
    - post reserves as expense and deposit (Webgility).

    Each changes month-end figures differently. — A2X; Link My Books; Bookkeep; Synder; Webgility; Lingxing's settlement-time vs ship-time profit bases.
33. **P-flow-33.** A settlement can span two calendar months. Accounting tools split it and carry a balance between the two halves. Lingxing values a settlement's FX at the month-start rate of the month the settlement began. These are tools' methods, not Amazon rules. — A2X support 959836; Link My Books; Lingxing SettlementCenter.
34. **P-flow-34.** From 2026-08-01 (deferred; the earlier date, 2026-04-15, is a seller report on 知无不言, not on Amazon's page), a small, directly contacted group of advertisers moves from card payment to deduction from the seller balance or Pay by Invoice, with the card kept as backup. For most advertisers, balance deduction is already the method. Amazon's page does not say whether the change took effect; ppc.land (quoting Amazon) reports it from 2026-08-01. — Amazon Ads, Update on advertiser payments (2026-04-14, re-read 2026-11-10); ppc.land [opinion].
35. **P-flow-35.** [seat] The day a seller can spend a sale's money is the later of its `maturityDate` and the next disbursement it falls into, plus bank transit. Shown for reasoning only; it enters no skill.
36. **P-flow-36.** Amazon's store pages state payout timing per store where they state it at all: JP pays "in principle every two weeks" (sell.amazon.co.jp); IN first settles "14 days after you register" then "every 7 days", 2–3 working days to the bank (sell.amazon.in, 2017); CA, AE, SA and AU say "up to five business days" from payment initiation to the bank; Amazon pays only to a bank account, not to "a credit card or online payment system, such as PayPal". None of these pages gives a reserve period; SG and MX pages give nothing. — sell.amazon.co.jp beginners-guide and pricing; sell.amazon.in payments blog; sell.amazon.ca/learn; sell.amazon.ae/learn; sell.amazon.sa/en/learn; sell.amazon.com.au new-seller-guide (all read 2026-11-10). Read at run time: the store's actual cadence is the group dates in `listFinancialEventGroups` and `scheduledDate` in `listExpectedPayouts`, and the days to the bank are each payout's `statusHistory` in `listPayouts`.
37. **P-flow-37.** Amazon's contract lets it hold or keep a seller's money in three ways:
    - withhold payments "for as long as we determine any related risks to Amazon or third parties persist";
    - offset anything it says the seller owes against payments;
    - "permanently withhold any payments" where it finds the account was used for "deceptive, fraudulent, or illegal activity" or to "repeatedly violate our Program Policies". In the EU, from 2024-07-12, this extends to "any other account that you have operated" and names counterfeit goods.

    Amounts required as security may be "refundable or nonrefundable" and may be forfeited. §2 survives termination, and the available balance excludes amounts withheld under §2. — NA BSA §2, §3, S-1.4, S-5 (redline PDF); News_Amazon EU 2024-06-27.
38. **P-flow-38.** The Funds Withholding policy was renamed the Funds Disbursement Eligibility policy on 2024-10-09 (US) and 2024-10-04 (EU). Amazon cut the time after which a deactivated seller may appeal for withheld funds from 90 to 60 days. The policy text:
    - after a deactivation under §3, Amazon "may withhold any funds", usable to "offset amounts that you owe, such as product returns or refunds, A-to-z claims from customers, inventory removal costs, outstanding fees, or monetary and non-monetary damages inflicted on Amazon";
    - on reinstatement, funds are "released and disbursed according to your disbursement schedule";
    - otherwise the seller may appeal by email "at any point after 60 days", and Amazon releases "any remaining funds (less any amounts used to offset amounts you owe us)" after evaluating the account and "confirming your identity". It may ask for documents on "identity, financial instruments, or supply chain";
    - if Amazon "cannot confirm your identity", or finds deceptive, fraudulent, harmful or illegal activity, abuse or repeated violations, it "may be legally required to withhold any payments".

    The older 90-day texts (forum quotes 2020–2022, the JP PDF) predate the change. — News_Amazon (US 2024-09-24; UK 2024-09-20); Fund Disbursement Eligibility Policy PDF (EU); staff replies (CA 2024-09; US 2022-11). Read at run time: Fund Disbursement Eligibility Policy (EU PDF, https://m.media-amazon.com/images/G/02/Program_Policy/Fund_Disbursement_Eligibility_Policy.pdf); the US policy page is a JS shell, so for the US the 60 days stand as News_Amazon posted them on 2024-09-24 (https://sellercentral.amazon.com/seller-forums/discussions/t/e5457317-25d9-4562-9207-86a19b3d38e9), read 2026-11-10.
39. **P-flow-39.** Money is held without a deactivation too:
    - an account "under review as per section 3" has its funds "withheld in accordance with our Funds Disbursement Eligibility Policy", with FBA shipment creation disabled (notice as posted, 2025-04);
    - a US identity-verification (INFORM) hold is aimed to be lifted "within 24 hours" after the seller submits the information. The Account Health banner then disappears, and "The available balance will disburse on your next scheduled settlement date";
    - a bank change can bring "a temporary hold on disbursements for security purposes".

    UK sellers report KYC reviews holding all payouts for more than a quarter while they keep selling (ChannelX 2026-02, [opinion]). — notice as posted (US forum 94e0a55b); Sonny_Amazon (2023-06-19); ChannelX.
40. **P-flow-40.** How a held balance appears in the API:
    - `listExpectedPayouts` can read `DISABLED` ("Payouts have been disabled for this account"), `AT_RISK` (invalid deposit instrument) or `NO_PAYOUT_EXPECTED` (negative expected balance), and `listPayouts` can show `NO_PAYOUT` and a free-text `failureReason`;
    - `listBalances` has five types with Amazon's definitions: `AVAILABLE`, `DEFERRED`, `ACCOUNT_LEVEL_RESERVE` ("Based on sales volume, product category, and account history"), `RESERVED` (the sum of Deferred and Account Level Reserve) and `TOTAL`.

    No type, status or field names funds withheld under the contract or the Funds Disbursement Eligibility policy, and none carries a reason. Which bucket a withheld balance sits in is not stated by Amazon. — transfers_2024-06-01.json; finances_2024-06-19.json [command-verified 2026-11-10].
41. **P-flow-41.** In US litigation, a court's temporary restraining order (TRO) makes platforms and payment providers freeze a seller's balances at once. Under "Schedule A" suits the defendant list is sealed, so the seller learns of the suit from the freeze. A TRO lasts up to 14 days, extendable once, and is usually followed by a preliminary injunction that keeps the freeze. Defaulting defendants' frozen funds can be awarded to the plaintiff. — 中伦 (Zhong Lun), 2026-10 [opinion]; Amazon's policy says only that it "may be legally required to withhold any payments".
42. **P-flow-42.** Whether BSA §2's permanent withholding is enforceable has been decided both ways by arbitrators under Washington law. A New York appellate court (Mariana Trading v Amazon, 2024) upheld an award that rejected the penalty argument, and seller-advocacy firms report awards striking the clause. — court records and law-firm reports, search snippets only [research/opinion; not read in full].
43. **P-flow-43.** ACCS CNY (亚马逊全球收款) pays store proceeds in CNY to a domestic bank account. Amazon's China page says:
    - it covers ten stores;
    - all fees are "包含在汇率中" ("included in the exchange rate"), and the rate shows on hover over the converted amount in the Payments overview;
    - the tier follows the past 12 months' net sales, updated monthly, with linked NA, EU and JP accounts pooled;
    - money arrives in 1–3 business days after Amazon's payment notice;
    - payments into China are processed by the licensed providers 首信易支付 (PayEase) or 富友支付 (Fuiou) under PBOC and SAFE rules;
    - it triggers no extra seller identity verification.

    Conversion happens on payout, so a seller using it holds no foreign currency (PingPong [opinion]). Amazon China says a PSP's USD account receiving CA or MX proceeds converts twice (local currency → USD → CNY), each with a cost. — gs.amazon.cn/accs; globalselling.amazon.com zhishi article-250208-1 (2025-02); PingPong 2026-09. Read at run time: coverage and tiering on 亚马逊全球收款 (https://gs.amazon.cn/accs), and the rate applied to a payout on the Payments overview hover or as `ConvertedTotal` against `OriginalTotal` in `listFinancialEventGroups`.
44. **P-flow-44.** SAFE's rules for PSP conversion (汇发〔2019〕13号, 2019-04-29). A PSP must:
    - verify the seller's identity and trade authenticity from transaction information (goods, quantity, currency, amount, parties and countries, order time), and match receipts to the transaction by party, item and amount;
    - refuse what it cannot confirm;
    - keep single transactions in principle at or below USD 50,000 equivalent;
    - convert through its partner bank by T+1 after receiving funds;
    - agree rate quotation, fees, clearing time and FX gains/losses in advance, show the partner bank's quoted rate, and not adjust it.

    Individuals' conversions under PSP business do not count towards the individual annual facilitation quota. — SAFE 汇发〔2019〕13号 arts 4, 21–25, 27, 38 [official: PRC regulator]. Read at run time: SAFE 汇发〔2019〕13号 as published in the State Council Gazette (https://www.gov.cn/gongbao/content/2019/content_5428473.htm), or a later SAFE notice that replaces it.
45. **P-flow-45.** SAFE's 2020 notice (汇发〔2020〕11号, 2020-05-20) lets a cross-border e-commerce firm:
    - net overseas warehousing, logistics and tax costs against export proceeds;
    - receive, for goods exported to an overseas warehouse, actual sales income that differs from the declared export value.

    Individuals may settle e-commerce receipts through a personal FX account, outside the annual facilitation quota (USD 50,000 per person per year) when they provide proof of transaction amounts or electronic transaction information. Customs codes 9610, 9710 and 9810 (the last for export to overseas warehouses) are the export modes these receipts tie to. — SAFE 汇发〔2020〕11号 items 二 and 四 [official: PRC regulator]; 个人外汇管理办法实施细则 art. 2 (snippet); 汉坤 on GACC 2020 No.75 [opinion]. Read at run time: SAFE 汇发〔2020〕11号 (SAFE Xiamen copy, https://www.safe.gov.cn/xiamen/file/file/20201117/2e54c8a76703447baee7773d476b5d0a.docx) for the netting and overseas-warehouse rules; for the USD 50,000 annual quota no operation or page read in full gives it, and it stands as read on 2026-11-10, CN (个人外汇管理办法实施细则 art. 2, search snippet).
46. **P-flow-46.** A PSP converts to CNY only up to a "人民币结汇额度" ("CNY conversion quota"): the amount it has verified as having a genuine trade background, after the seller uploads transaction details. The receiving account at a PSP must be in the seller's own name. Unlike ACCS, a PSP lets the seller hold store currency and choose when to convert. — WorldFirst CN FAQ; WorldFirst Amazon guide; PingPong 2026-09 [opinion]; SAFE 汇发〔2019〕13号 art. 22.
47. **P-flow-47.** For a China-based seller, an FX difference can arise at each point where a rate is applied:
    - (a) the conversion from store currency to payout currency (ACCS at its provider's rate on the transfer-initiation day, fee inside the rate; seen as `ConvertedTotal` against `OriginalTotal`), or a PSP's conversion between currencies;
    - (b) the PSP's or bank's conversion to CNY against the partner bank's quoted rate;
    - (c) the difference between the rate the seller books and the rate received. CAS 19 books a foreign-currency transaction at the transaction-date spot rate or a systematic approximation, and re-translates monetary items such as receivables at the balance-sheet date, taking differences to profit or loss.

    Which booking rate (day rate, month-start rate, average rate) a seller uses is the seller's choice. — ACCS pages (US, CN); SAFE 汇发〔2019〕13号 art. 27; CAS 19 arts 10–11 [official: PRC regulator]; Lingxing (P-flow-33); AMZ123 booking Q&A [opinion].
48. **P-flow-48.** Amazon.co.za (opened 2024-05) settles in ZAR. Amazon says:
    - "Do I need a South African bank account? No, however your bank account needs to be chargeable in ZAR", with ACCS available to receive the proceeds abroad;
    - the account "must be in your name or the name of your business";
    - fees are "in South African Rand (ZAR) and do not include applicable taxes, such as VAT", and "VAT is additonal to all fees displayed".

    No reserve period or cadence is published. — sellercentral.amazon.co.za registration and fees pages; aboutamazon 2023-10-17. Read at run time: Amazon.co.za seller pages, fees (https://sellercentral.amazon.co.za/welcome/sell-online/fees) and register (https://sellercentral.amazon.co.za/welcome/sell-online/how-to-register-as-a-seller).
49. **P-flow-49.** Amazon.eg: fees in EGP "excluding applicable VAT. We will additionally apply VAT to all fees displayed above". Proceeds are paid by ACH or EFT, "up to five business days" after initiation, to a bank account only. Charges the balance does not cover go to the card. No reserve period or cadence is published. — sell.amazon.eg learn and pricing (en). Read at run time: sell.amazon.eg learn and pricing (https://sell.amazon.eg/learn?mons_sel_locale=en_EG ; https://sell.amazon.eg/pricing?mons_sel_locale=en_EG).
50. **P-flow-50.** Amazon.com.tr:
    - sellers are companies with a Turkish tax number;
    - the first payout is 14 days after registration, then every 14 days, reaching the bank within 5 business days of transfer;
    - a payout needs a balance that is not below zero;
    - referral fees are subject to KDV (VAT) where applicable, and the card covers fees the balance cannot;
    - Amazon's CA ACCS page excludes .com.tr from ACCS volume pricing.

    — satis.amazon.com.tr/satis and başlangıç kılavuzu; sell.amazon.ca ACCS page. Read at run time: satis.amazon.com.tr satis and baslangic-kilavuzu (https://satis.amazon.com.tr/satis ; https://satis.amazon.com.tr/satis/baslangic-kilavuzu), the ACCS exclusion on Amazon Currency Converter for Sellers (CA, https://sell.amazon.ca/cad-usd-currency-converter), and the store's actual cadence in `listFinancialEventGroups` and `listExpectedPayouts`.
51. **P-flow-51.** Amazon.ie (opened 2025-03) and Amazon.com.be are EUR stores in the European Seller Central account ("Your professional selling plan will include the Ireland store"). Both are covered by Seller Wallet EUR. `initiatePayout` covers BE but not IE. No IE- or BE-specific payout, reserve or fee-VAT rule was found. ZA, EG, TR, IE and BE all sit in the SP-API's Europe/Middle East/India/Africa store group. — News_Amazon 2024-12-10; Seller Wallet page; transfers_2024-06-01.json; Store Identifiers (2026-10-23).

## Verification

Verified 2026-11-10 by an adversarial verifier (the previous verifier was cut off mid-edit; its edits to the dated-changes lines for 2025-09-29/30, 2026-03-02 and 2026-07-29 were kept and re-checked). Method: every [official] quote a position rests on was re-read from the raw source with `curl` plus a tag strip (developer-docs pages as `.md`; the two BSA PDFs with a stdlib text extractor, since `pdftotext` would not load); the models clone (db2936aa) with `python3 -I`; the commits df7c6298 and db2936aa as `.patch` from github.com; roles against `web01/role-mappings.md` (2026-10-28) and `role-mappings-for-types.md` (2026-09-09).

**Checked and confirmed as written** (✓ in the body): A1 email (US forum, created 2025-09-29T22:33Z); A2, A4, A5 (Danny), A6, A7, B2, B3, B4, C2, C4 (EU and US), D2, E1/E3 (EU 2023 notice, Roberto 2025-09-01), G1, G2, the BR post, the JP thread, the PSP notice; sell.amazon.com payments blog, Business invoices, Express Payout, ACCS (US, CA), Seller Wallet; the NA BSA (S-5, §2) and AU BSA clauses; S1–S8 model text, enums and rates (listTransactions/listBalances/listSummary 0.5/10, v0 0.5/30, listPayouts/listExpectedPayouts 0.5/10, getPaymentMethods .5/30, initiatePayout 0.017/2); the deprecation rows (settlement V1 deprecated 2025-03-17, removed 2026-11-11; v0 events deprecated 2025-07-21, removed 2027-08-27; `listFinancialEventGroups` not listed); Settlement Reports, Payment Reports, Notification Type Values (`CurrencyAmount` typed `int`), Get the latest transactions, Determine payment transactions (filters `transactionStatus = RELEASED`), Finance Remittance ("Vendors only"), TPP Registration; every role row in the operations table; Amazon Ads "Update on advertiser payments" (2026-04-14).

**Changes (old → new, why, source)**
1. S1 `relatedIdentifierName`: "The model text lags the release note" → there is no `SETTLEMENT_ID` filter; added 2026-10-28 (df7c6298, with `AMAZON_FBA_FROM_ORIGIN`) and removed 2026-10-29 (db2936aa); live reference lists `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID` only. Also "What cx must read" rows and open question 2. Meaning changed.
2. A3 / P-flow-3: "the two examples agree … 8th calendar day" → Amazon's examples disagree: English (three, incl. a UK one) give the 8th day, Amazon China's explainer gives May 3 → May 10 (7th) and May 5 → May 13 (8th); `maturityDate` is the authority. Meaning changed.
3. Dated changes, table E, P-flow-14: "remaining (mostly North American) accounts … 2026-03-12; some 2026-03-05" → US email 2026-03-12; UK/EU emails 2026-03-05, 2026-03-12 or 2026-03-19; route stated: emails pasted in Seller Forums only (US thread cd0dfc4d, EU thread 7d30d954). Dropped the unlocatable "Danny_Amazon 2025-10-01" source. Meaning changed.
4. B6 / P-flow-8: "not in any Seller Central text read" → the 7-days-or-5%-of-28-days rule is reproduced by AMZ123 (2022-01-18) as Amazon's old payments FAQ, second-hand; no current Amazon page reached carries it or any ALR formula.
5. `initiatePayout`: "Rate changed 2024-12-18" → rate changed 2024-11-11, GA 2024-12-18 (release notes). P-flow-13 now quotes the Role Mappings row.
6. S4 / P-flow-22: regions now quote both Amazon texts (Role Mappings "NA, EU, FE"; model and live references "DE, FR, IT, ES, SE, NL, PL, and BE"); the claim that the model text "predates" the reads is marked [seat].
7. S7: deprecated `…FLAT_FILE` roles "Inventory and Order Tracking, Finance and Accounting, Amazon Fulfillment" → Amazon Fulfillment or Finance and Accounting (types page). S8: types page date 2026-10-28 → 2026-09-09.
8. S9: "None of the four Data Kiosk schemas carries … payout, balance" → Seller Analytics has a `Lending` group with `disbursements` and `totalBalanceByStandardOrders` under PAAM right `analytics_sales_and_lending_view` (no seller role; nothing built). Added the open Economics role (correction page, 2024-07-02).
9. D4 / P-flow-12 / open question 10: Express Payout is a Seller Central deposit-method opt-in for US store proceeds (sell.amazon.com; Amazon China explainer with its conditions). D2 gains the explainer's facts (DoD on Standard/Invoiced rows, truncates the 14-day period).
10. A5 / P-flow-2: added Amazon's DD+14 email (EU, 2024-07-19). CR_Amazon "about 2023" → thread 2024-04-30. Glenn "October 2025" → 2025-10-01. KJ "2026-03-31" → 2026-04-01.
11. Seller Wallet EUR: F3 "launched 2026-03-02" stated as fact → both Amazon dates given (forum 2026-03-09; aboutamazon "In 2025", re-read); P-flow-28 likewise.
12. G4 / P-flow-34: Amazon's page re-read; "deferred from 2026-04-15" attributed to a seller report; whether it took effect is ppc.land's [opinion].
13. Table E filled from Amazon store pages: JP every two weeks; CA/AE/SA/AU "up to five business days"; IN page dated 2017-06-15 (was "undated"); SG and MX nothing. New P-flow-36.
14. P-flow-27: dropped the unread "2021-07-05" source.

**Could not verify**: the KYC 45-day email (wearesellers), D6 disbursement-appeals snippet, the Chinese ACCS guidebook tiers (PDF unparsed), Retail Times / pubt.io press quotes, most practitioner quotes (A2X 2016/2025 articles, Synder, Webgility, Payability, SellersFi, cifnews, Lingxing) other than A2X 959836 and two Link My Books quotes, which matched.

**Positions**: 36 (35 checked + 1 added). Changed: 11 (P-2, 3, 8, 12, 13, 14, 18, 22, 27, 28, 34). Added: 1 (P-36). [seat]: P-35 (unchanged). Removed: none. D233: no position states when to ask the seller, a sequence, a threshold or a ceiling; P-32 lists booking choices without ranking them.

**Cross-file disagreements (for the lead)**: reconciliation P-rec-40 says no Amazon page was read for the ads billing change; Amazon Ads' own page exists and was re-read here. reconciliation P-rec-21 gives a single migration date 2026-03-12; UK/EU sellers were given 2026-03-05, -12 or -19. finance-surface P-api-11 gives NA, EU, FE without the model's EU-only text.

**Gaps left**: no Amazon page gives a reserve period or on-demand availability for JP, MX, CA, AU, IN, AE, SA or SG (only cadence and transit for some); per-store Seller Central help pages remain JS shells; the per-account reserve period is read only from `maturityDate`.

### Gap fill (2026-11-10)

Requested by two completeness critics (a US/EU controller and a Chinese 财务总监). Method: Amazon pages, forum posts and PDFs fetched with `curl` and read through a tag-strip or a stdlib PDF text dump (`python3 -I`; poppler's `pdftotext` would not load). Models were read from the clone db2936aa. PRC regulations were read from gov.cn and safe.gov.cn copies. Practitioners were read with `curl`, or with WebFetch where `curl` was refused (marked in Pages read). No Amazon API host was called.

**Gap 1: the CNY leg (结汇) and where FX loss arises.** Not covered before; filled.
- New §J (J1–J6): ACCS CNY in Amazon China's words (fee inside the rate, licensed processors PayEase / Fuiou, 1–3 business days, tiering, no extra SIV); Amazon China on PSP double conversion; SAFE 汇发〔2019〕13号 (trade authenticity from transaction data, USD 50k per transaction, T+1 conversion, disclosed bank rate, individual quota carve-out); SAFE 汇发〔2020〕11号 (netting of overseas costs, overseas-warehouse income differing from the declared value, individuals' personal FX accounts); customs modes 9610/9710/9810 (via 汉坤); CAS 19 arts 10–11.
- Practitioners: PingPong, WorldFirst (CNY conversion quota), AMZ123 booking-rate practice, listed sellers' FX lines.
- Positions P-flow-43 to P-flow-47. New rows in What cx must read, What only Seller Central shows and Facts for human readers only. Open questions 16–17.

**Gap 2: funds held at deactivation, suspension, review or verification.** D6 had only a 90-day snippet, which is out of date. Filled.
- New §I (I1–I6): NA BSA §2 withholding, offset, permanent withholding, security amounts and forfeiture, §3 survival, S-1.4, S-5; the EU change of 2024-07-12; the policy rename and the cut from 90 to 60 days (2024-10-09 US / 2024-10-04 EU); the EU Fund Disbursement Eligibility Policy PDF text; §3 review notice; INFORM hold FAQ; how held money shows (or does not) in `listExpectedPayouts`, `listPayouts` and `listBalances`.
- D6 rewritten to point to §I.
- Practitioners: 中伦 on TROs and Schedule A, the split arbitration record, ChannelX on UK KYC holds.
- Positions P-flow-37 to P-flow-42. Open questions 14–15.

**Gap 3: ZA, EG, TR, IE, BE.**
- Five rows added to table E from each store's own pages (currency, bank-account rule, VAT on fees, cadence where stated, SP-API store group).
- Dated changes: Amazon.ie opened 2025-03-18; BSA update 2026-03-04.
- Positions P-flow-48 to P-flow-51. Promotions and fee figures are in Facts for human readers only. Open question 18.
- Note: sell.amazon.co.za, sell.amazon.ie and sell.amazon.com.tr do not resolve. The stores' seller pages are sellercentral.amazon.co.za, sellercentral.amazon.ie and satis.amazon.com.tr.

**Correction found while filling:** S2 and open question 3 said the model does not define `RESERVED` vs `ACCOUNT_LEVEL_RESERVE`. finances_2024-06-19.json does: `RESERVED` = Deferred + Account Level Reserve, and ALR is "Based on sales volume, product category, and account history" [command-verified]. Both were corrected in place. No existing position was renumbered or changed.

**Positions:** 51 (36 + 15 added: P-flow-37 to P-flow-51). D233 check: the new positions state contract terms, policy text, model fields, regulations and practitioners' accounts. None says when to ask the seller, sets a sequence or a threshold, or classifies a held balance as an asset or not; P-flow-47 leaves the booking rate to the seller.

**Gaps left**
- Gap 1:
  - Whether ACCS CNY accepts an individual's (对私) account, or only a company account with foreign-trade rights: only the earlier 雨果网 Amazon-credited piece (enterprise ACCS needs 对外贸易经营权); no Amazon page states the rule.
  - Which ten stores ACCS CNY covers today (the page gives no list).
  - The ACCS guidebook PDF's tier table and terms (CJK text not extractable).
  - LianLian's fee and conversion pages (404) and PingPong's help centre (HTTP 412): no first-hand PSP terms on rate spreads against the central parity beyond WorldFirst's and PingPong's marketing.
  - GACC announcements 2014 No.12 and 2020 No.75, and the 2024-12-15 change: read only through a law firm and the press.
  - CAS 19 application guide (central parity as spot rate): snippet only.
- Gap 2:
  - The US-English text of the Funds Disbursement Eligibility policy (help page 9RA9LYBJ3QP27M6 and the US copy are JS shells; only the EU PDF was read).
  - The live G1791 BSA (the NA text is the redline PDF).
  - Where a withheld balance sits in `listBalances`, and whether the SP-API keeps answering after deactivation: Amazon states neither (open question 14).
  - The Mariana Trading decision and arbitration awards: read as search snippets only.
- Gap 3:
  - For ZA, EG, TR, IE and BE: reserve period or DD+7 status, Disburse on Demand, ACCS currency support and rate class (only ZA's ACCS mention and the .com.tr volume-pricing exclusion were found), whether Egypt requires an EGP account, and the VAT treatment of Amazon's fees in IE and BE.
  - JP/IN-style first-payout rules for ZA and EG: none published.

### Correction 1 (2026-11-10)

Applied brief 2026-11-03-306 correction 1 (the plugin zen's item 4: a value that differs by marketplace or changes from year to year is looked up, not carried). Every value stays in its position as evidence, with its store, day read and citation. Operation names were checked against the models clone (db2936aa); pages are taken from Pages read. No page was re-fetched and no Amazon API host was called.

- **Positions changed** (one "Read at run time:" sentence added at the end, nothing else reworded): P-flow-1, 2, 3, 6, 11, 12, 20, 23, 26, 28, 30, 36, 38, 43, 44, 45, 48, 49, 50 (19).
- **Left as they were:** history (P-flow-10, 14, 27's 2021-07-15, 34, 37's 2024-07-12), and positions whose substance is a rule, a field or a structure rather than such a value (the rest).
- **No operation or page:** the USD 50,000 individual annual quota (P-flow-45) stands as read on 2026-11-10, CN, from a search snippet. The US text of the 60-day appeal wait (P-flow-38) stands as News_Amazon posted it on 2024-09-24. Disburse on Demand eligibility (P-flow-12) and the account's reserve period (P-flow-2) are shown only in Seller Central.
- **Stable enough for a skill:** the values in items 1 (days to the bank), 2 (DD+7), 5 (14 days), 6 (on-demand frequencies and limits), 7 (seven days past due), 11 (48 hours, 180 days, two minutes, 90-day retention), 13 (60 days), 14 (T+1, USD 50,000) and 16 (VAT on ZA, EG, TR fees) were taken out of the items. They now sit in What cx must read at run time: eight new rows, with item 16 covered by the existing ZA/EG/TR/IE/BE row.
- **Reconciliation verifier note:** none for this file.
