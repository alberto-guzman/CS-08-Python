class Card:
    def __init__(self):  # this means its private
        self.__rank = 1  # makes it private
        self.__suit = '\u2660'

    def as_string(self):  # public
        return self.__rank_string() + self.__suit

    def __rank_string(self):  # client cant change the rank of the object,private
        if self.__rank == 1:
            return 'A'
        elif self.__rank == 11:
            return 'J'
        elif self.__rank == 12:
            return 'Q'
        elif self.__rank == 13:
            return 'K'
        else:
            return str(self.__rank)


# modified

class Card:
    def __init__(self, rank='A', suit='spade'):  # this means its private, two attributes of the card
        if rank == 'A':
            self.__rank = 1
        elif rank == 'J':
            self.__rank = 11
        elif rank == 'Q':
            self.__rank = 12
        elif rank == 'K':
            self.__rank = 13
        else:
            self.__rank = int(rank)
        self.__rank = 1  # makes it private
        self.__suit = '\u2660'

    def __str__(self):  # public, if you need to convert it into a string do this
        return self.__rank_string() + self.__suit

    def __rank_string(self):  # client cant change the rank of the object,private
        if self.__rank == 1:
            return 'A'
        elif self.__rank == 11:
            return 'J'
        elif self.__rank == 12:
            return 'Q'
        elif self.__rank == 13:
            return 'K'
        else:
            try:
                return str(self.__rank)  # if you give me anything other than an int i will return an error and initialize it as a 1
            except ValueError:
                self.__rank = 1
        if self.__rank < 1 or self.__rank > 13:  # outside the range it will initiaze as 1, deals with the invariance
            self.__rank = 1
        self.__suit = suit


# interactive

import card
from card import Card  # import the class called Card

a_card = Card()
print(a_card.as_string())

a_card.__rank = 10  # cant modify the private attribute


#interactive witht he seond once

import card
from card import Card

Card('A')

print(Card('A'))


a_card - Card() #give me a card
print(a_card)
