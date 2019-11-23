import utils
import sys
#django import statements
from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.core.management import execute_from_command_line

urlpatterns = [
  path("index.html", utils.index),
  path("about.html", utils.about),
  path("events.html", utils.events),
  path("spaces.html", utils.spaces)
]

# Main
def main():
  command = None
  print("command line:", sys.argv)

  if len(sys.argv) == 1:
    print('''
    Usage:
      Rebuild site: python3 manage.py build
      Create new page: python3 manage.py new)
      ''')
    return
  elif len(sys.argv) >= 2:
    command = sys.argv[1]
  

  while True:
    print("evaluating command:", command)
    if command == "build":
      fullpage_template = utils.set_template('templates/whole_page_template.html')
      event_template = utils.set_template('templates/event_template.html')
      space_template = utils.set_template('templates/space_template.html')
      pages = []

      utils.build_pages_list(pages)
      utils.build_site(pages, fullpage_template, event_template, space_template)
      break
    elif command == "new":
      utils.create_new_content()
      break
    elif command == "quit":
      print("quitting without doing anything")
      break
    else:
      print("invalid or missing command")
      print("please enter either build, new or quit")
      command = input(">> ")
  
  #new django boilerplate --- this will probably have to change
  print("now serving our static html page")
  settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
  )
  execute_from_command_line(sys.argv)
  
if __name__ == "__main__":
  main()