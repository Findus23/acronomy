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
            num_letters = []
            for num in acronym.acro_letters:
                num_letters.append(acronym.full_name[num])
            for letter, acro_letter in zip(num_letters, acronym.name):
                letter = letter.lower()
                acro_letter = acro_letter.lower()
                if letter != acro_letter:
                    yield CheckWarning(
                        f"letters don't match ({letter}≠{acro_letter})",
                        obj=acronym
                    )


registry.register(LetterCheck)
