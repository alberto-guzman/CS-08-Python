# prompt user for number (integer)
# determin which numbers are prime within  0 -n


def is_square(num):
    i = 1
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False


def main():
    # Prompt the user for a number
    number = int(input("Number: "))
    # print all squares not great than number
    print_all_squares_lower(number + 1)


def print_all_squares_lower(how_big):
    for candidate in range(how_big):
        if is_square(candidate):
            print(candidate)

main()
