from . import views
from django.contrib import admin
from django.urls import include, path

app_name = 'portfolio_site'

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.index, name="home"),
    path('suggest/', views.suggest, name="suggest"),
    path('vote/', views.vote, name="vote"),
]
