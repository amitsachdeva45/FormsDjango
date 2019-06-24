from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextData, PostModelForm
# Create your views here.
def forms(request):
    return HttpResponse("<h2>Forms Views</h1>")

def modelForm(request):
    forms = PostModelForm
    if request.method == "POST":
        print(request.POST)
    return render(request, "modelforms.html", {"forms": forms})


def normalForm(request):
    initial_data = {
        "some_text": "Amit",
        "boolean": True,
    }

    forms = TextData(request.POST or None, initial=initial_data)
    #It means it is requiring post request data or nothing///It can also be used for validation

    if forms.is_valid():
        print(forms.cleaned_data)
        print(forms.cleaned_data.get("some_text"))

        if request.method == "POST":
            print(request.POST)
            #print(request.POST["username"])#Raise error no prefarable to use
            print(request.POST.get("some_text"))#Return none if no value found
        elif request.method == "GET":
            print(request.GET)
    return render(request, "forms.html",{"forms":forms})

