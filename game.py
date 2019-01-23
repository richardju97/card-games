# game.py

from card import Deck

class Game:
    
    def __init__(self, num_players=1, deck=Deck()):
        self.num_players = num_players
        self.deck = deck
        self.players = []
    #        def addplayers(self, names):
    #            """add a player object to self.players for each name in list names"""
    #            for player in range(self.num_players):
    #                self.player.append(Player(names[player]))
    #        addplayers()
    
    def deal(self, num):
        """removes and returns a card from the deck"""
        if (num == 0):
            while (self.deck.notempty()):
                for p in self.players:
                    temp = self.deck.getnextcard()
                    p.addtohand(temp)
        else:
            for i in range(0, num):
                for p in self.players:
                    temp = self.deck.getnextcard()
                    p.addtohand(temp)
#        return self.deck.getnextcard()
