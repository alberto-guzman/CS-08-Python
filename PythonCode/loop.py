# do you have any friend named bob

# name = 'bob'

# number = int(input('how many friends?'))

# for friend in range(number):
#     this_friend = input('Name?')
#     if this_friend == name:
#         print('you have a friend named bob')


# sentinel value
# ask user over and over again until they no longer want to enter and its the end of the sequence

# priming input

name = 'bob'
sentinel = ''
this_friend = input('Name1?')

while this_friend != sentinel:  # if they type the sentinel it should stop
    if this_friend == name:
        print('you have a friend named bob')
    else:
        print('thats not bob')
    this_friend = input('Name2?')
