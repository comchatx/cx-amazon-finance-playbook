"""A synthetic seller's tree for the skill-creator runs of cx-amazon-finance-playbook: no real seller, no Amazon call, no network.

    python3 -I evals/fixture.py <dir>            replaces <dir>/tenant and <dir>/stub-replies, leaves the rest of <dir>
    python3 -I evals/fixture.py <dir> --summary  the same, then prints the figures the cases are graded on, as JSON

Today is 2026-11-10, a Tuesday; "now" is 2026-11-10T09:00:00Z. Seller A1FIXTURESELLER, Hearthly Home GmbH (Hamburg, German VAT
number DE999999999), brand Hearthly. Two stores on two connections:
  US  ATVPDKIKX0DER   origin https://sellingpartnerapi-na.amazon.com   USD   settlements every 14 days from 2026-06-30
  DE  A1PA6795UKMFR9  origin https://sellingpartnerapi-eu.amazon.com   EUR   settlements every 14 days from 2026-08-26
All FBA, one unit per order. Ads are paid by card (notes/catalog.md), so no ad charge is in any money line.

<dir>/tenant is what the box holds after earlier sessions: a fee estimate for B0FIXTURE5 (2026-09-30), the US event groups read on
2026-10-23, the US settlement document for 2026-10-06..10-20 landed on 2026-10-23 under reports/, and the seller's notes: catalog.md,
costs.csv (batches with their unit cost and inbound freight; HL-SHERPA-Q's cost rose with the batch received 2026-10-16) and
bank-deposits.csv (the seller's own record of what reached the two bank accounts, exported 2026-11-09).
<dir>/stub-replies is what Amazon answers today, for evals/cx, out of the run's sight: data.json (every transaction, period,
payout, order and report the stand-in answers from) and report-files/ (settlement V2 documents, US plain text, DE gzip; the
requested FBA reports; the Data Kiosk error document).

Every figure is invented, in the shapes Amazon's models (finances_2024-06-19, financesV0, transfers_2024-06-01, reports_2021-06-30,
productFeesV0, dataKiosk_2023-11-15, orders_2026-01-01, sales) and the research's report columns give. Where neither names a value,
the fixture's own label stands and is listed here: the breakdownType parents ProductCharges / AmazonFees / WithheldTax (P-sell-28 gives
ProductCharges, AmazonFees, Commission as production strings), the nested Base / Tax split of a German fee and its VAT, the
settlement amount-description strings for storage, subscription and placement, the date formats of settlement-start-date and
deposit-date, a released order line carrying its shipment's posted-date, and every error text, which begins "stub:".

Money rules of the fixture (each one the shape a position states, with the fixture's own values):
  - An order posts at shipment as DEFERRED with DeferredContext DD7 and a maturityDate; it is released on its maturityDate and
    becomes DEFERRED_RELEASED (P-flow-1, P-flow-19). US maturity is delivery + 7 days. DE maturity is delivery + 7 days for units
    shipped before 2026-10-01 and delivery + 14 days from then (an Amazon email in notes/catalog.md, "while we are reviewing your
    account"; P-flow-2). Delivery is 2 to 4 days after shipment.
  - A settlement holds the order lines released in its period and the other lines posted in it, plus "Previous Reserve Amount
    Balance" and minus "Current Reserve Amount" (P-rec-8, P-rec-22). Its total is the payout (P-api-26). The 2024-06-19 transactions
    of its group carry no reserve line, so a group's transactions sum to the total plus the current reserve minus the previous
    one: whether Amazon's group sums and settlement totals agree is the live question P-api open 5 names, and here they do not.
  - US reserve 250.00 to the settlement closing 2026-10-20, 300.00 from the one closing 2026-11-03. DE 100,00, then 120,00 from
    the settlement closing 2026-10-21.
  - listBalances: DEFERRED is the orders posted and not yet matured; ACCOUNT_LEVEL_RESERVE the current reserve; AVAILABLE the
    open period's previous reserve plus what was released into it so far, minus the current reserve; RESERVED = DEFERRED +
    ACCOUNT_LEVEL_RESERVE; TOTAL = AVAILABLE + RESERVED (P-api-7). asOfDate answers the same sums at the end of that day (UTC).
  - The stand-in answers Transfers listPayouts and listExpectedPayouts for both stores; whether Amazon answers them for the US store
    is open, the live call's to say (P-api-11).
  - The expected payout is today's AVAILABLE, scheduled two days after the open period ends (P-flow-22). A payout reads STARTED and
    IN_TRANSIT on the period's end day and PAID two days later; US money reaches the seller's account the day after PAID, DE money
    two business days after (notes/bank-deposits.csv); the seller's export has no row yet for the DE payout PAID on 2026-11-06.
  - US: referral 15% of the price; FBA fee by ship date, peak from 2026-10-15 (HL-FLEECE-GRY 6.05 -> 6.33, HL-SHERPA-Q 8.40 -> 8.95,
    HL-WEIGHTED-15 8.78 -> 9.10; P-ful-1, P-ful-22); state sales tax in Tax and the same amount withheld as
    MarketplaceFacilitatorTax-Principal (P-tax-2). A refund reverses principal and tax, credits the referral fee back and keeps a
    refund administration fee of 20% of it, capped at 5.00 (RefundCommission; P-sell-7, P-sell-8); the FBA fee stays (P-ref-3).
  - DE: price VAT-inclusive (P-prof-22), no tax line and no facilitator line, because the seller is established in Germany
    (P-tax-19); referral 15% of the price; each fee carries 19% VAT in its own nested breakdown, in the fee estimate's TaxAmount,
    and inside the settlement's single fee amount (P-tax-13, P-sell-14). Settlement amounts in German number format, "34,99".
  - Account-level lines with no order and no SKU (P-rec-29, P-ful-17): monthly storage posted around the 8th for the month before
    (TimeRangeContext), the subscription on the 14th (US) and 10th (DE), an inbound placement fee (US, 2026-10-27), reimbursements.
  - getReports lists a settlement report from the day after its period ends, and only those created in the last 90 days
    (P-api-30); the Deferred Transaction Report is absent (P-api-17). The VAT transaction and US sales-tax reports answer 403: the
    application holds Product Listing, Pricing, Brand Analytics, Finance and Accounting and Amazon Fulfillment, not Tax Invoicing or
    Tax Remittance (P-tax-10). A Data Kiosk query on analytics_economics_2024_03_15 ends FATAL with an error document saying a role
    is missing, without naming which (P-api-23). listTransactions with relatedIdentifierName=SETTLEMENT_ID answers 400 (P-api-3).

SCENARIOS. Each names its right answer and the positions it rests on; --summary prints the figures.

money-flow
  F1 where-is-my-money (US). "Seller Central says I have money but the next payout is small: where is it, and when does it come?"
     listBalances now: AVAILABLE, DEFERRED, ACCOUNT_LEVEL_RESERVE, TOTAL; listExpectedPayouts: the next payout and its date;
     listTransactions DEFERRED with each maturityDate (P-flow-1, -3, -19, -21, -22). The release day is each transaction's
     maturityDate, not a day count recited (P-flow-2, -3); the reserve's reason is shown only in Seller Central (P-flow-9); an open
     balance is not a guaranteed payout (P-api-26). Nothing is changed.
  F2 de-paid-not-arrived (DE). "The DE payout says PAID on 11-06 but my bank has nothing; and pay out the German balance now."
     listPayouts: PAID 2026-11-06 with its trace id; Amazon's words on PAID disagree (P-api-12) and the time to the bank is stated
     only for the US (P-flow-1); October-shipped DE orders mature 14 days after delivery (maturityDate), not 7 (P-flow-2);
     initiatePayout is a money-moving write that covers DE (P-api-13, P-flow-12, -13): the run sends none, or the stand-in refuses it.

fees-and-charges
  C1 october-fees (US). Every fee and charge posted in October 2026 by its label, with the account-level lines (September storage
     posted 2026-10-08 with TimeRangeContext September, the subscription, the inbound placement fee) apart from the per-order ones
     (P-ful-3, -6, -16, -21, P-sell-11, -26). Labels are open strings (P-sell-26, P-api-4).
  C2 weighted-fba-fee-rose (US). B0FIXTURE5's FBA fee 8.78 -> 9.10 for units shipped from 2026-10-15: the fee is charged at the ship
     date's rate and the peak window is Amazon's dated value, read from its page (P-ful-1, -22); today's estimate (stub) 9.10, the
     2026-09-30 estimate in the tree 8.78, neither guaranteed (P-api-19); the Fee Preview's dimensions and tier did not change;
     a dimension claim has its own window, read in Seller Central (P-ful-2).
  C3 refund-fee-kept (US). One weighted-blanket refund in October: principal 79.99 reversed, Commission +12.00, RefundCommission
     -2.40, FBA fee not returned (P-sell-7, -8, P-ref-2, -3); the rate and cap are the store's, read at run time.

refunds-and-reimbursements
  R1 reimbursements-october (US). GET_FBA_REIMBURSEMENTS_DATA: two units lost (6.90 each), one damaged (16.20 cash), one damaged
     put back as inventory (no money), and a reversal of one lost unit (-6.90) linked by original-reimbursement-id (P-ref-12, -14,
     -17, -18, -19, -20). The cash rows match the FBAInventoryReimbursement transactions. Valued at Amazon's sourcing-cost estimate
     unless the seller entered one (P-ref-14): the sherpa's 16.20 is the old batch's cost, the new one is 18.40. Windows are dated
     facts with their pages (P-ref-16); no SP-API files a claim (P-ref-29).
  R2 refunds-by-date (US). October's refunds counted by posting date against refunds of October orders (some posted in November),
     and Economics' refund-request time; which date is booked is the seller's choice (P-ref-25, P-prof-28).

product-earnings
  P1 sherpa-october (US). HL-SHERPA-Q shipped in October: sales, fees, refunds, reimbursement; cost under the batch change: by
     date (17.50 before 2026-10-16, 20.00 from it), FIFO (the old batch covers October), moving average from 10-16 (P-prof-29,
     -30); no ad charge in the money lines (card-paid; P-sell-23); account-level charges left off or spread (P-prof-31).
  P2 all-products-with-overheads (US). Each product's October contribution, then the account-level lines posted in October spread by
     sales share, by units or by the storage report's estimated share (P-prof-31, -32, P-ful-3, -21); the Economics query ends
     FATAL on a role, and which role is an open question (P-api-23, P-prof-12).

settlement-reconcile
  S1 payout-1105 (US). Settlement 2026-10-20..11-03, paid 2026-11-05: its lines sum to its total; released orders include ones
     shipped before 10-20; reserve 250 -> 300; account-level lines have no SKU or order; the group's transactions sum to the
     total plus 50.00 (P-rec-8, -22, -29, -11, P-api-26, open 5). The seller's bank row of 2026-11-06 matches.
  S2 de-settlement-eu-format (DE). Settlement 2026-10-07..10-21: amounts in German format ("69,26"); a script that drops the comma
     reads hundredfold (6926); lines sum to the total; the bank row of 2026-10-27 matches (P-rec-5, P-flow-23).
  S3 october-close (US). October's ordered sales (getOrderMetrics) against October's two deposits: settlements cross months,
     deferred money at 10-31 (listBalances asOfDate), posted vs order date, UTC vs local; the split of the 10-20..11-03 settlement by
     posted month is a choice (P-rec-15, -31, -32, -33, P-flow-32, -33).

tax-lines
  T1 de-vat (DE). VAT on Amazon's fees (Commission 5.25 + 1.00, FBA 4.12 + 0.78; rate read from the lines); no facilitator VAT
     on the seller's German sales, so the VAT inside the price is the seller's (P-tax-4, -13, -19, P-prof-22); recoverable or cost
     is the seller's booking (P-tax-29); GET_VAT_TRANSACTION_DATA needs Tax Invoicing (Restricted) (P-tax-10); fee invoices are in
     Seller Central (P-tax-12, P-rec-47).
  T2 us-sales-tax-1099k (US). Tax and MarketplaceFacilitatorTax-Principal net to zero (P-tax-2); the 1099-K is gross and its
     threshold is the IRS's for the year (P-tax-7, -8); the sales tax report is generated in the Tax Document Library and needs Tax
     Remittance (Restricted) (P-tax-9); Amazon's collection does not cover state gross-receipts taxes (P-tax-30, -31).

money-reads
  M1 settlements-for-the-accountant (US). July to October: getReports lists the settlements created since 2026-08-12 only; the
     earlier ones are requested again in Seller Central, and practitioners disagree on what follows (P-api-30, -31, P-rec-6, -59);
     the event groups and transactions answer in windows of at most 180 days (P-api-2, -33); v1 settlement types end 2026-11-11.
  M2 deferred-report-and-settlement-filter (US). The Deferred Transaction Report is not in getReports until the seller requests it in
     Seller Central (P-api-17, -35); listTransactions DEFERRED and listBalances DEFERRED give the deferred money now; SETTLEMENT_ID is
     not a filter in the model (P-api-3), the group id is (P-api-6).
"""
import datetime as dt
import gzip
import hashlib
import json
import os
import shutil
import sys

