#blackjack.py

from player import Player
from game import Game
from card import Deck
import time

class BlackJackPlayer(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        self.score = 0
        self.ghostcards = 0

    def getscore(self):
        return self.score

    def getMove(self, p):
        return int(input("1. Stand \n2. Hit \n"))

class GreedyBlackJackPlayer(BlackJackPlayer):

    # Stand = 1
    # Hit = 2
    def getMove(self, p):
        time.sleep(2)
        if (self.getscore() < 21):
            return 2 # Always hit if under 21
        else:
            return 1 # Stand if greater than 21? (the game will be over by then)

class ProbabilityThresholdBlackJackPlayer(BlackJackPlayer):
    
    threshold = 0.8 # Probability threshold : if probability of losing > threshold, stand 

    # Stand = 1
    # Hit = 2
    def getMove(self, p):
        time.sleep(2)
        if (p > self.threshold):
            return 1 # probability of losing is too great
        else:
            return 2 # probability of losing is less than threshold

class PerceptronBlackJackPlayer(BlackJackPlayer): 

    threshold =  0.5 # threshold. Max value = 2 if weights are all 1

    # Weights
    score_weight = 0.8 # Score is on a scale of 0 - 1
    probability_weight = 0.2 # Probability of losing is on a scale of 0 - 1


    # Stand = 1
    # Hit = 2
    def getMove(self, p):
        time.sleep(2)
        # Current activiation function is basic threshold function
        if (self.getscore() /  21 * score_weight + p * probability_weight > self.threshold):
            return 1 # probability of losing is too great
        else:
            return 2 # probability of losing is less than threshold

class Dealer(BlackJackPlayer):

    def __init__(self, name):
        BlackJackPlayer.__init__(self, name)

    # Stand = 1
    # Hit = 2
    def getMove(self, p):
        time.sleep(2)

        #Dealer's turn
        if(self.getscore() >= 17):
            return 1
        else:
            return 2





class BlackJack(Game):

    def __init__(self, n, d):
        Game.__init__(self, num_players=n, deck=d)
        self.dealer = Dealer("Dealer") #initializes a dealer for every game.
        for i in range(2): #Adds two cards to dealer's hands
            self.dealer.addtohand(self.deck.getnextcard())


    # type parameter: 0 = blackjack player , 1 = greedy blackjack player, 2 = probability threshold player, 
    # 3 = perceptron, 4 = Dealer
    def newplayer(self, name, type=0):
        self.num_players += 1

        if (type == 0):
            #print("Normal player initialized!")
            temp = BlackJackPlayer(name)
        elif (type == 1):
            #print("Greedy AI Initialized!")
            temp = GreedyBlackJackPlayer(name)
        elif (type == 2):
            temp = ProbabilityThresholdBlackJackPlayer(name)
        elif (type == 3):
            temp = PerceptronBlackJackPlayer(name)

        self.players.append(temp)
        return temp


    # Returns true if the dealer does not have a natural 21 else false if the dealer has a natural 21
    def start(self):
        for p in self.players:
            print("Welcome to BlackJack, " + p.name + "!")
        print("******** GAME START ********")
        self.deal(2)
        self.calcallscores()
        self.calcscores(self.dealer)
        # Shows the first card of the dealer's hand
        print("The first card in the dealer's hand is: " + str(self.dealer.gethand()[0]))
        # If the dealer has a natural 21
        if (self.dealer.getscore() == 21):
            print("The dealer has a natural 21! Players must also have a natural 21 to tie!")
            return False
        
        return True


    def startdealer(self):
        print("***************************")
        print("The dealer's full hand was: ")
        for card in self.dealer.gethand():
            print(card)
        print("Dealer score: " + str(self.dealer.getscore()))
        
        playing = True
        while(playing): # Dealer plays 
            option = self.dealer.getMove(0)
            if (option == 1):
                self.stand(self.dealer)
                playing = False
            elif (option == 2):
                self.hit(self.dealer)
                print("Dealer hits!")
                print("---------------------------")
                print("Updated Score: " + str(self.dealer.getscore()))
            else:
                print("Please select a valid option!")

        return self.dealer.getscore()


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

