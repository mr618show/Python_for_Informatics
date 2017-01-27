lst = []
while True:
    num = raw_input('Enter a number:')
    if num == 'done': 
        break
    num = float(num)
    lst.append(num)
#print lst
print'Maximum:', max(lst)
print'Minimum:', min(lst)

