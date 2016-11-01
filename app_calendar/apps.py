from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppCalendarConfig(AppConfig):
    name = 'app_calendar'
    verbose_name = _('App : calendrier')
