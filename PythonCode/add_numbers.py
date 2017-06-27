def main():
    numbers_file = open('numbers.txt', 'r')
    num = numbers_file.readline()
    total = 0
    while num != ' ':
        num = num.rstrip('\n')
        num = int(num)
        total += num
        num = numbers_file.readline()
    numbers_file.close()
    print(total)

main()

#os.chdir('/Users/albertoguzman-alvarez/Desktop/CS 08 Python/PythonCode')
