import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoCountries.settings")
from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
from MainApp.models import Country, Languages


items = Country.objects.filter(name='Aruba')
print(items.laguage)


# with open('/home/student/Projects/DjangoCountries/countries.json') as f:
#     lst = json.load(f)
#
#
# for i in lst:
#     if not Country.objects.filter(name=i['country']).exists():
#         country = Country(name=i['country'])
#         country.save()
#     for lang in i['languages']:
#         if not Languages.objects.filter(language=lang).exists():
#             languages = Languages(language=lang)
#             languages.save()
#
#
# all_countries = Country.objects.all()
# for country in all_countries:
#     for i in lst:
#         if country.name == i['country']:
#             country = Country.objects.get(name=country.name)
#             for z in i['languages']:
#                 country.languages.add(Languages.objects.get(language=z).id)
