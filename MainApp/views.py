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
    for item in lst:
        if item['country'] == country:
            text = f"""
                <h1>{item['country']}</h1>
            """
            text += '<ul>'
            for i in item['languages']:
                text += f'<li>{i}</li>'
            text += '</ul>'
            return HttpResponse(text)


def languages(request):
    language_lst = []
    out = '<ol>'
    for item in lst:
        for i in item['languages']:
            if i not in language_lst:
                language_lst.append(i)
                out += f'<li>{i}</li>'
    out += '</ol>'
    return HttpResponse(out)
