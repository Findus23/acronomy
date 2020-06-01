from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers

from acronomy import settings
from . import views

router = routers.DefaultRouter()
router.register(r'acronym', views.AcronymViewSet)
router.register(r'tag', views.TagViewSet)

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('acro', RedirectView.as_view(pattern_name="overview")),
    path('acro/add', views.AddView.as_view(), name="add"),
    path('acro/<str:slug>', views.DetailView.as_view(), name='detail'),
    path('acro/<str:slug>/edit', views.EditView.as_view(), name='edit'),
    path('acros', views.OverView.as_view(), name='overview'),
    path('tags', views.TagListView.as_view(), name='tags'),
    path('tag', RedirectView.as_view(pattern_name="tags")),
    path('tag/<str:slug>', views.TagAcroView.as_view(), name='tag'),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
