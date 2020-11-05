from django.db import models
from django.urls import reverse


class Analysis(models.Model):
    analysis_name = models.CharField(
        "Nome da Análise",
        max_length=255,
        help_text="Digite um nome para identificar sua análise.",
    )
    substance_name = models.CharField(
        "Nome da Substância",
        max_length=255,
        help_text="Digite o nome da substância que você está analisando.",
    )
    absorbance = models.CharField(
        "Absorbâncias",
        max_length=255,
        help_text="Valores das absorbâncias lidas separados por vírgula.",
    )
    concentration = models.CharField(
        "Concentrações",
        max_length=255,
        help_text="Valores das concentrações para cada absorbância fornecida separados por vírgulas.",
    )

    class Meta:
        verbose_name_plural = "Analyses"

    def get_absolute_url(self):
        return reverse("analysis-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.analysis_name} -> {self.substance_name} -> {self.id}"
