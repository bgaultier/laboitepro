# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppMetroConfig(AppConfig):
    name = label = 'laboite.apps.metro'
    verbose_name = _('App : Métro')
