from django.contrib import admin

from .models import Class


class ClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'reference']
    ordering = ['title']


admin.site.register(Class, ClassAdmin)
