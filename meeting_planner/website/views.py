from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


# Please add: An about page that shows some text about yourself
def about(request):
    return HttpResponse("I'm Reindert and I make courses for Pluralsight.")
