# This file has the "routing" -- it associates "view functions" (found in
# views.py) with different paths.

from django.urls import path

import views

urlpatterns = [
  path("index.html", views.serve_index),
  path("about.html", views.serve_about),
  path("events.html", views.serve_events),
  path("dspaces.html", views.serve_spaces),
]

# Boilerplate to include static files.
# Static files include CSS and images -- basically anything that isn't HTML or
# Python code -- stuff we just want to "serve up" for the browser to download
# and utilize and won't be changed by Python code (hence the term "static").
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

