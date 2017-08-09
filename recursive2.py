def sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum(lst[1:])


# now to reverse it


def sum(lst):
    if len(lst) <= 1:
        return lst
    else:
        return reverse(lst[1:]) + lst[:1]


# find sub problem
lst = [1, 15, 2.5, 7, 10, 100]


# divide and conquer approache, recursion
# more efficient runtime

# reverse the two halfs

def dcreverse(lst):
        if len(lst) <= 1:
        return lst
    else:
        mid = len(lst)//2
        left = dcreverse(lst[:mid])
        right = dcreverse(lst[mid:])
        return right+left


# palindrome example

def is_pal(st):
    if     :
        return
    else:
        lst[:-1] == lst[]
        return

