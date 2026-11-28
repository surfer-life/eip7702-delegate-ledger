# Latest window

Blocks 26503515–26510714 (2026-11-27T02:19:59Z to 2026-11-28T02:24:59Z): 28628 type-4 transactions, 71051 authorizations, 401 targets.

Share of authorizations by grade: **forwards-incoming-eth** 27.1%, **unverified-source** 19.9%, **resembles-known-malicious** 18.7%, **verified-source** 18.2%, **known-malicious** 12.2%, **flagged-by-research** 2.7%, **evidence-missing** 0.6%, **no-code** 0.5%, **verified-but-upgradeable** 0.0%, **verified-forwarder** 0.0%

Signed by 27478 distinct accounts. 2714 of them signed for more than one target in the window and produced 39301 of the authorizations. Share of account–target pairs by grade: **verified-source** 38.6%, **unverified-source** 29.8%, **known-malicious** 13.8%, **forwards-incoming-eth** 11.4%, **resembles-known-malicious** 4.8%, **evidence-missing** 0.8%, **no-code** 0.7%, **verified-but-upgradeable** 0.0%, **flagged-by-research** 0.0%, **verified-forwarder** 0.0%

| grade | delegate | name | authorizations | accounts | senders | nonce 0 | notes |
|---|---|---|---:|---:|---:|---:|---|
| forwards-incoming-eth | `0x8a67b5020ee254ef48e3b6a04927f39baf7e408a` |  | 14961 | 914 | 6 | 0% | 913 of the 914 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xcc04506d439d338bde8ebbb074f17a54b7673b95. |
| resembles-known-malicious | `0x8332a5c2f00ab7e20c53210be2192aea7bdc77f0` |  | 13269 | 1520 | 2 | 0% | Unverified, but its bytecode is 92% similar to CrimeEnjoyor (0x84d05511614272694d3a9cebe896514dbde51f40) and exposes the same function selectors. 1520 of the 1520 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| known-malicious | `0xe6b97aa1490c93c28a14d86c13c9dc9c950643ed` | Poisoner | 7208 | 2841 | 1 | 40% | Verified source on Blockscout carries a comment saying this is a scam contract recreated and exposed by Wintermute. |
| unverified-source | `0x7bafbc8c81159fddf5e1b825d7ba88de0007e40a` |  | 3777 | 3407 | 1 | 91% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| unverified-source | `0x2e623468c560072e91d7a94a1dcb2eefbdbe69cb` |  | 3545 | 399 | 1 | 10% | 399 of the 399 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| flagged-by-research | `0x84d05511614272694d3a9cebe896514dbde51f40` | CrimeEnjoyor | 1870 | 2 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 2 of 2 sampled accounts delegated here was passed straight on to 0x333333320bb4a0345a7a102c49c72b37647aa088. In 2 of those, the receiving address is written in the delegated account's own storage slot 0, so each account can carry its own payout address. Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact. Verified on Blockscout but not found on Sourcify. |
| verified-source | `0xd2e28229f6f2c235e57de2ebc727025a1d0530fb` | Biz | 1863 | 1845 | 20 | 77% | 2 of the 1845 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x34fff33dc9c0ead473a1878923b3858d8ed04dfb` |  | 1829 | 1425 | 1 | 12% |  |
| verified-source | `0x0000fb7702036ff9f76044a501ac1aa74cbab16b` | UniversalGaslessDelegate | 1692 | 1609 | 65 | 85% |  |
| unverified-source | `0x5dfbdb4212812a54d600d0de0b258ebc2034fc2e` |  | 1639 | 1569 | 1 | 0% | 1324 of the 1569 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| forwards-incoming-eth | `0xc11e9f54ce559011cb8e04a51f1876c735482152` |  | 1625 | 1625 | 1 | 69% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. 760 of the 1625 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xf152bba5fd127f7a8b3ebbfcd335bd86317de405. |
| known-malicious | `0xc43b6c6a43e5760a756a67756b2155c7fa735310` |  | 1493 | 1493 | 1 | 100% | Flagged as scam by Blockscout. Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0x67b743f3642f7cc863c823c6708708d039f65be2` | PackedPayoutWallet | 1364 | 1364 | 1 | 98% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0xe6cae83bde06e4c305530e199d7217f42808555b` | Simple7702Account | 1036 | 1020 | 31 | 96% | 1 of the 1020 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x293b175e89458db63c0e47d650ea4640b16d3792` |  | 1000 | 99 | 1 | 0% | 13 of the 99 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x4687239ed32da83ee49bd783094c80cea0a320d4. |
| verified-source | `0xb94b392b61c16ddb7118849d4970570c07f75dd1` | Tangem7702GaslessExecutorL1 | 943 | 539 | 1 | 11% |  |
| verified-source | `0x63c0c19a282a1b52b07dd5a65b58948a07dae32b` | EIP7702StatelessDeleGator | 846 | 821 | 404 | 18% | 25 of the 821 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| verified-source | `0x69007702764179f14f51cdce752f4f775d74e139` | SemiModularAccount7702 | 754 | 753 | 25 | 50% | 8 of the 753 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| verified-source | `0x000000009b1d0af20d8c6d0a44e162d11f9b8f00` | CaliburEntry | 636 | 622 | 24 | 85% |  |
| unverified-source | `0x490aac77c960b0569c8e446ac7e12490bd44ca1d` |  | 606 | 592 | 78 | 73% | 1 of the 592 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x03a8a3ae0b496f6988f467798beb60bd3c81f4ac` |  | 555 | 335 | 1 | 0% | Unverified, but its bytecode is 92% similar to CrimeEnjoyor (0x84d05511614272694d3a9cebe896514dbde51f40) and exposes the same function selectors. 335 of the 335 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x8863786bebe8eb9659df00b49f8f1eeec7e2c8c1. In 3 of those, the receiving address is written in the delegated account's own storage slot 0, so each account can carry its own payout address. |
| verified-source | `0x69e6bd1c4082403fc7917a61f6216552fc1a541d` | WalletCore | 533 | 517 | 15 | 80% | 3 of the 517 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| verified-source | `0x7702cb554e6bfb442cb743a7df23154544a7176c` | EIP7702Proxy | 512 | 512 | 239 | 34% | 3 of the 512 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Marked as malicious on base, optimism (not Ethereum) in the Huang et al. (USENIX Security 2026) artifact. I have not checked whether the code at this address is the same there; treat this as a disagreement to look into, not a verdict. |
| evidence-missing | `0xf4b2569a806c1f4d1be0cebc3f0475a3d17a1c4d` |  | 448 | 232 | 1 | 2% | 190 of the 232 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x77021100bd87b7008e5e1989d0eb38555d0d0000` | SemiModularAccount7702 | 447 | 443 | 16 | 74% | 18 of the 443 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| forwards-incoming-eth | `0x4049d89f5c83a76aff4a1ddffc504da5e0597bff` |  | 430 | 328 | 1 | 0% | 328 of the 328 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xa1b1444fdc5a78961b5288b37a517d489e26a4da. |
| forwards-incoming-eth | `0x2e13de8763a53a6af340930fadcad966ee79c845` |  | 399 | 107 | 46 | 0% | 56 of the 107 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x63e2f0bf6966256dad9c590de0fb68acc81c1f51. |
| no-code | `0x0000000000000000000000000000000000000000` |  | 354 | 234 | 91 | 0% | 179 of the 234 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Delegating to the zero address clears a delegation (revocation). |
| unverified-source | `0x4c99e0e4b1147425cbf254e470a4eb3487909c80` |  | 340 | 242 | 1 | 92% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0xd6cedde84be40893d153be9d467cd6ad37875b28` | Kernel | 331 | 329 | 30 | 98% | Verified on Sourcify; Blockscout did not report it as verified in this run. |
| unverified-source | `0xff26b51fb5a6420453f362e26dc5e3d5adbfa208` |  | 262 | 262 | 1 | 100% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0xcda3577ca7ef65f6b7201e9bd80375f5628d15f7` | Collector | 250 | 250 | 1 | 98% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0x000000005c84f8fd50b21cac312528a64437030e` | CaliburEntry | 191 | 191 | 78 | 55% | 1 of the 191 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x5ac4c3f3d60d9186baf971aa1bda7c3924adec4c` | Utila7702Delegate | 173 | 172 | 31 | 83% |  |
| unverified-source | `0x0f9fd457c12999245c2be5645ab61e10f787c72a` |  | 171 | 171 | 1 | 100% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| unverified-source | `0x86485b8eed03bd710bf243982392dc61f3257785` |  | 171 | 60 | 1 | 1% | 60 of the 60 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x1f74b4339990db761bc0168f20d294a3a141497e` | RelayAdapt7702 | 170 | 73 | 41 | 41% |  |
| verified-source | `0x6c35fbcf24e57e5aa2e3aa2ca82e052499d02cf8` | TokenPocketStatelessDelegator | 166 | 166 | 62 | 51% | 1 of the 166 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| unverified-source | `0x90391cd3764b23a7a44c3edc3da7557e3faa2b8a` |  | 160 | 3 | 1 | 0% | 3 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 3 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x68556d641d419817b3a8ddc9418a84352c93fb95` | EIP7702Contract | 138 | 111 | 2 | 1% | 40 of the 111 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x5328cb0accfb156354710d3d04452963a17af63e` |  | 129 | 129 | 1 | 99% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0x7785a22facd31db653ba4928f1d5b81d093f0b2f` | BasicSmartAccount | 104 | 50 | 5 | 21% |  |
| unverified-source | `0x4eff4d390d89b2195fe3cb63b06731ae584a1375` |  | 102 | 102 | 10 | 100% |  |
| unverified-source | `0xd4029f06cd24ca9237eab6c2827b9408ee305bad` |  | 100 | 37 | 3 | 0% | 21 of the 37 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x6d42377d3559a1555ba8d680132041e43a731fce` |  | 99 | 98 | 1 | 1% | 13 of the 98 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0xed4b70b5e78a11070bdd4fcea96ec18c1a8798e3` |  | 97 | 6 | 1 | 0% | 6 of the 6 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 6 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x24b576bc271823bf9c24be627b4363b9b00191e9` | HermesDelegateV1 | 94 | 94 | 14 | 84% |  |
| forwards-incoming-eth | `0xcd7b35a913dff15a364e4611d2db1cfcb179ae5b` |  | 90 | 16 | 1 | 1% | 13 of the 16 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x07b26e3e228778b6c132b1cbaa9a716f72bbf05b. |
| verified-source | `0xa34e1e389097409aa65ff374af50b402e4a8f5c3` | DfnsSmartAccount | 81 | 78 | 11 | 91% |  |
| forwards-incoming-eth | `0xdc78583d3bb386b055174a485aacfed52ce3d37a` |  | 77 | 50 | 1 | 1% | 43 of the 50 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x11d92f0bdbbe98094595991bf5d3214252fdb662. |
| verified-source | `0x05ae73c5925d843864ae6f261f3175de2ebcd963` | RelayAdapt7702 | 65 | 64 | 19 | 72% |  |
| unverified-source | `0xfe593c393bae5aa57c81a15c20810df99c40d70d` |  | 62 | 59 | 1 | 3% | 7 of the 59 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x2350f22f3472b3cd2c915aa12338c2bb9e2311b3` |  | 62 | 26 | 26 | 0% | 20 of the 26 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x955d84139e7621bc571b117d8eb5d28a4a222c6f` | TKGasDelegate | 57 | 57 | 49 | 95% |  |
| verified-source | `0x31c934f4db134d3110e963044836d7a89609b783` | CTOCDelegate | 55 | 55 | 1 | 98% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0x79cd70284ed78fc78e459bdff06a06177f7375d9` | BatchCallAndSponsor | 53 | 53 | 8 | 98% |  |
| unverified-source | `0x535023ed14a1862444ec29d0fe07cf3092c73bc2` |  | 53 | 15 | 15 | 0% |  |
| unverified-source | `0x027f5eed8c0f8b9d8e68f60dc437175af7b52ff9` |  | 50 | 50 | 2 | 92% |  |
| unverified-source | `0xda98669de7f4c4d5c2e41baf12574a67ecc25619` |  | 44 | 29 | 1 | 2% | 7 of the 29 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x51fa1cce1c8b11dd89a053544d02c71c275cdec8` |  | 42 | 33 | 1 | 7% | 31 of the 33 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0xd52573f6d4f68d8e7f8fe2ed50a1023c5f6fe82a. |
| unverified-source | `0x3516d8db77e41319011f4265cd61e743e9b9822c` |  | 37 | 1 | 1 | 0% |  |
| unverified-source | `0x60b82581a0f2ddbf0f2f3709365f9b9081b16eed` |  | 37 | 23 | 1 | 0% | 23 of the 23 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x8544e1d67ac134ce6642cd086cca98df3f0a4c3f` | Consent7702Account | 36 | 36 | 1 | 94% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. 1 of the 36 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x612373d7003d694220f7800eeaf8e3924c0951d3` | CaliburEntry | 35 | 34 | 34 | 0% | 1 of the 34 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x893b612461326a6deeac2dad5ff5cf03e114772f` |  | 33 | 33 | 1 | 3% | 2 of the 33 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0xdc86dea6ee5a9d4df5b6f4ea8f469be4c1aebc3d` |  | 31 | 31 | 1 | 3% | 27 of the 31 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xf9b681edbe2260b5e508c78ad56878432cd548fc` | TransferDelegate | 31 | 30 | 3 | 97% | Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0x532ba46934e877585b293d582ab6a6b62f0cee44` |  | 31 | 31 | 3 | 0% | 10 of the 31 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0xb55387309203aeabb56339da3c4c0fa3e7a04a96` | TransferContract | 30 | 23 | 1 | 63% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| unverified-source | `0xb5216738ca143b4ed6c1bb585f442f4c5cad9648` |  | 30 | 1 | 1 | 0% |  |
| forwards-incoming-eth | `0x9676d9f94ece8d97cb4aec6ea3cf3a6e3ebb0b09` |  | 30 | 12 | 1 | 3% | 9 of the 12 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x44d71f883da04c10dfa9f540c53a552f0bc941e9. |
| verified-source | `0x9ed18ba902951c16c2299ac234921380743a0a67` | EIP7702AccountLogicV2 | 27 | 27 | 2 | 100% |  |
| unverified-source | `0x27bfd156c8c0df64e6a863c589dc9593ddac3ee2` |  | 25 | 21 | 1 | 8% |  |
| unverified-source | `0x715e7694c9789c06d25dd197a130cd42ebb2190b` |  | 25 | 25 | 1 | 0% | 25 of the 25 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x33f0c2f0f2377df77349bf2818c88123fcc645dc` |  | 24 | 1 | 1 | 0% |  |
| verified-source | `0xcc0c946eecf01a4bc76bc333ea74ceb04756f17b` | TokenPocketSimple7702Account | 22 | 22 | 10 | 55% |  |
| verified-source | `0xca11bde05977b3631167028862be2a173976ca11` | Multicall3 | 22 | 22 | 3 | 9% | 12 of the 22 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0xb544282ddc2906de7f610e54e08e4f568997017f` |  | 22 | 19 | 1 | 5% | 6 of the 19 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x8e13000d307c02dfef9c5c2d23f92a90824c918a` |  | 21 | 21 | 1 | 0% | 20 of the 21 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xe73d866b2acc6f93476a722ad2d26c89104d360b` | SimpleCustodySponsorV2 | 21 | 21 | 1 | 62% |  |
| unverified-source | `0xc1c1e18accec66ce640633d638102b3efba4d596` |  | 21 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| forwards-incoming-eth | `0x1bcc6b722dd35072823ea7f80b50442aaf57aac5` |  | 20 | 20 | 1 | 100% | Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xa7c91c2911206de0d3054372d6af188fb11af07a. |
| unverified-source | `0x07241d6ae14a6605e12a5febc187885d91b40da0` |  | 19 | 17 | 17 | 0% |  |
| unverified-source | `0xe7b42f0a78346cdb69815317099dd6977928b2ea` |  | 19 | 19 | 1 | 5% | 18 of the 19 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xad9cca330a131cd3bf3886db21d734ec60ab3076` | BatchCallAndSponsor | 18 | 18 | 1 | 100% |  |
| verified-source | `0xe40ccb2d94975c51bff0c004efdfd9b3a5796fa4` | SmartWalletEntry | 17 | 17 | 17 | 0% | Verified on Sourcify; Blockscout did not report it as verified in this run. |
| flagged-by-research | `0xb6da1852c218d74257593126fdfbd20f0bceb2a8` | Porwarder | 16 | 1 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact. Verified on Blockscout but not found on Sourcify. |
| forwards-incoming-eth | `0x399fbfea9fce84e57976c5c57d6ce7725a7f96f4` |  | 15 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0xf37a277d125f8d5b690f2078dd97bbc9aac1ad4c. |
| unverified-source | `0x5546a14921647a6fc3c8927a2c0cc3afe2e9ae77` |  | 14 | 14 | 1 | 7% | 13 of the 14 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0xf366fbf916917117e6a2782ae5f920b4b0c5b3e4` |  | 13 | 7 | 1 | 0% | 4 of the 7 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-but-upgradeable | `0x7c27e3aecbf42879b64d76f604dc3430f4886462` | EIP7702Proxy | 13 | 13 | 3 | 100% |  |
| unverified-source | `0xd2bc5c2823856ae0fa5c79744cf09c3e9a9ff35b` |  | 13 | 13 | 3 | 0% | 5 of the 13 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x09b2fcb8bd90193f3a82c9a7f06ccf1d23707794` |  | 12 | 12 | 10 | 100% |  |
| unverified-source | `0x54bf93ee1a08af3c90c1cf9973d6e95be9ef65d7` |  | 12 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x5a7fc11397e9a8ad41bf10bf13f22b0a63f96f6d` | AmbireAccount7702 | 11 | 11 | 10 | 45% |  |
| verified-source | `0xa2c6eb5f4095a19571a206f39612faadbbe702cf` | UxuySmartProxyV3 | 11 | 11 | 8 | 100% |  |
| unverified-source | `0x65a46f03d618af4f486a02de181b947ecc97943e` |  | 11 | 9 | 1 | 0% | 3 of the 9 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0xdfcf191d5c948af5e1a641eaf1ea1eaedaa15ce0` |  | 10 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x85bb292af8ab89645aaf552869c15c768a5f99e2` |  | 10 | 8 | 1 | 0% | 8 of the 8 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x81f604e86f6c02c982075efcea800de826598f2a` |  | 9 | 9 | 1 | 0% | 7 of the 9 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0xf3ed64f43472c1ccafd3afa7a3aafe0fde783141` |  | 9 | 9 | 1 | 100% |  |
| verified-source | `0x42c0634bddb659d34aac612f81c3daa0e791919a` | recoverooor | 9 | 9 | 1 | 0% | 9 of the 9 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0x575456fa1004eb5c6331cdbbf9f0e5acce5d87be` |  | 8 | 8 | 1 | 100% |  |
| verified-source | `0xaf2fd3b15843131064f5c604f04778730c682523` | Consent7702Account | 8 | 8 | 1 | 88% | 1 of the 8 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x80f42d5cb6091466c74cbb135cec03c4ad4d1fc5` |  | 8 | 8 | 1 | 75% |  |
| verified-source | `0x2f5e05a65f25d7bec3d8f02a9689cdf43eccd3e6` | MerchantConsolidator | 8 | 8 | 1 | 25% | 1 of the 8 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0xdeb42478c7cab616ad70e0cd0b342cbf0be4652c` |  | 7 | 7 | 1 | 0% | 5 of the 7 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0xc3c89ff8589644332c916d9c6ec2883eb69d44e5` | FixedOwnerCollectProxy | 7 | 5 | 1 | 28% |  |
| unverified-source | `0x74f2b03fdec0e9cc35aac867c67bc938233088fd` |  | 7 | 7 | 1 | 100% |  |
| forwards-incoming-eth | `0x3ae1f70cf6da80955936f5599d103fcf62162d10` | Reconstructed | 7 | 6 | 1 | 14% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 2 of the 6 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x43b18f8fb488e30d524757d78da1438881d1aaaa. |
| unverified-source | `0xb7294bb10ccb260de99cc775b46664555b641407` |  | 7 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 2 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xa0878a0d2ec7cf0666dbcf68f4c1988012191de6` |  | 7 | 7 | 1 | 14% | 7 of the 7 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 7 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| forwards-incoming-eth | `0x1f49381c59a867491e97b7e94923a32da1de8634` |  | 6 | 5 | 1 | 33% | 5 of the 5 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x3d903e1e806ad3ab8a9f36b6048abf87892b5374. |
| verified-source | `0x14f01bbaa1dcff8f12bfe1cd54b58a7ebe211b29` | BronAccount | 6 | 6 | 1 | 50% |  |
| unverified-source | `0x53e3ba12677c461939ef60c94abe33d8a833da10` |  | 6 | 6 | 1 | 67% |  |
| unverified-source | `0x74abd7dc7017f6ee00302f3cd2653096befd86bf` |  | 6 | 6 | 1 | 100% |  |
| flagged-by-research | `0xe9eaef23ac3ce6c232517541c7d361852b06f911` |  | 6 | 5 | 1 | 0% | 3 of the 5 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 2 of 2 sampled accounts delegated here was passed straight on to 0x276d4366c056040b8f93f2e50ea1773a81af9d1f. Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact. |
| forwards-incoming-eth | `0x77f64403a328ffd675bc12e18bff559242a7f510` |  | 6 | 3 | 1 | 33% | 3 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0xa61919b4591110c344b3c7fb231dcb4e2df10e8a. |
| unverified-source | `0xdab6351800f3b48ebb518259950303dbffc2ad18` |  | 6 | 2 | 1 | 17% |  |
| unverified-source | `0xef93688b67019e4b48f19d924f9f8c1f01fb4b3f` |  | 5 | 3 | 1 | 0% | 3 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 3 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xd208fcea4077cb1bfc7d4e7d3d45ae28de430c6b` |  | 5 | 5 | 1 | 40% | 5 of the 5 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 5 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xfb1b8fb55d1aabeb96bc1c36a9754b28e46a8b6a` |  | 5 | 5 | 2 | 100% |  |
| unverified-source | `0x709a519eb51f7153b7560a4aa7033ee4ff45a907` |  | 5 | 5 | 1 | 100% |  |
| verified-source | `0xe2aad4ae4eda149d9eb8bc885529ef2ee04f62d7` | BatchCallAndSponsor | 5 | 5 | 2 | 100% | Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0xef40acdb728e0feabafb07ab89bd0cdc9d3d7fab` |  | 5 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x9c34ac9479ea7b9f5df8525ff5ed98363057a87e` | Crime | 5 | 3 | 1 | 0% | 3 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 3 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| evidence-missing | `0x00000000228a69a77a83bba0d354505b8d17dc65` |  | 5 | 5 | 5 | 40% |  |
| unverified-source | `0x4f577087064ea4b5cf294d44cfd56275d9d1ed18` |  | 5 | 5 | 1 | 60% | 5 of the 5 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 5 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| forwards-incoming-eth | `0x42505b8dac31d70bd9d9006c7ffface81544dee6` | Forwarder | 4 | 1 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x94943b987a73fa0213f540d6efea887fc73bf6ea. |
| verified-source | `0x4cd241e8d1510e30b2076397afc7508ae59c66c9` | Simple7702Account | 4 | 4 | 4 | 75% |  |
| forwards-incoming-eth | `0x6e4f81bcd0d14af02c2b39fec16c72770fe22509` |  | 4 | 4 | 1 | 100% | Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xdaf2fe0cf8c462067cbc6084dd1ff8ee42041ea9. |
| unverified-source | `0x0000886f49de8c71a20f7f8cd681e2b8f0bb2982` |  | 4 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 2 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xfae8c7c7d6b69a020d686dee4877fc7b7700f426` |  | 4 | 4 | 3 | 50% |  |
| unverified-source | `0x87dc58542dbda22af93f122f289969b3cf7609b6` |  | 4 | 3 | 1 | 0% | 3 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 3 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x08bf3aa11cf3063ae49c9383e74eb72b3329aa24` |  | 4 | 4 | 4 | 0% |  |
| unverified-source | `0x13e00e089f81ad9f36b655c9e9a07c6bf1489a5a` |  | 4 | 4 | 1 | 100% |  |
| unverified-source | `0x343ba89125228f99f3f8afaf8d52e5add227627b` |  | 4 | 1 | 1 | 0% |  |
| unverified-source | `0x26961e781bb3b8b5617bba5929c105f38759816d` |  | 4 | 3 | 1 | 50% |  |
| verified-source | `0x3427a6911210aac809e6d0bfeea6dea570c9bb58` | GaslessDelegate | 3 | 2 | 1 | 0% |  |
| forwards-incoming-eth | `0x7e7dd63e2d42993ce84060c594b52631fbb0505b` |  | 3 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x77d462c9e8a00909b512101299f3446b348687f0. |
| unverified-source | `0xc3564e2095885bd4c5dde9a3691c9bec9387fd3a` |  | 3 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| evidence-missing | `0x14eb85c766a24fa18a2008d9d2ba69344830e938` |  | 3 | 3 | 2 | 100% |  |
| unverified-source | `0xadcb814812ca5d40d44d70917fb4cf945bf45b9f` |  | 3 | 3 | 1 | 67% |  |
| forwards-incoming-eth | `0x9a99954123faaa68f9fa3c19109ad6e364558adf` |  | 3 | 3 | 1 | 100% | Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xd5badedd2566b7fd6b05cb560b6d792e00c51fd9. |
| unverified-source | `0x2c3cbe3b2cf2015602045e9b4b0f180897b369c1` |  | 3 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 2 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xb2fe786ec2584bac0217251cabc485e0b1116a9e` | AmbireAccount7702 | 3 | 3 | 3 | 0% |  |
| verified-source | `0x440eaad070ac7d4056c0c61157bfaa0ad51b4608` | EIP7702Contract | 3 | 3 | 1 | 0% | 1 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0xab77f99a308e52adec555e75d1b5e10a1517a4d2` | BatchCallAndSponsor | 3 | 3 | 1 | 67% | Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0xcc1b2113c8775c545660a8ac0bebe425da12f938` |  | 3 | 3 | 3 | 0% |  |
| flagged-by-research | `0x540fe9bec2470e93aa911906eb560ad6647612c2` | CrimeEnjoyor2 | 3 | 1 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact. Verified on Blockscout but not found on Sourcify. |
| verified-source | `0x438f67c2aa7ff150352295dcb190c19fb6672ad5` | AuthorizedExecutor | 3 | 1 | 1 | 0% |  |
| verified-source | `0x117a540d7a319757a9c49492b4fa577f30b73b6d` | Consent7702Account | 2 | 2 | 1 | 50% | 1 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x3b7f030bb3b906e949452daf3259e632eed5ca97` |  | 2 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 2 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xd1945bda1c461f68e0157e14c4f97ee3a6444f22` |  | 2 | 2 | 1 | 0% |  |
| unverified-source | `0x2fe8985f710efe2bf5f1c6e9035ef9f21eb0a6d4` |  | 2 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 2 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xe6259d8fa4535273a5bf00287f6d350c556a940d` |  | 2 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 2 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x4986579bcdd269b3f3c51eb0954114b2694afcf4` | UDABatchExecutor | 2 | 2 | 1 | 100% |  |
| unverified-source | `0x32ecfd6b17e48b760714a76a4155cca1e82daf1a` |  | 2 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x92e0eff1046ba2c2de30eaa8bfdb18f558e01d20` |  | 2 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x3e2b1f7c601300bd2a3c9a70edb1bbbf245cace0` | EOAForwarderPassive | 2 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xa46cc63ebf4bd77888aa327837d20b23a63a56b5` | Simple7702Account | 2 | 2 | 2 | 100% |  |
| forwards-incoming-eth | `0x64d9de27a6d769712148e6e14118c253bbfc1633` |  | 2 | 2 | 2 | 50% | 1 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 2 of 2 sampled accounts delegated here was passed straight on to 0x95b6b59ca57825eb85ff8c37242acd3fffba5b60. |
| unverified-source | `0x326b428527a0745ccebfd8d9c055b71e96b1f67a` |  | 2 | 2 | 1 | 0% |  |
| forwards-incoming-eth | `0xaaac4bd7d8bdc080beda8546658867cd45642629` |  | 2 | 2 | 1 | 0% | 1 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0xf87f1a3d738b5d2b7fe7045870316f9fc2ee1488. |
| unverified-source | `0xd5fa55563703fb13ace34cfad40313876550c56c` |  | 2 | 2 | 1 | 0% | 1 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x843469f223bad7ca390a8b6137c4f87955b97568` |  | 2 | 2 | 1 | 100% |  |
| unverified-source | `0xceffef058ca19c231261cb6d4e4b3808590663f5` |  | 2 | 2 | 2 | 0% | 1 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-but-upgradeable | `0xaeefb95c15330aefa29ef71a432e9f9cf9b3bd0c` | EIP7702Proxy | 1 | 1 | 1 | 100% | Verified on Blockscout but not found on Sourcify. |
| verified-source | `0x487db2fd20522c4a3ed542249483d9a12de66b1f` | Simple7702Account | 1 | 1 | 1 | 0% | Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0x47e747f5e8cb5819c966292dd969d989ae9dea5e` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xd43718c43299e56b668fe2a0bdb3b4b9dce5da15` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xe25746b0d27518e6f6219d44ab3cb42fb1d5adae` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xa09d0df9bbe050462c1ab6e7c5fd8b39414276d1` | Puffie7702DelegateV1 | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x692d138b1c77d6abdb3fdbdae584f1969b341c57` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x3cf32d4d57e91e0a1c3658884040889dafbe5103` | RewardyDualEntryAccountV3 | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xba7a5e581a12c180742e1b6ab221d474d7e6972a` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x1e1af9bbf26446dfeed701aaa31006932861998d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4313e94c7f09b9a0d0a7f6a4e706818e3b5be58b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x108fc03d51cd0b85ada676a914b83834bf77edb4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdfbd1858a39cf139b9920b1fc51488142493e853` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xb3c773d806513cd081895d1557415416864c503a` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x17b4b6f6a9f5d74960077d28972dcb3e70bf5dc3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6e6223fb14606670dcfc246df1a81767665ce7f9` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4fccd307b84a9407651c138b622cc1cf448659cb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe4f5df21c870093275e628d84dcbea036b167da5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5d14db3fee458839745377607a3efc7739f8d4d4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1e87f964ec7461de081bbda615bb1f05738a0521` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x12225438fe79f781abb53a76426ee49b630abf96` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x353187aae6601878df7b1e1ae7f6abaa634c3df9` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4416de1cc402fb74c243aa381fe218cf24406c9f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5704816c06367c2cea7f6973b56b0668f918fdbf` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x620cfd8f3b4cef421adad917352bc7c4f696d38d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x0446b7ca81b21bf64515e4a97aa8a0cabe4f866c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6a6547900d4af3be6e9e66f5e7a58f32ceef3350` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd73d5ef82c121f63dcbcfc4b3a30b6097394ecfd` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8a34362e36ea669fd0cd8359d05225569819908d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x574bb458aa60e2d5ff42b0381c6bfca9321090fa` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6643106e2a0bd810c9ab72eb2522d52a24996036` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x90b0bcfde7c08296ea594c2936bf7ffae03651f8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbd9e2e0e08e4e0a54cd127a60bac3c4ee70fda51` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1c11fb029b87aea564ce807dd20782013f7c2ebb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbd19003994062446beae4478a981d4c7526e5832` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x04bff6fd8da78efa2f6c529aa8ec01d946a557da` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x976129c0c161c3bafab71a12d9e2e55ad8853070` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6ab0181a03563f54992872ec0fb81fac64fd9274` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x87c66dc7c146ad0cdee2154e90fa4e86a1b8d991` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xaaf409098d367dbcc003f54c7aa70b2a6e665241` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6796f23c1a3960d1020299b69b4bc2c0676e0a78` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc5728f42c625fb53f806acdf8a5b13ba6eff4bb7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x73daa011cc118f60b2fb439b8d317fba08ff6267` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1adfcce1e3d22283aed3a9fa42e3e008983381ec` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xed54a651692f4ee4808a7db8f0d3df30ac34d48e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc496786776fee4de1fbb17b9b35b8f0845e59cd3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1568af117a2f3b05519874fd6b3cc1f2301ff074` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4ace74cab6f020f5380444665efb6c2f6c463fd8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x182fed8240626edd45a6dc763085b14f560f5c65` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8b8a458ed66fa45c9d0cb3cb82897474406fb951` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4d8890d9d81c859b5a540f07e3156ca80496b4ee` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x83fe35ee73b0c753db32f92b14c37d0cbf3c6ae7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7324a30605cc286f3238a3eec8e79c8f9f2621bd` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbace6fe81b27941e8e0ff9870b84e263a515bf70` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2460d8d05f748909b02c1d34b0962a880657e701` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x643c50277dbc68153e22d3faf2fe7859a67befbf` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x58fe0f529c82826fc7c74ea8071cf7c46822fbe8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x20492bdd3d0ca710b119c8c417aad4c0a027a0f3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd1d112204f46d8f9839fca55437559cc80932ac2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xfae64334091d8c82c7965c2c21b273c2e53217ee` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x642028922f06167fe0aaa36b5485fb02d3e68054` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5868057ccf4e8a627596efc0d1122738c4089708` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xad09faefbee707eba21165e8a26ec9f595776c06` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x69ddd19f5b9b5aa35fb5247e00a0fe2e148b2595` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa06faade5f569761544497d8d22581e156761870` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2d448979e6ae41e1429ef9f85ad4762cf87266cc` |  | 1 | 1 | 1 | 0% |  |
| verified-source | `0x000000004f43c49e93c970e84001853a70923b03` | Nexus | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x13d06f37169fba317b339b7ac6320b1d182a8e91` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4adbe86351855a722a23f041ca6babda6660cbfa` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa5326f50400f0b6d91de3a1e4254af6fc97a6cbe` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf61523d22e84bb44b8fc5f15db00894311b21b3e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb185b94107e3155963b166f8c99bbdbc81e72117` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xeb120ddebc22d8a00576be468d9fde6f9d624f01` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc527ef19472644da13e46763b62bbcd1f99e6d4f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2ad3c44dbaa40992b1f2d140c3db49c114d6b6da` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x0ca02c1d55885b127db4c2e2b0efca20d3263f70` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x51cde797f69347c68f52dd0a3c65537a21e16162` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3919c6bf530b0434d68dcec2a61d917112e16316` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x994b549e328269dd31f82bfd09232c623fc619c4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbcfe5bb1c1bf27eb0db8a4070c3e5c89d74929f6` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc8227e11b2cfe35cebebd13fdc960f07a11bb9eb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x0bf622eb7f11ad905e98c05cca559cd7a3edbea4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3d8117a1ea1279c128171c37dea7fe6a797599d9` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x733dacc63bbe94bb1558ebf79cdf3e82dd3e95a5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc93e3d28b4b47d7433f28508d996b7a7158bb91c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf0de621aa19ce886d1779b7fc6546c674560ed17` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9dc3c34286650fd6382e49975423faef12c24028` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4c10e231c1ee7542da6320e51ddf9982367d3772` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4c9315aef4f931aa860ffeae582d0d717c350fd1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xfe0e06b93472bd4d7e91b049767047494d15e8f1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x08cf3e255bc25b1f5ee1c539675e88e1cefa4c69` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5d80f299d4c457ef097c3a22dcd8e7bc1058255c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8adb55d8286b1e95b04a2f80ceebe10638d87a6f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x641ebce11071330d215ae4852bd7f7a1a9976f25` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5b9541c55a42940a5453e6083c7f5044b37de9ea` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdcf62b3455bd26f1ab843521615e2a03a14911eb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xfa7e1d1ad0909923251e139ee6df72579a547623` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5ad439bec598b22385690ef1d78d9c1f52ca61d2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4df0f2198876cb0cab16c0110bcb5f6e4d83343d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf5d800763c8468ef3ee59254bb567ff3d62009f5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8347c0e67e696e6a333b85232f0218942abc547e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x69b7913214495073e037880bf91f55a0a4096079` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x20f519baff10a5bdf1371c4acd7b8726ed26cff7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x041c971ea3354972eb2804297a253b0f48da1f03` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x031b1e4a2cf3dd4997dfdc7175bae37617e79081` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7e81871e8b3766ec3e2ded7c70d2c06a7b5bc564` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7899d33db197d9410a12368d0ef8a3bde119a809` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7e2c26b18eab100f393d2931868d616a00aea716` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa2933142b293773b1c26867b92de4ce4d4542a80` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2382c53684aa47d8acdc995e1ef5d9f7a2c3ae98` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xcaddea5e974b2c31439b1246180503cd4a342284` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x526875b2b9bef1c90a3d01c37195614fe6e5e551` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x747e567a88364149148cbbf1cdab67c48a3e4877` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x17e2275585f425a1c280aa998259b9c058273d83` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdeb2550dddf4a2f2a4fa7d7d445acc5dc95a2c8d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xcfd0e250c8a7e658827066133db7b07334123a42` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8da408d2608e0eb7b276d945f5b822880a1ceb63` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa7c53a1275e1bb91075cbb2c2c7524d4350db5b2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd2963d5db49fa4ba336092bae01924182119fef2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x54558159f90b17b0b54609b69d9adc486ff7ce74` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4dbd9ff9909b03e31322fe3ba8fa7a52bb09b050` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x40f15b5dc21979ccb90e1f3f4dc152c979573cbc` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd3484f02320b64e9b911c5d1352508d4076c48d7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x68066c1d41fc76f5885eae67a1275ae9738bdfc7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc3327178ecb80d3e53935ce1fd960f08dfcc6ae6` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x0c20d5f3ea2d50793b5b4eb2ed786bafae07ce46` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc435ab9be1257a2a7dee69f0a502373cffab2f92` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x55851dfc811fe7fa88e3f2baa93ccc18664faff7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf439700a19733bdbe6bd5bedc41f94161fd4a5ac` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4349db13d8cafa760b86fcd30fad8be1215e9f20` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdc954c2cfd0b3b68cde9ccd3ddd796943636dc98` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x054e5cf0ac7bce6b6c290aaed19476a078cff101` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd759edd5238d140219b8378656db97464fdf2146` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbe73ef6bab0b83566a402f0be8e7ee20c2276de9` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x65b36751a764405f603e7649a712be4b3cb4ea58` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf329ad50ede99b46786e6b3ca3c5ee418eb4a0f0` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb67d3b5a8e1b424486ee8b83729f1b4e11a43d6a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8cfab1fee72d3a4f0efc7d1fad4c90bb912e7cdc` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x06ac1b7adc0ea8483ed0b68400bf7d699ef4a604` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1fc9151875cd2232862c5330dbe57fdb84e17155` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8ab56cb81f8c27ac6ebbb9f643f54a08169170f1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7d5a37202d2e18fe7b6fa9b88f06401cebaecd03` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc9b6670502c731c529052cc4612c8d208774de72` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3948d97badaa6c1fc1f3b7d78fb9cc6c0ccaa653` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd7a95e4260a6c0c07373eed134de8c29b01b67b4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe10fb1c482f72746265ad6d84d55103f09b5c2cb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc5ec3249f9cf9a3ca49f5d9e1eadeb45fe5119cc` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x99ac92490a0d0f649b531ca97f54db781cf298b0` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xcb1c74cc7ebebcdd6930ef9269c66469efd404d1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7073d0cd57a04250f3d0bb3a2519dc34673a2969` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xcfeb3a386fd15b0f88b422cbd9ae295ee086681c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd339e8b9cd304ca890af67089805145f846f9080` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x83351bbb7a0e362d1d8a0b6c5f74a4b7424689f4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd630c76ce4acd93c3a735e2a7ed7d0708d207ad1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe1802a7588404164d7cdfe80d2ed14a6b753e2d5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x0b24a6c760cb3bc28b71bc1cd60b871b4c0a56d1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf95c5977b836bab9060cf6f598080f33dc857f9b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6d4d0cb23a2cfa9f9ec639f6a15297e6214c6627` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x742eb9c86aa6bb068e79c7a6655ed206362e4b87` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x41770ca467cdb239a26ffe5e024400171fd595de` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xfc51d8642e4c4a9b4fa5a32898c8d84f503b942c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1e8785b51a955265867eaa83ec0184dc2bbd46da` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xaacfc3400326c7203d85bbf3904f957d194e263c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x91d47b667fd128d6e3e62e1ce153a9fdbd60e982` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf333019df1e35cd408ee066b5999daeae783a64a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf41f4144225ebdd2fc1020a7959d367b20d83e7b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xad6170adfac772dec02ec142fc57a72e0cd1fb07` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xda6ff18f4251a25466cd94e0b8d650005658b98c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5a3e753e51db4c25adecb61efc341994a83ea1c8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2d718c759870a755e66c408e33dade7f26bdff2c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xfdd3b354a8256570585741e3223efe68b80e954d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xeb4d6bd25e1c4099f6b612301a0115249e99bdfe` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x30df2cb0f3d6a4ec16677c7f545edb6ecfbda6c3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x12d86ed926276cbaea4e8d53cfe1ecd497e4df1c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3c40669ab70d7cb25d4c13b88a0a009f565c136a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x31166748a64a7185ae629e7a517488553dca3924` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa0b24b664b3a197a662449f6c0ddf5ff4d952fae` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1acd89a601d34bb259487869b1a23910fd0ee822` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1f8afb9b7cec0af01b922634b51f395080b63226` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x30538c98a62ab35ec182c3b9052f8e7f5212976f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb027878c8fb07d8aa813568dd825372a5bbf2f83` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x0dcea3c4f7439c471bb762116840cba8dd206668` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3775a88c1563d48c2baa58d85b16f29c4497b2a6` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd6ae8e7a67571ad8fd8cee76bb196a4ed7dee0c4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8622e910e9e9eb48f57ad76ffb2ea0a5da0c38c3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x322d505fc86616288e3f0aca21f4b750418da52b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1d08396f6199ffdf4c69c537bd26b6a2dc6d8bc7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf0318bd0b121f8685e985214642c02b42ac57550` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x077339611d7903341ec3e3118cf7ff7c58045e9f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xcfab2c8d3eb16c838b5e1beaf2c3ec5f267bd8e9` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbcccd65b59915e72ef799a585b4f87a85bc36154` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd14f3c9d329eacdef6d214d83a3ad745d5f46f59` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x651779e9e6f24b3d85cbf1515749c0b3d27cda73` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7fcc3b347163b5964f8e01fbb77b6582271dc59a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3525a388cb86f35d5b72724be03ba9df830ad4b7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9aaefde17e905df2419e14e781fad2c6431979dc` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9b83bb0876a8cfe42798d5ad6543f260c58d0015` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x11af0b4d3f38f6d7e9c7231907674b6e18ad183b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe14cb75430a821666a32e0a8df42398e9ee8e8b8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xded3712f9beeb4aa160e019bc1b8fb67d1700691` |  | 1 | 1 | 1 | 0% |  |
| verified-source | `0xa34995732725b87aa889a31af23dac5029ec019a` | KentuckyDelegate | 1 | 1 | 1 | 100% |  |
| unverified-source | `0xb4c5f7b538eebadf6b9ff383b9ea16dada010aed` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x81e665a2d9099c726071566e0a2061db28e82701` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x3e515544f8d8293b0a353e10ff3b7ca03b52f35b` | MinimalAccount | 1 | 1 | 1 | 100% |  |
| forwards-incoming-eth | `0xd7d20e03c9793bd1b63291eea0021c8cc096a915` | EIP7702Delegate | 1 | 1 | 1 | 0% | Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x14f9f76863b57e89f2d482557828337234dcacad. |
| unverified-source | `0x9eb6a71464d4c19a0b096a57bf4a01ec1c915c38` |  | 1 | 1 | 1 | 100% |  |
| verified-source | `0x3d965cfdda791589ccab955498d509f2f7e30b79` | Atlas | 1 | 1 | 1 | 100% |  |
| unverified-source | `0xd086d522c3e4e5b5545aa4c420ab1670718bdfa6` |  | 1 | 1 | 1 | 100% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-but-upgradeable | `0xc0f16888f4198f53892c53af859f673e23f26fa3` | EIP7702Proxy | 1 | 1 | 1 | 100% | Verified on Blockscout but not found on Sourcify. |
| forwards-incoming-eth | `0xed736cdcdf0c0997f35322626c4e4b1878d8ad63` |  | 1 | 1 | 1 | 0% | Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x0bb1d147253dd0c69f7ea2e10a44ba271b960f10. |
| unverified-source | `0x2d67f1ad2375249ce7f87dae2c0f105ac3e30b89` |  | 1 | 1 | 1 | 100% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x6d154b2eccaf6c9d2ae0d07897d4cf522ecb2e93` | ExecutorV2 | 1 | 1 | 1 | 100% |  |
| unverified-source | `0xa335f903d7be3dcd8833df429af1cde718efbea9` |  | 1 | 1 | 1 | 0% |  |
| flagged-by-research | `0x557f37550196a3022aec6c2b1b4951900ea3e3c2` |  | 1 | 1 | 1 | 0% | Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x31a00175e7be8d8ba5453cfbf6c9be721069b32e. Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact. |
| unverified-source | `0x183cb0f9b078827fc94820ff55b103dd6f75ac53` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xf456464cd3ac63e94e122a88ec8d2bb9605d3823` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x80a9b429f90b28f9e530429acfea931250626061` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0xcaf44ef11914715356ea4fbe9c22f6e9c19be70b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdd19eed97b6d55582fe51c6ea9172cb175b429ba` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xf43e1918cac38e0d39c502dd954b59df2701459d` | PeniwalletV12 | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbf43b8e6a2b43790ee8a1d5978c92afd491d5fff` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x575f2f6b1b7c573c9c82944b48a2f0ff518edfc9` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x5fda61f6fb45b73a87b9bccb69f56475e3455567` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd00e628a486a7d48471e918623332de5b98e0103` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x80d95b9131883cbf4ec56ab7f2d96e23ae9a8b5c` |  | 1 | 1 | 1 | 100% |  |
| verified-source | `0x19506be08bf4829dd14fd4aad716a61776b04fed` | SNPadWithdrawAccount | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x249347d5ae4c3c1a725b7b353b522dbfa180764b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd75ba5e163fa5dd3b764f6d5c21210de3832a6ba` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x8773a2868e4e113381ec94c463d51479fb9a533f` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0xf87f1a3d738b5d2b7fe7045870316f9fc2ee1488. |
| verified-forwarder | `0x0727ca41efc85f75cef26ee48f825893b4836786` | Forwarder | 1 | 1 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x78608e7a956fe1ca4af4a31138fd67779b08f9b5` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x33bcd6304fc165ef0bb85bd5720bc677baae4ce7` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0xd9d6fe80e840c190dd44fcc21de58aa5ffd4894b. |
| unverified-source | `0xc703b7116caf748cb44b8766acdb604aaac62a14` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xa9d94a7c5adedaa684dd18dad23dc8c26beeda7e` |  | 1 | 1 | 1 | 100% |  |
