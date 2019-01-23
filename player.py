class Player:

    def __init__(self, name, cards=None):
        self.name = name
        self.cards = cards

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
    
    def gethand(self, can_see_cards=False):
        if can_see_cards:
            return self.cards
        return "Access denied"
