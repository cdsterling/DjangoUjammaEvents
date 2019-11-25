import requests
from django.http import HttpResponse
from django.shortcuts import render
import utils


#there are 4 django view functions index,about,events, spaces
def serve_index(request):
  print("Serving_index")
  content = open("./content/index.html").read()
  page_dictionary = utils.build_page_dictionary("index.html")
  print("--vvvv Content vvvv--")
  print(content)
  print("--^^^^ Content ^^^^--")
  page_navigation = utils.build_navigation_dictionary_list()
  context = {
    "page":page_dictionary,
    "pages": page_navigation,
    "PAGE_CONTENT": content,
  }

  return render(request, "whole_page_template.html", context)

def serve_about(request):
  content = open("./docs/about.html").read()
  return HttpResponse(content)

def serve_events(request):
  content = open("./docs/events.html").read()
  return HttpResponse(content)

def serve_spaces(request):
  content = open("./docs/spaces.html").read()
  return HttpResponse(content)