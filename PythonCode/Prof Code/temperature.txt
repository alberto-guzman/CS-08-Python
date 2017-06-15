# Print the header
print(format('C', '>4s'), format('F', '.>10s'), sep='')
# Print a row for each value 0 to 100, inclusive (by 5s)
for temp_celsius in range(0, 101, 5):
	temp_f = 9 / 5 * temp_celsius + 32
	print(format(temp_celsius, '4d'), format(temp_f, '.>10.2f'), sep='')

