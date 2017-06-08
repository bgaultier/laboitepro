# coding: utf-8


from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppCustomConfig(AppConfig):
    name = label = 'laboite.apps.custom'
    verbose_name = _('App : App personnalisée')
