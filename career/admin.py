from django.contrib import admin

from .models import Career


class CareerAdmin(admin.ModelAdmin):
    list_display = ['title', 'reference']
    ordering = ['title']


admin.site.register(Career, CareerAdmin)
