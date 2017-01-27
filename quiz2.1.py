import re
sumnum = 0
count = 0 
#fname = open('regex_sum_42.txt')
fname = open('regex_sum_190077.txt')
for line in fname:
    line = line.rstrip()
    #x = re.findall(r'\b\d+\b', line)
    x=re.findall('\s*([0-9]+)\s*',line)  
    if len(x) > 0 :
        print x
        count += len (x)
        res = [int(i) for i in x]
        total = sum(res)
        sumnum+= total
print 'There are',count,'values with a sum=', sumnum