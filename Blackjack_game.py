class Game:
    
    def __init__(self, num_players=1, deck=Deck()):
        self.num_players = num_players
        self.deck = deck
        self.players = []
        def addplayers(self, names):
            """add a player object to self.players for each name in list names"""
            for player in range(self.num_players):
                self.player.append(Player(names[player]))
        addplayers()

    def deal(self, deck):
        """removes and returns a card from the deck"""
        return deck.getnextcard()

class BlackJack(Game):
