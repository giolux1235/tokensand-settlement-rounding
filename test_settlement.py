"""Run the project's four Tokens& cases during standard unittest discovery."""
from vendor.tokensand_check import case_suite
from workflow import workflow


def load_tests(loader, tests, pattern):
    return case_suite(workflow)
