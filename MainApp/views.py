from django.shortcuts import render, HttpResponse
from MainApp.models import Country, Languages


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    lst = Country.objects.all()
    context = {
        'lst': lst
    }
    return render(request, 'countries_list.html', context)


def country_page(request, country):
    country1 = Country.objects.get(name=country)
    lst = country1.languages.all()
    context = {
        'lst': lst,
        'country': country1.name
    }
    return render(request, 'country_page.html', context)


def languages(request):
    lst = Languages.objects.all()
    context = {
        'language_lst': lst
    }
    return render(request, 'languages_list.html', context)

