exam1 = int(input("Grade on exam 1? "))
exam2 = int(input("Grade on exam 2? "))
final = int(input("Grade on final? "))
p1 = int(input("Grade on P1? "))
p2 = int(input("Grade on P2? "))
p3 = int(input("Grade on P3? "))
tophat = int(input("Grade on Top Hat? "))

# compute the project average
projects = (p1 + p2 + p3) / 3

average = exam1 * 0.12 + exam2 * 0.12 + final * 0.24 + projects * 0.39 \
			+ tophat * 0.13

print('Your average is:', average)

