from django.contrib import admin
# Register your models here.
from simple_history.admin import SimpleHistoryAdmin

from acros.models import Acronym, Weblink, PaperReference, WikipediaLink, Tag, Host


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


class TagAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["slug"]


class AcronymAdmin(SimpleHistoryAdmin):
    inlines = [
        LinkInline, WikiInline, PaperInline
    ]
    filter_horizontal = ["tags"]
    readonly_fields = ["slug"]
    list_display = ["name", "full_name"]
    list_filter = ["tags"]
    save_on_top = True


class PaperAdmin(admin.ModelAdmin):
    date_hierarchy = "pubdate"
    list_display = ["title", "authors"]


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ["host"]


class WikipediaAdmin(admin.ModelAdmin):
    readonly_fields = ["thumbnail_height", "thumbnail_width"]


admin.site.register(WikipediaLink, WikipediaAdmin)
admin.site.register(Weblink, LinkAdmin)
admin.site.register(PaperReference, PaperAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Acronym, AcronymAdmin)
admin.site.register(Host)
