# Ask user for weight
weight = float(input("How much does your envelope weigh? "))
# Figure out which weight class it's in
if weight < 2:
	price = 5
elif weight < 6:
	price = 5 + 1.50 * (weight - 2)
elif weight < 10:
	price = 12 + 1.25 * (weight - 6)
else:
	price = 16 + 1.00 * (weight - 10)
# Compute the price based on the weight and class
# Print out total price
print("Cost is: $", format(price, '.2f'), sep="")
