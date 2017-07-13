def main():
    # ask for name
    global name
    name = input('What is your name?')
    # set account to 1000
    account = 1000
    bet = 25
    bet = input_bet(bet, account)
    # while loop
    while account != 0:
        account += play_hand(account)
        print(name, 'has $', account)
        if account <= 0:
            print('You have no more $')
            break
        if input_bet(bet, account) == 0:
            break
        else:
            account += play_hand(account)
            print(name, 'has $', account)

# play_hand function


def play_hand(account):

    # initialize to 0
    player_points = 0
    dealer_points = 0

    deck = new_deck()
    shuffle_deck(deck)
    # shuffle_deck(deck)

    dealer_card = string_of_card(deck[1])
    dealer_points += value_of_card(dealer_card)
    print('Dealer received card of value', dealer_card)

    player_card = string_of_card(deck[2])
    player_points += value_of_card(player_card)
    print('Player received card of value', player_card)

    player_card = string_of_card(deck[3])
    player_points += value_of_card(player_card)
    print('Player received card of value', player_card)

    print('Dealer total:', dealer_points)
    print(name, 'total:', player_points)

    while player_points < 21:
        p_move = input('Move? (hit/stay)')
        if p_move == 'hit':
            player_card = string_of_card(deck[4])
            player_points += value_of_card(player_card)
            print('Player received card of value', player_card)
            print('Dealer total:', dealer_points)
            print(name, 'total:', player_points)
        else:
            break

    dealer_card = string_of_card(deck[5])
    dealer_points += value_of_card(dealer_card)
    print('Dealer received card of value', dealer_card)
    print('Dealer total:', dealer_points)
    print(name, 'total:', player_points)

    if player_points > 21:
        print('Dealer wins')
        return -25
    else:
        while player_points < 21 and dealer_points < 17:
            dealer_card = string_of_card(deck[6])
            dealer_points += value_of_card(dealer_card)
            print('Dealer received card of value', dealer_card)
            print('Dealer total:', dealer_points)
            print(name, 'total:', player_points)
        # time to decide who wins
        if player_points < 21:
            print(name, 'bust')
            return -25
        if player_points < 21 and dealer_points > 21:
            print('Dealer bust')
            return 25
        if player_points <= 21 and player_points > dealer_points:
            print(name, 'wins')
            return 25
        if dealer_points <= 21 and dealer_points > player_points:
            print('Dealer wins')
            return -25
        if dealer_points == player_points:
            print('Tie')
            return 0


# input_bet function
def input_bet(bet_amount, account):
    while True:
        bet = input('How much do you want to bet? (0 to quit, Enter to stay at previous bet)$' + str(bet_amount))
        # check if the amount is valid
        if bet == '':
            print("#####")
            return bet_amount
        try:
            bet = int(bet)
        except:
            print('You have to type in a valid number')
            pass  # this will prompt you to go back to the while loop
        else:
            if bet == 0:
                return 0
            if bet < 0:
                print('You need to type a positive integer')
            elif bet > account:
                print('You dont have enough money!')
            else:
                return bet


def new_deck():
    suit = ['\u2660', '\u2661', '\u2662', '\u2663']
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = [(i, j) for j in num for i in suit]
    return deck


def shuffle_deck(deck):
    import random
    random.shuffle(deck)


def value_of_card(card):
    point_list = [(1, 11), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 10), (12, 10), (13, 10)]
    for i in point_list:
        if card[1] == str(i[0]):
            return int(i[1])


def string_of_hand(hand):
    for i in hand:
        hand += string_of_card(i)
    return hand


def value_of_hand(hand):
    for i in hand:
        hand += value_of_card(i)
    return hand


############################
# coded this but was not able to intergrate.....
############################

def string_of_card(card):
    card = list(card)
    card[1] = str(card[1])
    card = ''.join(card)
    return card


def save(name, money):
    file = open('blackjack.save.txt', 'w+')
    file.write(str(name) + '\n')
    file.write(str(money) + '\n')
    file.close()


def restore():
    file = open('blackjack.save.txt', 'r')
    name = file.readline()
    name = name.rstrip('\n')
    name = str(name)
    money = file.readline()
    money = money.rstrip('\n')
    money = int(money)
    return name, money

# call to main
main()
