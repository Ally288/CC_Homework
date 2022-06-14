import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("hearts", 1)
        self.card2 = Card("spades", 4)
        self.card3 = Card("diamonds", 5)
        self.card4 = Card("clubs", 9)

        self.cardgame1 = CardGame()

        self.all_cards = [self.card1, self.card2, self.card3, self.card4]

    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame1.check_for_ace(self.card1))

    def test_highest_card(self):
        self.card1, self.cardgame1.highest_card(self.card1, self.card3)

    def test_cards_total(self):
        self.assertEqual(
            "You have a total of 19", self.cardgame1.cards_total(self.all_cards)
        )
