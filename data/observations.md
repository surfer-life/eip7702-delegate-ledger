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
