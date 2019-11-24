import utils
import sys
#django import statements
import os
from django.conf import settings
from django.core.management import execute_from_command_line


# Main
def main():
  command = None
  print("command line:", sys.argv)

  # if len(sys.argv) <= 2:
  #   print('''
  #   Usage:
  #     Rebuild site: python3 manage.py build
  #     Create new page: python3 manage.py new)
  #     ''')
  #   return
  # elif len(sys.argv) >= 3:
  #   command = sys.argv[2]
  

  # while True:
  #   print("evaluating command:", command)
  #   if command == "build":
  #     fullpage_template = utils.set_template('templates/whole_page_template.html')
  #     event_template = utils.set_template('templates/event_template.html')
  #     space_template = utils.set_template('templates/space_template.html')
  #     pages = []

  #     utils.build_pages_list(pages)
  #     utils.build_site(pages, fullpage_template, event_template, space_template)
  #     break
  #   elif command == "new":
  #     utils.create_new_content()
  #     break
  #   elif command == "quit":
  #     print("quitting without doing anything")
  #     break
  #   else:
  #     print("invalid or missing command")
  #     print("please enter either build, new or quit")
  #     command = input(">> ")
  
  #new django boilerplate --- this will probably have to change
  print("now serving our static html page")


  print("chad was here")
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))

  settings.configure(
      DEBUG=True,
      ROOT_URLCONF='urls',
      STATIC_URL='static/',
      STATIC_ROOT=os.path.join(BASE_DIR, 'static'),
      INSTALLED_APPS=[
          'django.contrib.staticfiles',
      ],
      TEMPLATES=[{
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')],
      }],
  )

  execute_from_command_line(sys.argv)
  
if __name__ == "__main__":
  main()