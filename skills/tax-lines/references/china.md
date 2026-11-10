# China-based sellers

## Platform reporting

- Under China's State Council Decree 810 (in force from June 2025) and STA Announcement 2025 No. 15, every platform reports to China's tax authority, in the month after each quarter, the identity and prior-quarter income of its in-platform operators. (P-tax-33)
- Overseas platforms report through a licensed domestic entity, a domestic service entity, or a designated domestic agent. (P-tax-33)
- The first report covered Q3 2025; data from before the Decree took effect is not reported. (P-tax-33)
- Overseas platforms need not report the identity of their overseas-resident sellers. (P-tax-33)
- As China Daily and Zhonglun relay Amazon's notice (Amazon's own page not reached), Amazon reports China-based sellers to China's tax authority quarterly, whatever Amazon store they sell in: identity, order count, income, and the commissions and service fees paid to Amazon. (P-tax-34)

## What the reported income is

- The income a platform reports is gross: 收入总额 is all consideration including VAT, "不扣除…向平台企业支付的佣金、服务费" (not reduced by commissions and service fees paid to the platform). (P-tax-35)
- It is reported with refunds, net income and order count, and it is therefore not the payout. (P-tax-35)

## Amazon's China tax report

- AMZ123's pieces relay Amazon's FAQ: the figure is dated by order ship date and converted to RMB at the PBOC central parity of the ship day. (P-tax-36)
- By the same relay, reported income includes shipping, gift wrap, discounts, taxes (overseas VAT and US sales tax among them) and surcharges. (P-tax-36)
- By the same relay, fees (referral, fulfilment, cross-border freight, sponsored ads, subscription) are reported as one total. (P-tax-36)
- By the same relay, Amazon says the figure is expected to differ from the Payments and Amazon VAT Transactions reports. (P-tax-36)
- No operation or page gives these bases; research/areas/tax-and-invoices.md, P-tax-36, holds them as read. (P-tax-36)
- The report reaches the seller only by email from `donotreply@amazon.com`, with a link valid for a limited time; research/areas/tax-and-invoices.md, P-tax-37, holds the value as read. (P-tax-37)
- No SP-API operation or report type carries Amazon's China tax report. (P-tax-37)
- STA Announcement 2025 No. 15 requires a platform to correct errors within a set period of finding them; research/areas/tax-and-invoices.md, P-tax-37, holds the period as read. (P-tax-37)
- AMZ123 reports that Amazon re-filed corrected Q4 2025 data for some sellers in September 2026. (P-tax-37)

## Overseas income and residence

- A Chinese resident individual declares overseas income in a window of the following year; research/areas/tax-and-invoices.md, P-tax-38, holds the window as read. (P-tax-38)
- Tax authorities match financial-account data received under CRS against filings, and recover unpaid tax with late fees within a limitation period; research/areas/tax-and-invoices.md, P-tax-38, holds the period as read. (P-tax-38)
- Since 2025 tax authorities have reminded taxpayers to self-check their 2022–2024 overseas income. (P-tax-38)
- A company incorporated abroad (for example in Hong Kong) whose 实际管理机构 (place of effective management) is in China is a Chinese resident enterprise, taxed on income from inside and outside China. (P-tax-39)
- Marketplace Pulse reports sellers' moves of their Amazon entity to Hong Kong. (P-tax-39)

## Export customs modes

- Chinese exports leave under a named customs mode: 0110 general trade, 9610 cross-border e-commerce retail, 9710 B2B direct export, 9810 export to an overseas warehouse, 1210 bonded zone, or 1039 market procurement. (P-tax-40)
- The 9810 mode was created by GACC Announcement 2020 No. 75. (P-tax-40)
- Practitioners (优品跨境物流) match FBA to 9810. (P-tax-40)

## Export VAT refund and exemption

- Since January 2025, goods exported under 9810 may have their export VAT refund claimed on departure, flagged HWC-YT. (P-tax-41)
- The claim is reconciled against actual sales by a date in the year after it was processed, or clawed back, and unsold goods are repaid in full; research/areas/tax-and-invoices.md, P-tax-41, holds the date as read. (P-tax-41)
- The seller keeps sales vouchers and ledgers for each sale, within a period STA Announcement 2025 No. 3 sets; research/areas/tax-and-invoices.md, P-tax-41, holds the period as read. (P-tax-41)
- An overseas-warehouse booking note may be filed in place of an export contract. (P-tax-41)
- Exporters registered in a cross-border e-commerce comprehensive pilot zone may export goods without valid purchase invoices exempt from VAT and consumption tax (财税〔2018〕103号). (P-tax-42)
- Such firms may pay enterprise income tax on a deemed taxable-income rate applied to total revenue (STA Announcement 2019 No. 36). (P-tax-42)

## What Amazon's records give as evidence

- In the Inventory Ledger, a receipt row's `Reference ID` is a "Transaction ID, such as a shipment ID", and sales leave as `Shipments` rows by FNSKU. (P-tax-43)
- So Amazon's records give the inbound shipment for each receipt and each sale's date and quantity; the columns do not tie a sale to the inbound shipment it came from. (P-tax-43)

## Amazon's fees in a Chinese ledger

- Amazon's fees come from Amazon entities outside China and carry no Chinese 发票. (P-tax-44)
- For a Chinese enterprise, spending on services bought from abroad is deducted on "对方开具的发票或者具有发票性质的收款凭证" (the other party's invoice or a receipt with invoice character). (P-tax-44)
- The tax authority may ask for confirmation by a foreign notary or CPA. (P-tax-44)
- No SP-API operation found returns the invoices Amazon issues to sellers for its fees; they sit in Seller Central, and references/reads.md holds the detail. (P-tax-12)
