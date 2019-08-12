# sim.py

from blackjack import BlackJack
from card import Deck

import random

MAX_SIMS = 3
simtype = "Test"

verbose = 1

simnum = 0
nwins = 0
nloss = 0
sum = 0
results = []

for simnum in range(MAX_SIMS):
#    print(simnum)
    if (verbose):
        print("")
    mydeck = Deck()
    mydeck.shuffle()
    bjgame = BlackJack(1, mydeck)
    myplayer = bjgame.newplayer("Test Simulation #" + str(simnum + 1),1)
    bjgame.start()

    myscore = 0
    
    playing = True
    while (playing):

        if (verbose):
            print("Your current score is: " + str(myplayer.getscore()))
            for mycard in myplayer.cards:
                print(mycard)

# edge case: what if player holds an ace and a small card
# ceiling will be higher than it should because we can reduce the entire score by 10    

        ceiling = 22 - myplayer.getscore()
        decksize = 52 - len(myplayer.cards)
        adjust = 0

        for mycard in myplayer.cards:
            if (mycard.getnumber() >= ceiling):
                adjust += 1

        if (ceiling >= 11):
            probability = 0
        else:
            probability = ((13 - ceiling + 1.0) * 4 - adjust) / decksize

        if (verbose):
            print("Probability of losing: " + str(probability * 100) + "%")

        if (verbose):
            print("Select an option:")
#        option = int(input("1. Stand \n2. Hit \n"))

        option = myplayer.getMove(probability)

#        option = random.randint(1, 3)
        if (option == 1):
            bjgame.stand(myplayer)
            playing = False
        elif (option == 2):
            bjgame.hit(myplayer)
            if (verbose):
                print("Updated Score: " + str(myplayer.getscore()))
        else:
            if (verbose):
                print("Please select a valid option!")

        if (myplayer.getscore() > 21):
            playing = False

    if (verbose):
        for mycard in myplayer.cards:
            print(mycard)

    bjgame.startdealer()

    if (myplayer.getscore() > 21):
        if (verbose):
            print("You lose")
        results.append(-1)
        nloss += 1
    else:
        if (verbose):
            print("Final Score: " + str(myplayer.getscore()))
        results.append(myplayer.getscore())
        nwins += 1
        sum += myplayer.getscore()

    if (verbose):
        print("")

if (nwins + nloss != len(results)):
    print("")
    print("ERROR")
    print("")

print("-----------------------------")
print("Simulation Results")
print("-----------------------------")
print("Simulation Type: " + simtype)
print("Games Played: " + str(MAX_SIMS))
lossratio = (1.0 * nloss / len(results))
winrate = 1 - lossratio
print("Win Rate: " + str(winrate * 100) + "%")
print("Total Score: " + str(sum))
print("Average Score: " + str(1.0 * sum/nwins))
print("-----------------------------")
      
print("")
print("-----------------------------")
print("End Simulation")
print("-----------------------------")
print("")


