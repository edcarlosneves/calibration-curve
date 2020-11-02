from django.db import models
from django.urls import reverse


class Analysis(models.Model):
    analysis_name = models.CharField("Analysis Name", max_length=200, help_text='Enter a name for you analysis')
    substance_name = models.CharField("Substance Name", max_length=200,
                                      help_text='Enter the name of the substance that you will analysis')
    absorbance = models.CharField("Absorbance", max_length=200, help_text='Absorbance measured separated by commas.')
    concentration = models.CharField("Concentration", max_length=200,
                                     help_text='Concentration measured separated by commas.')

    class Meta:
        verbose_name_plural = 'Analyses'

    def get_absolute_url(self):
        return reverse("analysis-detail", args=[str(self.id)])

    def __str__(self):
        return f'{self.analysis_name} -> {self.substance_name} -> {self.id}'
