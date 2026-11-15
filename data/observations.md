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
