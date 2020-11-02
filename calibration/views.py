from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from calibration.models import Analysis
from calibration.forms import AnalysisForm


@login_required
def index(request):
    form = AnalysisForm(request.POST or None)
    if request.method == "POST":
        form = AnalysisForm(request.POST or None)

        if form.is_valid():
            form.save()
            obj = Analysis.objects.latest("id")
            print("print(obj)")
            print(obj)
            analysis_name = form.cleaned_data["analysis_name"]
            substance_name = form.cleaned_data["substance_name"]
            absorbance = [
                float(data) for data in form.cleaned_data["absorbance"].split(",")
            ]
            concentration = [
                float(data) for data in form.cleaned_data["concentration"].split(",")
            ]
            absorbance_concentration = list(zip(absorbance, concentration))
            context = {
                "absorbance_concentration": absorbance_concentration,
                "analysis_name": analysis_name,
                "substance_name": substance_name,
            }
            return render(request, "report.html", context=context)
    context = {
        "form": form,
    }

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
