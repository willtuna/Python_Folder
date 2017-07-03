#!/usr/env python2.7

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter -')
# using read() would turn the webpage html into string

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
#print soup.prettify()

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
