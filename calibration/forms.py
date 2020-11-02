from django import forms
from calibration.models import Analysis


class AnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        exclude = []