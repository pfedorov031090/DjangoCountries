from django.shortcuts import render
from MainApp.models import Country, Language


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries_list_from_bd = Country.objects.all()
    context = {
        'countries_list': countries_list_from_bd
    }
    return render(request, 'countries_list.html', context)


def country_page(request, country):
    country_from_bd = Country.objects.get(name=country)
    language_list_from_bd = country_from_bd.languages.all()
    context = {
        'language_list': language_list_from_bd,
        'country': country_from_bd.name
    }
    return render(request, 'country_page.html', context)


def languages(request):
    language_list_from_bd = Language.objects.all()
    context = {
        'language_list': language_list_from_bd
    }
    return render(request, 'languages_list.html', context)

