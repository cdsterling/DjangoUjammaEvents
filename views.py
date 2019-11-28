import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
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
    "the_page_content": content,
    "spaces_nav": db.spaces,
  }
  return render(request, "generic_page_template.html", context)

def serve_about(request):
  content = open("./content/about.html").read()
  page_dictionary = utils.build_page_dictionary("about.html")
  page_navigation = utils.build_navigation_dictionary_list()
  context = {
    "page": page_dictionary,
    "pages": page_navigation,
    "the_page_content": content,
    "spaces_nav": db.spaces,
  }
  return render(request, "generic_page_template.html", context)

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

  return render(request, "event_template.html", context)

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
  return render(request, "space_template.html", context)

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
    "the_page_content": content,
  }
  return render(request, "generic_page_template.html", context)


def serve_contact(request):
  print("Contact page")
  response =requests.get('https://api.github.com/users/cdsterling/repos')
  git_repos = response.json()
  print(git_repos)
  page_dictionary = utils.build_page_dictionary("contact.html")
  page_navigation = utils.build_navigation_dictionary_list()
  
  context = {
    "page": page_dictionary,
    "pages": page_navigation,
    "spaces_nav": db.spaces,
    "git_repos":git_repos,
  }
  return render(request, "contact.html", context)


def send_email(request):
  
  if request.POST["name"] and request.POST["email"] and request.POST["message"]:
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
  

    requests.post(
      "https://api.mailgun.net/v3/sandboxfae1ac1364e846a5a9ad50abf118e90c.mailgun.org/messages",
      auth=("api", "63bcacf271ce3ed0c995a4943be51ba2-e470a504-4ba0d732"),
      data={"from": name+" <"+email+">",
        "to": ["cdsterling@gmail.com"],
        "subject": "Contact message",
        "text": message,
      }
    )
  return redirect("index.html")
