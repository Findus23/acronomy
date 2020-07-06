import markdown
import markdown_katex


def md_to_html(md: str) -> str:
    html = markdown.markdown(
        md,
        output_format="html5",
        extensions=[
            "nl2br",
            markdown_katex.KatexExtension(insert_fonts_css=False,no_inline_svg=True),
            "acros.utils.wikilinks"
        ]
    )
    return html
