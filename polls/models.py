from django.db import models

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class Question(models.Model):
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
