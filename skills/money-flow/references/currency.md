# Currency: store currency, conversion and the CNY leg

## Store currency and ACCS

- Each store settles in its own currency. (P-flow-26)
- Amazon Currency Converter for Sellers (ACCS) converts at its third-party provider's rate on the day the transfer is initiated, or, for a failed disbursement, on the re-initiation day. (P-flow-26)
- The ACCS fee is tiered on the seller's trailing cross-currency net proceeds across linked accounts, with exceptions by currency and by store. (P-flow-26)
- The tiers and exceptions are read on Amazon Currency Converter for Sellers (US https://sell.amazon.com/programs/amazon-currency-converter; CA https://sell.amazon.ca/cad-usd-currency-converter). (P-flow-26)
- The rate applied to a payout is `ConvertedTotal` against `OriginalTotal` in `listFinancialEventGroups`. (P-flow-26, P-flow-17)
- Amazon's Chinese seller site says a "zero-fee" collector is not "zero-cost": converting twice through a third party adds a second FX loss, while ACCS converts once with tiered pricing; the article is Amazon promoting its own service. (P-tool-16)

## Seller Wallet

- Seller Wallet is Amazon's own account for holding and moving store proceeds. (P-flow-28)
- Seller Wallet dates from 2022 in the US, and press reports a UK launch in 2026-11. (P-flow-28)
- Amazon dates Seller Wallet's EUR launch two ways: an EU forum announcement of 2026-03-09 and trade press of 2026-03-02, against aboutamazon's "In 2025". (P-flow-28)
- Link My Books says enrolling in Seller Wallet does not change the settlement cycle. (P-flow-28)
- Seller Wallet's API needs the AISP or PISP open-banking roles, available only to PSD2-licensed third-party providers with certificate and signature headers, so a seller's own Finance and Accounting app cannot read it. (P-flow-28)
- Which store currencies Seller Wallet covers is on Seller Wallet (https://sell.amazon.com/tools/seller-wallet) and, for the EU, Announcing Amazon Seller Wallet EU; no operation a seller's own app can call gives it. (P-flow-28)

## ACCS CNY

- ACCS CNY pays store proceeds in CNY to a domestic bank account. (P-flow-43)
- Amazon's China page states how many stores ACCS CNY covers without listing them; coverage is on Amazon's ACCS CNY page (https://gs.amazon.cn/accs). (P-flow-43)
- Amazon's China page says all ACCS CNY fees are "included in the exchange rate", and the rate shows on hover over the converted amount in the Payments overview. (P-flow-43)
- Amazon's China page says the ACCS CNY tier follows the seller's trailing net sales, updated monthly, with linked NA, EU and JP accounts pooled. (P-flow-43)
- Amazon's China page states a transit time after Amazon's payment notice; research/areas/money-flow.md, P-flow-43, holds it as read. (P-flow-43)
- Amazon's China page says payments into China under ACCS CNY are processed by the licensed providers PayEase or Fuiou under PBOC and SAFE rules, and that ACCS CNY triggers no extra seller identity verification. (P-flow-43)
- PingPong says ACCS CNY converts on payout, so a seller using it holds no foreign currency. (P-flow-43)
- Amazon China says a PSP's USD account receiving CA or MX proceeds converts twice (local currency to USD to CNY), each with a cost. (P-flow-43)
- The coverage and tiering are on Amazon's ACCS CNY page (https://gs.amazon.cn/accs), and the rate applied to a payout on the Payments overview hover or as `ConvertedTotal` against `OriginalTotal`. (P-flow-43)

## The PSP route under SAFE rules

- SAFE's notice Huifa [2019] No. 13 (2019-04-29) requires a PSP to verify the seller's identity and trade authenticity from transaction information, and to match receipts to the transaction by party, item and amount. (P-flow-44)
- Under that notice a PSP must refuse what it cannot confirm. (P-flow-44)
- Under that notice a PSP keeps single transactions in principle at or below a ceiling, and converts through its partner bank within a set time after receiving funds; both values are read in SAFE Huifa [2019] No. 13 as published in the State Council Gazette (https://www.gov.cn/gongbao/content/2019/content_5428473.htm), or a later SAFE notice that replaces it. (P-flow-44)
- Under that notice a PSP agrees rate quotation, fees, clearing time and FX gains or losses in advance, shows the partner bank's quoted rate, and does not adjust it. (P-flow-44)
- Individuals' conversions under PSP business do not count towards the individual annual facilitation quota. (P-flow-44)
- SAFE's notice Huifa [2020] No. 11 (2020-05-20) lets a cross-border e-commerce firm net some overseas costs against export proceeds. (P-flow-45)
- The costs that notice lets a firm net are overseas warehousing, logistics and tax costs. (P-flow-45)
- For goods exported to an overseas warehouse, the same notice lets a firm receive actual sales income that differs from the declared export value. (P-flow-45)
- Individuals may settle e-commerce receipts through a personal FX account, outside the individual annual facilitation quota, when they provide proof of transaction amounts or electronic transaction information; research/areas/money-flow.md, P-flow-45, holds the quota as read. (P-flow-45)
- Customs codes 9610, 9710 and 9810 (the last for export to overseas warehouses) are the export modes these receipts tie to. (P-flow-45)
- A PSP converts to CNY only up to a "CNY conversion quota": the amount it has verified as having a genuine trade background, after the seller uploads transaction details. (P-flow-46)
- The receiving account at a PSP must be in the seller's own name. (P-flow-46)
- Unlike ACCS, a PSP lets the seller hold store currency and choose when to convert (PingPong, WorldFirst). (P-flow-46)

## Where an FX difference can arise

- For a China-based seller, a first FX difference can arise at the conversion from store currency to payout currency: ACCS at its provider's rate on the transfer-initiation day with the fee inside the rate, seen as `ConvertedTotal` against `OriginalTotal`, or a PSP's conversion between currencies. (P-flow-47)
- A second can arise at the PSP's or bank's conversion to CNY against the partner bank's quoted rate. (P-flow-47)
- A third is the difference between the rate the seller books and the rate received. (P-flow-47)
- CAS 19 books a foreign-currency transaction at the transaction-date spot rate or a systematic approximation, and re-translates monetary items such as receivables at the balance-sheet date, taking differences to profit or loss. (P-flow-47)
- Which booking rate a seller uses (day rate, month-start rate, average rate) is the seller's choice. (P-flow-47)
- Lingxing values a settlement's FX at the month-start rate of the month the settlement began; this is a tool's method, not an Amazon rule. (P-flow-33)
