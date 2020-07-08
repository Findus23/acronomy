from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets, filters

from acros.forms import EditForm, AddForm, WikipediaForm, PaperForm, WeblinkForm
from acros.models import Acronym, Tag, AcroOfTheDay, WikipediaLink, PaperReference, Weblink
from acros.serializers import AcronymSerializer, AcronymListSerializer, TagSerializer
from acros.utils.assets import get_css

handler404 = 'acros.views.PageNotFoundView'


class IndexView(generic.TemplateView):
    template_name = "acros/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        aotd = AcroOfTheDay.objects.filter(date=date.today()).select_related('acronym')
        data['acronyms_of_the_day'] = aotd
        data['num_acronyms'] = Acronym.objects.all().count()
        return data


class PageNotFoundView(generic.TemplateView):
    template_name = "404.html"


class OverView(generic.ListView):
    template_name = "acros/overview.html"
    model = Acronym
    context_object_name = 'acros'
    ordering = "name"


class DetailView(generic.DetailView):
    template_name = 'acros/detail.html'
    context_object_name = 'acro'
    model = Acronym


class EditView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = 'acros/edit.html'
    context_object_name = 'acro'
    model = Acronym
    # fields = ['name', 'full_name', "description_md", "tags"]
    form_class = EditForm
    success_message = 'Acronym "%(name)s" was edited successfully'


class AddView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "acros/add.html"
    form_class = AddForm
    model = Acronym
    success_message = 'Acronym "%(name)s" was created successfully'


class AddReferenceView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    def form_valid(self, form):
        acro = Acronym.objects.get(slug=self.kwargs.get('slug'))
        form.instance.acronym = acro
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail", kwargs={"slug": self.kwargs.get('slug')})


class AddWikipediaView(AddReferenceView):
    template_name = "acros/addwiki.html"
    form_class = WikipediaForm
    model = WikipediaLink
    success_message = 'Wikipedia Reference "%(title)s" was created successfully'


class AddPaperView(AddReferenceView):
    template_name = "acros/addpaper.html"
    form_class = PaperForm
    model = PaperReference
    success_message = 'Paper Reference "%(title)s" was created successfully'


class AddWeblinkView(AddReferenceView):
    template_name = "acros/addwebsite.html"
    form_class = WeblinkForm
    model = Weblink
    success_message = 'Weblink "%(url)s" was created successfully'


class TagListView(generic.ListView):
    template_name = "acros/taglist.html"
    model = Tag
    context_object_name = 'tags'
    ordering = "name"
    queryset = Tag.objects.exclude(acronyms=None)


class TagAcroView(generic.ListView):
    template_name = "acros/tagacro.html"
    context_object_name = 'acros'
    ordering = "name"
    allow_empty = False

    def get_queryset(self):
        return Acronym.objects.filter(tags__slug__exact=self.kwargs['slug'])


#### API Views ####

class AcronymViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing Acronyms
    """
    queryset = Acronym.objects.all().order_by('name')
    serializer_class = AcronymSerializer

    serializer_classes = {
        'list': AcronymListSerializer,
        'retrieve': AcronymSerializer,
    }
    default_serializer_class = AcronymListSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer


##### DEBUG views #####


def debug_css(request):
    css, source_map = get_css(debug=True)
    return HttpResponse(css, content_type="text/css")


def debug_css_sourcemap(request):
    css, source_map = get_css(debug=True)
    return HttpResponse(source_map, content_type="application/json")
