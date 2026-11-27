"""Check conservation and deterministic beneficiary allocation."""
import os
from allocation import allocate


def sample(case, amount, currency, weights, total, expected):
    return {"id": case, "input": {"amount": amount, "currency": currency, "shares": weights,
                                  "total": total, "expected": expected}}


def run(item, protect):
    return allocate(item["amount"], item["currency"], item["shares"], conserve_units=protect)


def evaluate(item, output, variant):
    return {"total": lambda: sum(output.values()) == item["total"],
            "split": lambda: output == item["expected"]}


workflow = {
    "cases": [
        sample("usd-split-cent", "0.01", "USD", {"b": 1, "a": 1}, 1, {"a": 1, "b": 0}),
        sample("jpy-integer-control", "100", "JPY", {"a": 1, "b": 3}, 100, {"a": 25, "b": 75}),
        sample("kwd-three-decimals", "1.000", "KWD", {"c": 1, "b": 1, "a": 1}, 1000,
               {"a": 334, "b": 333, "c": 333}),
    ],
    "checks": [{"id": "total", "label": "Allocated minor units match the settlement"},
               {"id": "split", "label": "Each beneficiary receives its expected share"}],
    "baseline": lambda item: run(item, False),
    "candidate": lambda item: run(item, os.environ.get("SHOW_BUG") != "1"), "evaluate": evaluate,
}
