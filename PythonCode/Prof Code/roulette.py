number = int(input("What number? "))

is_even = (number % 2 == 0)
is_odd = not is_even

odd_is_red = 1 <= number <= 10 or 19 <= number <= 28
odd_is_black = not odd_is_red

if number == 0:
	print("Green")
if number > 0 and is_even and odd_is_red:
	print("Black")
if number > 0 and is_odd and odd_is_red:
	print("Red")
if number > 0 and is_even and odd_is_black:
	print("Red")
if number > 0 and is_odd and odd_is_black:
	print("Black")
