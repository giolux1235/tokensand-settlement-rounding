# Settlement rounding

Split synthetic USD, JPY, and KWD payouts between beneficiaries. Rounding each share independently can turn a one-cent settlement into two cents. The corrected code assigns whole minor units by largest remainder, breaking ties by beneficiary ID. It also handles refunds.

From a Python 3.10+ environment, install the public Tokens& checker once.

```sh
python3 -m pip install https://raw.githubusercontent.com/giolux1235/tokensand-agent-pack/0a6d1c9254d9b41a7888e1df29a358fc656952b5/packages/tokensand_workflow_check-0.1.5-py3-none-any.whl
```

Reproduce the defect, then run the repaired implementation.

```sh
SHOW_BUG=1 python3 -m tokensand_check --offline-workflow ./workflow.py
python3 -m tokensand_check --offline-workflow ./workflow.py
```

The broken version fails `usd-split-cent`, `kwd-three-decimals`, and `refund-conserves-units`. The repair passes all four cases. Both runs use identical cases and run locally with synthetic records. [Tokens& setup](https://tokensand.com/agents/install)

This is a first-party Tokens& workshop example using invented transactions. It runs without provider keys. Local checks stay on your machine.
