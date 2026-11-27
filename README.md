# Settlement rounding

Split synthetic USD, JPY, and KWD payouts between beneficiaries. Rounding each share independently can turn a one-cent settlement into two cents. The corrected code assigns whole minor units by largest remainder, breaking ties by beneficiary ID. It also handles refunds.

With Python 3.10 or later, clone the example and enter its directory. The Tokens& checker is included.

```sh
git clone https://github.com/giolux1235/tokensand-settlement-rounding
cd tokensand-settlement-rounding
```

Reproduce the rounding defect. Expect `usd-split-cent`, `kwd-three-decimals`, and `refund-conserves-units` to fail.

```sh
SHOW_BUG=1 python3 -m unittest -v
```

Verify the repair. All four cases should pass.

```sh
python3 -m unittest -v
```

Both commands run the same cases offline. Pull requests and pushes to `main` run the same four checks.

This is a first-party Tokens& workshop example using invented transactions. It runs without provider keys.

[View Settlement Rounding Check on Tokens&](https://tokensand.com/p/settlement-rounding-check) to share this example or set up checks for your own project.
