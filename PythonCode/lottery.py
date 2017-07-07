# generate lottery numbers
# write function lottery() that
# accepts parameters max(highest legal numberts) and count (# of numbers)
# returns a tuple of the numbers
# note: duplicates are not allowed


# def lottery(m, c):
#     my_list = [0, 0]
#     import random
#     m = int(m)
#     c = int(c)
#     for i in range[i, c]
#         my_list.append = random.int(1, m)
#     my_tup = tuple(my_list)
#     print(my_tup)


# lottery(4, 7)


# prof solution


def lottery(max=60, count=5):
    import random
    lottery_list = [''] * count  # this will make a list with c empty strings
    # print(lottery_list)
    for i in range(count):
        number = random.randint(1, max)
        while number in lottery_list:
            number = random.randint(1, max)
        lottery_list[i] = number
    return tuple(lottery_list)


def main():
    print(lottery(max=69, count=6))


main()
