# Changelog

## 0.1.4

- The tile's mark on the Plugins page is the signed drawing.

## 0.1.3

- Each template's body is its description, word for word, then the seller's own words: `money-where`, `fees-review`, `product-earnings`, `settlement-check` and `refunds-review`. Typing `/money-where` sends "See where my Amazon money is now and when the next payout is due."; typing `/money-where 只看欧洲站` sends that sentence, then 「只看欧洲站」.

## 0.1.2

- The README no longer names another plugin; what the playbook builds on is its `comchatx.builds`, each with its reason, as signed on 2026-11-18. The sentence "To see what holding stock costs and when to restock, also install [Amazon Stock Playbook](…)." and its Chinese are gone; `@comchatx/cx-amazon-stock-playbook` is an optional entry with the reason 「用于看清库存压着要花多少钱、什么时候该补货。」 / "Shows stock costs and when to restock."
- "What it uses" names the account, not the plugin: 「**你的亚马逊卖家账户**：cx 在这里读取交易、结算、回款和费用。」 / "**Your Amazon seller account:** cx reads your transactions, settlements, payouts and fees there." Its Amazon Ads line is gone; the `@comchatx/cx-amazon-ads` entry carries the reason 「用于补上亚马逊读不到的单品广告花费。」 / "Fills in each product's ad spend Amazon leaves out."
- `cx-amazon-seller` is a new optional entry, with the reason 「用于让 cx 从第一条消息起就知道你在亚马逊开店。」 / "Tells cx from the start that you sell on Amazon."
- Three templates' English reads as the seller's own message, as signed on 2026-11-17: `money-where`, `product-earnings` and `settlement-check` say "my" where they said "your". Their Chinese, and the other two templates, stay.

## 0.1.1

- The card's name is the one signed on 2026-11-17: "Amazon Finance Playbook" on the English page (`comchatx.name`) and 「亚马逊财务分析手册」 on the Chinese page (`comchatx.nameZh`).
- The README, in English and Chinese, calls each plugin of ours it names by the card's name signed on 2026-11-17.
- The README names each other plugin it speaks of by the card's name in its own language, a link to that plugin's page on npm, never by the npm name.

## 0.1.0

- Seven skills on a seller's Amazon money, read through `cx-amazon-sp-api`: `money-flow`, `fees-and-charges`, `refunds-and-reimbursements`, `product-earnings`, `settlement-reconcile`, `tax-lines` and `money-reads`, each line citing the research position it rests on.
- Five templates: `/money-where`, `/fees-review`, `/product-earnings`, `/settlement-check` and `/refunds-review`.
- The research: 430 positions in nine files under `research/`.
