# card.py

from random import randint

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
		temp = []
		while (len(self.deck) > 0):
			r = randint(0, len(self.deck) -1)	
			temp.append(self.deck[r])
			del self.deck[r]
		self.deck = temp
						
	def getnextcard(self):
		temp = self.deck[0]
		del self.deck[0]
		return temp

	def addcard(self, c):
		self.deck.append(c)	

	def __repr__(self):
		return "This is a deck of cards!"
