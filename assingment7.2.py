import os.path
count = 0
sum = 0
fname = raw_input('Enter the file name: ')
if os.path.isfile(fname):
    fhand = open(fname)
    for line in fhand: 
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:'):
            count+=1
           # print line
            copos=line.find(':')
            host = float(line[copos+2:])
            sum = sum + host
    ave = sum/count       
    print count
    print 'Average spam confidence:', ave

        