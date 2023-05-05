
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/', views.countries_list),
    path('countries-list/<country>/', views.country_page),
    path('languages/', views.languages),
]
