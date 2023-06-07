#!/usr/bin/python3
from card_deck import Deck

class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.lable = label


hand = Hand()
deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)
