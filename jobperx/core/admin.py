from django.contrib import admin
from core.models import ExlFile


@admin.register(ExlFile)
class ExlFileAdmin(admin.ModelAdmin):
    readonly_fields = ["date_load"]