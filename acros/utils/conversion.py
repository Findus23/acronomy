import markdown


def md_to_html(md: str) -> str:
    html = markdown.markdown(
        md,
        output_format="html5",
        extensions=[
            "nl2br",
        ]
    )
    return html
