# This file has the "routing" -- it associates "view functions" (found in
# views.py) with different paths.

from django.urls import path, re_path

import views

urlpatterns = [
  path("index.html", views.serve_index),
  path("about.html", views.serve_about),
  path("events.html", views.serve_events),
  path("spaces.html", views.serve_spaces),
  re_path(r'spaces/*', views.serve_generic_detailed_space),   #pretty sure there's a better way to do this, but i couldn't find anything to help me understand how to do the regular expressions for django
]

# Boilerplate to include static files.
# Static files include CSS and images -- basically anything that isn't HTML or
# Python code -- stuff we just want to "serve up" for the browser to download
# and utilize and won't be changed by Python code (hence the term "static").
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

