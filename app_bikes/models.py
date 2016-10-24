# coding: utf-8

from __future__ import unicode_literals

from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _L

from boites.models import Boite, App
from . import providers, settings


class AppBikes(App):
    provider = models.CharField(_L('Fournisseur de données'), help_text=_L('Choisissez le service de vélos désiré'), choices=providers.get_providers(), max_length=64)
    id_station = models.CharField(_L('Station'), help_text=_L('Choisissez la station dont vous voulez obtenir les informations'), max_length=64)
    station = models.TextField(_L('Nom station'))
    slots = models.PositiveIntegerField(_L('Nombre de places totales'), null=True)
    bikes = models.PositiveIntegerField(_L('Nombre de vélos disponibles'), null=True)
    status = models.NullBooleanField(_L('En fonctionnement ?'), null=True)

    def get_app_dictionary(self):
        if not self.enabled:
            return None

        if timezone.now() >= self.last_activity + timedelta(minutes=settings.VALUES_UPDATE_INTERVAL):
            provider_class = providers.get_provider(self.provider)
            data = provider_class.get_station_infos(self.id_station)
            if data is None:
                return None

            for field in ('station', 'slots', 'bikes', 'status'):
                setattr(self, field, data[field])
            self.save()
        return {
            'provider': self.provider,
            'station': self.station,
            'slots': self.slots,
            'bikes': self.bikes,
            'status': self.status
        }

    class Meta:
        verbose_name = _L('Configuration : vélos')
        verbose_name_plural = _L('Configurations : vélos')
