top_advanced = open('../templates/top_advanced.html').read()
bottom = open('../templates/bottom.html').read()

index_content = open('../content/index.html').read()
about_content = open('../content/about.html').read()
events_content = open('../content/events.html').read()
spaces_content = open('../content/spaces.html').read()

from string import Template
template = Template(top_advanced)
index_top=template.safe_substitute(PAGE_TITLE="WELCOME", ACTIVE_INDEX="active", ACTIVE_SPACES="", ACTIVE_EVENTS="", ACTIVE_ABOUT="")
spaces_top=template.safe_substitute(PAGE_TITLE="SPACES", ACTIVE_INDEX="", ACTIVE_SPACES="active", ACTIVE_EVENTS="", ACTIVE_ABOUT="")
events_top=template.safe_substitute(PAGE_TITLE="EVENTS", ACTIVE_INDEX="", ACTIVE_SPACES="", ACTIVE_EVENTS="active", ACTIVE_ABOUT="")
about_top=template.safe_substitute(PAGE_TITLE="ABOUT", ACTIVE_INDEX="", ACTIVE_SPACES="", ACTIVE_EVENTS="", ACTIVE_ABOUT="active")

open('../docs/index.html', 'w+').write(index_top + index_content + bottom)
open('../docs/about.html', 'w+').write(about_top + about_content + bottom)
open('../docs/events.html', 'w+').write(events_top + events_content + bottom)
open('../docs/spaces.html', 'w+').write(spaces_top + spaces_content + bottom)

