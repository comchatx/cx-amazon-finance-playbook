# Customer refunds as money

## What a refund reverses

- A customer refund reverses the sale's charge lines (principal, tax, shipping, gift wrap) and its promotions. (P-ref-1)
- The Finances v0 model lists those lines per item in `ItemChargeAdjustmentList` and `PromotionAdjustmentList`, and refunds, guarantee claims and chargebacks share one item shape. (P-ref-1)
- Settlement refund rows carry the refund's parts under `amount-type`: `ItemPrice` (`Principal`, `Shipping`, `Tax`, `Goodwill`, `RestockingFee`, `ReturnShipping`, …), `ItemFees` (`Commission`, `RefundCommission`, `ShippingChargeback`, …), `Promotion` and `ItemWithheldTax`. (P-ref-33)
- These values come from public mapping files and vendor glossaries; Amazon publishes no list of them, so they are read from the seller's own file. (P-ref-33)

## The referral fee and the refund administration fee

- On a refund, Amazon returns the referral fee minus a refund administration fee. (P-ref-2)
- The refund administration fee is charged per refunded line item and capped per store in that store's currency. (P-ref-2)
- On a partial refund, the referral fee comes back in proportion to the price refunded. (P-ref-2)
- The rate and cap are read from Amazon's page Selling on Amazon fee schedule (G200336920) as the seller's own store shows it; the amount actually retained is read from a posted refund's fee lines (`listTransactions` breakdowns; v0 `ItemFeeAdjustmentList`). (P-ref-2)
- Practitioners read the settlement `RefundCommission` line as the refund administration fee. (P-ref-33)

## The FBA fulfilment fee

- Practitioners report that the FBA fulfilment fee does not come back on a customer refund. (P-ref-3)
- No Amazon page read says so, and the Finances model neither lists nor excludes such a line, because `FeeType` is an open list. (P-ref-3)
- No live refund's `ItemFeeAdjustmentList` has yet been seen that shows whether any part of the FBA fulfilment fee comes back. (P-ref-3)

## Who triggers a refund

- On seller-fulfilled orders, refunds come from the seller and also from Amazon on the seller's behalf: refund at first scan (prepaid labels), a returnless rule the seller set, the automated refund after the seller's deadline, A-to-z claims, chargebacks and customer service. (P-ref-4)
- A refund in the seller's books is therefore not always one the seller issued. (P-ref-4)
- A Seller Forums News post on sellercentral.amazon.com says that from 2026-01-26 a seller-fulfilled return the seller does not refund within Amazon's window after receipt may be refunded automatically. (P-ref-5)
- That window is read from Amazon's Seller Forums News post "Update to seller-fulfilled refund process by January 26, 2026"; no SP-API operation gives it. (P-ref-5)
- Such an automatic refund cannot be recovered through SAFE-T, except when the item was lost in transit or the delivery confirmation was wrong. (P-ref-5)

## Return labels, restocking fees, return shipping

- From 2026-02-08, US seller-fulfilled returns use Amazon Prepaid Return Labels whatever the item's value, apart from the named category exemptions. (P-ref-6)
- Labels bought through Amazon post as `PostageBilling`, and as `PostageRefund` when a label is refunded, in Finances v0: read in Amazon's model, not yet seen on a live account. (P-ref-6)
- The seller-fulfilled returns reports carry `label_cost` and `label_to_be_paid_by`. (P-ref-6)
- A restocking fee can apply to a seller-issued refund for a damaged or materially different item, or for a return outside Amazon's policy; in Finances it is the `RestockingFee` charge type. (P-ref-7)
- Return shipping is deducted from the refund when the buyer changed their mind, and paid by the seller when the item was defective or misshipped (`ReturnShipping`). (P-ref-7)

## Returnless and partial refunds

- FBA returnless and partial refunds are refunds the seller chose to fund: the unit stays with the buyer and no reimbursement follows. (P-ref-8)
- They count toward the return rate. (P-ref-8)
- FBA Returnless Resolutions has no downloadable report. (P-ref-8)
- Partial refunds show in the FBA Returns dashboard as "Complete – Return not expected". (P-ref-8)
- Returnless refunds do not appear in the FBA customer returns report or the seller-fulfilled returns reports. (P-ref-8)
- Data Kiosk seller analytics `returnedUnits` counts them ("including returnless refunds"). (P-ref-8)

## Which date a refund carries

- The settlement report and Finances date a refund by its posting date. (P-ref-25)
- Data Kiosk economics counts `refundedProductSales` "by refund request time". (P-ref-25)
- Data Kiosk seller analytics attributes returns to the ship date, with a delay its schema states. (P-ref-25)
- The FBA returns report uses the date the fulfilment centre processed the return. (P-ref-25)
- Which of these dates the seller books a refund on is the seller's choice. (P-ref-25)
- Lingxing's order profit offers refund time or order time as the refund's date. (P-tool-4)
- Gerpgo's financial profit dates refunds by settlement time; its sales profit counts them by the order's refund time, not its order time. (P-tool-4)
- Sellerboard matches refunds to their orders and by default moves deferred refunds to their release date, "which can retroactively change past profit figures", with an option to hide them until released. (P-tool-4)
