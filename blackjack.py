#blackjack.py

from player import Player
from game import Game
from card import Deck

class BlackJackPlayer(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        self.score = 0
        self.ghostcards = 0

    def getscore(self):
        return self.score

class BlackJack(Game):

    def __init__(self, n, d):
        Game.__init__(self, num_players=n, deck=d)

    def newplayer(self, name):
        self.num_players += 1
        temp = BlackJackPlayer(name)
        self.players.append(temp)
        print("Welcome to BlackJack, " + name + "!")
        return temp
    
    def start(self):
        self.deal(2)
        self.calcallscores()

#    def turn(self, player):
    def stand(self, player):
        self.calcscores(player)

    def hit(self, player):
        player.addtohand(self.deck.getnextcard())
        self.calcscores(player)

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
        
        player.score = tempscore

    def calcallscores(self):
        for p in self.players:
            self.calcscores(p)

#    def end(self):

