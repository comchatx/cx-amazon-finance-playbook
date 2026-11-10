# Inbound freight: AGL, SEND, Amazon Freight and GWD

## Amazon Global Logistics (AGL)

- Amazon, or the affiliate named on the invoice, bills AGL; for China-origin services and ocean carriage from China that is Beijing Century Joyo Courier Co., Limited. (P-ful-29)
- AGL bills on delivery to the destination, or as costs are incurred. (P-ful-29)
- The seller pays every cost at the destination (freight, insurance, export, customs, duties, taxes, accessorials) "regardless of whether you are the IOR". (P-ful-29)
- AGL is paid either from the Seller Central disbursement balance or by wire through Shipper Central; the currencies are on Seller Central help *Paying for Amazon Global Logistics*. (P-ful-30)
- Balance-paid AGL appears in Transaction View under Service Fees as "FBA International Freight Shipping Charge" and "FBA International Freight Duties and Taxes Charge". (P-ful-30)
- Balance-paid AGL is charged after receipt at the fulfilment centre, and "additional fees" can follow later; the timing is on *Paying for Amazon Global Logistics*, and the dates a line actually posted are its `postedDate` in `listTransactions`. (P-ful-30)
- The AGL Preliminary Estimate and Collection Fee Estimate exclude import and export duties and taxes, accessorial charges and other services. (P-ful-31)
- The AGL charge moves with Amazon's or the carrier's measured weight and dimensions, and with the rate in effect on the cargo-ready or gate-in date. (P-ful-31)
- Cancellation fees, demurrage, detention, storage, exam fees and abandonment costs fall on the seller. (P-ful-31)
- Overcharge notices have a window from receipt of the invoice, stated in *Amazon Global Logistics Freight Service Terms* in the version in force for the booking, and accepted claims may be credited to the account. (P-ful-31)
- Amazon is the broker on an AGL entry, not the importer of record: the seller names the IOR (by default the seller), signs a power of attorney for Amazon's broker, and in the US holds a customs bond. (P-ful-32)
- Brokerage is included in the AGL price. (P-ful-32)
- Duty refunds from customs, such as IEEPA refunds after 2026-02-20, go from CBP to the IOR, outside the seller's Amazon balance. (P-ful-32)
- The duty on a US AGL entry is set by a duty bill the broker builds from the commercial invoice and packing list; the importer confirms or disputes it, and it auto-confirms if neither happens in time. (P-ful-33)
- Duty is paid before liquidation, either advanced by the broker or paid by the importer through its own ACH account. (P-ful-33)
- A duty bill can be corrected later: by the broker before the preliminary statement date, by Post Summary Correction before liquidation, and by protest after liquidation, so the duty first charged on a shipment can change months later. (P-ful-33)
- The confirmation, auto-confirmation and correction windows per import country are in Amazon's course *Logistics: cross-border logistics, import clearance preparation* (PDF). (P-ful-33)
- EU and UK duty bills also have a confirmation step, and JP bills auto-confirm. (P-ful-33)
- Amazon Managed Placement is a flat per-shipment rate that includes destination charges and no separate placement fee. (P-ful-34)
- Seller Managed Placement eliminates placement costs, subject to a minimum of identical boxes per item stated on the sell.amazon.com AGL page. (P-ful-34)
- AGL minimal shipment splits incur the inbound placement fee, and ship to AWD carries no separate placement fee. (P-ful-34)
- Practitioners (AMALYTIX, MyRealProfit, Synder) report AGL line names `FBAInternationalInboundFreightFee` and `FBAInternationalInboundFreightTaxAndDuty`, "FBA International Freight Shipping Charge Adjustments", and `GlobalInboundTransportationFreight` and `GlobalInboundTransportationDuty`; these are not an Amazon list and are not yet seen on a live account. (P-ful-38)

## Amazon SEND

- In the US, Amazon SEND bills to the Seller Central account: freight posts after booking as "FBA international shipping charge". (P-ful-35)
- SEND destination duty posts after delivery, at the actual duty customs charged the carrier, as "FBA international shipping customers charge". (P-ful-35)
- SEND carriers issue no invoices. (P-ful-35)
- In Australia SEND is contracted and paid with the carrier directly, offline, and the carrier passes on any duty. (P-ful-35)
- The billing currency and posting times are on *Amazon SEND (Seller Export & Delivery)* (US) or *Amazon SEND* (AU), and the posted lines and dates are in `listTransactions`. (P-ful-35)

## Amazon Freight and GWD

- Amazon Freight bills in its own shipper account: invoices sit in the portal's Billing & Payments table, on a credit limit set from payment and credit history and reviewable monthly. (P-ful-36)
- Global Warehousing and Distribution (from 2026-04-09) stores stock in China (Shenzhen; Shanghai from 2026-07-16) and replenishes US FBA through AGL, which a user must onboard. (P-ful-39)
- Under FOB, GWD's export declaration and origin port handling are invoiced separately. (P-ful-39)
- GWD's fee schedule was not public on any Amazon page read on 2026-11-10. (P-ful-39)

## What the API reaches

- No SP-API operation reads AGL bookings, estimates, Shipper Central statements, debit notes or broker duty bills. (P-ful-37)
- Fulfillment Inbound v2024-03-20 lists ocean and air `shippingMode` values but only partnered-carrier and own-carrier `shippingSolution` values. (P-ful-37)
- Balance-paid AGL and SEND lines reach Finances (Finance and Accounting role) under open-ended names, and Finances v0 `ServiceFeeEvent` has no inbound-shipment field. (P-ful-37)
- The Tracking API (grantless, US, from 2026-08-05) gives customs and delivery milestones without amounts. (P-ful-37)
- The Invoices API v2026-06-25 has no freight or duty field. (P-ful-37)
- One AGL shipment's cost is recorded in several places: the booking's Preliminary Estimate, balance lines posted in stages (freight, then duties and taxes, then "additional fees"), Shipper Central statements and debit notes for wire payers, the broker's duty bill, and any placement line, depending on the option booked. (P-ful-40)
- A settlement-built cost and the seller's own freight records can each hold part or all of one shipment's cost; which record a seller treats as the cost, and how it avoids counting a shipment twice, is the seller's choice. (P-ful-40)
