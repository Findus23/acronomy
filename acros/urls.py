from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView
from rest_framework import routers

from acronomy import settings
from . import views
from .sitemaps import AcronymSitemap

router = routers.DefaultRouter()
router.register(r'acronym', views.AcronymViewSet)
router.register(r'tag', views.TagViewSet)

sitemaps = {
    "acronyms": AcronymSitemap
}

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path("sitemap.xml", cache_page(60 * 15)(sitemap), {"sitemaps": sitemaps}, name="sitemap"),
    path('api/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('acronym', RedirectView.as_view(pattern_name="overview")),
    path('acronym/add', views.AddView.as_view(), name="add"),
    path('acronym/<str:slug>', views.DetailView.as_view(), name='detail'),
    path('acronym/<str:slug>/edit', views.EditView.as_view(), name='edit'),
    path('acronym/<str:slug>/edit-letters', views.EditLetterView.as_view(), name='edit_letter'),
    path('acronym/<str:slug>/add/wikipedia', views.AddWikipediaView.as_view(), name='add_wikipedia'),
    path('acronym/<str:slug>/add/paper', views.AddPaperView.as_view(), name='add_paper'),
    path('acronym/<str:slug>/add/weblink', views.AddWeblinkView.as_view(), name='add_weblink'),
    path('acronyms', views.OverView.as_view(), name='overview'),
    path('tags', views.TagListView.as_view(), name='tags'),
    path('tag', RedirectView.as_view(pattern_name="tags")),
    path('tag/<str:slug>', views.TagAcroView.as_view(), name='tag'),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("css", views.debug_css, name="css"))
    urlpatterns.append(path("css_sourcemap", views.debug_css_sourcemap, name="css_sourcemap"))

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
