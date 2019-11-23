from datetime import datetime
from jinja2 import Template
import glob
import os


page_links = {
  "index_link" : "./index.html",
  "spaces_link" : "./spaces.html",
  "events_link" : "./events.html",
  "about_link" : "./about.html",  
}
events = [
  {
    "content" : "events/afro_comic_con.html",
    "output" : "docs/afro_comic_con.html",
    "EVENT_IMAGE" : "images/events/acc_logo.jpg",
    "EVENT_TITLE" : "Afro Comic Con",
    "EVENT_DATES" : "Nov 3-7 2019",
    "EVENT_SPACE_NAME" : "SAE Expression College",
    "EVENT_SPACE_ADDRESS" : "6601 Shellmound St, Emeryville, CA 94608",
    "EVENT_ORGANIZER" : "The Afro Comic Con Planning Committe",
    "EVENT_ORGANIZER_URL": "https://www.afrocomiccon.org/",
    "EVENT_EMAIL" : "acc-planning@gmail.com",
    "EVENT_MODAL_ID" :"afro_comic_con",
  },
  {
    "content" : "events/travel_more5.html",
    "output" : "docs/travel_more5.html",
    "EVENT_IMAGE" : "images/events/trvl_black_flyer.png",
    "EVENT_TITLE" : "Travel More Spend Less #5",
    "EVENT_DATES" : "August 25, 2019",
    "EVENT_SPACE_NAME" : "Kingston 11 Cuisine",
    "EVENT_SPACE_ADDRESS" : "2270 Telegraph Ave, Oakland, CA 94612",
    "EVENT_ORGANIZER" : "Traveling Black",
    "EVENT_ORGANIZER_URL": "https://traveling.black/",
    "EVENT_EMAIL" : "travelingblack@gmail.com",
    "EVENT_MODAL_ID" : "travel_more5",
  },
  {
    "content" : "events/black_to_yoga.html",
    "output" : "docs/black_to_yoga.html",
    "EVENT_IMAGE" : "images/events/black_to_yoga_flyer.jpg",
    "EVENT_TITLE" : "Yoga Informational Workshop and Practice for Men",
    "EVENT_DATES" : "November 10, 2019",
    "EVENT_SPACE_NAME" : "Queen Hippie Gypsie",
    "EVENT_SPACE_ADDRESS" : "337 14th St, Oakland, CA 94612",
    "EVENT_ORGANIZER" : "Men of Substance",
    "EVENT_ORGANIZER_URL": "https://www.facebook.com/MenOfSubstanceMag/",
    "EVENT_EMAIL" : "menofsubstancemag@gmail.com",
    "EVENT_MODAL_ID" : "black_to_yoga",
  }, 
]

spaces = [
  {
    "content" : "spaces/kingston11.html",
    "output" : "docs/kingston11.html",
    "SPACE_LOGO" : "./images/spaces/k11_logo2.png",
    "SPACE_NAME" : "Kingston 11 Cuisine",
    "SPACE_IMAGE" : "./images/spaces/k11_event_space.jpg",
    "SPACE_PAGE_LINK" : "./kingston11.html",
  },
  {
    "content" : "spaces/queen_hippie_gypsy.html",
    "output" : "docs/queen_hippie_gypsy.html",
    "SPACE_LOGO" : "./images/spaces/qhg_storefront.jpg",
    "SPACE_NAME" : "Queen Hippie Gypsy",
    "SPACE_IMAGE" : "./images/spaces/qhg_kyrah_eventspace.jpg",
    "SPACE_PAGE_LINK" : "./queen_hippie_gypsy.html",
  },
  {
    "content" : "spaces/SAE_Expression_College.html",
    "output" : "docs/SAE_Expression_College.html",
    "SPACE_LOGO" : "./images/spaces/sae_logo.jpg",
    "SPACE_NAME" : "SAE Expression College",
    "SPACE_IMAGE" : "./images/spaces/sae_outdoor.jpg",
    "SPACE_PAGE_LINK" : "./SAE_Expression_College.html",
  }
]

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




#use glob to find all of the files in the given directory
def find_all_files(directory):
  all_files = glob.glob(directory+"/*.*")
  return(all_files)

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
      


# Main
def main():
  fullpage_template = set_template('templates/whole_page_template.html')
  event_template = set_template('templates/event_template.html')
  space_template = set_template('templates/space_template.html')
  pages = []

  build_pages_list(pages)

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
  
if __name__ == "__main__":
  main()