import requests
from django.http import HttpResponse
from django.shortcuts import render
import utils
#get all the event and spaces details
import db

#there are 4 django view functions index,about,events, spaces
def serve_index(request):
  print("Serving_index")
  content = open("./content/index.html").read()
  page_dictionary = utils.build_page_dictionary("index.html")
  # print("--vvvv Content vvvv--")
  # print(content)
  # print("--^^^^ Content ^^^^--")
  page_navigation = utils.build_navigation_dictionary_list()
  context = {
    "page":page_dictionary,
    "pages": page_navigation,
    "PAGE_CONTENT": content,
    "spaces_nav": db.spaces,
  }
  return render(request, "whole_page_template.html", context)

def serve_about(request):
  content = open("./content/about.html").read()
  page_dictionary = utils.build_page_dictionary("about.html")
  page_navigation = utils.build_navigation_dictionary_list()
  context = {
    "page": page_dictionary,
    "pages": page_navigation,
    "PAGE_CONTENT": content,
    "spaces_nav": db.spaces,
  }
  return render(request, "whole_page_template.html", context)

def serve_events(request):
  page_dictionary = utils.build_page_dictionary("events.html")
  page_navigation = utils.build_navigation_dictionary_list()
  event_list = utils.update_item_list(db.events)
  # print("--vvvv event_list vvvv--")
  # print(event_list)
  # print("--^^^^ event_list ^^^^--")
  context = {
    "page": page_dictionary,
    "pages": page_navigation,
    "event_list" : event_list,
    "spaces_nav": db.spaces,
  }

  return render(request, "whole_page_template.html", context)

def serve_spaces(request):
  
  page_dictionary = utils.build_page_dictionary("spaces.html")
  page_navigation = utils.build_navigation_dictionary_list()
  space_list = utils.update_item_list(db.spaces)
  print("--vvvv event_list vvvv--")
  print(request.path)
  print("--^^^^ event_list ^^^^--")
  context = {
    "page": page_dictionary,
    "pages": page_navigation,
    "space_list" : space_list,
    "spaces_nav": db.spaces,
  }
  return render(request, "whole_page_template.html", context)

def serve_generic_detailed_space(request):
  page_navigation = utils.build_navigation_dictionary_list()
  space_list = utils.update_item_list(db.spaces)
  content = ""
  page = {}
  for space in db.spaces:
    print("space page link:", space["SPACE_PAGE_LINK"])
    print("request path", request.path)
    if space["SPACE_PAGE_LINK"] == request.path:
      content = space["detailed_content"]
      page.update({"PAGE_TITLE": space["SPACE_NAME"]})
  
  print("--vvvv event_list vvvv--")
  print(page)
  print("----")
  print(content)
  print("--^^^^ event_list ^^^^--")
  context = {
    "page": page,
    "pages": page_navigation,
    "space_list" : space_list,
    "spaces_nav": db.spaces,
    "PAGE_CONTENT": content,
  }
  return render(request, "whole_page_template.html", context)
