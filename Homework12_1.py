"""Колода карт"""


import random


class Card:
    """A class to represent all the available cards in a Card Deck"""

    number_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "J", "Q", "K", "A"]
    mast_list = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, number=None, mast=None):
        self.number = number
        self.mast = mast

    def __str__(self):
        if self.number is None and self.mast is None:
            return "Joker"
        return f"{self.mast} {self.number}"


class CardsDeck:
    """A class to represent a Card Deck, from which the player draws a card"""
    def __init__(self, with_jokers=True):
        self.deck = []
        for number in Card.number_list:
            for mast in Card.mast_list:
                self.deck.append(Card(number, mast))
        if with_jokers:
            self.deck.append(Card())

    def shuffle(self):
        """Method for shuffling cards"""
        random.shuffle(self.deck)

    def get_card(self, card_index):
        """Method for taking a card from a deck by its number"""
        if 0 <= card_index < len(self.deck):
            return self.deck.pop(card_index)
        return "Неверный номер карты!"


deck = CardsDeck()
deck.shuffle()

card_number = int(input('Выберите карту из колоды в 54 карты (от 0 до 53): '))
card = deck.get_card(card_number)
print(f'Ваша карта: {card}')
