# Settlement periods and payouts

## The cycle

- Settlement runs on a cycle set by contract, "or at our option, more frequent", and may vary by store; research/areas/money-flow.md, P-flow-11, holds the NA contract's cycle as read. (P-flow-11)
- The store's settlement periods are each group's `FinancialEventGroupStart` and `FinancialEventGroupEnd` in `listFinancialEventGroups`, and the next payout's date is `scheduledDate` in `listExpectedPayouts`, whose answer in NA and FE is read in Amazon's documents, not yet seen on a live account. (P-flow-11)
- The withheld reserve becomes the next period's beginning balance, and the beginning balance includes reserves and failed disbursements. (P-flow-11)
- Amazon's store pages state payout timing for JP, IN, CA, AE, SA and AU; research/areas/money-flow.md, P-flow-36, holds the values as read. (P-flow-36)
- None of those store pages gives a reserve period, and the SG and MX pages give nothing on payouts. (P-flow-36)
- Amazon pays only to a bank account, not to "a credit card or online payment system, such as PayPal". (P-flow-36)
- A store's actual cadence is the group dates in `listFinancialEventGroups` and `scheduledDate` in `listExpectedPayouts`; whether `listExpectedPayouts` answers in NA and FE is read in Amazon's documents, not yet seen on a live account. (P-flow-36)
- The time from payout to bank is each payout's `statusHistory` in `listPayouts`, read in Amazon's documents, not yet seen on a live account. (P-flow-36)

## On-demand payouts

