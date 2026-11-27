"""Run the project's four Tokens& cases during standard unittest discovery."""
from vendor.tokensand_check import case_suite
from workflow import workflow


REQUIRED_CASES = {
    "usd-split-cent",
    "jpy-integer-control",
    "kwd-three-decimals",
    "refund-conserves-units",
}


def load_tests(loader, tests, pattern):
    declared = {case["id"] for case in workflow["cases"]}
    missing = REQUIRED_CASES - declared
    if missing:
        raise ValueError("Missing required settlement cases: " + ", ".join(sorted(missing)))
    return case_suite(workflow)
