from typing import Set

from . import BaseCheck


class CheckRegistry:
    def __init__(self):
        self.checks: Set[BaseCheck] = set()

    def register(self, check: BaseCheck):
        self.checks.add(check)

    def run_checks(self):
        errors = []
        for Check in self.checks:
            inst = Check()
            new_errors = list(inst.run())
            errors.extend(new_errors)
        return errors


registry = CheckRegistry()
