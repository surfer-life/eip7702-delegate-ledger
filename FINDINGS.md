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
- Collector `0xcc04…` was **funded by a FixedFloat deposit address** (a no-KYC instant exchange commonly used for laundering) and itself runs **address-poisoning** (fake "ETH" unicode-lookalike token dust to look-alike addresses).
- Operator `0x963819…14af` was **funded via the Across bridge** and operates across ~7 chains; its recent outflow just **re-funds the sweeper fleet's gas** (`0x3ad10f14…`, `0x80ed97ff…`). The operation largely **pays its own gas war from the proceeds.**

Suspected, not proven: that the collector/operator are one actor (same poison-dust pattern, look-alike destinations) and that the real cash-out leaves Ethereum via the bridge / FixedFloat rather than a labelled exchange deposit.

Check the forward yourself, live, no wallet: [the browser tool runs the same 1-wei dry run on `0x8a67…`](https://surfer-life.github.io/eip7702-delegate-ledger/?address=0x8a67b5020ee254ef48e3b6a04927f39baf7e408a) and shows the ETH leaving to `0xcc04…` in the same transaction.

## 4. Some contested accounts have publicly derivable keys

Three of the contested accounts are addresses of keys **anyone can compute**: indexes 31 and 88 of the textbook `abandon … about` mnemonic, and the key `sha256("ethereum")`. They are empty honeypots — fund one and it is swept in the same block. (Checked by deriving the keys and comparing addresses; I did nothing with the keys.)

---

Limits, kept honest: a window is not a census; counts include invalid authorizations; grades describe evidence, not intent; nothing here is audited by me; not security advice. Corrections live in the README.
