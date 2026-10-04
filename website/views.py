from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm, NewsLetterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request,"website/about.html")

def contact_view(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your Form submited successfully !")
        else:
            messages.add_message(request, messages.ERROR, "Wronggggg !")
    
    form= ContactForm()
    return render(request,"website/contact.html", {'form':form})


def test_view(request):
    if request.method == "POST":
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()

    form= ContactForm()
    return render(request, "website/test.html", {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form= NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