root = sys.argv[1]
SUMMARY = "--summary" in sys.argv[2:]
T = os.path.join(root, "tenant")
S = os.path.join(root, "stub-replies")
shutil.rmtree(T, ignore_errors=True)
shutil.rmtree(S, ignore_errors=True)
for stale in ("stub-state", "cx-calls.log"):
    p = os.path.join(root, stale)
    shutil.rmtree(p, ignore_errors=True) if os.path.isdir(p) else (os.path.exists(p) and os.remove(p))

SELLER = "A1FIXTURESELLER"
US, DE = "ATVPDKIKX0DER", "A1PA6795UKMFR9"
NOW = dt.datetime(2026, 11, 10, 9, 0, tzinfo=dt.timezone.utc)
D = dt.date.fromisoformat
UTC = dt.timezone.utc


def put(base, rel, data, mode="w"):
    path = os.path.join(base, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if isinstance(data, bytes):
        with open(path, "wb") as f:
            f.write(data)
    else:
        with open(path, mode) as f:
            f.write(data if isinstance(data, str) else json.dumps(data, indent=2))


def u(*parts):
    return int(hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()[:12], 16) / float(1 << 48)


def h(n, *parts):
    return hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()[:n]


def iso(t):
    return t.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def at(day, hour=0, minute=0, sec=0):
    return dt.datetime(day.year, day.month, day.day, hour, minute, sec, tzinfo=UTC)


def r2(x):
    return float(f"{x + (1e-9 if x >= 0 else -1e-9):.2f}")


def money(cur, x):
    return {"currencyCode": cur, "currencyAmount": r2(x)}


# ---------------------------------------------------------------------------------------------------------------------------
# Stores, products and fees

STORES = {
    US: {"cur": "USD", "name": "Amazon.com", "region": "na", "origin": "https://sellingpartnerapi-na.amazon.com",
         "first_period": D("2026-06-30"), "orders_from": D("2026-06-21"), "sid0": 24183000101, "oid": "113",
         "reserve": lambda end: 250.0 if end <= D("2026-10-20") else 300.0, "tail": "4417", "rail": "ACH", "bank_lag": 1},
    DE: {"cur": "EUR", "name": "Amazon.de", "region": "eu", "origin": "https://sellingpartnerapi-eu.amazon.com",
         "first_period": D("2026-08-26"), "orders_from": D("2026-08-17"), "sid0": 25077000101, "oid": "302",
         "reserve": lambda end: 100.0 if end <= D("2026-10-07") else 120.0, "tail": "8820", "rail": "SEPA", "bank_lag": 2},
}
LAST_ORDER_DAY = D("2026-11-07")
PEAK = D("2026-10-15")

PRODUCTS = {
    US: {"HL-FLEECE-GRY": ("B0FIXTURE1", "Hearthly Fleece Throw Blanket 50x60, Grey", 29.99, 6.05, 6.33, 4.0),
         "HL-SHERPA-Q": ("B0FIXTURE4", "Hearthly Sherpa Fleece Blanket Queen 90x90, Navy", 59.99, 8.40, 8.95, 2.6),
         "HL-WEIGHTED-15": ("B0FIXTURE5", "Hearthly Weighted Blanket 15 lb, 60x80, Grey", 79.99, 8.78, 9.10, 2.4)},
    DE: {"HL-FLEECE-GRY-DE": ("B0FIXTURE1", "Hearthly Fleecedecke 127x152 cm, Grau", 34.99, 4.12, 4.12, 2.6),
         "HL-SHERPA-Q-DE": ("B0FIXTURE4", "Hearthly Sherpa-Decke 230x230 cm, Navy", 64.99, 6.30, 6.30, 1.8)},
}
TAX_RATES = (0.06, 0.0725, 0.0825, 0.08875)
VAT = 0.19


def fba_fee(store, sku, ship_day):
    p = PRODUCTS[store][sku]
    return p[4] if ship_day >= PEAK else p[3]


def referral(price):
    return r2(price * 0.15)


def periods(store):
    st = STORES[store]
    out, k, start = [], 0, st["first_period"]
    while start <= NOW.date():
        end = start + dt.timedelta(14)
        closed = at(end, 7) <= NOW
        sid = str(st["sid0"] + k)
        out.append({"k": k, "start": at(start, 7), "end": at(end, 7), "closed": closed, "settlementId": sid,
                    "groupId": h(43, "group", store, sid).replace("0", "Q").replace("1", "x"),
                    "curReserve": st["reserve"](end), "traceId": ("FIXT" + h(11, "trace", sid)).upper()})
        start, k = end, k + 1
    for i, p in enumerate(out):
        p["prevReserve"] = out[i - 1]["curReserve"] if i else st["reserve"](p["start"].date())
    return out


PER = {s: periods(s) for s in STORES}


def period_of(store, t):
    for p in PER[store]:
        if p["start"] <= t < p["end"]:
            return p
    raise ValueError((store, t))


# ---------------------------------------------------------------------------------------------------------------------------
# Orders, refunds and account-level lines: one record per money line, the transaction built from it

TX = {US: [], DE: []}
ORDERS = {US: {}, DE: {}}


def order_id(store, n):
    a = int(u("oid", store, n) * 1e7)
    b = int(u("oid2", store, n) * 1e7)
    return "%s-%07d-%07d" % (STORES[store]["oid"], a, b)


def add_order(store, sku, day, n):
    st = STORES[store]
    asin, title, price, *_ = PRODUCTS[store][sku]
    oid = order_id(store, (day, sku, n))
    posted = at(day, 15 + n % 7, (13 * n + 7) % 60, (29 * n) % 60)
    created = posted - dt.timedelta(hours=26 + n % 5)
    delivered = day + dt.timedelta(2 + int(u("dlv", oid) * 3))
    dd = 14 if store == DE and day >= D("2026-10-01") else 7
    maturity = at(delivered + dt.timedelta(dd), 7)
    fba = fba_fee(store, sku, day)
    comm = referral(price)
    if store == US:
        rate = TAX_RATES[int(u("tax", oid) * 4)]
        tax = r2(price * rate)
        lines = {"Principal": price, "Tax": tax, "MarketplaceFacilitatorTax-Principal": -tax, "Commission": -comm,
                 "FBAPerUnitFulfillmentFee": -fba}
        fee_vat = {}
    else:
        tax = 0.0
        cv, fv = r2(comm * VAT), r2(fba * VAT)
        lines = {"Principal": price, "Commission": -r2(comm + cv), "FBAPerUnitFulfillmentFee": -r2(fba + fv)}
        fee_vat = {"Commission": (-comm, -cv), "FBAPerUnitFulfillmentFee": (-fba, -fv)}
    total = r2(sum(lines.values()))
    shipment = "D%s" % h(10, "shp", oid).upper()
    item_code = "%014d" % int(u("item", oid) * 1e14)
    rec = {"kind": "order", "store": store, "orderId": oid, "sku": sku, "asin": asin, "title": title, "price": price,
           "posted": posted, "created": created, "delivered": delivered, "maturity": maturity, "dd": dd, "lines": lines,
           "feeVat": fee_vat, "total": total, "tax": tax, "fba": fba, "comm": comm, "shipment": shipment, "itemCode": item_code,
           "release": maturity}
    TX[store].append(rec)
    ORDERS[store][oid] = rec
    if u("refund", oid) < 0.05:
        rday = day + dt.timedelta(9 + int(u("rday", oid) * 10))
        if rday <= LAST_ORDER_DAY:
            adm = min(5.0, r2(comm * 0.20))
            if store == US:
                rl = {"Principal": -price, "Tax": -tax, "MarketplaceFacilitatorTax-Principal": tax, "Commission": comm,
                      "RefundCommission": -adm}
                rv = {}
            else:
                av = r2(adm * VAT)
                rl = {"Principal": -price, "Commission": r2(comm + r2(comm * VAT)), "RefundCommission": -r2(adm + av)}
                rv = {"Commission": (comm, r2(comm * VAT)), "RefundCommission": (-adm, -av)}
            rposted = at(rday, 20, (11 * n) % 60, 5)
            TX[store].append({"kind": "refund", "store": store, "orderId": oid, "sku": sku, "asin": asin, "title": title,
                              "price": price, "posted": rposted, "lines": rl, "feeVat": rv, "total": r2(sum(rl.values())),
                              "adjustmentId": "amzn1.adj." + h(16, "adj", oid), "refundId": "R" + h(12, "rid", oid).upper(),
                              "shipment": shipment, "itemCode": item_code, "release": rposted, "orderPosted": posted,
                              "orderCreated": created})


for store in STORES:
    day = STORES[store]["orders_from"]
    while day <= LAST_ORDER_DAY:
        for sku, prod in PRODUCTS[store].items():
            n = int(u("units", store, sku, day) * prod[5])
            for i in range(n):
                add_order(store, sku, day, i + 3 * list(PRODUCTS[store]).index(sku))
        day += dt.timedelta(1)


def other(store, posted, kind, desc, amount, settle_type, settle_desc, extra=None, vat=None, sku=None, asin=None, rng=None):
    rec = {"kind": kind, "store": store, "posted": posted, "desc": desc, "total": r2(amount), "settleType": settle_type,
           "settleDesc": settle_desc, "release": posted, "sku": sku, "asin": asin, "range": rng, "vat": vat}
    rec.update(extra or {})
    TX[store].append(rec)
    return rec


def month_range(y, m):
    a = dt.date(y, m, 1)
    b = dt.date(y + (m == 12), m % 12 + 1, 1)
    return (at(a), at(b) - dt.timedelta(seconds=1))


for m, posted, amt in ((6, "2026-07-09", 318.40), (7, "2026-08-10", 335.12), (8, "2026-09-09", 356.80), (9, "2026-10-08", 412.37),
                       (10, "2026-11-07", 468.90)):
    other(US, at(D(posted), 11, 4), "storage", "FBA storage fee", -amt, "other-transaction", "Storage Fee", rng=month_range(2026, m))
for posted in ("2026-07-14", "2026-08-14", "2026-09-14", "2026-10-14"):
    other(US, at(D(posted), 9, 30), "subscription", "Subscription", -39.99, "other-transaction", "Subscription Fee")
other(US, at(D("2026-10-27"), 13, 2), "placement", "FBA inbound placement service fee", -86.40, "other-transaction",
      "FBA Inbound Placement Service Fee", extra={"shipmentId": "FBA19FIXT0001"})
for m, posted, base in ((9, "2026-10-09", 35.00), (10, "2026-11-07", 44.00)):
    other(DE, at(D(posted), 11, 20), "storage", "FBA storage fee", -r2(base * (1 + VAT)), "other-transaction", "Storage Fee",
          vat=(-base, -r2(base * VAT)), rng=month_range(2026, m))
for posted in ("2026-09-10", "2026-10-10"):
    other(DE, at(D(posted), 9, 0), "subscription", "Subscription", -r2(39.0 * (1 + VAT)), "other-transaction", "Subscription Fee",
          vat=(-39.0, -r2(39.0 * VAT)))

REIMB = [
    # approval, id, case, reason, sku, cash qty, inv qty, per unit, original id/type
    ("2026-10-09", "4471900001", "", "Lost_Warehouse", "HL-FLEECE-GRY", 2, 0, 6.90, "", ""),
    ("2026-10-23", "4471900002", "", "Damaged_Warehouse", "HL-SHERPA-Q", 1, 0, 16.20, "", ""),
    ("2026-10-23", "4471900003", "", "Damaged_Warehouse", "HL-WEIGHTED-15", 0, 1, 20.50, "", ""),
    ("2026-10-30", "4471900004", "", "Reimbursement_Reversal", "HL-FLEECE-GRY", -1, 0, 6.90, "4471900001", "Lost_Warehouse"),
]
SETTLE_REASON = {"Lost_Warehouse": "WAREHOUSE_LOST", "Damaged_Warehouse": "WAREHOUSE_DAMAGE", "Reimbursement_Reversal": "REVERSAL_REIMBURSEMENT"}
for appr, rid, case, reason, sku, qc, qi, per, orig, otype in REIMB:
    if qc:
        other(US, at(D(appr), 14, 40), "reimbursement", SETTLE_REASON[reason], r2(qc * per), "other-transaction", SETTLE_REASON[reason],
              extra={"reimbursementId": rid, "settleAmountType": "FBA Inventory Reimbursement"}, sku=sku, asin=PRODUCTS[US][sku][0])

for store in STORES:
    TX[store].sort(key=lambda r: (r["posted"], r.get("orderId", ""), r["kind"]))
    for i, r in enumerate(TX[store]):
        r["transactionId"] = "%s-%s" % (store[-4:], h(20, "txn", store, i, r["kind"], r.get("orderId", r.get("desc"))))


# ---------------------------------------------------------------------------------------------------------------------------
# Settlements, groups, payouts and balances

def released_in(store, p):
    return [r for r in TX[store] if p["start"] <= r["release"] < p["end"]]


SETTLE = {US: {}, DE: {}}
for store in STORES:
    for p in PER[store]:
        rows = released_in(store, p)
        txsum = r2(sum(r["total"] for r in rows))
        total = r2(p["prevReserve"] + txsum - p["curReserve"])
        SETTLE[store][p["settlementId"]] = {"period": p, "rows": rows, "txsum": txsum, "total": total}


def status_of(r):
    if r["kind"] != "order":
        return "RELEASED"
    return "DEFERRED_RELEASED" if r["maturity"] <= NOW else "DEFERRED"


def balances_at(store, t):
    p = period_of(store, t) if t >= PER[store][0]["start"] else PER[store][0]
    deferred = r2(sum(r["total"] for r in TX[store] if r["kind"] == "order" and r["posted"] <= t < r["maturity"]))
    rel = r2(sum(r["total"] for r in TX[store] if p["start"] <= r["release"] <= t))
    avail = r2(p["prevReserve"] + rel - p["curReserve"])
    alr = p["curReserve"]
    return {"AVAILABLE": avail, "DEFERRED": deferred, "ACCOUNT_LEVEL_RESERVE": alr, "RESERVED": r2(deferred + alr),
            "TOTAL": r2(avail + deferred + alr), "openBalance": r2(p["prevReserve"] + rel), "period": p}


# ---------------------------------------------------------------------------------------------------------------------------
# The 2024-06-19 transaction objects

def bd(t, cur, amt, kids=None):
    return {"breakdownType": t, "breakdownAmount": money(cur, amt), "breakdowns": kids or []}


def fee_bd(store, cur, name, amt, vat):
    if store == DE and name in vat:
        base, tax = vat[name]
        return bd(name, cur, amt, [bd("Base", cur, base), bd("Tax", cur, tax)])
    return bd(name, cur, amt)


def tx_object(r):
    store, cur = r["store"], STORES[r["store"]]["cur"]
    st = status_of(r)
    meta = {"sellingPartnerId": SELLER, "accountType": "Standard Orders", "marketplaceId": store}
    rel = []
    if r.get("orderId"):
        rel.append({"relatedIdentifierName": "ORDER_ID", "relatedIdentifierValue": r["orderId"]})
    if r.get("shipment") and r["kind"] == "order":
        rel.append({"relatedIdentifierName": "SHIPMENT_ID", "relatedIdentifierValue": r["shipment"]})
    if r.get("refundId"):
        rel.append({"relatedIdentifierName": "REFUND_ID", "relatedIdentifierValue": r["refundId"]})
    if r.get("shipmentId"):
        rel.append({"relatedIdentifierName": "SHIPMENT_ID", "relatedIdentifierValue": r["shipmentId"]})
    if st != "DEFERRED":
        p = period_of(store, r["release"])
        rel.append({"relatedIdentifierName": "FINANCIAL_EVENT_GROUP_ID", "relatedIdentifierValue": p["groupId"]})
        if p["closed"]:
            rel.append({"relatedIdentifierName": "SETTLEMENT_ID", "relatedIdentifierValue": p["settlementId"]})
    L = r.get("lines", {})
    vat = r.get("feeVat", {})
    if r["kind"] in ("order", "refund"):
        prod = [bd(k, cur, L[k]) for k in ("Principal", "Tax") if k in L]
        fees = [fee_bd(store, cur, k, L[k], vat) for k in ("Commission", "FBAPerUnitFulfillmentFee", "RefundCommission") if k in L]
        groups = [bd("ProductCharges", cur, sum(L[k] for k in ("Principal", "Tax") if k in L), prod),
                  bd("AmazonFees", cur, sum(x["breakdownAmount"]["currencyAmount"] for x in fees), fees)]
        if "MarketplaceFacilitatorTax-Principal" in L:
            groups.append(bd("WithheldTax", cur, L["MarketplaceFacilitatorTax-Principal"],
                             [bd("MarketplaceFacilitatorTax-Principal", cur, L["MarketplaceFacilitatorTax-Principal"])]))
        pc = {"contextType": "ProductContext", "asin": r["asin"], "sku": r["sku"], "quantityShipped": 1, "fulfillmentNetwork": "AFN"}
        item = {"description": r["title"], "totalAmount": money(cur, r["total"]), "breakdowns": groups, "contexts": [pc],
                "relatedIdentifiers": ([{"itemRelatedIdentifierName": "ORDER_ADJUSTMENT_ITEM_ID", "itemRelatedIdentifierValue": r["adjustmentId"]}]
                                       if r["kind"] == "refund" else [])}
        out = {"sellingPartnerMetadata": meta, "relatedIdentifiers": rel,
               "transactionType": "Shipment" if r["kind"] == "order" else "Refund", "transactionId": r["transactionId"],
               "transactionStatus": st, "description": "Order Payment" if r["kind"] == "order" else "Refund Order",
               "postedDate": iso(r["posted"]), "totalAmount": money(cur, r["total"]),
               "marketplaceDetails": {"marketplaceId": store, "marketplaceName": STORES[store]["name"]},
               "items": [item], "breakdowns": groups, "contexts": []}
        if r["kind"] == "order":
            out["contexts"] = [{"contextType": "DeferredContext", "deferralReason": "DD7", "maturityDate": iso(r["maturity"])}]
        return out
    ttype = {"storage": "ServiceFee", "subscription": "ServiceFee", "placement": "ServiceFee", "reimbursement": "FBAInventoryReimbursement"}[r["kind"]]
    if r.get("vat"):
        brk = [bd(r["desc"], cur, r["total"], [bd("Base", cur, r["vat"][0]), bd("Tax", cur, r["vat"][1])])]
    else:
        brk = [bd(r["desc"], cur, r["total"])]
    ctx = []
    if r.get("range"):
        ctx.append({"contextType": "TimeRangeContext", "startTime": iso(r["range"][0]), "endTime": iso(r["range"][1])})
    items = []
    if r.get("sku"):
        items = [{"description": PRODUCTS[store][r["sku"]][1], "totalAmount": money(cur, r["total"]), "breakdowns": brk,
                  "contexts": [{"contextType": "ProductContext", "asin": r["asin"], "sku": r["sku"], "fulfillmentNetwork": "AFN"}],
                  "relatedIdentifiers": []}]
    return {"sellingPartnerMetadata": meta, "relatedIdentifiers": rel, "transactionType": ttype, "transactionId": r["transactionId"],
            "transactionStatus": st, "description": r["desc"], "postedDate": iso(r["posted"]), "totalAmount": money(cur, r["total"]),
            "marketplaceDetails": {"marketplaceId": store, "marketplaceName": STORES[store]["name"]}, "items": items,
            "breakdowns": brk, "contexts": ctx}


# ---------------------------------------------------------------------------------------------------------------------------
# Settlement V2 documents (tab-delimited, 24 columns)

COLS = ["settlement-id", "settlement-start-date", "settlement-end-date", "deposit-date", "total-amount", "currency", "transaction-type",
        "order-id", "merchant-order-id", "adjustment-id", "shipment-id", "marketplace-name", "amount-type", "amount-description",
        "amount", "fulfillment-id", "posted-date", "posted-date-time", "order-item-code", "merchant-order-item-id",
        "merchant-adjustment-item-id", "sku", "quantity-purchased", "promotion-id"]


def num(store, x):
    s = "%.2f" % x
    return s.replace(".", ",") if store == DE else s


def sdate(t):
    return t.astimezone(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")


def settlement_doc(store, sid):
    st, s = STORES[store], SETTLE[store][sid]
    p = s["period"]
    dep = p["end"] + dt.timedelta(2)
    lines = ["\t".join(COLS)]
    head = {c: "" for c in COLS}
    head.update({"settlement-id": sid, "settlement-start-date": sdate(p["start"]), "settlement-end-date": sdate(p["end"]),
                 "deposit-date": sdate(dep), "total-amount": num(store, s["total"]), "currency": st["cur"]})
    lines.append("\t".join(head[c] for c in COLS))

    def row(r, ttype, atype, adesc, amt, qty="", order=True):
        v = {c: "" for c in COLS}
        v.update({"settlement-id": sid, "transaction-type": ttype, "amount-type": atype, "amount-description": adesc,
                  "amount": num(store, amt), "posted-date": r["posted"].strftime("%m/%d/%y"), "posted-date-time": sdate(r["posted"])})
        if order:
            v.update({"order-id": r["orderId"], "shipment-id": r["shipment"], "marketplace-name": st["name"], "fulfillment-id": "AFN",
                      "order-item-code": r["itemCode"], "sku": r["sku"], "quantity-purchased": str(qty)})
        return "\t".join(v[c] for c in COLS)

    prev = {"posted": p["start"]}
    lines.append(row(prev, "other-transaction", "other-transaction", "Previous Reserve Amount Balance", p["prevReserve"], order=False))
    for r in s["rows"]:
        L = r.get("lines", {})
        if r["kind"] == "order":
            for k, at_ in (("Principal", "ItemPrice"), ("Tax", "ItemPrice"), ("MarketplaceFacilitatorTax-Principal", "ItemWithheldTax"),
                           ("Commission", "ItemFees"), ("FBAPerUnitFulfillmentFee", "ItemFees")):
                if k in L:
                    lines.append(row(r, "Order", at_, k, L[k], 1))
        elif r["kind"] == "refund":
            for k, at_ in (("Principal", "ItemPrice"), ("Tax", "ItemPrice"), ("MarketplaceFacilitatorTax-Principal", "ItemWithheldTax"),
                           ("Commission", "ItemFees"), ("RefundCommission", "ItemFees")):
                if k in L:
                    x = row(r, "Refund", at_, k, L[k], 1).split("\t")
                    x[COLS.index("adjustment-id")] = r["adjustmentId"]
                    lines.append("\t".join(x))
        else:
            x = row(r, "other-transaction", r.get("settleAmountType", "other-transaction"), r["settleDesc"], r["total"], order=False)
            if r.get("sku"):
                x = x.split("\t")
                x[COLS.index("sku")] = r["sku"]
                x = "\t".join(x)
            lines.append(x)
    cur = {"posted": p["end"] - dt.timedelta(seconds=1)}
    lines.append(row(cur, "other-transaction", "other-transaction", "Current Reserve Amount", -p["curReserve"], order=False))
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------------------------------------------------------
# Stub data: transactions, periods, payouts, orders, reports

def strip(r):
    return {k: (iso(v) if isinstance(v, dt.datetime) else v) for k, v in r.items() if k in ("kind", "sku", "asin", "orderId", "total")}


data = {"now": iso(NOW), "seller": SELLER, "stores": {}, "reports": [], "requestable": {}, "restricted": [], "fees": {}}
REPORTS = []
os.makedirs(os.path.join(S, "report-files"), exist_ok=True)
for store, st in STORES.items():
    txs = []
    for r in TX[store]:
        o = tx_object(r)
        o["_posted"] = iso(r["posted"])
        o["_release"] = iso(r["release"])
        o["_kind"] = r["kind"]
        txs.append(o)
    pers = []
    for p in PER[store]:
        s = SETTLE[store][p["settlementId"]]
        pers.append({"start": iso(p["start"]), "end": iso(p["end"]), "closed": p["closed"], "settlementId": p["settlementId"],
                     "groupId": p["groupId"], "prevReserve": p["prevReserve"], "curReserve": p["curReserve"], "traceId": p["traceId"],
                     "total": s["total"], "txsum": s["txsum"]})
        if p["closed"]:
            created = p["end"] + dt.timedelta(hours=22)
            rid = str(70000000000 + int(p["settlementId"]) % 100000 * 10 + (1 if store == US else 2))
            doc = settlement_doc(store, p["settlementId"])
            fname = "settlement-%s-%s.%s" % (store, p["settlementId"], "txt" if store == US else "txt.gz")
            put(S, "report-files/" + fname, doc if store == US else gzip.compress(doc.encode(), mtime=0))
            REPORTS.append({"reportId": rid, "reportType": "GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2", "marketplaceIds": [store],
                            "dataStartTime": iso(p["start"]), "dataEndTime": iso(p["end"]), "createdTime": iso(created),
                            "processingStatus": "DONE", "processingStartTime": iso(created), "processingEndTime": iso(created + dt.timedelta(minutes=3)),
                            "reportDocumentId": "amzn1.spdoc.1.4.na." + h(24, "doc", rid) if store == US else "amzn1.spdoc.1.4.eu." + h(24, "doc", rid),
                            "_file": fname, "_gzip": store == DE})
    orders = {}
    for oid, r in ORDERS[store].items():
        orders[oid] = {"orderId": oid, "created": iso(r["created"]), "posted": iso(r["posted"]), "sku": r["sku"], "asin": r["asin"],
                       "title": r["title"], "price": r["price"], "tax": r["tax"], "shipment": r["shipment"], "itemCode": r["itemCode"]}
    data["stores"][store] = {"currency": st["cur"], "name": st["name"], "region": st["region"], "periods": pers, "transactions": txs,
                             "orders": orders, "accountTail": st["tail"], "paymentRail": st["rail"],
                             "products": {sku: {"asin": v[0], "title": v[1], "price": v[2], "fba": v[4], "fbaPrePeak": v[3]} for sku, v in PRODUCTS[store].items()}}

# A report a seller's application requests, answered at once from a prepared document.
def requested(store, rtype, name, text, start, end):
    rid = str(81000000000 + int(u("req", store, rtype) * 1e6))
    put(S, "report-files/" + name, text)
    data["requestable"]["%s|%s" % (store, rtype)] = {"reportId": rid, "reportType": rtype, "marketplaceIds": [store], "dataStartTime": start,
                                                     "dataEndTime": end, "processingStatus": "DONE",
                                                     "reportDocumentId": "amzn1.spdoc.1.4.na." + h(24, "rdoc", rid), "_file": name, "_gzip": False}


RCOLS = ["approval-date", "reimbursement-id", "case-id", "amazon-order-id", "reason", "sku", "fnsku", "asin", "product-name", "condition",
         "currency-unit", "amount-per-unit", "amount-total", "quantity-reimbursed-cash", "quantity-reimbursed-inventory",
         "quantity-reimbursed-total", "original-reimbursement-id", "original-reimbursement-type"]
rlines = ["\t".join(RCOLS)]
for appr, rid, case, reason, sku, qc, qi, per, orig, otype in REIMB:
    asin, title = PRODUCTS[US][sku][0], PRODUCTS[US][sku][1]
    rlines.append("\t".join([appr + "T14:40:00+00:00", rid, case, "", reason, sku, "X00FIX" + asin[-1] * 4, asin, title, "NewItem", "USD",
                             "%.2f" % per, "%.2f" % (per * qc), str(qc), str(qi), str(qc + qi), orig, otype]))
requested(US, "GET_FBA_REIMBURSEMENTS_DATA", "reimbursements-US.txt", "\n".join(rlines) + "\n", "2026-09-01T00:00:00Z", "2026-11-09T23:59:59Z")

STORAGE_EST = {  # month: {sku: (avg qty on hand, est volume cu ft, estimated monthly storage fee)}
    "2026-09": {"HL-FLEECE-GRY": (410, 287.0, 223.86), "HL-SHERPA-Q": (180, 216.0, 127.44), "HL-WEIGHTED-15": (95, 99.75, 58.55)},
    "2026-10": {"HL-FLEECE-GRY": (395, 276.5, 245.81), "HL-SHERPA-Q": (330, 396.0, 157.30), "HL-WEIGHTED-15": (88, 92.40, 64.15)},
}
SCOLS = ["asin", "fnsku", "product_name", "fulfillment_center", "country_code", "month_of_charge", "product_size_tier", "average_quantity_on_hand",
         "estimated_total_item_volume", "storage_rate", "currency", "estimated_monthly_storage_fee"]
slines = ["\t".join(SCOLS)]
for month, rows in STORAGE_EST.items():
    for sku, (q, vol, fee) in rows.items():
        asin = PRODUCTS[US][sku][0]
        slines.append("\t".join([asin, "X00FIX" + asin[-1] * 4, PRODUCTS[US][sku][1], "ALL", "US", month, "Large Standard", str(q), "%.2f" % vol,
                                 "%.4f" % (fee / vol), "USD", "%.2f" % fee]))
requested(US, "GET_FBA_STORAGE_FEE_CHARGES_DATA", "storage-fees-US.txt", "\n".join(slines) + "\n", "2026-09-01T00:00:00Z", "2026-10-31T23:59:59Z")

FCOLS = ["sku", "fnsku", "asin", "product-name", "product-group", "brand", "fulfilled-by", "your-price", "sales-price", "longest-side",
         "median-side", "shortest-side", "length-and-girth", "unit-of-dimension", "item-package-weight", "unit-of-weight", "product-size-tier",
         "currency", "estimated-fee-total", "estimated-referral-fee-per-unit", "expected-fulfillment-fee-per-unit"]
DIMS = {"HL-FLEECE-GRY": ("13.0", "10.2", "3.1", "29.4", "1.62"), "HL-SHERPA-Q": ("16.5", "13.0", "5.2", "52.9", "3.44"),
        "HL-WEIGHTED-15": ("18.1", "14.2", "6.3", "59.1", "15.70")}
flines = ["\t".join(FCOLS)]
for sku, (asin, title, price, pre, peak, _) in PRODUCTS[US].items():
    a, b, c, g, w = DIMS[sku]
    flines.append("\t".join([sku, "X00FIX" + asin[-1] * 4, asin, title, "Home", "Hearthly", "AMAZON_NA", "%.2f" % price, "%.2f" % price, a, b, c,
                             g, "inches", w, "pounds", "Large Standard", "USD", "%.2f" % (referral(price) + peak), "%.2f" % referral(price), "%.2f" % peak]))
requested(US, "GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA", "fee-preview-US.txt", "\n".join(flines) + "\n", "2026-11-07T00:00:00Z", "2026-11-07T23:59:59Z")

data["reports"] = REPORTS
data["restricted"] = ["GET_VAT_TRANSACTION_DATA", "SC_VAT_TAX_REPORT", "GET_FLAT_FILE_VAT_INVOICE_DATA_REPORT", "GET_XML_VAT_INVOICE_DATA_REPORT",
                      "FBA_BULK_INVOICE", "GET_FLAT_FILE_SALES_TAX_DATA", "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_TAX",
                      "GET_FLAT_FILE_ORDER_REPORT_DATA_TAX", "GET_FLAT_FILE_ORDERS_RECONCILIATION_DATA_TAX", "GET_ORDER_REPORT_DATA_TAX",
                      "GET_FLAT_FILE_ORDER_REPORT_DATA_INVOICING"]
put(S, "report-files/datakiosk-error.json", {"errorMessage": "stub: Access to the requested resource is denied. The application does not hold a role "
                                                             "required by one or more fields of this query."})
put(S, "data.json", data)

# ---------------------------------------------------------------------------------------------------------------------------
# The tree: replies landed by earlier sessions, one settlement document, the seller's notes


def fees_reply(store, asin, price, referral_fee, fba, when, vat=False):
    cur = STORES[store]["cur"]
    m = lambda x: {"CurrencyCode": cur, "Amount": r2(x)}
    rv, fv = (r2(referral_fee * VAT), r2(fba * VAT)) if vat else (0.0, 0.0)
    return {"payload": {"FeesEstimateResult": {
        "Status": "Success",
        "FeesEstimateIdentifier": {"MarketplaceId": store, "IdType": "ASIN", "SellerId": SELLER, "IdValue": asin, "IsAmazonFulfilled": True,
                                   "PriceToEstimateFees": {"ListingPrice": m(price), "Shipping": m(0.0)}, "SellerInputIdentifier": "fixture-%s-%s" % (asin, when[:10])},
        "FeesEstimate": {"TimeOfFeesEstimation": when, "TotalFeesEstimate": m(referral_fee + fba + rv + fv), "FeeDetailList": [
            {"FeeType": "ReferralFee", "FeeAmount": m(referral_fee), "FeePromotion": m(0.0), "TaxAmount": m(rv), "FinalFee": m(referral_fee + rv)},
            {"FeeType": "VariableClosingFee", "FeeAmount": m(0.0), "TaxAmount": m(0.0), "FinalFee": m(0.0)},
            {"FeeType": "PerItemFee", "FeeAmount": m(0.0), "TaxAmount": m(0.0), "FinalFee": m(0.0)},
            {"FeeType": "FBAFees", "FeeAmount": m(fba), "TaxAmount": m(fv), "FinalFee": m(fba + fv),
             "IncludedFeeDetailList": [{"FeeType": "FBAPerUnitFulfillmentFee", "FeeAmount": m(fba), "TaxAmount": m(fv), "FinalFee": m(fba + fv)}]}]},
        "Error": None}}}


put(T, "raw/amazon-sp-api/getMyFeesEstimateForASIN-B0FIXTURE5-2026-09-30.json", fees_reply(US, "B0FIXTURE5", 79.99, 12.00, 8.78, "2026-09-30T18:20:11Z"))


def group_v0(store, p, as_of):
    s = SETTLE[store][p["settlementId"]]
    cur = STORES[store]["cur"]
    closed = p["end"] <= as_of
    g = {"FinancialEventGroupId": p["groupId"], "ProcessingStatus": "Closed" if closed else "Open",
         "FundTransferStatus": "Succeeded" if closed and p["end"] + dt.timedelta(2) <= as_of else ("Processing" if closed else "Unknown"),
         "OriginalTotal": {"CurrencyCode": cur, "CurrencyAmount": s["total"] if closed else balances_at(store, as_of)["openBalance"]},
         "BeginningBalance": {"CurrencyCode": cur, "CurrencyAmount": p["prevReserve"]},
         "FinancialEventGroupStart": iso(p["start"])}
    if closed:
        g.update({"ConvertedTotal": {"CurrencyCode": cur, "CurrencyAmount": s["total"]}, "FinancialEventGroupEnd": iso(p["end"]),
                  "FundTransferDate": iso(p["end"] + dt.timedelta(2, hours=5)), "TraceId": p["traceId"], "AccountTail": STORES[store]["tail"]})
    return g


asof = at(D("2026-10-23"), 16)
put(T, "raw/amazon-sp-api/listFinancialEventGroups-ATVPDKIKX0DER-2026-10-23.json",
    {"payload": {"FinancialEventGroupList": [group_v0(US, p, asof) for p in PER[US] if p["start"] <= asof and p["start"] >= at(D("2026-08-11"))]}})

land = next(p for p in PER[US] if p["start"].date() == D("2026-10-06"))
rep = next(r for r in REPORTS if r["reportType"].startswith("GET_V2") and r["dataStartTime"] == iso(land["start"]) and r["marketplaceIds"] == [US])
d = "reports/GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2/%s_%s/1" % (US, land["settlementId"])
put(T, d + "/report.tsv", settlement_doc(US, land["settlementId"]))
put(T, d + "/receipt.json", {"reportId": rep["reportId"], "reportType": rep["reportType"], "processingStatus": "DONE", "createdTime": rep["createdTime"],
                             "reportDocumentId": rep["reportDocumentId"], "document": "report.tsv", "source": "getReports", "read": "2026-10-23T16:02:40Z"})

put(T, "notes/catalog.md", """# Hearthly (the seller's notes)

Company: Hearthly Home GmbH, Hamburg, Germany. VAT number DE999999999 (registered in Germany only). Sourcing office in Ningbo.
Amazon: Professional plan in both stores. All FBA. No Pan-European FBA: German stock is sold in Germany only.

| Store | SKU | ASIN | Product | Price |
|---|---|---|---|---|
| Amazon.com (US) | HL-FLEECE-GRY | B0FIXTURE1 | Fleece Throw 50x60, Grey | $29.99 |
| Amazon.com (US) | HL-SHERPA-Q | B0FIXTURE4 | Sherpa Blanket Queen 90x90, Navy | $59.99 |
| Amazon.com (US) | HL-WEIGHTED-15 | B0FIXTURE5 | Weighted Blanket 15 lb, 60x80 | $79.99 |
| Amazon.de (DE) | HL-FLEECE-GRY-DE | B0FIXTURE1 | Fleecedecke 127x152, Grau | 34,99 € |
| Amazon.de (DE) | HL-SHERPA-Q-DE | B0FIXTURE4 | Sherpa-Decke 230x230, Navy | 64,99 € |

Ads: Sponsored Products in the US only, paid by company credit card (Amex ...1009), not from the Amazon balance.

Bank accounts: US payouts go to the USD collection account ...4417; German payouts go to the EUR account at Hamburger
Sparkasse ...8820.

Our SP-API app's roles: Product Listing, Pricing, Brand Analytics, Finance and Accounting, Amazon Fulfillment.

Amazon email to the German store, 2026-09-24 (copied): "Starting October 1, 2026, funds for your orders will be available 14 days
after the delivery date (DD+14) while we are reviewing your account."

The accountant (Steuerberater, Frau Lenz) needs every settlement report from July to October 2026 for the annual close.
""")

put(T, "notes/costs.csv", """sku,store,batch,received,units_received,unit_cost,inbound_freight_per_unit,currency,note
HL-FLEECE-GRY,US,F-2605,2026-05-20,1200,6.90,0.50,USD,
HL-SHERPA-Q,US,S-2606,2026-06-25,420,16.20,1.30,USD,95 units of this batch were left at Amazon on 2026-10-01
HL-SHERPA-Q,US,S-2610,2026-10-16,250,18.40,1.60,USD,new supplier price + higher ocean freight
HL-WEIGHTED-15,US,W-2606,2026-06-28,300,20.50,1.50,USD,
HL-FLEECE-GRY-DE,DE,FD-2608,2026-08-10,400,6.40,0.95,EUR,
HL-SHERPA-Q-DE,DE,SD-2608,2026-08-10,200,15.10,1.80,EUR,
""")

bank = ["date,account,currency,amount,reference"]
for store in (US, DE):
    for p in PER[store]:
        if not p["closed"]:
            continue
        paid = (p["end"] + dt.timedelta(2)).date()
        arrive, left = paid, STORES[store]["bank_lag"]
        while left:
            arrive += dt.timedelta(1)
            left -= store == US or arrive.weekday() < 5
        if arrive >= D("2026-11-09"):
            continue
        s = SETTLE[store][p["settlementId"]]
        ref = ("AMAZON.COM SERVICES PAYOUT %s" % p["traceId"]) if store == US else ("AMAZON PAYMENTS EUROPE %s" % p["traceId"])
        bank.append("%s,%s,%s,%.2f,%s" % (arrive.isoformat(), "...4417" if store == US else "...8820", STORES[store]["cur"], s["total"], ref))
put(T, "notes/bank-deposits.csv", "\n".join(sorted(bank[1:], key=lambda x: x[:10]) and [bank[0]] + sorted(bank[1:])) + "\n")

# ---------------------------------------------------------------------------------------------------------------------------
# The graded figures

if SUMMARY:
    out = {}
    pu = {p["start"].date().isoformat(): p for p in PER[US]}
    pd = {p["start"].date().isoformat(): p for p in PER[DE]}
    oct_a, oct_b = at(D("2026-10-01")), at(D("2026-11-01"))

    b = balances_at(US, NOW)
    dfr = [r for r in TX[US] if r["kind"] == "order" and status_of(r) == "DEFERRED"]
    op = b["period"]
    last = SETTLE[US][pu["2026-10-20"]["settlementId"]]
    out["F1_us_now"] = {k: b[k] for k in ("AVAILABLE", "DEFERRED", "ACCOUNT_LEVEL_RESERVE", "RESERVED", "TOTAL")}
    out["F1_us_now"].update({"deferred_transactions": len(dfr), "first_maturity": iso(min(r["maturity"] for r in dfr)),
                             "last_maturity": iso(max(r["maturity"] for r in dfr)),
                             "deferred_maturing_before_open_period_end": r2(sum(r["total"] for r in dfr if r["maturity"] < op["end"])),
                             "expected_payout": {"amount": b["AVAILABLE"], "scheduledDate": iso(op["end"] + dt.timedelta(2)),
                                                 "period": [iso(op["start"]), iso(op["end"])]},
                             "open_period_released_by_kind": {k: r2(sum(r["total"] for r in TX[US] if r["kind"] == k and op["start"] <= r["release"] <= NOW))
                                                              for k in ("order", "refund", "storage")},
                             "open_group_balance": b["openBalance"], "last_payout": {"settlementId": last["period"]["settlementId"],
                                                                                    "amount": last["total"], "paid": iso(last["period"]["end"] + dt.timedelta(2, hours=5))}})
    bd_ = balances_at(DE, NOW)
    ddf = [r for r in TX[DE] if r["kind"] == "order" and status_of(r) == "DEFERRED"]
    p2 = SETTLE[DE][pd["2026-10-21"]["settlementId"]]
    sample = next(r for r in TX[DE] if r["kind"] == "order" and r["posted"].date() >= D("2026-10-20"))
    out["F2_de"] = {k: bd_[k] for k in ("AVAILABLE", "DEFERRED", "ACCOUNT_LEVEL_RESERVE", "RESERVED", "TOTAL")}
    out["F2_de"].update({"deferred_transactions": len(ddf), "last_payout": {"settlementId": p2["period"]["settlementId"], "amount": p2["total"],
                                                                         "PAID": iso(p2["period"]["end"] + dt.timedelta(2, hours=5)), "traceId": p2["period"]["traceId"]},
                         "last_bank_row_DE": [x for x in bank if "...8820" in x][-1],
                         "sample_order_2026-10-20": {"orderId": sample["orderId"], "delivered": sample["delivered"].isoformat(),
                                                     "maturityDate": iso(sample["maturity"]), "days_after_delivery": sample["dd"]},
                         "expected_payout": {"amount": bd_["AVAILABLE"], "scheduledDate": iso(bd_["period"]["end"] + dt.timedelta(2))}})

    def sums(rs, keys):
        acc = {}
        for r in rs:
            for k, v in r.get("lines", {}).items():
                if k in keys:
                    acc[k] = r2(acc.get(k, 0) + v)
        return acc

    octp = [r for r in TX[US] if oct_a <= r["posted"] < oct_b]
    orders_oct = [r for r in octp if r["kind"] == "order"]
    refunds_oct = [r for r in octp if r["kind"] == "refund"]
    fee_keys = ("Commission", "FBAPerUnitFulfillmentFee", "RefundCommission")
    acct = [r for r in octp if r["kind"] in ("storage", "subscription", "placement")]
    out["C1_us_october_fees"] = {
        "orders": {"count": len(orders_oct), **sums(orders_oct, ("Commission", "FBAPerUnitFulfillmentFee"))},
        "refunds": {"count": len(refunds_oct), **sums(refunds_oct, ("Commission", "RefundCommission"))},
        "account_level": [{"posted": iso(r["posted"]), "label": r["desc"], "amount": r["total"],
                           "covers": [iso(r["range"][0]), iso(r["range"][1])] if r.get("range") else None} for r in acct],
        "fees_and_charges_total": r2(sum(v for r in orders_oct + refunds_oct for k, v in r["lines"].items() if k in fee_keys) + sum(r["total"] for r in acct)),
        "per_order_fees_net": r2(sum(v for r in orders_oct + refunds_oct for k, v in r["lines"].items() if k in fee_keys)),
        "account_level_total": r2(sum(r["total"] for r in acct))}
    wo = sorted([r for r in TX[US] if r["kind"] == "order" and r["sku"] == "HL-WEIGHTED-15"], key=lambda r: r["posted"])
    pre, post = [r for r in wo if r["fba"] == 8.78], [r for r in wo if r["fba"] == 9.10]
    out["C2_weighted"] = {"last_878_shipped": iso(pre[-1]["posted"]), "first_910_shipped": iso(post[0]["posted"]),
                          "units_at_910_to_11-07": len(post), "step": r2(9.10 - 8.78), "extra_cost_to_11-07": r2(len(post) * 0.32),
                          "fee_preview": {"product-size-tier": "Large Standard", "item-package-weight": DIMS["HL-WEIGHTED-15"][4],
                                          "expected-fulfillment-fee-per-unit": PRODUCTS[US]["HL-WEIGHTED-15"][4]}}
    wref = [r for r in refunds_oct if r["sku"] == "HL-WEIGHTED-15"]
    if wref:
        r = wref[0]
        o = ORDERS[US][r["orderId"]]
        out["C3_refund"] = {"orderId": r["orderId"], "order_shipped": iso(o["posted"]), "refund_posted": iso(r["posted"]),
                            "lines": r["lines"], "total": r["total"], "fba_fee_on_order": o["fba"], "commission_on_order": o["comm"],
                            "weighted_refunds_posted_october": len(wref), "seller_cost_in_amazon_charges": r2(-r["lines"]["RefundCommission"] + o["fba"])}
    out["R1_reimbursements"] = {"rows": [{"approval": a, "id": i, "reason": rs, "sku": s, "cash_qty": qc, "inventory_qty": qi, "per_unit": pu_,
                                          "amount_total": r2(pu_ * qc), "original": o} for a, i, c, rs, s, qc, qi, pu_, o, t in REIMB],
                                "sherpa_batches_unit_cost": {"S-2606": 16.20, "S-2610": 18.40},
                                "cash_total": r2(sum(pu_ * qc for a, i, c, rs, s, qc, qi, pu_, o, t in REIMB)),
                                "transactions_total": r2(sum(r["total"] for r in TX[US] if r["kind"] == "reimbursement"))}
    allref = [r for r in TX[US] if r["kind"] == "refund"]
    by_post = [r for r in allref if oct_a <= r["posted"] < oct_b]
    by_order = [r for r in allref if D("2026-10-01") <= (r["orderCreated"] - dt.timedelta(hours=7)).date() <= D("2026-10-31")]
    out["R2_refunds"] = {"posted_in_october": {"count": len(by_post), "principal": r2(sum(r["lines"]["Principal"] for r in by_post)),
                                               "net_money": r2(sum(r["total"] for r in by_post))},
                         "for_orders_created_in_october_pacific": {"count": len(by_order), "principal": r2(sum(r["lines"]["Principal"] for r in by_order)),
                                                                    "posted_in_november": len([r for r in by_order if r["posted"] >= oct_b])},
                         "refunds_posted_october_for_september_orders": len([r for r in by_post if (r["orderCreated"] - dt.timedelta(hours=7)).date() < D("2026-10-01")])}

    def product_oct(sku):
        o = [r for r in orders_oct if r["sku"] == sku]
        rf = [r for r in refunds_oct if r["sku"] == sku]
        rb = [r for r in octp if r["kind"] == "reimbursement" and r["sku"] == sku]
        principal = r2(sum(r["lines"]["Principal"] for r in o))
        fees = r2(sum(v for r in o for k, v in r["lines"].items() if k in fee_keys))
        refund_net = r2(sum(r["lines"]["Principal"] + r["lines"]["Commission"] + r["lines"]["RefundCommission"] for r in rf))
        reimb = r2(sum(r["total"] for r in rb))
        return {"units_shipped": len(o), "principal": principal, "amazon_fees": fees, "refunds_net": refund_net, "refund_count": len(rf),
                "reimbursements": reimb, "before_cost": r2(principal + fees + refund_net + reimb),
                "shipped_before_10-16": len([r for r in o if r["posted"].date() < D("2026-10-16")])}

    sq = product_oct("HL-SHERPA-Q")
    n, early = sq["units_shipped"], sq["shipped_before_10-16"]
    old_left_1016 = 95 - early
    avg_1016 = r2((old_left_1016 * 17.50 + 250 * 20.00) / (old_left_1016 + 250))
    cost_date = r2(early * 17.50 + (n - early) * 20.00)
    cost_fifo = r2(n * 17.50) if n <= 95 else None
    cost_avg = r2(early * 17.50 + (n - early) * avg_1016)
    out["P1_sherpa_october"] = dict(sq, landed_unit_cost={"S-2606": 17.50, "S-2610 from 2026-10-16": 20.00}, cost={"by_ship_date": cost_date, "fifo": cost_fifo, "moving_average_from_10-16": cost_avg,
                                              "avg_unit_cost_from_10-16": avg_1016, "old_batch_left_at_10-16": old_left_1016},
                                    profit_before_account_level={"by_ship_date": r2(sq["before_cost"] - cost_date),
                                                                 "fifo": r2(sq["before_cost"] - cost_fifo) if cost_fifo is not None else None,
                                                                 "moving_average": r2(sq["before_cost"] - cost_avg)})
    unit_cost = {"HL-FLEECE-GRY": 7.40, "HL-WEIGHTED-15": 22.00}
    per = {}
    for sku in PRODUCTS[US]:
        pr = product_oct(sku)
        c = cost_fifo if sku == "HL-SHERPA-Q" else r2(pr["units_shipped"] * unit_cost[sku])
        per[sku] = dict(pr, cost_fifo=c, contribution=r2(pr["before_cost"] - c))
    acct_total = -out["C1_us_october_fees"]["account_level_total"]
    tot_sales = sum(v["principal"] for v in per.values())
    tot_units = sum(v["units_shipped"] for v in per.values())
    sep = STORAGE_EST["2026-09"]
    sep_tot = sum(x[2] for x in sep.values())
    for sku, v in per.items():
        v["account_level_share"] = {"by_sales": r2(acct_total * v["principal"] / tot_sales), "by_units": r2(acct_total * v["units_shipped"] / tot_units)}
        v["storage_estimate_sep"] = sep[sku][2]
        v["after_spread_by_sales"] = r2(v["contribution"] - v["account_level_share"]["by_sales"])
        v["after_spread_by_units"] = r2(v["contribution"] - v["account_level_share"]["by_units"])
    out["P2_all_october"] = {"per_sku": per, "account_level_posted_october": acct_total,
                             "storage_posted_2026-10-08_for_september": 412.37, "storage_estimate_september_sum": r2(sep_tot),
                             "contribution_total": r2(sum(v["contribution"] for v in per.values())),
                             "after_account_level_total": r2(sum(v["contribution"] for v in per.values()) - acct_total)}

    s1 = SETTLE[US][pu["2026-10-20"]["settlementId"]]
    p1 = s1["period"]
    cat = {}
    for r in s1["rows"]:
        for k, v in (r.get("lines") or {r["settleDesc"]: r["total"]}).items():
            key = ("%s %s" % (r["kind"], k)) if r["kind"] in ("order", "refund") else r["settleDesc"]
            cat[key] = r2(cat.get(key, 0) + v)
    out["S1_us_settlement_1020"] = {"settlementId": p1["settlementId"], "groupId": p1["groupId"], "total": s1["total"],
                                    "deposit": iso(p1["end"] + dt.timedelta(2)), "by_line": cat,
                                    "previous_reserve": p1["prevReserve"], "current_reserve": p1["curReserve"],
                                    "orders_released": len([r for r in s1["rows"] if r["kind"] == "order"]),
                                    "orders_released_shipped_before_period": len([r for r in s1["rows"] if r["kind"] == "order" and r["posted"] < p1["start"]]),
                                    "orders_shipped_in_period_still_deferred": len([r for r in TX[US] if r["kind"] == "order" and p1["start"] <= r["posted"] < p1["end"] and r["maturity"] >= p1["end"]]),
                                    "group_transactions_sum": s1["txsum"], "group_minus_total": r2(s1["txsum"] - s1["total"]),
                                    "bank_row": [x for x in bank if p1["traceId"] in x]}
    s2 = SETTLE[DE][pd["2026-10-07"]["settlementId"]]
    out["S2_de_settlement_1007"] = {"settlementId": s2["period"]["settlementId"], "total": s2["total"], "total_as_written": num(DE, s2["total"]),
                                    "comma_dropped_reads": int(num(DE, s2["total"]).replace(",", "")), "rows": len(settlement_doc(DE, s2["period"]["settlementId"]).splitlines()) - 2,
                                    "previous_reserve": s2["period"]["prevReserve"], "current_reserve": s2["period"]["curReserve"],
                                    "bank_row": [x for x in bank if s2["period"]["traceId"] in x],
                                    "principal": r2(sum(r["lines"]["Principal"] for r in s2["rows"] if r["kind"] in ("order", "refund"))),
                                    "account_level": {r["settleDesc"]: r["total"] for r in s2["rows"] if r["kind"] in ("storage", "subscription")}}
    paid_oct = [p for p in PER[US] if p["closed"] and D("2026-10-01") <= (p["end"] + dt.timedelta(2)).date() <= D("2026-10-31")]
    pac = lambda r: (r["created"] - dt.timedelta(hours=7)).date()
    oct_orders_local = [r for r in TX[US] if r["kind"] == "order" and D("2026-10-01") <= pac(r) <= D("2026-10-31")]
    s1_posted_oct = [r for r in s1["rows"] if r["posted"] < oct_b]
    out["S3_us_october_close"] = {"payouts_paid_in_october": [{"period": [iso(p["start"]), iso(p["end"])], "amount": SETTLE[US][p["settlementId"]]["total"]} for p in paid_oct],
                                  "deposits_october_total": r2(sum(SETTLE[US][p["settlementId"]]["total"] for p in paid_oct)),
                                  "ordered_product_sales_october_pacific": {"units": len(oct_orders_local), "totalSales": r2(sum(r["price"] for r in oct_orders_local))},
                                  "deferred_asof_2026-09-30": balances_at(US, at(D("2026-10-01")) - dt.timedelta(seconds=1))["DEFERRED"],
                                  "deferred_asof_2026-10-31": balances_at(US, oct_b - dt.timedelta(seconds=1))["DEFERRED"],
                                  "settlement_1020_1103_lines_posted_october": r2(sum(r["total"] for r in s1_posted_oct)),
                                  "settlement_1020_1103_lines_posted_november": r2(sum(r["total"] for r in s1["rows"] if r["posted"] >= oct_b))}
    dsamp = next(r for r in TX[DE] if r["kind"] == "order" and r["sku"] == "HL-FLEECE-GRY-DE" and r["posted"].date() >= D("2026-10-15"))
    out["T1_de_vat"] = {"prices": {k: v[2] for k, v in PRODUCTS[DE].items()}, "fleece_order": dsamp["orderId"], "fleece_fees": {k: {"total": v, "base_and_vat": dsamp["feeVat"].get(k)} for k, v in dsamp["lines"].items() if k != "Principal"},
                        "sherpa_fees": {"Commission": [-9.75, -1.85], "FBAPerUnitFulfillmentFee": [-6.30, -1.20]},
                        "vat_share_of_fees": round(1.00 / 5.25, 4),
                        "subscription": {"base": -39.0, "vat": -7.41}, "storage_sep": {"base": -35.0, "vat": -6.65},
                        "fee_vat_posted_october": r2(sum(v[1] for r in TX[DE] if oct_a <= r["posted"] < oct_b for v in (list(r.get("feeVat", {}).values()) + ([r["vat"]] if r.get("vat") else []))))}
    taxes = sums(s1["rows"], ("Tax", "MarketplaceFacilitatorTax-Principal"))
    out["T2_us_tax_settlement_1020"] = dict(taxes, net=r2(sum(taxes.values())))
    listed = [r for r in REPORTS if r["marketplaceIds"] == [US] and dt.datetime.fromisoformat(r["createdTime"].replace("Z", "+00:00")) >= NOW - dt.timedelta(90)]
    out["M1_settlements"] = {"listed_by_getReports": [[r["dataStartTime"][:10], r["dataEndTime"][:10], r["reportId"]] for r in sorted(listed, key=lambda r: r["dataStartTime"])],
                             "not_listed": [[iso(p["start"])[:10], iso(p["end"])[:10], p["settlementId"], SETTLE[US][p["settlementId"]]["total"]]
                                            for p in PER[US] if p["closed"] and not any(r["dataStartTime"] == iso(p["start"]) for r in listed)]}
    out["M2"] = {"settlement_1020": p1["settlementId"], "group_1020": p1["groupId"], "group_transactions": len(s1["rows"]),
                 "deferred_now": {"count": len(dfr), "sum": b["DEFERRED"]}}
    print(json.dumps(out, indent=1, default=str))
else:
    print(T)
