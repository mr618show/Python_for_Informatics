

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

#url = raw_input('Enter - ')

#url = ' http://python-data.dr-chuck.net/known_by_Fikret.html '
url = 'http://python-data.dr-chuck.net/known_by_Triniti.html '

for i in range (1,8):

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    res= []
    for tag in tags:
        #print tag.get('href', None)
        res.append(tag.get('href', None))
    #print res[2]
    url = res[17]

print res[17]
# how to extract the name "Shanyse"?

