import json
from collections.abc import Generator
from functools import lru_cache
from pathlib import Path
from typing import TypedDict

from django import template
from django.templatetags.static import static

from acronomy.secrets import STATICFILES_DIRS

register = template.Library()


class Asset(TypedDict):
    file: str
    srf: str
    isEntry: bool
    imports: list[str] | None
    isDynamicEntry: bool | None


Manifest = dict[str, Asset]


@lru_cache
def load_vite_manifest() -> Manifest:
    with (Path(STATICFILES_DIRS[0]) / "build" / ".vite" / "manifest.json").open() as f:
        return json.load(f)


@register.simple_tag
@lru_cache
def js_asset(entry_point: str) -> Asset:
    manifest = load_vite_manifest()
    try:
        return manifest[entry_point]
    except KeyError:
        return manifest[f"static/{entry_point}"]


@register.simple_tag
@lru_cache
def js_asset_url(entry_point: str) -> str:
    asset = js_asset(entry_point)

    return static("build/" + asset["file"])


@register.simple_tag
def get_dependencies(entry_point: str) -> Generator[Asset, None, None]:
    asset = js_asset(entry_point)
    print(asset)
    if "imports" in asset:
        for imp in asset["imports"]:
            yield from get_dependencies(imp)
    yield static("build/" + asset["file"])
