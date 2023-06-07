#!/usr/bin/python3

class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

	
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
         


    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])


    def __lt__(self, other):
        '''
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        else:
            return self.rank < other.rank
        '''
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
'''
queen_of_diamonds = Card(1, 13)
queen1_of_diamonds = Card(1, 13)
print(queen1_of_diamonds < queen_of_diamonds)
'''
