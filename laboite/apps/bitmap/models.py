# coding: utf-8

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

from boites.models import App


class AppBitmap(App):
    width = models.PositiveIntegerField(verbose_name=_("Largeur de l'icône"), default=16)
    height = models.PositiveIntegerField(verbose_name=_("Hauteur de l'icône"), default=16)

    def get_bitmaps(self):
        bitmaps = Bitmap.objects.filter(app_id=self.id)
        bitmap_list = []
        for bitmap in bitmaps:
            bitmap_list.append(str(bitmap.bitmap))
        return bitmap_list

    def _get_data(self):
        bitmaps = Bitmap.objects.filter(app_id=self.id)
        if len(bitmaps) == 1:
            bitmap = bitmaps.first()
            bitmap_list = hex(int(bitmap.bitmap, 2))
            type = 'icon'
        else:
            bitmap_list = []
            for bitmap in bitmaps:
                bitmap_list.append(hex(int(bitmap.bitmap, 2)))
            type = 'animation'
        return {
            'width': self.width,
            'height': self.height,
            'data': [
                {
                    'type': type,
                    'width': self.width,
                    'height': self.height,
                    'x': 0,
                    'y': 0,
                    'content':  bitmap_list,
                },
            ]
        }

    def delete(self, *args, **kwargs):
        bitmaps = Bitmap.objects.filter(app_id=self.id)
        bitmaps.delete()
        super(AppBitmap, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Configuration : icône personnalisée')
        verbose_name_plural = _('Configurations : icône personnalisée')


class Bitmap(models.Model):
    app_id = models.PositiveIntegerField(verbose_name=_("Identifiant de l'app"), default=0)
    bitmap = models.TextField('Bitmap', max_length=1024, default='', blank=True)

    class Meta:
        verbose_name = 'Bitmap'
