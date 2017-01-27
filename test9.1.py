import os.path
file = 'test.txt'
counts = dict()
if os.path.isfile(file):
    fhand = open(file)
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        for word in line:
            counts[word]=counts.get(word,0)+1
    print (counts)
for key in counts:
    if len(counts[key]>1):
        print (key)


