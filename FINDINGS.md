# Field notes: what the ledger surfaced (2026-11-15)

These are findings I reached with the tools in this repo — every number is reproducible from public RPC, and I separate what I **checked** from what I only **suspect**.

## 1. Authorizations are not victims — a tug of war inflates the headline

Counting EIP-7702 "authorizations" overstates the problem. I recovered the *signer* of every authorization in a day (`scripts/authority.py`, pure-Python secp256k1) and found that a few hundred accounts are **re-delegated back and forth between competing sweeper contracts**, many times an hour.

- 24h window: **37,883 authorizations from only 20,618 distinct accounts.**
- **366** of those accounts signed for more than one target and produced **~36% of all authorizations.**
- In a tighter 1-hour sample, two sweepers (`0x8a67…` and CrimeEnjoyor-like `0x8332…`) traded the same 38 accounts; one reclaims in ~1 block, the other in ~7; each account flips 56–58 times/hour.

So "X% of 7702 delegations are scams" mostly counts *that contest*, not victims. The ledger now reports **distinct accounts** next to authorizations. (Checked.)

## 2. "Does ETH sent here get swept?" — don't guess, simulate

For the question a user actually cares about, the ledger doesn't read code — it has a node **dry-run** a 1-wei transfer (`eth_simulateV1`, nothing sent) and watches where the ETH goes. In the latest day, **~18–26%** of authorizations point at contracts that forward incoming ETH straight to a collector in the same transaction. Verified against known accounts: a CrimeEnjoyor look-alike forwards to `0x63a3aaba…`. (Checked.)

## 3. Anatomy of one operation (traced, with one labelled hop)

Hand-disassembling the 3rd-largest *unverified* target `0x8a67b502…408a` (717 bytes) showed a hand-written sweeper: empty calldata forwards received ETH to `0xcc04506d…3b95`; a `msg.value` opcode selects which asset to sweep; an `onERC721Received` hook forwards NFTs; one backdoor gated on `tx.origin == 0x963819…14af`.

Following the money on Etherscan:
- Collector `0xcc04…` was **funded by an address Etherscan labels as a FixedFloat deposit address** ~~(a no-KYC instant exchange commonly used for laundering) and itself runs **address-poisoning** (fake "ETH" unicode-lookalike token dust to look-alike addresses)~~. *(Struck 2026-11-16 — see Corrections 1 and 2 below.)*
- Operator `0x963819…14af` was **funded via the Across bridge** ~~and operates across ~7 chains; its recent outflow just **re-funds the sweeper fleet's gas** (`0x3ad10f14…`, `0x80ed97ff…`). The operation largely **pays its own gas war from the proceeds.**~~ *(Struck 2026-11-16 — see Corrections 3 and 4 below.)*

Suspected, not proven: that the collector/operator are one actor ~~(same poison-dust pattern, look-alike destinations)~~ *(that argument is withdrawn, Correction 1; what remains is the `tx.origin` gate in the sweeper code and one 0.25 ETH transfer from collector to operator)* and that the real cash-out leaves Ethereum via the bridge / FixedFloat rather than a labelled exchange deposit.

Check the forward yourself, live, no wallet: [the browser tool runs the same 1-wei dry run on `0x8a67…`](https://surfer-life.github.io/eip7702-delegate-ledger/?address=0x8a67b5020ee254ef48e3b6a04927f39baf7e408a) and shows the ETH leaving to `0xcc04…` in the same transaction.

## 4. Some contested accounts have publicly derivable keys

Three of the contested accounts are addresses of keys **anyone can compute**: indexes 31 and 88 of the textbook `abandon … about` mnemonic, and the key `sha256("ethereum")`. They are empty honeypots — fund one and it is swept in the same block. (Checked by deriving the keys and comparing addresses; I did nothing with the keys. *Added 2026-11-16: "swept in the same block" comes from the dry-run simulation; I never sent real funds to see it — Correction 5.*)

---

## Corrections (2026-11-16)

I re-read this file against my own raw logs and found statements in the "checked" part of section 3 that I had not checked. I am striking them rather than deleting them.

1. **"The collector itself runs address-poisoning" — withdrawn; the evidence points the other way.** The fake "ETH" look-alike-token transfers do show `0xcc04506d…3b95` in the `from` field, but a token contract can put any address in that field. I opened the transactions behind 12 of the 42 such transfers on the first page of its Blockscout token-transfer history (2026-11-09 … 11-15): **none was sent by `0xcc04…`**. They were sent by six other EOAs (`0x8b27bb23…`, `0x5565f176…`, `0xba1d7201…`, `0x1584a8ee…`, `0x20d13237…`, `0xfb94da13…`) through three contracts (`0x61f0fda3…`, `0x129b898c…`, `0x77eb52e4…`). The fake recipients are look-alikes of `0xcc04…` itself (`0xCc04070D…`, `0xcC0dD40f…`, `0xcC046179…`) and of the operator (`0x96388408…`, `0x9638E677…`), and two use the amount 0.25 — the size of a real transfer from collector to operator. That is the shape of someone poisoning the collector's history, i.e. `0xcc04…` looks like a **target**. I have not checked who controls those six senders, and I only opened 12 of 42.
2. **"FixedFloat … commonly used for laundering" — not something I checked.** That was from my memory. What I saw is an Etherscan label on the funding address.
3. **"Operates across ~7 chains" — not established.** All I saw was one Etherscan line, "7 addresses found via Blockscan". I did not look at activity on any other chain.
4. **"Its recent outflow re-funds the sweeper fleet's gas … pays its own gas war from the proceeds" — overstated.** Re-checked today, the operator's last 50 outgoing transactions (2026-11-08 … 11-15): 44 go to `0x3ad10f14…` carrying about 29 wei each (1,276 wei in total — calls, not gas funding); 3 go to `0x80ed97ff…` totalling 0.105 ETH; 2 to `0x31bf3c27…` (~0.0005 ETH). I have not verified that `0x80ed97ff…` is a sweeper sender. The "pays its own gas war" sentence was an interpretation stacked on one 0.25 ETH transfer and those small ones.
5. **Section 4, "fund one and it is swept in the same block"** is what the simulation shows. I did not send funds.

Posts that repeated these claims (X threads linked from this repo) get a reply pointing here.

---

Limits, kept honest: a window is not a census; counts include invalid authorizations; grades describe evidence, not intent; nothing here is audited by me; not security advice. Corrections live in the README.
