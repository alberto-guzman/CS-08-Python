import prime
import random


def large_prime(keysize=16):
    num = -1
    while not prime.is_prime(num):
        num = random.randrange(2**(keysize - 1), 2**(keysize))
    return num


def main():
    k = int(input('Bit Size? '))
    print(large_prime())

main()
