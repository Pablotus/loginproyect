from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def login_account(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user is not None:
                login(request, user)

                return redirect("AppCoderCursos")
            else:
                return redirect("AppCoderEstudiantes")
    form = AuthenticationForm()
    context = {
    "form": form,
}
    return render(request, "account/login.html", context=context )

