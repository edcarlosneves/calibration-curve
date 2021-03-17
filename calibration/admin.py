from django.contrib import admin
from .models import Analysis


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    search_fields = ("analysis_name",)
    raw_id_fields = ("analyst",)
    ordering = ("analysis_name",)
