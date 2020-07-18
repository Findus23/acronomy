from django.contrib import admin
# Register your models here.
from simple_history.admin import SimpleHistoryAdmin

from acros.models import Acronym, Weblink, PaperReference, WikipediaLink, Tag, Host, WikipediaImage


class OwnInline(admin.TabularInline):
    extra = 1


class LinkInline(OwnInline):
    model = Weblink


class PaperInline(OwnInline):
    model = PaperReference
    fields = ["bibcode"]
    readonly_fields = ["title"]


class WikiInline(OwnInline):
    model = WikipediaLink
    fields = ["title"]


class TagAdmin(SimpleHistoryAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["slug"]


class AcronymAdmin(SimpleHistoryAdmin):
    inlines = [
        LinkInline, WikiInline, PaperInline
    ]
    filter_horizontal = ["tags"]
    readonly_fields = ["slug"]
    list_display = ["name", "full_name"]
    list_filter = ["tags", "modified_date", "created_date"]
    save_on_top = True


class PaperAdmin(SimpleHistoryAdmin):
    date_hierarchy = "pubdate"
    list_display = ["title", "authors"]


class LinkAdmin(SimpleHistoryAdmin):
    readonly_fields = ["host"]


class WikipediaAdmin(SimpleHistoryAdmin):
    # readonly_fields = ["thumbnail_height", "thumbnail_width"]
    ...

admin.site.register(WikipediaLink, WikipediaAdmin)
admin.site.register(Weblink, LinkAdmin)
admin.site.register(PaperReference, PaperAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Acronym, AcronymAdmin)
admin.site.register(Host)
admin.site.register(WikipediaImage)

admin.site.site_header="Acronomy Administration"
admin.site.site_title="Acronomy Administration"
