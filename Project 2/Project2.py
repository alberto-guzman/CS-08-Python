def main():
    # ask for name
    name = input('What is your name?')
    return name
    # set account to 1000
    account = 1000
    play_again = 'y'
    # while loop
    while account != 0:
        play_hand()
        account += play_hand(account)
        if account <= 0:
            print('You have no more $')
            break
        else:
            play_again = input('Do you want to play another hand y/n?')
    while play_again == 'y':
        play_hand()
        account += play_hand()


# play_hand function


def play_hand():
    import random

    # initialize to 0
    player_points = 0
    dealer_points = 0

    dealer_card = random.randint(1, 13)
    dealer_points += dealer_card
    print('Dealer received card of value', dealer_card)

    player_card = random.randint(1, 13)
    player_points += player_card
    print('Player received card of value', player_card)

    player_card = random.randint(1, 13)
    player_points += player_card
    print('Player received card of value', player_card)

    print('Dealer total:', dealer_points)
    print(name, 'total:', player_points)

    while player_points < 21:
        p_move = input('Move? (hit/stay')
        if p_move == 'h':
            player_card = random.randint(1, 13)
            player_points += player_card
            print('Player received card of value', player_card)
            print('Dealer total:', dealer_points)
            print(name, 'total:', player_points)
        else:
            break

    dealer_card = random.randint(1, 13)
    dealer_points += dealer_card
    print('Dealer received card of value', dealer_card)
    print('Dealer total:', dealer_points)
    print(name, 'total:', player_points)

    if player_points > 21:
        print('Dealer wins')
        account -= 25
        print(name, 'has $', account)
    else:
        while player_points < 21 and dealer_points < 17:
            dealer_card = random.randint(1, 13)
            dealer_points += dealer_card
            print('Dealer received card of value', dealer_card)
            print('Dealer total:', dealer_points)
            print(name, 'total:' + player_points)
        # time to decide who wins
        if player_points < 21:
            print(name, 'bust')
            account -= 25
            print(name, 'has $', account)
        if player_points < 21 and dealer_points > 21:
            print('Dealer bust')
            account += 25
            print(name + 'has $' + account)
        if player_points <= 21 and player_points > dealer_points:
            print(name, 'wins')
            account += 25
            print(name, 'has $', account)
        if dealer_points <= 21 and dealer_points > player_points:
            print('Dealer wins')
            account -= 25
            print(name, 'has $', account)


# call main function
main()


# activity 2 logic

# def input_bet(bet,money):
#     while True:
#         bet_amount = input(?)
#         #check if the amount is valid
#         if bet_amount == '':
#             return bet
#         try:
#             bet_amount == int(bet_amount)
#         except:
#             print('you have to type in a vlid number')
#             pass # this will prompt you to go back to the while loop


# #before
# def main():
#     name
#     bet = 25
#     play_again=y
#         while play again == y
#             money += play_hand(name)
#             if money <= 0
#                 break

#         play_again?
