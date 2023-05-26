from django.shortcuts import render
from MainApp.models import Country, Language


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries = Country.objects.all()
    context = {
        'countries': countries
    }
    return render(request, 'countries_list.html', context)


def country_page(request, country_id):
    country = Country.objects.get(id=country_id)
    language_list = country.languages.all()
    context = {
        'languages': language_list,
        'country': country.name
    }
    return render(request, 'country_page.html', context)


def language_page(request, language_id):
    countries_by_language = Country.objects.filter(languages__id=language_id)
    language = Language.objects.get(id=language_id)
    context = {
        'countries': countries_by_language,
        'language': language
    }
    return render(request, 'language_page.html', context)


def languages_list(request):
    language_list = Language.objects.all()
    context = {
        'languages': language_list
    }
    return render(request, 'languages_list.html', context)


