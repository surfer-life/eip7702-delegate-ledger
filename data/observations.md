# Hand observations

Things I looked at by hand that the daily pipeline does not capture. Each entry says what I sampled and what I did not check. These do not change a contract's grade.

## 2026-11-15 — `0x67b743f3642f7cc863c823c6708708d039f65be2` (unverified, 1,302 authorizations in the day, one sender, 98% nonce-0 accounts)

Sample: 4 accounts delegated to it (`0x2ec5a6f3…c2e5`, `0x30ff30d5…0c08`, `0x71898708…0f95`, `0x839a54fe…6b97`), token-transfer history from Blockscout.

What each of the four showed:
- zero transactions of their own
- real USDC dust in and out (0.0005 and 0.002001 USDC) and zero-value USDC transfers
- large "incoming" transfers (5,000 to 161,450) of tokens whose symbol is spelled `ÚЅDС` with look-alike letters, issued by contracts that are not USDC

That is the address-poisoning pattern. Its bytecode is not a copy of the exposed `Poisoner` contract (33% similar, different function selectors, one of which is `a9059cbb` = `transfer`), so it looks like a separate implementation used the same way.

Not checked: who controls it, whether anyone lost money to these four addresses, and whether every account delegated to it behaves like this. Four accounts is a small sample.

## 2026-11-15 — What do accounts delegated to unverified targets actually do? (a first, rough pass)

Why: a third of authorizations go to targets with no published source. The grade says only that nobody can read the code. I wanted to see behaviour instead.

Sample: 300 recent blocks; 25 targets that were unverified or not yet in the ledger; up to 3 delegating accounts each (58 accounts); ERC-20 transfer history from Blockscout.

Before looking I wrote down a guess: about 30% of these targets would be address-poisoning farms. That was wrong.

What a rule-based sort gave (majority behaviour per target): poisoning 1, no trace at all 2, long-lived active accounts 6, **everything else 16**. Two thirds landing in "everything else" meant my rules were too coarse, so I read accounts by hand.

What reading by hand showed, for 14 targets whose delegating accounts have no transactions of their own but tokens going in and out:

- **Swapping through a DEX** (tokens to and from Uniswap v4 `PoolManager`, a Uniswap v3 pool, the 1inch router): 3 or 4 targets. These look like gasless-swap wallets or trading bots.
- **Mint and burn** (in from and out to the zero address): 1 target.
- **Collection into one wallet** (several delegating accounts each receive a token and send it on to the same single address): at least 2 targets (e.g. three accounts → `0x48f9bE7A…0333`). From the outside this is what both an exchange sweeping deposit addresses and a thief sweeping compromised wallets look like. I could not tell which.
- **Loops with a contract the explorer flags as scam**: 1 target (`0x490aac77…ca1d`, both in and out via `0x08eC0883…31a7`).
- **Scattered**: the rest send to different unnamed wallets with no obvious pattern in 3 accounts.

What I take from it: "unverified" covers very different things: trading tools, token mechanics, collection schemes and scams. It is not a synonym for malicious, and a ledger that hinted otherwise would be misleading people. Telling the collection schemes apart (deposit sweeping vs theft) is the open question, and three accounts per target is too few to answer it.

Not checked: ETH flows for most accounts, who controls any of the collecting wallets, and whether these 25 targets are representative.

## 2026-11-15 — The shape of the authorizations does not tell you intent

I hoped two cheap numbers from the ledger would separate good from bad: how many senders submit the authorizations for a target, and how many of the delegating accounts are brand new (authorization nonce 0). They do not. In the day ending 2026-11-15 02:44 UTC, among targets with one sender and at least 100 authorizations:

| | mostly existing accounts (nonce-0 share near 0) | mostly fresh accounts (nonce-0 share near 1) |
|---|---|---|
| **known bad** | `CrimeEnjoyor` (1,729 authorizations, 0% nonce 0): a sweeper put on wallets that already had a history | a Blockscout-flagged target (1,055, 100%); `Poisoner` is mixed (6,188, 54%) |
| **known fine** | `Tangem7702GaslessExecutorL1` (1,409, 12%): a hardware-wallet vendor's verified gasless executor, one relayer | none confirmed. Candidates are the collection schemes above, if they turn out to be deposit sweeping |
| **unknown** | six unverified targets (172 to 1,855 authorizations, 0–11%) | six unverified targets (129 to 1,276, 96–100%) |

