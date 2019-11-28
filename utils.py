from datetime import datetime
from django.template import Template, Context
from django.shortcuts import render
import glob
import os
#Django import statements:
from django.http import HttpResponse
import db
# from urls import urlpatterns




def build_page_dictionary(page_name):
  single_file = find_specific_file("content", page_name)
  print("single_file", single_file)
  page_dict = {}
  page_dict.update({"ACTIVE_INDEX" : ""})
  page_dict.update({"ACTIVE_SPACES" : ""})
  page_dict.update({"ACTIVE_EVENTS" : ""})
  page_dict.update({"ACTIVE_ABOUT" : ""})
  file_name = os.path.basename(single_file)
  name_only, extension = os.path.splitext(file_name)
  page_dict.update({"page_link" : file_name})
  page_dict.update({"output": "docs/"+file_name})
  page_dict.update({"PAGE_TITLE": name_only})
  active_page_switch = {
      "index" : "ACTIVE_INDEX",
      "events" : "ACTIVE_EVENTS",
      "about" : "ACTIVE_ABOUT",
      "spaces": "ACTIVE_SPACES",
  }
  page_dict.update({active_page_switch.get(name_only): "active"})
  
  print("page_dict", page_dict)
  
  return page_dict

#use glob to find all of the files in the given directory
def find_all_files(directory):
  all_files = glob.glob(directory+"/*.*")
  return(all_files)

def find_specific_file(directory, file_name):
  theFile = glob.glob(directory+"/"+file_name+"*")[0]
  return(theFile)
  
##current
def update_item_list(list_of_dicts):
  for item in list_of_dicts:
    short_content=[]
    detailed_content =[]
    description_content_reader(item["content"], short_content, detailed_content)
    if len(short_content) >= 1:
      item.update({"short_content": short_content[0]})
    if len(detailed_content) >= 1:
      item.update({"detailed_content":detailed_content[0]}
    )
  return list_of_dicts
    
def build_navigation_dictionary_list():
  files = find_all_files("content")
  pages = []
  for file_path in files:
    page = {}
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    page.update({"PAGE_TITLE": name_only})
    page.update({"page_link" : "/"+file_name})
    pages.append(page)
 
  return pages




# description_content_reader - pulls both the long and short versions of the content out of the content file
# stores the short content as the first list entry in short_descripton variable (this is available to the calling function)
# stores the detailed content as the 1st entry in the detailed description variable (this is available to the calling funciton)
def description_content_reader(content, short_description, detailed_description):
  description_type = None
  current_description = None

  description_text = open(content).read()
  description_lines = description_text.splitlines()

  for line in description_lines:
    if line == "----SHORT DESCRIPTION----":
      description_type="short"
      short_description.append("")
      current_description=""
      continue
    elif line == "----DETAILED DESCRIPTION----":
      description_type="detailed"
      detailed_description.append("")
      current_description=""
      continue

    line = line.strip()  
    if description_type == "short":
      short_description[0] += " " + line
    elif description_type == "detailed":
      detailed_description[0] += " " + line
    else:
      print("something wroing in the description file", content)
      chad= input("cancel now before it's too late!!")
#vvvvvvvvvvvvvv -- old stuff: may be out of use--vvvvvvvvvvvvvvvvvvvvv

# set template takes the file name of a template file, 
# reads it and uses that to creates a object of Type Template
def set_template(template_file):
  page_template = open(template_file).read()
  my_template = Template(page_template)
  return my_template

# apply_fullpage_template takes a Template object and all of the 
# template replacement strings for a page and returns 
# the new page with the templated values replaced with the replacement strings
def apply_fullpage_template(page_template, page, content, pages, content_type_is_filename=True):
   
  print("applying template to:", page["PAGE_TITLE"])
  
  if content_type_is_filename:
    print("----> Taking this content:",content)
    content = open(content).read() 
  
  # Each page in pages looks 
  # { 
  #  'ACTIVE_INDEX':'active',
  #  'ACTIVE_SPACES':'',
  #  'ACTIVE_EVENTS':'',
  #  'ACTIVE_ABOUT':'',
  #  'content':'content/index.html',
  #  'page_link':'index.html',
  #  'output':'docs/index.html',
  #  'PAGE_TITLE':'index'
  # } 
  full_page = page_template.render(
    page=page,
    PAGE_CONTENT=content,
    COPYRIGHT_YEAR=datetime.now().year,
    pages=pages,
    spaces=spaces,
  )
  return full_page


    


