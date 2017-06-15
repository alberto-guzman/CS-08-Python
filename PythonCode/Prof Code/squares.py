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
    # Determine if the number is square
    result = is_square(number)
    # Print result
    print_result(result)


def print_result(is_square):
    if is_square:
        print("This is a perfect square")
    else:
        print("This is not a square")

main()
