# How sellers' books and tools carry a settlement

## Counting choices (the seller's, none Amazon's rule)

- A settlement that crosses month end can be booked whole on its period or split by the month each line posted; the choice is the seller's. (P-rec-32)
- A2X splits it through a carried-forward account, and Lingxing reconciles a month-crossing statement month by month ("部分对账，需要分月进行对账"). (P-rec-32)
- A2X splits "according to which month the sales or fee actually occurred in". (P-tool-7)
- Link My Books states "Splits only ever happen at calendar month end", with earlier parts rolled forward. (P-tool-7)
- Taxomate splits "to match the sales and the related fees to their own months", and the split can be turned off. (P-tool-7)
- Practitioners describe a clearing account ("Amazon Settlement Clearing") that receives each settlement, with the bank deposit booked as a transfer. (P-rec-33)
- Practitioners describe booking gross sales with fees as expenses, or booking net. (P-rec-33)
- Practitioners describe reserves as a current asset. (P-rec-33)
- Practitioners describe marketplace facilitator tax as a pass-through Amazon withheld, which v0 carries as `MarketplaceFacilitatorTax-*` charge types. (P-rec-33)
- A2X, Link My Books and Bookkeep describe a month-end deferral accrual. (P-rec-33)
- Each of these choices changes what the P&L and the balance sheet show, and none is Amazon's rule. (P-rec-33)

## The reserve in connectors

- A2X books reserve transactions as "neither sales nor expenses", to "Amazon Reserved Balances". (P-tool-6)
- Taxomate states "Reserved Balance is a balance-sheet account". (P-tool-6)
- Webgility states "Record your reserve as a current asset". (P-tool-6)
- Synder books a Transfer to "Balance Reserve". (P-tool-6)
- An explainer promoting 积加 writes "应收账款余额 = 账户预留余额 + 净收入额", the reserve being "亚马逊暂扣、未结算给卖家的款项". (P-tool-33)
- 万里牛 writes "核算时把预留变动当作应收处理，不混入当期利润". (P-tool-33)
- No source read states whether the reserve sits in the one Amazon receivable account or on a separate line. (P-tool-33)

## Deferred money in tools

- Synder shows deferred money only once released ("can only import transactions that Amazon has 'released'"), as does tool4seller Standard. (P-tool-5)
- A2X, Link My Books (an "Amazon Deferred Balances" asset), Finaloop, 领星 (预结算) and tool4seller Enhanced accrue it to the month earned and reverse it on release. (P-tool-5)
- Sellerboard by default shows it, then moves it. (P-tool-5)
- 赛狐 reads it daily from Amazon's deferred data. (P-tool-5)
- 积加 reads Seller Central's Date Range Report, which has no SP-API report type, by "RPA或者插件", and its financial profit refreshes the last 39 days overnight. (P-tool-19)
- A2X says the Date Range Summary now includes deferred transactions, so A2X "will not match Seller Central until you enable deferred transactions adjustments". (P-tool-19)

## Currency conversion

- 领星 and 积加 convert settlement totals at the rate for the month in which the settlement period starts, not the transfer month. (P-tool-8)
- Sellerboard uses "the exchange rate from the last day of the selected reporting period". (P-tool-8)
- Synder uses "Amazon's exchange rate", and Taxomate imports Amazon's own conversion rates. (P-tool-8)
- Finaloop uses "the spot rate at the time of the transaction", and A2X leaves conversion to the ledger. (P-tool-8)
- A Chinese practitioner (金方圆财务) chooses one rate rule ("当月月初汇率或结汇当日汇率") and holds it for the year, books settlement differences to "财务费用汇兑损益", revalues at month end at the official middle rate, and books platform fees separately rather than netting them against revenue. (P-tool-15)

## Clocks in tools

- Link My Books states settlement reports "are in UTC" while business reports use marketplace time, "a 1-10 hour window". (P-tool-20)
- Finaloop reports in UTC against Amazon NA's PST. (P-tool-20)
- 领星 notes "亚马逊配送报告会有3天数据延迟" and syncs only "最近3个月" of settlement data. (P-tool-20)

## Errors practitioners name

- Named accountants and bookkeeping vendors (A2X, Link My Books, Bean Ninjas, Taxomate, ConnectBooks) name the same errors: the deposit booked as revenue, sales tax or VAT booked as income, reimbursements booked as sales, the reserve booked in the P&L, settlements straddling months, and deferred revenue slipping into the next month. (P-tool-13)
- Each of them is a vendor of the fix. (P-tool-13)
- A2X's figure for the share of revenue slipping into the next month is a vendor's; research/beyond/sellers-tools-and-research.md, P-tool-13, holds it as read.
- Chinese practitioners hold that revenue is declared gross ("按客户支付全额交易总额"; "包括平台未回款的部分"), keep accounting, VAT filing and cash received as three separate bases, and call booking "提现净额" as revenue the common wrong practice. (P-tool-14)
- ../tax-lines/SKILL.md: China's platform tax report and how it meets filings.

## Ledger mapping

