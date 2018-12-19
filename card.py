# card.py

class Card:
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	def __init__(self, n, s):
		self.number = n
		self.suit = s

	#def __str__(self):



class Deck:

	def __init__(self):
		self.deck = []
		for suit in Card.suits:
			for i in range(1, 14):
				self.deck.append(Card(i, suit))
	def shuffle(self):
		

	def getnextcard(self):
		temp = self.deck[0]
		del self.deck[0]
		return temp

	def __repr__(self):
		return "This is a deck of cards!"
