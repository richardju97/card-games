class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return self.name + "\nCards: " + self.cards

    def draw(self, deck):
        self.cards.append(deck.getnextcard())

    def play(self, card=None):
        if card:
            return card
        return self.cards.pop()

    def addtohand(self, card):
        self.cards.append(card)
    
    def gethand(self):
#        if can_see_cards:
        return self.cards
#        return "Access denied"
    
    def getMove(self):
        return int(input("1. Stand \n2. Hit \n"))
