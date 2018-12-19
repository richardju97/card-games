# card.py

class Card:
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	def __init__(self, n, s):
		self.number = n
		self.suit = s

	def __str__(self):
		val = self.number
		if self.number == 1:
			val = "Ace"
		if self.number == 11:
			val = "Jack"
		if self.number == 12:
			val = "Queen"
		if self.number == 13:
			val = "King"
		return str(val) + " of " + self.suit


class Deck:

	def __init__(self):
		self.deck = []
		for suit in Card.suits:
			for i in range(1, 14):
				self.deck.append(Card(i, suit))

	def __repr__(self):
		return "This is a deck of cards!"

	def shuffle(self):
