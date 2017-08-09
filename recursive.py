#write recursive method to print a triangle
#argument will be the top row pyramid



# def stars(num):
#     if num < 0:
#         return 'x'*num
#     else:
#         return ''


# print(stars(5))


# def triangle(num):
#     if num > 0:
#         print(num * '*')
#     else:
#         return''

# print(triangle(5))


# def fibonacci(num):
#     if num == 1:
#         return [1]
#     elif num ==2:
#         return[1,1]
#     elif num>2:
#         smaller - fibonacci(num-1)
#         smaller.append(smaller[-2]+smaller[-1])
#         return smaller

# print(fibonacci(int(input())))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
