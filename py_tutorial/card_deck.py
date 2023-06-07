#!/usr/bin/python3

from card_class import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        cards = []
        for card in self.cards:
            cards.append(str(card))
        return '\n'.join(cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()


    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


'''
deck = Deck()
pop1 = deck.pop_card()
pop2 = deck.pop_card()
print(pop1, pop2)
deck.add_card(pop1)
deck.add_card(pop2)
deck.sort()
pop3 = deck.pop_card()
print(pop3)
'''
