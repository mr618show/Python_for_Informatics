import os.path
fname = raw_input ('Enter the file name: ')
if os.path.isfile(fname):
    fhand = open(fname)
    for line in fhand:
        #lineUpper = line.upper()
        print line.upper()