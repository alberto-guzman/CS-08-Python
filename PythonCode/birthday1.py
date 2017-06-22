# write 2 programs:
# 1) ask user for their birthday and save it to a file (MM/DD)
# 2) Ask user for the date, and wish them Happy Birthday if applicable


def main():
    birthday = input('What is your birthday (mm/dd)?')
    birthday_file = open('user.bd', 'w')
    birthday_file.write(birthday + '\n')
    birthday_file.close()

main()
