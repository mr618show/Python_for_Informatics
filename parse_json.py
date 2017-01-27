import urllib
import json
sum = 0
#url= ' http://python-data.dr-chuck.net/comments_42.json'
url = 'http://python-data.dr-chuck.net/comments_190083.json'

uh= urllib.urlopen(url)
data = uh.read()


parsed_data = json.loads(data)
comments = parsed_data["comments"]
for comment in comments:
    sum += int(comment['count'])

print sum