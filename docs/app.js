// Delegate Ledger — everything runs in the browser. No wallet code, no analytics.
"use strict";
const RPC = {
  ethereum: ["https://ethereum-rpc.publicnode.com", "https://eth.drpc.org"],
  base: ["https://mainnet.base.org", "https://base-rpc.publicnode.com"],
};
const LEDGER = "https://raw.githubusercontent.com/surfer-life/eip7702-delegate-ledger/main/data/latest.json";
const CONTESTED = "https://raw.githubusercontent.com/surfer-life/eip7702-delegate-ledger/main/data/contested.json";
const EXPLORER = { ethereum: "https://eth.blockscout.com/address/", base: "https://base.blockscout.com/address/" };
const BLACKLISTS = [
  { chain: "ethereum", token: "USDC", contract: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", sel: "0xfe575a87" },
  { chain: "ethereum", token: "USDT", contract: "0xdAC17F958D2ee523a2206206994597C13D831ec7", sel: "0x59bf1abe" },
  { chain: "base", token: "USDC", contract: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", sel: "0xfe575a87" },
];
const GRADE = {
  "known-malicious": { cls: "bad", text: "known malicious" },
  "flagged-by-research": { cls: "bad", text: "flagged by research" },
  "verified-forwarder": { cls: "bad", text: "published source forwards funds" },
  "forwards-incoming-eth": { cls: "bad", text: "passes incoming ETH on" },
  "resembles-known-malicious": { cls: "bad", text: "resembles known malicious" },
  "unverified-source": { cls: "warn", text: "source not published" },
  "verified-source": { cls: "ok", text: "source published" },
  "verified-but-upgradeable": { cls: "ok", text: "source published, upgradeable" },
  "evidence-missing": { cls: "", text: "no evidence this run" },
  "no-code": { cls: "", text: "revocation (no code)" },
};
const $ = id => document.getElementById(id);
const el = (tag, attrs = {}, ...kids) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) { if (k === "class") n.className = v; else if (k === "text") n.textContent = v; else n.setAttribute(k, v); }
  for (const k of kids) n.append(k);
  return n;
};
const short = a => a.slice(0, 8) + "…" + a.slice(-6);
const fmt = n => Number(n).toLocaleString("en-US");

async function rpc(chain, method, params) {
  let last;
  for (const url of RPC[chain]) {
    try {
      const r = await fetch(url, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ jsonrpc: "2.0", id: 1, method, params }) });
      const d = await r.json();
      if (d.error) throw new Error(d.error.message || "rpc error");
      return d.result;
    } catch (e) { last = e; }
  }
  throw last || new Error("no node answered");
}

let ledger = null, contested = null;
const ledgerReady = fetch(LEDGER).then(r => r.json()).then(d => { ledger = d; renderLedger(); }).catch(() => {
  $("window").textContent = "Could not load today's ledger. The lookup above still works.";
});
fetch(CONTESTED).then(r => r.json()).then(d => { contested = d; }).catch(() => {});

function contestedCard(addr) {
  if (!contested || !contested.accounts) return null;
  const c = contested.accounts[addr.toLowerCase()];
  if (!c) return null;
  const card0 = card("bad", "re-delegated account", "This account is being fought over by sweepers",
    kv([["Authorizations in the window", fmt(c.authorizations)], ["Delegated to", (c.targets || []).length + " different sweeper contracts in the same window"]]),
    "This account was re-delegated back and forth between different sweeper contracts many times. That pattern means its private key is compromised: anyone who funds it will have the balance swept away in the same block.");
  card0.append(el("p", {}, el("strong", { text: "Do not send anything to this address." })));
  return card0;
}

function pill(grade) { const g = GRADE[grade] || { cls: "", text: grade }; return el("span", { class: "pill " + g.cls, text: g.text }); }

