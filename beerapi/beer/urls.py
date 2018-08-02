from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('new_user/', views.new_user, name="new_user"),
    path('new_beer/', views.new_beer, name="new_beer"),
    path('rate_beer/', views.rate_beer, name="rate_beer"),
    path('beers/', views.BeerModelList.as_view(), name="beers"),
    path('rates/', views.RateModelList.as_view(), name="rates"),
]
