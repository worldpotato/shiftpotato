from django.db import models

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")# Create your models here.
