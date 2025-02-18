from django.apps import AppConfig

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _


class SimpleTimeseriesConfig(AppConfig):
    name = "django_simple_timeseries"
    verbose_name = _("Django Simple Timeseries")

    def ready(self):
        pass
