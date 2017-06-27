# Problem: Ask the user for a letter.
# Print "yes" if the entered letter is in ANY of my friends' names
# Print "no" otherwise

# Priming input
letter = input("What letter? ")
# Input validation loop
while len(letter) != 1:
	# Second input for incorrect values
	letter = input("NO! What letter? ")

# List of friends
friends = ['Alice', 'Bob', 'Charlie', 'Dina', 'Edgar']
# Flag to determine if the letter was found
is_found = False

# Check each friend
for friend in friends:
	# Check each letter of the friend's name
	for friend_letter in friend:
		# Compare this letter of the name to the typed letter
		if friend_letter == letter:
			is_found = True
# Print the result
if is_found:
	print("Yes")
else:
	print("No")
