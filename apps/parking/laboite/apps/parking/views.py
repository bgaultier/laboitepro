# coding: utf-8
from __future__ import unicode_literals
from .models import AppParking
from boites.views import AppCreateView, AppUpdateView, AppDeleteView


class AppParkingCreateView(AppCreateView):
    model = AppParking
    fields = ['parking']


class AppParkingUpdateView(AppUpdateView):
    model = AppParking
    fields = ['parking', 'enabled']


class AppParkingDeleteView(AppDeleteView):
    model = AppParking
