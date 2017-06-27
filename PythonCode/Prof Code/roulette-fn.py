# Asks the user for a pocket number. With input validation.
def ask_user():
	temp = int(input("What number? "))
	while temp < 0 or temp > 36:
		temp = int(input("Invalid. What number? (0-36) "))
	return temp

# Checks whether this number is even
def is_even(some_number):
	# return True if even, False if not
	if some_number % 2 == 0:
		return True
	else:
		return False

# Checks whether this number is odd
def is_odd(some_number):
	return not is_even(some_number)

# Checks whether this number is in the range where odd is red
def odd_is_red(some_num):
	return (1 <= some_num <= 10 or 19 <= some_num <= 28)

# Checks whether this number is in the range where odd is black
def odd_is_black(some_number):
	return not odd_is_red(some_number)

# Determines the color of a pocket by its number
def color(number):
	if number == 0:
		return "green"
	elif is_even(number) and odd_is_red(number):
		return "black"
	elif is_odd(number) and odd_is_red(number):
		return "red"
	elif is_even(number) and odd_is_black(number):
		return "red"
	elif is_odd(number) and odd_is_black(number):
		return "black"

def main():
	number = ask_user()
	print("This pocket is " + color(number))

main()