function renderLedger() {
  const w = ledger.window, rows = ledger.delegates;
  $("window").textContent = `Ethereum blocks ${fmt(w.from_block)}–${fmt(w.to_block)} (${w.from.replace("T", " ").replace("Z", " UTC")} to ${w.to.replace("T", " ").replace("Z", " UTC")}): ${fmt(w.authorizations)} authorizations pointing at ${fmt(w.delegates)} contracts.`;
  const bad = (ledger.share_of_authorizations_by_grade["known-malicious"] || 0) + (ledger.share_of_authorizations_by_grade["resembles-known-malicious"] || 0) + (ledger.share_of_authorizations_by_grade["flagged-by-research"] || 0) + (ledger.share_of_authorizations_by_grade["verified-forwarder"] || 0);
  const st = $("stat");
  if (w.distinct_accounts) { st.textContent = `Last day: ${fmt(w.distinct_accounts)} accounts signed EIP-7702 delegations on Ethereum. ${fmt(w.contested_accounts)} of them were re-delegated back and forth between different contracts and produced ${(100 * w.authorizations_from_contested / w.authorizations).toFixed(0)}% of all authorizations.`; st.hidden = false; }
  else if (bad > 0) { st.textContent = `Last day: ${(bad * 100).toFixed(0)}% of EIP-7702 authorizations on Ethereum pointed at known scam contracts. Most of those are the scammers' own throwaway accounts, not victims.`; st.hidden = false; }
  const order = ["verified-source", "unverified-source", "known-malicious", "flagged-by-research", "forwards-incoming-eth", "verified-forwarder", "resembles-known-malicious", "evidence-missing", "no-code", "verified-but-upgradeable"];
  const color = { "verified-source": "var(--ok)", "unverified-source": "var(--warn)", "known-malicious": "var(--bad)", "resembles-known-malicious": "var(--bad)", "flagged-by-research": "var(--bad)", "verified-forwarder": "var(--bad)", "forwards-incoming-eth": "var(--bad)" };
  const bars = $("bars"); bars.replaceChildren();
  const legend = el("div", { class: "legend" });
  for (const k of order) {
    const v = ledger.share_of_authorizations_by_grade[k]; if (!v) continue;
    const s = el("span"); s.style.width = (v * 100) + "%"; s.style.background = color[k] || "var(--mut)"; bars.append(s);
    const d = el("span", {}, el("span", { class: "dot" }), `${(GRADE[k] || { text: k }).text} ${(v * 100).toFixed(1)}%`); d.firstChild.style.background = color[k] || "var(--mut)"; legend.append(d);
  }
  bars.after(legend);
  const tb = $("t").tBodies[0]; tb.replaceChildren();
  rows.forEach((r, i) => {
    const tr = el("tr"); if (i >= 15) tr.hidden = true;
    const a = el("a", { href: EXPLORER.ethereum + r.delegate, rel: "noopener", class: "addr", text: r.delegate });
    tr.append(el("td", {}, pill(r.grade)), el("td", {}, el("span", { class: "name", text: r.name || "(no name)" }), a),
      el("td", { class: "num", text: fmt(r.authorizations) }), el("td", { class: "num", text: r.distinct_accounts == null ? "–" : fmt(r.distinct_accounts) }), el("td", { text: (r.notes || []).join(" ") }));
    tb.append(tr);
  });
  if (rows.length > 15) { const b = $("more"); b.hidden = false; b.textContent = `Show all ${rows.length} targets`; b.onclick = () => { for (const tr of tb.rows) tr.hidden = false; b.hidden = true; }; }
}

function card(cls, chain, title, ...body) {
  const c = el("div", { class: "card " + cls }, el("div", { class: "chain", text: chain }), el("h3", { text: title }));
  for (const b of body) if (b) c.append(typeof b === "string" ? el("p", { text: b }) : b);
  return c;
}
const kv = pairs => { const dl = el("dl", { class: "kv" }); for (const [k, v] of pairs) dl.append(el("dt", { text: k }), el("dd", {}, v)); return dl; };

