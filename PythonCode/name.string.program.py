# 1. ask user for their full name, print their initials


# def initials():
#     name = input('What is your name?')
#     for name_part in name.split(' '):
#         for word in name:
#             word[]


# initials()


def main():
    full_name = input("What is your full name?")
    initials = ''
    for word in full_name.split(' '):
        initials = initials + word[0]
    print('your initials are:', initials)


main()
