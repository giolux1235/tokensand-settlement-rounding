# Settlement rounding

Split synthetic USD, JPY, and KWD payouts between beneficiaries. Rounding each share independently can turn a one-cent settlement into two cents. The corrected code assigns whole minor units by largest remainder, breaking ties by beneficiary ID. It also handles refunds.

With Python 3.10 or later, run the same four Tokens& cases that run on every pull request and push to main. A fresh checkout includes the checker and runs offline.

```sh
python3 -m unittest -v
```

To reproduce the rounding defect:

```sh
SHOW_BUG=1 python3 -m unittest -v
```

The broken version fails `usd-split-cent`, `kwd-three-decimals`, and `refund-conserves-units`. The repair passes all four cases. Both runs use identical cases and run locally with synthetic records. [Tokens& setup](https://tokensand.com/agents/install)

This is a first-party Tokens& workshop example using invented transactions. It runs without provider keys. Local checks stay on your machine.