# used to take a single event and apply the short description template to it
def apply_event_template(event_template, event_template_dict):
  print("applying event template to", event_template_dict["EVENT_TITLE"])
  event_short_content = []
  event_detailed_content = []
  description_content_reader(event_template_dict["content"], event_short_content, event_detailed_content)
  event_entry = event_template.render(
    ET = event_template_dict,
    EVENT_DETAILS = event_short_content[0],
    EVENT_EXTENDED_DETAILS = event_detailed_content[0]
  )
  return event_entry

# used to build the full content from multiple different singular event/space contents
def apply_all_template(all_template, page_content):
  print("creating the content of the full page")
  full_page_content = all_template.render(
    ALL_CONTENT = page_content
  )
  return full_page_content

# used to take a single space and apply the short description template to it
def apply_space_template(space_template, space_template_dict, fullpage_template, page, pages):
  print("applying space template to", space_template_dict["SPACE_NAME"])
  space_short_content = []
  space_detailed_content = []
  description_content_reader(space_template_dict["content"],space_short_content, space_detailed_content)
  space_entry = space_template.render(
    ST = space_template_dict,
    SPACE_DESCRIPTION = space_short_content[0]
  )
  
  # Create the new space pages here
  individual_space_page = apply_fullpage_template(fullpage_template, page, space_detailed_content[0], pages, False)
  write_file(individual_space_page, space_template_dict["output"])

  return space_entry

# write_file takes html content (or really any content) and an output file to write to
def write_file(html_page, output):
  print("----> Writing the output to", output)
  open(output, 'w+').write(html_page)









    


# Auto generate the pages list of dictionaries. 
# pages list of dicts is taken in as function parameter all_content_dict
def build_pages_list(all_content_dict):  
  files = find_all_files("content")
  print("--------",files)
  for file_path in files:
    page_dict = {}
    page_dict.update({"ACTIVE_INDEX" : ""}),
    page_dict.update({"ACTIVE_SPACES" : ""}),
    page_dict.update({"ACTIVE_EVENTS" : ""}),
    page_dict.update({"ACTIVE_ABOUT" : ""}),
    print("------------ File Path",file_path)
    file_name = os.path.basename(file_path)
    print("----------------File Name",file_name)
    name_only, extension = os.path.splitext(file_name)
    print("----------------",name_only)
    page_dict.update({"content": file_path})
    page_dict.update({"page_link" : file_name})
    page_dict.update({"output": "docs/"+file_name})
    page_dict.update({"PAGE_TITLE": name_only})

    active_page_switch = {
      "index" : "ACTIVE_INDEX",
      "events" : "ACTIVE_EVENTS",
      "about" : "ACTIVE_ABOUT",
      "spaces": "ACTIVE_SPACES",
    }
    page_dict.update({active_page_switch.get(name_only): "active"})
    all_content_dict.append(page_dict)
    print(all_content_dict)

def create_new_content():
  new_content= '''<h1>New Content!</h1>
<p>New content...</p>'''
  write_file(new_content, "./content/new_content_page.html")
      
def build_site(pages, fullpage_template, event_template, space_template):
  for page in pages:
    item_content = ""
    full_page = None
    page_title = page["PAGE_TITLE"]
    #special caveat for spaces and events
    if page_title == "spaces" or page_title == "events" :
      if page_title == "events":
        for event in events:
          #for events we use the apply_event_template function to build up the content
          item_content += ' '+ apply_event_template(event_template, event)
      elif page_title == "spaces":
        for space in spaces:
          #for spaces we use the apply_space_template to build up the content
          #note this function also builds out the individual space pages
          item_content += apply_space_template(space_template, space, fullpage_template, page, pages)
      
      full_item_template = set_template(page["content"])
      item_content =  apply_all_template(full_item_template, item_content)
      full_page = apply_fullpage_template(fullpage_template, page, item_content, pages, False)
      write_file(full_page, page["output"])
    else:
      full_page = apply_fullpage_template(fullpage_template, page, page["content"], pages)
      write_file(full_page, page["output"])