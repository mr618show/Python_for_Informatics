try:
    count =0
    sum =0
    while True :
            line = raw_input('Enter a number:')
            if line == 'done':
                break
            num = float(line)
            count = count +1
            sum = sum + num
            mean = sum/ count
    print ('Sum: %s, Count: %s, Mean: %s' %(sum, count, mean ))
except:
        print 'This is not a number, please enter a number.'
