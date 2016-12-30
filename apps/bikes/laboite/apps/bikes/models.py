# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from boites.exceptions import ExternalWebserviceError
from boites.models import App
from . import providers


class AppBikes(App):
    UPDATE_INTERVAL = 10 * 60

    provider = models.CharField(_('Fournisseur de données'), help_text=_('Choisissez le service de vélos désiré'), choices=providers.get_providers(), max_length=64)
    id_station = models.CharField(_('Station'), help_text=_('Choisissez la station dont vous voulez obtenir les informations'), max_length=64)
    station = models.TextField(_('Nom station'))
    slots = models.PositiveIntegerField(_('Nombre de places totales'), null=True)
    bikes = models.PositiveIntegerField(_('Nombre de vélos disponibles'), null=True)
    status = models.NullBooleanField(_('En fonctionnement ?'), null=True)

    def update_data(self):
        provider_class = providers.get_provider(self.provider)
        data = provider_class.get_station_infos(self.id_station)
        if data is None:
            raise ExternalWebserviceError("Could not find station")

        for field in ('station', 'slots', 'bikes', 'status'):
            setattr(self, field, data[field])

        self.save()

    def _get_data(self):
        return {
            'provider': self.provider,
            'station': self.station,
            'slots': self.slots,
            'bikes': self.bikes,
            'status': self.status
        }

    class Meta:
        verbose_name = _('Configuration : vélos')
        verbose_name_plural = _('Configurations : vélos')