async function lookupChain(chain, addr) {
  let block, code;
  try { block = await rpc(chain, "eth_blockNumber", []); code = (await rpc(chain, "eth_getCode", [addr, block])).toLowerCase(); }
  catch (e) { return card("warn", chain, "The node did not answer", "I can't say anything about this chain right now. Try again in a moment."); }
  const at = `Read at block ${fmt(parseInt(block, 16))}.`;
  if (code === "0x") return card("ok", chain, "Plain account, not delegated", `No code at this address. ${at}`);
  if (!(code.startsWith("0xef0100") && code.length === 48))
    return card("", chain, "This is a contract", `It has ${fmt((code.length - 2) / 2)} bytes of its own code, so it is not a delegated account. ${at}`);
  const target = "0x" + code.slice(8);
  const row = chain === "ethereum" && ledger ? ledger.delegates.find(d => d.delegate === target) : null;
  const link = el("a", { href: EXPLORER[chain] + target, rel: "noopener", class: "addr", text: target });
  if (!row) {
    return card("warn", chain, "Delegated to a contract I have no evidence row for", kv([["Points at", link]]),
      chain === "ethereum" ? "This contract was not among the targets seen in the last daily window. Open the link and check whether its source is published before trusting it." : "The ledger only covers Ethereum mainnet so far. Open the link and check the contract yourself.",
      el("p", { class: "muted small", text: at + " While an account is delegated, the contract's code runs as the account. If you did not set this delegation yourself, treat the account's key as compromised." }));
  }
  const g = GRADE[row.grade] || { cls: "warn", text: row.grade };
  const title = row.grade === "known-malicious" ? "Delegated to a known malicious contract" : row.grade === "resembles-known-malicious" ? "Delegated to a contract that resembles a known malicious one" : row.grade === "flagged-by-research" ? "Delegated to a contract a published study marked as malicious" : row.grade === "verified-forwarder" ? "Delegated to a contract whose published source forwards incoming funds" : row.grade === "forwards-incoming-eth" ? "Delegated to a contract that passes incoming ETH on" : row.grade === "verified-source" ? "Delegated to a contract with published source" : "Delegated to a contract whose source is not published";
  return card(g.cls || "warn", chain, title,
    kv([["Points at", link], ["Name", row.name || "(none reported)"], ["Evidence", pill(row.grade)],
        ["Last day", `${fmt(row.authorizations)} authorizations from ${fmt(row.distinct_senders)} sender${row.distinct_senders === 1 ? "" : "s"}`]]),
    (row.notes || []).join(" "),
    row.grade === "known-malicious" || row.grade === "resembles-known-malicious" || row.grade === "flagged-by-research" || row.grade === "verified-forwarder" ? el("p", {}, el("strong", { text: "Do not send funds to this address." })) : null,
    el("p", { class: "muted small", text: at + " While an account is delegated, the contract's code runs as the account. If you did not set this delegation yourself, treat the account's key as compromised. \"Source published\" means the code is readable, not that it is safe." }));
}

