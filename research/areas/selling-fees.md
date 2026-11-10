# Selling, program and service fees: what Amazon charges beyond fulfilment, and where each charge lands

Read 2026-11-09 by the research seat. Tags:
- **[official]**: Amazon's own page, post or model.
- **[opinion]**: a named practitioner or vendor.
- **[research]**: a published study.
- **[seat]**: this seat's reasoning, never a position.
- **[command-verified]**: a command run over the local models clone (`~/ComChatX_Project/scratch/sp-api-plugins/models`, commit db2936aa, 2026-10-29) or over the saved Amazon pages in `web01/`.

**How the web was read.**
- Plain GET only. No Amazon API host was called, and nothing was POSTed to the help hub.
- Every Seller Central help page tried returned a navigation or JavaScript shell with no article body. That held for both the `/gp/help/external/<id>` and the `/help/hub/reference/external/<id>` forms, across the US, UK, EU and JP hosts. Where a help page is quoted, the words come from:
  - a search-engine snippet, marked "(snippet)";
  - an Amazon staff post on Seller Forums (`News_Amazon`, `*_Amazon`), sell.amazon.*, aboutamazon.* or gs.amazon.cn; or
  - the listing playbook's reading of 2026-10-14. That seat read help pages through the help-hub content call, which this pack's brief forbids, so those quotes cannot be re-read here and are marked "(listing seat, 2026-10-14)".
- Web pages were read through fetch helpers. A "direct" quote is the fragment the helper returned from the live page.

## What this covers

**Scope.** Every charge or credit Amazon books against a seller that is not a fulfilment or logistics charge:
- referral fees, closing fees, the per-item fee, the subscription, the high-volume listing fee, the refund administration fee;
- the digital services fee;
- program and promotion fees: coupons, deals, Prime Exclusive Discounts, Vine, Transparency, Amazon Business, Handmade;
- program credits: Brand Referral Bonus, New Seller Incentives, the FBA New Selection program;
- the advertising charge as it shows in finances, Buy Shipping label charges, A-to-z, chargeback and SAFE-T debits (as charges only);
- the currency conversion fee (ACCS) and the EU VAT on Amazon's fees;
- EU and UK extended producer responsibility (EPR) charges Amazon pays on a seller's behalf (eco-contributions and the service fee), and the EPR reserve (section P, added 2026-11-10);
- Amazon Haul (and Amazon Bazaar) and "FBA from origin" as stores whose money is marked apart in the API (section Q, added 2026-11-10).

For each, the file records Amazon's definition, how it is computed, and every place it is recorded: Finances v2024-06-19, Finances v0, settlement V2, the fee previews, Product Fees, Data Kiosk economics, the Promotions API and notifications.

**Out of scope.**
- FBA fulfilment, storage, inbound, removal, AWD and MCF charges belong to a sibling seat. They appear here only where they share a record with a selling fee.
- Ads API spend is another seat's.
- Refunds as refunds are a sibling's. Here they appear only as what a refund does to the referral fee.

**Skills it would feed.**
- A `fees` skill: definitions, how each fee is computed, where each lands, and the open label sets.
- The `profit` skill: what a per-unit fee figure includes and leaves out, and the program costs that need allocation.
- Any reconciliation or accounting-export skill: the labels, and which fee reverses on a refund.

**Why a senior operator cares.**
- Selling fees are usually the largest Amazon charge after FBA.
- They are computed on a base that differs by marketplace (tax-inclusive or not) and change on dated announcements.
- They land under labels Amazon never lists.
- The known overcharge routes are a wrong fee category, a refund administration fee on every refund, program fees charged despite a credit, and a subscription charged without listings. A seller finds each only by reading the labels against the rules.

**Dated changes since 2025-01-01** (each sourced in the sections below):
- **2025-02-01, EU.** Heavy-bulky minimum referral fee cut (gs.amazon.cn, snippet).
- **2025-04-07, IN.** Zero referral fee below ₹300 in 135+ categories.
- **2025-06-02, US/UK (EU and JP per practitioners).** Coupons move from a per-redemption fee to an upfront fee plus a percentage of coupon sales. Deals move from a flat per-deal fee to a per-day fee plus a capped percentage.
- **2025-07-15, US.** Coupon fee lines relabelled in the transaction view: "Coupon Performance Based Fee / Coupon Participation Fee" under "Amazon Fees". Seller-observed; not denied by staff.
- **2025-08-01, AU.** "some of our fees" adjusted. Referral mostly unchanged. **2025-08, SG.** Referral fee changes (snippet).
- **2025-10-01, US.** Amazon Business bulk-order referral fee discount.
- **2025-11-05.** Coupon variable fee cut and capped for coupons created from this date: UK (official), EU (practitioner), US and CA (listing seat and snippet).
- **2025-12-15, EU/UK.** Clothing referral cut for low-price items.
- **2026-01-05, EU/UK.** Home, Pet, Grocery and Vitamins low-price referral cuts. First announced for 2026-02-01, then moved.
- **2026-01-15, US.** The yearly fee changes. Amazon names no referral rate change.
- **2026-02-17, MX.** Subscription cut. **2026-03-03, MX.** Some referral increases. **2026-06-04, MX.** Grocery threshold raised.
- **2026-03-16, IN.** Zero referral below ₹1,000 in 1,800+ categories; cuts above. **2026-09-07, IN.** Closing fees raised.
- **2026-03-20, EU/UK.** The digital services fee becomes based on the DST rate of the country of sale.
- **2026-04-01, JP.** Referral +0.4 points above ¥750, and on media at every price.
- **2026 peak events (US).** Best Deals, Lightning Deals and Prime Exclusive Price Discounts: an upfront fee plus a capped percentage.
- **2026-07-30, US.** FBA New Selection program (2026) with referral caps on early units (practitioners).
- **2026-08-01, US.** Ads billing option change for contacted advertisers (practitioner quoting Amazon).
- **2026-11-05, US.** The 2027 fee letter. FBA fees up from 2027-01-15. Amazon's letter does not mention referral rates at all; practitioners report a lower 3D-printer rate, a Renewed promotion, a "Buy X, Get Y" fee and monthly promotion billing from 2027-02.
- **2026-11-11.** Settlement V1 flat file and XML removed; only `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` remains.
- **2027-08-27.** Finances v0 `listFinancialEvents*` removed (deprecated 2025-07-21).
- **EPR and Haul dates (gap fill, 2026-11-10; sourced in P and Q):**
  - **2025-01 (ES).** Sellers on Amazon.es with no valid packaging ERN by 2024-12-31 are enrolled in EPR Pay on Behalf (Amazon notice as relayed by AMZ123 / baijing, 2024-03-11).
  - **2025-04-01 (UK).** An annual EPR Pay on Behalf service fee per EPR category starts for sellers not established in the UK (News_Amazon).
  - **2025-05-06 (UK).** Amazon Haul launches in the UK (aboutamazon.co.uk). **2025-05-28** Sales `getOrderMetrics` takes `amazonProgram=AmazonHaul`; **2025-06-25** `listTransactions` marks Haul transactions with `storeName` `AMAZON_HAUL` (release notes).
  - **2025-08-27 (UK, ES, FR).** One EPR Pay on Behalf policy: fee reserves and charges outside the reporting cycle (News_Amazon).
  - **2025-11 (FR, ES).** Some sellers' EPR Pay on Behalf moves to an account-level reserve (gs.amazon.cn, 2025-11-12). Haul's "beta" label removed; Haul serves 25 locations, some as Amazon Bazaar (aboutamazon.com, 2025-11-10).
  - **2025-12 (CN summit).** Amazon announces 源仓全球履约服务 (Fulfill From Origin, FFO), already run on Haul, to widen in 2026 (Chinese media reports).
  - **2026-04 (EU).** `EPRChargebackServiceFee` and `EPRChargebackEcoFee` lines first seen in a practitioner's settlement data (AMALYTIX).
  - **2026-11-06.** `storeName` value `AMAZON_FBA_FROM_ORIGIN` announced for `listTransactions` (changelog 2026-10-21); not in the rolled-back model.

## Amazon's own rules

### A. Referral fee: base, rate, minimum, tiers

- **A1. What it is charged on (US).**
  - "For every item sold, you'll pay a percentage of the total price or a minimum amount, whichever is greater." "An item's total price includes its list price, as well as shipping costs and any gift-wrapping charges." "Note: A product's fee category may not be the same as the category that appears to customers in the Amazon store." [official] *How much does it cost to sell on Amazon?*, https://sell.amazon.com/pricing (direct, 2026-11-09; the fee-category note as quoted in the ads playbook's `beyond/goals-and-economics.md` §C).
  - The help page adds the tax exclusion: "For all products, Amazon deducts the applicable referral fee percentage calculated on the total sales price, excluding any taxes calculated through Amazon tax calculation services. The total sales price is the total amount paid by the buyer, including the item price and any delivery charges or gift wrapping charges." And: "Referral fee = [(Item price + delivery charges + giftwrap charges) multiplied by the category referral fee rate] OR [applicable minimum referral fee], whichever is greater." [official] *Referral fees*, https://sellercentral.amazon.com/gp/help/external/200735910 (snippet). The same wording, with "Amazon deducts the greater of the applicable referral fee percentage or applicable per-item minimum referral fee", is in *Selling on Amazon fee schedule*, G200336920 v119 (listing seat, 2026-10-14).
- **A2. Two kinds of price tier.** Both appear on sell.amazon.com/pricing (direct) and G200336920 (listing seat).
  - *Whole price*: the rate for the whole price changes at a threshold. Example: "8% for products with a total sales price of $10.00 or less, and 15% for products with a total sales price greater than $10.00". Used for Baby; Beauty, Health and Personal Care; Clothing and Accessories (three bands); Grocery and Gourmet; Lawn Mowers and Snow Throwers.
  - *Portion of price*: only the part above the line pays the second rate. Example: "15% for the portion of the total sales price up to $200.00". Used for 3D Printers; Compact Appliances; Electronics Accessories; Fine Art (four portions, "with a minimum Referral Fee of $1.00"); Furniture; Jewelry; Watches.
  - Other marketplaces use both kinds too. UK examples: Furniture "15% for the portion of the total price up to £175.00"; Clothing "5% for items priced at or up to £15" (sell.amazon.co.uk/pricing, direct). JP: clothing above ¥3,000 is charged 「3,000円までの部分については…12.4%、3,000円を超える部分については…8.4%」 (12.4% on the part up to ¥3,000, 8.4% on the part above) (sell.amazon.co.jp/pricing, direct). AU: Computers "8% for the portion of the total sales price of $150 or less" (sell.amazon.com.au/pricing, direct).
- **A3. The tax base differs by marketplace.**
  - **US**: excluding taxes Amazon calculates (A1).
  - **JP**: tax-inclusive. 売上の合計 (the sales total) is 「商品の価格、配送料、ギフト包装料を含む購入者によって支払われた合計金額」 (the total paid by the buyer, including item price, shipping and gift wrap). A footnote says it includes 「購入者によって支払われた適用のある税金額」 (applicable taxes paid by the buyer). [official] sell.amazon.co.jp/pricing (direct).
  - **MX**: the base includes IVA, and so does the MXN 8.00 minimum. [official] vender.amazon.com.mx/precios (direct).
  - **BR**: "A porcentagem da comissão é calculada em relação ao preço total de venda do produto (preço final do comprador)" (the percentage is applied to the product's total sale price, i.e. the buyer's final price). [official] venda.amazon.com.br/precos (direct).
  - **UK/EU**: Amazon's pages contradict each other.
    - The UK body text is the total "including the item price and any delivery or gift wrapping charges", while its FAQ says "excluding any taxes" (sell.amazon.co.uk/pricing).
    - DE and FR have the same split. The DE body says 「der vom Käufer zu zahlende Gesamtbetrag」 (the total the buyer pays) and the FAQ says 「ohne Steuern」 (excluding taxes). The FR body says 「prix total (comprenant le prix de l'article, les frais d'expédition et les frais d'emballage cadeau)」 (total price, including item price, shipping and gift wrap) and the FAQ says 「prix hors taxes」 (price excluding taxes) (sell.amazon.de/preisgestaltung, sell.amazon.fr/tarifs, direct).
    - Amazon India's Global Selling page says the EU fee is "calculated as a percentage of the total sales price (including VAT where applicable)" (https://sell.amazon.in/grow-your-business/amazon-global-selling/cost-to-sell-in-europe, direct).
    - A gs.amazon.cn snippet says the opposite: 「佣金按不含增值税的售价计算」 (commission is calculated on the price excluding VAT); its source page was not identified.
    - The staff "Referral Fees Series Part 2" gives only "Referral Fee = Total Price * Referral Fee Percentage" (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/e5b39e29-db38-4d08-a887-d62d0699bf48).
    - [opinion] Sellers on SC-EU threads report the fee charged on the VAT-inclusive price. Elver Accountants (UK) says the base excludes VAT.
    - Unresolved. The charged `Commission` against the order's principal and tax shows it per order.
  - **AE/SA**: "a percentage of the total price—including item price, shipping cost, and any gift-wrapping charges"; "All listed fees are displayed excluding applicable VAT" (sell.amazon.ae/pricing, sell.amazon.sa/pricing, direct).
- **A4. Minimums differ; AU has none.**
  - Per-item minimums: US "$0.30" in most categories; CA CAD 0.40; MX MXN 8.00; BR R$1 or R$2; UK £0.25; EU €0.30; JP ¥30; AE AED 1; SA SAR 1.
  - Media, and in some stores grocery, carry no minimum.
  - "There is no minimum or maximum referral fee." [official] sell.amazon.com.au/pricing (direct). (Pages as in A2/A3; CA sell.amazon.ca/pricing, direct.)
- **A5. The fee category is Amazon's assignment, not the browse category** (A1's note). A wrong category can be disputed:
  - "If you believe you were charged an incorrect referral fee (e.g., wrong fee category applied), you can request a review"; "only one claim per charge is allowed, and Amazon's appeal decision is final"; "Pull your Custom Unified Transaction report". [official, staff post] Roberto_Amazon, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/ff7c3c15-8655-4086-af58-9b726d178e77.
  - An Amazon policy notice (snippet only; source post not opened) says that from 2023-01-13 reimbursement is "based on the referral fee rate effective at the date of the disputed transaction", with the fee-category guidelines submitted with the claim.