- Amazon publishes no mapping from its charges to ledger accounts. (P-tool-28)
- In Finances 2024-06-19, `breakdownType` is a free string ("The type of charge.") with no enumerated values, and `transactionType` and `description` give only examples. (P-tool-28)
- Every ERP's or connector's account mapping is keyed on charge labels seen in data or on the settlement report's `amount-type` and `amount-description`; 领星 maps them "按映射规则映射为summary项目". (P-tool-28)
- Amazon's documents give no closed list of `breakdownType` or `amount-description` values, and which ones a seller's data carries is not yet seen on a live account. (P-tool-28, P-rec-4)

## Chinese ERPs and 金蝶 / 用友

- Lingxing reconciles statements against the monthly Summary and splits a statement that crosses months by month. (P-rec-41)
- Sellfox splits each store's month into settled-this-month, deferred-earlier-settled-this-month and deferred-this-month-settled-later, and counts receivables on a shipped or settled basis with time-zone conversion. (P-rec-41)
- Zying shows settlement groups with status open, paid or failed, the opening balance, reserve held, payout and a CNY conversion at the period rate. (P-rec-41)
- 领星's 金蝶云星空 integration pushes documents and the vouchers are made in 金蝶: 销售出库单 "根据站点发货时间，按店铺+订单+按天维度", 销售退货单 by return time, and 收款单 from transferred settlement summaries. (P-tool-29)
- Its receivables run in one of two modes: "对接店铺月利润报表" (the default) pushes one monthly 费用应收单 of "平台收入、平台支出和税费", and "对接结算中心结算明细" pushes a 标准应收单 linked to the 销售出库单 for "已发货xx月已结算" lines and a 费用应收单 for every other line. (P-tool-29)
- Receivable and receipt are written off "按支持相同结算编号" within one period, and the two modes use different fee-item codes. (P-tool-29)
- 领星 states day-mode data push "最早于次日" and month-mode "最早于次月3日", and that the month's FBA receipts, overages, negative receipts and unshipped items "最早可于次月6号推送". (P-tool-30)
- 领星 attributes differences to "亚马逊数据变动", "一般是近5天的数据不稳定", with occasional re-collection. (P-tool-30)
- 领星 states its 金蝶 FBA stock, taken from 领星's cost flow, "无法保证和库存分类账的一致性". (P-tool-30)
- 金蝶's voucher template sets each voucher's date, voucher word, summary, account, side and amount from document fields, the account rule reading "科目影响因素的来源字段". (P-tool-31)
- In 金蝶 the GL voucher date can be the document date, the current system date or "期间最后一天", and a document type flagged "必须生成总账凭证" blocks 总账结账 until its vouchers exist. (P-tool-31)
- 金蝶's manual warns that editing the chart without editing the template "可能会导致生成凭证失败或错误". (P-tool-31)
- 易仓 says it builds vouchers itself from preset 凭证模板, pushes them to 金蝶云星空 and 云星辰 manually or on a timer, and sorts settlement-report fee categories "到用户指定的费用项上". (P-tool-32)
- 积加 says it pushes to "金蝶、用友、SAP、Oracle", summarising detail by dimension on push, and offers this to "亿级规模、准 IPO 及上市企业". (P-tool-32)
- 轻易云, which sells the integration, describes cutting Amazon's settlement cycle against 金蝶's calendar month ("金蝶自然月需做周期切割") and receivables split "按“费用类型”…销售收入、广告费、FBA 服务费、赔偿". (P-tool-36)
- 轻易云 also describes receipts without a document number summarised "以“店铺+月份”", "仅退款不退货时生成“其他应收单”", USD at "当月记账汇率", and "月末重估价自动生成汇兑损益凭证", with one case closing books "每月 6 号". (P-tool-36)
- No 金蝶 or 用友 first-party page on Amazon settlement data was found; their pages describe generic foreign-currency accounting and voucher generation, and the Amazon-specific mapping lives in the ERPs (领星, 易仓, 积加, 赛狐) and integration vendors. (P-tool-37)

## Where deductions land in a Chinese ledger

- 轻松财税 books commission, ads, storage and withdrawal fees to 销售费用, via "应收账款——亚马逊平台". (P-tool-34)
- 金方圆财务 books commission and withdrawal fees to 财务费用 (a 手续费 sub-account), freight and customs to 销售费用, and dates revenue at "平台结算完成时间". (P-tool-34)
- 百运网 nets commission off revenue, and 畅捷通 (用友 group, marketing) treats commission "通常作为销售成本的一部分". (P-tool-34)
- CAS 14 art. 34: a principal recognises revenue "按照已收或应收对价总额". (P-tool-35)
- CAS 19 art. 10 allows the spot rate or a "系统合理的方法确定的、与交易发生日即期汇率近似的汇率" at initial recognition, and art. 11 revalues foreign-currency 货币性项目 at the balance-sheet date, with differences "计入当期损益". (P-tool-35)
- CAS 1 art. 6 includes "运输费、装卸费、保险费" in inventory purchase cost. (P-tool-35)
