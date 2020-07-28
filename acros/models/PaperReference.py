import ads
from ads.search import Article
from django.db import models
from simple_history.models import HistoricalRecords

from acros.models import Acronym
from acronomy.settings import ADS_AUTH_TOKEN


class PaperReference(models.Model):
    acronym = models.ForeignKey(Acronym, on_delete=models.CASCADE, related_name="papers")
    bibcode = models.CharField(max_length=255)
    title = models.CharField(max_length=500, null=True, blank=True)
    authors = models.CharField(max_length=500, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    pubdate = models.DateTimeField(null=True, blank=True)
    arxiv_id = models.CharField(max_length=20, null=True, blank=True)
    doi = models.CharField(max_length=255, null=True, blank=True)
    fetched = models.BooleanField(default=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    def clean(self, *args, **kwargs):
        if not self.fetched:
            ads.config.token = ADS_AUTH_TOKEN
            cols = ["title", "author", "year", "pubdate", "doi", "identifier"]
            papers = ads.SearchQuery(bibcode=self.bibcode, fl=cols)
            paper: Article = next(papers)
            self.title = paper.title[0]
            if len(paper.author) > 3:
                self.authors = paper.author[0] + " et al."
            else:
                self.authors = ", ".join(paper.author)
            self.year = paper.year
            self.pubdate = paper.pubdate.replace("-00", "-01")
            if paper.doi and len(paper.doi) > 0:
                self.doi = paper.doi[0]
            else:
                self.doi = None
            arxiv_papers = [ident for ident in paper.identifier if "arXiv:" in ident]
            if len(arxiv_papers) > 0:
                self.arxiv_id = [ident for ident in paper.identifier if "arXiv:" in ident][0].split("arXiv:")[-1]
            else:
                self.arxiv_id = None
            self.fetched = True

    @property
    def ads_url(self):
        return f"https://ui.adsabs.harvard.edu/abs/{self.bibcode}/abstract"

    @property
    def arxiv_url(self):
        return "https://arxiv.org/abs/" + self.arxiv_id

    @property
    def doi_url(self):
        return "https://doi.org/" + self.doi

    @property
    def publisher_url(self):
        return f"https://ui.adsabs.harvard.edu/link_gateway/{self.bibcode}/PUB_PDF"

    @property
    def preprint_url(self):
        return "https://arxiv.org/pdf/" + self.arxiv_id
