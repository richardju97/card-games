#blackjack.py

from player import Player
from game import Game
from card import Deck

class BlackJackPlayer(Player):

    def __init__(self):
        self.score = 0

class BlackJack(Game):

    def __init__(self, n, d):
        Game.__init__(self, num_players=n, deck=d)

    def newplayer(self, name):
        self.num_players += 1
        self.players.append(BlackJackPlayer(name))
    
    def start(self):
        self.deal(2)

#    def turn(self, player):
    def hit(self, player):
        player.addtohand(self.deck.getnextcard())
        calcscores(player)

    def calcscores(self, player):
        
        hand = player.gethand()
        hand.sort(key=lambda Card: Card.number, reverse=True)
        
        tempscore = 0
        for i in range(0, len(hand)):
            temp = hand[i].getnumber()
            
            if (temp == 1):
                if(i == len(hand)-1):
                    if(tempscore + 11 <= 21):
                        temp = 11
#                else:
#                    temp = 1
            elif (temp >= 10):
                temp = 10
            
            tempscore += temp
        
        self.score = tempscore

    def calcallscores(self):
        for p in self.players:
            calcscores(p)

#    def end(self):

