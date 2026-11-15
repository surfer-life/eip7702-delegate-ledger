// Delegate Ledger — everything runs in the browser. No wallet code, no analytics.
"use strict";
const RPC = {
  ethereum: ["https://ethereum-rpc.publicnode.com", "https://eth.drpc.org"],
  base: ["https://mainnet.base.org", "https://base-rpc.publicnode.com"],
};
const LEDGER = "https://raw.githubusercontent.com/surfer-life/eip7702-delegate-ledger/main/data/latest.json";
const EXPLORER = { ethereum: "https://eth.blockscout.com/address/", base: "https://base.blockscout.com/address/" };
const BLACKLISTS = [
  { chain: "ethereum", token: "USDC", contract: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", sel: "0xfe575a87" },
  { chain: "ethereum", token: "USDT", contract: "0xdAC17F958D2ee523a2206206994597C13D831ec7", sel: "0x59bf1abe" },
  { chain: "base", token: "USDC", contract: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", sel: "0xfe575a87" },
];
const GRADE = {
  "known-malicious": { cls: "bad", text: "known malicious" },
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

let ledger = null;
const ledgerReady = fetch(LEDGER).then(r => r.json()).then(d => { ledger = d; renderLedger(); }).catch(() => {
  $("window").textContent = "Could not load today's ledger. The lookup above still works.";
});

function pill(grade) { const g = GRADE[grade] || { cls: "", text: grade }; return el("span", { class: "pill " + g.cls, text: g.text }); }

function renderLedger() {
  const w = ledger.window, rows = ledger.delegates;
  $("window").textContent = `Ethereum blocks ${fmt(w.from_block)}–${fmt(w.to_block)} (${w.from.replace("T", " ").replace("Z", " UTC")} to ${w.to.replace("T", " ").replace("Z", " UTC")}): ${fmt(w.authorizations)} authorizations pointing at ${fmt(w.delegates)} contracts.`;
  const order = ["verified-source", "unverified-source", "known-malicious", "resembles-known-malicious", "evidence-missing", "no-code", "verified-but-upgradeable"];
  const color = { "verified-source": "var(--ok)", "unverified-source": "var(--warn)", "known-malicious": "var(--bad)", "resembles-known-malicious": "var(--bad)" };
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
      el("td", { class: "num", text: fmt(r.authorizations) }), el("td", { class: "num", text: fmt(r.distinct_senders) }), el("td", { text: (r.notes || []).join(" ") }));
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
  const title = row.grade === "known-malicious" ? "Delegated to a known malicious contract" : row.grade === "resembles-known-malicious" ? "Delegated to a contract that resembles a known malicious one" : row.grade === "verified-source" ? "Delegated to a contract with published source" : "Delegated to a contract whose source is not published";
  return card(g.cls || "warn", chain, title,
    kv([["Points at", link], ["Name", row.name || "(none reported)"], ["Evidence", pill(row.grade)],
        ["Last day", `${fmt(row.authorizations)} authorizations from ${fmt(row.distinct_senders)} sender${row.distinct_senders === 1 ? "" : "s"}`]]),
    (row.notes || []).join(" "),
    row.grade === "known-malicious" || row.grade === "resembles-known-malicious" ? el("p", {}, el("strong", { text: "Do not send funds to this address." })) : null,
    el("p", { class: "muted small", text: at + " While an account is delegated, the contract's code runs as the account. If you did not set this delegation yourself, treat the account's key as compromised. \"Source published\" means the code is readable, not that it is safe." }));
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
    out.replaceChildren(el("p", { class: "muted small" }, "Result for ", el("code", { text: addr })), ...parts);
    history.replaceState(null, "", "?address=" + addr);
  } finally { btn.disabled = false; btn.textContent = "Check"; }
});
const pre = new URLSearchParams(location.search).get("address");
if (pre && /^0x[0-9a-fA-F]{40}$/.test(pre)) { $("a").value = pre; $("f").requestSubmit(); }
