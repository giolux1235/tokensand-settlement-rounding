"""Allocate synthetic settlement totals in integer currency minor units."""
from decimal import Decimal, ROUND_HALF_UP


def allocate(amount, currency, shares, *, conserve_units):
    digits = {"USD": 2, "JPY": 0, "KWD": 3}[currency]
    minor = Decimal(amount).scaleb(digits)
    if minor != minor.to_integral_value():
        raise ValueError("Amount is smaller than the currency minor unit")
    if not shares or any(weight <= 0 for weight in shares.values()):
        raise ValueError("Expected positive weights")
    total = int(minor)
    weights = sum(shares.values())
    if not conserve_units:
        return {key: int((Decimal(total * weight) / weights).quantize(1, rounding=ROUND_HALF_UP))
                for key, weight in shares.items()}
    whole, remainder = {}, {}
    for key, weight in shares.items():
        whole[key], remainder[key] = divmod(abs(total) * weight, weights)
    # Descending remainder, then beneficiary ID gives input-order-independent ties.
    for key in sorted(shares, key=lambda key: (-remainder[key], key))[:abs(total) - sum(whole.values())]:
        whole[key] += 1
    return {key: units if total >= 0 else -units for key, units in whole.items()}
