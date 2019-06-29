from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TextData, PostModelForm
from django.forms import formset_factory,modelformset_factory
from .models import Post

from django.core.urlresolvers import reverse
# Create your views here.
def forms(request):
    return HttpResponse("<h2>Forms Views</h1>")

#FORMSETS
def modelFormSetQuerySet(request):
    if request.user.is_authenticated():
        modelForm = modelformset_factory(Post,form = PostModelForm)
        formset = modelForm(request.POST or None, queryset = Post.objects.filter(user=request.user))
        if formset.is_valid():
            for form in formset:
                obj = form.save(commit = False)
                if form.cleaned_data:
                    if not form.cleaned_data.get("publish"):
                        obj.publish = "2019-02-12"
                    obj.save()
        context = {
            "formset": formset
        }
        return render(request, "modelformsetView.html", context)
    else:
        print("HOME")
        return redirect("home")
        #return reverse("home")

def modelFormSet(request):
    modelForm = modelformset_factory(Post,fields=['user','title','slug','image'])
    formset = modelForm(request.POST or None)
    if formset.is_valid():
        for form in formset:
            obj = form.save(commit = False)
            obj.title = "amit sach"
            obj.publish = "2019-02-12"
            obj.save()
    context = {
        "formset": formset
    }
    return render(request, "modelformsetView.html", context)



def testFormSet(request):
    TestForm = formset_factory(TextData,extra=2)
    formset = TestForm(request.POST or None)
    if formset.is_valid():
        print(formset)
        for form in formset:
            print(form.cleaned_data)
    context = {
        "formset": formset
    }
    return render(request,"formsetView.html",context)
#FORMSETS

def modelForm(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
    if request.method == "POST":
        print(request.POST)
    if form.has_error:
        #print(form.errors.as_json())
        #print(form.errors.as_text())
        #print(dir(form.errors))
        data = form.errors.items()
        for key,value in data:
            #print(dir(value))
            #print(dir(form.errors))
            error_str = "{field}:{error}".format(field = key,
                                       error = value)
            print(error_str)
    return render(request, "modelforms.html", {"forms": form})


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

