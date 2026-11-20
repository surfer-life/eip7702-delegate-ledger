# Latest window

Blocks 26446099–26453298 (2026-11-19T02:20:23Z to 2026-11-20T02:24:35Z): 26233 type-4 transactions, 60043 authorizations, 374 targets.

Share of authorizations by grade: **forwards-incoming-eth** 27.8%, **verified-source** 23.7%, **resembles-known-malicious** 22.5%, **known-malicious** 12.4%, **unverified-source** 9.0%, **flagged-by-research** 3.8%, **no-code** 0.4%, **evidence-missing** 0.3%, **verified-but-upgradeable** 0.0%, **verified-forwarder** 0.0%

Signed by 21936 distinct accounts. 305 of them signed for more than one target in the window and produced 33859 of the authorizations. Share of account–target pairs by grade: **verified-source** 60.0%, **known-malicious** 18.7%, **unverified-source** 17.5%, **forwards-incoming-eth** 1.9%, **no-code** 0.7%, **resembles-known-malicious** 0.7%, **evidence-missing** 0.3%, **flagged-by-research** 0.0%, **verified-but-upgradeable** 0.0%, **verified-forwarder** 0.0%

| grade | delegate | name | authorizations | accounts | senders | nonce 0 | notes |
|---|---|---|---:|---:|---:|---:|---|
| forwards-incoming-eth | `0x8a67b5020ee254ef48e3b6a04927f39baf7e408a` |  | 16091 | 43 | 6 | 0% | 43 of the 43 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xcc04506d439d338bde8ebbb074f17a54b7673b95. |
| resembles-known-malicious | `0x8332a5c2f00ab7e20c53210be2192aea7bdc77f0` |  | 13516 | 159 | 1 | 0% | Unverified, but its bytecode is 92% similar to CrimeEnjoyor (0x84d05511614272694d3a9cebe896514dbde51f40) and exposes the same function selectors. 159 of the 159 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| known-malicious | `0xe6b97aa1490c93c28a14d86c13c9dc9c950643ed` | Poisoner | 6493 | 3282 | 1 | 52% | Verified source on Blockscout carries a comment saying this is a scam contract recreated and exposed by Wintermute. |
| flagged-by-research | `0x84d05511614272694d3a9cebe896514dbde51f40` | CrimeEnjoyor | 2237 | 2 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 2 of 2 sampled accounts delegated here was passed straight on to 0x333333320bb4a0345a7a102c49c72b37647aa088. In 2 of those, the receiving address is written in the delegated account's own storage slot 0, so each account can carry its own payout address. Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact. Verified on Blockscout but not found on Sourcify. |
| verified-source | `0xd2e28229f6f2c235e57de2ebc727025a1d0530fb` | Biz | 2154 | 2134 | 19 | 77% | 1 of the 2134 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x34fff33dc9c0ead473a1878923b3858d8ed04dfb` |  | 1693 | 1309 | 1 | 10% |  |
| verified-source | `0x67b743f3642f7cc863c823c6708708d039f65be2` | PackedPayoutWallet | 1671 | 1671 | 1 | 98% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0xe6cae83bde06e4c305530e199d7217f42808555b` | Simple7702Account | 1586 | 1570 | 32 | 96% | 6 of the 1570 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x000000009b1d0af20d8c6d0a44e162d11f9b8f00` | CaliburEntry | 1337 | 1280 | 23 | 89% | 5 of the 1280 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x0000fb7702036ff9f76044a501ac1aa74cbab16b` | UniversalGaslessDelegate | 1290 | 1283 | 79 | 92% |  |
| verified-source | `0x63c0c19a282a1b52b07dd5a65b58948a07dae32b` | EIP7702StatelessDeleGator | 1003 | 974 | 453 | 18% | 8 of the 974 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| verified-source | `0xb94b392b61c16ddb7118849d4970570c07f75dd1` | Tangem7702GaslessExecutorL1 | 979 | 564 | 1 | 12% |  |
| known-malicious | `0xc43b6c6a43e5760a756a67756b2155c7fa735310` |  | 929 | 929 | 1 | 100% | Flagged as scam by Blockscout. Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0x69007702764179f14f51cdce752f4f775d74e139` | SemiModularAccount7702 | 906 | 901 | 20 | 50% | 6 of the 901 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| unverified-source | `0x2e623468c560072e91d7a94a1dcb2eefbdbe69cb` |  | 745 | 48 | 1 | 0% | 48 of the 48 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x490aac77c960b0569c8e446ac7e12490bd44ca1d` |  | 624 | 601 | 75 | 78% | 4 of the 601 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x69e6bd1c4082403fc7917a61f6216552fc1a541d` | WalletCore | 504 | 487 | 15 | 80% | 2 of the 487 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| verified-source | `0x7702cb554e6bfb442cb743a7df23154544a7176c` | EIP7702Proxy | 478 | 478 | 246 | 28% | 2 of the 478 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Marked as malicious on base, optimism (not Ethereum) in the Huang et al. (USENIX Security 2026) artifact. I have not checked whether the code at this address is the same there; treat this as a disagreement to look into, not a verdict. |
| verified-source | `0xd6cedde84be40893d153be9d467cd6ad37875b28` | Kernel | 331 | 330 | 27 | 97% | 1 of the 330 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| verified-source | `0x77021100bd87b7008e5e1989d0eb38555d0d0000` | SemiModularAccount7702 | 320 | 319 | 17 | 72% | 11 of the 319 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| unverified-source | `0xcda3577ca7ef65f6b7201e9bd80375f5628d15f7` |  | 242 | 242 | 1 | 97% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| no-code | `0x0000000000000000000000000000000000000000` |  | 220 | 165 | 102 | 0% | 71 of the 165 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Delegating to the zero address clears a delegation (revocation). |
| unverified-source | `0x4eff4d390d89b2195fe3cb63b06731ae584a1375` |  | 217 | 217 | 11 | 100% |  |
| unverified-source | `0x5328cb0accfb156354710d3d04452963a17af63e` |  | 215 | 215 | 1 | 99% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| unverified-source | `0xff26b51fb5a6420453f362e26dc5e3d5adbfa208` |  | 203 | 203 | 1 | 100% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| forwards-incoming-eth | `0x2e13de8763a53a6af340930fadcad966ee79c845` |  | 193 | 100 | 79 | 1% | 29 of the 100 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x63e2f0bf6966256dad9c590de0fb68acc81c1f51. |
| verified-source | `0x000000005c84f8fd50b21cac312528a64437030e` | CaliburEntry | 190 | 186 | 76 | 55% | 2 of the 186 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x03a8a3ae0b496f6988f467798beb60bd3c81f4ac` |  | 175 | 87 | 1 | 0% | Unverified, but its bytecode is 92% similar to CrimeEnjoyor (0x84d05511614272694d3a9cebe896514dbde51f40) and exposes the same function selectors. 87 of the 87 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x8863786bebe8eb9659df00b49f8f1eeec7e2c8c1. In 1 of those, the receiving address is written in the delegated account's own storage slot 0, so each account can carry its own payout address. |
| evidence-missing | `0xf4b2569a806c1f4d1be0cebc3f0475a3d17a1c4d` |  | 174 | 66 | 1 | 1% | 25 of the 66 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x2d36fa3b1279eecaa198bacbd578bb4dbe139953` |  | 155 | 155 | 1 | 98% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| verified-source | `0x6c35fbcf24e57e5aa2e3aa2ca82e052499d02cf8` | TokenPocketStatelessDelegator | 152 | 152 | 59 | 52% | Verified on Sourcify; Blockscout did not report it as verified in this run. |
| verified-source | `0x5ac4c3f3d60d9186baf971aa1bda7c3924adec4c` | Utila7702Delegate | 145 | 141 | 32 | 75% |  |
| verified-source | `0x7785a22facd31db653ba4928f1d5b81d093f0b2f` | BasicSmartAccount | 139 | 63 | 5 | 15% |  |
| verified-source | `0x24b576bc271823bf9c24be627b4363b9b00191e9` | HermesDelegateV1 | 135 | 135 | 13 | 84% |  |
| verified-source | `0x955d84139e7621bc571b117d8eb5d28a4a222c6f` | TKGasDelegate | 124 | 124 | 91 | 98% |  |
| forwards-incoming-eth | `0xdc78583d3bb386b055174a485aacfed52ce3d37a` |  | 113 | 96 | 1 | 0% | 66 of the 96 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x11d92f0bdbbe98094595991bf5d3214252fdb662. |
| unverified-source | `0x4049d89f5c83a76aff4a1ddffc504da5e0597bff` |  | 107 | 66 | 1 | 0% | 66 of the 66 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x0f9fd457c12999245c2be5645ab61e10f787c72a` |  | 107 | 107 | 1 | 100% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| unverified-source | `0x86485b8eed03bd710bf243982392dc61f3257785` |  | 106 | 59 | 1 | 1% | 59 of the 59 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xa34e1e389097409aa65ff374af50b402e4a8f5c3` | DfnsSmartAccount | 105 | 105 | 9 | 98% |  |
| verified-source | `0x1f74b4339990db761bc0168f20d294a3a141497e` | RelayAdapt7702 | 103 | 103 | 38 | 100% |  |
| unverified-source | `0x893b612461326a6deeac2dad5ff5cf03e114772f` |  | 90 | 90 | 1 | 0% | 18 of the 90 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x79cd70284ed78fc78e459bdff06a06177f7375d9` | BatchCallAndSponsor | 78 | 78 | 10 | 100% |  |
| flagged-by-research | `0xb6da1852c218d74257593126fdfbd20f0bceb2a8` | Porwarder | 68 | 6 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 6 of the 6 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 6 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact. Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0x027f5eed8c0f8b9d8e68f60dc437175af7b52ff9` |  | 55 | 55 | 2 | 95% |  |
| verified-source | `0x31c934f4db134d3110e963044836d7a89609b783` | CTOCDelegate | 54 | 54 | 1 | 100% | Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts. |
| unverified-source | `0xc1c1e18accec66ce640633d638102b3efba4d596` |  | 49 | 4 | 1 | 0% | 4 of the 4 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 4 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xd75ba5e163fa5dd3b764f6d5c21210de3832a6ba` |  | 48 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xcc1b2113c8775c545660a8ac0bebe425da12f938` |  | 47 | 47 | 3 | 0% | 2 of the 47 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x68556d641d419817b3a8ddc9418a84352c93fb95` | EIP7702Contract | 46 | 30 | 2 | 0% | 4 of the 30 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| verified-source | `0x05ae73c5925d843864ae6f261f3175de2ebcd963` | RelayAdapt7702 | 44 | 39 | 23 | 43% | 1 of the 39 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x535023ed14a1862444ec29d0fe07cf3092c73bc2` |  | 42 | 18 | 18 | 0% | 1 of the 18 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0xe40ccb2d94975c51bff0c004efdfd9b3a5796fa4` | SmartWalletEntry | 42 | 40 | 40 | 0% | 3 of the 40 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Verified on Sourcify; Blockscout did not report it as verified in this run. |
| unverified-source | `0xfe8abbd9847af7b02ff9a43eab797917f2140e3f` |  | 42 | 36 | 1 | 19% | 3 of the 36 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0xf9b681edbe2260b5e508c78ad56878432cd548fc` | TransferDelegate | 41 | 41 | 3 | 100% | Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0x6d94554900937c5b3efb52ed21c09a4953b7c451` |  | 38 | 9 | 1 | 0% |  |
| unverified-source | `0x07241d6ae14a6605e12a5febc187885d91b40da0` |  | 36 | 29 | 29 | 0% |  |
| verified-source | `0x4cd241e8d1510e30b2076397afc7508ae59c66c9` | Simple7702Account | 34 | 34 | 5 | 9% |  |
| unverified-source | `0x54bf93ee1a08af3c90c1cf9973d6e95be9ef65d7` |  | 33 | 4 | 2 | 0% | 4 of the 4 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 4 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xcc0c946eecf01a4bc76bc333ea74ceb04756f17b` | TokenPocketSimple7702Account | 32 | 32 | 15 | 53% |  |
| unverified-source | `0x27bfd156c8c0df64e6a863c589dc9593ddac3ee2` |  | 30 | 22 | 1 | 7% |  |
| verified-source | `0xc3c89ff8589644332c916d9c6ec2883eb69d44e5` | FixedOwnerCollectProxy | 28 | 19 | 1 | 18% |  |
| unverified-source | `0xd2bc5c2823856ae0fa5c79744cf09c3e9a9ff35b` |  | 28 | 28 | 3 | 0% | 7 of the 28 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0xb55387309203aeabb56339da3c4c0fa3e7a04a96` | TransferContract | 27 | 27 | 1 | 78% |  |
| verified-source | `0x612373d7003d694220f7800eeaf8e3924c0951d3` | CaliburEntry | 27 | 27 | 27 | 0% | 1 of the 27 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x51fa1cce1c8b11dd89a053544d02c71c275cdec8` |  | 26 | 26 | 1 | 0% | 19 of the 26 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xd52573f6d4f68d8e7f8fe2ed50a1023c5f6fe82a. |
| unverified-source | `0x33f0c2f0f2377df77349bf2818c88123fcc645dc` |  | 24 | 1 | 1 | 0% |  |
| unverified-source | `0x9a6bc2f56b9bbcb5a354d336dbda10ef8febd0ec` |  | 24 | 24 | 1 | 0% | 23 of the 24 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| forwards-incoming-eth | `0x60b82581a0f2ddbf0f2f3709365f9b9081b16eed` |  | 23 | 14 | 1 | 0% | 14 of the 14 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x269ba5e2d3c430c50178134652b3a948c8b9c307. |
| verified-source | `0x00000000383e8cbe298514674ea60ee1d1de50ac` | Nexus | 22 | 22 | 7 | 86% | 10 of the 22 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0xcd7b35a913dff15a364e4611d2db1cfcb179ae5b` |  | 18 | 6 | 1 | 6% | 3 of the 6 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x07b26e3e228778b6c132b1cbaa9a716f72bbf05b. |
| unverified-source | `0x4f577087064ea4b5cf294d44cfd56275d9d1ed18` |  | 18 | 3 | 1 | 11% | 3 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 3 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xf3ed64f43472c1ccafd3afa7a3aafe0fde783141` |  | 16 | 15 | 1 | 88% |  |
| unverified-source | `0xef93688b67019e4b48f19d924f9f8c1f01fb4b3f` |  | 15 | 10 | 1 | 0% | 10 of the 10 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 8 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x3516d8db77e41319011f4265cd61e743e9b9822c` |  | 14 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x1f49381c59a867491e97b7e94923a32da1de8634` |  | 13 | 4 | 2 | 38% | Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x3d903e1e806ad3ab8a9f36b6048abf87892b5374. |
| forwards-incoming-eth | `0x1bcc6b722dd35072823ea7f80b50442aaf57aac5` |  | 13 | 13 | 1 | 100% | Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xa7c91c2911206de0d3054372d6af188fb11af07a. |
| verified-source | `0x5a7fc11397e9a8ad41bf10bf13f22b0a63f96f6d` | AmbireAccount7702 | 12 | 12 | 12 | 17% |  |
| no-code | `0x718832b571f40448a8cb543e63042660055dfc56` |  | 12 | 1 | 1 | 0% | Delegating to the zero address clears a delegation (revocation). |
| unverified-source | `0xda98669de7f4c4d5c2e41baf12574a67ecc25619` |  | 11 | 6 | 1 | 0% | 5 of the 6 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x2f5e05a65f25d7bec3d8f02a9689cdf43eccd3e6` | MerchantConsolidator | 11 | 11 | 1 | 27% | 9 of the 11 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0xad9cca330a131cd3bf3886db21d734ec60ab3076` | BatchCallAndSponsor | 11 | 11 | 1 | 100% |  |
| evidence-missing | `0x14eb85c766a24fa18a2008d9d2ba69344830e938` |  | 10 | 6 | 4 | 30% |  |
| verified-source | `0x9ed18ba902951c16c2299ac234921380743a0a67` | EIP7702AccountLogicV2 | 10 | 10 | 1 | 100% |  |
| forwards-incoming-eth | `0xa93f476e66f7b456fcca575cdb261d887c7ab463` |  | 10 | 7 | 1 | 0% | 2 of the 7 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x0991d832a8efe64d5c94678eba0f459c8ddc4b3b. |
| unverified-source | `0x74f2b03fdec0e9cc35aac867c67bc938233088fd` |  | 9 | 9 | 1 | 89% |  |
| verified-source | `0x487db2fd20522c4a3ed542249483d9a12de66b1f` | Simple7702Account | 9 | 5 | 3 | 33% | Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0x575456fa1004eb5c6331cdbbf9f0e5acce5d87be` |  | 9 | 9 | 1 | 100% |  |
| verified-source | `0xa2c6eb5f4095a19571a206f39612faadbbe702cf` | UxuySmartProxyV3 | 9 | 9 | 6 | 100% |  |
| verified-but-upgradeable | `0x7c27e3aecbf42879b64d76f604dc3430f4886462` | EIP7702Proxy | 9 | 9 | 2 | 100% |  |
| unverified-source | `0xf12286e6f4f9970146ce5239f143b2c335e417a0` |  | 8 | 7 | 1 | 0% | 5 of the 7 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0xe2aad4ae4eda149d9eb8bc885529ef2ee04f62d7` | BatchCallAndSponsor | 8 | 8 | 3 | 100% | Verified on Blockscout but not found on Sourcify. |
| unverified-source | `0x2c3cbe3b2cf2015602045e9b4b0f180897b369c1` |  | 8 | 2 | 1 | 0% | 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 2 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xb544282ddc2906de7f610e54e08e4f568997017f` |  | 8 | 7 | 1 | 0% | 1 of the 7 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0x45e87d68ff89dd2bc7729a86e776af9393ebf845` |  | 8 | 1 | 1 | 0% | Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x89fc1e38e17539e681b878eba80ba4500e12db26. |
| forwards-incoming-eth | `0x64d9de27a6d769712148e6e14118c253bbfc1633` |  | 7 | 7 | 1 | 0% | 6 of the 7 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x95b6b59ca57825eb85ff8c37242acd3fffba5b60. |
| unverified-source | `0xb197b363d5329b31fd0aeeac74c7b12602b71a69` |  | 6 | 6 | 1 | 67% |  |
| verified-source | `0x25054a2b9d4544ed292dc1a74e8bf1f6f449d988` | ProviderBatchCallAndSponsor | 6 | 6 | 1 | 100% |  |
| unverified-source | `0xc3564e2095885bd4c5dde9a3691c9bec9387fd3a` |  | 6 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x80f42d5cb6091466c74cbb135cec03c4ad4d1fc5` |  | 5 | 5 | 1 | 40% |  |
| unverified-source | `0x0000048a98ed27a0edc3f19cc52056b39b60419f` |  | 5 | 5 | 2 | 0% | 5 of the 5 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 5 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| forwards-incoming-eth | `0x8773a2868e4e113381ec94c463d51479fb9a533f` |  | 5 | 5 | 1 | 0% | 1 of the 5 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0xf87f1a3d738b5d2b7fe7045870316f9fc2ee1488. |
| unverified-source | `0x709a519eb51f7153b7560a4aa7033ee4ff45a907` |  | 5 | 5 | 1 | 100% |  |
| unverified-source | `0x343ba89125228f99f3f8afaf8d52e5add227627b` |  | 5 | 3 | 3 | 0% |  |
| unverified-source | `0x80d95b9131883cbf4ec56ab7f2d96e23ae9a8b5c` |  | 5 | 5 | 1 | 100% |  |
| unverified-source | `0xdc86dea6ee5a9d4df5b6f4ea8f469be4c1aebc3d` |  | 4 | 4 | 1 | 0% | 3 of the 4 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| forwards-incoming-eth | `0xd086d522c3e4e5b5545aa4c420ab1670718bdfa6` |  | 4 | 4 | 1 | 50% | 1 of the 4 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 3 of 3 sampled accounts delegated here was passed straight on to 0x984f1fe18f58c22d17858d489518c5b15c3fd879. |
| unverified-source | `0x953d925c9d045c719e91d9b7a8777f870ed7387f` |  | 4 | 4 | 1 | 0% | 1 of the 4 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| verified-source | `0x4986579bcdd269b3f3c51eb0954114b2694afcf4` | UDABatchExecutor | 4 | 4 | 1 | 100% |  |
| unverified-source | `0xb9a31ea25df400bf7fb7019bc8417307e8d88c03` |  | 4 | 3 | 1 | 0% | 3 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 3 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xd208fcea4077cb1bfc7d4e7d3d45ae28de430c6b` |  | 4 | 3 | 1 | 0% | 3 of the 3 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 3 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x843469f223bad7ca390a8b6137c4f87955b97568` |  | 4 | 4 | 1 | 100% |  |
| unverified-source | `0x8af0e573e5ffadfb0aaaf8703a573b46d68b2fa1` |  | 3 | 3 | 1 | 33% |  |
| unverified-source | `0x9c24f8c2980f3e99836b9e59cab0cdfe103db8e6` |  | 3 | 3 | 1 | 100% |  |
| verified-source | `0x14f01bbaa1dcff8f12bfe1cd54b58a7ebe211b29` | BronAccount | 3 | 3 | 1 | 100% |  |
| verified-source | `0x3cf32d4d57e91e0a1c3658884040889dafbe5103` | RewardyDualEntryAccountV3 | 3 | 3 | 3 | 67% |  |
| verified-source | `0xb24043ebdc72ddc1923ec749cfbdfbeff3fc82f6` | HinkalWallet | 3 | 3 | 1 | 100% | Verified on Blockscout but not found on Sourcify. |
| forwards-incoming-eth | `0x42505b8dac31d70bd9d9006c7ffface81544dee6` |  | 3 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x94943b987a73fa0213f540d6efea887fc73bf6ea. |
| evidence-missing | `0x00000000228a69a77a83bba0d354505b8d17dc65` |  | 3 | 3 | 3 | 100% |  |
| unverified-source | `0x08bf3aa11cf3063ae49c9383e74eb72b3329aa24` |  | 3 | 3 | 3 | 0% |  |
| verified-source | `0x86dd7fdd4207bb569b822ca80e8ab46d7dc6c0e5` | Safe7702Executor | 3 | 3 | 1 | 67% |  |
| flagged-by-research | `0x540fe9bec2470e93aa911906eb560ad6647612c2` | CrimeEnjoyor2 | 3 | 1 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact. Verified on Blockscout but not found on Sourcify. |
| verified-source | `0xe3014e9ab2739adef234b3829c79128746160178` | Tangem7702GaslessExecutorL1 | 3 | 1 | 1 | 33% |  |
| unverified-source | `0x6d4be179527a261e8651d3ba3bc44a612149f926` |  | 2 | 1 | 1 | 0% |  |
| forwards-incoming-eth | `0x69d016bcdc926b3719d6e1c239e0d3a5fca43c20` |  | 2 | 1 | 1 | 0% | Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x6c48d8ae9107d3c91b71e09f57282505d19c4123. |
| verified-forwarder | `0x3ae1f70cf6da80955936f5599d103fcf62162d10` | Reconstructed | 2 | 2 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 2 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 2 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xc3be6c19e34f899086fe7ab22bbb0ad7615db802` |  | 2 | 2 | 1 | 0% |  |
| unverified-source | `0x0000886f49de8c71a20f7f8cd681e2b8f0bb2982` |  | 2 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xef40acdb728e0feabafb07ab89bd0cdc9d3d7fab` |  | 2 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x1eaac9b1ef52cb538972d510251ab78c09c571d6` |  | 2 | 2 | 1 | 0% | 1 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x555281e828e907fc1c0b3b09c28685b45762125c` |  | 2 | 2 | 1 | 50% | 1 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| evidence-missing | `0x119013a9a45ed5b3afc2d1623724985a34ca60d8` |  | 2 | 1 | 1 | 0% |  |
| unverified-source | `0x2b0f06f7717bb606d0c7cdf0df3960c980be0c52` |  | 2 | 2 | 1 | 0% |  |
| no-code | `0x789bdc19cf81c477f9636942130d88c9234fc592` |  | 2 | 1 | 1 | 0% | Delegating to the zero address clears a delegation (revocation). |
| forwards-incoming-eth | `0x77f64403a328ffd675bc12e18bff559242a7f510` |  | 2 | 2 | 1 | 50% | 1 of the 2 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0xa61919b4591110c344b3c7fb231dcb4e2df10e8a. |
| unverified-source | `0x06346b700d2858bfe43bf29b9a3bd8f07aa28061` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x47e747f5e8cb5819c966292dd969d989ae9dea5e` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0xa58588fbff536471a529833eb7fb818d7287844f` | ETWallet | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd29b6e697011b1545a3f6fc90f80bf414061cff6` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9a65e0e0a2139b6118b6f81a525aab0ff4d878ba` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc2f4fb855519ba324ff7bf4e0ed3c8b7a627cec2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe59bd876911511604a480a694e316c079c742ebe` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2abf7bd195624b5f87af3b763de317e97ea1e377` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5ae50d3a608b1cb5b64cf4857930320d80ca0a87` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc9411fd11afd0321e41d80d8497fafa36290ecbf` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1543590e29a8ad32083edd37ecddad274e4bd11b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xaeaabfe720c8eb3d362b9330d69ed3800142230e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x79b69c0b230a9f79bf3ddb544150f5761270fb28` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x59e6c7e691f03f2e00eb02155ec3932d91864d87` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3910e2e45e3a87c773b9bac3fbe1fee618178a59` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1d66f678ebeedd9885a89797a26a0e412d91f29a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x47b98640276e3753f402bcecc74b6a56f47340b3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb5abae6655ae9d0939a6dfd636e9e48644fde54e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9bca1f74e2d6d0ea5ace7e795b50c4c71e6a868a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x787a731e14d5d85db0301c3d4e4273d75b143508` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4f83dab4b51902cbfb0548d49f70fecf2078ffe1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7e6110a95857777f2bea1b9a55971667f012dad4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb1e9b01c469b7647ddc3eca18ab69cd3f9ec2d0a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc32ec9d63088f7aeeae93c124fcccc804686f8b0` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x059f7335a30085186327446253aab0fa7a543f2b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc62d4deb2fce7b455210d8acfb7a722760e357e1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8c60cd01b8e0881505db1d077e4f14e6292fc792` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa1d9a987b5e2bfd17b62f0681c99003a6e4593ce` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5a825cf6f427de6ae9b3bf0d8f188d2a1065dc70` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3d1568b8ceec4bc443e0f5960f6cc06b24cc98f7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb5673b58abb77850aacf418ddddb6c1fcf35e843` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x741112b9acfcce0105ddc54d0be0aa3ebbc5e380` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6554865bc2df8d1694e1c431482c846fb22e67b7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb49a066925723789caaf76b79c076328899348ac` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdb2bdd3365c59d86ef46f2ce52974557a4a54fcd` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb9f68bea03d03867aa8b9c00ea318e96785c7b65` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2da7f30da39449d28af0128895dc3f7567216b95` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x701b3a50ebdf6ff30d6b5b71f9e9b5d1bbe5488a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x78727d5e78eb8f850cb78531ccd6334c8bb1f61a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x131d7e2ad44c0bea4b84821cc005ce02d3b40c1b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4b4cd1c1d0cec5496ef93e19e2ea835ff0c8797d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9e9e73c28ff756fe47c2be5015534f45e3728913` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1a3a19966c2bf1fac4f21df2823e03a30a1df0af` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe68d96322b6461a166a2a006b56e937d6975dfb5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4faeda09cbd216dea5db66e2c305fab01b9d4bea` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd597bcc921901c2f8892efabc395c878cbd058e7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x47a5b3df8cb1738a505fda9dcf5043ee9d012d44` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6a8a7aff3589fe34db5c2664c720cfc089ed001b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1d589def1081a68c205ed0201f661f799b406b83` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3f267f68e4fc2eacd00471901f22613380266eca` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xfd30da763c29f848ebf2a1eac95d87343c7154a5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x62f3998fe7a9cd74fcc599d0a0ae0125e7da9f62` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x388f93347cab1ed7d92d9b93858013057ade0d0a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1942b6a08642bec6742846c082bd9157cdc72f70` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x490dbac18cf4de7f71f36b91c721dccca281f045` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa4979c0c0d457f63064ef33aeaa6eef1b92b9393` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb805cf6a641bc0b1a98ee780691a28e5e4517686` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb577c75e7bd00206cb7adb87eb31e5a151a61179` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8498a4197d275f123babf33d891a7c0e3c05a8ad` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x628c00f589c2fc325ab35677fd29ea134a3e8d92` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7b3542718b36d1455aac5e9bd9baa3a724fa4a26` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa468d03ec06fa88efbb50038f44a271ed5ff3a40` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc63e4ba61baf38d32917dab001bb4955e2fdfae8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2c0788c40ed00a786a4921d8a752aedd8ad7f84c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9a58fad1c5a9a4ef258e92a3db72f5c73d34b515` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7a8e504a422afea5a32a1fc3cea969d7082dc74b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x0087fe1fd8ea6550d0d7c35719480da945f605c4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb70aa4b66028ac12ec1ec30419a9723eb76d9341` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe8ec8be36d57645e49ace5535c554d40ea474e74` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x14cb9f05a23dc2f12923aed5ad98fc379f2f1515` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf947893ef62f110180dbc48a4922c28547cc4c13` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9539b76bf3b19fb52c3d0b220c0c1e7514490bc4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x361ea0e5fa8a3185a13f11b60716cf3e94f7f132` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbcbcf4a182f8369e32da53f6b16986e2297f5bb3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdfacb7a0f66493580518001150f078dcb0221ed1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3110f8eef428600f760b48ae9d32bb0bc845859a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5d1a5a73ee9972eed2fdc88908571c298279f273` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd00b23531231382156b09324c701696bee3f5afb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc84625edbdb68c20349723256e9226eecc8f5090` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x111def24a2c614baea01b6d515b28d3ab3ec63bd` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x509496817d8603771fbcf24fb22fff4fe17c193d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe8d595534917a080b4cff4c08ebc255db1064f7a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x132cd025db5fc4b3fa67d60494f253b98b788075` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9015801601c86dcf37fbc12d7938c809f2caef83` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x2d5de071d225c75be0a691e8ac467125340576cc` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xaffe846b25fd1afa00b4dc5a8227bafd97fb3466` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x313d1b440d2d01a16e3419783df04b0b19574546` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8500f275b7edf4a6a361406e0de80af4f6948632` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5d1515d5c94683fc6da9ce8a56587da956e04c18` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xeaefeaeae7b74c4293962bc3b709bbc14baca494` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xaf66dded62b8bde9af09a0c94c16535283aeb3f0` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7b46c2a25093512af1f6a17b266b27bf55992062` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xfeff29ccae6ef1c473e6987c557c88c6a1ae8cef` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe09a481cef6ad8865f93f6be91c17245750693b2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdc9bdfcad017acb096b39fe13220976136381145` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x87d72b7475c60ae4342e5db66c65e34cefcda03e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x204a4c3d9e613b7e82a0d4646b5ca19dce86b72f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc18a246d398768dbefdbcbb51867506ff333ed88` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x51fc5862b8c7c631673179296c8cef5dd8db5898` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe076b5851113d8d8766f08093218a51a9cfc2bde` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd724009ed800d7cfaa82aae0368a32f34434b510` |  | 1 | 1 | 1 | 0% |  |
| verified-source | `0xa46cc63ebf4bd77888aa327837d20b23a63a56b5` | Simple7702Account | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa335adc0b9c14a5a2bc6a06163503f1bd45eab7f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe98fa6609d8925149644cfb62c76a2dd110bfe19` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xac4f2e245b2286d622350c1aa2b0e35653a46a87` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5071b27c25537e39fbbc09d7822e955f0938b76a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd07df3d5e689a0f3ab2e527bfe2c015f522b2e17` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc4498a4e9e35c73b0ddd55ec801e49a4c1a99b88` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4171c7e33b6db58dfe8f9689839be03cdc544de2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf152f2c6f325c22a063cf8df47b3daee9378ded5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf1628fec5f7c9b087110993e6b45826bf8c34521` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe3a189c4f3584e71c0afdf230c1bd2bb85fba5b0` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa45b84dfac01d9acd2a09f5dce19dc7dc5fce9e9` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe4c6bb827b229eb96620c47879bbd08f70440fa2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3b7f030bb3b906e949452daf3259e632eed5ca97` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xc40d76e94f47d5b98f28dc83ef154e228dd035ee` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3210cd9b34d1729e349b9aaacb13dd5efd037f15` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x029019c57a94ee726e22f200f7a8b3560761b9a0` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf0881027c7d1b1abf29bc7e1fed1e1838fb1ff4a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x4120d12b0c2f2d749462ba23a94d4fa011f1338f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7bb8942d87aaf5a5e7b9ed3f049f6ffdfbb8184e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc54b353b348d7a1c7e946d1d05920d9cb63be367` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x588f234ee82e02e4c71fd937cd8358aab07e673f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x35434c92db52a751103a4804d8dc3ce2cd15ebe5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9e435a840a8a2e93d6dff54a92ded99126770a82` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x68ce21a125c40f42fd3c7cf9adb6361dc82ea736` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x90546ca005bb8905393d40a29992af1e1d7d85d6` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe74ea885de4cd6199e9517b308bc05ea92f4e624` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xca00f62fbfb47f0dc6d825f314be54771172f1c4` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x49255e3ee8f8e37d901a123e93a2627a68d76c59` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x00efb866cd18d099406f10b6366fa395ff823c67` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe71c7a38db1ba3a099a7aac4a61ab26f6b6be05a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe36ea2e70fcbb2bb5429f7c358d331247f2b2b5b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9a85ed70ed619045a254c7ee16873be31ce311ee` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x779236ad34b011287dfd7a1b1323a6896a609ce1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x96c7eb987fb3289500464e44fa2c2b82fc35fbbe` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb3b485c44165b96cb3601515137f2c2ffe0bbe4a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x08b0e5c60dfb153a18a900d15ef0d670366dc16f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc4c225d7fadc9028d5784a99b81da4f15dd7b5be` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3fb9520f3dab315a98832e1c4cac6b9c31f6e0c5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe187fd85cb5ff1d8b97af62fa833639a2a33d53c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x3e730a98a9b73ea350c19f81a21fd3f8659fb8e8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xdd38cdc3011b2de6acf238b81c30aa9db095e2d6` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x33c1154274b0bb03b5458ae306a9f6dd4751b1d7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf503119df97b89a0eff53cf81a463dd3a5c40ead` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9eee4ad25ace8ab1440bc14a9ae530c265c0f0d3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf470a5c1d37b68c07924b8d2486b7ed4ed21b685` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8ffbea4278bc7fa426b03f8f822c6896fdf1f5a7` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb298ac6a02c9bdd43cee84d66f6e4195292109c5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb7c31ade18b2120cfc2b1d69bb23e8a1d4d25edf` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x00358e56ecd4346aac86472ca943dd8de83e4204` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xc2080a5d3ae2353cbd8b2ba4ae882f653d084d24` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd429285004a4288e050255821f1bfb2cb14ad329` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x01799625c0cecf5a5f03e92d85455ae8db9cc13e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x36db933ff5523e1c9b6d21e3a5f80d815caa41d3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x9a836be915a8835bfb7bafcc3308f32d56c9baf8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x15285b0b7e39c5e01e691847dfae7039ad153e33` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x51fc3eee4d8b13884e3f42ca627b7f3ab7027db0` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x42e6eb5badb7802c1713356ff0357186f01db3e3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa3ccfae17985a0e7a4a53a3694f19869135c053a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x75a91f91cf95d35e1a8a90fd85fe4f7096b02718` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x593e6cd86c90df827096435e62ab7c5dfb320069` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x10522b937063a5f71afd8cc81093be767f57fc73` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbec3fc823658d0a67214ce045e63e8e6b7861692` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd8fa6dc8ea6ade4cbb6d99fa101e34e5916e792b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x05c7d9dc0397815481a45698dc7d2f80c24dad0c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x51793c994fd336f4c9e3d3e64ac6edd6758b2c8f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6fa1f780714a40451179f0a605969199d788d18c` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1b61d06bfcb57bb166b61563f7d2928a519980a8` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x226908c91f1641872adc377f603f26572f41aa51` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x80e2c18c02edbbbc2fe988150538a4fa7d68aedb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd261d8496924175a7b42f160d0ac2bb302263144` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x77dae9d2cef61a2c40724d39c0895837cc8b445a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8ab9ae8da1c2658b2262f19e61aa52b39a4a4927` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x22ba6d5302f8343033a658765d950ea56a71db08` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7279066fead8f6af58d4f16e7c21ba042c90c721` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x5f5c7698d18a8f2aa2a2601f4309b68410902ff2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x750fcf92253d5a9ee8fd4966f2f3543300bff19a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x1b48ea0409b60f1f75f947078abf0b9c4d7ee3cc` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7fbe8571eba3d661a8b5ece5792f5448646c5fa2` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xea03932d61b47ea3186a009a670607d4caf032eb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa8842afff1b6097bc4816c242f2a83bf3148d95b` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd79009c61f9df6de2d780406136ee22b98942fc3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xa21914e79d2491a78591b0ad99087c61723bb429` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf41f7729b92bc200fa13da04b0cde65aea6adb22` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xd1fce7e2d8b4eed3c9b8683b32df923e342cd88e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x65f9b12e97a3ba1e16f9de6c92a15e5def36de1e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf5e302a3eb32c9c1f77c6ab69bdc630c6b18d94e` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x06f9de81c56d464a81be3fdd33ead1898e7c7f17` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x832d2d5a3d66c16df3033895a3a2906d48dbb29f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xb47e9e6228fcfbaaf2d65f8d0748127c0b04ed78` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x700687d73a3e3c019ed10caf54d2c95403ea50ab` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xbaefbe2a090347b7e8f81cd65414fc03d2ab8660` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf91ed512b8e759b32677dd05f504382dfc588e6d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xe72d0c7c2b2bd767acd3ca8353c4a2455c2596cb` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x8f2d28889bfb5d00bcbfca3ea7d5adb253477e5f` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x13fe575bff9ce38785d2af1d994b90b9da7158a3` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x943ade3c448ecfb6effb2056fc2168958c31374d` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x7ed2e03310b14e409efaaed2f294ef93fea5f1ee` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x78af478b9cfbff75f29726f168f163865dc3baf1` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xab8ffd14ceefc6b62dbc978dd927d2405e5d50e9` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x0b429d3b676234299cd06d6365539b59c8627ad1` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x3d965cfdda791589ccab955498d509f2f7e30b79` | Atlas | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x87dc58542dbda22af93f122f289969b3cf7609b6` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| verified-source | `0x9c34ac9479ea7b9f5df8525ff5ed98363057a87e` | Crime | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x91b145d4874b04cbce68c80886c6de7cfb945317` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x6153015c73f59916e442397bffe999d2adca8f4f` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0xeb22a9d52f13d3887e358b4c28ad13ee90d2f0ab` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0xd1945bda1c461f68e0157e14c4f97ee3a6444f22` |  | 1 | 1 | 1 | 100% |  |
| forwards-incoming-eth | `0x32ecfd6b17e48b760714a76a4155cca1e82daf1a` |  | 1 | 1 | 1 | 100% | Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x7190aa3a9c0fd2c847b14dfa3f9109288fa76990. |
| verified-source | `0x5884bff4876c979271e65d2fea8d0cf3bf6e6ccc` | Delegate | 1 | 1 | 1 | 100% |  |
| forwards-incoming-eth | `0xe6dd12cf1db2c7afb34865d753780fe714622a6a` | Executor | 1 | 1 | 1 | 0% | Dry run: 1 wei sent to 1 of 1 sampled accounts delegated here was passed straight on to 0x47fa538ae6c1aec385b17e903463bafe132c9a8b. |
| verified-source | `0x268d193d74d3b9a13a82da831302cf8dbdc9245a` | Simple7702Account | 1 | 1 | 1 | 100% |  |
| unverified-source | `0xfb1b8fb55d1aabeb96bc1c36a9754b28e46a8b6a` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x81e665a2d9099c726071566e0a2061db28e82701` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xd5adabc8f98a485c8efa50599afbe926b3e6dd49` |  | 1 | 1 | 1 | 100% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xa660b149f2dee492c62ad502a920c4ed4f0830e0` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| evidence-missing | `0x8da00456ffc3a0ba1a69d359ad1447b88a4285b0` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x7d091cb2e1d577c431cbda26677c3ae8f57fce92` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xf93ac5526713239ad575b25afbb8fb9d50b2e6fb` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xd00e628a486a7d48471e918623332de5b98e0103` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x8616ed1a686bdb577814db0377a102e82f5097d6` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x755d74a5fb74146eecad950bb3a8d1020b8f5688` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xe6259d8fa4535273a5bf00287f6d350c556a940d` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x80a9b429f90b28f9e530429acfea931250626061` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x40500e54cfbd716fedc767040f313da2c50c8d28` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x3f760f303789032d72f740c5178ef6298aa79cd5` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0x13e00e089f81ad9f36b655c9e9a07c6bf1489a5a` |  | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x5d5f27872742a38745e9563f3b02f34982887d7a` |  | 1 | 1 | 1 | 0% |  |
| unverified-source | `0xaabc3661d6c3458236b542272ed765e028e1a74d` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x532ba46934e877585b293d582ab6a6b62f0cee44` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x2852a7cc5b6520278104527f495e474ef49e5ebf` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). |
| unverified-source | `0x51d5a11e467f9cc6439f627ad73e34d0964bdcea` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x5546a14921647a6fc3c8927a2c0cc3afe2e9ae77` |  | 1 | 1 | 1 | 0% |  |
| verified-source | `0x3e515544f8d8293b0a353e10ff3b7ca03b52f35b` | MinimalAccount | 1 | 1 | 1 | 100% |  |
| unverified-source | `0x336fc59d52ab7ddec13495a595f6fe1b4bcbd2bd` |  | 1 | 1 | 1 | 100% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0x78608e7a956fe1ca4af4a31138fd67779b08f9b5` |  | 1 | 1 | 1 | 0% |  |
| verified-forwarder | `0x4182d1c577dcee57b72993ff35926cf84582ab48` | Support | 1 | 1 | 1 | 0% | Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there. 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
| unverified-source | `0xdd19eed97b6d55582fe51c6ea9172cb175b429ba` |  | 1 | 1 | 1 | 0% | 1 of the 1 accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth). None of the 1 sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared). |
