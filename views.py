import requests
from django.http import HttpResponse
from django.shortcuts import render


#there are 4 django view functions index,about,events, spaces
def serve_index(request):
  content = open("./docs/index.html").read()
  return HttpResponse(content)

def serve_about(request):
  content = open("./docs/about.html").read()
  return HttpResponse(content)

def serve_events(request):
  content = open("./docs/events.html").read()
  return HttpResponse(content)

def serve_spaces(request):
  content = open("./docs/spaces.html").read()
  return HttpResponse(content)