- **A6. Before or after a seller discount?** No Amazon page read states whether the referral fee is computed on the price before or after a seller coupon or promotion.
  - The only Amazon wording is "the total amount paid by the buyer" (A1).
  - [opinion] A2X says after: "Amazon will deduct the referral fee from the new discounted price". Gorilla ROI and Dotcomreps agree.
  - [opinion] SellerView.ai and a non-staff forum poster say before ("Referral fee will start for the full price", https://sellercentral.amazon.com/seller-forums/discussions/t/4ab076bd8ae3d522592b4008816110b1).
  - The order's own `Commission` against its `Principal` and `Promotion` lines answers it per order (section *SP-API faces*).
- **A7. Category rate tables live on Amazon's pages and move by announcement.** Rates are in *Facts for human readers only*.

### B. Closing fees and the per-item fee

- **B1. Media closing fee (US).**
  - "In addition to the referral fee, media items incur a closing fee $1.80 per item." [official] sell.amazon.com/pricing (direct).
  - "Sellers also pay a closing fee of $1.80 per item that is sold in the categories of Books, DVD, Music, Software & Computer/Video Games, Video Game Consoles, and Video Game Accessories." [official] G200336920 (snippet).
  - **Name mismatch.** The fee is flat in the US, yet Amazon's machine names call it variable. Data Kiosk has `CLOSING_FEES`, "Closing Fees, also know as Variable Closing Fees". The MWS fee-type table mapped `VariableClosingFee` to "Closing Fees" (Finances_FeeTypes, snippet; the MWS host no longer resolves).
- **B2. Per-item fee (Individual plan).**
  - It is named `FixedClosingFee` in Amazon's machine names. Data Kiosk `PER_ITEM_SELLING_FEES` is "Per-item Selling Fees, also know as Fixed Closing Fee" [command-verified, analytics_economics_2024_03_15.graphql]. The MWS table: `FixedClosingFee` = "Per-item fees for Individual Sellers" (snippet).
  - So `FixedClosingFee` is **not** the media closing fee.
  - US: "$0.99 / item sold" (sell.amazon.com/pricing, direct).
- **B3. Other marketplaces.**
  - AU: "All sellers (regardless of plan type) also pay a closing fee of $1.00 per media item that is sold" (direct).
  - UK, DE and FR describe "a fixed fee charged on certain types of product sales" without amounts (direct).
  - JP's page shows no 成約料 (category closing fee) line. Practitioners cite Seller Central's 変動するカテゴリー成約料 (variable category closing fee) page.
  - **IN** has a broad "Closing fee: starts at ₹ 2, Varies by product price range and fulfillment channel" (FBA, Easy Ship, Self Ship, Seller Flex). From **2026-09-07**: "we are updating closing fees for sellers in India", +₹1 up to ₹500 and +₹3 above. [official] sell.amazon.in/fees-and-pricing (direct).
  - AE/SA pages show no closing fee.

### C. Subscription and high-volume listing fee

- **C1. Professional subscription.**
  - US: "$39.99/month + selling fees"; "You pay a monthly subscription fee of $39.99 per month no matter how many items you sell"; "your subscription begins immediately after upgrading". The page advises timing the switch "to avoid unexpected prorated charges", so proration exists. [official] sell.amazon.com/pricing; *Amazon's Individual vs Professional selling plan*, https://sell.amazon.com/blog/amazon-professional-vs-individual-selling-plan (2025-10-01) (direct).
  - **Is it charged with no active listings?** No current US Amazon page read says either way.
    - AU's page conditions it: "$49.95 (excl. GST)/month when you have active listings" (direct).
    - [opinion] Seller Union quotes a 2021 Amazon announcement for unified NA accounts: "You will be charged subscription fees only where you have active listings during the current month".
    - [opinion] A2X says the fee "is charged regardless of whether any sales are made" and "Amazon may charge the registered credit card on file".
  - A correction posts as `ChargeRefundEvent` with `ReasonCode` "For example, `SubscriptionFeeCorrection`" [command-verified, financesV0.json].
  - Handmade: "The monthly Professional selling fee is waived when you sell on Handmade", "following a one-time, first-month payment" [official] https://sell.amazon.com/programs/handmade (direct).
  - MX: the Professional plan is free for 12 months, then tiered by the prior month's sales; cut from 2026-02-17 ("Reduciremos la tarifa de suscripción mensual", we will reduce the monthly subscription fee) (vender.amazon.com.mx/precios; https://sellercentral.amazon.com.mx/seller-forums/discussions/t/2ce2205a-31fe-45b4-9c5b-9b47d039bd28, direct).
  - BR: first year free, then monthly (venda.amazon.com.br/precos, direct).
  - AE/SA: no monthly fee "for a limited time", with no end date (direct).
  - SG: a waiver "till December 31, 2025" (snippet).
- **C2. High-volume listing fee.**
  - "a monthly high-volume listing fee of $0.001 per eligible SKU… The high-volume listing fee is waived for the first 1.5 million SKUs." "All SKUs across all product categories, irrespective of creation date or sales history, will be counted towards the fee." It is "applied to your highest number of eligible SKUs from the fifth day through the thirty-first day of the month." [official] G200336920 (snippet).
  - CA: "CAD 0.001 per SKU" over 1.5 million active SKUs (sell.amazon.ca/pricing, direct).
  - It counts SKUs, not ASINs. No change since 2025 was found.

### D. Refund administration fee: the referral fee on a refund

- **D1. US.**
  - "If you refund a customer for an order for which you have already received payment, Amazon will refund you the amount of the referral fee you paid for the item(s), minus the applicable refund administration fee, which is the lesser of $5.00 or 20% of the applicable referral fee." Worked example: a $10.00 item at 15% gives "your refund administration fee will be $0.30". [official] G200336920 (snippet; also listing seat, 2026-10-14).
  - A support mirror instead reads "20% of the original order-related-fees, up to a maximum of $5, for each line item" (non-BMVD) [opinion, mirror of an older Amazon text, https://amzsupport.freshdesk.com/support/solutions/articles/47000984433-refund-credits-and-administration-fees]. The two disagree on the base (referral fee vs all order-related fees). The current Amazon wording read here says the referral fee.
- **D2. By marketplace.**
  - CA: lesser of CAD 5 or 20% (sell.amazon.ca/pricing).
  - UK: lesser of £5 or 20% (sell.amazon.co.uk/pricing).
  - DE: 「5,00 € oder, falls niedriger, 20 % der jeweiligen Verkaufsgebühr」 (€5.00 or, if lower, 20% of the referral fee) (sell.amazon.de/preisgestaltung).
  - FR: 「5,00 € ou 20 % des frais de vente applicables, selon l'éventualité la moins élevée」 (€5.00 or 20% of the referral fee, whichever is lower) (sell.amazon.fr/tarifs).
  - **JP**: 「500円または販売手数料の10%のどちらか金額の小さいほうを返金処理手数料として適用」 (the lower of ¥500 or **10%** of the referral fee is applied as the refund processing fee) (sell.amazon.co.jp/pricing).
  - MX says an administrative cost is charged for refunds, without an amount (vender.amazon.com.mx/precios).
  - Not found on Amazon's AU, BR, IN, AE, SA or SG pages.
  - All read direct.
- **D3. How it shows.**
  - Practitioners describe two lines on the refund: the referral fee credited back (`Commission`, positive), and the retained part (`RefundCommission`). A2X's display name is "Adjustment Item Fees Refund Commission", glossed as "A retained fee Amazon charges to sellers on refunds" [opinion, A2X, https://a2xaccounting.com/blog/list-of-amazon-seller-transactions].
  - AMALYTIX: "First, Amazon credits you the full referral fee," then "the refund administration fee: €5.00 or 20% of the original referral fee, whichever is lower" [opinion, AMALYTIX, https://www.amalytix.com/en/knowledge/controlling/amazon-seller-fees/, updated 2026-10-20].
  - Amazon does not name the line on any page read.
- **D4. Other refund-like debits carry the same pair.** SellingPilot's triples include `A-to-z Guarantee Refund / ItemFees / RefundCommission` and `Chargeback Refund / ItemFees / RefundCommission` [opinion, SellingPilot, https://www.sellingpilot.com/helpcenter/en/report/amazon/]. A2X defines the A-to-z line as "Fee reversal for the original referral fee when an A-to-z Guarantee claim is approved" [opinion, A2X]. No Amazon page read confirms that the administration fee applies on A-to-z and chargeback debits.
- **D5. Since 2025.** No change to the refund administration fee was found in any marketplace. The 2026 US changes to return charges were to the FBA returns-processing fee (sibling seat's) [opinion, sellerboard, 2026-08-25].

### E. Digital services fee (DSF)

- **E1. What it is.**
  - From **2024-10-01**, Amazon replaced the DST costs it had built into fees with "a stand-alone digital services fee". It covers the DSTs of the UK, France, Italy, Spain and Canada.
  - It is charged as a percentage of Selling on Amazon fees (referral, closing, subscription: Amazon's "SOA") and, in stated cases, of FBA fees.
  - It depends on the seller's country of establishment and the store. Example: UK-established sellers pay 2% on SOA and FBA fees (£0.05 on £2.25 of SOA fees).
  - [official] News_Amazon, *Change to digital services tax charges from October 1*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/ed2f04c2-afa0-4bd4-b0fb-08efa212b5a6 (direct).
- **E2. From 2026-03-20** it is based on "the DST rate in the country of sale":
  - UK-established sellers: "3% digital services fee will apply on Selling on Amazon and FBA fees for sales in our France, Italy and Spain stores".
  - IT/ES-established sellers: 3% on SOA and FBA fees for UK and France store sales.
  - Sellers established elsewhere: 3% on SOA fees in IT, ES and FR, and "A 3% fee will also apply on FBA fees for sales in our France store."
  - [official] News_Amazon, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/4fdf2816-9760-45d8-b763-26051640abb9 (direct). The linked help page "2026 digital services fee changes" is a shell. [opinion] Corroborated by ChannelX (Chris Dawson, 2026-02-18) and Threecolts (Gary Neale, 2026-03-02).
- **E3. Canada.** [opinion] Canada rescinded its DST on 2025-06-30 (MediaPost and Reuters coverage). No Amazon statement was found that the Canadian DSF stopped or was refunded. Sellers on the CA forums are still asking. Open.
- **E4. Where it is recorded.**
  - Data Kiosk preview types `DIGITAL_SERVICES_FEE_SOA` ("Digital Services Fees. For details about these fees, refer to … GMVQXVHHG8Q8KN7L") and `DIGITAL_SERVICES_FEE_FBA` (no description in the schema) [command-verified].
  - Amazon's changelog *Data Kiosk economics dataset includes more fee types* added both (https://developer-docs.amazon/sp-api/changelog/update-data-kiosk-economics-dataset-includes-more-fee-types).
  - Settlement/Finances strings `DigitalServicesFee` and `DigitalServicesFeeFBA` are third-party observed (AMALYTIX; xieyi138-star/amazon-settlement-parser).

### F. VAT, GST and consumption tax on Amazon's fees

- **F1. EU/UK.**
  - From **2024-08-01**, Amazon EU S.à r.l. is the invoicing entity.
  - For sellers established in the UK, DE, FR, IT, ES, NL, PL, BE or SE: "local VAT rules apply and VAT will be charged on your Amazon fees", and "you will be invoiced by the AEU branch in your country of establishment".
  - Others are invoiced by the "AEU head office in Luxembourg" with VAT treatment unchanged.
  - [official] News_Amazon, *Update to Amazon UK and EU agreements and VAT treatment* (Seller Forums EU thread fe8e800e…, direct). The post does not describe reverse-charge mechanics.
- **F2. JP: Amazon's page contradicts itself.**
  - 「販売手数料のみが税抜きで計算され、その他のすべての手数料には適用される税金が含まれます。」 (Only the referral fee is calculated excluding tax; all other fees include applicable tax.)
  - 「手数料はすべて税抜き表示…税金が課金されます」 (All fees are shown excluding tax… tax is charged.)
  - The FBA table says 「上記の手数料には10％の消費税が含まれます」 (the fees above include 10% consumption tax).
  - [official] sell.amazon.co.jp/pricing (direct).
- **F3. Other marketplaces.**
  - IN: "We will apply 18% (eighteen percent) GST to all fees displayed above."
  - AE: "We will additionally apply VAT to all fees displayed above."
  - AU: fees "don't include applicable taxes, such as GST".
  - SA's page, as read, says 5% VAT. Saudi VAT is 15%, so this looks like a copy of the AE text; verify before use.
  - All [official], direct.
- **F4. Records.**
  - Product Fees and Data Kiosk carry `TaxAmount` / `taxAmount` beside each fee.
  - `SellerDealPaymentEvent` carries `taxAmount`; `ProductAdsPaymentEvent` carries `baseValue` + `taxValue` [command-verified].
  - The fee **invoice** documents themselves are not reachable through SP-API (section *SP-API faces*, Invoices).

### G. Promotions: coupons, deals, price discounts

- **G1. Coupons, US.**
  - "Coupon fees will change from $0.60 per unit sold to an up-front fee of $5 per coupon plus 2.5% of coupon sales", effective **2025-06-02**. [official] News_Amazon, *Amazon is making it easier to try using deals and coupons…*, https://sellercentral.amazon.com/seller-forums/discussions/t/c71e49a4-8f57-42ea-8d6a-accec5de1ebe (direct).
  - "Any Coupon created after June 2, 2025 will be charged based on the new fee structure." [official, staff reply quoting the help page] https://sellercentral.amazon.com/seller-forums/discussions/t/063ad82b-6d0b-45c4-91e2-1dcc3abe67b4.
  - "These fees are separate from your Coupon budget, which funds customer discounts." [official, staff reply] https://sellercentral.amazon.com/seller-forums/discussions/t/55b241a8-7054-4d56-8ccb-13328559cb7f.
  - From the help page (listing seat, 2026-10-14, *Coupon fees*, GM2HYLSWFBZ267BB): "Coupon fees are based on the final price after that coupon has been redeemed. Multiple promotion fees (like deals and coupons) are charged separately"; "Coupon fees apply to all coupon types (Standard, Subscribe and Save, Reorder and Save)"; fees are not refunded on returns. (Corroboration, 2026-11-10: none of these three found on a public Amazon page. A web search for the first sentence returned no copy. They stay as the listing seat's 2026-10-14 reading.)
  - From the fee summary (listing seat, *2026 US Referral and FBA fee changes summary*, G201411300): "Coupons variable fees will be capped at $2000 per coupon, effective for coupons created on or after November 5, 2025". This pack's routes could not re-read either page. The US cap is corroborated only by practitioners (Novadata, SellerSprite), and one of them (Novadata) also states a fee Amazon had retired.
- **G2. Coupons elsewhere.**
  - UK vouchers: £0.45 per unit became "£2 per voucher plus 1.50% of voucher sales" (2025-06-02) [official] https://sellercentral-europe.amazon.com/seller-forums/discussions/t/16177e61-3737-4e03-b9bb-b0ebe8062436.
  - UK from **2025-11-05**: the variable rate goes "from 1.5% to 0.75%", "Variable voucher fees will be capped at £200 per voucher", for "vouchers created on or after November 5, 2025" [official] https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2f6ff399-f09e-4119-9fcc-cb4e5e36e6f7.
  - EU: €0.50 per redemption before June 2025, confirmed by the reimbursement post https://sellercentral-europe.amazon.com/seller-forums/discussions/t/44048388-fe48-4b93-946e-5d108b1c5e61. [opinion] ChannelX (2025-11-03) reports €2 + 0.50% capped at €100 from 2025-11-05.
  - CA: "variable coupon fees will be capped at CAD 500 per coupon" (News_Amazon, *2026 Updates to Canada referral and Fulfilment by Amazon fees*, https://sellercentral.amazon.ca/seller-forums/discussions/t/a9383e96-87ef-484e-bbe7-cc07584331bb).
  - [opinion] JP: ¥60 per redemption until 2025-06-01, then 「作成したクーポンごとに150円」 (¥150 per coupon created) plus 「クーポンによる売り上げの1.5%」 (1.5% of coupon sales), set by the coupon's start date (ECのミカタ, https://ecnomikata.com/column/47922/).
- **G3. Deals.**
  - US non-peak from 2025-06-02: Best Deal and Lightning Deal fees went from $300/$150 per deal to "$70 each per day plus a variable fee of 1.0% of deal sales with a cap for the variable fee at $2,000 per deal" (c71e49a4).
  - "You will be charged the daily fee even if your Deal does not produce any sales." The variable fee is on the price the customer paid after the deal. Peak events "will be charged a single flat fee, regardless of performance … The rates will vary by event". [official text relayed by a seller from G202111590] https://sellercentral-europe.amazon.com/seller-forums/discussions/t/c1d34a7a-ca34-4f05-9f4a-b9642b1fb75f.
  - **2025 peaks** were flat fees per deal. **Holiday 2026** (Prime Big Deal Days, Black Friday Week, Cyber Monday) for Best Deals, Lightning Deals and Prime Exclusive Price Discounts: "Upfront fee: $100 per promotion, plus Variable fee: 1.5% of promotional sales (capped at $5,000)", the same as Prime Day 2026, with $50 off for early submission. [official] News_Amazon, *Holiday 2026: Same fees, same eligibility, earlier deadlines*, https://sellercentral.amazon.com/seller-forums/discussions/t/3e31fbb7-04e0-4ed4-873e-f74b1052e2ff.
  - UK non-peak from 2025-06-02: "£2.50 each per day" plus 0.75% capped at £400 (16177e61). UK/EU holiday 2026 fees are recorded in the ads playbook (P-seasons-and-deals-53).
  - **Per promotion or per day?** The Promotions API's `FeeFrequency` is `ONE_TIME` or `DAILY` (section *SP-API faces*). The promotion's own `feeSnapshot` is the record.
- **G4. Prime Exclusive (price) discounts.**
  - Prime Day 2025: "$100 flat fee for event merchandising"; "You will not be charged this fee unless you generate at least one sale on a Prime Exclusive Discount SKU." [official] https://sellercentral.amazon.com/seller-forums/discussions/t/da0ba626-01ee-4133-b7a3-f4101bc0ceb0.
  - BFCM 2025 set a different flat fee (https://sellercentral.amazon.com/seller-forums/discussions/t/0b8b8c26-1804-41b5-a61d-4efb6799305f).
  - 2026 peaks: as in G3.
  - No fee on non-event days (listing seat's paraphrase of *Price discount fee*, GVZXV3WZFCBR3VL2, 2026-10-14; the listing file gives it unquoted, so it is not Amazon's wording). The Holiday 2026 post (3e31fbb7) puts Prime Exclusive Price Discounts under event fees, which is consistent with it but does not state the non-event case.
- **G5. "Buy X, Get Y" and monthly promotion billing (2027).**
  - Amazon's 2027 letter names "Buy X, Get Y" promotions among the summary's updates [official] https://sellingpartners.aboutamazon.com/update-to-us-referral-and-fulfillment-by-amazon-fees-for-2027.
  - [opinion] ppc.land (2026-11-06) reports the fee and monthly billing of promotion fees from February 2027. Not confirmed on an Amazon page read.
- **G6. Earlier reimbursements of coupon fees** were paid automatically. "Reimbursements will be automatically disbursed to your Seller Central account by February 28, 2025." [official] https://sellercentral.amazon.com/seller-forums/discussions/t/0492dffc-9521-46e9-9270-1a1e67e6df3a.

### H. Vine, Early Reviewer, Transparency, Brand Registry, Manage Your Experiments

- **H1. Vine.**
  - Fee per parent product by units enrolled; child products carry no extra charge.
  - "You aren't charged until 30 days after enrollment and after your first review is published." "If you don't receive a Vine review within 90 days from the date of enrollment, you aren't charged." [official] *Get customer reviews with Amazon Vine*, https://sell.amazon.com/tools/vine (direct).
  - The help page says the charge comes "seven days after the publication date of the first Vine review" [official] GX3CEV63Y4ZZAP37 (snippet). Amazon's two pages disagree on timing.
  - Tiers for CA, UK, EU and JP are on the same page.
- **H2. Early Reviewer Program.**
  - Retired in spring 2021 [opinion, Modern Retail 2021-03-17; Acadia; eStore Factory].
  - Its event type survives in the model: `SellerReviewEnrollmentPaymentEvent`, "A fee payment event for the Early Reviewer Program" [command-verified, financesV0.json].
- **H3. Transparency.**
  - "no enrollment costs, no subscription costs, and no minimums"; "There's a per-unit cost for Amazon-issued Transparency codes…"; "Fees vary based on volume and geography." The volume resets yearly on the account-creation date. [official] https://sell.amazon.com/brand-registry/transparency (direct).
  - No Finances event names it. [seat] It is likely a `ServiceFeeEvent` or an invoice outside the seller balance; open.
- **H4. Free programs.**
  - "Amazon Brand Registry is a free program" (https://sell.amazon.com/brand-registry).
  - Manage Your Experiments states no fee. It needs a Professional plan and the Brand Representative role (https://sell.amazon.com/tools/manage-your-experiments).
  - Both [official], direct.

### I. Program credits: Brand Referral Bonus, New Seller Incentives, FBA New Selection

- **I1. Brand Referral Bonus.**
  - "a bonus averaging 10% of qualifying sales", varying by category. Bonuses accrue as credits applied against referral fees on future sales, "credited after a waiting period of two months" to allow for returns and cancellations. It needs a Professional plan and Brand Registry. [official] *Brand Referral Bonus*, https://sell.amazon.com/blog/brand-referral-bonus (2023-10-20, direct).
  - No Amazon page read names its Finances or settlement line. Open.
- **I2. New Seller Incentives (US).**
  - "10% back on your first $50,000 in branded sales, then 5% back through your first year until you reach $1,000,000"; "$100 off shipments into the Amazon fulfillment network using the Amazon Partner Carrier program"; "Free storage and customer returns with auto-enrollment in the FBA New Selection program"; "Up to a $1,000 credit to create Sponsored Products ads" [official] https://sell.amazon.com/ (direct).
  - "over $50,000 in automatic referral-fee waivers for your first year" [official] https://sell.amazon.com/pricing.
  - The ads playbook's `areas/launch.md` D1 records the incentives page's Vine credit. No Amazon text read says how these credits post.
- **I3. FBA New Selection program (2026).** [opinion] EcomCrew (Alexa Alix, updated 2026-06-18) and ppc.land (Luís Rijo) describe:
  - branded ASINs launched from 2026-07-30;
  - referral fee capped at 10% for units 1–100 and 5% for units 101–200, "calculated automatically at the point of sale" (ppc.land);
  - $50 coupon-fee and $75 Vine credits within 60 days;
  - a 300 IPI requirement;
  - acceptance of terms by 2026-10-31;
  - no stacking with New Seller Incentives.
  - The Amazon seller-news article returned "Server Busy" (https://sellercentral.amazon.com/seller-news/articles/QVRWUERLSUtYMERFUiNHRDVVS0VERjlHRTlYVk5B). Unconfirmed from Amazon.
- **I4. Other marketplaces.**
  - UK New Seller Incentives: 10% on the first £40,000 of branded sales, then 5% on the next £760,000 (forum snippet).
  - MX: a 90-day 100% referral waiver for new and reactivated sellers enrolling 2026-07-15 to 2026-12-30 (vender.amazon.com.mx/terminos/promocion, direct).

### J. Amazon Business and Handmade

- **J1. Amazon Business.**
  - "Starting October 1, 2025", a bulk-order referral fee discount for business orders, requiring a business price or quantity discount of "3% or more off your standard price". The tiers sit on the help page *Amazon Business bulk order fee discount*, which was not readable. [official] News_Amazon, https://sellercentral.amazon.com/seller-forums/discussions/t/e692b3c2-dfae-45c5-a1f4-80a8283244ab (direct).
  - "For business orders over $1,000 of a single product, you can earn lower referral fee rates", "as low as 5% for the largest orders", FBA and FBM alike [official] https://sell.amazon.com/blog/business-discount-insights (direct).
  - Referral fees on business orders otherwise "follow the Selling on Amazon fee schedule" (listing seat, G201762480).
  - The FBA multi-unit discount is the sibling seat's.
- **J2. Handmade.** Referral "15% or $0.30, whichever is greater"; Professional fee waived after the first month [official] https://sell.amazon.com/programs/handmade (direct). The minimum is $0.30, not $1.
- **J3. Subscribe & Save.** "There are no additional selling costs for the Subscribe & Save program. Participants pay standard selling fees and normal costs for FBA." [official] https://sell.amazon.com/programs/subscribe-and-save (direct). The seller-funded discount lowers the price; it is not a fee. Coupon fees apply to S&S coupons (G1).

### K. Advertising as a charge in finances

- **K1. Payment route.**
  - "By default, your advertising fees are deducted from your selling account balance", with any remainder "charged to the credit card you used to register". Charges appear "in the Selling Fees section of your invoice". [official, older help page quoted by a seller] https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a0cca43ea83a1c90844a62db9c634fb8.
  - [opinion quoting Amazon] ppc.land (2026-04-15) quotes an Amazon Ads notice of 2026-04-14: "we're deferring this change until August 1, 2026"; it "applies only to the small group of advertisers who have been contacted directly". Affected advertisers choose balance deduction or monthly Pay by Invoice.
  - [seat] Where ads are paid by card or invoice, they do not appear in the seller's Finances at all.
- **K2. Model.**
  - `ProductAdsPaymentEvent`, "A Sponsored Products payment event", carries `transactionType` `charge`/`refund`, `invoiceId`, `baseValue`, `taxValue` and `transactionValue` [command-verified]. It is invoice-level, not per ASIN.
  - Per-product ad charges exist only in Data Kiosk `ads[]` (`adTypeName`, e.g. "Sponsored Products charge") and the preview type `SPONSORED_PRODUCTS_CHARGES` [command-verified].
  - Settlement: `ServiceFee / Cost of Advertising / TransactionTotalAmount` [opinion, SellingPilot]. Lingxing matches 「费用类型= Servie Fee，描述=Cost of Advertising，金额 < 0」 (fee type = Service Fee, description = Cost of Advertising, amount < 0; "Servie" is their misspelling) [opinion, Lingxing].

### L. Buy Shipping and FBM label charges

- **L1. Model values.**
  - `AdjustmentType` `PostageBilling`: "The amount paid by a seller for shipping labels". `PostageRefund`: "The reimbursement of shipping labels purchased for orders that were canceled or refunded". [command-verified, financesV0.json]
  - `AdjustmentItem.TransactionNumber` was added 2024-11-06 "to identify what the adjustment is related to", e.g. an Amazon Shipping invoice number [official] SP-API Release Notes (web01/sp-api-release-notes.md).
- **L2. Carrier adjustments.** These are "passed through from carriers … based on differences between the information on the shipping label and the carrier-audited package information"; "prices shown at Buy Shipping label purchase are estimates, and final charges reflect the carrier's actual rates" [official staff replies, snippets].
  - Labels seen: "Shipping label purchase", "Shipping label purchase for return" (SellingPilot), "Carrier Delivery Label Adjustment" (UK forum titles).
  - AMALYTIX observes `PostageBilling_Postage`, `PostageBilling_FuelSurcharge`, `ReturnPostageBilling_*` and `PostageRefund_*` [opinion].
  - Buy Shipping itself carries no fee (https://sell.amazon.com/tools/buy-shipping, direct).

### M. A-to-z, chargebacks, SAFE-T: as charges

- **M1. Debits.**
  - Grant notices read "We have granted an A-to-z Guarantee claim … We have debited the amount from your account" (forum quotes).
  - In the model, `ShipmentEvent` covers "A shipment, refund, guarantee claim, or chargeback"; `GuaranteeClaimEventList` and `ChargebackEventList` hold them; `ItemFeeAdjustmentList` is "only returned for refunds, guarantee claims, and chargeback events" [command-verified].
  - So the fee reversal on these debits sits in the same item-level fee adjustment list as on a refund.
- **M2. SAFE-T.** `SAFETReimbursementEvent` (`SAFETClaimId`, `ReimbursedAmount`, `ReasonCode`) is money in. SAFE-T covers buyer refunds Amazon issued that were debited from the seller; A-to-z orders are excluded (G202188810, snippet). The sibling seat owns it as a refund.

### N. Currency conversion (ACCS)

- **N1. Pricing basis.**
  - "Our volume-based pricing is based on your total cross-currency net proceeds during the past 12 months." Tiers apply by volume. "Sellers who receive funds in AED, CHF, MXN, KRW, and TWD pay a flat rate of 1.5% regardless of tier." "Sellers who receive funds in JPY pay a flat rate of 2.0%." The rate is that of "our third-party service provider on the day the transfer" is initiated. Amazon.com.br is excluded. [official] https://sell.amazon.com/programs/amazon-currency-converter (direct).
  - [seat] The fee is in the converted payout amount, not a line. `FinancialEventGroup.OriginalTotal` vs `ConvertedTotal` brackets it (survey note §2.2). No Amazon page read says where it appears.

### O. Fee-change announcements, by marketplace (dated)

- **US.**
  - 2025: "we will not increase US referral and FBA fees and will not introduce any new fee types" [official] https://sellercentral.amazon.com/seller-forums/discussions/t/a54a4c97-befe-4a60-bcd4-09ee78f5d25d.
  - 2026 (letter 2025-10-15): "FBA fees will increase by an average of $0.08 per unit sold"; "Unless otherwise noted, all changes will be effective January 15, 2026". No referral rate change is named. [official] https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026.
  - 2027 (letter **2026-11-05**): FBA fulfilment fees "will increase by $0.19 per unit sold"; most changes "take effect on January 15, 2027"; the summary covers "Buy X, Get Y" promotions [official] https://sellingpartners.aboutamazon.com/update-to-us-referral-and-fulfillment-by-amazon-fees-for-2027. FBA content: see the ads playbook's goals-and-economics §C.
  - [opinion] ppc.land (2026-11-06) reports "a new, lower referral fee for 3D printers" effective 2026-11-05, and "a promotional referral rate of 10% for Amazon Renewed products" through 2027-10-18. Novadata (2026-11-06): "The announcement does not mention a change to referral fees." sell.amazon.com/pricing, read again on 2026-11-10, shows "3D Printers · 12% for the portion of the total sales price up to $200.00, and · 5% for any portion of the total sales price greater than $200.00", minimum $0.30. The page carries no date, so it does not say when the tier began. Practitioners date it 2026-11-05 (ppc.land) or 2026-10-31 (one other outlet, search summary). [official for the live tier; opinion for its start date]
- **CA.** 2025 and 2026: no referral increases; the 2026 post also caps the coupon variable fee (a9383e96; 2025 post c76ff083-1004-4d74-a00c-8533e426fa54).
- **MX.** From **2026-03-03**, "algunos aumentos de las tarifas por referencia" (some increases to referral fees): Baby and Pets to 15% at any price; Beauty/Health and Grocery to new low-price rates; Industry 12%→14%. From **2026-06-04**, the grocery threshold rises. [official] 2ce2205a; vender.amazon.com.mx/terminos/promocion.
- **BR.** "Consulte comissões atualizadas em 20/01/2025" (see commissions updated 20/01/2025) (venda.amazon.com.br/precos). [opinion] Mercado&Consumo: cuts "até 3%" (up to 3%) in about 17 categories (2025-02-28).
- **EU/UK.**
  - *Update to European referral and FBA fees for 2026* (Dharmesh Mehta, 2025-12-02) [official] aboutamazon.eu:
    - Clothing ≤ £15/€15 and £15–20/€15–20 cut from **2025-12-15**.
    - Home (new category) ≤ £20/€20, Pet Clothing & Food ≤ £10/€10, Grocery and Vitamins/Minerals/Supplements (new category) ≤ £10/€10 cut.
  - The cuts were first set for 2026-02-01 (News_Amazon b3ec0524…; gs.amazon.cn news-notices-251201), then moved to **2026-01-05** (News_Amazon a3b6d192…: "All remaining fee updates announced on December 2 will take effect on February 1, 2026").
  - The UK page also records new referral categories from 2025-10-01.
- **JP.** From **2026-04-01**: 「亚马逊将对所有产品类别中定价高于750日元的商品，提高0.4%的销售佣金率」 (Amazon will raise the referral rate by 0.4 points on items priced above ¥750 in every category). Media and Amazon device and video-game accessories rise 0.4 points at every price. Example: 「一件定价1000日元的电子配件产品将收取10.4%或104日元的佣金（之前为10%或100日元）」 (a ¥1,000 electronics accessory pays 10.4%, ¥104, previously 10%, ¥100). [official] gs.amazon.cn, *2026亚马逊日本站销售佣金与亚马逊物流费用变更* (2026 Amazon Japan referral fee and FBA fee changes), https://gs.amazon.cn/news/news-notices-251202 (2025-12-02, direct). sell.amazon.co.jp's live rates match.
- **AU.** "Starting August 1, 2025, we will adjust some of our fees". The Professional subscription and "most referral fee types" are unchanged (News_Amazon AU thread f3f70d01…). Detail is on an unreadable help page.
- **IN.**
  - "zero referral fees on over 1.2 crore products that are priced below ₹300 across 135+ product categories … from April 7, 2025" [official] aboutamazon.in (2025-03-24).
  - From **2026-03-16**: zero referral below ₹1,000 across "1800+ categories", and "Referral fees reduced by 4%–9.5%" above [official] press.aboutamazon.com/in; sell.amazon.in seller blog. The fee page limits the zero fee to "select categories and for products falling under the Average Selling Price Band of INR 0-500", which contradicts the headline.
  - Closing fees rise on 2026-09-07 (B3). [opinion] Novadata (2026-08-25): a percentage cancellation fee on Easy Ship and Self Ship from 2026-08-17.
- **AE/SA.** KSA: "Starting August 1, 2024 … Referral fees for 14 product categories". No 2025–2026 referral change was found.
- **SG.** "Fee updates: Changes to … referral fees on Amazon Singapore from August 2025" (snippet; rates not visible). The SG pricing page returned 404.

### P. EU and UK extended producer responsibility (EPR): charges Amazon pays on the seller's behalf (gap fill, 2026-11-10)

- **P1. What the service is.** Amazon's environmental-compliance pages for the UK, ES, FR, DE and IT carry the same text (English from sell.amazon.co.uk and sell.amazon.es; FR, DE, IT pages in their own language, same wording):
  - "The EPR Pay on Behalf reports and pays eco-contribution fees for your sales in Amazon stores, where available, and then debits those amounts from your selling account."
  - "Step 1 Automatic enrolment: Amazon automatically enrols you in EPR Pay on Behalf if you sell products subject to EPR obligations and have not submitted a valid EPR Registration Number (ERN)."
  - "Step 3 Eco-contribution payments: EPR Pay on Behalf calculates and pays the eco-contributions for your sales during each reporting period."
  - "Step 4 Charges and invoicing: Amazon invoices you for the use of the service and the eco-contributions paid on your behalf, and debits those fees directly from your Selling Account."
  - "There are two types of fees: Service fee: represents the amount that Amazon charges sellers for the use of the service… Eco-contributions: mandatory fees required by EPR regulations in applicable countries. We pay these fees on your behalf to PROs and then charge them back to you. The fee amounts may vary based on your product categories and sales volume. Visit your EPR Pay on Behalf dashboard for pricing and reporting cycle details."
  - "For a given category Amazon calculates the eco-contributions based on your sales volume or weight, following the rates set by the approved PRO."
  - French name 「Service REP Nous Payons en Votre Nom」 (EPR "We pay in your name" service), which 「enregistre et paie les frais d'écocontribution … puis débite ces montants de votre compte vendeur」 (records and pays the eco-contribution fees … then debits those amounts from your seller account). German: 「EPR – Bezahlung in Ihrem Namen」 (EPR – payment in your name). Italian: 「EPR Pagamento a Tuo Nome」.
  - [official] *Environmental compliance* / *EPR Registration and Filings Services*, https://sell.amazon.co.uk/compliance-solutions/environmental ; https://sell.amazon.es/en/soluciones-cumplimiento/medioambiental ; https://sell.amazon.fr/solutions-conformite/environnement ; https://sell.amazon.de/einhaltungs-losungen/umweltsicherheit ; https://sell.amazon.it/soluzioni-conformita/ambientale (all direct, raw HTML, 2026-11-10; the pages carry no date).
- **P2. Where it applies, by Amazon's own notices.**
  - **France.** "In France, non-compliant listings will be suspended, and we will recover the cost of your eco-contributions." [official] News_Amazon, *Extended Producer Responsibility (EPR): Upload your EPR registration number if you sell in Germany or France* (2021), https://sellercentral-europe.amazon.com/seller-forums/discussions/t/d39fc5dbcb5095d02de209d578585c87 (direct). The UK page adds: "If you sell products on Amazon.fr and don't take the above steps, Amazon will automatically enrol you in the EPR Pay on Behalf service."
    - [opinion, ChannelX quoting Amazon] For 2022 sales Amazon paid "without any additional service fee"; reports go "at the end of the PRO's reporting cycle (which may be quarterly, semi-annual or annual, depending on the PRO and EPR category)"; "Amazon will recover these amounts from your seller account later" (Chris Dawson, 2022-11-30). The service fee started on 2023-03-29, "applicable annually", per EPR category, and "does not include VAT" (ChannelX 2023-03-01 and 2023-06-12, quoting Amazon's notices).
  - **Germany.** "In Germany, if you can't prove your compliance with EPR to Amazon, we will be legally obliged to suspend your non-compliant listings under EPR product categories: Packaging (effective July 1, 2022) and Electric and Electronic Equipment listings (effective January 1, 2023)." The registration number is the "LUCID number for packaging in Germany" (same 2021 post). The 2021 post describes no payment on behalf for Germany. [opinion] A 2026-03-17 AMZ123 article (紫鸟浏览器) lists DE, NL, PL, SE and IE as self-registration countries and BE, ES, IT and FR as countries where Amazon offers 代扣代缴 (pay on behalf).
  - **UK (packaging).** "If you're not established in the UK, Amazon will assume reporting obligations for your sales on Amazon.co.uk in the UK and automatically enrol you in our Pay on Behalf service." "Starting April 1, 2024, Amazon reserves the right to charge you the eco-contributions that we pay." [official] News_Amazon, *Comply with new EPR obligations for packaged goods in the UK*, https://sellercentral.amazon.co.uk/seller-forums/discussions/t/ae4a8fa2-7e21-4585-8878-b1411f668cf4 (direct). From **2025-04-01**: "an annual Extended Producer Responsibility (EPR) Pay on Behalf service fee will apply … in addition to the eco-contribution fees that Amazon pays on behalf of your sales, if you're not established in the UK", "of £20 per EPR category" [official] News_Amazon, *EPR Pay on Behalf service fee for UK packaging starts April 1, 2025*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/9af45752-9777-41f8-8509-b27c39e8fdeb (direct).
  - **Italy.** 「2024/11/15，所有在意大利销售的适用商品必须符合当地生产者责任延伸（EPR）要求。未在规定日期前提供注册号的卖家，将自动加入EPR代付（POB）服务。」 (From 2024-11-15 all applicable products sold in Italy must meet local EPR requirements; sellers who have not provided a registration number by the deadline are automatically enrolled in EPR Pay on Behalf (POB).) [official] gs.amazon.cn, *重要！重要！重要！亚马逊近期政策大汇总！* (Important: summary of recent Amazon policies), https://gs.amazon.cn/news/news-notices-251112 (2025-11-12, direct).
  - **Spain (packaging).** [opinion relaying an Amazon notice, shown as a screenshot] Sellers selling packaged goods on Amazon.es who have not provided a valid ERN by **2024-12-31**, and cannot show they are not the producer, keep selling but are enrolled in EPR Pay on Behalf, and 「亚马逊将根据西班牙第三方卖家延伸生产者责任要求政策中指定的条款和条件，从卖家账户中扣除费用」 (Amazon deducts the fees from the seller's account under the terms of its Spain EPR policy for third-party sellers) (baijing.cn / AMZ123, 2024-03-11). The Amazon notice itself was not found on a public page.
  - **Austria** is named on the UK page among countries with service providers and an EPR education page; no Pay on Behalf text for Austria was found.
- **P3. One policy, reserves and off-cycle charges (from 2025-08-27).** "We're updating our Extended Producer Responsibility (EPR) Pay on Behalf service policy for the UK, Spain and France. Here's what's changing on 27 August 2025: One simple policy… EPR fee reserves: We may hold EPR eco-contribution and service fees in reserve to ensure that we can make timely payments to environmental organisations. Flexible charging: We may charge additional EPR eco-contribution and service fees at times that may differ from the applicable reporting cycle, including additional charges due to regulatory recalculations." [official] News_Amazon, *EPR Pay on Behalf policy update for UK, Spain and France*, https://sellercentral.amazon.co.uk/seller-forums/discussions/t/732822dc-4a85-429e-8d91-ea2ffa32d9e5 (direct). The policy page it links (*EPR Pay on Behalf Service Policy for Third-Party Sellers*) is in Seller Central help and was not read. [opinion] ChannelX (2025-07-29) adds that the charges are eco-contributions plus a service fee "(plus VAT if applicable)", and that enrolment follows if a valid number is not submitted "before the end of the applicable reporting cycle".
- **P4. The account-level reserve (FR, ES, from 2025-11).** 「2025/11月起，部分卖家的法国及西班牙站点EPR代付服务将升级为账户级别预留金机制。简单来说，就是提前在您的账户里"留一笔小金库"，用来按时支付环保款项。此机制不会额外收费，但会影响您的可提现余额」 (From November 2025 some sellers' FR and ES EPR Pay on Behalf service is upgraded to an account-level reserve: in short, a small fund is set aside in your account in advance to pay the environmental fees on time. It charges nothing extra but reduces your withdrawable balance.) 「在此之前，部分卖家的英国站点已经开始此账户级别预留金机制的升级」 (Before this, some sellers' UK accounts had already moved to the same account-level reserve.) [official] gs.amazon.cn news-notices-251112 (2025-11-12, direct).
  - [seat] So an EPR reserve reduces the payable balance without being a cost; the cost is the eco-contribution and service fee when charged. Which line the reserve uses in the settlement or in `listTransactions` is not stated on any page read.
- **P5. What is not stated by Amazon on any page read.** The settlement `amount-description` or `breakdownType` of the EPR charges; whether a charge carries an ASIN or SKU; the reporting cycle per category (Amazon points to the Pay on Behalf dashboard); the current service fee for FR and ES (the 2023 figures are ChannelX's quotes of Amazon).
- **P6. Practitioner labels (not Amazon's).** "EPR fees (EPRChargebackServiceFee, EPRChargebackEcoFee) … We assume that Amazon passes on to you here fees it pays on the seller's behalf. Both lines have shown up in our data since April 2026." [opinion] AMALYTIX (Trutz Fries, updated 2026-10-20), https://www.amalytix.com/en/knowledge/controlling/amazon-seller-fees/. My Real Profit's fee glossary lists "EPR Pay on Behalf service fee (all categories)" and "EPR Pay on Behalf eco-contribution (all categories)", the latter "Currently applies to sales on Amazon.fr, Amazon.es, and Amazon.co.uk", with categories Battery, Chemicals, Construction, DIY, EEE, Furniture, Packaging, Sports, Textile and Toys [opinion] https://intercom.help/myrealprofit/en/articles/14116503.

### Q. Amazon Haul, Amazon Bazaar and "FBA from origin" (gap fill, 2026-11-10)

- **Q1. What Haul is.**
  - "Amazon Haul is a dedicated shopping experience for the Amazon US store that allows customers to shop low-priced, generic fashion, home, and lifestyle products. You can sell your low-priced selection in the product types listed in selection allowed on the Amazon Haul." To create a Haul listing, "ensure that you set the attribute `is_value_store_item` to `true` and `audience` attribute to `BZR`." Not supported for Haul listings: `fulfillment_availability`, `externally_assigned_product_identifier`, `merchant_suggested_asin`. [official] *Manage Amazon Haul, Advanced Multiple-Offer, and Multiple-Fulfillment Use Cases*, https://developer-docs.amazon/sp-api/docs/manage-amazon-haul-advanced-multiple-offer-multiple-fulfillment-use-cases.md (updatedAt 2026-10-28, direct). The guide spells the attribute both `is_value_stores_item` and `is_value_store_item`. [seat] The schema from `getDefinitionsProductType` settles the name.
  - "In 12 months, Haul has expanded from a U.S.- and mobile-only experience into a global ultra-low price shopping destination." "Amazon Haul now serves customers in Australia, France, Germany, Italy, Japan, Spain, and the UK, and through the Amazon Bazaar brand in Mexico, Saudi Arabia, and the United Arab Emirates. We also recently launched a standalone Amazon Bazaar app in 14 locations…" "we're removing the "beta" designation on the experience globally." [official] *Amazon Haul offers over a million items under $10, with many more under $5*, https://www.aboutamazon.com/news/retail/amazon-haul-ultra-low-prices-under-10 (published 2025-11-10, direct).
  - UK: "Amazon Haul launched in the UK on 6 May 2025"; products "for £20 or less, with most of these priced under £10"; "5% off orders over £30 and 10% off orders over £50" (customer discounts). [official] aboutamazon.co.uk, https://www.aboutamazon.co.uk/news/retail/amazon-haul-uk-everything-you-need-to-know (2025-09-12, direct). US launch 2024-11-13 in beta, "all priced $20 and under" (aboutamazon.com, via search summary; the launch article URL tried returned 404).
- **Q2. Haul fees: no Amazon page read gives them.** The Haul selection help page (GAK9UAJGQRN3Y87A) is a shell to a plain GET (tried 2026-11-10). No sell.amazon.com or gs.amazon.cn Haul page was found (sell.amazon.com/programs/amazon-haul, /haul and gs.amazon.cn/haul returned 404). Practitioners disagree on the referral fee (section *What practitioners add*). Amazon's notice text on Haul returns is known only through Chinese media relays: a 15-day return window; items priced at $3 or less not returnable; returned Haul items liquidated, donated or disposed of rather than returned to the seller, with fees charged and liquidation proceeds paid less fees; sellers cannot opt out of refund-without-return [opinion relaying Amazon's seller notice, baijing.cn 2024-11-25; chwang.com 2024-11-15].
- **Q3. Haul money is marked apart in three faces** [official, command-verified]:
  - `listTransactions`: "If a transaction is an Amazon Haul transaction, the value of the `storeName` property in the `listTransactions` response is `AMAZON_HAUL`" (release notes, 2025-06-25). Model: `BusinessContext.storeName`, "The store name associated with the transaction", enum `AMAZON_HAUL` (finances_2024-06-19.json).
  - Sales `getOrderMetrics` `amazonProgram=AmazonHaul`: "`AmazonHaul` returns order metrics for the Amazon Haul program only"; "The Amazon Haul program is only available in the Amazon US store" (sales.json; release notes, 2025-05-28; the note predates Haul's other stores).
  - Orders v2026-01-01 `Order.programs`: "Special programs associated with this order…", values include `AMAZON_BAZAAR` and `AMAZON_HAUL` (orders_2026-01-01.json).
- **Q4. "FBA from origin".**
  - "Starting **6 November 2026**, the `BusinessContext.storeName` field in the Finances API `ListTransactions` operation … will include a new possible value: `AMAZON_FBA_FROM_ORIGIN`, representing FBA from origin transactions." "The new `AMAZON_FBA_FROM_ORIGIN` value will only appear on new FBA from origin transactions." "This change applies to all Amazon stores." [official] changelog *SP-API Updates: New Shipment Notification for Tracking Number Changes in MCF, New EU Customs Product Identifiers Requirement, and New Enum Value for Finances API*, https://developer-docs.amazon/sp-api/changelog/sp-api-updates-new-shipment-notification-for-tracking-number-changes-in-mcf-new-eu-customs-product-identifiers-requirement-and-new-enum-value-for-finances-api.md (direct, 2026-11-10). The model added and then rolled back the value (reconciliation.md P-rec-36; finance-surface.md).
  - No Amazon page read defines "FBA from origin" or gives its fees. Chinese coverage of Amazon's 2025-12 Global Selling summit names 「亚马逊源仓全球履约服务(Fulfill From Origin，FFO)」 (Amazon Fulfill From Origin service): 「卖家只需将商品在货源地仓库入库，即可在亚马逊国际站点上架销售。海外消费者下单后，由亚马逊直接完成全球订单配送」 (the seller only inbounds goods to a warehouse in the source country and can then list them on Amazon's international stores; when an overseas customer orders, Amazon delivers the order directly) and 「已在亚马逊Haul上成功实践，明年将进一步扩展至更多销售目的地国家和地区，并覆盖更多亚马逊Haul之外的商品」 (already run on Amazon Haul; next year it extends to more destination countries and to goods beyond Haul) [opinion, media reports of the summit: AMZ123 https://www.amz123.com/t/3Ctp8WrF (2025-12-09) and /t/TwfZrlQ1 (2025-12-04); 10jqka and yzwb.net (2025-12-05)]. [seat] That `AMAZON_FBA_FROM_ORIGIN` names this service is a reading of the two names, not an Amazon statement.
  - Related but distinct: Global Warehousing & Distribution (GWD) in Shenzhen, from 2026-04-09, stores inventory in China and replenishes the US fulfilment network; "GWD is the first step in our Next Generation of Global Selling vision — where you list once, bring your inventory to the warehouse at origin, and sell it globally from day one." [official] News_Amazon, https://sellercentral.amazon.com/seller-forums/discussions/t/91f2bda1-ff49-456e-9319-9b61058c7c03 (direct). GWD storage is an AWD-family charge (sibling seat).

## The SP-API and report faces

The roles below are from *Role Mappings for SP-API Operations* (web01/role-mappings.md, updatedAt 2026-10-28) and *Role Mappings for SP-API Types* (web01/role-mappings-for-types.md, updatedAt 2026-09-09). Rates are from the models [command-verified]. The roles sellers tick today are Product Listing, Pricing, Brand Analytics and Finance and Accounting, with Amazon Fulfillment being added.

| Read | Path / type | Model | Rate (rps / burst) | Role | Carries |
|---|---|---|---|---|---|
| `listTransactions` | `GET /finances/2024-06-19/transactions` | finances_2024-06-19.json | 0.5 / 10 | Finance and Accounting | Every posted fee as nested `breakdowns` |
| `listSummary` | `GET /finances/2024-06-19/summary` | same | 0.5 / 10 | Finance and Accounting | Period or settlement `breakdowns` of net proceeds |
| `listFinancialEvents`, `…ByGroupId`, `…ByOrderId` | `/finances/v0/...` | financesV0.json | 0.5 / 30 | Finance and Accounting. Also AISP (EU) for `listFinancialEvents` / `ByGroupId`, and Amazon Fulfillment (NA, FE) for `listFinancialEvents`. | Typed event lists (below). Deprecated 2025-07-21; removal **2027-08-27**. |
| Settlement V2 | `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` via `getReports` | Reports | door.md | Finance and Accounting | `transaction-type` / `amount-type` / `amount-description` / `amount`. V1 flat and XML removed **2026-11-11**. |
| `getMyFeesEstimateForSKU`, `…ForASIN` | `POST /products/fees/v0/listings/{SellerSKU}/feesEstimate`, `…/items/{Asin}/feesEstimate` | productFeesV0.json | 1 / 2 | Any of a long list, incl. Finance and Accounting, Pricing, Product Listing, Amazon Fulfillment | Estimated referral, closing, per-item and FBA fees at a given price |
| `getMyFeesEstimates` | `POST /products/fees/v0/feesEstimate` (≤ 20 items) | same | 0.5 / 1 | Pricing or Product Listing | same |
| Fee Preview | `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` | Reports | once per day per seller | Amazon Fulfillment or Pricing | `estimated-referral-fee-per-unit`, `estimated-variable-closing-fee` (US/CA), `estimated-fee-total` |
| Referral Fee Preview | `GET_REFERRAL_FEE_PREVIEW_REPORT` | Reports | — | Finance and Accounting | Per-listing referral estimate at the listed price |
| Data Kiosk economics | `analytics_economics_2024_03_15` (`economics`, `economicsPreview`) | schemas/data-kiosk | `createQuery` 0.0167 / 15; `getQuery` 2 / 15; `getDocument` 0.0167 / 15 | Brand Analytics per Role Mappings (2026-10-28) and the Data Kiosk API page (updatedAt 2026-10-20). Selling Partner Insights per *Correction: Data Kiosk role requirements* (page timestamp 2024-07-02, https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements): "The Vendor Analytics and Sales and Traffic datasets require the Brand Analytics role. The Economics dataset requires the Selling Partner Insights role." Unresolved; the `createQuery` reply settles it. | Per product: `fees[]`, `ads[]`, `netProceeds`; preview of referral, closing, per-item and DSF |
| `searchPromotions`, `getPromotion`, `getSelection` | `GET /promotions/2025-12-01/promotions…` | promotions_2025-12-01.json | 0.1 / 4; 0.1 / 2; 0.1 / 2 | Pricing or Product Listing | `feeSnapshot` of each promotion |
| `GET_COUPON_PERFORMANCE_REPORT` | Reports | schemas/reports/sellerCouponReport.json | — | Brand Analytics | `budget`, `budgetSpent`, `budgetRemaining`, `budgetPercentageUsed` (discounts, not fees) |
| `GET_PROMOTION_PERFORMANCE_REPORT` | Reports | promotionReport.json | — | Brand Analytics or Selling Partner Insights | Promotion sales (not fees) |
| `FEE_PROMOTION` notification | Notifications | FeePromotionNotification.json | — | Finance and Accounting or Product Listing | Fee discounts in force (needs a queue destination) |
| `TRANSACTION_UPDATE` notification | Notifications | TransactionUpdateNotification.json | — | not on the types page read (2026-09-09) | A new posted transaction (needs a destination) |
| Transfers `listPayouts`, `listExpectedPayouts` | `/finances/transfers/2024-06-01/...` | transfers_2024-06-01.json | 0.5 / 10 | Finance and Accounting (NA, EU, FE) | Payout totals. `getPaymentMethods` and `initiatePayout` are EU only (F&A or AISP/PISP). |
| Invoices v2026-06-25 | `getInvoiceHeaders`, `getInvoice` | financesInvoices_2026-06-25.json | not stated | Finance and Accounting (per the *Invoices API* page; these operations are not on Role Mappings, whose `getInvoice` row is the Tax Invoicing (Restricted) Invoices API v2024-06-19) | **"Availability: Vendors only"** (Invoices API page). Not Amazon's fee invoices to sellers. |

### Finances v2024-06-19

- **Fields** [command-verified]:
  - `transactionType`: "**Possible value:** `Shipment`".
  - `description`: "Describes the reasons for the transaction. **Example:** `Order Payment`, `Refund Order`".
  - `breakdowns[]` of `breakdownType` ("The type of charge.") and `breakdownAmount`, nested.
  - `items[]` with `ItemRelatedIdentifier` names `ORDER_ADJUSTMENT_ITEM_ID`, `COUPON_ID`, `REMOVAL_SHIPMENT_ITEM_ID` and `TRANSACTION_ID`.
  - `contexts` (Product, Deferred, Business, TimeRange, Payments, AmazonPay).
  - Amounts are "A signed decimal number".
- **No closed list exists.** "breakdownType is an open-ended string; Amazon does not publish a closed list of values, so integrations should handle unknown values." [official] *Get the latest transactions*, https://developer-docs.amazon/sp-api/docs/get-latest-transactions (snippet).
- **Strings seen.**
  - The model's own sandbox examples use `Sales`, `Product Charges`, `Principle` (sic), `Expenses`, `FBA fees` and `Refunds` [command-verified].
  - Production strings reported by vendors are camel-case: `Sales`/`ProductCharges`/`Base` and `Expenses`/`AmazonFees`/`Commission` [opinion, Trellis, https://gotrellis.com/resources/reports/amazon-financial-transactions-report]; `ProductCharges`, `Tax`, `FBAFees`, `OurPricePrincipal` [opinion, Openbridge, https://docs.openbridge.com/en/articles/14489871-amazon-finance-api-v2].
  - Amazon's guide examples cited in the survey: `CSBAFee`, `MPFRegulatoryFee` → `MarketplaceFacilitatorRegulatoryFee-Principal`, `OurPriceRegulatoryFee`.
  - The sandbox strings and the production strings differ.
- **The `COUPON_ID` item identifier** ties a coupon fee to its coupon. `PROMOTION` fees for deals have no named identifier in the enum [command-verified].
- **Filter (re-checked 2026-11-10).** The release note of 2026-07-29 says `SETTLEMENT_ID` was "Added … for the `relatedIdentifierName` query parameter for the `listTransactions` operation". Amazon added it to the model's filter text on 2026-10-28 (commit df7c6298) and removed it on 2026-10-29 (db2936aa, "SPAPI October Release Finance API Rollback"). The diff restores "`FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID` are the only `relatedIdentifier` with filtering capabilities at the moment" [command-verified, GitHub commit API]. The live reference page (https://developer-docs.amazon/sp-api/reference/listtransactions.md, read 2026-11-10) carries the same two-value text. So `listTransactions` filters by `ORDER_ID` or `FINANCIAL_EVENT_GROUP_ID`. `SETTLEMENT_ID` filters `listSummary` only, and appears in transactions only as a response identifier.
- **Pitfalls Amazon names.**
  - "Financial events might not include orders from the last 48 hours."
  - Windows over 180 days "the response is empty".
  - "this operation can return empty pages".
  - For US MFN orders "do not supply the `marketplaceId` parameter".

### Finances v0: where each selling and program fee lands [command-verified, financesV0.json]

| Fee | v0 location | Model's words |
|---|---|---|
| Referral, closing, per-item, DSF, gift-wrap/shipping chargebacks on an order | `ShipmentEvent.ShipmentItemList[].ItemFeeList[]` (`FeeComponent.FeeType`, `FeeAmount`) | `FeeType`: "The type of fee. For more information about Selling on Amazon fees, see [Selling on Amazon Fee Schedule](…/gp/help/200336920)…" (no enum) |
| The same, reversed or retained on refund, A-to-z or chargeback | `RefundEventList` / `GuaranteeClaimEventList` / `ChargebackEventList` → `ItemFeeAdjustmentList` | "only returned for refunds, guarantee claims, and chargeback events" |
| Shipment-level or order-level fees | `ShipmentFeeList`, `OrderFeeList` (MCF) | "A list of shipment-level fees"; order-level fees "applicable to Multi-Channel Fulfillment orders" |
| Subscription and other account fees | `ServiceFeeEventList` (`FeeReason`, `FeeList`, `FeeDescription`, optional `SellerSKU`/`ASIN`/`FnSKU`) | "A service fee on the seller's account" |
| Coupon fees | `CouponPaymentEventList` (`CouponId`, `SellerCouponDescription`, `ClipOrRedemptionCount`, `FeeComponent`, `ChargeComponent`, `TotalAmount`) | "An event related to coupon payments" |
| Deal fees | `SellerDealPaymentEventList` (`dealId`, `dealDescription`, `eventType` "`SellerDealComplete`", `feeType` "`RunLightningDealFee`", `feeAmount`, `taxAmount`, `totalAmount`) | "An event linked to the payment of a fee related to the specified deal" |
| Ads | `ProductAdsPaymentEventList` | "A Sponsored Products payment event" |
| Early Reviewer (retired) | `SellerReviewEnrollmentPaymentEventList` | "A fee payment event for the Early Reviewer Program" |
| Imaging services | `ImagingServicesFeeEventList` | "A fee event related to Amazon Imaging services" |
| Other support services | `ValueAddedServiceChargeEventList` | `TransactionType` "For example, 'Other Support Service fees'" |
| Fee corrections (credit) | `ChargeRefundEventList` | `ReasonCode` "For example, `SubscriptionFeeCorrection`" |
| Retrocharges | `RetrochargeEventList` | `Retrocharge` / `RetrochargeReversal` (tax) |
| Buy Shipping labels | `AdjustmentEventList` `PostageBilling` / `PostageRefund` | quoted in L1 |
| Card debits for a negative balance | `DebtRecoveryEventList` | `DebtPayment`, `DebtPaymentFailure`, `DebtAdjustment` |
| Affordability promotions (IN) | `AffordabilityExpense(Reversal)EventList` | GST fields |
| Liquidation fee (US) | `FBALiquidationEventList.LiquidationFeeAmount` | sibling seat |
| `ChargeType` values beside fees | `Principal`, `Tax`, `MarketplaceFacilitatorTax-*`, `Discount`, `ShippingCharge`, `Giftwrap`, `RestockingFee`, `PaymentMethodFee` ("collected for certain payment methods in certain marketplaces"), `ExportCharge`, `PointsFee`, `GenericDeduction`… | `ChargeType` **is** enumerated; `FeeType` is **not** |

- **Model vs practice.** The model's own deal label `RunLightningDealFee` is reported as "not seen in the last 12 months". Newer strings `DealParticipationFee`, `DealPerformanceFee`, `CouponParticipationFee`, `CouponPerformanceFee` and `VineFee` are observed instead [opinion, AMALYTIX]. [seat] Under which event list the newer strings arrive in v0 is not documented; the model descriptions predate them.

### Settlement V2 flat file

- **What Amazon says.** `amount-type` and `amount-description` "contain the type of charge or fee you have incurred, and indicates whether different fees are related to a common type" [official] *Settlement Reports*, https://developer-docs.amazon/sp-api/docs/settlement-reports-attributes. Price columns are "condensed into three general purpose columns: amount-type, amount-description, and amount" (report-type-values-settlement, snippet). Amazon lists no values.
- **Selling and program fee strings seen by third parties** (none from an Amazon list):
  - `ItemFees`: `Commission`, `RefundCommission`, `FixedClosingFee`, `VariableClosingFee`, `DigitalServicesFee`, `DigitalServicesFeeFBA`, `GiftwrapCommission`, `ShippingHB`, `ShippingChargeback`, `GiftwrapChargeback`, `SalesTaxServiceFee` / `SalesTaxCollectionFee`, `RenewedProgramFee`, `MarketplaceFacilitatorVAT-Principal`/`-Shipping`. Sources: Webgility, https://helpcenter.webgility.com/en/articles/6257546-amazon-settlement-report-fee-groups-and-fee-names; AMALYTIX; xieyi138-star/amazon-settlement-parser, whose README says Amazon "does not publish" the values and that its lists are "incomplete by construction"; Intentwise.
  - `other-transaction`: `Subscription Fee`, `Shipping label purchase`, `Shipping label purchase for return`, `NonSubscriptionFeeAdj`, `CS_ERROR_ITEMS`, `INCORRECT_FEES_ITEMS`, `INCORRECT_FEES_NON_ITEMIZED`, `LightningDealFee Special`, `Manual Processing Fee`, `Current Reserve Amount`, `Previous Reserve Amount Balance`.
  - Triples: `ServiceFee / Cost of Advertising / TransactionTotalAmount`; `Refund`, `A-to-z Guarantee Refund` and `Chargeback Refund` each with `ItemFees / RefundCommission`; `Order / ItemFees / VariableClosingFee`; `AmazonFees / Coupon Participation Fee / Base fee` (SellingPilot).
  - [opinion] A2X's joined display names, e.g. "Other Transaction Subscription Fee Correction".
- **Not found as settlement strings in any public source:** a Vine, Transparency, Prime Exclusive or refund-admin string by those names.

### Product Fees v0: what the estimate includes and leaves out [command-verified, productFeesV0.json]

- **Inputs:** `MarketplaceId`, `IsAmazonFulfilled`, `PriceToEstimateFees` (`ListingPrice` required, `Shipping`, `Points` — "The Amazon Points program is only available in Japan"), `Identifier` and `OptionalFulfillmentProgram` (`FBA_CORE`, `FBA_SNL`, `FBA_EFN`).
- **No input exists for:** a coupon or promotion, a business order, the seller's plan, or the seller's country of establishment (DSF).
- **Outputs:** `TotalFeesEstimate`, and `FeeDetailList` of `FeeType` (free string), `FeeAmount`, `FeePromotion` ("The promotion amount for a given fee"), `TaxAmount`, `FinalFee`, plus nested `IncludedFeeDetailList`.
- **Caveats:** "The estimated fees returned by this API are not guaranteed. Actual fees can vary." "Search "fees" in Seller Central and consult the store-specific fee schedule for the most up-to-date information." ASIN estimates "use the item's catalog size".
- **Release note 2025-08-27**: "Removed the `itemPrice` field from the `previewContext` attribute" and "Updated the `feeTransactionId` operation's response from `feeTransactionContext` to `transactionContext`". Neither field nor that operation is in the clone's model [command-verified]. Unexplained.
- [seat] By its inputs, an estimate is per unit at one price. Program fees (coupon, deal, Vine), the subscription, the high-volume listing fee, the refund administration fee and advertising cannot be in it. Whether DSF appears as a `FeeType` is open.

### Data Kiosk economics: the selling-fee view [command-verified]

- **Preview types.** `PreviewFeeType` includes `REFERRAL_FEES`, `CLOSING_FEES` ("also know as Variable Closing Fees"), `PER_ITEM_SELLING_FEES` ("also know as Fixed Closing Fee"), `DIGITAL_SERVICES_FEE_SOA`, `DIGITAL_SERVICES_FEE_FBA` and `SPONSORED_PRODUCTS_CHARGES`, beside the FBA types.
- **History.** `economics` reports `fees[]` by `feeTypeName` (e.g. "FBA fulfillment fees") with `aggregatedDetail` (`amount` "calculated by rate card", `promotionAmount`, `taxAmount`, `totalAmount`, `amountPerUnit`, `amountPerUnitDelta`, `quantity`).
  - Ranges spanning "the Amazon fee change date" are split.
  - The supported types are on help page GZ8Y22NL2FSRY8M5 (shell).
- **Lag.** The release note of 2026-09-30 says the dataset gained "deal, coupon, removal, disposal, and fuel fees". The clone's enum has none of them, so the model lags the note.
- **Net proceeds.** `netProceeds` = "sales.netProductSales - sum of fees.charge.totalAmount - sum of ads.charge.totalAmount - (cost …) * sales.netUnitsSold".
- **Retention.** All fields carry `P30D` retention.

### Promotions API v2025-12-01 [command-verified, promotions_2025-12-01.json; *Promotions API* page, web01/api/promotions-api.md]

- **Scope.** Sellers only. Three GET operations; no write is in the model, although the release note says "search, retrieve, and manage".
- **Types.** `PromotionType` is `BASKET_BUILDING`, `DEAL`, `PRICE_DISCOUNT` or `COUPON`. `CouponType` is `STANDARD`, `SUBSCRIBE_AND_SAVE` or `REORDER_REWARDS`.
- **Fee snapshot.** `PromotionRevisionAttributes.feeSnapshot` (`PromotionFeeSnapshot`): "The promotion's fee information (rates and incentive programs) that was locked at the time of promotion creation. You can estimate promotion fees (fee preview) at time t1, while promotion creation can happen at time t2. This object includes the fee information captured at time t2. If empty, it means that no fee information was recorded, which indicates that either a promotion type or a marketplace does not currently support promotion fees."
  - It holds `previewedFeeRates`: `upfrontFee` ("Upfront fee (or a flat fee) for each promotion submitted": `rate`, `frequency` ∈ `ONE_TIME`/`DAILY`) and `variableFee` ("Performance based fee, usually represented as a percentage of promotion sales with a cap amount": `salesPercentage`, `feeCapAmount`).
- **Budget.** A budget is "monetary or unit-based". It funds the discount, not the fee.
- **Cross-reference.** `GET_COUPON_PERFORMANCE_REPORT` and `GET_PROMOTION_PERFORMANCE_REPORT` gained `promotionsApiMappingId` to cross-reference (release notes, 2026-08-26).

### FEE_PROMOTION notification [command-verified, FeePromotionNotification.json]

- The payload carries `FeePromotionType`, `FeePromotionTypeDescription`, `PromotionActiveTimeRange` (`EffectiveFromDate`, `EffectiveThroughDate`), `Identifiers`, and `PromotionInformation[]` (`FeeType`, `FeeDiscountType`, `FeeDiscountValue`, `PriceThreshold`, `FeeDiscountMonetaryAmount`, `FeesEstimate`).
- Roles: Finance and Accounting or Product Listing.
- It needs a subscription with a queue or EventBridge destination, which the box does not have (survey §2.1).

### Roles beyond the four ticked today

- **Selling Partner Insights.** May be needed for the economics dataset (unresolved). It would open per-product fees and ads.
- **AISP / PISP.** Needed for Seller Wallet and EU transfers. They would open the Seller Wallet ledger and payout writes. Not built on.
- **Direct to Consumer Shipping (Restricted).** Needed for Merchant Fulfillment label operations. It would open label purchase. Not needed to read label charges, which are in Finances.

### EPR, Haul and FBA from origin in the faces (gap fill, 2026-11-10)

| Read | Path / type | Model / page | Rate | Role | Carries |
|---|---|---|---|---|---|
| EPR Monthly / Quarterly / Annual Report | `GET_EPR_MONTHLY_REPORTS`, `GET_EPR_QUARTERLY_REPORTS`, `GET_EPR_ANNUAL_REPORTS` via `createReport` | *Regulatory Compliance Reports*, https://developer-docs.amazon/sp-api/docs/report-type-values-regulatory-compliance.md (updatedAt 2026-10-28) | door.md | Product Listing (NA, EU, FE) | "data used to declare EPR compliance to regulatory bodies and pay EPR fees, aggregated by month" (quarter, year). "This report can only be requested." CSV. Columns: `unique_account_identifier`, `report_period_start`/`_end`, `asin`, `amazon_marketplace`, `ship_to_country_code`, `ship_to_country`, item names, `registration_number`, `epr_category`, `epr_subcategory1`–`4`, `gl_product_group_description`, `product_type`, `total_units_sold`, `units_per_asin`, `battery_embedded`, item and package weights and dimensions, `total_reported_weight_kg`, and packaging material weights `paper_kg`, `glass_kg`, `aluminum_kg`, `steel_kg`, `plastic_kg`, `wood_kg`, `other_kg`. **No fee or eco-contribution amount column.** The quarterly and annual entries list no attributes on the page. |
| EPR charges as money | `listTransactions`; settlement V2; v0 events | — | as above | Finance and Accounting | Amazon names no line. Practitioners see `EPRChargebackServiceFee` and `EPRChargebackEcoFee` (AMALYTIX, since 2026-04). Under which v0 event list they arrive is undocumented. |
| Haul and FBA from origin transactions | `listTransactions` → `contexts[]` `BusinessContext.storeName` | finances_2024-06-19.json; changelog 2026-10-21 | 0.5 / 10 | Finance and Accounting | `AMAZON_HAUL` (model and reference); `AMAZON_FBA_FROM_ORIGIN` (changelog only, "Starting 6 November 2026"). "The `BusinessContext` object is an optional element in the response `contexts[]` array, so it only appears for program-specific transactions." |
| Haul sales | `getOrderMetrics?amazonProgram=AmazonHaul` | sales.json | 0.5 / 15 | Product Listing or Inventory and Order Tracking (all regions) | Units, orders, sales for Haul only |
| Haul and Bazaar orders | `searchOrders` / `getOrder` → `Order.programs` | orders_2026-01-01.json | 0.0056 / 20; 0.5 / 30 | any of 12, incl. Finance and Accounting, Pricing, Product Listing, Amazon Fulfillment (finance-surface.md E2) | `AMAZON_HAUL`, `AMAZON_BAZAAR` among the program values |

- [seat] The EPR reports give the per-ASIN units and weights an eco-contribution is computed from; the charge itself is only in the finance data. Joining the two is a per-category, per-period allocation, which is the seller's method.
- The EPR reports need Product Listing, a role sellers tick today. Nothing here needs a role beyond the four ticked and Amazon Fulfillment.

## What practitioners add

- **Tools reconcile against different Amazon sources.** Lingxing's profit report (利润报表) reconciles against the Date Range transaction report, not the settlement file. Its matching rules, verbatim (with the original misspelling "Servie"):
  - 广告费 (ad spend): 「费用类型= Servie Fee，描述=Cost of Advertising，金额 < 0」 (fee type = Service Fee, description = Cost of Advertising, amount < 0)
  - 秒杀费 (Lightning Deal fee): 「费用类型= Lightning Deal Fee」 (fee type = Lightning Deal Fee)
  - 优惠券 (coupons): 「费用类型= Service Fee，描述=以【Coupon Redemption Fee：】开头的」 (fee type = Service Fee, description starting with "Coupon Redemption Fee:")
  - VINE: 「描述= VineFee」 (description = VineFee)
  - 订阅费 (subscription): 「描述= Subscription」 (description = Subscription)
  - 平台费 (platform fee): 「费用类型= Order，列= selling fee」 (fee type = Order, column = selling fee), split FBA/FBM, with refunds 「费用类型= Refund，列= selling fee」 (fee type = Refund, column = selling fee).
  - Adjustments include `CommissionCorrection`, `COMPENSATED_CLAWBACK` and `ReturnPostageBilling_Postage`.
  - Its older multi-platform report defines 平台费 as "Commission on Product+Commission on Shipping" (commission on the product plus commission on shipping).
  - [opinion, Lingxing, *利润报表（新）公式核对* (profit report (new): formula check), https://www.lingxing.com/help/article/Formulacheck]

  [seat] So a tool's coupon rule written against "Coupon Redemption Fee:" misses lines after the 2025-07-15 relabelling, if that relabelling holds.
- **The coupon label changed.** Before 2025-07-15 the line read "Type: Service Fee", "Coupon Redemption Fee: Save $## on …". After, it reads "Type: Amazon Fees", "Coupon Performance Based Fee / Coupon Participation Fee", without the coupon title. [opinion, a seller; a staff reply (Indy_Amazon) did not deny it] https://sellercentral.amazon.com/seller-forums/discussions/t/d6c96093-691c-46ac-a1b1-122720bed3ec.
- **A2X** maps "COMMISSIONS AND SELLING FEES" (order and refund commission) to "Amazon Seller Fees and Charges". It puts "Cost of Advertising" **and "lightning deal fees"** under "AMAZON ADVERTISING", with a separate "SUBSCRIPTION AND SERVICE FEES" category [opinion, A2X, https://support.a2xaccounting.com/en/articles/6008311]. [seat] Where a deal fee is booked (advertising, promotion or selling fee) is a seller's choice, and tools differ.
- **Link My Books** uses 11 buckets ("LMB3: Amazon Seller Fees", "LMB4: Amazon FBA Fees", "LMB6: Amazon Advertising Costs") [opinion, https://help.linkmybooks.com/en/articles/8101365].
- **Sellerboard** calls the retained refund fee "a refund handling fee". Some account-level charges appear "under 'more' on the tiles" [opinion, Sellerboard blog, snippets]. The survey records its claim of "more than a total of 100 other Amazon fees".
- **赛狐 SellFox** claims "解析1000+平台费用" (parses 1,000+ platform fees) (survey §3).
- **Not found:** public fee-mapping documents for Helium 10 Profits, 积加 Gerpgo, 马帮 or 易仓.
- **Fee lists that mix codes and display names.**
  - Gorilla ROI's FEETYPE list includes `Commission`, "Refund Administration Fee", "Coupon redemption fee", "Coupon clip fee", `RunLightningDealFee Principal` / `Tax`, "Review Enrollment Fee", `MFNPostageFee`, `TechnologyFee`, "High-volume listing fee" [opinion, https://help.gorillaroi.com/en/articles/10670078].
  - My Real Profit's glossary (2026-03-18) maps `VineFee` to "Vine Enrollment Fee" [opinion].
  - AMALYTIX: the settlement and SP-API share "technical codes", while the Seller Central transaction view shows plain-language names [opinion].
- **What sellers say they miss or are overcharged on:**
  - **Wrong fee category.** GETIDA: "if you sell an item in the electronics category for 8%… suddenly it was incorrectly categorized within the kitchen category which is 15%… you may be eligible for a category fee reimbursement" [opinion, https://getida.com/quick-guide-to-fba-auditing-reimbursements/]. Sellers on Amazon's EU *Referral Fees Series. Part 1* thread (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/4768ea70-6b3c-47d6-b5f3-8cd9eff300db) report "hundreds of orders where the fees were mischarged", one after a Grocery fee-category move ("from 10.2% to 15.3%") [opinion, sellers]. AMZ123 Q&A gives the Seller Central route 「我的产品未被正确计费」 ("my product was not charged correctly") [opinion, https://www.amz123.com/ask/6PfczLKj].
  - **The refund administration fee** as a cost on every refund. 「亚马逊确实会扣除 20%的佣金…此 20%的佣金被定义为退款管理费」 (Amazon does deduct 20% of the commission… this 20% is defined as the refund administration fee) [opinion, AMZ123, https://www.amz123.com/ask/3qmWu3LE]. A2X and Sellerboard list it as a separate line.
  - **Vine fee charged despite a New Seller Incentives credit** (forum title "I have New Seller Incentives but still being charged the Vine Enrollment Fee") [opinion, seller].
  - **Subscription charged with no listings or in vacation mode** (forum threads) [opinion, sellers].
  - **Canadian DSF still charged after the DST was rescinded** (CA forum questions) [opinion, sellers].
- **Wrong-answer warning.** On an SC-EU thread, a seller's definitions of `amount-description` values came from ChatGPT ("I managed to get this info out of ChatGPT"), https://sellercentral-europe.amazon.com/seller-forums/discussions/t/328bfeed-9007-478e-bea8-20b370db2cde. They are not a source.
- **Novadata.** Its coupon article (2025-12-09) both states a cap and claims the retired $0.60 fee still applies [opinion]. Its fee figures are not relied on here.
- **EPR (gap fill, 2026-11-10).**
  - AMALYTIX names the two settlement lines `EPRChargebackServiceFee` and `EPRChargebackEcoFee`, seen "since April 2026", and books them as fees [opinion]. My Real Profit lists a service fee and an eco-contribution line "(all categories)" [opinion]. No public EPR mapping was found for A2X, Link My Books, Lingxing (its *Formulacheck* page as fetched has no EPR rule, grep 2026-11-10), Sellerboard, 积加 or 赛狐.
  - AVASK (compliance provider) summarises the 2025-08-27 policy: before it, FR and ES "non‑compliant sellers were automatically enrolled and charged a €24.99 annual service fee plus 3% of eco‑contributions, per category"; UK "from 1 Apr 2025, £20 annual fee per EPR category"; after it, the same fees "under unified policy with reserve and flexible billing provisions", and "sellers may see charges applied at different times" [opinion, https://avask.com/amazon-epr-pay%e2%80%91on%e2%80%91behalf-uk-spain-france/].
  - 乐鱼跨境 on AMZ123 (2025-10-14) gives the FR pay-on-behalf cost as 「24.99欧元/年+回收费×1.03」 (€24.99 per year plus the recycling fee × 1.03), says it can come to about four times a provider's cost above 2,500 declared packaging units, and notes 「亚马逊的代扣代缴只是帮卖家完成费用的缴纳，但根据法国合规要求，卖家仍然必须拥有自己的UIN」 (Amazon's pay-on-behalf only pays the fee; French rules still require the seller's own UIN) [opinion, a compliance provider, https://www.amz123.com/t/0IOzrduR].
  - 紫鸟浏览器 on AMZ123 (2026-03-17): for countries with pay on behalf, 「代付费用直接从账户扣除，影响现金流」 (the pay-on-behalf charge is deducted straight from the account and affects cash flow) [opinion, https://www.amz123.com/t/17cuFRau].
  - A 2021 AMZ123 article lists France's EPR streams and their declaration rhythm at the time: packaging and batteries yearly, WEEE twice a year, furniture yearly or quarterly by turnover, textiles yearly [opinion, https://www.amz123.com/t/KJnxHO9J, 2021-12-02; old].
  - Sellers on SC-EU report pay-on-behalf invoices they did not expect: €300 for FR packaging ("the charges for more items are very high from numbers estimated on packaging weight"), and €60 after a single French order on a UK-focused account [opinion, sellers, threads a07edf75 and 1a56b43f]. Staff replies asked for case IDs only.
- **Haul (gap fill, 2026-11-10).**
  - Referral fee reports conflict. chwe.cn (2025-10-23): 「亚马逊Haul尚未公开统一的佣金标准…佣金比例大致在5%-10%之间」 (Haul has published no single referral standard… roughly 5–10%), 10% for low-priced phone accessories, as low as 5% for clothing under $15. A search summary of other Chinese articles says the referral is the same as the main store. [opinion; unconfirmed by Amazon]
  - chwang.com (2024-11-15), relaying the invitation terms: goods ship from Amazon's warehouse in China; white-label only; ≤ 1 lb and ≤ 14×8×5 in; price caps by product type ($7, $10, $14, $20); 「退款的管理费和主站一样，是5美元或者销售佣金的20%」 (the refund administration fee is the same as the main store, $5 or 20% of the referral fee) [opinion].
  - chwe.cn: sellers deliver to Amazon's 东莞 (Dongguan) operations centre; Amazon carries cross-border transport, clearance and last mile; 1–2 week delivery [opinion].
  - Marketplace Pulse (2026-03-05): 3,287 US Haul sellers; about $2 billion annual GMV; 97.5% of sellers averaging under $10 per item are in China or Hong Kong [opinion, Marketplace Pulse data, https://www.marketplacepulse.com/articles/amazon-haul-has-over-3000-sellers].

## Published research

None found. No published study of Amazon selling-fee itemisation, fee-category errors or refund administration costs turned up in this seat's searches. The searches were practitioner-oriented, not a literature search.

## Stable enough for a skill

1. The referral fee is the greater of a category percentage of a total price and a per-item minimum. The total price includes the item price, shipping and gift wrap. The tax treatment of the base and the minimum differ by marketplace (moved to *What cx must read at run time*, correction 1).
2. Category tiers come in two kinds. A whole-price threshold changes the rate on the whole price. A portion-of-price tier charges a second rate only on the part above the line.
3. The fee category is Amazon's assignment and can differ from the store category. A wrong category is disputed per charge in Seller Central.
4. On a refund the referral fee is credited back less the refund administration fee. That fee is the lesser of a fixed amount or a percentage of the referral fee; both differ by marketplace (moved to *What cx must read at run time*, correction 1).
5. The machine names do not match the prose names:
   - `FixedClosingFee` is the Individual per-item fee.
   - `VariableClosingFee` / `CLOSING_FEES` is the media closing fee, even where it is a flat amount.
   - `Commission` is the referral fee.
   - `RefundCommission` is the retained refund administration fee (practitioner reading).
6. The digital services fee is a percentage of Amazon's fees, not of sales. It depends on the seller's establishment and the store, and has been a separate line since 2024-10-01.
7. Coupon and deal fees are separate from the coupon or deal budget that funds the discount. They consist of an upfront part and a variable part, the variable part capped in some stores. The rates locked at creation are in the Promotions API `feeSnapshot`.
8. Advertising appears in Finances only as an invoice-level charge (`ProductAdsPaymentEvent`, settlement "Cost of Advertising") when it is deducted from the balance. Per-product ad charges are only in Data Kiosk economics or the Ads API.
9. Amazon publishes no closed list of fee labels in any face: v0 `FeeType`, v2024-06-19 `breakdownType`, settlement `amount-description`, Product Fees `FeeType`. Labels change over time; deal and coupon labels changed in 2025. Only v0 `ChargeType` is enumerated.
10. A fee estimate (Product Fees, Fee Preview, `economicsPreview`) is per unit at one price. It cannot carry promotion, Vine, subscription, high-volume listing, refund administration or advertising costs.
11. EPR Pay on Behalf (gap fill): where a seller has no valid EPR registration number for an EPR category in a country that has the service, Amazon enrols the seller, pays eco-contributions per reporting period and debits them plus a service fee from the selling account. Since 2025-08-27 (UK, ES, FR) Amazon may hold these fees in reserve and charge outside the reporting cycle. The charge is an account-level debit after the period, not an order line. No fee preview carries it.
12. The EPR reports (`GET_EPR_*`, Product Listing) carry per-ASIN units, categories and material weights, not money.
13. Haul (and Bazaar) money is marked in the finance, sales and orders data (`storeName` `AMAZON_HAUL`; `amazonProgram=AmazonHaul`; `Order.programs`). Amazon publishes no Haul fee schedule on a public page.

## What cx must read at run time

| Figure or state | Where |
|---|---|
| Each charged fee on an order or refund (referral, closing, per-item, DSF, refund admin) | `listTransactions` `breakdowns`, by order (`relatedIdentifierName=ORDER_ID`); v0 `listFinancialEventsByOrderId` `ItemFeeList` / `ItemFeeAdjustmentList` until 2027-08-27; settlement V2 rows |
| Account and program fees (subscription, coupon, deal, Vine, ads, labels, corrections) | `listTransactions` (transactions without an order); v0 `ServiceFeeEventList`, `CouponPaymentEventList`, `SellerDealPaymentEventList`, `ProductAdsPaymentEventList`, `ChargeRefundEventList`, `AdjustmentEventList`; settlement `other-transaction` / `ServiceFee` rows |
| The current label strings in this account | The above, read whole. No list exists. |
| The fee a listing will pay at a price | `getMyFeesEstimateForSKU` / `…ForASIN` / `getMyFeesEstimates`; `GET_REFERRAL_FEE_PREVIEW_REPORT`; `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` |
| A dated future rate | `economicsPreview` (≤ 120 days); the Fee Preview future columns (US/MX) |
| Per-product fees and ads over a period | Data Kiosk `economics` (role permitting) |
| A promotion's fee rates and frequency | `getPromotion` → `feeSnapshot` |
| Fee discounts in force | `FEE_PROMOTION` (only with a destination) |
| Transactions of one settlement | `listTransactions` by `FINANCIAL_EVENT_GROUP_ID` (the filter Amazon documents); `listSummary` by `SETTLEMENT_ID` for the settlement's totals |
| The account's plan, Brand Registry, BRB enrollment, DSF establishment | Not in SP-API. Inferred from what is charged (e.g. `FixedClosingFee` present means the Individual plan) or asked of the seller. |
| Category rates, minimums, refund admin amounts, coupon/deal/Vine/Transparency rates | Amazon's pages (sell.amazon.*, News_Amazon posts) at the date of the charge; never from a skill |
| EPR eco-contribution and service-fee charges, and their labels in this account | `listTransactions` (transactions without an order) and settlement V2 rows; practitioners' labels `EPRChargebackServiceFee` / `EPRChargebackEcoFee` to look for |
| EPR reserve held or released | `listSummary` / settlement reserve rows (`Current Reserve Amount`, `Previous Reserve Amount Balance`); whether EPR has its own reserve line is open |
| Units and weights an EPR charge was computed on | `GET_EPR_MONTHLY_REPORTS` / `_QUARTERLY_` / `_ANNUAL_` (Product Listing) |
| EPR enrolment, categories, reporting cycles, service-fee rates | Seller Central EPR Pay on Behalf dashboard and *Manage your EPR Compliance*; no API |
| Which transactions are Haul or FBA from origin | `listTransactions` `contexts[]` `BusinessContext.storeName`; orders `Order.programs`; Haul sales via `getOrderMetrics?amazonProgram=AmazonHaul` |
| Haul referral, fulfilment and other charges | The posted Haul transactions themselves; no public schedule |
| Tax treatment of the referral base, and the per-item referral minimum (moved from *Stable enough*, correction 1) | The pricing page for the seller's marketplace: *How much does it cost to sell on Amazon?*, https://sell.amazon.com/pricing, or its counterpart in *Pages read*; where the page states it both ways (UK/EU), the posted `Commission` against the order's principal and tax in `listTransactions`. As read 2026-11-09: US excludes Amazon-calculated tax; JP and MX include it; UK and EU pages contradict each other; AU has no minimum. |
| Refund administration fee: fixed amount and percentage (moved from *Stable enough*, correction 1) | *Selling on Amazon fee schedule*, https://sellercentral.amazon.com/gp/help/external/200336920 (US; a shell to a plain GET), or the pricing page for the seller's marketplace in *Pages read*; the amount retained on a refund in `listTransactions`. As read 2026-11-09: 20% in US, CA, UK and EU (DE, FR); 10% in JP. |

## What only Seller Central shows

- **The per-category fee schedule and the Revenue Calculator.**
  - The public calculator (`https://sellercentral.amazon.com/hz/fba/profitabilitycalculator/index?lang=en_US`) loads without sign-in as a JavaScript app. `/revcal` redirects to sign-in.
  - It includes "Referral fees", "FBA fulfillment fees", "FBA inbound placement fees", "Monthly storage fees", "Long-term storage fees" and "Variable closing fees".
  - It excludes "Subscription fees", "Per-item fees", "Removal order fees", "Return processing fees", "Unplanned service fees", "Refund administration fees", "Rental book fees", "High volume listing fees" and "Other less common fees".
  - [official, staff post] Christine_Amazon, *The Revenue Calculator*, https://sellercentral.amazon.ca/seller-forums/discussions/t/debaf0b9-7ad8-4014-beb3-7b9a392fcd21.
  - API reach: Product Fees and `economicsPreview` give per-SKU estimates. No API returns the schedule as a table.
- **Fee Explainer** ("Refund administration", "Subscription", "Referral", "Variable closing", "Fixed closing" explainers) [official] News_Amazon, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/22b77a3b-70b5-4172-b285-a4f95c1081b8. No API.
- **Transaction view and Date Range reports**, with plain-language fee names (AMALYTIX) and the "Shipping Services" filter for labels. API reach: `listTransactions` carries the data, with technical names.
- **Fee invoices / VAT invoices for Amazon's fees.** The Invoices API v2026-06-25 is "Vendors only". [seat] No seller-side API for Amazon's fee invoices was found.
- **Fee-category disputes, Vine enrollment, coupon and deal creation, Brand Referral Bonus enrollment and balance, New Seller Incentives status, the plan switch, and the Amazon Business bulk-discount tiers.**
  - No SP-API operation creates or disputes any of them [command-verified: ops.tsv has no write in Promotions; no fee dispute operation].
  - Promotions are readable (`getPromotion`).
- **The 2027 rate pages** and the help pages behind every fee rule above: readable only in Seller Central, or through the help-hub call this pack does not make.
- **EPR (gap fill).** The EPR Pay on Behalf dashboard (enrolment by country and category, "pricing and reporting cycle details"), the *EPR Pay on Behalf Service Policy for Third-Party Sellers*, *Manage your EPR Compliance* (registration numbers), and the EPR invoices. API reach: the charges in Finances; the units and weights in `GET_EPR_*`; nothing for enrolment, rates or invoices.
- **Haul and FFO (gap fill).** Haul invitation, its selection rules and fee terms (help page GAK9UAJGQRN3Y87A and Seller Central notices), and any FFO enrolment. API reach: listings (`is_value_stores_item`, `audience` `BZR`), orders, sales and transactions are marked; terms are not.

## Facts for human readers only

All figures are dated and for human readers only; a skill reads the live rate.

- **US** (sell.amazon.com/pricing, 2026-11-09):
  - Plans: Individual $0.99 per item; Professional $39.99 per month.
  - Referral minimum: $0.30 in most categories; Fine Art $1.00.
  - Rates and tiers:
    - Amazon Device Accessories 45%.
    - Everything Else 15%.
    - Consumer Electronics and Computers 8%.
    - Clothing: 5% ≤ $15, 10% $15–$20, 17% > $20 (whole price).
    - Beauty/Health and Baby: 8% ≤ $10, 15% above.
    - Grocery: 8% ≤ $15, 15% above.
    - Lawn Mowers: 15% ≤ $500, 8% above.
    - Furniture 15%/10% at $200.
    - Jewelry 20%/5% at $250.
    - Watches 16%/3% at $1,500.
    - Electronics Accessories 15%/8% at $100.
    - Compact Appliances 15%/8% at $300.
    - 3D Printers 12%/5% at $200.
    - Fine Art 20/15/10/5% at $100, $1,000 and $5,000.
    - Pet 15% (veterinary diets 22%).
  - Media closing fee: $1.80.
  - High-volume listing fee: $0.001 per SKU over 1.5M.
  - Refund administration fee: lesser of $5 or 20% of the referral fee.
- **CA:** Individual CAD 1.49; Professional CAD 29.99; minimum CAD 0.40; refund administration fee lesser of CAD 5 or 20%; coupon variable fee capped at CAD 500.
- **MX:** minimum MXN 8.00 (IVA included). From 2026-03-03: Baby and Pets 15%; Beauty/Health 12% ≤ MXN 200; Grocery 12% ≤ MXN 300 (threshold MXN 500 from 2026-06-04).
- **BR:** Individual R$2.00 per item; Professional R$19 per month from the 13th month; minimum R$1 or R$2.
- **UK:** Professional £25 per month (excl. VAT); Individual £0.75; minimum £0.25; refund administration fee lesser of £5 or 20%.
- **EU:**
  - Plans and fees: Professional €39 per month (excl. VAT); Individual €0.99; minimum €0.30; refund administration fee lesser of €5 or 20%; heavy-bulky minimum €20 since 2025-02-01 (snippet).
  - Cuts from 2025-12-15: Clothing 5% ≤ €15/£15 and 10% for €15–20/£15–20.
  - Cuts from 2026-01-05: Home 8% ≤ €20/£20; Pet food/clothing 5% ≤ €10/£10; Grocery and Vitamins 5% ≤ €10/£10.
- **DSF:** 2% (UK-established, from 2024-10-01); 3% on FR/IT/ES (and UK/FR for IT/ES-established sellers) from 2026-03-20.
- **JP:**
  - Plans and fees: Professional ¥4,900 per month (excl. tax); Individual ¥100; minimum ¥30; refund administration fee lesser of ¥500 or 10%.
  - Rates: 8.4% / 10.4% / 12.4% / 15.4% after the +0.4-point change of 2026-04-01; 5% ≤ ¥750.
  - Category closing fee [opinion]: books ¥80; CD/DVD/video ¥140.
- **AU:** Professional A$49.95 per month (excl. GST; "when you have active listings"); Individual A$0.99; no minimum; media closing fee A$1.00.
- **IN:** zero referral below ₹300 (from 2025-04-07) and below ₹1,000 in 1,800+ categories (from 2026-03-16); closing fee from ₹2, +₹1/+₹3 from 2026-09-07; 18% GST on fees.
- **AE/SA:** minimum AED 1 / SAR 1; subscription waived for now.
- **SG:** S$29.95, waived to 2025-12-31 (snippet); minimum S$0.50 [opinion].
- **Coupons:**
  - US: $0.60 per redemption before 2025-06-02; then $5 per coupon + 2.5% of coupon sales; cap $2,000 from 2025-11-05 (listing seat).
  - UK: £0.45 per unit, then £2 + 1.5%, then £2 + 0.75% capped at £200 (from 2025-11-05).
  - EU: €0.50 per redemption, then €2 + 1.0% (implied), then €2 + 0.5% capped at €100 [opinion].
  - JP: ¥60 per redemption, then ¥150 + 1.5% [opinion].
- **Deals:**
  - US non-peak: $300/$150 per deal, then $70 per day + 1% capped at $2,000 (from 2025-06-02).
  - UK non-peak: £50/£25 per deal, then £2.50 per day + 0.75% capped at £400.
  - US 2025 peaks: Best Deal $1,000; Lightning Deal $500; PED $100 (Prime Day, Prime Big Deal Days) and $245 (BFCM).
  - US 2026 peaks: $100 + 1.5% capped at $5,000, with $50 off for early submission.
- **Vine** (per parent): $0 for up to 2 units; $75 for 3–10; $200 for 11–30. CA CAD 100/240; UK £60/£140; EU €70/€170; JP ¥10,000/¥22,000.
- **Transparency:** $0.05 / $0.03 / $0.01 per code by annual volume (1M and 10M breaks).
- **Programs:**
  - Brand Referral Bonus: about 10% on average, credited after two months.
  - New Seller Incentives (US): 10% on the first $50,000 of branded sales, then 5% to $1M; $100 Partner Carrier; up to $1,000 Sponsored Products credit.
  - FBA New Selection 2026 [opinion]: referral 10% (units 1–100) and 5% (101–200); $50 coupon and $75 Vine credits.
  - Handmade: 15% or $0.30 minimum.
  - Amazon Business bulk orders: over $1,000 of one product, down to 5% (from 2025-10-01).
- **ACCS:** under $500k 1.50%; $500k–1M 1.25%; $1M–10M 1.00%; over $10M 0.75%; AED, CHF, MXN, KRW and TWD flat 1.5%; JPY flat 2.0%.
- **EPR Pay on Behalf (gap fill, read 2026-11-10):**
  - UK: £20 per EPR category per year, from 2025-04-01, for sellers not established in the UK, plus eco-contributions [official, News_Amazon 9af45752].
  - FR: €24.99 + 3% of the eco-contributions paid, per EPR category, yearly, excluding VAT, from 2023-03-29; free for 2022 sales, and for 2023 in a category first sold in during 2023 [opinion, ChannelX quoting Amazon, 2023]. FR and ES: same figures in 2025 [opinion, AVASK; 乐鱼跨境 2025-10-14].
  - Eco-contribution rates are the PROs', per category, by units or weight.
- **Haul (gap fill):**
  - Customer price ceilings: US $20 and under; UK £20 or less; CA "for $25 or less" (aboutamazon.ca article title, search result only) [official].
  - Customer side: 15-day returns; items ≤ $3 not returnable [opinion relaying Amazon; matches press reports of the 2024-11-13 US launch].
  - Referral: 5–10% by category and price band, or the main store's rates [opinion, conflicting; chwe.cn 2025-10-23 vs search summaries].
  - Invitation-era price caps by product type: $7, $10, $14, $20 [opinion, chwang.com 2024-11-15].
  - Scale: 3,287 US sellers, about $2B annual GMV [opinion, Marketplace Pulse 2026-03-05].

## Pages read

All read 2026-11-09 unless stated. "(snippet)" means seen only in a search summary.

| Title | URL | Tag |
|---|---|---|
| How much does it cost to sell on Amazon? | https://sell.amazon.com/pricing | official |
| Referral fees (help) | https://sellercentral.amazon.com/gp/help/external/200735910 | official (snippet) |
| Selling on Amazon fee schedule (help) | https://sellercentral.amazon.com/gp/help/external/200336920 | official (snippet; listing seat v119, 2026-10-14) |
| Amazon's Individual vs Professional selling plan | https://sell.amazon.com/blog/amazon-professional-vs-individual-selling-plan | official |
| sell.amazon.ca pricing | https://sell.amazon.ca/pricing?lang=en-CA | official |
| vender.amazon.com.mx precios / términos promoción | https://vender.amazon.com.mx/precios ; https://vender.amazon.com.mx/terminos/promocion | official |
| Novedades sobre las tarifas de venta de México en 2026 | https://sellercentral.amazon.com.mx/seller-forums/discussions/t/2ce2205a-31fe-45b4-9c5b-9b47d039bd28 | official |
| venda.amazon.com.br preços | https://venda.amazon.com.br/precos | official |
| 2025 Updates to US Referral and FBA Fees | https://sellercentral.amazon.com/seller-forums/discussions/t/a54a4c97-befe-4a60-bcd4-09ee78f5d25d | official |
| Update to U.S. Referral and FBA fees for 2026 | https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026 | official |
| Update to US Referral and FBA fees for 2027 | https://sellingpartners.aboutamazon.com/update-to-us-referral-and-fulfillment-by-amazon-fees-for-2027 | official |
| 2026 Updates to Canada referral and FBA fees | https://sellercentral.amazon.ca/seller-forums/discussions/t/a9383e96-87ef-484e-bbe7-cc07584331bb | official |
| sell.amazon.co.uk / .de / .fr pricing | https://sell.amazon.co.uk/pricing ; https://sell.amazon.de/preisgestaltung ; https://sell.amazon.fr/tarifs | official |
| Cost to sell in Europe (Amazon India Global Selling) | https://sell.amazon.in/grow-your-business/amazon-global-selling/cost-to-sell-in-europe | official |
| Referral Fees Series Part 2 (staff) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/e5b39e29-db38-4d08-a887-d62d0699bf48 | official |
| Referral Fees Series. Part 1 (thread) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/4768ea70-6b3c-47d6-b5f3-8cd9eff300db | official post; seller replies opinion |
| Incorrect referral fee review (Roberto_Amazon) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/ff7c3c15-8655-4086-af58-9b726d178e77 | official |
| sell.amazon.co.jp pricing | https://sell.amazon.co.jp/pricing | official |
| 2026亚马逊日本站销售佣金与亚马逊物流费用变更 | https://gs.amazon.cn/news/news-notices-251202 | official |
| sell.amazon.com.au pricing | https://sell.amazon.com.au/pricing | official |
| sell.amazon.ae / .sa pricing | https://sell.amazon.ae/pricing ; https://sell.amazon.sa/pricing | official |
| sell.amazon.in fees and pricing; seller fee change 2026 blog | https://sell.amazon.in/fees-and-pricing | official |
| aboutamazon.in zero referral fee (2025-03-24); press.aboutamazon.com/in (2026-03) | aboutamazon.in; press.aboutamazon.com/in | official |
| Update to European referral and FBA fees for 2026 | aboutamazon.eu (Dharmesh Mehta, 2025-12-02) | official |
| Change to digital services tax charges from October 1 | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/ed2f04c2-afa0-4bd4-b0fb-08efa212b5a6 | official |
| 2026 digital services fee changes (News_Amazon) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/4fdf2816-9760-45d8-b763-26051640abb9 | official |
| Update to Amazon UK and EU agreements and VAT treatment | Seller Forums EU thread fe8e800e… | official |
| Amazon Currency Converter for Sellers | https://sell.amazon.com/programs/amazon-currency-converter | official |
| Amazon is making it easier to try using deals and coupons… (US) | https://sellercentral.amazon.com/seller-forums/discussions/t/c71e49a4-8f57-42ea-8d6a-accec5de1ebe | official |
| Prime Day Prep: Understanding Promotion Fees | https://sellercentral.amazon.ca/seller-forums/discussions/t/05d936ee-b79d-451d-b03c-827df41df300 | official |
| Clarification on Coupon Fee Transition | https://sellercentral.amazon.com/seller-forums/discussions/t/063ad82b-6d0b-45c4-91e2-1dcc3abe67b4 | official (staff reply) |
| Coupon fees separate from budget (staff reply) | https://sellercentral.amazon.com/seller-forums/discussions/t/55b241a8-7054-4d56-8ccb-13328559cb7f | official |
| Coupon fee label change thread | https://sellercentral.amazon.com/seller-forums/discussions/t/d6c96093-691c-46ac-a1b1-122720bed3ec | opinion (seller; staff reply) |
| UK deals and vouchers (2025-06-02) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/16177e61-3737-4e03-b9bb-b0ebe8062436 | official |
| Reduced voucher fees starting November 5, 2025 | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2f6ff399-f09e-4119-9fcc-cb4e5e36e6f7 | official |
| Voucher fee reimbursement (EU/UK 2025) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/44048388-fe48-4b93-946e-5d108b1c5e61 | official |
| Coupon fee reimbursement for new FBA selection (US) | https://sellercentral.amazon.com/seller-forums/discussions/t/0492dffc-9521-46e9-9270-1a1e67e6df3a | official |
| Deal Fees - How did I miss this news? | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/c1d34a7a-ca34-4f05-9f4a-b9642b1fb75f | official text relayed by a seller |
| Holiday 2026: Same fees, same eligibility, earlier deadlines | https://sellercentral.amazon.com/seller-forums/discussions/t/3e31fbb7-04e0-4ed4-873e-f74b1052e2ff | official |
| Submit Prime-Exclusive Price Discounts for Prime Day 2025 | https://sellercentral.amazon.com/seller-forums/discussions/t/da0ba626-01ee-4133-b7a3-f4101bc0ceb0 | official |
| Plan your Black Friday and Cyber Monday deals (2025) | https://sellercentral.amazon.com/seller-forums/discussions/t/0b8b8c26-1804-41b5-a61d-4efb6799305f | official |
| Create deals now for Prime Big Deal Days (2025) | https://sellercentral.amazon.com/seller-forums/discussions/t/f2687fda-9f9f-4e73-a00e-115727a1464e | official |
| Amazon Vine | https://sell.amazon.com/tools/vine | official |
| Amazon Transparency | https://sell.amazon.com/brand-registry/transparency | official |
| Brand Registry; Manage Your Experiments | https://sell.amazon.com/brand-registry ; https://sell.amazon.com/tools/manage-your-experiments | official |
| Brand Referral Bonus | https://sell.amazon.com/blog/brand-referral-bonus | official |
| Sell on Amazon home (New Seller Incentives) | https://sell.amazon.com/ | official |
| Subscribe & Save; Handmade; Buy Shipping | https://sell.amazon.com/programs/subscribe-and-save ; …/programs/handmade ; …/tools/buy-shipping | official |
| Amazon Business bulk order referral fee discount (Oct 1, 2025) | https://sellercentral.amazon.com/seller-forums/discussions/t/e692b3c2-dfae-45c5-a1f4-80a8283244ab | official |
| Business discount insights | https://sell.amazon.com/blog/business-discount-insights | official |
| How do I pay for my ads? (quoted) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a0cca43ea83a1c90844a62db9c634fb8 | official (quoted by seller) |
| The Revenue Calculator (staff) | https://sellercentral.amazon.ca/seller-forums/discussions/t/debaf0b9-7ad8-4014-beb3-7b9a392fcd21 | official |
| Fee Explainer announcement | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/22b77a3b-70b5-4172-b285-a4f95c1081b8 | official |
| Settlement Reports (attributes; report type values) | https://developer-docs.amazon/sp-api/docs/settlement-reports-attributes ; …/report-type-values-settlement | official |
| Get the latest transactions | https://developer-docs.amazon/sp-api/docs/get-latest-transactions | official (snippet) |
| Data Kiosk economics more fee types (changelog) | https://developer-docs.amazon/sp-api/changelog/update-data-kiosk-economics-dataset-includes-more-fee-types | official |
| MWS Finances FeeTypes | https://docs.developer.amazonservices.com/en_CA/finances/Finances_FeeTypes.html | official (snippet; host gone) |
| Finances API; Product Fees API; Promotions API; Invoices API; Role Mappings (ops, types); Release Notes; Deprecations | web01/api/*.md, web01/role-mappings*.md, web01/sp-api-release-notes.md, web01/sp-api-deprecations.md (saved Amazon pages) | official, command-verified |
| Models: financesV0, finances_2024-06-19, financesInvoices_2026-06-25, transfers_2024-06-01, productFeesV0, promotions_2025-12-01, analytics_economics_2024_03_15, FeePromotionNotification, sellerCouponReport | models clone db2936aa | official, command-verified |
| A2X: list of Amazon seller transactions; account mapping | https://a2xaccounting.com/blog/list-of-amazon-seller-transactions ; https://support.a2xaccounting.com/en/articles/6008311 | opinion |
| Webgility fee groups and names | https://helpcenter.webgility.com/en/articles/6257546-amazon-settlement-report-fee-groups-and-fee-names | opinion |
| amazon-settlement-parser (README) | https://github.com/xieyi138-star/amazon-settlement-parser | opinion |
| Intentwise V1→V2 mapping | https://help.intentwise.com/amazon-settlement-report-v1-to-v2-mapping-guide | opinion |
| AMALYTIX Amazon seller fees | https://www.amalytix.com/en/knowledge/controlling/amazon-seller-fees/ | opinion |
| SellingPilot report help | https://www.sellingpilot.com/helpcenter/en/report/amazon/ | opinion |
| Gorilla ROI FEETYPE list | https://help.gorillaroi.com/en/articles/10670078 | opinion |
| My Real Profit fee glossary | https://intercom.help/myrealprofit/en/articles/14116503 | opinion |
| Trellis financial transactions report | https://gotrellis.com/resources/reports/amazon-financial-transactions-report | opinion |
| Openbridge Finance API v2 | https://docs.openbridge.com/en/articles/14489871-amazon-finance-api-v2 | opinion |
| Link My Books mappings | https://help.linkmybooks.com/en/articles/8101365 | opinion |
| Lingxing 利润报表（新）公式核对 (profit report (new): formula check) | https://www.lingxing.com/help/article/Formulacheck | opinion |
| AMZ123 Q&A (refund admin; fee category) | https://www.amz123.com/ask/3qmWu3LE ; https://www.amz123.com/ask/6PfczLKj | opinion |
| GETIDA FBA auditing guide | https://getida.com/quick-guide-to-fba-auditing-reimbursements/ | opinion |
| Refund credits and administration fees (mirror) | https://amzsupport.freshdesk.com/support/solutions/articles/47000984433 | opinion |
| ChannelX coupon fees; DSF | https://channelx.world/2025/11/amazon-to-reduce-coupon-fees-from-wednesday/ | opinion |
| ECのミカタ coupon fees | https://ecnomikata.com/column/47922/ | opinion |
| ppc.land 2027 fees; ads billing; New Selection | https://ppc.land/ | opinion |
| EcomCrew New Selection Program / Prime Day 2026 | ecomcrew.com | opinion |
| Seller Union (2021 subscription quote) | https://seller-union.com/?p=4754 | opinion |
| Novadata coupon cap | https://novadata.io/resources/news/amazon-coupon-fee-cap | opinion (unreliable) |
| Correction: Data Kiosk role requirements (page timestamp 2024-07-02) | https://developer-docs.amazon/sp-api/changelog/correction-data-kiosk-role-requirements | official (verifier, 2026-11-10) |
| Data Kiosk API (updatedAt 2026-10-20) | https://developer-docs.amazon/sp-api/docs/data-kiosk-api.md | official (verifier, 2026-11-10) |
| listTransactions reference | https://developer-docs.amazon/sp-api/reference/listtransactions.md | official (verifier, 2026-11-10) |
| GitHub commits db2936aa (2026-10-29) and df7c6298 (2026-10-28) | https://api.github.com/repos/amzn/selling-partner-api-models/commits/db2936aa19f4b48185173c385c51ab115166f221 | official, command-verified (verifier, 2026-11-10) |
| Environmental compliance / EPR Pay on Behalf (UK, ES, FR, DE, IT) | https://sell.amazon.co.uk/compliance-solutions/environmental ; https://sell.amazon.es/en/soluciones-cumplimiento/medioambiental ; https://sell.amazon.fr/solutions-conformite/environnement ; https://sell.amazon.de/einhaltungs-losungen/umweltsicherheit ; https://sell.amazon.it/soluzioni-conformita/ambientale | official (2026-11-10, raw HTML) |
| EPR: Upload your EPR registration number if you sell in Germany or France (2021) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/d39fc5dbcb5095d02de209d578585c87 | official (2026-11-10) |
| Comply with new EPR obligations for packaged goods in the UK | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/ae4a8fa2-7e21-4585-8878-b1411f668cf4 | official (2026-11-10) |
| EPR Pay on Behalf service fee for UK packaging starts April 1, 2025 | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/9af45752-9777-41f8-8509-b27c39e8fdeb | official (2026-11-10) |
| EPR Pay on Behalf policy update for UK, Spain and France (2025-08-27) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/732822dc-4a85-429e-8d91-ea2ffa32d9e5 | official (2026-11-10) |
| 重要！重要！重要！亚马逊近期政策大汇总！(EPR reserve; IT pay on behalf) | https://gs.amazon.cn/news/news-notices-251112 | official (2026-11-10, re-read) |
| Regulatory Compliance Reports (GET_EPR_*) | https://developer-docs.amazon/sp-api/docs/report-type-values-regulatory-compliance.md | official (updatedAt 2026-10-28; read 2026-11-10) |
| Role Mappings for Types (GET_EPR_*) | web01/role-mappings-for-types.md | official, command-verified |
| Manage Amazon Haul, Advanced Multiple-Offer, and Multiple-Fulfillment Use Cases | https://developer-docs.amazon/sp-api/docs/manage-amazon-haul-advanced-multiple-offer-multiple-fulfillment-use-cases.md | official (updatedAt 2026-10-28; read 2026-11-10) |
| Changelog: New `AMAZON_FBA_FROM_ORIGIN` Enum Value for Finances API | https://developer-docs.amazon/sp-api/changelog/sp-api-updates-new-shipment-notification-for-tracking-number-changes-in-mcf-new-eu-customs-product-identifiers-requirement-and-new-enum-value-for-finances-api.md | official (2026-11-10) |
| Amazon Haul offers over a million items under $10 (2025-11-10) | https://www.aboutamazon.com/news/retail/amazon-haul-ultra-low-prices-under-10 | official (2026-11-10) |
| Amazon Haul: everything you need to know (UK, 2025-09-12) | https://www.aboutamazon.co.uk/news/retail/amazon-haul-uk-everything-you-need-to-know | official (2026-11-10) |
| Introducing Global Warehousing & Distribution (Shenzhen) | https://sellercentral.amazon.com/seller-forums/discussions/t/91f2bda1-ff49-456e-9319-9b61058c7c03 | official (2026-11-10) |
| Models: finances_2024-06-19 (`BusinessContext`), sales (`amazonProgram`), orders_2026-01-01 (`Order.programs`) | models clone db2936aa | official, command-verified (2026-11-10) |
| ChannelX EPR Pay on Behalf (2022-11-30; 2023-03-01; 2023-06-12; 2025-07-29) | https://channelx.world/2022/11/amazon-french-epr-payments-charged-to-you/ ; …/2023/03/new-fee-amazon-epr-pay-on-behalf/ ; …/2023/06/amazon-pay-on-behalf-french-eco-contribution-fees/ ; …/2025/07/amazon-epr-pay-on-behalf-combined-for-uk-spain-and-france/ | opinion (quoting Amazon) |
| AVASK: Amazon streamlines EPR Pay on Behalf policy | https://avask.com/amazon-epr-pay%e2%80%91on%e2%80%91behalf-uk-spain-france/ | opinion |
| AMZ123: 法国EPR合规：亚马逊代扣代缴vs服务商续费 (2025-10-14); 亚马逊欧洲EPR新规4月1日生效 (2026-03-17); 法国EPR品类大全 (2021-12-02) | https://www.amz123.com/t/0IOzrduR ; https://www.amz123.com/t/17cuFRau ; https://www.amz123.com/t/KJnxHO9J | opinion |
| baijing.cn: 西班牙EPR最新政策生效 (2024-03-11); 黑五惨烈，亚马逊低价商城 (2024-11-25) | https://www.baijing.cn/article/47865 ; https://www.baijing.cn/article/50836 | opinion (relaying Amazon notices) |
| SC-EU seller threads on EPR invoices | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a07edf75-aa38-4553-9359-3a3b9cd6b438 ; …/1a56b43f-f1b3-4e3f-9c29-dfef3205ac20 | opinion (sellers) |
| AMALYTIX (EPR lines); My Real Profit glossary (EPR) | as above | opinion (re-read 2026-11-10) |
| chwe.cn Haul 发货/核价/佣金 (2025-10-23); chwang.com 亚马逊低价商城正式上线 (2024-11-15) | https://www.chwe.cn/article/QcDAciMacxR ; https://www.chwang.com/article/185726366482 | opinion |
| Marketplace Pulse: Amazon Haul has over 3,000 sellers (2026-03-05) | https://www.marketplacepulse.com/articles/amazon-haul-has-over-3000-sellers | opinion (vendor data) |
| AMZ123 / 10jqka / yzwb summit coverage (FFO, GWD) | https://www.amz123.com/t/3Ctp8WrF ; https://www.amz123.com/t/TwfZrlQ1 ; https://stock.10jqka.com.cn/20251205/c673008628.shtml ; https://www.yzwb.net/news/ch/202512/t20251205_297291.html | opinion (media) |
| Unreadable or absent (gap fill): Haul help GAK9UAJGQRN3Y87A (shell); sell.amazon.com/programs/amazon-haul, sell.amazon.com/haul, gs.amazon.cn/haul (404); aboutamazon Haul launch URLs tried (404); EPR Pay on Behalf Service Policy (Seller Central help, not tried by the forbidden route) | — | — |
| Unreadable (shell): G200336920, G200735910, G201411300, G202189390, G27951, GMVQXVHHG8Q8KN7L, GX3CEV63Y4ZZAP37, G1701 (EU), FBA New Selection seller-news article ("Server Busy"), sell.amazon.com.sg/pricing (404) | — | — |

## Open questions

For a first run on a real account:

1. Which `breakdownType` strings and nesting does `listTransactions` return for this seller's orders, refunds, coupons, deals, Vine, subscription and ads? Do they match the settlement `amount-description` strings?
2. Is the referral fee (`Commission`) computed on the price before or after a seller coupon or promotion? Compare an order's `Commission` with its `Principal` and `Promotion` lines.
3. EU/UK: is the referral base VAT-inclusive? Compare `Commission` with principal and tax on one EU order.
4. Under which v0 list and which v2024-06-19 transaction do coupon and deal fees arrive today: `CouponPaymentEvent` / `SellerDealPaymentEvent`, or `ServiceFeeEvent` with `CouponParticipationFee`, `DealPerformanceFee` and the like? Is `RunLightningDealFee` still emitted?
5. How do the Brand Referral Bonus credit, New Seller Incentives credits and FBA New Selection referral caps post: a reduced `Commission`, a separate credit line, or a `FeePromotion` on the fee?
6. Where do the Vine and Transparency fees post (`ServiceFeeEvent`?), and with what label?
7. (Settled from Amazon's documents on 2026-11-10: no. The filter was rolled back from the model on 2026-10-29, and the reference page lists only `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`. Still open: whether a settlement's `FINANCIAL_EVENT_GROUP_ID` and its `SETTLEMENT_ID` are the same number; see reconciliation.md.)
8. Does Product Fees return a DSF `FeeType` for a seller established in the UK, IT or ES?
9. Is the subscription charged in a month with no active listings (US)?
10. Is the Canadian DSF still charged after 2025-06-30?
11. Does the Data Kiosk economics query run under the seller's current roles (Brand Analytics), or does it need Selling Partner Insights? Which deal and coupon fee types does it return now (2026-09-30 note)?
12. Does a promotion's `feeSnapshot` show `DAILY` or `ONE_TIME` for each deal type, and does it agree with the posted fee?
13. Does the refund administration fee apply on A-to-z and chargeback debits as on refunds?
14. Is the 2.5% coupon variable fee posted per order or at the coupon's end?
15. (EPR) Which `breakdownType` / `amount-description` strings do EPR charges carry in this account (`EPRChargebackServiceFee`, `EPRChargebackEcoFee`, or others), and in which v0 event list? Do they carry a marketplace, a category, an ASIN or a period?
16. (EPR) Does an EPR reserve show as its own line or inside `Current Reserve Amount`, and does `listSummary` show it?
17. (EPR) Does the eco-contribution charged for a period match the units and weights in `GET_EPR_*` for that period and category? Is VAT charged on the service fee for this seller?
18. (EPR) For which countries and categories is this seller enrolled (only the dashboard says)?
19. (Haul) Does a Haul order post the same fee strings as a main-store order (`Commission`, FBA fees), or Haul-specific ones? At what referral rate?
20. (Haul) Does `storeName` appear on every transaction of a Haul order (charges, refunds, fees) or only on the sale?
21. (FBA from origin) Does any transaction after 2026-11-06 carry `AMAZON_FBA_FROM_ORIGIN`, and which fee strings does it carry?

## Positions

- **P-sell-1.** The referral fee is the greater of the category percentage of the total sales price and the per-item minimum. The total sales price includes the item price, delivery and gift-wrap charges. Source: [official] sell.amazon.com/pricing; *Referral fees* G200735910 (snippet); G200336920 (listing seat).
- **P-sell-2.** The tax treatment of the referral base differs by marketplace. US excludes taxes Amazon calculates. JP includes taxes the buyer paid. MX includes IVA, including in the minimum. UK and EU pages state it both ways, so the base is read from a charged order there. Source: [official] US help (snippet); sell.amazon.co.jp/pricing; vender.amazon.com.mx/precios; sell.amazon.co.uk/pricing, sell.amazon.de, sell.amazon.fr, sell.amazon.in cost-to-sell-in-Europe. Read at run time: Amazon's pricing page for the seller's marketplace, *How much does it cost to sell on Amazon?*, https://sell.amazon.com/pricing, or its counterpart in *Pages read* (e.g. https://sell.amazon.co.jp/pricing, https://vender.amazon.com.mx/precios, https://sell.amazon.co.uk/pricing); where the page states it both ways, the posted `Commission` against the order's principal and tax in `listTransactions`.
- **P-sell-3.** Price-dependent referral rates come in two kinds. A whole-price threshold changes the rate on the whole price when the price crosses the line. A portion-of-price tier charges the second rate only on the part above the line. A price change near a threshold changes the fee differently under each. Source: [official] sell.amazon.com/pricing; sell.amazon.co.uk/pricing; sell.amazon.co.jp/pricing.
- **P-sell-4.** Per-item minimum referral fees differ by marketplace. Media and some grocery categories carry none, and Amazon.com.au states "There is no minimum or maximum referral fee." Source: [official] sell.amazon.com.au/pricing and the pricing pages of the other stores. Read at run time: the minimum for the seller's marketplace and category on Amazon's pricing page, *How much does it cost to sell on Amazon?*, https://sell.amazon.com/pricing, or its counterpart in *Pages read* (e.g. https://sell.amazon.com.au/pricing, https://sell.amazon.ca/pricing?lang=en-CA); a listing's referral fee at a given price in `getMyFeesEstimateForSKU` / `getMyFeesEstimates`.
- **P-sell-5.** The referral fee category is Amazon's assignment and "may not be the same as the category that appears to customers". A seller who believes a wrong fee category was applied can request a review per charge in Seller Central; "only one claim per charge is allowed". Source: [official] sell.amazon.com/pricing (via ads playbook §C); Roberto_Amazon staff post ff7c3c15.
- **P-sell-6.** No Amazon page read states whether the referral fee is computed before or after a seller-funded coupon or promotion; practitioners disagree. The order's own posted `Commission` against its principal and promotion lines is the record. Source: [official] absence across G200735910, sell.amazon.com/pricing; [opinion] A2X vs SellerView.ai.
- **P-sell-7.** On a refund Amazon credits back the referral fee minus a refund administration fee. That fee is the lesser of a fixed amount and a percentage of the referral fee: 20% in the US, CA, UK, DE and FR, and 10% in JP. Source: [official] G200336920 (snippet); sell.amazon.ca, .co.uk, .de, .fr, .co.jp pricing pages. Read at run time: for the seller's marketplace, *Selling on Amazon fee schedule*, https://sellercentral.amazon.com/gp/help/external/200336920 (US; a shell to a plain GET), or the pricing page in *Pages read* (https://sell.amazon.ca/pricing?lang=en-CA, https://sell.amazon.co.uk/pricing, https://sell.amazon.de/preisgestaltung, https://sell.amazon.fr/tarifs, https://sell.amazon.co.jp/pricing); the amount retained on a refund in `listTransactions`.
- **P-sell-8.** Practitioners read the refund as two fee lines: the referral fee credited back (`Commission`) and the retained administration fee (`RefundCommission`, "Adjustment Item Fees Refund Commission"). The same pair appears on A-to-z Guarantee and chargeback debits. Amazon names neither line. Source: [opinion] A2X; AMALYTIX; SellingPilot. [official] v0 `ItemFeeAdjustmentList` is "only returned for refunds, guarantee claims, and chargeback events".
- **P-sell-9.** In Amazon's machine names, `FixedClosingFee` is the Individual-plan per-item fee ("Per-item Selling Fees, also know as Fixed Closing Fee"). The media closing fee is `VariableClosingFee` / `CLOSING_FEES` ("also know as Variable Closing Fees"), even where Amazon now charges it as a flat amount per media item. Source: [official] analytics_economics_2024_03_15.graphql [command-verified]; MWS Finances FeeTypes (snippet); sell.amazon.com/pricing.
- **P-sell-10.** India's "closing fee" is a broad fixed fee by price band and fulfilment channel (FBA, Easy Ship, Self Ship, Seller Flex), not a media fee. It changed on 2026-09-07. Source: [official] sell.amazon.in/fees-and-pricing. Read at run time: the closing-fee bands for each channel on *sell.amazon.in fees and pricing*, https://sell.amazon.in/fees-and-pricing; the closing fee charged on an order in `listTransactions`.
- **P-sell-11.** The Professional subscription is a monthly account fee, not a per-unit fee, and can be prorated on a plan switch. Corrections post as `ChargeRefundEvent` with `ReasonCode` such as `SubscriptionFeeCorrection`. Whether it is charged in a month with no active listings is stated only for AU ("when you have active listings"). Source: [official] sell.amazon.com/pricing; Individual vs Professional blog (2025-10-01); financesV0.json; sell.amazon.com.au/pricing.
- **P-sell-12.** The high-volume listing fee is monthly per SKU above a SKU threshold. It counts all SKUs "irrespective of creation date or sales history", at the month's highest count from day 5 to day 31. Source: [official] G200336920 (snippet); sell.amazon.ca/pricing. Read at run time: the per-SKU rate, the SKU threshold and the counting days for the seller's marketplace on *Selling on Amazon fee schedule*, https://sellercentral.amazon.com/gp/help/external/200336920 (US; a shell to a plain GET), or *sell.amazon.ca pricing*, https://sell.amazon.ca/pricing?lang=en-CA; the fee charged in `listTransactions` (transactions without an order).
- **P-sell-13.** The digital services fee is a percentage of Amazon's Selling on Amazon fees, and in stated cases FBA fees, not of sales. It has been a separate line since 2024-10-01. From 2026-03-20 it is based on the DST rate of the country of sale, and it depends on the seller's country of establishment. Source: [official] News_Amazon ed2f04c2 and 4fdf2816. Read at run time: the rate by country of establishment and store on News_Amazon *2026 digital services fee changes*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/4fdf2816-9760-45d8-b763-26051640abb9; the fee charged per order in `listTransactions`, and per product in Data Kiosk `analytics_economics_2024_03_15` (`DIGITAL_SERVICES_FEE_SOA`, `DIGITAL_SERVICES_FEE_FBA`).
- **P-sell-14.** Amazon's fees carry their own tax, by marketplace. EU-established sellers in the listed countries are invoiced by the AEU branch in their country, with local VAT on fees, since 2024-08-01. India adds 18% GST. AE, AU and JP state their own treatment, and JP's page is internally inconsistent. Tax on each fee is a separate field in Product Fees, Data Kiosk and the deal and ads events. Source: [official] News_Amazon fe8e800e; sell.amazon.in, .ae, .com.au, .co.jp; productFeesV0.json; financesV0.json. Read at run time: the tax on each fee in `TaxAmount` of `getMyFeesEstimateForSKU` / `getMyFeesEstimateForASIN` / `getMyFeesEstimates` and in `taxAmount` of Data Kiosk `analytics_economics_2024_03_15`; the stated treatment on the pricing page for the seller's marketplace in *Pages read* (e.g. https://sell.amazon.in/fees-and-pricing, https://sell.amazon.ae/pricing, https://sell.amazon.com.au/pricing, https://sell.amazon.co.jp/pricing) and, for EU-established sellers, News_Amazon *Update to Amazon UK and EU agreements and VAT treatment* (Seller Forums EU thread fe8e800e…).
- **P-sell-15.** Coupon fees are separate from the coupon budget that funds the customer discount. Since 2025-06-02 (US, UK) they are an upfront fee per coupon plus a percentage of coupon sales. Coupons created from 2025-11-05 carry a capped variable fee in the UK and CA (Amazon's posts) and in the US (Amazon's 2026 summary page as read by the listing seat on 2026-10-14; no public Amazon page re-read here carries it). Which regime applies follows the coupon's creation date. Source: [official] News_Amazon c71e49a4, 2f6ff399, a9383e96; staff replies 063ad82b, 55b241a8; G201411300 (listing seat). Read at run time: the upfront fee, variable percentage and cap locked on each coupon in `getPromotion` `feeSnapshot.previewedFeeRates` (`upfrontFee`, `variableFee.salesPercentage`, `variableFee.feeCapAmount`); the regime for the seller's marketplace on News_Amazon *Amazon is making it easier to try using deals and coupons…* (US), https://sellercentral.amazon.com/seller-forums/discussions/t/c71e49a4-8f57-42ea-8d6a-accec5de1ebe, *Reduced voucher fees starting November 5, 2025* (UK), https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2f6ff399-f09e-4119-9fcc-cb4e5e36e6f7, or *2026 Updates to Canada referral and FBA fees* (CA), https://sellercentral.amazon.ca/seller-forums/discussions/t/a9383e96-87ef-484e-bbe7-cc07584331bb.
- **P-sell-16.** Deal fees since 2025-06-02 (US, UK, non-peak) are a per-day upfront fee plus a capped percentage of deal sales. The daily fee is charged "even if your Deal does not produce any sales". Peak events carry their own announced fee per event. Source: [official] News_Amazon c71e49a4, 16177e61, 3e31fbb7; G202111590 text relayed in c1d34a7a. Read at run time: the fee locked on each deal in `getPromotion` `feeSnapshot.previewedFeeRates` (`upfrontFee` with its `frequency`, `variableFee`); the non-peak fees for the seller's marketplace on News_Amazon *Amazon is making it easier to try using deals and coupons…* (US), https://sellercentral.amazon.com/seller-forums/discussions/t/c71e49a4-8f57-42ea-8d6a-accec5de1ebe, or *UK deals and vouchers (2025-06-02)*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/16177e61-3737-4e03-b9bb-b0ebe8062436, and each peak event's fee in that event's own post (holiday 2026, US: *Holiday 2026: Same fees, same eligibility, earlier deadlines*, https://sellercentral.amazon.com/seller-forums/discussions/t/3e31fbb7-04e0-4ed4-873e-f74b1052e2ff).
- **P-sell-17.** A promotion's fee rates are locked at creation and readable in the Promotions API `getPromotion` `feeSnapshot`: an upfront fee with frequency `ONE_TIME` or `DAILY`, and a variable sales percentage with a cap. An empty snapshot means that promotion type or marketplace records no fee. Roles: Pricing or Product Listing. Source: [official] promotions_2025-12-01.json [command-verified]; Role Mappings.
- **P-sell-18.** Vine is charged per parent product by enrolled units. It is charged only after a first Vine review is published, and not if no review comes within 90 days. Amazon's two pages differ on how long after the first review the charge falls. Source: [official] sell.amazon.com/tools/vine; GX3CEV63Y4ZZAP37 (snippet). Read at run time: the tiers and charging terms for the seller's marketplace on *Amazon Vine*, https://sell.amazon.com/tools/vine; the charge itself in `listTransactions` (transactions without an order).
- **P-sell-19.** Brand Registry and Manage Your Experiments carry no fee. Transparency has no enrolment cost but a per-code charge by annual volume. Source: [official] sell.amazon.com/brand-registry, /tools/manage-your-experiments, /brand-registry/transparency. Read at run time: the Transparency per-code rates by volume and geography on *Amazon Transparency*, https://sell.amazon.com/brand-registry/transparency.
- **P-sell-20.** The Brand Referral Bonus is a credit applied against referral fees on later sales, after a two-month wait. New Seller Incentives give automatic referral-fee waivers and program credits. Their posting line is not documented by Amazon. Source: [official] sell.amazon.com/blog/brand-referral-bonus; sell.amazon.com; sell.amazon.com/pricing. Read at run time: the bonus rate and wait on *Brand Referral Bonus*, https://sell.amazon.com/blog/brand-referral-bonus; the US incentive amounts on *Sell on Amazon home (New Seller Incentives)*, https://sell.amazon.com/, and *How much does it cost to sell on Amazon?*, https://sell.amazon.com/pricing.
- **P-sell-21.** Amazon Business orders pay the normal referral schedule. Since 2025-10-01 (US), high-value business orders with a business discount of at least 3% can qualify for a reduced referral rate. Source: [official] News_Amazon e692b3c2; sell.amazon.com/blog/business-discount-insights; G201762480 (listing seat). Read at run time: the discount threshold and reduced rates on News_Amazon *Amazon Business bulk order referral fee discount (Oct 1, 2025)*, https://sellercentral.amazon.com/seller-forums/discussions/t/e692b3c2-dfae-45c5-a1f4-80a8283244ab, and *Business discount insights*, https://sell.amazon.com/blog/business-discount-insights (US); the tier table itself sits on a help page that was not readable.
- **P-sell-22.** Amazon Handmade's referral fee has its own rate and minimum, and the Professional subscription is waived after the first month. Subscribe & Save adds no selling fee. Its seller-funded discount is a price reduction, and coupon fees apply to S&S coupons. Source: [official] sell.amazon.com/programs/handmade, /programs/subscribe-and-save; Coupon fees GM2HYLSWFBZ267BB (listing seat). Read at run time: the Handmade rate, minimum and subscription waiver on *Subscribe & Save; Handmade; Buy Shipping*, https://sell.amazon.com/programs/handmade (US).
- **P-sell-23.** Advertising reaches the seller's finances only when deducted from the selling balance, the default. It then posts as an invoice-level `ProductAdsPaymentEvent` (`charge`/`refund`, `invoiceId`, base plus tax) or the settlement "Cost of Advertising" line, never per ASIN. Ads paid by card or invoice do not appear there. Source: [official] financesV0.json; quoted help text a0cca43e; [opinion] SellingPilot.
- **P-sell-24.** Buy Shipping label costs post as `PostageBilling` and refunds as `PostageRefund`. Carrier-audited adjustments pass through later, because the label price "is an estimate". Source: [official] financesV0.json; staff replies (snippets).
- **P-sell-25.** v0 places selling fees in `ShipmentEvent` item fee lists. Account and program fees sit in their own lists: `ServiceFeeEventList`, `CouponPaymentEventList`, `SellerDealPaymentEventList`, `ProductAdsPaymentEventList`, `ImagingServicesFeeEventList`, `ValueAddedServiceChargeEventList`, and `ChargeRefundEventList` for corrections. `SellerReviewEnrollmentPaymentEventList` serves the retired Early Reviewer Program. Source: [official] financesV0.json [command-verified].
- **P-sell-26.** In v0 `ChargeType` is an enumerated list, while `FeeType` is a free string pointing to the fee schedule. In v2024-06-19 `breakdownType` is "an open-ended string; Amazon does not publish a closed list". The settlement `amount-description` values are published nowhere. Fee labels are read from the account, and unknown ones are kept, not dropped. Source: [official] financesV0.json; finances_2024-06-19.json; *Get the latest transactions* (snippet); *Settlement Reports* attributes.
- **P-sell-27.** Fee labels change over time without a version change. Practitioners report coupon and deal lines moving to participation and performance-based names (`CouponParticipationFee`, `DealPerformanceFee`, `VineFee`), and the model's `RunLightningDealFee` not seen in a year. Source: [opinion] AMALYTIX; seller thread d6c96093 with staff reply. [official] financesV0.json for the model's value.
- **P-sell-28.** The model's sandbox `breakdownType` strings ("Product Charges", "Principle", "FBA fees") differ from the camel-case strings vendors report from production (`ProductCharges`, `AmazonFees`, `Commission`). Example payloads are not a label source. Source: [official] finances_2024-06-19.json [command-verified]; [opinion] Trellis, Openbridge.
- **P-sell-29.** A fee estimate (Product Fees, Fee Preview, Referral Fee Preview, `economicsPreview`) is per unit at one price. Product Fees takes no coupon, promotion, business or establishment input. Program fees, the subscription, the high-volume listing fee, the refund administration fee and advertising cannot be in it, and Amazon's Revenue Calculator explicitly excludes several of them. Source: [official] productFeesV0.json; Christine_Amazon *The Revenue Calculator*.
- **P-sell-30.** Product Fees estimates "are not guaranteed". An ASIN estimate uses catalog size, while a SKU estimate uses measured size once the item is at Amazon. Source: [official] productFeesV0.json; *Product Fees API* page.
- **P-sell-31.** Data Kiosk economics itemises selling fees per product under Amazon's own type names (`REFERRAL_FEES`, `CLOSING_FEES`, `PER_ITEM_SELLING_FEES`, `DIGITAL_SERVICES_FEE_SOA`/`_FBA`, `SPONSORED_PRODUCTS_CHARGES`). It splits a range at an Amazon fee-change date, and its schema can lag Amazon's release notes on new fee types. Source: [official] analytics_economics_2024_03_15.graphql [command-verified]; SP-API Release Notes 2026-09-30.
- **P-sell-32.** The Invoices API v2026-06-25 is "Vendors only". No SP-API operation returns Amazon's fee invoices to a seller. Source: [official] *Invoices API* page (web01/api/invoice-api.md, updatedAt 2026-09-09).
- **P-sell-33.** The finance reads take Finance and Accounting: `listTransactions`, `listSummary`, v0 events, settlement V2, `GET_REFERRAL_FEE_PREVIEW_REPORT`, Transfers `listPayouts`/`listExpectedPayouts`. Product Fees and `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` accept Pricing. The Promotions API takes Pricing or Product Listing. `GET_COUPON_PERFORMANCE_REPORT` takes Brand Analytics. `GET_PROMOTION_PERFORMANCE_REPORT` takes Brand Analytics or Selling Partner Insights. Source: [official] Role Mappings (2026-10-28); Role Mappings for Types (2026-09-09).
- **P-sell-34.** Dated removals: settlement V1 flat file and XML on 2026-11-11; Finances v0 `listFinancialEvents`, `…ByGroupId` and `…ByOrderId` on 2027-08-27 (deprecated 2025-07-21). Source: [official] SP-API Deprecations (updatedAt 2026-09-09).
- **P-sell-35.** Amazon announces selling-fee changes on dated letters and posts per marketplace, usually effective mid-January (US) and on other dates elsewhere. A fee on a transaction is the rate in force on its date. Source: [official] US 2025/2026/2027 letters; aboutamazon.eu 2026 letter; gs.amazon.cn news-notices-251202; vender.amazon.com.mx 2026 post; aboutamazon.in. Read at run time: the effective date and changes for the seller's marketplace in that year's letter or post (US: *Update to US Referral and FBA fees for 2027*, https://sellingpartners.aboutamazon.com/update-to-us-referral-and-fulfillment-by-amazon-fees-for-2027; the other marketplaces' letters as listed in *Pages read*), and a product's fees across a coming change date in Data Kiosk `analytics_economics_2024_03_15` `economicsPreview`.
- **P-sell-36.** Amazon's 2027 US letter (2026-11-05, Sunny Jain) states FBA, storage and low-inventory changes. It names "Buy X, Get Y" promotions, MCF and AWD among the summary's further updates, and does not mention referral rates. The summary page it links (G201411300) is a JS shell to a plain GET. sell.amazon.com/pricing shows 3D Printers as a portion tier (12% up to $200, 5% above) without a start date. Practitioner reports of a Renewed promotional rate, a "Buy X, Get Y" fee and monthly promotion billing are unconfirmed on Amazon's pages read. Source: [official] 2027 letter (https://sellingpartners.aboutamazon.com/update-to-us-referral-and-fulfillment-by-amazon-fees-for-2027, read word for word 2026-11-10); sell.amazon.com/pricing (2026-11-10); [opinion] ppc.land, Novadata. Read at run time: the 3D Printers tier and any later US referral rate on *How much does it cost to sell on Amazon?*, https://sell.amazon.com/pricing.
- **P-sell-37.** ACCS converts payouts at a volume-tiered fee on trailing-12-month cross-currency net proceeds, with flat rates for some currencies and JPY. The fee is not documented as a separate statement line. Source: [official] sell.amazon.com/programs/amazon-currency-converter. Read at run time: the volume tiers and flat rates on *Amazon Currency Converter for Sellers*, https://sell.amazon.com/programs/amazon-currency-converter.
- **P-sell-38.** A-to-z Guarantee claims and chargebacks are debits recorded as `ShipmentEvent`s in `GuaranteeClaimEventList` and `ChargebackEventList`, with their fee adjustments in the item fee adjustment list. SAFE-T reimbursements are a separate inbound event. Source: [official] financesV0.json [command-verified]; G202188810 (snippet).
- **P-sell-39.** Per-category rate tables, minimums, plan prices and program rates are read from Amazon's pages at the date in question. The Seller Central help pages behind them are not reachable by plain GET; sell.amazon.* pages and News_Amazon posts are. Source: [official] as listed in *Pages read*; [command-verified] fetch attempts. Read at run time: *How much does it cost to sell on Amazon?*, https://sell.amazon.com/pricing, or the pricing page for the seller's marketplace in *Pages read* (e.g. https://sell.amazon.ca/pricing?lang=en-CA, https://sell.amazon.co.uk/pricing, https://sell.amazon.de/preisgestaltung, https://sell.amazon.co.jp/pricing, https://vender.amazon.com.mx/precios); a listing's own fee at a price in `getMyFeesEstimateForSKU` / `getMyFeesEstimates`.
- **P-sell-40.** The Revenue Calculator's public page loads without sign-in. Amazon states it includes referral, FBA fulfilment, inbound placement, storage and variable closing fees, and excludes the subscription, per-item, removal, returns processing, refund administration and high-volume listing fees. Source: [official] Christine_Amazon staff post debaf0b9.
- **P-sell-41.** [seat, enters no skill] Where a deal or coupon fee, the subscription, Vine or the high-volume listing fee is booked (selling fee, marketing, advertising, overhead), and how it is spread over products, is the seller's choice. Tools differ: A2X puts lightning deal fees under advertising.
- **P-sell-42.** EPR Pay on Behalf: a seller who sells EPR-subject products in a country where Amazon offers the service, without a valid EPR registration number for that category, is enrolled automatically. Amazon reports to the PROs, pays the eco-contributions for each reporting period, and debits them plus a service fee from the selling account. Eco-contributions are computed per category from sales volume or weight at the PRO's rates. Source: [official] sell.amazon.co.uk, .es, .fr, .de, .it environmental-compliance pages (2026-11-10); News_Amazon 9af45752.
- **P-sell-43.** By Amazon's notices, Pay on Behalf covers France (eco-contributions recovered since the 2022 rules), UK packaging for sellers not established in the UK (eco-contributions from 2024-04-01; an annual per-category service fee from 2025-04-01), Spain (in the combined 2025 policy) and Italy (automatic enrolment from 2024-11-15). Amazon's notice for Germany states listing suspension for packaging and electrical equipment without a valid registration number (LUCID for packaging), not payment on behalf. Source: [official] News_Amazon d39fc5db (2021), ae4a8fa2, 9af45752, 732822dc; gs.amazon.cn news-notices-251112. [opinion] AMZ123/baijing relay of the Amazon.es notice (ERN deadline 2024-12-31).
- **P-sell-44.** Since 2025-08-27 one Pay on Behalf policy covers the UK, Spain and France. Amazon "may hold EPR eco-contribution and service fees in reserve" and "may charge additional EPR eco-contribution and service fees at times that may differ from the applicable reporting cycle, including additional charges due to regulatory recalculations". From 2025-11 some sellers' FR and ES service runs as an account-level reserve (some UK sellers' earlier), which charges nothing extra but lowers the withdrawable balance. Source: [official] News_Amazon 732822dc; gs.amazon.cn news-notices-251112. Read at run time: the policy for the seller's store on News_Amazon *EPR Pay on Behalf policy update for UK, Spain and France*, https://sellercentral.amazon.co.uk/seller-forums/discussions/t/732822dc-4a85-429e-8d91-ea2ffa32d9e5, and *重要！重要！重要！亚马逊近期政策大汇总！*, https://gs.amazon.cn/news/news-notices-251112; the amount held in the reserve rows of `listSummary` and of the settlement report `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` (whether EPR has its own reserve line is open).
- **P-sell-45.** An EPR charge is an account-level debit for a past reporting period (quarterly, semi-annual or annual by category and PRO), not a line on the order whose sale caused it, and no fee estimate or preview carries it. The service fee is annual per category. Source: [official] sell.amazon.* environmental pages ("for your sales during each reporting period"); News_Amazon 9af45752 ("annual … per EPR category"); [opinion] ChannelX 2022-11-30 and 2023-06-12 quoting Amazon on reporting cycles and later recovery. Read at run time: the UK service fee on News_Amazon *EPR Pay on Behalf service fee for UK packaging starts April 1, 2025*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/9af45752-9777-41f8-8509-b27c39e8fdeb; the reporting cycle by category and PRO no operation or page gives (Amazon points to the Seller Central dashboard), so it stands as read on 2026-11-10, FR (ChannelX quoting Amazon).
- **P-sell-46.** Amazon names no EPR line in any finance face. Practitioners see `EPRChargebackServiceFee` and `EPRChargebackEcoFee` in settlements since April 2026, and list a service-fee line and an eco-contribution line "(all categories)". Source: [opinion] AMALYTIX (updated 2026-10-20); My Real Profit glossary. [official] absence on the sell.amazon.* pages and News_Amazon posts read.
- **P-sell-47.** `GET_EPR_MONTHLY_REPORTS`, `GET_EPR_QUARTERLY_REPORTS` and `GET_EPR_ANNUAL_REPORTS` ("data used to declare EPR compliance to regulatory bodies and pay EPR fees") are request-only CSV reports under the Product Listing role. They carry per-ASIN units, EPR category and subcategories, registration number, ship-to country, item and package weights and packaging material weights, and no fee amount. Source: [official] *Regulatory Compliance Reports* (updatedAt 2026-10-28); Role Mappings for Types.
- **P-sell-48.** Amazon Haul is a separate ultra-low-price shopping experience, with its own listings (`is_value_stores_item` true, offer `audience` `BZR`). It launched in the US in 2024-11 (items $20 and under) and in the UK on 2025-05-06 (£20 or less). By 2025-11 it served 25 locations, as Amazon Bazaar in MX, SA and AE and through a Bazaar app in 14 more, and Amazon removed its "beta" label. Source: [official] Haul listings guide (updatedAt 2026-10-28); aboutamazon.com (2025-11-10); aboutamazon.co.uk (2025-09-12).
- **P-sell-49.** Haul money is marked apart: `listTransactions` `BusinessContext.storeName` `AMAZON_HAUL` (from 2025-06-25; the context "only appears for program-specific transactions"), Sales `getOrderMetrics` `amazonProgram=AmazonHaul` (Product Listing or Inventory and Order Tracking), and Orders v2026-01-01 `Order.programs` `AMAZON_HAUL` / `AMAZON_BAZAAR`. Source: [official] finances_2024-06-19.json, sales.json, orders_2026-01-01.json [command-verified]; release notes 2025-05-28 and 2025-06-25; changelog 2026-10-21.
- **P-sell-50.** No public Amazon page read states Haul's referral or fulfilment fees; practitioners disagree (the main store's rates, or about 5–10% by category and price). Practitioners relaying Amazon's notice report that Haul returns are not sent back to the seller but liquidated, donated or disposed of, with fees, and that the refund administration fee is the main store's. Source: [official] absence (Haul help page a shell; no sell.amazon.* Haul page); [opinion] chwe.cn 2025-10-23; chwang.com 2024-11-15; baijing.cn 2024-11-25. Read at run time: the referral and other fees actually charged on a Haul order, in `listTransactions` transactions whose `BusinessContext.storeName` is `AMAZON_HAUL`; no page gives the schedule.
- **P-sell-51.** Amazon's changelog announces `storeName` `AMAZON_FBA_FROM_ORIGIN` "Starting 6 November 2026", "representing FBA from origin transactions", for "all Amazon stores", only on new such transactions; the model rolled the value back on 2026-10-29. No Amazon page read defines FBA from origin or its fees. Amazon's 2025-12 China summit, as reported, announced Fulfill From Origin (FFO): the seller inbounds at an origin-country warehouse, lists on international stores, and Amazon delivers each order cross-border; it ran first on Haul and widens in 2026. Source: [official] changelog (read 2026-11-10); [opinion] AMZ123 3Ctp8WrF, TwfZrlQ1; 10jqka, yzwb (2025-12-05). That the two names are one service is [seat].
- **P-sell-52.** [seat, enters no skill] Whether EPR eco-contributions are a per-unit product cost (spread by the `GET_EPR_*` units or weights) or a period overhead, whether an EPR reserve is treated as cash held or as cost, and whether Haul and FBA from origin are separate channels for product earnings, are the seller's choices; `storeName`, `Order.programs` and the EPR reports make each choice computable.

## Verification

The verifier checked this file on 2026-11-09/10. Methods:
- plain GET of public pages, with the text extracted and grepped;
- greps and `python3 -I` over the models clone (db2936aa);
- the GitHub commit API (read-only);
- the saved Role Mappings pages.

**What was checked.**
- **Re-read word for word, direct:** sell.amazon.com/pricing (A1, B1, the 3D-printer tier); the pricing pages of AU, CA, UK, DE, FR, JP and MX (A3, A4, C1, D2, F2); the 2027 US letter (O, G5, P-sell-36).
- **Seller Forums staff posts, re-read word for word:**
  - c71e49a4 (coupon and deal fees from 2025-06-02);
  - 3e31fbb7 (Holiday 2026 "Upfront fee: $100 per promotion, plus Variable fee: 1.5% of promotional sales (capped at $5,000)");
  - 2f6ff399 (UK voucher cap);
  - 4fdf2816 and ed2f04c2 (DSF);
  - a9383e96 (CA coupon cap CAD 500; "no increases to Canada referral and Fulfilment by Amazon fees").
- **Against the clone:** every model quote in B1, B2, C1, H2, K2, L1, M1, the v0 table and the Data Kiosk, Product Fees and Promotions sections.
- **Rates:** every rate in the table.
- **Roles:** every role claim, against Role Mappings (operations 2026-10-28; types 2026-09-09).
- **Dates:** release notes (2024-11-06, 2025-08-27, 2025-12-22, 2026-07-29, 2026-08-26, 2026-09-30) and deprecations. Settlement V1 flat file and XML were deprecated 2025-03-17 and are removed 2026-11-11; Finances v0 was deprecated 2025-07-21 and is removed 2027-08-27.

**Changes made** (old → new; why; source):
1. **`SETTLEMENT_ID` filter** (*Finances v2024-06-19* Filter; *What cx must read at run time*; open question 7).
   - Old: "Which holds is a run-time answer."
   - New: settled from Amazon's documents. `SETTLEMENT_ID` was added to the model's filter text in df7c6298 (2026-10-28) and removed in db2936aa (2026-10-29), whose diff is quoted. The live reference page (2026-11-10) lists only `FINANCIAL_EVENT_GROUP_ID` and `ORDER_ID`. `SETTLEMENT_ID` filters `listSummary` only. The run-time row now names `FINANCIAL_EVENT_GROUP_ID` / `listSummary`.
2. **Data Kiosk role** (table).
   - Old: "Selling Partner Insights per Amazon's correction (unresolved; survey §2.6)".
   - New: the correction's exact words, its URL and its page timestamp (2024-07-02, from the page's own metadata). Also the Data Kiosk API page (updatedAt 2026-10-20), which still lists only Brand Analytics, and the Data Kiosk rates.
3. **Invoices v2026-06-25 role.**
   - Old: bare "Finance and Accounting".
   - New: from the Invoices API page. Its operations are not on Role Mappings, whose `getInvoice` row belongs to the Tax Invoicing (Restricted) Invoices API v2024-06-19.
4. **2027 letter** (dated changes; P-sell-36).
   - Old: "states no referral rate change".
   - New: it does not mention referral rates. Its own words name "Buy X, Get Y" promotions, MCF and AWD among the summary's updates, and it links the summary G201411300, which is a shell.
   - The 3D-printer portion tier (12% to $200, 5% above) is confirmed live on sell.amazon.com/pricing, without a start date. The practitioners' 2026-11-05 start, the Renewed 10% rate, the "Buy X, Get Y" fee and monthly promotion billing stay [opinion].
5. **G4.**
   - Old: "No fee on non-event days" given in quotation marks as Amazon's.
   - New: marked as the listing seat's unquoted paraphrase.
6. **G1.** The coupon-fee help quotes are annotated: not corroborated on any public Amazon page found.
7. **P-sell-15.** The US cap is attributed to the listing seat's 2026-10-14 reading of G201411300. The UK and CA caps rest on Amazon posts re-read here.

**Point (c): quotes credited to the listing seat's 2026-10-14 help-hub reads.** All were found verbatim in `cx-listing-playbook` `research/angles/price-position.md` (origin/main). What corroborates each elsewhere:

| Quote (page) | Corroborated elsewhere? |
|---|---|
| Referral base "excluding any taxes calculated…", "greater of…" (G200336920 v119) | Partly. Search snippet of G200735910. sell.amazon.com/pricing gives the total-price basis but not the tax exclusion. |
| Refund administration fee "lesser of $5.00 or 20%" (G200336920) | Yes. Search snippet. The same rule is on the CA, UK, DE and FR pricing pages (direct), and JP gives 10% / ¥500. |
| US coupon cap "$2000 per coupon … on or after November 5, 2025" (G201411300 v47) | Not by Amazon. The UK and CA analogues are Amazon posts. The US figure is backed only by practitioners: SellerSprite, Novadata, repricerexpress. |
| "Coupon fees are based on the final price…", "all coupon types…", not refunded on returns (GM2HYLSWFBZ267BB) | No. |
| Price discount: no fee on non-event days (GVZXV3WZFCBR3VL2) | No. It is a paraphrase. |
| Business orders "follow the Selling on Amazon fee schedule" (G201762480) | Partly. News_Amazon e692b3c2 and sell.amazon.com/blog/business-discount-insights give the reduced-rate exception. |

**Positions checked:** 41.
- Changed: 2 (P-sell-15 attribution; P-sell-36 wording and the 3D-printer fact).
- Made [seat]: 0; P-sell-41 was already [seat].
- Removed: 0.
- No position states a behaviour rule. P-sell-2's "so the base is read from a charged order there" describes where the fact is found, not a step.

**Cross-file consistency.**
- reconciliation.md holds the same `SETTLEMENT_ID` history and is consistent.
- refunds-reimbursements-adjustments.md (open question 5 and line 29) still treats the filter as open. It should be aligned to the rollback.
- product-profit.md (P-prof-12) and method/finance-surface.md (P-api-23) agree on the Data Kiosk role conflict.
- refunds file P-ref-2 adds that the refund administration fee is per refunded line item and that a partial refund returns a proportional referral fee. That is not in this file's D, and does not conflict with it.

**Not verified.**
- Search-snippet quotes from help pages that are JS shells: G200735910, G200336920 high-volume listing fee, GX3CEV63Y4ZZAP37 Vine timing, G202188810.
- The 2023-01-13 referral-dispute policy.
- AU 2025-08-01 detail.
- SG changes.
- EU coupon €2 + 0.50% (practitioner).
- The FBA New Selection 2026 terms (the seller-news article is still unreachable).
- The SA 5% VAT line (F3), which looks like a copy of the AE text.

**Gaps a long-time operator would name.**
- How the Brand Referral Bonus and New Seller Incentives post as money lines.
- The Vine and Transparency posting labels.
- Whether the referral fee is computed after a seller coupon. Only an order's own lines answer it.
- The Canadian DSF after the DST repeal.
- The refund administration fee on partial refunds (see the refunds file).
- The 2027 US summary itself, behind a shell page.
- EU/UK and JP 2027 letters, not yet found.

**Gap fill (2026-11-10).** Two completeness critics named EPR charges and Haul / FBA from origin as missing. The file had no word on either, so nothing was skipped. Added:
- *What this covers*: two scope lines and eight dated bullets (2025-01 ES to 2026-11-06).
- *Amazon's own rules*: **P** (EPR Pay on Behalf: what it is, country by country, the 2025-08-27 single policy with reserves and off-cycle charges, the 2025-11 FR/ES account-level reserve, what Amazon does not state, practitioner labels) and **Q** (Haul and Bazaar, the absence of a public Haul fee schedule, the three faces that mark Haul money, FBA from origin / FFO, GWD as distinct).
- *SP-API faces*: a subsection with `GET_EPR_*` (Product Listing; columns; no money column), EPR charges in Finances, `storeName`, `amazonProgram`, `Order.programs`.
- *What practitioners add*: EPR (AMALYTIX, My Real Profit, AVASK, ChannelX, 乐鱼跨境, 紫鸟, sellers' invoices) and Haul (chwe.cn, chwang.com, Marketplace Pulse).
- *Stable enough* 11–13; seven run-time rows; two *Seller Central only* items; EPR and Haul figures under *Facts for human readers only*; 24 page rows; open questions 15–21.
- Positions **P-sell-42 to P-sell-52** (P-sell-52 is [seat]).
- Methods: plain GET with curl of every page quoted, text extracted with `python3 -I`; greps over the models clone (db2936aa) and `web01/role-mappings*.md`. No Amazon API host, no help-hub call.

**Gaps left (gap fill, 2026-11-10).**
- Amazon's own name for EPR charges in `listTransactions`, settlement or v0, and for an EPR reserve: no Amazon page found; only practitioner labels.
- The *EPR Pay on Behalf Service Policy for Third-Party Sellers* and the EPR help pages: Seller Central help only, not read.
- The current FR and ES service fee from an Amazon page: only ChannelX's 2023 quotes and AVASK / AMZ123 (2025).
- The Amazon.es packaging Pay on Behalf notice itself: known only through a Chinese media relay of a screenshot.
- Whether Italy and Austria Pay on Behalf charges post the same way: no source.
- Haul referral, fulfilment and storage fees from Amazon: no public Amazon page (help page a shell, program pages 404); practitioners conflict.
- What "FBA from origin" is and what it charges, in Amazon's words: none. The FFO link is media-reported and [seat]-inferred.
- No EPR or Haul mapping found in A2X, Link My Books, Lingxing, Sellerboard, 积加 or 赛狐 public pages.

**Correction 1 (2026-11-10).** Under brief 306 correction 1 and the plugin zen's item 4, a value that differs by marketplace or changes by year is looked up, not carried.
- **Positions changed** (each kept its value as evidence, and gained one closing sentence that begins "Read at run time:"): P-sell-2, P-sell-4, P-sell-7, P-sell-10, P-sell-12, P-sell-13, P-sell-14, P-sell-15, P-sell-16, P-sell-18, P-sell-19, P-sell-20, P-sell-21, P-sell-22, P-sell-35, P-sell-36, P-sell-37, P-sell-39, P-sell-44, P-sell-45, P-sell-50. No other wording changed. Nothing renumbered or removed.
- **Value no operation or page gives:** the EPR reporting cycle by category and PRO (P-sell-45). It stands as read on 2026-11-10, FR (ChannelX quoting Amazon). Amazon points to the Seller Central Pay on Behalf dashboard.
- **Left as they were:**
  - Rules, faces and labels: P-sell-1, 3, 5, 6, 8, 9, 11, 17, 23–33, 38, 40, 42, 46, 47 and 49.
  - Facts of history: P-sell-34, 43, 48 and 51.
  - [seat] positions: P-sell-41 and 52.
- **Stable enough for a skill.** Items 1 (the referral base's tax treatment by marketplace, and AU's lack of a minimum) and 4 (the refund administration fee's percentages) carried varying values. The values moved to two new rows of *What cx must read at run time*, as read 2026-11-09, with where each is read.
- **Methods.** Operation and field names were checked against the models clone (db2936aa): `listTransactions`, `listSummary`, `getMyFeesEstimateForSKU`, `getMyFeesEstimateForASIN`, `getMyFeesEstimates`, `getPromotion` (`feeSnapshot.previewedFeeRates`), and Data Kiosk `economicsPreview` / `DIGITAL_SERVICES_FEE_SOA` / `_FBA` / `taxAmount`. Report type names come from this file's SP-API section. Page titles and URLs come from *Pages read*. No web request, no Amazon API host and no help-hub call.
