from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
            obj = Analysis.objects.filter(analysis_name=analysis_name)
            if not obj:
                form.save()
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

            absorbance_concentration = list(zip(absorbance, concentration))

            calibration_curve = CalibrationCurve(absorbance, concentration)
            calibration_curve.plot()

            context = {
                "absorbance_concentration": absorbance_concentration,
                "analysis_name": analysis_name,
                "substance_name": substance_name,
            }
            return render(request, "calibration/report.html", context=context)
    return render(request, "index.html", context=context)


class AnalysisListView(generic.ListView):
    model = Analysis
    paginate_by = 10


class AnalysisUpdate(UpdateView):
    model = Analysis
    fields = "__all__"


class AnalysisDetailView(generic.DetailView):
    model = Analysis


class AnalysisDelete(DeleteView):
    model = Analysis
    success_url = reverse_lazy("analyses")
