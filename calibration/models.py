from django.db import models
from django.urls import reverse
from django.conf import settings


class Analysis(models.Model):
    CONCENTRATION_UNIT_CHOICES = [
        ("mg/l", "mg/l"),
        ("g/l", "g/l"),
        ("mg/ml", "mg/ml"),
        ("mol/l", "mol/l"),
    ]

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

    concentration_units = models.CharField(
        "Unidades das Concentrações",
        max_length=255,
        help_text="Valores das unidades das concentrações.",
        choices=CONCENTRATION_UNIT_CHOICES,
        default="mg/l",
    )

    analyst = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Analista",
    )

    class Meta:
        verbose_name_plural = "Analyses"

    def get_absolute_url(self):
        return reverse("analysis-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.analysis_name} -> {self.substance_name} -> {self.id}"
