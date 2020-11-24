from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from accounts.models import User
from calibration.models import Analysis
from calibration.forms import AnalysisForm
from utils.calibration_curve import CalibrationCurve


@login_required
def index(request):
    form = AnalysisForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.method == "POST":
        form = AnalysisForm(request.POST or None)
        if form.is_valid():
            analysis_name = form.cleaned_data["analysis_name"]
            analyst = request.user
            obj = Analysis.objects.filter(analysis_name=analysis_name, analyst=analyst)
            if not obj:
                analysis = form.save(commit=False)
                analysis.analyst = analyst
                analysis.save()
            substance_name = form.cleaned_data["substance_name"]

            try:
                absorbance = [
                    float(data) for data in form.cleaned_data["absorbance"].split(",")
                ]
                concentration = [
                    float(data)
                    for data in form.cleaned_data["concentration"].split(",")
                ]
            except ValueError:
                messages.warning(
                    request,
                    "Existe(m) erro(s) nos inputs de absorbâncias e/ou concentrações.",
                )
                return render(request, "index.html", context=context)

            concentration_unit = form.cleaned_data["concentration_units"]

            absorbance_concentration = list(zip(absorbance, concentration))

            calibration_curve = CalibrationCurve(
                absorbance, concentration, concentration_unit
            )
            calibration_curve.plot()

            context = {
                "absorbance_concentration": absorbance_concentration,
                "analysis_name": analysis_name,
                "substance_name": substance_name,
                "concentration_unit": concentration_unit,
            }
            return render(request, "calibration/report.html", context=context)
    return render(request, "index.html", context=context)


class AnalysisListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 10

    def get_queryset(self):
        self.analyst = self.request.user
        return Analysis.objects.filter(analyst=self.analyst)


class AnalysisUpdate(LoginRequiredMixin, UpdateView):
    model = Analysis
    fields = "__all__"


class AnalysisDetailView(LoginRequiredMixin, generic.DetailView):
    model = Analysis


class AnalysisDelete(LoginRequiredMixin, DeleteView):
    model = Analysis
    success_url = reverse_lazy("analyses")
