# Regions, accounts, stores and account types

## Account shapes and regions

- Amazon sells through a North America and Brazil unified account (US, CA, MX, BR), a Europe account, and country-specific Asia-Pacific accounts. (P-rec-50)
- The SP-API serves them from three regional endpoints: NA (CA, US, MX, BR), EU (IE, ES, UK, FR, BE, NL, DE, IT, SE, ZA, PL, SA, EG, TR, AE, IN) and FE (SG, AU, JP). (P-rec-50)

## Authorizations

- Each selling account is authorized separately, and each authorization yields its own refresh token. (P-rec-51)
- For accounts merged across regions, Amazon states "The **Authorize app** button appears for each of your merged accounts." (P-rec-51)
- Only the Primary User can self-authorize an account. (P-rec-51)
- A private application has a self-authorization limit, stated on Authorization Limits. (P-rec-51)
- Amazon deactivates an authorization that is neither renewed nor called within the period its Selling Partner Authorizations FAQ states. (P-rec-51)
- A2X (a connector) uses one connection per region, and one per Seller ID where stores in a region have different Seller IDs. (P-rec-51)

## Stores and account types

- Amazon limits on-demand payouts per marketplace and account type, `listPayouts` returns payouts "grouped by the seller's account groups", and `listBalances` and `listSummary` filter by `marketplaceIds` and `accountType`. (P-rec-53)
- Each transaction carries `sellingPartnerMetadata.accountType` and `marketplaceId`. (P-rec-53)
- Seller Central shows Standard Orders and Invoiced Orders rows, and an "All" account type on Date Range reports. (P-rec-53)

## The subscription across merged accounts

- Amazon states how a merged global account's Professional subscription is split and in which store's currency it is charged on Changes to Professional Selling Plan subscription fees for global sellers. (P-rec-52)
- AMZ123 answers say a North America unified account pays only the US subscription, which conflicts with Amazon's post. (P-rec-52)
- Where and in which currency the seller's subscription was charged is read from the subscription rows of each store's settlement V2 and from `listTransactions` (`marketplaceDetails`, `totalAmount.currencyCode`). (P-rec-52)

## Where a cross-store charge lands

- Amazon states EU removal, disposal and liquidation fees are charged "in the currency of the country where your inventory is stored". (P-rec-54)
- Per search snippets of Amazon's pages, Remote Fulfillment orders appear in the Canada or Mexico account where the customer bought, with referral fees by the store of purchase. (P-rec-54)
- Per search snippets of Amazon's FBA Europe pages, the EFN fee is per order, set by the store of sale and the inventory pool. (P-rec-54)
- Amazon states no store for Pan-EU storage, AWD or account-wide service fees; per practitioners they appear on rows with an empty `marketplace-name`, and which store's settlement carries them is not stated by Amazon. (P-rec-54, P-rec-29)
- The currency and store of each charge are read on the charge itself: `listTransactions` `totalAmount.currencyCode` and `marketplaceDetails`, and settlement V2 `currency` and `marketplace-name`. (P-rec-54)
- The rules are on Amazon's Rate Card Europe Fees, Remote Fulfillment with FBA FAQ and FBA Europe pages. (P-rec-54)