- In the US, Disburse on Demand is open to sellers who completed the move to the delivery-date reserve policy, and needs a positive available balance, an active disbursement instrument and a set interval since the last request. (P-flow-12)
- In Europe the on-demand payout is Disburse Now. (P-flow-12)
- Disburse on Demand and Disburse Now eligibility shows only in Seller Central. (P-flow-12)
- Through the API, `initiatePayout` covers the EU stores listed in the transfers_2024-06-01 model and on the Transfers API page (https://developer-docs.amazon/sp-api/docs/transfers-api.md), with account type `Standard Orders`. (P-flow-12)
- `initiatePayout` allows one payout per store and account type within an interval stated in the transfers_2024-06-01 model and on the Transfers API page (https://developer-docs.amazon/sp-api/docs/transfers-api.md). (P-flow-12)
- Express Payout is US only: a deposit-method choice in Seller Central, with conditions Amazon lists on Get paid faster with Express Payout (https://sell.amazon.com/blog/express-payout). (P-flow-12)
- Amazon China's explainer says each Disburse on Demand withdrawal truncates the current settlement period and restarts it. (P-flow-12)
- Past on-demand payouts show as `type` `ON_DEMAND` in `listPayouts`, whose answer in NA and FE is read in Amazon's documents, not yet seen on a live account. (P-flow-12)
- `initiatePayout` is a money-moving write. (P-flow-13)
- Role Mappings list `initiatePayout` for the EU with "Required roles (need at least one) | Finance and Accounting, Payment Initiation Service Provider", so Finance and Accounting alone suffices. (P-flow-13)
- A seller's app with Finance and Accounting can start a payout in the stores that model lists. (P-flow-13)

## Negative balance

- A negative balance at the end of a settlement period is charged to the payment method on file. (P-flow-15)
- Where the bank imposes a credit limit, Amazon may retry the charge every 24 hours until paid. (P-flow-15)
- A valid card is required of every seller. (P-flow-15)
- The contract also allows offset, invoicing and reversal of bank credits. (P-flow-15)
- In the v0 model, a negative balance's recovery is a `DebtRecoveryEvent` (`DebtPayment`, `DebtPaymentFailure`, `DebtAdjustment`) carrying the card's tail and amount and the original debt's group dates. (P-flow-16)
- In Transfers, `NO_PAYOUT_EXPECTED` means "The expected balance is negative". (P-flow-16)

## Bank account and providers

- Changing or first adding a bank account can defer the remittance calculation under the NA contract (S-5), and in Brazil it causes a reserve; research/areas/money-flow.md, P-flow-30, holds both lengths as read. (P-flow-30)
- A missing or invalid bank account stops a payout from starting, and the effect on the next payout shows in `listExpectedPayouts`, whose answer in NA and FE is read in Amazon's documents, not yet seen on a live account. (P-flow-30)
- Since 2021-07-15, a seller who receives proceeds through a third-party payment service provider must use one participating in Amazon's PSP Program. (P-flow-27)
- Amazon stops disbursement to non-participating providers. (P-flow-27)
- Providers' KYC requests carry deadlines, as one Amazon email shows. (P-flow-27)
- Payability advances a share of the previous day's payouts, with the rest "made available once the marketplace payout is received"; research/beyond/sellers-tools-and-research.md, P-tool-18, holds its rates as read. (P-tool-18)
- Payability's terms cap its purchasing commission and require the marketplace payout to be redirected to Payability. (P-tool-18)
- A seller on such a product sees Amazon's disbursements land with the financier, not in the seller's bank. (P-tool-18)

## Advertising charges

- Amazon's page set a move, from 2026-08-01 after a postponement, for a small, directly contacted group of advertisers from card payment to deduction from the seller balance or Pay by Invoice, with the card kept as backup; whether it took effect is not stated by Amazon. (P-flow-34)
- The earlier date, 2026-04-15, is a seller report on Zhiwubuyan, not on Amazon's page. (P-flow-34)
- For most advertisers, balance deduction is already the method. (P-flow-34)
- ppc.land, quoting Amazon, reports the change from 2026-08-01. (P-flow-34)

## Newer stores

- Amazon.co.za (opened 2024-05) settles in ZAR. (P-flow-48)
- Amazon.co.za says a South African bank account is not needed, but the bank account "needs to be chargeable in ZAR", with ACCS available to receive the proceeds abroad. (P-flow-48)
- On Amazon.co.za the account "must be in your name or the name of your business". (P-flow-48)
- Amazon.co.za fees are "in South African Rand (ZAR) and do not include applicable taxes, such as VAT", and "VAT is additonal to all fees displayed". (P-flow-48)
- The Amazon.co.za pages read publish no reserve period or payout cadence. (P-flow-48)
- Amazon.eg fees are in EGP "excluding applicable VAT. We will additionally apply VAT to all fees displayed above". (P-flow-49)
- Amazon.eg pays proceeds by ACH or EFT to a bank account only, and charges the balance does not cover go to the card. (P-flow-49)
- Amazon.eg states a bank transit time after initiation, and the Amazon.eg pages read publish no reserve period or cadence; research/areas/money-flow.md, P-flow-49, holds the transit time as read. (P-flow-49)
- Amazon.com.tr sellers are companies with a Turkish tax number. (P-flow-50)
- Amazon.com.tr states a first-payout point, a payout cadence and a bank transit time on its seller pages (satis.amazon.com.tr); research/areas/money-flow.md, P-flow-50, holds them as read. (P-flow-50)
- On Amazon.com.tr a payout needs a balance that is not below zero, and the card covers fees the balance cannot. (P-flow-50)
- Referral fees on Amazon.com.tr are subject to KDV (VAT) where applicable. (P-flow-50)
- Whether .com.tr proceeds get ACCS volume pricing is on Amazon Currency Converter for Sellers (CA, https://sell.amazon.ca/cad-usd-currency-converter). (P-flow-50)
- Amazon.ie (opened 2025-03) and Amazon.com.be are EUR stores in the European Seller Central account ("Your professional selling plan will include the Ireland store"). (P-flow-51)
- Whether `initiatePayout` covers IE or BE is in the transfers_2024-06-01 model. (P-flow-51)
- No IE- or BE-specific payout, reserve or fee-VAT rule was found. (P-flow-51)
- ZA, EG, TR, IE and BE all sit in the SP-API's Europe/Middle East/India/Africa store group. (P-flow-51)
