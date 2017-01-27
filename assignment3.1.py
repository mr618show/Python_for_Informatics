try:
    Hours = float(input("Enter Hours:"))
    Rate = float(input("Enter Rate:"))
    if Hours <= 40:
        Pay= Hours * Rate
    else:
        Pay = 40 * Rate + (Hours - 40) * 1.5 * Rate
    print ("Pay:" , Pay)
except:
    print ("Error, please enter numeric input")

