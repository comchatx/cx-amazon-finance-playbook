# How sellers and the tools they pay for run the money job, and what published research says

Read 2026-11-09 by the research seat. Tags: [official] Amazon's own page, model or notice; [opinion] a named vendor or practitioner; [research] a published study, regulator or court record; [seat] this seat's reasoning, never a position; [command-verified] a command run here (a `curl` plain GET plus an exact-string check of the quoted text, or a grep over the local Role Mappings copy).

How the reading was done. Public pages only, by plain GET or through a fetch tool. No Amazon API host was called and no sign-in page was used. Six fetch passes covered: English accounting tools; English profit tools; recovery and financing tools; Chinese ERPs; Chinese seller practice; and practitioners plus published research. The fetch tool returns condensed extracts. Quotes it returned are marked as such where they could not be re-checked. The quotes this file leans on hardest were re-fetched with `curl` and matched exactly; those are tagged [command-verified]. Items seen only in a search-result summary are marked "(snippet)" and carry no weight.

## What this covers

This file covers how the money job is done outside Amazon: by the paid tools sellers use (profit dashboards, bookkeeping connectors, recovery services, payout financing; English and Chinese), by Chinese large-seller finance teams, and by the accountants and educators who write about Amazon money. It ends with what regulators and economists have published on Amazon's seller fees.

It feeds every skill of the money pack as **context**:

- the vocabulary a seller brings ("estimated payout", 结算利润, 预结算, TACoS);
- the choices each tool makes, which a seller will expect cx to understand (allocation keys, refund dating, FX rate, DD+7 handling);
- the reasons a tool's number differs from Seller Central's.

Nothing here is a rule for cx. A tool's choice is a fact about that tool. Where tools disagree, the disagreement is the fact.

Why a senior operator cares. Every seller who asks "what did this product earn?" already has a number from a tool or a spreadsheet. When cx's number differs, the first question is why, and the answer is nearly always one of a short list: the dating basis (order, ship, settlement, transfer), the FX rate, the deferred and reserve treatment, the allocation key for shared fees, or the COGS method. Every tool below picks among these, and they pick differently.

