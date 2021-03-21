from django.contrib import admin
from .models import Analysis


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "analysis_name",
        "substance_name",
        "analyst",
        "created",
        "updated",
    ]
    search_fields = ("analysis_name",)
    raw_id_fields = ("analyst",)
    ordering = ("id",)
