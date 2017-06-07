exam1 = int(input("Grade on exam 1?"))
exam2 = int(input("Grade on exam 2?"))
final = int(input("Grade on final?"))

p1 = int(input("Grade on p1?"))
p2 = int(input("Grade on p2?"))
p3 = int(input("Grade on p3?"))


# compute the program average
program = (p1 + p2 + p3) / 3
tophat = int(input("Grade on top hat?"))

average = exam1 * 0.12 + exam2 * 0.12 + final * 0.24 + program * 0.39 \
    + tophat * 0.13

print('your average is:', average)
