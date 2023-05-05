from django.shortcuts import render, HttpResponse
import json


with open('countries.json') as f:
    lst = json.load(f)


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    context = {
        'lst': lst
    }
    return render(request, 'countries_list.html', context)


def country_page(request, country):
    context = {
        'lst': lst,
        'country': country
    }
    return render(request, 'country_page.html', context)


def languages(request):
    language_lst = []
    for item in lst:
        for i in item['languages']:
            if i not in language_lst:
                language_lst.append(i)
    context = {
        'language_lst': language_lst
    }
    return render(request, 'languages_list.html', context)

