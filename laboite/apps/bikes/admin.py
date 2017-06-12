from django.contrib import admin

from .models import AppBikes
from .forms import BikeModelForm


class AppBikesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'last_activity', 'slots', 'bikes', 'status')

    list_display = ('boite', 'enabled', 'station', 'bikes',  'slots', 'status', 'get_app_dictionary', 'created_date', 'last_activity')

    form = BikeModelForm


admin.site.register(AppBikes, AppBikesAdmin)
