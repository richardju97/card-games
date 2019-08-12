# play.py

from blackjack import BlackJack
from card import Deck

mydeck = Deck()
mydeck.shuffle()

#Player initialization
bjgame = BlackJack(2, mydeck)
name = input("What is your name? ") #Prompts the user for a name
myplayer = bjgame.newplayer(name, 0)

#AI initialization
print("What type of AI would you like to play against? ") # Select AI type
ai_type = int(input("1. Greedy AI \n2. Probability AI \n3. Perceptron \n"))
ai = bjgame.newplayer("AI", ai_type)

players = [myplayer, ai]

bjgame.start()


############## PLAYER PHASE ################
# Goes through each turn for each of the players (PLAYER PHASE)
for p in players:

    playing = True

    while (playing):

        print("---------------------------")
        print(p.name + ", your current score is: " + str(p.getscore()))
        print("---------------------------")
        for mycard in p.cards:
            print(mycard)
        print("---------------------------")

    # edge case: what if player holds an ace and a small card
    # ceiling will be higher than it should because we can reduce the entire score by 10    

        ceiling = 22 - p.getscore()
        decksize = 52 - len(p.cards)
        adjust = 0

        for mycard in p.cards:
            if (mycard.getnumber() >= ceiling):
                adjust += 1

        if (ceiling >= 11):
            probability = 0
        else:
            probability = ((13 - ceiling + 1.0) * 4 - adjust) / decksize

        print("Probability of losing: " + str(probability * 100) + "%")

        #("Select an option:")
        option = p.getMove(probability)
    #    print(option)

        if (option == 1):
            bjgame.stand(p)
            playing = False
        elif (option == 2):
            bjgame.hit(p)
            print("Updated Score: " + str(p.getscore()))
        else:
            print("Please select a valid option!")
        
        if (p.getscore() >= 21):
            playing = False

    for mycard in p.cards:
        print(mycard)

    if (p.getscore() > 21):
        print("You lose!")
    elif (p.getscore() == 21):
        print("Congrats, " + p.name + " you win!")
    else:
        print("Final Score: " + str(p.getscore()))

    print("***************************")

print("Final Scores: \n")
for p in players:
    print(p.name + " " + str(p.getscore()))
    if (p.getscore() > 21):
        players.remove(p) #Removes all the players that are out of the game because they have a score > 21

########### DEALER PHASE ############
bjgame.startdealer()
playing = True

while(playing): # Dealer plays 
    option = bjgame.dealer.getMove(0)
    if (option == 1):
        bjgame.stand(bjgame.dealer)
        playing = False
    elif (option == 2):
        bjgame.hit(bjgame.dealer)
        print("Updated Score: " + str(bjgame.dealer.getscore()))
    else:
        print("Please select a valid option!")

print("***************************")
for mycard in bjgame.dealer.cards:
    print(mycard)
print("Final Score:")
print(str(bjgame.dealer.getscore()))

if (bjgame.dealer.getscore() == 21): #If the dealer ends up with a 21
    print("The dealer wins!")
elif (bjgame.dealer.getscore() > 21): # If dealer ends up with a score greater than 21
    print("The dealer busts!")
    for p in players:
        print("Congrats, " + p.name + " you win!")
else:                                #If the dealer ends up with a score less than 21 and greater than 17
    for p in players:
        if (p.getscore() > bjgame.dealer.getscore()):
            print("Congrats, " + p.name + " you win! " + str(p.getscore()) + " is greater than " +
                str(bjgame.dealer.getscore()))
        elif (p.getscore() == bjgame.dealer.getscore()):
            print(p.name + " you have tied with the dealer!")
        else:
            print(p.name + " you lose! Your score of " + str(p.getscore()) + " is less than " + str(bjgame.dealer.getscore()))




