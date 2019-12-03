import utils
import sys
#django import statements
import os
from django.conf import settings
from django.core.management import execute_from_command_line



# Main
def main():
  #new django boilerplate --- this will probably have to change
  print("now serving our html pages")

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
