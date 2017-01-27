import re
fhand= open('mbox.txt')
counts = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
        if len(x) > 0:
            addr = x[0]
            counts[addr] = counts.get(addr,0) +1 

lst = counts.keys()
lst.sort()
for key in lst:
    print (key, counts[key])
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3, 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1, 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3, 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1, 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2, 'ray@media.berkeley.edu': 1}

#Note: without str() it will error out
