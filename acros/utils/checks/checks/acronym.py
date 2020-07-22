from acros.models import Acronym
from acros.utils.checks import BaseCheck, CheckWarning, registry, CheckInfo


class LetterCheck(BaseCheck):
    def run(self):
        for acronym in Acronym.objects.all():
            if acronym.acro_letters is None:
                yield CheckInfo(
                    "missing acronym letters",
                    obj=acronym
                )
                continue
            let_len = len(acronym.acro_letters)
            acr_len = len(acronym.name)
            if let_len != acr_len:
                yield CheckWarning(
                    f"number of letters selected ({let_len}) not equal to letters in acronym ({acr_len})",
                    obj=acronym
                )


registry.register(LetterCheck)
