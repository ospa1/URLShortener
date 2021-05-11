from django.urls import path
from . import views

app_name = "url_shorts"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:url_hash>', views.go, name='go'),
    path('shorten', views.shorten, name='shorten'),
]
