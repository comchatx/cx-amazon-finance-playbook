# Money Amazon bills or pays outside the settlement

## Advertising

- Amazon Ads' page Update on advertiser payments (2026-04-14) says Amazon told a small number of advertisers it would move them to paying from the seller or vendor account balance or by Pay by Invoice, deferring the change until 2026-08-01. (P-rec-40)
- The same page states that an advertiser who selects no preference gets deduction from the available account balance as the default. (P-rec-40)
- Amazon says balance deduction is already the method of most advertisers. (P-rec-40)
- Amazon's page does not say whether the change took effect; ppc.land and Sellfox report it from 2026-08-01. (P-rec-40)
- Balance-deducted ad charges sit in the settlement as `ProductAdsPaymentEvent` lines carrying the Ads `invoiceId`, `baseValue` and `taxValue`. (P-rec-42)
- Card-paid and Pay-by-Invoice ad charges are billed outside the settlement on monthly invoices; the invoice terms are on Amazon Ads' page Update on advertiser payments, and no SP-API operation gives them. (P-rec-42)
- A card stays on file as a backup even for balance-deducted advertisers. (P-rec-42)
- Ads invoices sit in the ads console's Billing history, per country, with a consolidated statement whose window is stated on Sponsored ads consolidated invoice statement download is now global. (P-rec-42)
- ConnectBooks (a connector) says card-paid ads are not in its settlement import. (P-rec-42)

## Amazon Lending

- Amazon's UK Lending page states repayments are collected "monthly directly via Direct Debit", which takes them outside the settlement. (P-rec-43)
- The US Lending page lists partner lenders and does not say how they collect. (P-rec-43)
- The repayment method is read on the Amazon Lending page of the seller's own store; no SP-API operation gives it. (P-rec-43)
- Loan money that does pass through the account posts as v0 `LoanServicingEvent` (`LoanAdvance`, `LoanPayment`, `LoanRefund`). (P-rec-43)

## Amazon Global Logistics

- Per search snippets of Amazon's help page Paying for Amazon Global Logistics (not read whole), AGL is paid either from the Seller Central disbursement account or by wire through Shipper Central against a Chinese tax bureau invoice; the currencies and paths are on that page. (P-rec-44)
- Per the same snippets, AGL paid from the account appears as "FBA International Freight Shipping Charge" and "FBA International Freight Duties and Taxes Charge", read in Amazon's documents, not yet seen on a live account; AGL paid by wire is outside the settlement. (P-rec-44)
- The AGL charges as they posted are read from the settlement V2 rows by `amount-description`. (P-rec-44)

## Amazon Shipping and Amazon Freight

- Amazon Shipping, the carrier service, bills by invoice in Shipper Central, payable at any time, and by card with autopay. (P-rec-45)
- Finances v0 `AdjustmentItem.TransactionNumber` can carry an Amazon Shipping invoice number; whether every Amazon Shipping invoice appears that way is read in Amazon's documents, not yet seen on a live account. (P-rec-45)
- Amazon Freight extends credit allowances to shippers and is offered by Amazon Logistics, Inc., a separate Amazon company. (P-rec-45)
- Seller Central's Buy Shipping labels, by contrast, are charged in the settlement. (P-rec-45)

## Transparency

- In one seller's account, Transparency codes were invoiced monthly and paid outside the settlement, and Amazon staff named the invoice-remittance and past-due addresses. (P-rec-46)
- No Amazon page read states the Transparency billing rule. (P-rec-46)

## Amazon's invoices for its own fees

- Amazon staff state that Amazon's fee invoices sit in the Tax Document Library, that payment reports show fees as they occur, and that Order ID is the matching key. (P-rec-47)
- The same staff reply expects timing differences at month end between the invoices and the payment reports. (P-rec-47)
- No operation or page gives the invoice timing; research/areas/reconciliation.md, P-rec-47, holds it as read.
- A2X says the invoice uses the transaction completion date, can lag the settlement, and is followed by credit notes for refunded fees or retro-charges; research/areas/reconciliation.md, P-rec-47, holds A2X's lag as read. (P-rec-47)
- ../tax-lines/SKILL.md: Amazon's VAT invoices for its own fees.

## Account-level movements in the v0 model

- `AdhocDisbursementEvent` records money disbursed elsewhere, for example "Disbursed to Amazon Gift Card balance". (P-rec-48)
- `FailedAdhocDisbursementEvent` records a failed one, for example `CREDIT_CARD` and `HARD_DECLINED`. (P-rec-48)
- `DebtRecoveryEvent.ChargeInstrumentList` records charges to an instrument other than the bank deposit. (P-rec-48)
- `ValueAddedServiceChargeEvent` and `CapacityReservationBillingEvent` record charges billed at account level. (P-rec-48)

## Seller Wallet

- Seller Wallet does not change the settlement cycle. (P-rec-49)
- Money moved, converted or charged inside the wallet after disbursement is recorded in the wallet's own statements. (P-rec-49)
- The Seller Wallet API needs AISP or PISP, not Finance and Accounting. (P-rec-49)
