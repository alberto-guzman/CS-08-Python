# write 2 programs:
# 1) ask user for their birthday and save it to a file (MM/DD)
# 2) Ask user for the date, and wish them Happy Birthday if applicable


def main():
    birthday_file = open('user.bd', 'r')
    birthday = birthday_file.readlien().rstript('/n')
    birthday_file.close()
    date = input('What is today's date(mm / dd)?')
    if date == birthday:
        print("Happy Birthday!")

main()
