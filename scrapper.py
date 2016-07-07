
# https://www.youtube.com/watch?v=qfGthiqwaZo

import urllib2
from import html2text #formats HTML to markdown

# read each line of the md
for line in html2text(urllib2.urlopen("http://www.moviebodycounts.com/Braveheart.htm").read()).split("\n")
    if "IMDb" in line:
        print line.split("[IMDb]")
    if "Film:" in line:
        print line.split("[IMDb]")
