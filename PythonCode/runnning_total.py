# ask the user for a number
# add the number to a running total
# ask if the use has more numbers to enter (if yes, repeat)

total = 0  # accumulator

more = 'y'
while more == 'y':
    num = int(input('What is the number?'))
    total += num  # agmented assignment
    more = input('do you have more(y/n?')

print('total:' + format(total, '3d'))
