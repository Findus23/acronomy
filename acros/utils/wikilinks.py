"""
Original code Copyright [Waylan Limberg](http://achinghead.com/).

All changes Copyright The Python Markdown Project

License: [BSD](https://opensource.org/licenses/bsd-license.php)

------------

Custom modification by Lukas Winkler

"""

import xml.etree.ElementTree as etree

from markdown import Extension
from markdown.inlinepatterns import InlineProcessor

from acros.models import Acronym

invalid_wikilink = "invalid wikilink"


class WikiLinkExtension(Extension):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        self.md = md

        # append to end of inline patterns
        WIKILINK_RE = r"\[\[([\w0-9_ -]+)\]\]"
        wikilinkPattern = WikiLinksInlineProcessor(WIKILINK_RE, self.getConfigs())
        wikilinkPattern.md = md
        md.inlinePatterns.register(wikilinkPattern, "acrowikilink", 75)


class WikiLinksInlineProcessor(InlineProcessor):
    base_url = "/"
    end_url = "/"
    html_class = "wikilink"

    def __init__(self, pattern, config):
        super().__init__(pattern)

    def handleMatch(self, m, data):
        label = m.group(1).strip()
        try:
            acro = Acronym.objects.get(name=label)
        except Acronym.DoesNotExist:
            # TODO: Notify user of invalid acronym
            span = etree.Element("span")
            span.text = invalid_wikilink
            span.set("style", "display:none")
            return span, m.start(0), m.end(0)
        url = f"/acronym/{acro.slug}"
        a = etree.Element("a")
        a.text = label
        a.set("href", url)
        a.set("title", acro.full_name)
        a.set("data-toggle", "tooltip")
        if self.html_class:
            a.set("class", self.html_class)
        return a, m.start(0), m.end(0)


def makeExtension(**kwargs):  # pragma: no cover
    return WikiLinkExtension(**kwargs)
