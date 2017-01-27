import urllib
count = 0
fhand = urllib.urlopen('http://www.py4inf.com/code/intro-short.txt')
while True:
    data = fhand.read(512)
    if len(data)<1: break
    count+=len(data)
    if count <3000:
        print data
print count
fhand.close()


# Exercise 12.3 Use urllib to replicate the previous exercise of 
# (1) retrieving the document from a URL, 
# (2) displaying up to 3000 characters, and 
# (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.