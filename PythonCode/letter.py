
friends = ['alice', 'bob', 'charlie', 'dina', 'edgar']
letter = input('what letter?')
while len(letter) != 1:
    letter = input('no, what letter!')  # input validation loop


# second for of input validation
# priming assignment
# letter = 'abc'
# while len(letter) != 1:
#     letter = input('what letter?')


# print yes if the entered letter is in any of the names
# print no otherwise

is_found = False

for friend in friends:
    for letters in friend:
        if letters == letter:
            is_found = True
            break

if is_found:
    print('yes')
else:
    print('no')
