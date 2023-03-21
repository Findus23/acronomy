from django.contrib import admin
# Register your models here.
from simple_history.admin import SimpleHistoryAdmin

from acros.models import Acronym, Weblink, PaperReference, WikipediaLink, Tag, Host, WikipediaImage


class OwnInline(admin.TabularInline):
    extra = 1


class LinkInline(OwnInline):
    model = Weblink
    show_change_link = True


class PaperInline(OwnInline):
    model = PaperReference
    fields = ["bibcode"]
    readonly_fields = ["title"]
    show_change_link = True


class WikiInline(OwnInline):
    model = WikipediaLink
    fields = ["title"]
    show_change_link = True


class TagAdmin(SimpleHistoryAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["slug"]


class AcronymAdmin(SimpleHistoryAdmin):
    inlines = [
        LinkInline, WikiInline, PaperInline
    ]
    filter_horizontal = ["tags"]
    readonly_fields = ["slug"]
    list_display = ["name", "full_name", "pageviews"]
    list_filter = ["tags", "modified_date", "created_date"]
    search_fields = ["name", "full_name", "description_md"]
    save_on_top = True


class PaperAdmin(SimpleHistoryAdmin):
    date_hierarchy = "pubdate"
    list_display = ["title", "authors"]


class LinkAdmin(SimpleHistoryAdmin):
    list_display = ["title", "acronym", "url"]
    list_filter = ["host"]
    readonly_fields = ["host"]


class WikipediaAdmin(SimpleHistoryAdmin):
    list_display = ["title", "acronym", "thumbnail"]
    list_filter = ["description_source"]
    date_hierarchy = "timestamp"
    ...


class WikipediaImageAdmin(admin.ModelAdmin):
    readonly_fields = ["thumbnail", "thumb_width", "thumb_height", "imageurl", "credit", "artist", "license_short_name",
                       "attribution", "license_url", "attribution_required", "copyrighted", "timestamp"]
    list_filter = ["thumb_width", "license_short_name", "attribution_required", "copyrighted"]
    date_hierarchy = "timestamp"
    search_fields = ["artist", "credit", "attribution"]


admin.site.register(WikipediaLink, WikipediaAdmin)
admin.site.register(Weblink, LinkAdmin)
admin.site.register(PaperReference, PaperAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Acronym, AcronymAdmin)
admin.site.register(Host)
admin.site.register(WikipediaImage, WikipediaImageAdmin)

admin.site.site_header = "Acronomy Administration"
admin.site.site_title = "Acronomy Administration"
