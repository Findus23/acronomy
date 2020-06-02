from pathlib import Path

import sass
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'compile scss'

    def handle(self, *args, **kwargs):
        basedir = Path(__file__).resolve().parent.parent.parent.parent

        inputdir = basedir / "static/scss/"
        inputfile = inputdir / "main.scss"
        outputfile = basedir / "static/css/main.css"
        sourcemap = outputfile.with_suffix(".css.map")
        with inputfile.open() as f:
            sass_text = f.read()

        css,sourcemap_text = sass.compile(
            filename=str(inputfile),
            output_style="compressed",
            include_paths=[str(inputdir), str(basedir)],
            source_map_filename=str(sourcemap)
        )

        with outputfile.open("w") as f:
            f.write(css)
        with sourcemap.open("w") as f:
            f.write(sourcemap_text)
