// Check a Node reconciliation agent that calls this project's Python allocator.
import { execFileSync } from "node:child_process";
import { isDeepStrictEqual } from "node:util";

const cases = [
  { id: "usd-split-cent", input: { amount: "0.01", currency: "USD", shares: {b:1,a:1}, expected: {a:1,b:0} } },
  { id: "jpy-whole", input: { amount: "100", currency: "JPY", shares: {a:1,b:3}, expected: {a:25,b:75} } },
  { id: "kwd-three-decimals", input: { amount: "1.000", currency: "KWD", shares: {c:1,b:1,a:1}, expected: {a:334,b:333,c:333} } },
  { id: "refund", input: { amount: "-0.01", currency: "USD", shares: {a:1,b:1}, expected: {a:-1,b:0} } }
];
function reconcile(item) {
  const program = "from allocation import allocate; import json, sys; a=json.load(sys.stdin); print(json.dumps(allocate(a['amount'],a['currency'],a['shares'],conserve_units=False)))";
  const { amount, currency, shares } = item;
  return JSON.parse(execFileSync("python3", ["-c", program], {input: JSON.stringify({amount,currency,shares}), encoding:"utf8"}));
}
export default {
  cases, candidate: reconcile, checks:[{id:"settlement",label:"Settlement allocation agrees"}],
  evaluate: ({input,output})=>({settlement:isDeepStrictEqual(output,input.expected)}),
  maxCallsPerRun:{baseline:0,candidate:0}
};
