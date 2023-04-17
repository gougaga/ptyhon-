#chapter3\HelloWorld\HelloWorld\urls.py
from django.urls import path
from . import views
from about import views as about_views
urlpatterns = [
    path('', views.hello, name='hello'),
    path('about/', about_views.about,name="about"),
]
