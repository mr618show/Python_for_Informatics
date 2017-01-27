import re
counts = dict()
lst = list()
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        line = line.split()
        #print line
        if len(line)>3:
            x = line[2]
            print x
        counts[x] = counts.get(x,0)+1
print counts



#     Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt {'Fri': 20, 'Thu': 6, 'Sat': 1}