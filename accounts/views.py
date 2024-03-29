from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from accounts.forms import CustomUserCreationForm


def register(request):
    if request.method == "GET":
        return render(
            request, "accounts/register.html", {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("analyses"))
        else:
            return render(request, "accounts/register.html", {"form": form})
