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


# ask user to type any string, then determine
# the most frequent characted.
# hint: double loop, what do you have to keep track of

def string():
    string = input("Type a string?")
    initials = ''
    for i in string:
        for j in i:

        initials = initials + word[0]
    print('your initials are:', initials)


string()


# pseudo code
# get sging as imports
# condiser each character:
# how many occurances?
# if > max so far, this is the new most frequent


def main():
    string = input("Type a string:")
    highest_count = 0
    most_frequent = ''
    for char in string:
        count = how_many(string, char)  # how many times does the character appear in the string
        if count > highest_count:
            highest_count = count  # replace if you find something higher
            most_frequent = char
    print("Most frequent:", most_frequent)


def how_many(string, character):
    result = 0
    for string_char in string:
        if string_char == character:
            result += 1
        return result


main()


# could also include str.count method


def main():
    string = input("Type a string:")
    highest_count = 0
    most_frequent = ''
    for char in string:
        count = string.count(char)
        if count > highest_count:
            highest_count = count  # replace if you find something higher
            most_frequent = char
    print("Most frequent:", most_frequent)
