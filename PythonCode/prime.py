# wirte is_prime(num) that
# determines if num is prime


# bring bills code in


def is_prime(num):
    result = True
    if num < 2:
        result = False
    if divides(2, num):
        result = False
    for i in range(3, num, 2):
        if divides(i, num):
            result = False
    return result  # this makes it if it goes trhough and doesnt find one


def divides(a, b):
    return (b % a == 0)  # this will return a true or a false