So "one relayer, existing accounts" is what both a wallet vendor sponsoring gas for its users and a drainer look like, and "one relayer, fresh accounts" is what both a poisoning farm and (possibly) a deposit-address scheme look like. The ledger keeps reporting these numbers because they are facts, but the note on a row describes a shape, not a verdict.

## 2026-11-15 — Cross-check against a published dataset, and a "verified" contract that is a sweeper

Huang et al. (USENIX Security 2026) published their detection results ([Zenodo 17895541](https://zenodo.org/records/17895541), CC-BY-4.0; data up to 2025-07-15, seven chains). I extracted the 718 delegation targets they marked as malicious for EOA-targeted attacks (`data/reference/huang2026_eoa_targeted.json`) and compared them with the 176 targets in the day ending 2026-11-15 02:44 UTC.

- **3 of my 176 targets are in their malicious list.** 19 more appear in their data without a malicious mark. 154 are not in their data at all: most of today's targets did not exist, or were not used, sixteen months ago.
- `CrimeEnjoyor` (0x84d0…1f40): flagged by them on Ethereum; already `known-malicious` here. Agreement.
- **`Porwarder` (0xb6da1852…b2a8): flagged by them on Ethereum; this ledger had it as `verified-source`.** I read the verified source. It is fifteen lines: a public `initialize(destination)` with no access control, and a `receive()` that forwards any incoming ETH to `destination`. That is the forward-on-receive pattern their paper describes, and it shows concretely why `verified-source` is not a safety grade: the code is published, and what it publishes is a sweeper. It now carries the grade `flagged-by-research`.
- `EIP7702Proxy` (0x7702cb55…176c), which Walletbeat lists as Coinbase's EIP-7702 proxy: they marked it on Base and Optimism, not on Ethereum. I have not checked what code sits at that address on those chains or why their detector matched it, so here it stays `verified-source` with a note recording the disagreement.

A mistake I caught before publishing: my first pass pulled every address out of their spreadsheet `sa_contract_malicious.xlsx` and treated all 2,320 as malicious, which "found" 22 matches including MetaMask's delegator. The file lists all delegation targets with a `matched` / `unmatched` column; only `matched` rows are their detections. The absurd result is what made me open the columns.

## 2026-11-15 — Reading the "verified" sources for forward-on-receive

After `Porwarder` I ran a text filter over the published source of all 62 verified targets in the day's ledger, looking for a `receive()` or `fallback()` that sends the incoming ETH somewhere, and read every hit.

- `Porwarder` (0xb6da1852…b2a8): as above.
- **`Reconstructed` (0x3ae1f70c…2d10, 6 authorizations, source verified 2026-11-05).** It looks like a small wallet: `execute(calls, signature)` checks a signature from the account itself. But it also has `forwardAllEth()`, `forwardTokens(token)` and `forwardMultipleTokens(tokens)`, all `external` with no access check, that send the account's whole ETH or token balance to a hard-coded address `0x43b18F8f…AAAA`, and its `receive()` and `fallback()` forward incoming ETH to the same address. So anyone can empty an account delegated to it, and the money can only go to one place. The contract name suggests someone reconstructed it from bytecode and published the source.
- `MASW` (0x50055dc4…7896): **a false positive of my filter**, caught by reading. The words "receive() or fallback()" appear in a code comment of a test helper bundled in the verified sources; the wallet's real `receive()` is empty. The filter now strips comments and only matches function definitions. I am leaving this entry here because the first version of the filter would have published a wrong label.

Both real hits now carry the grade `verified-forwarder` (`Porwarder` keeps `flagged-by-research`, which it also has). The filter only sees this one pattern in published Solidity; a verified contract can drain an account in other ways and not be caught, and an honest forwarder would be caught too. It is a reason to read the source, not a verdict.
