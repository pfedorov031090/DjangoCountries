from django.shortcuts import render
from MainApp.models import Country, Language


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries_list_from_bd = Country.objects.all()
    context = {
        'countries': countries_list_from_bd
    }
    return render(request, 'countries_list.html', context)


def country_page(request, country):
    country_from_bd = Country.objects.get(name=country)
    language_list_from_bd = country_from_bd.languages.all()
    context = {
        'languages': language_list_from_bd,
        'country': country_from_bd.name
    }
    return render(request, 'country_page.html', context)


def language_page(request, language):
    countries_by_language = Country.objects.filter(languages__language_name=language)
    context = {
        'countries': countries_by_language,
        'language': language
    }
    return render(request, 'language_page.html', context)


def languages_list(request):
    language_list_from_bd = Language.objects.all()
    context = {
        'languages': language_list_from_bd
    }
    return render(request, 'languages_list.html', context)


