
try:
    s = raw_input("Enter Score: ")
    score = float(s)

    #print type(score)
    #if score in range (int(0.0), int(1.0)):
    if score >= 0.9:
        print 'A'
    elif score >= 0.8:
        print 'B'
    elif score >= 0.7:
        print'C'
    elif score >= 0.6:
        print 'D'
    else:
        print 'F'
        
except:
    print "The input is not a number or out of range."