**Dated changes since 2025-01-01 that touch this area** (Amazon's date first where Amazon gives one):

- **2024-11-01 or 2025-01-15.** Amazon begins proactive reimbursement of FC-lost items, and its posts give two dates. The post created 2024-07-24 on the US forum gives "November 1, 2024" (*Update on Reimbursement Automation and Eligibility Window*, https://sellercentral.amazon.com/seller-forums/discussions/t/6605eede-df8e-4498-803f-cb612d95d7ce); a post created 2024-10-10, in British spelling and naming no store, gives "January 15, 2025" (same title, https://sellercentral.amazon.com/seller-forums/discussions/t/d0fc997e-de50-4100-9803-76b7993b66df) [official, via `04-job-money.md` §4.3 and refunds-reimbursements-adjustments.md P-ref-13]. No page says which store each date addresses; a per-store rollout is a reading only [seat]. Recovery vendors' pages still advertise 18-month audits (GETIDA, Helium 10 MRS) [opinion].
- **2025-01-27.** China's State Taxation Administration Announcement 2025 No. 3 sets the 9810 "离境即退税、销售再核算" export-refund route for overseas-warehouse goods [official, Chinese government].
- **2025-03-31** (announced for 2025-03-10, moved on 2025-02-28). FBA lost or damaged pre-order inventory is reimbursed at manufacturing cost. Amazon: "The updated Fulfillment by Amazon (FBA) inventory reimbursement policy will now go into effect on March 31, 2025, instead of March 10, 2025." [official] *New effective date for FBA inventory reimbursement policy* (News_Amazon, `createdAt` 2025-02-28), https://sellercentral.amazon.com/seller-forums/discussions/t/ed8abc33-a1d5-417d-b2e2-03b789099833, read 2026-11-10. (Corrected by the verifier: the file had 2025-03-10 as Amazon's date and March 31 as the vendors'; it is the other way round.)
- **2025-03-17.** Settlement report V1 flat file and XML deprecated; removal on **2026-11-11** [official, via `04-job-money.md`]. A2X still "fall[s] back to using the V1 format if V2 is not available".
- **2025-05-02 / 2025-08-29.** The US de minimis exemption ends for China-origin goods, then for all countries. Chinese sources report the cost and margin effect [opinion].
- **2025-09 (UK/EU)** and **2026-03-12 (North America, then "global")**. Remaining accounts move to the DD+7 reserve. The Amazon wording comes from a notice e-mail a seller quoted on Seller Forums; Chinese and English trade press agree on the date [opinion].
- **2025-09-17.** Amazon announces **Profit Analytics** at Accelerate 2025: "Amazon introduced Profit Analytics this year" (aboutamazon, 2025-09-17) and "To get started, go to Profit Analytics" (Seller Forums, 2025-09-17); a News post naming the path "Reports, and select Selling Economics and Fees" follows on 2025-11-13 [official]. Trade press dates the release 2025-09-18 (PPC Land) [opinion]. The help page itself (G8CXLSH94WNPB9R4) is a JS shell.
- **2025-09-25.** FTC settlement with Amazon over Prime ($2.5B). This is a consumer case, not seller fees [research/regulator].
- **2025-10-15.** Claim windows revised (US) [official, via `04-job-money.md` §4.3].
- **2025-10-31.** First quarterly report by platforms to Chinese tax authorities (covering July–September 2025) [opinion, 36氪].
- **2025-11.** Some sellers' France and Spain EPR fee-payment service becomes an account-level reserve [official, gs.amazon.cn 2025-11-12].
- **2026-02-04.** Bundeskartellamt prohibition decision B2-73/20 on Amazon's price-control mechanisms, made public 2026-02-05, with "rund 59 Millionen Euro" disgorgement (beck-aktuell, 2026-02-05). Amazon has appealed to the BGH (KVB 13/26; a hearing on suspensive effect 2027-01-26 per a law-firm note, snippet) [research/regulator, via secondary reports; the authority's own page not reached].
- **2026-04-17.** US/CA 3.5% fuel and logistics surcharge [official, via `04-job-money.md` §4.2].
- **2026-08-13.** 领星 adds ship time (「发货时间」) as a new profit basis beside settlement time and 预结算, framed by its release as the answer to Amazon's Date Range / Transaction report change (「还在为亚马逊后台日期交易范围报告口径调整头疼吗？」) [opinion; AMZ123 post by 领星ERP, verified 2026-11-10].
- **2026-08-31.** FTC and states sue over the Sponsored Ads "soft reserve price" [research/regulator, via the ads playbook].
- **2026-10-09.** Judge Chun refuses to move the FTC v. Amazon monopoly trial from **2027-03-29** to June 2027 [research: PYMNTS/CPI 2026-10-11 citing Law360 and MLex; the order itself not read].
- **2026-11-14.** A2X price increase (vendor notice). **2027-01-01:** Taxomate sizes plans on a 3-month average order count. **2027-01-19:** California v. Amazon trial date.

## Amazon's own rules

This file's subject is not Amazon's rules. The rules below are the ones the tools are built against or measured against. The full set lives in the area files and in `04-job-money.md`, whose sources are reused here and not re-read unless marked.

### A. Amazon now publishes its own per-product profit face

- **SKU Economics (SKU Central) and the SKU Economics report.** "SKU Economics is a tool on SKU Central, for all third-party sellers, that collects fees, sales, ads, off-Amazon costs, and net proceeds in a single view". "The report allows you to view the economics of your selection at the FNSKU, MSKU, ASIN, and parent-ASIN level. This single source for historical economics data eliminates the need to merge sales, fees, and ads reports to understand your net proceeds." [official] *Track fees with the new SKU Economics report* (News, Seller Forums), https://sellercentral-europe.amazon.com/seller-forums/discussions/t/3a20e851-096e-4fca-a62d-c8e48b30e367, read 2026-11-09 [command-verified].
  - A seller reply in the same thread: "only sponsored product ads are added (while other ad types are missing)", and "FBA fees quantity is not equal to number on units sold". This is [opinion, an unnamed seller], undated in the extract.
- **Profit Analytics.** Amazon's own words: "Amazon introduced Profit Analytics this year to help sellers who wanted deeper insights into their business costs and profitability. The tool consolidates cost data from multiple sources like advertising spend, refunds and returns, including costs from other sales channels" (*Amazon announces new tools to help sellers save time and money*, aboutamazon, 2025-09-17, https://sellingpartners.aboutamazon.com/amazon-announces-new-tools-to-help-sellers-save-time-and-money); "Consolidate costs from 8+ resources … To get started, go to Profit Analytics" (Accelerate forum post, 2025-09-17, https://sellercentral.amazon.com/seller-forums/discussions/t/48876abe-209c-41e2-ab6f-68f0c30adc9d); "To start using Profit Analytics, go to Reports, and select Selling Economics and Fees" (News_Amazon, 2025-11-13, https://sellercentral.amazon.com/seller-forums/discussions/t/3d72b2ff-5559-4e3a-b8a4-7bfbe7c0bdc1). [official; all read 2026-11-10] Trade press reports it was released on September 18, 2025, under seller economics. It shows SKU, ASIN and parent-ASIN profit from "sales, returns, fees, advertising data, and seller-provided cost data", with tiles for Net Proceeds, Sales, Fulfillment Cost, Selling Fees, Storage Cost, "Return & Recovery Operations" and Advertising Cost of Sales.
  - Latency: "Data in Profit Analytics typically runs 1-2 days behind real-time transactions, though some fee data may delay up to 7 days".
  - Scale: listings up to 500,000; beyond that, "SKU Economics and Configurable Economics Preview reports".
  - Seller inputs: "cost of goods sold data, total cost per unit, storage cost per unit, shipping costs, packing costs, and LTL freight costs", plus off-Amazon ad spend (Meta, TikTok, Google).
  - Source: [opinion: PPC Land, Luis Rijo, 2025-09-20, paraphrasing Amazon's documentation], https://ppc.land/amazon-releases-new-profit-analytics-dashboard-for-sellers/ [command-verified fetch].
  - A search summary attributes to Amazon the note that estimated net proceeds "represent estimates dependent on seller-provided inputs" and "may differ from net proceeds in other Amazon reports that exclude these costs". That is (snippet); the Amazon help page was not found.
  - The API face of these is the Data Kiosk economics dataset (`analytics_economics_2024_03_15`) and the economics preview report; see `04-job-money.md` §2.6. Roles: Role Mappings list Brand Analytics for every Data Kiosk operation, while Amazon's correction of 2024-07-02 says "The Economics dataset requires the Selling Partner Insights role" (product-profit.md P-prof-12).
- **What follows** [seat]: Amazon's own "net proceeds" is a third profit definition beside the tools' "net profit" and "gross profit". It counts by Amazon's dataset rules, which `04-job-money.md` §4.8 notes date refunds "by refund request time". A seller comparing Sellerboard with Profit Analytics is comparing two definitions.

### B. The payout timeline the tools are built against

Reused from `04-job-money.md` §4.1, with its sources:

- settlement "every two weeks";
- deferred transactions under the delivery-date reserve ("DD+7");
- the account-level reserve;
- disbursement "up to five business days".

Added here:

- **DD+7 for remaining North American accounts, 2026-03-12.** A seller posted the notice: "On March 12, 2026, in line with your feedback, we'll update your reserve settings to the standard reserve period of seven days after delivery date (DD+7). Most Amazon sellers worldwide already use DD+7. … funds made available for disbursement seven days after we confirm order delivery." Source: *Your account will be migrated to DD+7 …* (Seller Forums thread), https://sellercentral.amazon.com/seller-forums/discussions/t/afacf90a-3e68-4d8d-87aa-8e66d3c24500, read 2026-11-09 [command-verified]. This is Amazon's e-mail as a seller quoted it, not an Amazon post. Tag it [official-as-quoted].
- **Europe.** Amazon forum notices offered EU sellers a transition extension to 30 September 2025, before moving accounts to DD+7 (snippet, Seller Forums EU; not opened).
- **Chinese official guide (globalselling.amazon.com, 2026-01).** It gives "付款频率： 每14天一次（双周结算）" and an arrival window of "T+17至T+21日". The page also gives reserve percentages by seller stage, and elsewhere contradicts itself; it is not used as a rule. https://globalselling.amazon.com/zhishi/article-260113-2 [official, via fetch extract].
- **Account-level reserve for EPR (FR/ES), 2025-11.** "2025/11月起，部分卖家的法国及西班牙站点EPR代付服务将升级为账户级别预留金机制"; it "不会额外收费，但会影响您的可提现余额". https://gs.amazon.cn/news/news-notices-251112 [official, via fetch extract].
- **Payment-provider rule (2021, still standing).** For non-approved payment providers: "您的资金预留期将被延长，最长可到预计最迟送达日期后21天". https://globalselling.amazon.com/news/news-notices-210201 [official, via fetch extract].

### C. Amazon on the cost of converting currency

- Amazon's Chinese 全球开店 knowledge page on its own currency service (ACCS, 亚马逊全球收款) says "「0费率」并不等于「0成本」", warns of "「二次汇损」" when a third-party collector converts twice, and describes ACCS as "只经过一次换汇，只收取一次费用", with tiered pricing ("阶梯定价…生意越大，费率越低"). No rate table is printed. https://gs.amazon.cn/zhishi/article-250208-1 (2025-02) [official, via fetch extract; Amazon promoting its own product].
- Link My Books on the same mechanics: "Amazon sets the exchange rate once, on the day the transfer to your bank account is initiated", with a conversion fee of "0.75%–1.5% of the transfer" (vendor's figure). Link My Books help 3447820 [opinion].

### D. Reimbursements as money received

Windows and valuation are in `04-job-money.md` §4.3–4.4 (Amazon's posts). Two vendor statements disagree with them; see *Where tools disagree*.

### E. Amazon's own agent tooling has no finance skill

Amazon's "Amazon Selling Partner" Claude plugin 1.0.0 has no finance skill. Its seller-analytics skill rules out "tax/financial-settlement reporting" (`04-job-money.md` §4.7) [command-verified there]. Nothing to borrow for this pack.

### F. What Amazon's data gives a ledger mapping, and the standards a Chinese ledger posts under (added 2026-11-10)

Amazon publishes no chart-of-accounts mapping. No Amazon page read maps its charge types to ledger accounts, and none names 金蝶 Kingdee or 用友 Yonyou. The mapping every ERP and connector builds is keyed on Amazon's charge labels:

- **Finances v2024-06-19.** `Breakdown.breakdownType` is a plain string, "The type of charge.", with no enumeration in the model. `Transaction.transactionType` lists one example value ("**Possible value:** `Shipment`"), and `description` gives examples ("`Order Payment`, `Refund Order`"). So a mapping table on this face is built from the values seen in data, not from a published list. [official, command-verified: `models/finances-api-model/finances_2024-06-19.json`, `definitions.Breakdown`, `definitions.Transaction`, models clone db2936aa, read 2026-11-10]
- **Settlement V2 flat file.** The columns are `transaction-type` / `amount-type` / `amount-description` (`reconciliation.md` holds their meaning). 领星 maps "每一笔明细金额…按映射规则映射为summary项目" (§9 below), which keys the mapping to Amazon's Summary (statement) categories.

A Chinese entity's ledger posts under the Ministry of Finance's Accounting Standards for Business Enterprises (企业会计准则). These are not Amazon's rules. Three articles bear directly on the voucher lines practitioners argue about. Each was read from the full-text copy on fadada.com's law database (the MOF page itself was not reached), on 2026-11-10 [official (PRC Ministry of Finance), via a law-database copy]:

- **CAS 14 收入 (revised 2017, in force 2018-01-01), art. 34.** "企业在向客户转让商品前能够控制该商品的，该企业为主要责任人，应当按照已收或应收对价总额确认收入；否则，该企业为代理人，应当按照预期有权收取的佣金或手续费的金额确认收入". The same standard on goods sold with a right of return: revenue "不包含预期因销售退回将退还的金额", with that amount recognised as a liability. https://www.fadada.com/article/Basics-008725
- **CAS 19 外币折算, arts. 10–11.** At initial recognition: "采用交易发生日的即期汇率…也可以采用按照系统合理的方法确定的、与交易发生日即期汇率近似的汇率折算". At the balance-sheet date: "外币货币性项目，采用资产负债表日即期汇率折算…产生的汇兑差额，计入当期损益". Article 12's translation of a foreign operation's statements, with its difference going to equity, is a different case. https://www.fadada.com/article/Basics-008770
- **CAS 1 存货, art. 6.** "存货的采购成本，包括购买价款、相关税费、运输费、装卸费、保险费以及其他可归属于存货采购成本的费用". https://www.fadada.com/notice/detail-11131.html

What follows [seat]: an amount Amazon holds (a reserve, a deferred balance, an unsettled balance) is a foreign-currency receivable, which makes it a monetary item under CAS 19 art. 11. That is why the ERP-side vouchers carry month-end 汇兑损益 on balances Amazon has not paid out. An amount translated at a "近似汇率" (a month-start or monthly rate, as 领星 and 积加 use) is a permitted choice under art. 10, and it differs from Amazon's own conversion.

## The SP-API and report faces

This section lists the faces the tools **say** they read, and the role Amazon's Role Mappings give for each. Roles come from `web01/role-mappings-for-types.md` (updatedAt 2026-09-09) and `web01/role-mappings.md` [command-verified by grep]. Rates and pitfalls are `04-job-money.md` §2's.

| Face | Tools that name it | Role (Role Mappings) | Note |
|---|---|---|---|
| `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` (settlement flat file, V2) | A2X ("will use the V2 format, but it will fall back to using the V1 format if V2 is not available", "except in India and Japan"); 积加 结算中心 ("页面数据来源：V2报表"; reserve "取自上一结算周期的V2报表中 amount-description = Current Reserve Amount"); Link My Books ("uses the Amazon settlement reports"); Taxomate ("Payment Settlement Report"); Webgility; 易仓; 领星 ("需要亚马逊的Settelment report生成才可获取") | Finance and Accounting | V1 flat file and XML are removed **2026-11-11**. A tool on V1 fallback loses it then [seat]. |
| Finances API: financial events / financial event groups (v0), transactions (v2024-06-19) | Synder ("settlement reports and Amazon's Financial Events API"); Sellerboard blog ("financial event groups, which map charges and credits to settlement periods"); 领星 ("接入亚马逊财务API接口"); 店小秘 ("取的是三级交易类型的数据"); Finaloop ("directly from Amazon's Selling Partner API"); Link My Books deferred add-on ("Built directly on Amazon's API data"); 赛狐 | Finance and Accounting (`listTransactions`, `listBalances`, `listSummary`). `listFinancialEventGroups` lists Finance and Accounting or Account Information Service Provider. | v0 event operations are removed 2027-08-27; `listFinancialEventGroups` is not on the schedule (`04-job-money.md`). No tool page says which version it calls. |
| Deferred transactions | A2X takes opening balances from the Seller Central "Deferred Transactions Report"; 赛狐 "自动获取亚马逊后台每日延迟交易数据"; 领星 fetches "每天晚上12点至早上8点"; 积加 has an "Amazon延迟交易报告" menu | In the API: `transactionStatus=DEFERRED` in v2024-06-19 (Finance and Accounting) | None of the tools names an API path for deferred data. |
| Date Range Reports (Payments → Reports repository) | 积加 财务利润分析 "是取值日期范围报告中的数据", collected by "RPA或者插件" | **No SP-API report type** (`04-job-money.md` §1) | 积加 reaches a Seller-Central-only report by browser automation; see *What only Seller Central shows*. |
| `GET_FBA_STORAGE_FEE_CHARGES_DATA`, `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` | 领星 ("仓储费报告、长期仓储费报告"); 赛狐 allocation keys "月仓储费占比", "长期仓储费占比" | **Amazon Fulfillment or Pricing** (either) | Pricing is a role sellers already tick. |
| `GET_FBA_REIMBURSEMENTS_DATA` | Recovery vendors in general (none names it on the pages read) | **Amazon Fulfillment or Pricing** | Same. |
| `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` | Not named by tools read | Amazon Fulfillment or Pricing | — |
| `GET_LEDGER_DETAIL_VIEW_DATA`, `GET_LEDGER_SUMMARY_VIEW_DATA` | Recovery vendors' "FNSKU reconciliation" (GETIDA) implies it; none names it | Amazon Fulfillment only | — |
| Data Kiosk (`createQuery`) | None of the tools read names Data Kiosk | Brand Analytics (Data Kiosk ops) | The dataset-level role for economics is the economics seat's. |
| Ads API | Sellerboard blog ("a separate interface from SP-API"); Helium 10 (snippet: Sponsored Brands "at the campaign level") | Not SP-API; another seat's | — |

Two pitfalls the tools name that Amazon's docs do not state in these words:

- **Time zone.** Link My Books: settlement reports "are in UTC time zone" while business reports use marketplace time, giving "a 1-10 hour window" of mismatch. Finaloop: "Finaloop records transactions and presents your reports in UTC", while Amazon North America uses PST [opinion].
- **Shipment report lag.** 领星: "亚马逊配送报告会有3天数据延迟" [opinion].

## What practitioners add

All [opinion] unless marked. Each item is a fact about what a named tool or person says or does.

### 1. English bookkeeping connectors (settlement → ledger)

| Tool | Money job | How it splits and books | Dating | Reserve / deferred | FX | COGS |
|---|---|---|---|---|---|---|
| **A2X** | Settlement summary journals; accrual add-on for deferred | Default mapping (support 6008311): Product Sales → income "Amazon Sales"; Refunds → "Amazon Refunds"; reimbursements → income "Amazon Reimbursements"; "Cost of Advertising" → expense "Amazon Advertising"; storage under "Fulfillment and Warehousing" → "Amazon FBA Fees"; inventory placement under "Amazon Delivery and Transport" → "Amazon FBA Fees"; "the monthly Amazon subscription fee" → "Amazon Seller Fees and Charges"; "Reserved Balance" → current asset "Amazon Reserved Balances". | "A2X will split the settlement data according to which month the sales or fee actually occurred in". | "Reserve balance transactions are neither sales nor expenses" [command-verified]. Deferred adjustment "accrues transactions deferred during the month / reverses transactions released during the month", "generated on the 5th day of the following month", from April 2025 [command-verified]. | "The conversion to your home currency happens in your accounting software." | Seller-entered or synced cost × quantity sold, one entry, months split; no FIFO named. |
| **Link My Books** | Settlement summary invoices; deferred add-on (£15/account/month) | "Amazon bank deposits are net cash payouts, not gross sales revenue". Deferred items to "LMB9d: Amazon Deferred Balances" (Other Current Asset). Reserve: "Current Reserve Amount … is Amazon holding the funds". | "Splits only ever happen at calendar month end"; earlier parts are rolled forward into the final part. | As left. A negative balance can be offset by a cross-marketplace debt adjustment. | Posts in the original currency (see §C above). | "landed product costs" per settlement "COGS Bill"; it "does not reverse the original COGS entry" on a refund. |
| **Synder** | Per-transaction sync or summary (day, month, payout) | Reserve as a Transfer to an asset "Balance Reserve". In QuickBooks Online multicurrency the sync "can fail, since the 'from' and 'to' accounts must be in the same currency". | Two dates: "Sales/Invoice Date" and "Payment/Cash Date". | "Synder can only import transactions that Amazon has 'released'". | "converts them to home currency using Amazon's exchange rate". | Computed per sale from uploaded costs; method not named. |
| **Webgility** | Orders posted one by one or in summary; the settlement posted as a Bill/Expense; net deposit as a Transfer | Definitions (help 7000560): Revenue = "Your gross sales minus refunds"; Gross profit = "Your revenue minus your COGS"; Cost of sales = "All fees, including processor, selling, and advertising"; Net profit = earnings before tax minus taxes. Reimbursements go to an income-type account. | Orders: "Transaction date as Order Date". Settlement: "Payment Date will be Settlement End Date". | "Record your reserve as a current asset because it represents money Amazon owes you". | A multicurrency setup is needed in the ledger. | Item cost synced from QuickBooks. |
| **Taxomate** | Settlement invoices split by month (the split can be turned off) | Reserved Balance "is a balance-sheet account", also taking "Transfer of funds unsuccessful" and "Cross-Account Debt Adjustment". "Successful Charge is usually any money you've paid Amazon through your credit card". Reimbursements as Other Income (blog). Advertising: "keep separate from other Amazon fees". | Split to "match the sales and the related fees to their own months". | As left. | "can import up to 18 months of conversion rates used by Amazon"; Xero rates for older settlements. | "FIFO is our default recommendation" (blog). Its advice on basis: "Start with cash basis … Switch to accrual when you hit $250K". |
| **Finaloop** | Full ledger, cash or accrual ("defaults to cash basis until you confirm your method") | Funds held go to "Undeposited funds on hold". Ads appear as "Ad payment via seller account". | Accrual: "Revenue and COGS are recognized when the order is fulfilled" (fulfilment date from 2026-01-01). Cash: release dates. Periods from 2024-10 to 2025-12 "are not retroactively restated". | As left. | "spot rate at the time of the transaction" to USD. | FIFO from POs with landed costs ("InventoryIQ"). |

Sources: A2X support articles 11698773, 1828440, 6008311, 959828, 959816, 1136907, 8871866 and hub pages; Link My Books help 4155809, 12080631, 4184943, 12086764, 2570701, 3490105, 3447820 and blog; Synder help and integration pages; Webgility help 8011616, 7000560, 8780600 and blogs; Taxomate docs 6180397, 8752420, 12005966, 6180400, 6181560 and blog; Finaloop help 15070376, 10499774, 9813151, 6636161. Full URLs are in *Pages read*. None of the six names an SP-API report type or Data Kiosk in what was read, apart from A2X's V1/V2 format note.

### 2. English profit dashboards

| Tool | Definitions as published | Allocation | Dating, deferred, FX | COGS |
|---|---|---|---|---|
| **Sellerboard** | Gross Profit = "Sales − COGS − Refund costs − Advertising costs − Amazon fees − Shipping costs − VAT (EU only)"; Net Profit = "Gross Profit − Expenses"; margin is net profit over sales, optionally on net-of-VAT sales; "Estimated payout" is a "Projected Amazon disbursement" (no method). A separate Cashflow module: "Profit shows performance; Cashflow shows liquidity and timing". | Storage optionally "distributes your total FBA storage fee evenly across each day of the month" [command-verified]. Indirect expenses go to a marketplace or to products, "evenly across the selected time period". Ads are split by type; the Sponsored Brands key is not found. | Refunds are matched to orders. Deferred refunds are shown, then moved to their release date, "which can retroactively change past profit figures"; an option "hides deferred refunds until they are officially released" [command-verified]. FX: "based on the exchange rate from the last day of the selected reporting period" [command-verified]. Each marketplace is calculated independently. | Batches with receipt date; FIFO, weighted average or by period; "Historical orders are recalculated accordingly". |
| **Helium 10 Profits** | No formula found (knowledge base 403). | (snippet) Sponsored Brands at campaign level because the Ads API "aggregates spend and sales data at the campaign level"; storage left out of product performance "because these fees are applied at the store or account level". The account P&L tool covers storage, aged surcharge and all ad types at account level (blog 2026-08-12). | Not found. | (snippet) Dated cost periods with product cost, shipping and tariff, or "Persistent COGS". |
| **Jungle Scout Sales Analytics** | (snippet) Gross Profit = revenue minus unit cost, supplier shipping, FBA inbound shipping, miscellaneous cost and order fees; Total Profit = sales − COGS − operating expense. "Order Fees represent fees at the SKU level, while Seller Fees are charged at the company level". | As left. | (snippet) Pending units are estimated "based on your past sales history" and replaced once shipped. | "Effective From" dated costs; "Since Product Launch" back-fill. |
| **SellerApp** | "Gross Profit = Sales Revenue – (Cost of Goods + Shipping + Amazon Fees + Variable Cost)"; "Estimated Payout = Revenue – Total expenses"; "Net Profit = Sales Revenue – (Cost of Goods + Shipping + Amazon Fees + Variable Cost + Expenses)", where "'Expenses' include discounts, Amazon Fees, and ad spend"; "ROI = (Gross Profit ÷ Cost of Goods) * 100%"; "The Net Profit is calculated once every 24 hours" [command-verified]. | — | — | — |
| **ShopKeeper** | Final line "Profit after Adjustments and Refunds"; display toggles leave it unchanged. | — | (snippet) Display currency at the latest Yahoo Finance rate. | Per ASIN and marketplace; cost periods. |
| **SellerLogic** | — | — | "Order view… based on the order creation date"; "Transaction view… Recalculates data according to the actual transaction dates"; "Estimated transactions remain tied to the order creation date". | — |
| **tool4seller** | — | Sponsored Brands keys: products in the creative, click share or sales share (via `04-job-money.md`). | Two modes: Standard counts only Released transactions; Enhanced counts Deferred ones and "The transaction continues to be reported based on its original transaction date" [command-verified]. | — |
| **Fetcher** | Closed: "Fetcher officially closed on September 15, 2021"; its technology went into Jungle Scout. | | | |

A [seat] observation on SellerApp: as published, "Amazon Fees" appears in both the Net Profit bracket and its "Expenses". Read literally the fee is counted twice. This is a reading of the formula text, not a tested behaviour.

### 3. Recovery and financing

- **GETIDA.** "sole focus is Amazon FBA reimbursements"; "performance-based pricing starting at 20%"; "first audits the past 18 months worth of Amazon FBA transactions" (the page does not mention Amazon's 60-day windows). Claim types: Disposed, Lost Warehouse, Damaged Inbound, Inbound, Inbound Retro, FNSKU Reconciliation, Lost Removal Order, Cancelled Shipping Costs, Pick & Pack overcharge (US), Wrong FNSKU Returns, Lost in Transit. Its own figures: "more than 90% of claims we open" are reimbursed. https://www.getida.com/pricing
- **Seller Investigators (Carbon6).** "only pay a 25% commission fee when your money is back". Categories include "unfair reimbursements" (underpaid claims), "Refunded orders (not returned within 60 days)" and "chargebacks not refunded". Carbon6 today lists 15 products. The money ones are Seller Investigators, ChargeGuard (1P vendor chargebacks) and ManageByStats ("Analyze and optimize your Amazon profits"). https://www.sellerinvestigators.com/ ; https://carbon6.io/
- **Threecolts.** Margin Pro FBA reimbursements: "Typical fee share ranges 15–25%"; "audits up to 9 months of data"; reads "receiving scans, weight/size fees, transfer records, and disposal events". Seller 365: commission "ranging from 5% to 15%" by plan; "scan your settlements, inventory records, and inbound shipments". Its own unsourced figures: "FBA sellers see 1-3% of their revenue vanish" and "we've found sellers recover 40% of what they're owed".
- **Helium 10.** Managed Refund Service: "the last 18 months of FBA transactions". The fee is 15% (Diamond) and 18% (Platinum) on the service page, but the pricing page reads "Included | 15% fee" (Platinum) and "Included | 10% fee" (Diamond): the vendor's two pages conflict. Refund Genie is self-serve, no commission, and "does not include Inbound FBA shipment discrepancies".
- **Refunds Manager.** Today's homepage is about vendor (1P) and Walmart deduction recovery: "Shortage deductions", "Co-op & agreement fees", "Chargebacks". No FBA claims face was found.
- **Payability.** "Each day we advance 80% of your previous day's payouts into your Payability account. The remaining 20% is made available once the marketplace payout is received." The supplier terms cap the purchasing commission at "eight percent (8%)" and the advance rate at "ninety percent (90%)". The seller must redirect the marketplace payout ("directs and instructs each Marketplace to remit payment" to Payability). No page mentions DD+7 or reserves.
- **8fig.** Revenue-based "Growth Plan"; reads "View access to select reports on your primary selling platform" plus bank transactions; cost "usually between $6,000-$10,000 for every $100,000".
- **Shulex.** An AI customer-service product ("企业级 AI 客服员工"). It does no money job.

What the recovery pages share [seat]: none states how it values a claim against the seller's COGS. Since 2025-03-31 Amazon values lost pre-sale stock at the manufacturing cost the seller enters, or at Amazon's estimate. So the seller's IDR-portal entry, not the vendor, sets the ceiling (`04-job-money.md` §4.4).

### 4. Chinese ERPs

**领星 Lingxing** (fullest public docs, lingxing.com/help):

- **Two profit reports.**
  - 订单利润 aggregates "以下单时间按照订单号+MSKU", updated "每15min".
  - 结算利润 "按照订单号+结算编号+结算时间+MSKU整合亚马逊结算中心-交易明细".
  - Since 2026-08-13 a switch: "利润报表支持结算时间、发货时间与预结算三种口径灵活切换" (AMZ123 release note by 领星ERP, verified 2026-11-10). The help page (ProfitStatementnew) says the ship basis is 「本次新增」, the default stays settlement time, and ship time is read from 「亚马逊 Transaction 报告中的 Date/Time」.
- **Formulas.**
  - Order gross profit sums sales, refunds, buyer shipping, promotions, platform fees, FBA fees, other order fees, ads, purchase cost, first-leg cost and other cost, with fees stored negative. Margin = "毛利润/销售额".
  - In the settlement report the formula is configurable. Margin = "毛利润/（平台收入）", where platform income depends on the configured income items.
  - "含税毛利润=毛利润+销售税+销售税退款额+市场税+市场税退款额+混合网络费".
  - ROI = "订单毛利润 / (采购成本 + 头程费用)".
- **Allocation.**
  - Default by sales share. The base "是（FBA销售额+FBM销售额）" [command-verified].
  - Ads by each MSKU's share of that day's store sales; SB/SBV tied to campaign ASINs.
  - Storage by sales, units, business report or 计提 (accrual), and by billing month or month incurred.
  - Subscription and other store fees "在此店铺下所有MSKU分摊".
  - 头程 chosen per shipment: "计费重，实重，体积重，数量，自定义". It includes logistics, taxes, port and clearance fees.
- **Dating.** Refunds can be dated "按实际退货（退款）时间…按下单时间".
- **Deferral (预结算).** "提前将本月应结算，但是被亚马逊推迟的订单提前计入对应月份利润报表，在结算后自动将其剔除".
- **Reserve, as 领星 describes it.** "依据店铺最近28天的销售额的5%从本期转账金额中扣除…目前无法预判预留金额，且亚马逊无提供实时的预留金额" [command-verified].
- **FX.**
  - Settlement summary: "取值的是结算开始时间对应月份的月初汇率转换的，不是转账时间对应月的汇率" [command-verified].
  - Cost: "业务发生当月的我的汇率". The official rate updates hourly; a month with no user rate inherits last month's.
- **Cost method.** "移动加权平均、先进先出两种计价方法可以切换，切换后需要将所有月份重算", in CNY. Month close (结账/反结账) freezes costs.
- **Retention.** "结算中心仅同步最近3个月数据".
- **Price.** Free while ≤5,000 orders a month.
- **Why it differs from Amazon.** Rates stored to two decimals; ad report vs actual ad charge ("差异分摊"); payout account in another currency; the 3-day shipment-report lag.

**积加 Gerpgo** (help.jijiaerp.com):

- 财务利润分析 reads the Date Range report via "RPA或者插件", refreshed overnight for "近39天". 销售利润分析 is "直接从亚马逊API接口获取".
- **Formulas.** "销售净毛利: 销售毛利 + 仓储费 + 广告花费" (fees negative); margin "销售毛利/销售额".
- **Allocation.** Other fees "按照具体日期的销售额分摊，如果当日无销售额或销量则不分摊". Sales-profit storage "采用日均分摊的方式，分摊上个月的完整仓储费到当月的MSKU". Ads = SP + SD + SB + "广告差异分摊金额"; credit-card ad invoices go to the "发票开具日期" month.
- **Dating.** Financial profit dates refunds and long-term storage "以结算时间统计". Sales profit dates refunds "按照订单退款时间统计，而不是订单订购时间统计".
- **Reconciliation.** The V2 settlement total is reconciled against the Date Range report ("通过：V2报表的结算金额与日期范围报告一致"). FX: "取“结算周期开始时间”所在月份的月汇率换算" [command-verified; page modified 2026-11-06].
- **Cost.** FIFO or custom.

**赛狐 SellFox**:

- **Bases.** The profit report runs "按结算时间、预计结算时间、转账时间和订购时间", and its order view 「支持按结算口径和发货口径查看数据」 [verified on https://www.sellfox.com/help/features/profit-statement, 2026-11-10]. It pulls daily deferred-transaction data and rejects "DD+7推测的临时方案" (blog 2026-08-13).
- **Timing.** Last month's report lands "每月2号-5号" (not found on the profit-statement page as read 2026-11-10, which now says it 「能即时获取最近一天的完整结算数据，不必等到结算关闭」; source page for the 2–5 line not identified).
- **Allocation keys** ("均取自亚马逊结算报告") [command-verified]:
  - FBA sales share;
  - FBA+FBM sales share;
  - "月仓储费占比";
  - "长期仓储费占比";
  - custom ASINs;
  - plus rules for Lightning Deal fees (by promotion report) and Vine ("往前推30天找vine订单中的产品进行均摊").
- **Why its two views differ.** "【销售利润】是按订单的订购时间统计的，包含了Pending,Shipped,Unshipped三种状态的订单，【利润报表】是按结算时间统计的，指包含Shipped订单".
- **Price.** Free to 3,000 orders a month; paid tiers by annual order volume.

**Others:**

- **易仓 ECCANG.** Settlement report "对接Amazon官方接口"; fixed or batch cost; Kingdee voucher sync to the general ledger. 2025-07 update: monthly and long-term storage allocated separately; 头程 by quantity; estimated vs actual 头程.
- **店小秘.** "利润 = (平台总收入 + 其他收入) - (平台总支出 + 其他支出) + 平台调整"; cost "优先取出库成本"; imported fees allocated by SKU units, sales, volume or weight share.
- **马帮.** Daily settlement pull, configurable allocation; no formulas published.
- **通途.** No public finance docs.
- **旺销王.** AliExpress-style order profit; nothing Amazon-settlement-specific.
- **紫鸟.** A browser and account-management product with no money job.
- **店铺管家.** No site found.

### 5. Chinese sellers' practice (大卖财务)

- **Revenue is gross, not the payout.**
  - 轻松财税 (新浪, 2026-08-04) calls "直接按照平台提现净额确认主营业务收入" the "错误旧做法（绝大多数卖家现状）". It requires "按客户支付全额交易总额" and keeps "会计确认、增值税申报、资金回款三条独立口径", noting "金税四期一比对就预警".
  - Yiju谈跨境 (雨果网 180164, 2025-11-03): "必须按照销售额申报，包括平台未回款的部分".
  - 36氪 / 品牌工厂 (2025-10-16) on platform reporting to tax authorities: "过往的申报数据将与平台回款数据形成直接对比…触发税务预警".
- **DD+7 changed the month.** 闯盟跨境 (雨果网 185409, 2026-04-23): "当月总销售额 = Released（已到账）+ Deferred（延迟/预留）… 不再是 “到账才算收入”，而是按订单发生月统计". 侃侃跨境 (雨果网 169921, 2025-01-08) quotes a seller: "自从延迟交易的订单不计入当月账单后，我的账单就变得一团糟".
- **Commission vs held cash.** 谦亨跨境 (知无不言 101964, 2025-02-09): finance says "这笔钱还在店铺冻结" while operations wants commission on the sale; "没有一个非常完美的解决方案".
- **FX (结汇, 汇兑损益).** 金方圆财务 (搜狐, 2026-05-19):
  - book at "当月月初汇率或结汇当日汇率，统一核算口径", "全年不得随意变更";
  - the settlement difference "计入财务费用汇兑损益科目";
  - "月末按照官方中间价调整外币账面金额";
  - "平台扣费必须单独入账，不可直接冲减收入".
- **Collector fees (dated 2023).** 跨境内参 (雨果网 139307, 2023-01-31): 万里汇 "0.3% 封顶", 连连 "0.7%", PingPong "1%". There are no current figures; see *Facts for human readers only*.
- **Export tax routes.** 优品跨境物流 (AMZ123, 2025-11-19):
  - 0110 "退税率最高（10 %-13 %）";
  - 1039 "免征增值税…0.4 %-1 % 的核定征收";
  - 9610 above 5,000 yuan per shipment converts to general trade;
  - 9810 fits FBA;
  - 买单出口 "无法完成合规申报".
  - The 9810 pre-refund rule is State Taxation Administration Announcement 2025 No. 3 (2025-01-27).
- **头程 and benchmarks.** 远道知识产权 (卖家之家 57558, 2021) sets 头程 at "一般我们定在5%-7%" of price and storage at "2.5%". These are one firm's targets.
- **Inventory valuation in tools.** FIFO, moving weighted average, month-end weighted average; closed periods frozen (AMZ123 百科 on 领星, 2025-09-22).
- **TACoS.** AMZ流量君 (雨果网 60233, 2020): "（广告支出/总收入）x100"; "ACOS只能说明广告系列的整体情况". 跨境电商优匠学堂 (卖家之家, 2025-11-04) gives bands (<10% excellent, 10–20% moderate, >20% high). The ads playbook owns TACoS (`ads-playbook/research/beyond/goals-and-economics.md` §J).
- **Reimbursement value.** Rayna (白鲸出海 51162, 2024-12-23, written before Amazon moved the date to 2025-03-31): from 2025-03-10 lost or damaged stock is reimbursed at "制造成本", which "不包括运费、手续费、关税"; with no seller cost, "亚马逊将默认使用估算".
- **De minimis.** 无招 (36氪, 2025-09-12): one seller's tariff cost "直接跃升约25%", margin "从25%降到了个位数". This is one seller's figure.

### 6. Named English practitioners: what sellers most often get wrong

| Mistake | Who says it, where |
|---|---|
| **Counting the deposit as revenue** | Amy Crooymans (A2X, 2025-01-17): the settlement "is not only made up of "sales"". Dan Little (Link My Books CEO, 2026-05-07): sellers book the payout "as "Sales" or "Revenue"". Wayne Richard (Bean Ninjas, 2024-01-20): "recognizing income based on net deposits rather than true sales figures can be misleading". Taxomate blog: "that $10,000 deposit isn't $10,000 in revenue". |
| **Settlements that straddle months** | Dan Little: "A single 14-day settlement period often crosses over two different calendar months" [command-verified]. Colleen Quattlebaum (ConnectBooks, 2026-07-02): "Identify any settlement cycle that straddles month-end" [command-verified]. |
| **Reserve and deferred ignored** | Geoffrey Gualano (A2X, 2025-08-18): "as much as 20-25 % of your revenue can slip into the following month"; "If COGS post weeks after inventory ships, your gross profit for the original month is wrong". Quattlebaum: "Carry the unreleased reserve as a balance-sheet asset, not as P&L" [command-verified]. Stefan Dobrev (Link My Books, podcast): "Reserves held on the account can delay part of the payout". |
| **Sales tax / VAT as income** | Denym Bird quoting Crooymans (A2X, 2022-06-06): "Sales tax doesn't belong in a profit and loss sheet. It needs to be in a liability account"; "over 400 different transaction types" in one payout. Crooymans (2025-01-17): don't treat "the VAT received on your payouts as additional revenue". |
| **Reimbursements as sales** | Quattlebaum: "reimbursements as recoveries, not sales" [command-verified]. A2X: "Reimbursements should be recorded separately from sales" as "other revenue". |
| **Missing reimbursements** | Yoni Mazor (GETIDA, MWQHJ #449, ~2023): "1% to 3% of gross revenue every year". Himanshu Gaba (Helium 10, 2026-08-13): "Money you do not claim in the window is gone for good". On dimensions, Gaba says "Amazon gets it wrong constantly" and Mazor says "starts billing higher fees on every future unit". |
| **Cash basis / bank-balance accounting** | Matt Remuzzi (CapForge, Helium 10 podcast #287, 2021): "accrual basis, done correctly". Ellen Main (Bean Ninjas, 2020): "bank balance accounting". Sam Hill (EcomCFO, 2022-11-16): the switch to monthly accrual "may be the most important investment". |
| **Fees inside COGS** | Sam Hill: "Variable expenses should not be considered when computing the cost of goods." |
| **ACoS without TACoS; ads as optional** | Chuck Kessler (Canopy, 2025-10-10): "TACoS is a business health metric". Sam Dillon (Eightx, 2026-07-06): "If you are not budgeting ad spend as a fixed cost of the channel, your modeled margin is fiction"; "15% is the starting bid, not the settlement". |
| **Freight expensed instead of capitalised** | Sellerboard blog (2026-08-10) and beancount.io (2026-05-14) (snippet): freight, duty and brokerage belong in inventory and are released through COGS. |
| **A month is not final at close** | Sellerboard blog (~2026-09-04): "A month is not truly final until refunds and fee assessments against it have stopped arriving"; it suggests about 90 days provisional. |

Most of these voices sell a tool that fixes the mistake they name. That is the main bias in this section.

### 7. What large sellers do that small ones don't

These are practices as named sources describe them; none is a rule.

- **Month-end close as a checklist.** ConnectBooks' seven steps: reconcile each settlement to the bank; split straddling settlements; FIFO COGS; count inventory "across all locations: FBA, in transit, 3PL, and your own warehouse"; post fees and ads, including card-paid ads; separate marketplace-facilitated tax; lock the period.
- **Closing periods in the tool.** 领星 结账/反结账 and frozen cost data; 积加 关账 and 月结算.
- **Two profit bases kept side by side.** An operator's order-time view and finance's settlement-time view (领星, 积加, 赛狐). 领星 adds a ship-time basis matching batch cost by ship date.
- **Reconciliation against Amazon's statement.** 领星 against the Summary PDF ("提供与summary月度账单的对账功能"); 积加 V2 settlement against the Date Range report; manual reconciliation from "后台-付款-日期范围报告" (知无不言 76282).
- **Multi-entity and FX.** Fractional-CFO pages list consolidation across marketplaces, intercompany, transfer pricing and "FX hedging accounting" (Eightx, snippet). No independent source on how sellers hedge was found.
- **Fee audits.** Dimension and weight audits (GETIDA, Threecolts Margin Pro: "weight/size fees"); inbound placement-fee and mislabel errors (Margin Pro). The Amazon route and window are `04-job-money.md` §4.2.
- **Tax compliance (China).** Gross-revenue declaration, three bases kept separate, 9810/1039/0110 export routes, quarterly platform data reporting from 2025-10.

Added by the verifier (2026-11-10), each a fact about a named source, none a rule:

- **Multi-entity structures (Chinese large sellers).** 跨境电商跨境屋 (AMZ123, 2026-06-01, https://www.amz123.com/t/KhfDMPaS): 「为什么跨境卖家要搞多店铺、多主体？…账号有关联风险，品牌要隔离，店铺要分散，收款要稳定，供应链、运营、采购又经常不在同一个主体下面」; the article reports a tax-authority guidance said to be circulating since 2026-04 (「圈里流传…《跨境电商企业涉税问题相关口径》」, not an official document read) and lists what it says a Hong Kong selling entity is challenged for lacking: 「没有独立办公地址。没有本地员工。没有强积金。没有董事会记录。没有业务决策痕迹。没有转让定价文档。没有ODI备案和清晰的利润回流路径」. 跨境知道网 (AMZ123, 2026-05-30, https://www.amz123.com/t/ftaAgudr) names the same three documents (ODI 备案, 实质经营证明, 关联交易定价文件). What it means for a product's money [seat]: where the store's entity is not the entity that bought the goods, the store entity's COGS is an intercompany price, not the factory invoice.
- **Several Amazon accounts in one ledger.** A2X: "there are subscriptions that allow for many Amazon marketplaces and merchant IDs" (support FAQ, snippet, https://support.a2xaccounting.com/en/collections/379203-faqs). No vendor page read describes intercompany entries between seller entities.
- **FX hedging.** World First (via SellerEngine, 2015-01-28, modified 2019-09-04, https://sellerengine.com/sellerengine-mailbag-international-selling-forward-contracts/): a forward contract "gives you the option to lock in an exchange rate with your dealer in advance for your incoming funds from abroad"; "World First will book a forward under the condition … that you are locking in at least $50,000 for a minimum of two months"; "It's generally recommended that international sellers book a forward for a maximum of six months ahead" (dated vendor terms; human readers only). Airwallex (2025-09-27, https://www.airwallex.com/en-ca/blog/how-can-amazon-sellers-forecast-fx-impact-on-profits): "Airwallex provides tools to lock in favorable rates when market conditions align". Both are vendors of the service. The Chinese booking side (one rate rule held for the year, 汇兑损益 to 财务费用, month-end revaluation) is 金方圆财务's (§5).
- **Month-end close calendar.** A2X's deferred adjustment is "generated on the 5th day of the following month" (§1); Sellerboard calls about 90 days provisional (§6); 领星 and 积加 lock periods (结账/关账). Amazon's own `finance-month-end-closer` skill (2026-10-08, repo `amzn/selling-partner-agentic-toolkit`) refuses the current month and classes settlements as inside / straddling / open at month end (`07-reuse.md`; the reconciliation sibling owns it).
- **Fee audit against the rate card.** Amazon's measurement sets size-tier fees and a dimension-based fee reimbursement must be requested within 90 days of the charge (fulfilment-charges.md P-ful-2, Amazon's pages). The economics dataset returns each fee's `properties` (example: "Product Size Tier") per SKU, and the Fee Preview report gives Amazon's measured dimensions and tier (fulfilment-charges.md), so the charged tier can be set against the published rate card; the recovery vendors sell this as "Pick & Pack overcharge" and "weight/size fees" audits (§3).

### 8. Where tools disagree with each other or with Seller Central, and why

| Disagreement | Cause the tools give | Source |
|---|---|---|
| Profit view vs payout | "Payments is a deposit, calculated from a much narrower set of inputs"; "Refund timing creates a lag"; "Neither number is wrong — they're answering different questions" | Sellerboard blog ?p=3570 |
| A tool's two profit views | Order time including Pending/Unshipped vs settlement time with Shipped only | 赛狐 difference explainer |
| Connector vs Seller Central's Date Range Summary | Amazon's summary includes deferred transactions; the connector books only settled ones until the deferred adjustment is on. MCF orders "may be missing for periods prior to May 2024". | A2X support 8871866 |
| Connector vs Seller Central totals | "is never an exact match": timing, UTC vs marketplace time ("1-10 hour window"), DD+7 | Link My Books 4155809 |
| Connector vs Amazon's dashboard | "our organization method is different from Amazon's method on their dashboard" | Taxomate 8752420 |
| ERP vs Amazon's statement | FX rate rounding to two decimals; ad report vs actual ad charge ("差异分摊"); payout account currency; 3-day shipment-report lag | 领星 MonthlyProfitReportnew, SettlementCenter, ShipSettlVarReport |
| ERP financial profit gaps | Date Range report not synced "当RPA或者插件存在问题时" | 积加 fPlZrZZp |
| Ledger vs Amazon NA | Ledger in UTC vs Amazon NA in PST; spot FX; cash vs accrual | Finaloop 15070376 |
| Amazon SKU Economics vs settlement | A seller reports that only Sponsored Products ads appear and that FBA fee quantity differs from units sold | Amazon News thread (seller reply) |
| Helium 10 product view vs account | Storage and Sponsored Brands excluded from product performance because charged at account or campaign level (snippet) | Helium 10 KB 360056383594 |
| Vendor claim windows vs Amazon | Helium 10's 2024 blog: returns "between 60-120 days"; Amazon's US notices: 45–105. GETIDA and Helium 10 MRS advertise 18-month audits. | Helium 10 blog [command-verified]; `04-job-money.md` §4.3 |
| Vendor fee pages vs each other | Helium 10 MRS 15%/18% on the service page vs 15%/10% on the pricing page | Helium 10 pages |
| Reimbursement valuation date | Amazon first announced "Effective March 10, 2025", then moved it: "will now go into effect on March 31, 2025, instead of March 10, 2025" (2025-02-28). Vendors still writing March 10 (白鲸出海 2024-12) predate the move. | Amazon News posts …/68864b6f-… and …/ed8abc33-…; refunds sibling E4 |
| ERP's documents in 金蝶 vs the ERP's own screens | "亚马逊数据变动引起": the last ~5 days are unstable, and the ERP may re-collect last month ("重采"). 领星 advises pushing next month, or a sync window of "前7天-前7天". | 领星 KingdeeIntegration (§9) |
| 金蝶 FBA stock vs Amazon's inventory ledger | 金蝶 data come from 领星's cost flow, so 领星 can confirm agreement with that flow but "无法保证和库存分类账的一致性" | 领星 KingdeeIntegration (§9) |
| 金蝶 receivable vs Amazon's settlement view | The receivable is pushed either as one monthly fee-receivable from the profit report or line by line from settlement detail. The two modes use different fee-item codes, so the totals per item differ by mode. | 领星 KingdeeIntegration (§9) |
| Vouchers by calendar month vs settlements every 14 days | "亚马逊14天结算 vs 金蝶自然月需做周期切割" | 轻易云 case article (§9) |
| Ledger RMB vs Amazon's conversion | The ledger converts at a booking rule held for the year and revalues month-end at the official middle rate. Amazon converts per transfer. | 金方圆财务 (§5); 轻易云; CAS 19 (§F) |

### 9. From the ERP to the general ledger: 金蝶 Kingdee and 用友 Yonyou (added 2026-11-10)

Large Chinese sellers close their books in 金蝶 (云星空 for mid-to-large firms, 云星辰 for smaller ones) or 用友 (YonSuite, U8; 畅捷通 is the group's small-business arm). The ERP (领星, 积加, 易仓, 赛狐) holds Amazon's data and pushes it into the ledger. Neither Kingdee nor Yonyou publishes an Amazon connector page that was found. What is public is the ERPs' own integration docs, Kingdee's voucher-template manual, integration vendors' case articles and accountants' columns. All [opinion] unless marked.

**领星 → 金蝶云星空** (the fullest public document; 领星 help *金蝶云星空集成*, https://www.lingxing.com/help/article/KingdeeIntegration, page created 2023-04-04 per its metadata, read 2026-11-10 [command-verified: plain GET, text matched]):

- **It pushes documents (单据), not vouchers.** The 凭证 is then made inside 金蝶 from those documents. The flows on the page:
  - 销售订单 → 销售出库单, "根据站点发货时间，按店铺+订单+按天维度推送发货流水";
  - 退货订单 → 销售退货单, by return time;
  - 收款单 from "财务-亚马逊结算中心-结算汇总-已转账状态";
  - FBA shipments, receipts, removals, stock counts and transfers → 金蝶 transfer and other in/out documents, from 领星's cost flow ("成本流水（来源为库存分类账）").
- **Two receivable modes, switchable** ("云星空集成-参数配置-单据内容-财务"):
  - "对接店铺月利润报表（默认选项）": "店铺每月利润报表，按月推送一张费用应收单", pushing "平台收入、平台支出和税费，推送维度为利润报表的二级子项";
  - "对接结算中心结算明细": "销售出库的结算数据推送标准应收单，支持标准应收与销售出库勾稽；非销售出库的结算数据推送费用应收单". On a standard receivable, "每一笔明细金额都按映射规则映射为summary项目，记录在标准应收单的备注". It separates "结算与发货相匹配的结算流水（结算类型=已发货xx月已结算）", which can be linked to the 销售出库单, from "未发货已结算", which cannot.
  - "由于两个模式费用项目编码不一样", switching re-pushes new fee-item codes. The full code list is "请联系实施顾问获取" (not public).
- **Matching receipts to receivables.** "自动核销：支持同一账期内的应收和收款按支持相同结算编号核销".
- **Timing.**
  - Push by order, day or month. Day data arrive "最早于次日推送", and month data "最早于次月3日推送".
  - "对于当月FBA签收、串票、负数签收、未发货业务，最早可于次月6号推送". FBA counts, removals and transfers are pushed "延迟5天".
  - Negative-stock and reconciliation-difference adjustments: "次月6号才允许推送上月的".
- **Why the ledger and the ERP differ, in 领星's words.**
  - "亚马逊数据变动引起"; "一般是近5天的数据不稳定，但也有可能出现偶发重采的情况". The suggested sync window is "前7天-前7天或者前6天-前7天", and a changed document is fixed by "删除单据，重新推送".
  - "仅支持将金蝶数据和系统数据核对，不支持直接和库存分类账核对…无法保证和库存分类账的一致性".
- **Setup facts.**
  - Master data: 金蝶 materials, customers, suppliers, bank accounts, warehouses and organisations are synced in.
  - Pairing is one-to-one: "SKU、本地仓库可以领星一对多金蝶配对吗？…不支持".
  - Document status can be 暂存 / 保存 / 已审核, with "金蝶暂存接口易出错".

**金蝶's own voucher template** (金蝶云产品手册 *凭证模板*, 智能会计平台, https://help.open.kingdee.com/dokuwiki/doku.php?id=凭证模板, read 2026-11-10 [opinion: Kingdee's own manual; command-verified text]):

- "凭证模板用于设置凭证各要素的取值规则，如凭证日期、凭证字、摘要、科目、借贷方向及金额等"; "系统预置了日常经营活动常用的凭证模板，用户可以根据企业的实际情况修改或细化".
- **Account rule.** "定义凭证分录行的会计科目（核算维度、现金流量项目）的取值规则以及科目影响因素的来源字段". An entry can be conditional, and document lines can be merged.
- **Voucher date.** It can come from the document date, "总账凭证日期取系统当前日期", or "总账凭证日期取期间最后一天".
- **Close gate.** "必须生成总账凭证…勾选此标识，总账结账时会检查该类单据是否已生成总账凭证，若未生成总账凭证则不允许结账".
- **Chart changes.** "若用户对【科目】基础资料进行了修改，则建议对凭证模板的科目字段进行相应修改，不修改可能会导致生成凭证失败或错误".

**金蝶云星辰 (Kingdee's small-business line)** on its own site, in a 2025-10-10 article on cross-border ERP selection, says "针对多币种业务，系统支持外币核算与自动计算汇兑损益" and "业务单据一键生成凭证". It names no Amazon connector. https://www.jdy.com/article/1976537696977367042.html [opinion: Kingdee's own page].

**易仓 ECCANG → 金蝶 (云星空, 云星辰).**

- "自动生成财务凭证，推送至金蝶（云星空、云星辰）".
- "凭证模板：提前设置，系统即可自动生成会计凭证".
- "自动将结算报告中的费用类目，归类到用户指定的费用项上".
- Push is manual or by "自动推送开关" on a set time.
- "确认应收，自动对账：自动获取结算报告、回款明细".
- Its Amazon profit report's "数据来源和计算逻辑与亚马逊payment付款报告一致".

Sources: eccang.com/news/2390 (c. 2022-02); eccang.com/cwjq.html ("实现自动生成财务凭证流和单据流，并推送至金蝶ERP同步到总账"). Read 2026-11-10 [command-verified]. Unlike 领星's document flow, 易仓 says it produces the vouchers itself.

**积加 Gerpgo → 金蝶 / 用友 / SAP / Oracle.**

- "自动推送至金蝶、用友、SAP、Oracle 等财务系统".
- On push it can "按维度汇总明细数据". Its example: "以日期范围报告为例，可在半小时内完成推送".
- It markets to "亿级规模、准 IPO 及上市企业" a model of "积加 ERP + 金蝶、SAP、甲骨文、用友等财务厂商 / 服务商".

Source: jijiaerp.com news 510 (2025-09-10, framed by the State Taxation Administration's 2025-06-26 platform-reporting announcement). Read 2026-11-10 [command-verified]. Its finance product page names two customer cases, "积加 ERP +金蝶集成" (jijiaerp.com/products-and-services/finance). No public 积加 page was found that gives its voucher template or account mapping.

**How the reserve sits in the receivable (积加).** An explainer promoting 积加's 财务结算中心 (跨境知道, 2022-02-11, written by "小G") says:

- "应收账款余额 = 账户预留余额 + 净收入额";
- the reserve is "亚马逊暂扣、未结算给卖家的款项（一般在下一个回款周期里面进行结算）".

https://www.ikjzd.com/articles/1658378894475730945 [command-verified]. 万里牛 (hupun, 2026-09-20, user-submitted article) adds: "核算时把预留变动当作应收处理，不混入当期利润". https://www.hupun.com/articles/amazon-settlement-bill-fee-guide.html

**Integration vendors' case notes (轻易云 Qeasy, an iPaaS that sells these links; case articles, figures theirs):**

- **赛狐 → 金蝶云星空旗舰版** (qeasy.cloud/a/13573, c. 2026-04):
  - "亚马逊14天结算 vs 金蝶自然月需做周期切割";
  - settlement → "销售应收单" with "订单号、站点、币种、汇率、人民币收入";
  - costs and fees are allocated by SKU/MSKU to "主营业务成本/销售费用/广告费";
  - "月末重估价自动生成汇兑损益凭证" at the bank middle rate;
  - Kingdee "需要企业版或旗舰版" for the API (vendor's claim).
- **领星 → 金蝶云星空** (m.qeasy.cloud/a/13407, c. 2025-12):
  - the customer's books close "每月 6 号";
  - Amazon receivables are split "按“费用类型”拆分：销售收入、广告费、FBA 服务费、赔偿等";
  - Amazon receipts have no document number and are summarised "以“店铺+月份”做汇总，金额需与应收勾稽";
  - "仅退款不退货时生成“其他应收单”而非退货单";
  - 领星 suppliers lack a finance tab, so each is defaulted to "应付账款".
- **易仓 → 金蝶云星空旗舰版** (m.qeasy.cloud/a/13580, c. 2026-04):
  - "USD 销售额按当月记账汇率自动转为 RMB 记账金额";
  - 金蝶's own business-voucher rules generate the voucher once the 销货单 is approved.

**用友 Yonyou.**

- No Yonyou page on Amazon data was found.
- YonSuite's own article on cross-border multi-currency (yonsuite.com/infoNew/2250606355082.html) speaks of "实时汇率转换、自动生成多币种财务报表" in general terms.
- 畅捷通 (Chanjet, the Yonyou group's small-business arm) has a marketing article (service-ask.chanapp.chanjet.com/yxwz/d84c6a83292e4417829.html, undated in the extract). It says "订单佣金则与销售收入直接挂钩，通常作为销售成本的一部分进行核算". It also says period-end FX translation differences "应计入“其他综合收益”". [seat: under CAS 19 that applies to translating a foreign operation's statements (art. 12), not to a seller's own foreign-currency receivables (art. 11, 当期损益).]
- 积加 names 用友 as a push target (above).
- The previous note on a WorldFirst → Yonyou voucher claim stays unverified (`reconciliation.md`).

**Which P&L line Amazon's deductions go to: Chinese practitioners disagree.**

| Source | Revenue | Commission / platform fees | Ads, FBA, storage | Withdrawal / collector fees | Inbound freight (头程) | Reserve / held money |
|---|---|---|---|---|---|---|
| 轻松财税 (新浪, 2026-08-04) | Gross: "借：应收账款——亚马逊平台 / 贷：主营业务收入——跨境出口" | "借：销售费用—平台佣金 … 贷：应收账款——亚马逊平台" | 销售费用 ("销售费用—广告宣传费") | 销售费用 ("提现手续费（全部计入销售费用）") | — | The net amount clears 应收账款——亚马逊平台 on receipt ("借：其他货币资金/银行存款 / 贷：应收账款——亚马逊平台") |
| 金方圆财务 (搜狐, 2026-05-19) | Gross, "收入确认时间以平台结算完成时间为准" | "将亚马逊佣金、提现手续费…计入财务费用，单独设立手续费明细科目" | FBA storage "单独标注运营服务费" | 财务费用 | "头程运费、尾程配送费、报关杂费计入销售费用" | No reserve treatment stated; the accounts it names are "外币货币资金、跨境应收账款、平台扣费手续费、汇兑损益" |
| 百运网 by56 (undated) | Net of commission: "在销售收入中扣除佣金金额后确认净销售收入" | Deducted from revenue | "月费和广告费则作为销售费用"; FBA fees "分摊到销售成本中" | — | Included in purchase cost | — |
| 畅捷通 / 用友 group (marketing, undated) | — | "通常作为销售成本的一部分" | Storage "存货保管费用"; delivery "运输费用"或"销售成本" | — | — | — |

The CAS anchors (§F): CAS 14 art. 34 makes a principal recognise the gross amount; CAS 1 art. 6 puts "运输费" in inventory purchase cost. [seat] Where each practitioner's line lands changes the gross margin a 金蝶 or 用友 P&L shows: commission under 销售费用, under 财务费用, under 销售成本 or netted off revenue. It does not change net profit. A seller comparing the ledger's 毛利 with an ERP's 毛利 is comparing whichever line their accountant chose.

## Published research

[research]. Advocacy and industry analyses are marked as such.

**Take-rate analyses:**

- **Marketplace Pulse** (Juozas Kaziukėnas), 2023-02-13 (industry): "Amazon is pocketing more than 50% of sellers' revenue - up from 40% five years ago"; a typical seller pays "a 15% transaction fee (Amazon calls it a referral fee), 20-35% in Fulfillment by Amazon fees (including storage and other fees), and up to 15% for advertising and promotions" [command-verified]. https://www.marketplacepulse.com/articles/amazon-takes-a-50-cut-of-sellers-revenue
  - 2024-03-18: "50-60% of their sales" for a typical private-label seller.
  - 2026-04-16: active sellers fell from 584k (Jan 2025) to 500k (Mar 2026); fewer than 8,000 sellers produce half of US 3P GMV.
- **ILSR** (Stacy Mitchell; advocacy):
  - *Amazon's Toll Road*, 2021-12-01: "a 34 percent cut".
  - Update 2023-09-21: "Amazon's cut of sellers' revenue in the U.S. has soared to 45 percent" [command-verified]. https://archive.ilsr.org/?p=102720
  - No 2024–2026 update was found.
- **Fortune** (Jason Del Rey, 2025-02-07; journalism): seller fees were "more than 29% of Amazon's non-AWS revenue" in 2024.

**Regulators and courts:**

- **FTC et al. v. Amazon**, W.D. Wash. 2:23-cv-01495, filed 2023-09-26. It alleges "Anti-discounting measures that punish sellers" and "Conditioning sellers' ability to obtain "Prime" eligibility" on Amazon's fulfilment. The FTC says sellers pay "close to 50% of their total revenues to Amazon" (press release read through the fetch tool; a plain GET returned a stub). Trial is set for **2027-03-29**: "U.S. District Judge John Chun rejected Amazon's request on Friday, October 9, to move the federal trial from March 29, 2027, to June 2027, according to reporting by Bryan Koenig of Law360 and a separate report by MLex" (PYMNTS/CPI, 2026-10-11, https://pymnts.com/cpi-posts/amazon-loses-bid-to-delay-ftc-antitrust-trial-as-california-case-looms, read 2026-11-10; the court order itself not read). An earlier ruling confines the trial to liability, with remedies later (search).
- **FTC and states v. Amazon (Sponsored Ads "soft reserve")**, 2026-08-31. Amazon's response is on aboutamazon. This is the ads playbook's (`goals-and-economics.md` §E). Nothing has been tried.
- **FTC Prime settlement**, 2025-09-25: $1B civil penalty plus $1.5B refunds. This is consumer enrolment and cancellation, not seller fees.
- **California v. Amazon**, filed 2022-09-15: summary judgment on a cross-claim denied 2026-04-15; trial **2027-01-19**. It alleges sellers who price lower elsewhere lose the "Buy Box" (CA AG release 2026-04-16).
- **EU AT.40462 / AT.40703** commitments, 2022-12-20: equal Buy Box treatment and a second offer; "Prime sellers can freely choose their carrier and negotiate the terms"; Prime and Buy Box commitments run "seven years and six months" (via Cuatrecasas; the Commission PDF was unreadable).
- **UK CMA**, 2023-11-03: equal Buy Box treatment; sellers can negotiate their own Prime carrier rates; no use of rivals' data. Monitoring trustee approved 2024-02-05.
- **Bundeskartellamt**: decision B2-73/20 dated 2026-02-04, barring Amazon's price-control mechanisms on amazon.de, with a provisional €59M disgorgement; appeal to the BGH (KVB 13/26, snippet). Confirmed 2026-11-10 by beck-aktuell (2026-02-05): "Das Bundeskartellamt hat Amazon die Anwendung bestehender Preiskontrollmechanismen untersagt"; "rund 59 Millionen Euro", https://www.beck-aktuell.de/heute-im-recht/rechtsgeschehen/bundeskartellamt-preiskontrollen-amazon-marketplace-2026-02-05. The Bundeskartellamt's own release was not reached (the guessed URL returned 404).
- **JFTC** on-site inspection 2024-11-26 (snippet): no outcome found. **India CCI** investigation reports 2024 (snippet): no final order found.

**Academic** (peer-reviewed marked; others are working papers):

- **Zhu & Liu**, "Competing with Complementors", *Strategic Management Journal* 39(10), 2018 (peer-reviewed). Amazon enters successful product spaces, and small sellers it enters against are discouraged from growing (abstract via snippet).
- **Hsin-Tien Tsai** (National University of Singapore), "Incidence of Platform Fees: Evidence from Amazon Marketplace", working paper, October 2021. Abstract, read from the PDF 2026-11-10: "The difference-in-differences estimators suggest that about 45% of seller fees were passed on to consumers, and at least 64% of consumer fees were passed on to sellers. The empirical finding suggests that sellers bear more of the burden of platform fees than consumers." Identification: "two platform fee increases that affected a subset of products". [research; command-verified] (Gutiérrez's pass-through estimate is a second one, product-profit.md *Published research*.)
- **Langenmayr & Muddasani**, CESifo WP 12713, 2026. Amazon raised fees by roughly each country's digital services tax (snippet).
- **Gutiérrez**, "The Welfare Consequences of Regulating Amazon", NBER conference draft 2022. "Optimal regulation is product- and platform-specific". It is funded to test "whether Amazon's fees to sellers reflect market power" (abstract and grant page).
- **Lee & Musolff**, "Entry into Two-Sided Markets Shaped by Platform-Guided Search", working paper 2022: "recommendations are highly price elastic but favor Amazon".
- **Raval**, "Steering in One Click", working paper 2024: "the Amazon platform substantially prioritizes its retail arm and fulfillment arm".
- **Waldfogel**, NBER WP 32299, 2024: Amazon's own products rank "24 positions better on average" [command-verified].

What this research does and does not give the pack [seat]. It describes the fee level and who bears it at market scale. It gives no per-seller fact. A skill can say that fee share of sales is an industry-measured quantity that analysts put at 45–60% for typical FBA sellers, with dates and who measured it, and nothing more.

## Stable enough for a skill

Facts about the landscape, true as long as the named tools and Amazon's surfaces stay as read:

1. Amazon gives its own per-product "net proceeds" (SKU Economics, Profit Analytics), built from Amazon data plus seller-entered costs. It is one definition among several, not the seller's books.
2. The tools use at least four dating bases for the same order: order time, ship time, settlement time and transfer time. 领星, 积加, 赛狐 and SellerLogic each expose more than one. A refund can be dated by refund time or by its order's time.
3. Settlement-based bookkeeping connectors (A2X, Link My Books, Taxomate, Webgility) treat the reserve as a balance-sheet asset, not income or expense, and split settlements at calendar month end.
4. DD+7 deferral is handled one of four ways:
   - shown only once released (Synder; tool4seller Standard);
   - accrued into the month earned and reversed on release (A2X, Link My Books add-ons; Finaloop accrual; 领星 预结算; tool4seller Enhanced);
   - shown then moved (Sellerboard default);
   - read daily from Amazon's deferred data (赛狐).
5. FX rates differ by tool:
   - settlement-start month's month-start rate (领星, 积加);
   - last day of the reporting period (Sellerboard);
   - Amazon's own conversion rate (Synder, Taxomate);
   - transaction-time spot rate (Finaloop);
   - the ledger's rate (A2X).
6. Shared-fee allocation keys in use:
   - sales share (default in 领星, 积加, 易仓);
   - FBA-only sales share, storage-report share, long-term-storage share and custom ASIN lists (赛狐);
   - units, volume or weight (店小秘);
   - even daily spread (Sellerboard storage; 积加 storage);
   - left at account level (Helium 10 for storage and Sponsored Brands).
7. 头程 (inbound freight) is allocated per shipment by chargeable weight, actual weight, volumetric weight, quantity or custom (领星), by quantity (易仓), or folded into COGS (Sellerboard option).
8. COGS methods offered: FIFO, moving weighted average, month-end weighted average, dated cost periods and fixed cost. Several tools recompute history when the method or cost changes (Sellerboard, 领星).
9. Practitioners agree on what the books get wrong: the deposit is not revenue, sales tax and VAT are liabilities, the reserve is an asset, reimbursements are recoveries, and settlements straddle months.
10. Reimbursement recovery vendors charge a share of recoveries (the share is read at run time; see *What cx must read at run time*) and file through Seller Central channels, not SP-API (`04-job-money.md` §4.7).
11. Chinese ERPs post Amazon money into 金蝶 or 用友 as documents (sales outbound, receivables, receipts, stock movements) or as vouchers built from preset templates. The account each Amazon line lands in is set by the seller's mapping (领星's summary-item mapping, 易仓's fee items, 金蝶's voucher template) against the seller's own chart of accounts. Amazon publishes no mapping, and `breakdownType` has no enumerated values.
12. The ledger's month and Amazon's settlement differ by construction. Settlement periods do not follow the calendar month (their dates are read at run time; see *What cx must read at run time*), the ledger runs by calendar month, and the ERP pushes the previous month's FBA data from about the 6th of the next month (领星).
13. Chinese practitioners book revenue gross under CAS 14 art. 34, but they put Amazon's deductions on different lines: 销售费用, 财务费用, 销售成本, or netted off revenue.

## What cx must read at run time

- **Which basis a seller's own tool uses.** Only the seller can say; the tools allow several. [seat] If a seller quotes a tool's number, the tool's basis is part of the number.
- **Deferred and reserve amounts.** Finances v2024-06-19 `listTransactions` (`DEFERRED`, `DEFERRED_RELEASED`, `maturityDate`); `listBalances` (`ACCOUNT_LEVEL_RESERVE`); the settlement V2 `Current Reserve Amount` / `Previous Reserve Amount Balance` lines (Finance and Accounting). None of the tools can predict the reserve; 领星 says so ("目前无法预判预留金额").
- **FX.** Amazon's conversion rate and fee per transfer, from the disbursement and settlement data, not quoted (see `04-job-money.md`).
- **Storage and long-term storage charges per product.** `GET_FBA_STORAGE_FEE_CHARGES_DATA`, `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` (Amazon Fulfillment **or Pricing**).
- **Reimbursements received.** `GET_FBA_REIMBURSEMENTS_DATA` (Amazon Fulfillment **or Pricing**).
- **Fee and price figures.** Read at run time from Amazon's pages and the Product Fees API, never from this file.
- **Settlement period and payout dates.** Moved from *Stable enough* item 12, which said settlements run every 14 days (`04-job-money.md` §4.1, "every two weeks", read 2026-11-09; globalselling.amazon.com/zhishi/article-260113-2, "每14天一次（双周结算）", China-facing guide, read 2026-11-09). Read for the seller's own marketplace from Finances v0 `listFinancialEventGroups` (`FinancialEventGroupStart`, `FinancialEventGroupEnd`), the `settlement-start-date`, `settlement-end-date` and `deposit-date` columns of `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`, and Transfers v2024-06-01 `listExpectedPayouts`.
- **Recovery vendors' commission share.** Moved from *Stable enough* item 10 ("5–25% on the pages read", vendor pages read 2026-11-09). Read from each vendor's own page (the pages P-tool-17 names); no SP-API operation or Amazon page gives it.
- **The seller's ledger mapping, if they keep books in 金蝶 or 用友.** Only the seller can give it: which ERP pushes, in which mode (领星: profit report vs settlement detail; by order, day or month), which voucher-date rule, which chart lines take commission, ads, FBA fees, the reserve and FX differences, and which monthly booking rate. No API reaches it. The `breakdownType` and settlement `amount-description` values the mapping is keyed on are read from the seller's own data.

## What only Seller Central shows

- **Date Range Reports.** No SP-API report type. 积加 reaches them by browser automation ("RPA或者插件") [opinion], which shows that a large Chinese ERP needed them. No API reaches them. Since Amazon's Date Range Summary now includes deferred transactions, A2X warns its report "will not match Seller Central until you enable deferred transactions adjustments".
- **The Deferred Transactions report page.** A2X takes opening balances from it. The API face is `transactionStatus=DEFERRED` in Finances v2024-06-19.
- **The Summary (monthly statement PDF)** that 领星 reconciles against. Its API equivalent was not identified; 领星 says it reconciles "API数据与summary数据".
- **Profit Analytics and SKU Economics views.** The Data Kiosk economics dataset and economics preview report carry their data (`04-job-money.md` §2.6).
- **Manufacturing cost entry (IDR portal)**, which sets reimbursement value. Not writable by API.
- **Claim filing.** Recovery vendors file through Seller Central channels ("Notifications in Seller Central", GETIDA). No API.

## Facts for human readers only

Dated figures read on 2026-11-09 from vendors' public pages. A skill never states them.

| Tool | Price as published | Page |
|---|---|---|
| Sellerboard | Standard $19/mo ($15 annual) to 3,000 orders; Professional $29 ($23); Business $39 ($31); Enterprise $79 ($63) to 50,000; 1-month trial | sellerboard.com/en/ |
| Helium 10 | Platinum $129/mo ($99 yearly); Diamond $359 ($279); Enterprise from $1,499/mo annual; MRS fee 15%/10% (pricing page) vs 15%/18% (MRS page) | helium10.com/pricing/; …/managed-refund-service/ |
| Jungle Scout | Extra seat $49/month; plan prices not shown on the official page | junglescout.com/pricing/ |
| ShopKeeper | $20 (250 orders) to $250 (10,000); Enterprise by quote | shopkeeper.com/pricing |
| SellerApp | Pro from $99; Smart from $149; Freemium $0 | sellerapp.com/pricing.html |
| A2X | Mini $29 (200 orders), Starter $59 (1,000), Standard $79 (5,000) … Premium 250k $1,499; increase from 2026-11-14 (not Mini) | a2xaccounting.com/amazon/pricing |
| Link My Books | Deferred add-on £15/account/month; plan prices did not render | linkmybooks.com/amazon-deferred-payments |
| Synder | Basic $65 ($52), Essential from $129 ($103), Pro from $299 ($240), Pro Max from $599 ($480); page inconsistent | synder.com/pricing/ |
| Webgility | Pro $79/$69 (300 orders), Advanced $149/$129 (800), Complete $349/$299 (1,500) | webgility.com/pricing |
| Taxomate | $16–19 to 200 orders; Starter $49–59 to 5,000; 3-month average sizing from 2027-01-01 | taxomate.com/pricing |
| Finaloop | Starter $245/mo up to $1M revenue | finaloop.com/pricing |
| GETIDA | From 20% of recoveries | getida.com/pricing |
| Seller Investigators | 25% of recoveries | sellerinvestigators.com |
| Threecolts | Margin Pro 15–25%; Seller 365 5–15% | threecolts.com |
| Payability | Advance 80% of the previous day's payouts; commission cap 8% and advance cap 90% in terms | payability.com/instant-access-2/; /supplier_terms/ |
| 8fig | "$6,000-$10,000 for every $100,000" | 8fig.co |
| 领星 | Free while ≤5,000 orders a month; paid by quote | lingxing.com/price |
| 赛狐 | Free to 3,000 orders a month; ￥12,000 (200k orders/yr) to ￥120,000 (6M) | sellfox.com/price.html |
| 旺销王 | VIP1 ￥680/yr to VIP5 ￥8,980/yr (fetch summary) | wxwerp.com |
| Collectors (2023) | 万里汇 0.3% cap; 连连 0.7%; PingPong 1%; 结行国际 0.25% cap | cifnews 139307 (2023-01-31) |
| Take rate | 50%+ (MP 2023), 50–60% (MP 2024), 45% (ILSR 2023), "close to 50%" (FTC 2023) | as cited |

## Pages read

| Title | URL | Date read | Tag |
|---|---|---|---|
| Track fees with the new SKU Economics report | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/3a20e851-096e-4fca-a62d-c8e48b30e367 | 2026-11-09 | official [command-verified] |
| Your account will be migrated to DD+7 … (seller-quoted Amazon e-mail) | https://sellercentral.amazon.com/seller-forums/discussions/t/afacf90a-3e68-4d8d-87aa-8e66d3c24500 | 2026-11-09 | official-as-quoted [command-verified] |
| 亚马逊平台的收费标准是怎样的？(跨境知识荟) | https://globalselling.amazon.com/zhishi/article-260113-2 | 2026-11-09 | official |
| 重要！亚马逊近期政策大汇总 (2025-11-12) | https://gs.amazon.cn/news/news-notices-251112 | 2026-11-09 | official |
| 选择了「0费率」，但跨境收款真的是「0成本」吗？ | https://gs.amazon.cn/zhishi/article-250208-1 | 2026-11-09 | official |
| Payment provider notice (2021-02-01) | https://globalselling.amazon.com/news/news-notices-210201 | 2026-11-09 | official |
| 国家税务总局公告2025年第3号 | https://fgk.chinatax.gov.cn/zcfgk/c100012/c5238152/content.html | 2026-11-09 | official (CN government) |
| Amazon releases new profit analytics dashboard for sellers (PPC Land) | https://ppc.land/amazon-releases-new-profit-analytics-dashboard-for-sellers/ | 2026-11-09 | opinion [command-verified fetch] |
| Role Mappings / Role Mappings for types (local copies) | saved copies of https://developer-docs.amazon/sp-api/docs/role-mappings.md and its types page (updatedAt 2026-09-09) | 2026-11-09 | official [command-verified] |
| A2X support: deferred adjustments, V1/V2, default mappings, reserves, COGS, FX, MCF | https://support.a2xaccounting.com/en/articles/11698773 (and 1828440, 6008311, 959828, 959816, 1136907, 8871866) | 2026-11-09 | opinion [11698773 command-verified] |
| A2X: Amazon reserve balances | https://www.a2xaccounting.com/ecommerce-accounting-hub/amazon-reserve-balances | 2026-11-09 | opinion [command-verified] |
| A2X: DD+7 deferred transactions (Gualano, 2025-08-18) | https://www.a2xaccounting.com/ecommerce-accounting-hub/amazon-dd-7-deferred-transactions-accounting-challenges-and-a2x-workarounds | 2026-11-09 | opinion |
| A2X: Avoid these Amazon accounting mistakes (Crooymans, 2025-01-17) | https://www.a2xaccounting.com/blog/avoid-these-amazon-accounting-mistakes/ | 2026-11-09 | opinion |
| A2X: Top 3 accounting mistakes (Bird, 2022-06-06) | https://www.a2xaccounting.com/blog/top-3-accounting-mistakes-that-cost-your-business-money | 2026-11-09 | opinion |
| A2X pricing | https://www.a2xaccounting.com/amazon/pricing | 2026-11-09 | opinion |
| Link My Books: Amazon FBA accounting errors (Little, 2026-05-07) | https://linkmybooks.com/blog/amazon-fba-accounting-errors-why-your-numbers-are-wrong | 2026-11-09 | opinion [command-verified] |
| Link My Books help 4155809, 12080631, 4184943, 12086764, 2570701, 3490105, 3447820; deferred payments page; settlement reconciliation blog | https://linkmybooks.com/amazon-deferred-payments ; https://linkmybooks.com/blog/amazon-settlement-reconciliation-explained | 2026-11-09 | opinion |
| Synder: integration page; help on reserves, deferred, pending fees, per-payout sync; pricing | https://synder.com/integrations/quickbooks/amazon/ ; https://synder.com/pricing/ | 2026-11-09 | opinion |
| Webgility help 8011616, 7000560, 8780600, 6257099; reserve and deposit blogs; pricing | https://helpcenter.webgility.com/en/articles/8011616 ; https://www.webgility.com/blog/account-level-reserve-amazon ; https://www.webgility.com/pricing | 2026-11-09 | opinion |
| Taxomate docs 6180397, 8752420, 12005966, 6180400, 6181560; blog; pricing | https://docs.taxomate.com/en/articles/6180397 ; https://taxomate.com/blog/amazon-seller-accounting ; https://taxomate.com/pricing | 2026-11-09 | opinion |
| Finaloop help 15070376, 10499774, 9813151, 6636161; pricing | https://help.finaloop.com/en/articles/15070376 ; https://finaloop.com/pricing | 2026-11-09 | opinion |
| Sellerboard general settings | https://help.sellerboard.com/general-settings/ | 2026-11-09 | opinion [command-verified] |
| Sellerboard FAQ, products, cashflow, indirect expenses, reports, tiles; blog posts (?p=3570, ?p=3790, SP-API 2026-09-08, freight 2026-08-10) | https://sellerboard.com/faq ; https://help.sellerboard.com/?p=3413 ; https://blog.sellerboard.com/?p=3570 | 2026-11-09 | opinion |
| Helium 10 Profits, pricing, MRS, Refund Genie, account P&L blog (2026-08-12), reimbursement policy blog (VanAkker, 2024) | https://www.helium10.com/tools/analytics/profits/ ; https://www.helium10.com/pricing/ ; https://www.helium10.com/tools/operations/managed-refund-service/ ; https://www.helium10.com/blog/amazon-fba-inventory-reimbursement-policy-update/ | 2026-11-09 | opinion [policy blog command-verified] |
| Helium 10: The Amazon profit leak audit (Gaba, 2026-08-13) | https://www.helium10.com/blog/the-amazon-profit-leak-audit-12-places-your-margin-quietly-disappears/ | 2026-11-09 | opinion |
| Jungle Scout Sales Analytics; pricing; Fetcher FAQ | https://www.junglescout.com/features/sales-analytics/ ; https://www.junglescout.com/fetcher/faq | 2026-11-09 | opinion |
| SellerApp net profit breakdown | https://www.sellerapp.com/help/docs/analyze-net-profit-breakdown-chart/ | 2026-11-09 | opinion [command-verified] |
| ShopKeeper P&L guide; pricing | https://shopkeeper.com/guide/en/shopkeeper-profit-and-loss-page ; https://shopkeeper.com/pricing | 2026-11-09 | opinion |
| SellerLogic profit dashboard refunds | https://support.sellerlogic.com/profit_dashboard/refunds | 2026-11-09 | opinion |
| tool4seller deferred transactions calculation | https://www.tool4seller.com/faqs/faq-amazon-deferred-transactions-calculation-method | 2026-11-09 | opinion [command-verified] |
| GETIDA pricing and home | https://www.getida.com/pricing | 2026-11-09 | opinion |
| Seller Investigators; Carbon6 | https://www.sellerinvestigators.com/ ; https://carbon6.io/ | 2026-11-09 | opinion |
| Threecolts Margin Pro; Seller 365 reimbursements; blog (2025-05-21) | https://www.threecolts.com/margin-pro/marketplace-seller-reimbursements/fba-reimbursement-service ; https://www.threecolts.com/seller-365/reimbursements | 2026-11-09 | opinion |
| Refunds Manager | https://refundsmanager.com/ | 2026-11-09 | opinion |
| Payability Daily Payouts; supplier terms | https://www.payability.com/instant-access-2/ ; https://payability.com/supplier_terms/ | 2026-11-09 | opinion |
| 8fig home; FAQ | https://www.8fig.co/ ; https://www.8fig.co/static/faq | 2026-11-09 | opinion |
| Shulex | https://www.shulex.com/ | 2026-11-09 | opinion |
| 领星 help: SettlementCenter | https://www.lingxing.com/help/article/SettlementCenter | 2026-11-09 | opinion [command-verified] |
| 领星 help: MonthlyProfitReportnew | https://www.lingxing.com/help/article/MonthlyProfitReportnew | 2026-11-09 | opinion [command-verified] |
| 领星 help: Orderprofit, ProfitStatementnew1, costPricing, productExpressionNew, ShipSettlVarReport, PerformanceStatementnew, headDistanceStatistics, deferredSettlement, exchangeRateManagement; price | https://www.lingxing.com/help/article/ProfitStatementnew1 (and siblings) ; https://www.lingxing.com/price | 2026-11-09 | opinion |
| 领星 three-basis release (AMZ123, 2026-08-13) | https://www.amz123.com/t/QRQ8vQyk | 2026-11-09 | opinion |
| 积加 help: settlement center | https://help.jijiaerp.com/docs/iWN6Y4MP | 2026-11-09 | opinion [command-verified] |
| 积加 help: 2vIEQwzy, CsdBvZ96, NUHRNtNL, MyAuOX8Q, VzaJGf2X, fPlZrZZp, qF7LLY0s, uRFqleEx, 1PQUsonf, h1aN9U0C | https://help.jijiaerp.com/docs/CsdBvZ96 (and siblings) | 2026-11-09 | opinion |
| 赛狐 help: shared management | https://www.sellfox.com/help/features/shared-management | 2026-11-09 | opinion [command-verified] |
| 赛狐 help: profit statement; difference explainer; blog (2026-08-13); price | https://www.sellfox.com/help/features/profit-statement ; https://www.sellfox.com/help/solution/difference-in-the-financial-profit-statement ; https://www.sellfox.com/blog/article/ymx-cwdz-sellfox ; https://www.sellfox.com/price.html | 2026-11-09 | opinion |
| 易仓 finance page; 2025-07 update (搜狐) | https://www.eccang.com/cwjq.html ; https://m.sohu.com/a/911514008_609544/ | 2026-11-09 | opinion |
| 店小秘 financial management; blog 241 | https://help.dianxiaomi.com/article/financialManagement/3061 ; https://www.dianxiaomi.com/blog/article/241 | 2026-11-09 | opinion |
| 马帮 (派代) | https://www.pai.com.cn/200639.html | 2026-11-09 | opinion |
| 旺销王; 紫鸟; 通途 help | https://www.wxwerp.com ; https://www.ziniao.com ; https://help.tongtool.com/service.html?groupId=2 | 2026-11-09 | opinion |
| 雨果网 185409 (闯盟跨境, 2026-04-23); 169921 (2025-01-08); 180164 (2025-11-03); 139307 (2023-01-31); 183741 (2026-02-27); 60233 (2020-02-10) | https://www.cifnews.com/article/185409 (and siblings) | 2026-11-09 | opinion |
| AMZ123 t/5bJ2W1nh, t/1pyPezpH, t/1TaORlzI, t/InOHDETa, t/CyG0p4SU, kx/kZFLfBre, b/ygSxkvSd | https://www.amz123.com/t/5bJ2W1nh (and siblings) | 2026-11-09 | opinion |
| 知无不言 76282; 101964 | https://www.wearesellers.com/question/76282 ; https://www.wearesellers.com/question/101964 | 2026-11-09 | opinion |
| 卖家之家 57558; f3274d3ht2ps | https://mjzj.com/article/57558 ; https://m.mjzj.com/article/f3274d3ht2ps | 2026-11-09 | opinion |
| 36氪 3511488078731650; 3463346027026820; 2043364439314435 | https://www.36kr.com/p/3511488078731650 (and siblings) | 2026-11-09 | opinion |
| 搜狐 金方圆财务 (2026-05-19); 新浪 轻松财税 (2026-08-04); 白鲸出海 51162 | https://m.sohu.com/a/1024519392_100110381 ; https://www.sina.cn/news/detail/5328110355744292.html ; https://www.baijing.cn/article/51162 | 2026-11-09 | opinion |
| ConnectBooks month-end close checklist (Quattlebaum, 2026-07-02) | https://www.connectbooks.com/blog-posts/checklist-month-end-close-for-amazon-sellers | 2026-11-09 | opinion [command-verified] |
| Bean Ninjas accounting mistakes (Richard, 2024-01-20) | https://beanninjas.com/blog/accounting-mistakes/ | 2026-11-09 | opinion |
| EcomCFO Amazon seller accounting (Hill, 2022-11-16) | https://ecomcfo.co/amazon-seller-accounting/ | 2026-11-09 | opinion |
| Eightx all-in take rate (Dillon, 2026-07-06) | https://eightx.co/blog/amazon-all-in-take-rate | 2026-11-09 | opinion |
| Canopy Management ACoS/TACoS (Kessler, 2025-10-10) | https://canopymanagement.com/ultimate-guide-to-acos-and-tacos/ | 2026-11-09 | opinion |
| Helium 10 podcast #287 (Remuzzi, 2021) | https://www.helium10.com/es/podcast/bookkeeping-accounting-tips-for-amazon-sellers/ | 2026-11-09 | opinion |
| MWQHJ episode 449 (Mazor) | https://mywifequitherjob.com/episode449/ | 2026-11-09 | opinion |
| Marketplace Pulse: 50% cut (2023-02-13) | https://www.marketplacepulse.com/articles/amazon-takes-a-50-cut-of-sellers-revenue | 2026-11-09 | research (industry) [command-verified] |
| Marketplace Pulse: fees only go up (2024-03-18); GMV 2025 (2026-02-06); paradoxical dependence (2026-04-16) | https://marketplacepulse.com/articles/amazon-fees-only-go-up ; https://www.marketplacepulse.com/articles/the-paradoxical-dependence-of-amazon-its-sellers | 2026-11-09 | research (industry) |
| ILSR Amazon's Monopoly Tollbooth in 2023 | https://archive.ilsr.org/?p=102720 | 2026-11-09 | research (advocacy) [command-verified] |
| ILSR Amazon's Toll Road (2021) | https://ilsr.org/amazons-toll-road/ | 2026-11-09 | research (advocacy) |
| Fortune, Del Rey (2025-02-07) | https://fortune.com/2025/02/07/amazon-2024-earnings-third-party-seller-fees-profits/ | 2026-11-09 | research (journalism) |
| FTC sues Amazon (2023-09-26) | https://www.ftc.gov/news-events/news/press-releases/2023/09/ftc-sues-amazon-illegally-maintaining-monopoly-power | 2026-11-09 | research (regulator); plain GET returned a stub, read through the fetch tool |
| FTC Prime settlement (2025-09-25) | https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon | 2026-11-09 | research (regulator) |
| MLex: Amazon's bid to delay FTC trial rejected (2026-10) | https://www.mlex.com/mlex/antitrust/articles/2536525/amazon-s-bid-to-delay-us-ftc-monopolization-trial-rejected-by-judge | 2026-11-09 | research (journalism, via search) |
| California AG release (2026-04-16) | https://oag.ca.gov/node/621817 | 2026-11-09 | research (state AG) |
| CMA case page | https://www.gov.uk/cma-cases/investigation-into-amazons-marketplace | 2026-11-09 | research (regulator) |
| Cuatrecasas on EU commitments | https://www.cuatrecasas.com/en/latam/competition-eu-law/art/european-commission-accepts-amazons-commitments-and-closes-its-investigation | 2026-11-09 | research (law firm summary) |
| GRC Report on Bundeskartellamt decision (2026-02-05) | https://www.grcreport.com/post/german-watchdog-curbs-amazons-grip-on-seller-pricing-orders-eu59-million-disgorgement | 2026-11-09 | research (journalism) |
| Waldfogel NBER w32299 | https://www.nber.org/papers/w32299 | 2026-11-09 | research [command-verified] |
| Zhu & Liu SMJ 2018 (RePEc) | https://econpapers.repec.org/RePEc:bla:stratm:v:39:y:2018:i:10:p:2618-2642 | 2026-11-09 | research (peer-reviewed; abstract via snippet) |
| Lee & Musolff (TSE) | https://www.tse-fr.eu/entry-two-sided-markets-shaped-platform-guided-search | 2026-11-09 | research |
| Raval (SIOE 2024) | https://www.sioe.org/conference/2024/program/paper/858-steering-in-one-click-platform-self-preferencing-in-the-amazon-buy-box | 2026-11-09 | research |
| Gutiérrez NBER draft; Equitable Growth grant | https://conference.nber.org/conf_papers/f167093/f167093.pdf ; https://equitablegrowth.org/grants/understanding-amazon-strategy-and-welfare-implications/ | 2026-11-09 | research (PDF unreadable; abstract via snippet) |
| Tsai, Incidence of Platform Fees | https://www.tse-fr.eu/sites/default/files/TSE/documents/conf/2022/postal/tsai_abstract.pdf | 2026-11-09 | research (PDF unreadable; snippet) |
| Langenmayr & Muddasani CESifo 12713 | https://ideas.repec.org/p/ces/ceswps/_12713.html | 2026-11-09 | research (snippet) |
| Ads playbook research (overlap: TACoS, FTC ads suit) | `packages/ads-playbook/research/beyond/goals-and-economics.md` | 2026-11-09 | reused |
| Survey note 04-job-money.md | the sp-api-plugins seat's survey of SP-API for brief 306 (not published) | 2026-11-09 | reused |
| 领星 help: 金蝶云星空集成 (created 2023-04-04 per page metadata) | https://www.lingxing.com/help/article/KingdeeIntegration | 2026-11-10 | opinion [command-verified] |
| 金蝶云产品手册: 凭证模板 | https://help.open.kingdee.com/dokuwiki/doku.php?id=%E5%87%AD%E8%AF%81%E6%A8%A1%E6%9D%BF | 2026-11-10 | opinion (Kingdee's own manual) [command-verified] |
| 金蝶AI星辰: 跨境电商ERP选型指南 (2025-10-10) | https://www.jdy.com/article/1976537696977367042.html | 2026-11-10 | opinion (Kingdee's own page) [command-verified] |
| 易仓: 财务居家办公指南 (c. 2022-02); 财务解决方案 | https://www.eccang.com/news/2390 ; https://www.eccang.com/cwjq.html | 2026-11-10 | opinion [command-verified] |
| 积加: 涉税新规下…业财集成 (2025-09-10); finance product page | https://www.jijiaerp.com/news/detail/index510.html ; https://www.jijiaerp.com/products-and-services/finance | 2026-11-10 | opinion [command-verified] |
| 跨境知道: 做亚马逊，你真的知道应收账款怎么对账吗？ (2022-02-11, 积加 promotion) | https://www.ikjzd.com/articles/1658378894475730945 | 2026-11-10 | opinion [command-verified] |
| 万里牛: 亚马逊账单怎么看明白？ (2026-09-20) | https://www.hupun.com/articles/amazon-settlement-bill-fee-guide.html | 2026-11-10 | opinion [command-verified] |
| 轻易云 case articles: 赛狐×金蝶 (13573), 领星×金蝶 (13407), 易仓×金蝶 (13580) | https://qeasy.cloud/a/13573 ; https://m.qeasy.cloud/a/13407 ; https://m.qeasy.cloud/a/13580 | 2026-11-10 | opinion (integration vendor) [command-verified] |
| YonSuite: 跨境电商业财一体化的多币种处理方案详解 | https://www.yonsuite.com/infoNew/2250606355082.html | 2026-11-10 | opinion (Yonyou's own page) [command-verified] |
| 畅捷通: 跨境电商财务做账技巧 | https://service-ask.chanapp.chanjet.com/yxwz/d84c6a83292e4417829.html | 2026-11-10 | opinion (Yonyou group marketing) [command-verified] |
| 新浪 轻松财税 (2026-08-04), re-read for the journal entries | https://www.sina.cn/news/detail/5328110355744292.html | 2026-11-10 | opinion [command-verified] |
| 搜狐 金方圆财务 (2026-05-19), re-read for the account lines | https://m.sohu.com/a/1024519392_100110381 | 2026-11-10 | opinion [command-verified] |
| 百运网: 用亚马逊FBA服务的卖家，该如何做好电商会计 (undated) | https://www.by56.com/news/42372.html | 2026-11-10 | opinion [command-verified] |
| 企业会计准则第14号——收入 (2017 revision), law-database copy | https://www.fadada.com/article/Basics-008725 | 2026-11-10 | official (PRC MOF), via copy [command-verified] |
| 企业会计准则第19号——外币折算, law-database copy | https://www.fadada.com/article/Basics-008770 | 2026-11-10 | official (PRC MOF), via copy [command-verified] |
| 企业会计准则第1号——存货, law-database copy | https://www.fadada.com/notice/detail-11131.html | 2026-11-10 | official (PRC MOF), via copy [command-verified] |
| Finances v2024-06-19 model (`Breakdown`, `Transaction`) | `models/finances-api-model/finances_2024-06-19.json` (clone db2936aa) | 2026-11-10 | official [command-verified] |
| Update on Reimbursement Automation and Eligibility Window (posted 2024-07-24, US forum; "November 1, 2024") | https://sellercentral.amazon.com/seller-forums/discussions/t/6605eede-df8e-4498-803f-cb612d95d7ce | 2026-11-09 (refunds sibling) | official, reused |
| Update on Reimbursement Automation and Eligibility Window (posted 2024-10-10, British spelling, no store named; "January 15, 2025") | https://sellercentral.amazon.com/seller-forums/discussions/t/d0fc997e-de50-4100-9803-76b7993b66df | 2026-11-09 (refunds sibling) | official, reused |
| Update to FBA inventory reimbursement claim windows (eff. 2025-10-15) | https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465 | 2026-11-09 (refunds sibling) | official, reused |
| FBA inventory reimbursement policy (G200213130) | https://sellercentral.amazon.com/gp/help/external/G200213130 | 2026-11-09 (refunds sibling) | JS shell, unread |
| Finances v2024-06-19 `listBalances`; Finances v0 `listFinancialEventGroups`; Transfers v2024-06-01 `listExpectedPayouts` (models) | `models/finances-api-model/finances_2024-06-19.json`, `financesV0.json`, `transfers_2024-06-01.json` (clone db2936a) | 2026-11-10 | official [command-verified] |

**Unreachable or failed:**

- kb.helium10.com and support.junglescout.com (HTTP 403 to automated fetch; snippets only).
- help.shopkeeper.com (DNS).
- managebystats.com (HTTP 500).
- Carbon6 blog posts (404).
- refundsmanager.com/pricing and sellerinvestigators.com/pricing (404).
- jijiaerp.com/taocan (prices are an image).
- linkmybooks.com/pricing (prices did not render).
- dianxiaomi.com/price.htm (404).
- EU Commission press PDFs, Raval and Gutiérrez PDFs (body unreadable). The Tsai abstract PDF was read on 2026-11-10 with PDFKit.
- The Bundeskartellamt's own page (not fetched; secondary report used).
- 卖家大学 courses (sign-in).
- gs.amazon.cn/zhishi/article-260309-3 (empty).
- No official gs.amazon.cn DD+7 notice was found.
- (2026-11-10) Did not resolve or were not readable: cjtax.cn (天赋长江税务师事务所 column on net-payout bookkeeping; connection failed twice); zhuanlan.zhihu.com (403); caigeek.com reserve article (404); Deloitte and CICPA PDFs of CAS 19 (404 / HTML stub). AMZ123 t/TPCJX214, t/upmNCeLB, t/qh8JRyPq and ask/QUHR0OdA were read but are generic entry tutorials with nothing Amazon-specific, so they are not cited. No kingdee.com or yonyou.com page on Amazon or cross-border settlement was found by search.

## Open questions

These are for a first run on a real account:

1. Does the seller already run a tool (Sellerboard, A2X, 领星…)? Which basis, FX rate and allocation keys does it use? Only the seller or the tool's settings can say. The answer decides what "matches" means.
2. Does Data Kiosk economics (Profit Analytics' data) agree with the settlement V2 lines for the same SKU and month? How far apart are they, and on which lines (ads types, FBA fee quantity, as the seller in Amazon's SKU Economics thread reported)?
3. Is the reserve on this account a fixed percentage (领星 describes "最近28天的销售额的5%") or something else? `listBalances` and the settlement reserve lines over a few cycles would show it.
4. Does `GET_FBA_STORAGE_FEE_CHARGES_DATA` / `GET_FBA_REIMBURSEMENTS_DATA` actually return under the **Pricing** role alone, as Role Mappings say?
5. Does the account's Date Range Summary include deferred transactions (A2X's warning)? Does it match the sum of `listTransactions` for the month?
6. Which currency and rate does the seller's payout actually use (ACCS, a third-party collector, a local bank)? The rate Amazon applies appears per transfer.
7. For a Chinese entity: does finance book revenue gross (the tax-reporting practice the Chinese sources describe), and at which FX rate rule?
8. If the seller's books are in 金蝶 or 用友: which ERP pushes, in which mode, and is the voucher dated by the document or by the last day of the period? Which account holds the reserve and the deferred balance (one 应收账款——亚马逊 account, or a separate 其他应收款 line)? Only the seller's ledger and ERP settings say.
9. Do the seller's ledger's monthly revenue and fee totals for one store match the month's `listTransactions` sum, once deferred items and the booking rate are accounted for? Which of the causes 领星 names (data re-collection, late FBA data, mode) explains what is left?
10. Which `breakdownType` values does this account's data actually carry, and does each map one-to-one to a settlement `amount-description`? That decides whether a seller's existing mapping table, keyed on settlement labels, carries over to the v2024-06-19 face.

## Positions

Each position is a fact about named tools, people or published work, with its source. None is a rule for cx; every choice it names stays the seller's.

**P-tool-1.** Amazon publishes its own per-product profit view. SKU Economics on SKU Central "collects fees, sales, ads, off-Amazon costs, and net proceeds in a single view", and its report gives economics "at the FNSKU, MSKU, ASIN, and parent-ASIN level". Source: Amazon News post *Track fees with the new SKU Economics report* (Seller Forums EU). [official]

**P-tool-2.** Amazon announced Profit Analytics on 2025-09-17 as "introduced … this year" (aboutamazon; Accelerate forum post) and gives its path as Reports → Selling Economics and Fees (News, 2025-11-13) [official]. Trade press (PPC Land, 2025-09-20) dates it 2025-09-18 and reports that it combines sales, returns, fees, advertising and seller-provided costs into "Net Proceeds", runs "1-2 days behind" with some fee data "up to 7 days", and accepts seller inputs for COGS, per-unit storage, shipping, packing, LTL freight and off-Amazon ad spend. Source: aboutamazon (2025-09-17); Seller Forums Accelerate post (2025-09-17) and News post (2025-11-13); PPC Land (Luis Rijo, 2025-09-20), paraphrasing Amazon's documentation (quotes re-checked on the page 2026-11-10). The help page is a JS shell. [official for the dates and path; opinion for the latency, scale and input list]

**P-tool-3.** The tools date the same order on different bases:
- 领星: order time (订单利润); in its profit report settlement time (default), settlement time with 预结算, and ship time (new on 2026-08-13, read from the Transaction report's Date/Time);
- 赛狐: settlement, expected settlement, transfer, order time, with a settlement or ship basis in its order view;
- 积加: settlement time (financial profit) vs API real time (sales profit);
- SellerLogic: order creation vs transaction date.
Sources: 领星 help Orderprofit / ProfitStatementnew1 and AMZ123 release note; 赛狐 profit-statement help; 积加 help fPlZrZZp / h1aN9U0C; SellerLogic support. [opinion]

**P-tool-4.** Refund dating differs:
- 领星 order profit offers refund time or order time;
- 积加 financial profit dates refunds by settlement time, and its sales profit "按照订单退款时间统计，而不是订单订购时间统计";
- Sellerboard matches refunds to their orders and by default moves deferred refunds to their release date, "which can retroactively change past profit figures", with an option to hide them until released.
Sources: 领星 Orderprofit; 积加 uRFqleEx, CsdBvZ96; Sellerboard general settings [command-verified]. [opinion]

**P-tool-5.** DD+7 deferral is handled four ways:
- shown only once released (Synder: "can only import transactions that Amazon has 'released'"; tool4seller Standard);
- accrued to the month earned and reversed on release (A2X adjustment on the 5th of the following month; Link My Books add-on to an "Amazon Deferred Balances" asset; Finaloop accrual; 领星 预结算; tool4seller Enhanced, "based on its original transaction date");
- shown then moved (Sellerboard default);
- read daily from Amazon's deferred data (赛狐).
Sources: as named. [opinion]

**P-tool-6.** The settlement-based bookkeeping connectors book Amazon's reserve as a balance-sheet asset, not income or expense:
- A2X: "Reserve balance transactions are neither sales nor expenses", to "Amazon Reserved Balances";
- Taxomate: "Reserved Balance is a balance-sheet account";
- Webgility: "Record your reserve as a current asset";
- Synder: a Transfer to "Balance Reserve".
Sources: A2X hub page [command-verified] and support 6008311; Taxomate 12005966; Webgility reserve blog; Synder reserve help. [opinion]

**P-tool-7.** A2X, Link My Books and Taxomate split a settlement that crosses a calendar month. A2X: "according to which month the sales or fee actually occurred in". Link My Books: "Splits only ever happen at calendar month end", with earlier parts rolled forward. Taxomate splits "to match the sales and the related fees to their own months" (the split can be turned off). Sources: A2X support; LMB help 3490105; Taxomate 6180397. [opinion]

**P-tool-8.** FX conversion rules differ:
- 领星 and 积加 convert settlement totals at the rate for the month in which the settlement period starts, not the transfer month;
- Sellerboard uses "the exchange rate from the last day of the selected reporting period";
- Synder uses "Amazon's exchange rate";
- Taxomate imports "up to 18 months of conversion rates used by Amazon";
- Finaloop uses "the spot rate at the time of the transaction";
- A2X leaves conversion to the ledger.
Sources: 领星 SettlementCenter [command-verified]; 积加 iWN6Y4MP [command-verified]; Sellerboard general settings [command-verified]; Synder integration page; Taxomate 6181560; Finaloop 15070376; A2X 1136907. [opinion]

**P-tool-9.** Shared-fee allocation keys in published tool docs:
- sales share is the default in 领星 (base "（FBA销售额+FBM销售额）") and 积加 ("如果当日无销售额或销量则不分摊");
- 赛狐 offers FBA sales share, FBA+FBM sales share, monthly-storage-report share, long-term-storage share and custom ASINs;
- 店小秘 offers units, sales, volume or weight share;
- Sellerboard can spread storage "evenly across each day of the month";
- 积加 spreads last month's storage daily over this month;
- Helium 10 leaves storage and Sponsored Brands at account or campaign level (snippet).
Sources: 领星 MonthlyProfitReportnew [command-verified]; 积加 VzaJGf2X, CsdBvZ96; 赛狐 shared-management [command-verified]; 店小秘 blog 241; Sellerboard general settings [command-verified]; Helium 10 KB 360056383594 (snippet). [opinion]

**P-tool-10.** Inbound freight (头程) is allocated per shipment in 领星 by "计费重，实重，体积重，数量，自定义", and includes logistics, taxes, port and clearance fees. 易仓 added equal allocation by quantity (2025-07). Sellerboard lets inbound shipping be imported and distributed, or folded into COGS. Sources: 领星 headDistanceStatistics; 搜狐 911514008 (易仓 update); Sellerboard general settings. [opinion]

**P-tool-11.** COGS methods offered:
- 领星: moving weighted average or FIFO, switching "需要将所有月份重算";
- 积加: FIFO or custom;
- 赛狐: FIFO or fixed;
- Sellerboard: FIFO, weighted average or by period, "Historical orders are recalculated accordingly";
- Finaloop: FIFO from purchase orders with landed cost;
- Jungle Scout: "Effective From" dated costs.
Sources: 领星 costPricing; 积加 MyAuOX8Q; 赛狐 profit-statement; Sellerboard products help; Finaloop 9813151; Jungle Scout support (snippet). [opinion]

**P-tool-12.** Published profit formulas differ in what "gross profit" contains:
- Sellerboard's Gross Profit already subtracts advertising and Amazon fees;
- Webgility's gross profit is revenue minus COGS only, with fees and advertising in a separate "cost of sales";
- Jungle Scout's gross profit subtracts order fees but not company-level seller fees (snippet);
- 积加's "销售净毛利" adds storage and ad spend to "销售毛利".
ROI denominators also differ: SellerApp uses cost of goods; 领星 uses purchase cost plus first-leg cost. Sources: Sellerboard ?p=3413; Webgility 7000560; Jungle Scout 360036200053 (snippet); 积加 CsdBvZ96; SellerApp [command-verified]; 领星 productExpressionNew. [opinion]

**P-tool-13.** Named accountants and bookkeeping vendors name the same errors:
- the deposit booked as revenue (Crooymans/A2X; Little/Link My Books; Richard/Bean Ninjas; Taxomate);
- sales tax or VAT booked as income (Bird and Crooymans/A2X);
- reimbursements booked as sales (Quattlebaum/ConnectBooks; A2X);
- the reserve booked in P&L (Quattlebaum);
- settlements straddling months (Little; Quattlebaum);
- deferred revenue slipping into the next month (Gualano/A2X: "as much as 20-25 %", the vendor's figure).
Each is a vendor of the fix. Sources: as cited in *What practitioners add* §6. [opinion]

**P-tool-14.** Chinese finance practitioners hold:
- revenue is declared gross ("按客户支付全额交易总额"; "包括平台未回款的部分");
- three bases are kept separate: accounting, VAT filing and cash received;
- booking "提现净额" as revenue is called the common wrong practice;
- platform data reported to tax authorities (from 2025-10-31) is compared with filings.
Sources: 轻松财税 (新浪, 2026-08-04); Yiju谈跨境 (雨果网 180164); 品牌工厂 (36氪 3511488078731650). [opinion]

**P-tool-15.** A Chinese practitioner states the FX booking practice: one rate rule chosen ("当月月初汇率或结汇当日汇率") and held for the year; settlement differences to "财务费用汇兑损益"; month-end revaluation at the official middle rate; platform fees booked separately, never netted against revenue. Source: 金方圆财务 (搜狐, 2026-05-19). [opinion]

**P-tool-16.** Amazon's Chinese seller site says a "0费率" collector is not "0成本": converting twice through a third party adds a second FX loss, while ACCS converts once with tiered pricing. Source: gs.amazon.cn 跨境知识荟 article-250208-1 (Amazon promoting its own service). [official]

**P-tool-17.** Recovery vendors charge a share of what they recover: GETIDA from 20%, Seller Investigators 25%, Threecolts Margin Pro 15–25% and Seller 365 5–15%, Helium 10 MRS 10–18% (its two pages conflict). Their pages state look-backs of 18 months (GETIDA, Helium 10 MRS) or 9 months (Margin Pro), and none states how a claim's value relates to the seller's COGS. Sources: vendor pages as cited. [opinion] Read at run time: each vendor's own page, as listed in *Pages read*: GETIDA pricing (https://www.getida.com/pricing), Seller Investigators (https://www.sellerinvestigators.com/), Threecolts Margin Pro and Seller 365 reimbursements (https://www.threecolts.com/margin-pro/marketplace-seller-reimbursements/fba-reimbursement-service ; https://www.threecolts.com/seller-365/reimbursements), and Helium 10 pricing and Managed Refund Service (https://www.helium10.com/pricing/ ; https://www.helium10.com/tools/operations/managed-refund-service/); no SP-API operation or Amazon page gives a vendor's share or look-back.

**P-tool-18.** Payability advances "80% of your previous day's payouts", with the rest "made available once the marketplace payout is received". Its terms cap the purchasing commission at 8% and require the marketplace payout to be redirected to Payability. A seller on such a product sees Amazon's disbursements land with the financier, not in the seller's bank. Source: payability.com/instant-access-2/; payability.com/supplier_terms/. [opinion] Read at run time: Payability's own pages as listed in *Pages read*, *Payability Daily Payouts* (https://www.payability.com/instant-access-2/) and its supplier terms (https://payability.com/supplier_terms/); no SP-API operation or Amazon page gives a financier's advance rate or commission.

**P-tool-19.** 积加 reads Seller Central's Date Range Report, which has no SP-API report type, by "RPA或者插件", and its financial profit refreshes the last 39 days overnight. A2X says the Date Range Summary now includes deferred transactions, so A2X "will not match Seller Central until you enable deferred transactions adjustments". Sources: 积加 help fPlZrZZp; A2X support 8871866; `04-job-money.md` §1 (no report type). [opinion; official for the absence]

**P-tool-20.** Tools name time-zone and lag differences from Amazon's views:
- settlement reports "are in UTC" while business reports use marketplace time, "a 1-10 hour window" (Link My Books);
- Finaloop reports in UTC against Amazon NA's PST;
- 领星 notes "亚马逊配送报告会有3天数据延迟" and syncs only "最近3个月" of settlement data.
Sources: LMB 4155809; Finaloop 15070376; 领星 ShipSettlVarReport, SettlementCenter. [opinion]

**P-tool-21.** 领星 describes Amazon's reserve as "依据店铺最近28天的销售额的5%" and says "目前无法预判预留金额，且亚马逊无提供实时的预留金额". This is a vendor's description, not Amazon's rule; the API exposes the reserve in `listBalances` and in the settlement reserve lines. Sources: 领星 SettlementCenter [command-verified]; `04-job-money.md` §4.1. [opinion] Read at run time: the amount held on the seller's own account, from Finances v2024-06-19 `listBalances` (`balanceType` `ACCOUNT_LEVEL_RESERVE`, `RESERVED`, `DEFERRED`) and the `Current Reserve Amount` / `Previous Reserve Amount Balance` lines of `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`; no operation or page read gives the rule behind the amount, so 领星's "5%" of "最近28天" stands as read on 2026-11-09, no marketplace named.

**P-tool-22.** Helium 10's 2024 blog gives the customer-returns claim window as "between 60-120 days after the refund or replacement date". Amazon's US notices give 45–105 days. The blog predates the windows taking effect, and whether Amazon's own wording changed in between was not established; the vendor page and Amazon's notice disagree. GETIDA and Helium 10 MRS still advertise 18-month audits after Amazon shortened the windows (2024-10-23; revised 2025-10-15). Sources: Helium 10 blog [command-verified]; `04-job-money.md` §4.3 (Amazon's posts); GETIDA pricing; Helium 10 MRS. [opinion vs official] Read at run time: Amazon's *FBA inventory reimbursement policy* for the seller's own store (G200213130, https://sellercentral.amazon.com/gp/help/external/G200213130, a JavaScript shell to a plain GET) and the latest News post read, *Update to FBA inventory reimbursement claim windows* (US, effective 2025-10-15, https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465); no SP-API operation gives a claim window.

**P-tool-23.** Industry and advocacy measures of Amazon's total take from a typical third-party seller:
- "more than 50%" (Marketplace Pulse, 2023-02-13);
- "50-60%" for private label (Marketplace Pulse, 2024-03-18);
- "45 percent" in H1 2023 (ILSR, advocacy, 2023-09-21);
- "close to 50%" (FTC complaint, 2023-09-26, an allegation).
Each splits the take into referral, FBA (including storage) and advertising. Sources: as named [Marketplace Pulse and ILSR command-verified]. [research]

**P-tool-24.** A working paper estimates fee incidence on Amazon: "about 45% of seller fees were passed on to consumers, and at least 64% of consumer fees were passed on to sellers", so "sellers bear more of the burden of platform fees than consumers" (Tsai, October 2021). A 2026 CESifo paper reports Amazon raised fees by about each country's digital services tax. Sources: Tsai TSE abstract PDF (read 2026-11-10) [research; command-verified]; Langenmayr & Muddasani CESifo WP 12713 (snippet) [research; unverified].

**P-tool-25.** FTC et al. v. Amazon (W.D. Wash. 2:23-cv-01495) alleges anti-discounting punishment of sellers and conditioning Prime eligibility on Amazon's fulfilment. Trial is set for 2027-03-29 (a 2026-10-09 ruling kept the date, per Law360 and MLex as reported by PYMNTS), and no court has found these allegations true. California v. Amazon is set for trial on 2027-01-19. The EU (2022-12-20) and UK CMA (2023-11-03) commitments let Prime sellers choose and negotiate their own carriers. The Bundeskartellamt's 2026-02-04 decision bars Amazon's price-control mechanisms on amazon.de, with about €59M disgorgement, and is under appeal. Sources: FTC press release; PYMNTS/CPI (2026-10-11, citing Law360 and MLex); CA AG release; Cuatrecasas; gov.uk CMA case page; GRC Report; beck-aktuell (2026-02-05). [research/regulator; the court order and the Bundeskartellamt's own page not read]

**P-tool-26.** Role Mappings list **Amazon Fulfillment or Pricing** (either suffices) for `GET_FBA_STORAGE_FEE_CHARGES_DATA`, `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA`, `GET_FBA_REIMBURSEMENTS_DATA` and `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`. The ledger reports list Amazon Fulfillment only, and the settlement V2 report Finance and Accounting. Source: Role Mappings for report types, local copy updatedAt 2026-09-09. [official, command-verified]

**P-tool-27.** Most tools keep two profit views: an order-time "sales/order profit" that includes unshipped orders, and a settlement-time "financial profit" that includes only shipped, settled orders. 赛狐 states this as the cause of their disagreement. Sellerboard separates Profit from a Cashflow module ("Profit shows performance; Cashflow shows liquidity and timing"). Sources: 赛狐 difference explainer; 领星 / 积加 help as cited; Sellerboard cashflow help. [opinion]

**P-tool-28.** Amazon publishes no mapping from its charges to ledger accounts. In Finances v2024-06-19, `breakdownType` is a free string ("The type of charge.") with no enumerated values. `transactionType` and `description` give only examples (`Shipment`; `Order Payment`, `Refund Order`). So every ERP's or connector's account mapping is keyed on charge labels seen in data, or on the settlement report's `amount-type` / `amount-description`. Source: `models/finances-api-model/finances_2024-06-19.json` (clone db2936aa) [official, command-verified]; 领星 KingdeeIntegration ("按映射规则映射为summary项目") [opinion].

**P-tool-29.** 领星's 金蝶云星空 integration pushes documents, and the vouchers are made in 金蝶:
- 销售出库单 "根据站点发货时间，按店铺+订单+按天维度";
- 销售退货单 by return time;
- 收款单 from transferred settlement summaries;
- receivables in one of two modes. "对接店铺月利润报表" (the default) pushes one monthly 费用应收单 of "平台收入、平台支出和税费" at the profit report's second-level items. "对接结算中心结算明细" pushes a 标准应收单, linked to the 销售出库单, for "已发货xx月已结算" lines, and a 费用应收单 for every other line.
Receivable and receipt are written off "按支持相同结算编号" within one period. The two modes use different fee-item codes. Source: 领星 help KingdeeIntegration (created 2023-04-04) [opinion, command-verified].

**P-tool-30.** 领星 states when its 金蝶 data settle and why they differ:
- day-mode data push "最早于次日", month-mode "最早于次月3日";
- the month's FBA receipts, overages, negative receipts and unshipped items "最早可于次月6号推送";
- differences come from "亚马逊数据变动", "一般是近5天的数据不稳定", with occasional re-collection;
- 金蝶 FBA stock, which comes from 领星's cost flow, is checked against that flow only: "无法保证和库存分类账的一致性".
Source: 领星 help KingdeeIntegration [opinion, command-verified].

**P-tool-31.** 金蝶's voucher template sets each voucher's date, voucher word, summary, account, side and amount from document fields. The account rule reads "科目影响因素的来源字段". The GL voucher date can be the document date, the current system date or "期间最后一天". A document type flagged "必须生成总账凭证" blocks 总账结账 until its vouchers exist. Editing the chart without editing the template "可能会导致生成凭证失败或错误". Source: 金蝶云产品手册 凭证模板 [opinion: Kingdee's own manual, command-verified].

**P-tool-32.** 易仓 says it builds the accounting vouchers itself from preset 凭证模板 and pushes them to 金蝶云星空 and 云星辰, manually or on a timer. It sorts settlement-report fee categories "到用户指定的费用项上". 积加 says it pushes to "金蝶、用友、SAP、Oracle", summarising detail by dimension on push (its example is the Date Range report), and offers this to "亿级规模、准 IPO 及上市企业". Sources: eccang.com/news/2390, eccang.com/cwjq.html; jijiaerp.com news 510 (2025-09-10) [opinion, command-verified].

**P-tool-33.** Practitioners carry Amazon's reserve inside the Amazon receivable rather than in profit. An explainer promoting 积加: "应收账款余额 = 账户预留余额 + 净收入额", the reserve being "亚马逊暂扣、未结算给卖家的款项". 万里牛: "核算时把预留变动当作应收处理，不混入当期利润". Whether the reserve sits in the one receivable account or a separate line is not stated by any source read. Sources: ikjzd 1658378894475730945 (2022-02-11); hupun (2026-09-20); with P-tool-6 for the English connectors. [opinion]

**P-tool-34.** Chinese practitioners put Amazon's deductions on different P&L lines:
- 轻松财税: commission, ads, storage and withdrawal fees all to 销售费用, via "应收账款——亚马逊平台";
- 金方圆财务: commission and withdrawal fees to 财务费用 (a 手续费 sub-account), freight and customs to 销售费用, revenue dated at "平台结算完成时间";
- 百运网: commission netted off revenue;
- 畅捷通 (用友 group, marketing): commission "通常作为销售成本的一部分".
The choice moves 毛利 between a ledger and an ERP, not net profit [seat for the last clause]. Sources: 新浪 5328110355744292 (2026-08-04); 搜狐 1024519392_100110381 (2026-05-19); by56 42372; 畅捷通 d84c6a83292e4417829 [opinion, command-verified].

**P-tool-35.** The standards a Chinese ledger posts under:
- CAS 14 art. 34: a principal recognises "按照已收或应收对价总额";
- CAS 19 art. 10 allows the spot rate or a "系统合理的方法确定的、与交易发生日即期汇率近似的汇率" at initial recognition, and art. 11 revalues foreign-currency monetary items at the balance-sheet date, with differences "计入当期损益";
- CAS 1 art. 6 includes "运输费、装卸费、保险费" in inventory purchase cost.
An amount Amazon holds in a foreign currency is a monetary item, so it is revalued at month end [seat for the last clause]. Sources: 企业会计准则第14号, 第19号, 第1号, read from fadada.com law-database copies [official (PRC MOF), via copy; command-verified].

**P-tool-36.** Integration vendors describe the 金蝶 side of Amazon money:
- "亚马逊14天结算 vs 金蝶自然月需做周期切割";
- receivables split "按“费用类型”…销售收入、广告费、FBA 服务费、赔偿";
- receipts without a document number summarised "以“店铺+月份”";
- "仅退款不退货时生成“其他应收单”";
- USD at "当月记账汇率";
- "月末重估价自动生成汇兑损益凭证".
One case closes books "每月 6 号". Source: 轻易云 case articles qeasy.cloud/a/13573, /13407, /13580 (2025-12 to 2026-04; the vendor sells the integration) [opinion, command-verified].

**P-tool-37.** No 金蝶 or 用友 first-party page on Amazon settlement data was found. 金蝶's own pages describe generic "外币核算与自动计算汇兑损益" and "业务单据一键生成凭证" (金蝶AI星辰, 2025-10-10). YonSuite's describe generic "实时汇率转换、自动生成多币种财务报表". The Amazon-specific mapping lives in the ERPs (领星, 易仓, 积加, 赛狐) and in integration vendors' work. Sources: jdy.com 1976537696977367042; yonsuite.com 2250606355082; searches as listed under *Pages read* [opinion; absence by search].

### Seat's notes (enter no skill)

- [seat] When a seller's tool number and cx's number differ, the candidate causes are the dating basis, the FX rule, the deferred treatment, the allocation key, the COGS method and the time zone. The tools' own docs name each of these.
- [seat] SellerApp's published Net Profit formula, read literally, counts Amazon fees twice.
- [seat] A tool still on settlement V1 fallback (A2X documents one) loses that path on 2026-11-11.

## Verification

Date: 2026-11-09/10, by the verifier seat (brief 306). Method: plain GET of public pages with `curl`, tags stripped, the quoted phrase searched on the page text; PDFs read with macOS PDFKit; roles and dates against `web01/role-mappings*.md`, `sp-api-deprecations.md` and the models clone (db2936aa).

**Checked and confirmed as written**
- Marketplace Pulse 2023-02-13: "Amazon is pocketing more than 50% of sellers' revenue - up from 40% five years ago"; "According to P&Ls provided by a sample of sellers, a typical Amazon seller pays a 15% transaction fee …, 20-35% in Fulfillment by Amazon fees (including storage and other fees), and up to 15% for advertising and promotions".
- ILSR (archive.ilsr.org/?p=102720): "Amazon's cut of sellers' revenue in the U.S. has soared to 45 percent".
- Role rows: settlement V2 Finance and Accounting; storage, long-term storage, reimbursements, estimated FBA fees Amazon Fulfillment or Pricing; ledger detail Amazon Fulfillment only; `listTransactions` Finance and Accounting; `listFinancialEventGroups` Finance and Accounting or Account Information Service Provider (EU only); Data Kiosk ops Brand Analytics (P-tool-26 holds).
- Deprecations: settlement V1 flat file and XML removed November 11, 2026 (deprecated March 17, 2025); Finances v0 event operations removed August 27, 2027.
- 积加 FX rule (iWN6Y4MP, 最近修改 2026-11-06); 领星 three bases and the 2026-08-13 release; 赛狐 four time bases and its five-reason FAQ, incl. the Pending/Shipped/Unshipped sentence; PPC Land's Profit Analytics quotes ("1-2 days behind", "up to 7 days", "500,000", "LTL freight").

**Changes made (old → new, why, source)**
1. Reimbursement valuation date: "2025-03-10 (Amazon); some vendors write March 31" → effective **2025-03-31**, moved from March 10 by Amazon's News post of 2025-02-28 (quoted). Changed in the dated list, the §3 seat note, the 白鲸出海 line and the §8 table. This reverses which side was right. Agrees with refunds-reimbursements-adjustments.md E4.
2. Profit Analytics: "2025-09-18 per trade press; no Amazon page read" → Amazon's own words of 2025-09-17 (aboutamazon, Accelerate forum post) and 2025-11-13 (News post), quoted in §A; P-tool-2 retagged official for dates and path, opinion for PPC Land's details.
3. Roles for the economics dataset: "the economics seat's" → the two Amazon statements quoted (Brand Analytics on Role Mappings; Selling Partner Insights in the 2024-07-02 correction).
4. 领星 2026-08-13: "adds a third basis" → adds ship time, framed by its release as the answer to Amazon's Date Range report change; the help page reads ship time from the Transaction report's Date/Time. P-tool-3 rewritten to list 领星's and 赛狐's bases exactly.
5. 赛狐 "每月2号-5号": not on the profit-statement page read 2026-11-10 → marked, source not identified.
6. Tsai: "abstract via snippet; unverified" → read from the PDF, quoted with the 64% figure; P-tool-24 retagged command-verified for Tsai.
7. FTC trial date: "MLex, via search" → PYMNTS/CPI (2026-10-11) quoting Law360 and MLex, quoted; the order itself not read.
8. Bundeskartellamt: secondary GRC Report → also beck-aktuell (2026-02-05), quoted; the authority's own release not reached.
9. §7 extended with sourced facts on multi-entity structures, several accounts in one ledger, FX hedging, the month-end close calendar and fee audits against the rate card.

**Positions:** 27 checked; 5 changed (P-tool-2, -3, -24, -25; the §3 seat note's date); 0 made [seat]; 0 removed. Every position names a tool's or person's practice or a published finding; none sets a rule for cx, a threshold, a sequence or a ceiling. Stable item 9 and §6 ("what sellers most often get wrong") are the named vendors' claims, as the file's bias note says.

**Could not verify**
- Fortune (Del Rey, 2025-02-07) "more than 29%"; Marketplace Pulse 2024-03-18 and 2026-04-16 figures; ILSR 2021 "34 percent"; Waldfogel, Zhu & Liu, Lee & Musolff, Raval, Gutiérrez not re-read.
- The FTC complaint's "close to 50%" (plain GET returns a stub); California v. Amazon trial 2027-01-19 (CA AG release not re-read); EU and CMA commitments (secondary).
- The 2025-01-15 proactive reimbursement date (another Amazon post gives 2024-11-01, refunds sibling); DD+7 2026-03-12 (seller-quoted e-mail; money-flow.md agrees and notes some accounts got 2026-03-05).
- Vendor pages not re-fetched: A2X, Link My Books, Synder, Webgility, Taxomate, Finaloop, Sellerboard, Helium 10 (403), Jungle Scout (403), SellerApp, ShopKeeper, SellerLogic, tool4seller, GETIDA, Seller Investigators, Threecolts, Payability, 8fig; 易仓, 店小秘, 马帮; the Chinese practitioner articles in §5; prices in *Facts for human readers only*.
- The tax "口径" document that AMZ123's 2026-06-01 article says is circulating: not an official document read; treat as reported.

**Cross-file disagreements found**
- Reimbursement valuation date: this file (2025-03-10) vs refunds-reimbursements-adjustments.md (2025-03-31). The refunds file is right; this file fixed.
- Settlement V2 role: product-profit.md had "Amazon Fulfillment or Finance and Accounting"; this file, reconciliation.md and money-flow.md had Finance and Accounting only. Role Mappings list one role; product-profit.md fixed.
- Profit Analytics dates: this file said "2025-09-18, no Amazon page"; product-profit.md had Amazon's pages. Both now agree on 2025-09-17 / 2025-11-13.

**Gaps left** (a senior Amazon finance lead would look for): budgeting and forecast against actuals by SKU; cash-flow forecasting from the settlement calendar and reserve; year-end inventory count and write-down practice (ledger vs physical, LCM/NRV); US sales-tax nexus and 1099-K for non-facilitated sales; audit trail and controls at listed Chinese sellers (e.g. 赛维, 安克 annual-report disclosures on platform revenue recognition); intercompany entries between seller entities (no vendor page found); how large sellers hedge in practice (only vendors' pages found, no independent source).

### Gap fill (2026-11-10)

By the research seat. The gap filled was **ERP to general ledger**: how Chinese ERPs post Amazon money to 金蝶 Kingdee and 用友 Yonyou (vouchers, chart-of-accounts mapping, period close). It was named by the completeness critics. Method: plain GET with `curl`, tags stripped, and quoted phrases matched on the page text; a JSON read of the models clone for the Finances fields; searches for the rest. No Amazon API host was called.

**Added**
- *Amazon's own rules* §F: Amazon publishes no account mapping, and `breakdownType` has no enumeration [command-verified on the model]. Also the three PRC accounting-standard articles a Chinese ledger posts under (CAS 14 art. 34, CAS 19 arts. 10–11, CAS 1 art. 6), from law-database copies.
- *What practitioners add* §9: 领星 → 金蝶云星空 document flows, its two receivable modes, push timing and its own reasons for differences; 金蝶's voucher-template manual; 金蝶云星辰's own page; 易仓's template-built vouchers; 积加's push to 金蝶/用友/SAP/Oracle; the reserve carried inside the receivable (积加 explainer, 万里牛); 轻易云 case notes; 用友's pages; a table of four practitioners placing Amazon's deductions on different P&L lines.
- §8: five rows on why ERP or ledger totals differ from Amazon's views.
- *Stable enough* items 11–13; one *run-time* bullet; *Open questions* 8–10; 17 rows in *Pages read*; an unreachable-pages line.
- Positions **P-tool-28 to P-tool-37** (10 new). None was renumbered. Each states a fact about a named source or Amazon's model. None sets a rule, a threshold or a sequence for cx.

**Gaps left**
- No first-party 金蝶 (kingdee.com) or 用友 (yonyou.com / yonsuite.com) page on Amazon settlement data, an Amazon connector or a cross-border chart-of-accounts template was found. The mapping evidence is the ERPs', integration vendors' and accountants'.
- 领星's full summary-item → 金蝶 fee-item code list is "请联系实施顾问获取", so it is not public. No public 领星 page gives a 凭证模板 or 科目映射 screen for 用友 or for 金蝶云星辰.
- 积加 help pages on 凭证 and 关账/月结 were not found by search. The earlier §7 mention of 积加 关账 keeps no page citation.
- No source read says whether practitioners hold the reserve or the deferred balance in 应收账款 or in 其他应收款. Only "inside the receivable" (积加 explainer, 万里牛) is sourced.
- 知无不言 and 雨果网 posts on 亚马逊 记账 科目 were not found by search (知无不言 is not indexed). The 天赋长江 tax-firm column (cjtax.cn) and a Zhihu entry article were unreachable.
- The CAS texts were read from a law-database copy (fadada.com), not from the Ministry of Finance's own page.

### Correction 1 (2026-11-10)

By the research seat, under brief 306's correction 1 and the plugin zen's item 4: a value that differs by marketplace or changes from year to year is looked up, not carried. Method: each position in *Positions* read for such a value; operation names checked in the models clone (db2936a: `finances_2024-06-19.json` `listBalances` and its `balanceType` values, `financesV0.json` `listFinancialEventGroups` with `FinancialEventGroupStart` / `FinancialEventGroupEnd`, `transfers_2024-06-01.json` `listExpectedPayouts`); report type and column names from this file's SP-API section and reconciliation.md; Amazon's page titles and URLs from this file's *Pages read* and from refunds-reimbursements-adjustments.md's. No page was fetched and no Amazon API host was called.

**Positions changed** (a "Read at run time:" sentence added at the end; the value stays as evidence; no other wording changed, nothing renumbered or removed):
- **P-tool-17.** Recovery vendors' commission shares and look-backs: read from each vendor's own page; no operation or Amazon page gives them.
- **P-tool-18.** Payability's advance rate and commission cap: read from Payability's own pages.
- **P-tool-21.** 领星's reserve description ("最近28天的销售额的5%"): the amount is read from `listBalances` and the settlement V2 reserve lines; the rule behind it stands as read on 2026-11-09, no marketplace named.
- **P-tool-22.** Claim windows (Amazon's US 45–105 days; Helium 10's 60–120): read from Amazon's *FBA inventory reimbursement policy* (G200213130) and the latest News post on claim windows; no operation gives them.

Every other position was left untouched: its substance is a tool's or a person's practice, a published finding, a role mapping, an accounting standard or a dated fact of history (an effective date, a court date, an announcement).

**Stable enough for a skill.** Item 10's "5–25%" and item 12's "every 14 days" moved to *What cx must read at run time*, each with where it is read. Items kept their numbers.

**Dated changes.** The line that called 2025-01-15 the US start of proactive reimbursement → two Amazon dates: "November 1, 2024" in the post created 2024-07-24 on the US forum (6605eede), and "January 15, 2025" in the post created 2024-10-10, in British spelling and naming no store (d0fc997e). No page says which store each addresses; a per-store rollout is a reading only (refunds-reimbursements-adjustments.md P-ref-13). The four pages are added to *Pages read*, reused from that file.
