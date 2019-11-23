Ujamma Events
Chad Sterling


4 pages for Ujamma events - a community based website that puts people who have spaces in touch with people who want to host events.

Relevant Files:
  ./README.md
  ./build.py              -   Python script to create my static html files in the docs directory from files in the content directory templates directory and events directory
      
  ./docs/index.html       -   static html file built by build.py
  ./docs/events.html      -   static html file built by build.py
  ./docs/spaces.html      -   static html file built by build.py
  ./docs/about.html       -   static html file built by build.py
  ./docs/kingston11.html  -   static detaild description page for kingston 11, built by build.py
  ./docs/queen_hippie_gypsy.html  -  static detaild description page for Queen Hippie Gypsy, built by build.py
  ./docs/SAE_Expression_College.html  -  static detaild description page for SAE Expression College, built by build.py

  ./docs/css/uje.css      -   css file used by static html files
  ./docs/images/*         -   images used by static html files


  ./templates/whole_page_template.html    -   full page template for all static files, uses templating for page title, active link and page content (used by build_advanced2.py)
  ./templates/event_template.html - a template for a single event
  ./templates/space_template.html - a template for a single space
  
  ./content/index.html    -   content of the static docs/index.html file, used to create docs/index.html by build.sh and build.py
  ./content/events_using_templates.html   -   content of the static docs/events.html it has been templated for use with the ./templates/event_template.html file
  ./content/spaces_using_templates.html   -   content of the static docs/events.html it has been templated for use with the ./templates/event_template.html file
  ./content/spaces.html   -   content of the static docs/spaces.html file, used to create docs/index.html by build.sh and build.py
  ./content/about.html    -   content of the static docs/about.html file, used to create docs/index.html by build.sh and build.py
  ./originalSite/*        -   sub directory containing the original static html files and cooresponding supporting files
  

