whole_page_template = open('../templates/whole_page_template.html').read()
index_content = open('../content/index.html').read()
about_content = open('../content/about.html').read()
events_content = open('../content/events.html').read()
spaces_content = open('../content/spaces.html').read()

from string import Template
template = Template(whole_page_template)
index_page=template.safe_substitute(PAGE_TITLE="WELCOME", ACTIVE_INDEX="active", ACTIVE_SPACES="", ACTIVE_EVENTS="", ACTIVE_ABOUT="", PAGE_CONTENT=index_content)
spaces_page=template.safe_substitute(PAGE_TITLE="SPACES", ACTIVE_INDEX="", ACTIVE_SPACES="active", ACTIVE_EVENTS="", ACTIVE_ABOUT="", PAGE_CONTENT=spaces_content)
events_page=template.safe_substitute(PAGE_TITLE="EVENTS", ACTIVE_INDEX="", ACTIVE_SPACES="", ACTIVE_EVENTS="active", ACTIVE_ABOUT="", PAGE_CONTENT=events_content)
about_page=template.safe_substitute(PAGE_TITLE="ABOUT", ACTIVE_INDEX="", ACTIVE_SPACES="", ACTIVE_EVENTS="", ACTIVE_ABOUT="active", PAGE_CONTENT=about_content)

open('../docs/index.html', 'w+').write(index_page)
open('../docs/about.html', 'w+').write(about_page)
open('../docs/events.html', 'w+').write(events_page)
open('../docs/spaces.html', 'w+').write(spaces_page)

