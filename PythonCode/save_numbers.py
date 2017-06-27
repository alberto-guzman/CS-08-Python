def main():
    number = input("What number? ")
    num_file = open('numbers.txt', 'w')
    while number != '':
        number = int(number)
        num_file.write(str(number) + '\n')
        number = input("What number? ")
    num_file.close()

main()


#os.chdir('/Users/albertoguzman-alvarez/Desktop/CS 08 Python/PythonCode')
