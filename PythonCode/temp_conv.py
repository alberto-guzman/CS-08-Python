# write a program
# prints a celsius to farenheit temperature conversion chart
# show for  for 0 C to 100 C
# F = 9/5C+32

print(format('C', '>4s'), format('F', '>10s'), sep='')


temp_C = 0

while temp_C <= 100:
    temp_F = 9 / 5 * temp_C + 32
    print(format(temp_C, '4d'), format(temp_F, '6.2f'), sep='')
    temp_C += 5
