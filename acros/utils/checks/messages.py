from django.urls import reverse

from acros.models import Acronym

DEBUG = 10
INFO = "info"
WARNING = "warning"
ERROR = 40
CRITICAL = 50


class CheckMessage:
    def __init__(self, level: str, msg: str, obj=None):
        self.level = level
        self.msg = msg
        self.obj = obj

    def __str__(self):
        obj = str(self.obj)
        print(self.obj._meta.label)
        return f"{obj}: {self.msg}"

    @property
    def edit_url(self):
        if isinstance(self.obj, Acronym):
            return reverse("edit", args=[self.obj.slug])
        return None

    @property
    def admin_edit_url(self):
        if isinstance(self.obj, Acronym):
            return reverse("admin:acros_acronym_change", args=[self.obj.id])
        return None


class CheckWarning(CheckMessage):
    def __init__(self, msg: str, obj=None):
        super(CheckWarning, self).__init__(WARNING, msg, obj)


class CheckInfo(CheckMessage):
    def __init__(self, msg: str, obj=None):
        super(CheckInfo, self).__init__(INFO, msg, obj)