// Dry run: what would happen to 1 wei sent to this address right now? Nothing is sent; the node only simulates it.
async function dryRun(addr) {
  const from = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2";
  try {
    const r = await rpc("ethereum", "eth_simulateV1", [{ blockStateCalls: [{ calls: [{ from, to: addr, value: "0x1" }] }], traceTransfers: true, validation: false }, "latest"]);
    const c = r[0].calls[0], me = addr.toLowerCase(), out = [];
    for (const l of c.logs || []) {
      if (l.address.toLowerCase() !== "0x" + "e".repeat(40) || l.topics.length < 3) continue;
      const f = "0x" + l.topics[1].slice(-40), t = "0x" + l.topics[2].slice(-40);
      if (f === me && t !== me) out.push(t);
    }
    return { ok: c.status === "0x1", sentOnTo: [...new Set(out)] };
  } catch (e) { return null; }
}
async function dryRunCard(addr, delegated) {
  if (!delegated) return null;
  const d = await dryRun(addr);
  if (!d) return card("", "dry run", "Could not simulate a transfer", "The node did not run the simulation, so I can't say where ETH sent here would end up.");
  if (d.sentOnTo.length) {
    const c = card("bad", "dry run · ethereum", "ETH sent here would be passed straight on", "I asked a node to simulate sending 1 wei to this address (nothing was sent). In the simulation the ETH left again in the same transaction, to:");
    for (const t of d.sentOnTo) c.append(el("p", {}, el("a", { href: EXPLORER.ethereum + t, rel: "noopener", class: "addr", text: t })));
    c.append(el("p", {}, el("strong", { text: "Unless this is a forwarding setup you created yourself, do not send ETH to this address." })));
    return c;
  }
  return card(d.ok ? "" : "warn", "dry run · ethereum", d.ok ? "ETH sent here would stay here" : "A plain ETH transfer here would fail",
    d.ok ? "In a simulated transfer of 1 wei (nothing was sent) the ETH was not passed on. This only covers ETH arriving by a plain transfer; whoever controls the delegated code may still be able to move funds later."
         : "The simulated transfer reverted. That is unusual for an account and worth understanding before sending anything.");
}

async function blacklists(addr) {
  const arg = addr.slice(2).toLowerCase().padStart(64, "0");
  const res = await Promise.all(BLACKLISTS.map(async b => {
    try { return { ...b, frozen: BigInt(await rpc(b.chain, "eth_call", [{ to: b.contract, data: b.sel + arg }, "latest"])) === 1n }; }
    catch (e) { return { ...b, frozen: null }; }
  }));
  const any = res.some(r => r.frozen);
  const line = res.map(r => `${r.token} on ${r.chain}: ${r.frozen === null ? "no answer" : r.frozen ? "BLACKLISTED" : "not blacklisted"}`).join(" · ");
  return card(any ? "bad" : "", "issuer blacklists", any ? "Frozen by a stablecoin issuer" : "Not on the USDC or USDT blacklists", line,
    el("p", { class: "muted small", text: "Asked the token contracts directly (isBlacklisted / getBlackListStatus)." }));
}

$("f").addEventListener("submit", async ev => {
  ev.preventDefault();
  const addr = $("a").value.trim(), out = $("out"), btn = ev.target.querySelector("button");
  if (!/^0x[0-9a-fA-F]{40}$/.test(addr)) { out.replaceChildren(card("warn", "input", "That does not look like an address", "An address is 0x followed by 40 hex characters. Transaction hashes (64 characters) are not supported here.")); return; }
  btn.disabled = true; btn.textContent = "Reading…"; out.replaceChildren(el("p", { class: "muted", text: "Asking public nodes…" }));
  try {
    await Promise.race([ledgerReady, new Promise(r => setTimeout(r, 4000))]);
    const parts = await Promise.all([lookupChain("ethereum", addr), lookupChain("base", addr), blacklists(addr)]);
    const isDelegated = parts[0].querySelector("h3").textContent.startsWith("Delegated");
    const dry = await dryRunCard(addr, isDelegated);
    if (dry) parts.splice(1, 0, dry);
    const con = contestedCard(addr);
    if (con) parts.splice(1, 0, con);
    out.replaceChildren(el("p", { class: "muted small" }, "Result for ", el("code", { text: addr })), ...parts);
    history.replaceState(null, "", "?address=" + addr);
  } finally { btn.disabled = false; btn.textContent = "Check"; }
});
for (const b of document.querySelectorAll("[data-ex]")) b.addEventListener("click", () => { $("a").value = b.dataset.ex; $("f").requestSubmit(); });
const pre = new URLSearchParams(location.search).get("address");
if (pre && /^0x[0-9a-fA-F]{40}$/.test(pre)) { $("a").value = pre; $("f").requestSubmit(); }
