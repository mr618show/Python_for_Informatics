import os.path
fname = raw_input ('Enter the file name: ')
if os.path.isfile(fname):
    fhand = open(fname)
    count = 0 
    for line in fhand:
        if line.startswith('Subject:'):
            count+=1
    print 'There are', count, 'subject line in file', fname
elif fname == "na na boo boo":
    print  fname.upper(), ' TO YOU, You are punk\'d!'
else:
    print 'File cannot be opened : ', fname