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

class BlackJackPlayer(Player):

    def __init__(self):
        self.score = 0

class BlackJack(Game):

    def __init__(self, n, d):
        Game.__init__(self, num_players=n, deck=d)

    def addplayer(self, p)
        self.num_players += 1
        self.players.append(p)
    
    def start(self):
        self.deal(2)

#    def turn(self, player):
    def hit(self, player):
        player.addtohand(self.deck.getnextcard())
        calcscores(player)

    def calcscores(self, player):
        
        player.gethand().sort(key=lambda Card: Card.number, reverse=True)
        
        tempscore = 0
        for card in player.gethand():
            temp = card.getnumber()
            
            if (temp == 1):
            
            elif (temp >= 10):
                temp = 10
            
            tempscore += temp
        
        self.score = tempscore

    def calcallscores(self):
        for p in self.players:
            calcscores(p)

#    def end(self):

