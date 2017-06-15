speed = float(input("Know how fast you're going? "))

if speed < 0:
	print("That doesn't make sense...")
elif speed <= 55:
	print("No fine")
elif speed < 60:
	print("You should slow down, no fine this time")
elif speed < 70:
	print("Here's your $50 speeding ticket")
else:
	print("Here's your $200 speeding ticket")
