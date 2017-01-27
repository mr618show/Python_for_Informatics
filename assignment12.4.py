import urllib
# import re
url = 'http://data.pr4e.org/intro-short.txt'
html = urllib.urlopen(url).read()
# count = 0 
# print html
# links = re.findall('<p>', html) 
# for link in links:
#     print link
#     count+=1
# print count

from BeautifulSoup import *
soup = BeautifulSoup(html)
links = [tag for tag in soup.findAll('p') if tag.has_attr('href')]

# Exercise 12.4 Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the para- graphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several small web pages as well as some larger web pages.