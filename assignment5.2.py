try:
    min = None
    max = None
    while True :
            line = raw_input('Enter a number:')
            if line == 'done':
                break
            num = float(line)
            if min is None or num < min:
                min = num
            if max is None or num > max:
                max = num
            #print ('Loop:', num, min, max)
           
    print ('Min: %s, Max: %s' %(min, max))
except:
        print 'Invalid input, please enter a number.'
