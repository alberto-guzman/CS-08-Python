# 1 find avg grade
# 2 print student with highest grade
# 3 sort by name
# 4 sort by grade


gradebook = [['Charlier', 80], ['Greg', 95], ['Fiona', 100]]
print(gradebook)


# find average
avg = (gradebook[0][1] + gradebook[1][1] + gradebook[2][1]) / 3
print(avg)


# print student with highest grade


# sort by name


# prof solution


# function
def print_grades(book):
    print ('Name', 'Grade', sep='\t')
    for row in book:
        print(row[0], row[1], sep='\t')

print_grades(gradebook)


def average_grade(book):
    total = 0
    sutdent = len(book)
    for row in book:
        total += row[1]
    return total / len(book)


def max_grade(book):
    max_grade = 0
    for row in book:
        if row[1] > max_grade:
            max_grade = row[1]
    students = []
    for row in book:
        if row[1] == max_grade:
            students.append(row[0])
    return students


def sorted_by_grade(book):
    new_book = []
    grades = []
    for row in book:
        grades.append(row[1])  # list of all the grades
    grade.sort()
    grades.reverse()
    for grade in grades:
        for row in book:
            if row[1] == grade:
                new_book.append(row)
    return new_book


def main():
    print('Average:')
    print(average_grade(gradebook))
    print("Highest:")
    print(max_grade(gradebook))
    gradebook.sort()  # this will sort by the first element
    print(gradebook)

main()
