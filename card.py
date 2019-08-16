# card.py

from random import seed
from random import randint

seed(324)

class Card:
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	def __init__(self, n, s):
		self.number = n
		self.suit = s

	def getnumber(self):
		return self.number

	def __str__(self):
		val = self.number
		if self.number == 1:
			val = "Ace"
		elif self.number == 11:
			val = "Jack"
		elif self.number == 12:
			val = "Queen"
		elif self.number == 13:
			val = "King"
		return str(val) + " of " + self.suit

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
	
	def notempty(self):
		if(len(self.deck) > 0):
			return True
		else:
			return False
	
#    def notempty(self):
#        if(len(self.deck) > 0):
#            return True
#        else
#            return False

#    def notempty(self):
#        if (len(self.deck) > 0):
#            return True
#        else:
#            return False
