from itertools import chain

from acros.models import Acronym
from acros.utils.checks import BaseCheck, CheckWarning, registry, CheckInfo
from acros.utils.wikilinks import invalid_wikilink

greek_codes = chain(range(0x370, 0x3e2), range(0x3f0, 0x400))
greek_symbols = (chr(c) for c in greek_codes)
greek_letters = set([c for c in greek_symbols if c.isalpha()])


class LetterCheck(BaseCheck):
    def run(self):
        for acronym in Acronym.objects.filter(ignore_in_checks=False):
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
                if letter != acro_letter and acro_letter not in greek_letters:
                    yield CheckWarning(
                        f"letters don't match ({letter}≠{acro_letter})",
                        obj=acronym
                    )


registry.register(LetterCheck)


class FullNameCheck(BaseCheck):
    def run(self):
        for acronym in Acronym.objects.all():
            first_letter = acronym.full_name[0]
            if first_letter.islower():
                yield CheckInfo(
                    f"first letter of full name should be uppercase ({acronym.full_name})",
                    obj=acronym
                )


registry.register(FullNameCheck)


class WikiLinkCheck(BaseCheck):
    def run(self):
        for acronym in Acronym.objects.all():
            if invalid_wikilink in acronym.description_html:
                yield CheckWarning(
                    "invalid wikilink",
                    obj=acronym
                )


registry.register(WikiLinkCheck)
