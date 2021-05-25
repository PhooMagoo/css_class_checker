# Find style sheets, get list of classes, check to see if any go unused.

import bs4
import re
import requests
from pprint import pprint

##############################################################

css_list = []
css_classes = []

# The site we're lookin' at.
start_url = input(r"Enter URL: ")

# How we locate the CSS files.
regexCssFile = re.compile('(.*?)\.css')
regexCssClass = re.compile('\.(.*\w)')


# Get the site.
res = requests.get(start_url)

# Scan the site for CSS files.
cssFiles = regexCssFile.findall(res.text)

# Get the CSS files, build URLs and add them to a list
for file in cssFiles:
    file = file.strip()
    file = file[file.find('"/'):] + ".css"
    css_list.append(start_url + file.replace('"', ""))

for url in css_list:
    res = requests.get(url)
    cssClasses = regexCssClass.findall(res.text)

for cls in cssClasses:
    css_classes.append(cls)

pprint(css_classes)
