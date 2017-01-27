
import urllib
import xml.etree.ElementTree as ET

#url = ' http://python-data.dr-chuck.net/comments_42.xml'
url = ' http://python-data.dr-chuck.net/comments_190079.xml'
sum = 0

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)

counts = tree.findall('.//count')
for i in counts:
#    print i.text
    sum += int(i.text)
print sum