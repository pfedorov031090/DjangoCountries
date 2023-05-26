
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries-list/', views.countries_list, name='countries'),
    path('countries-list/<int:country_id>/', views.country_page, name='country_page'),
    path('languages/', views.languages_list, name='languages'),
    path('languages/<int:language_id>/', views.language_page, name='language_page'),
]
