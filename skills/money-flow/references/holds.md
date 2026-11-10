# Held and withheld funds

## The contract

- Amazon's contract (NA Business Solutions Agreement §2) lets it withhold payments "for as long as we determine any related risks to Amazon or third parties persist". (P-flow-37)
- The contract lets Amazon offset anything it says the seller owes against payments. (P-flow-37)
- The contract lets Amazon "permanently withhold any payments" where it finds the account was used for "deceptive, fraudulent, or illegal activity" or to "repeatedly violate our Program Policies". (P-flow-37)
- In the EU, from 2024-07-12, permanent withholding extends to "any other account that you have operated" and names counterfeit goods. (P-flow-37)
- Amounts required as security may be "refundable or nonrefundable" and may be forfeited. (P-flow-37)
- §2 survives termination, and the available balance excludes amounts withheld under §2. (P-flow-37)

## The Funds Disbursement Eligibility policy

- The Funds Withholding policy was renamed the Funds Disbursement Eligibility policy on 2024-10-09 (US) and 2024-10-04 (EU). (P-flow-38)
- With the rename, Amazon shortened the wait after which a deactivated seller may appeal for withheld funds. (P-flow-38)
- The wait is read on the Fund Disbursement Eligibility Policy (EU PDF, https://m.media-amazon.com/images/G/02/Program_Policy/Fund_Disbursement_Eligibility_Policy.pdf); for the US, research/areas/money-flow.md, P-flow-38, holds it as News_Amazon posted it. (P-flow-38)
- After a deactivation under §3, Amazon "may withhold any funds", usable to "offset amounts that you owe, such as product returns or refunds, A-to-z claims from customers, inventory removal costs, outstanding fees, or monetary and non-monetary damages inflicted on Amazon". (P-flow-38)
- On reinstatement, funds are "released and disbursed according to your disbursement schedule". (P-flow-38)
- Otherwise the seller may appeal by email once the wait has passed, and Amazon releases "any remaining funds (less any amounts used to offset amounts you owe us)" after evaluating the account and "confirming your identity". (P-flow-38)
- Amazon may ask for documents on "identity, financial instruments, or supply chain". (P-flow-38)
- If Amazon "cannot confirm your identity", or finds deceptive, fraudulent, harmful or illegal activity, abuse or repeated violations, it "may be legally required to withhold any payments". (P-flow-38)
- The older texts with the longer wait (forum quotes 2020 to 2022, the JP PDF) predate the change. (P-flow-38)

## Holds without a deactivation

- An account "under review as per section 3" has its funds "withheld in accordance with our Funds Disbursement Eligibility Policy", with FBA shipment creation disabled (notice as posted, 2025-04). (P-flow-39)
- Amazon aims to lift a US identity-verification (INFORM) hold within a stated time after the seller submits the information; research/areas/money-flow.md, P-flow-39, holds the time as read. (P-flow-39)
- After an INFORM hold is lifted, the Account Health banner disappears, and "The available balance will disburse on your next scheduled settlement date". (P-flow-39)
- A bank change can bring "a temporary hold on disbursements for security purposes". (P-flow-39)
- ChannelX (2026-02) reports UK sellers whose KYC reviews held all payouts for more than a quarter while they kept selling. (P-flow-39)

## What the API shows of a hold

- `listExpectedPayouts` can read `DISABLED` ("Payouts have been disabled for this account"), `AT_RISK` (invalid deposit instrument) or `NO_PAYOUT_EXPECTED` (negative expected balance); whether these read on a held account, and in which regions, is read in Amazon's documents, not yet seen on a live account. (P-flow-40)
- `listPayouts` can show `NO_PAYOUT` and a free-text `failureReason`; in which regions it answers is read in Amazon's documents, not yet seen on a live account. (P-flow-40)
- No type, status or field names funds withheld under the contract or the Funds Disbursement Eligibility policy, and none carries a reason. (P-flow-40)
- Amazon does not state which `listBalances` bucket a withheld balance sits in. (P-flow-40)

## Court freezes and disputes

- Zhong Lun (2026-10) describes how, in US litigation, a court's temporary restraining order (TRO) makes platforms and payment providers freeze a seller's balances at once. (P-flow-41)
- In Zhong Lun's description, the defendant list of a "Schedule A" suit is sealed, so the seller learns of the suit from the freeze. (P-flow-41)
- In Zhong Lun's description, a TRO lasts up to 14 days, extendable once, and is usually followed by a preliminary injunction that keeps the freeze; defaulting defendants' frozen funds can be awarded to the plaintiff. (P-flow-41)
- Amazon's policy says only that it "may be legally required to withhold any payments". (P-flow-41)
- Court records and law-firm reports, read as search snippets only, say arbitrators under Washington law have decided both ways whether §2's permanent withholding is enforceable. (P-flow-42)
- The same snippets say a New York appellate court (Mariana Trading v Amazon, 2024) upheld an award that rejected the penalty argument, and seller-advocacy firms report awards striking the clause. (P-flow-42)
