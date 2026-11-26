import { execFileSync } from "node:child_process";

export function reconcile(item) {
  const program = "from allocation import allocate; import json, sys; a=json.load(sys.stdin); print(json.dumps(allocate(a['amount'],a['currency'],a['shares'],conserve_units=True)))";
  const { amount, currency, shares } = item;
  return JSON.parse(execFileSync("python3", ["-c", program], {input: JSON.stringify({amount,currency,shares}), encoding:"utf8"}));
}
