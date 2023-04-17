#chapter3\HelloWorld\HelloWorld\views.py
from django.http import HttpResponse
from django.urls import reverse
def hello(request):
    ht="Hello Wold！<br/>导航列表：<br/>" +\
        "<a href='"+reverse("about")+"'>"+"关于HelloWord</a>"
    return HttpResponse(ht)
