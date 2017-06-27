# def main():
#     try:
#         num = int(input('Number:'))
#     except ValueError as err:
#         print(err)
#     else:
#         print("Nice number")
#     finally:
#         print("done")

# main()


def main():
    success = False
    while not success:
        try:
            num = int(input('Number:'))
        except ValueError as err:
            print(err)
        else:
            print("Nice number")
        finally:
            print("done")

main()
