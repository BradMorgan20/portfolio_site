from django.urls import path

from . import views

app_name = 'portfolio_site'

urlpatterns = [
    path('', views.index),
    path('suggest/', views.suggest, name="suggest"),
    path('vote/', views.vote, name="vote"),
]
