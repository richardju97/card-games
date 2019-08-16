# sim.py

from blackjack import BlackJack
from card import Deck

import random

MAX_SIMS = 100
simbots = 2
simtype = [1, 2]
assert (simbots == len(simtype)), "Declared number of bots must be equal to number of selected bots"

verbose = 1

simnum = 0
nwins = 0
nloss = 0
nties = 0
sum = []
results = []
for i in range(0, simbots):
    results.append([])
    sum.append(0)
print(results)

for simnum in range(MAX_SIMS):
#    print(simnum)
    if (verbose):
        print("")
    mydeck = Deck()
    mydeck.shuffle()
    bjgame = BlackJack(1, mydeck)

    myplayers = []
    for i in range(0, simbots):
        myplayers.append(bjgame.newplayer("Simulation #" + str(simnum+1) + " Bot Type " + str(simtype[i]),simtype[i]))

    bjgame.start()

#    myscore = 0
    i = 0
    for myplayer in myplayers:
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

#           option = random.randint(1, 3)
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
        i += 1

    dealerscore = bjgame.startdealer()
#        print(dealerscore)
    i = 0
    for myplayer in myplayers:
#        if (myplayer.getscore() > 21):
#            if (verbose):
#                print("You lose")
#            results[i].append(-1)
#            nloss += 1
#        else:
#            if (verbose):
#                print("Final Score: " + str(myplayer.getscore()))
#            results[i].append(myplayer.getscore())
#            nwins += 1
#            sum[i] += myplayer.getscore()
        r = bjgame.comparescores(myplayer.getscore())
        if (r == -1):
            if (verbose):
                print("You Lose")
            results[i].append(-1)
            nloss += 1
        elif (r == 1):
            if (verbose):
                print("Final Score: " + str(myplayer.getscore()))
            results[i].append(myplayer.getscore())
            nwins += 1
            sum[i] += myplayer.getscore()
        else:
            if (verbose):
                print("Tie")
            results[i].append(0)
            nties += 1
            sum[i] += myplayer.getscore()

        if (verbose):
            print("")

        i += 1

totalresults = 0
for i in range(0, len(results)):
    totalresults += len(results[i])

if ((nwins + nloss + nties) != totalresults):
    print("")
    print("ERROR")
    print("")

print("-----------------------------")
print("Simulation Results")
for i in range(0, simbots):
    print("-----------------------------")
    print("Bot Type: " + str(simtype[i]))
    print("Games Played: " + str(MAX_SIMS))
    w = 0
    t = 0
    l = 0
    print(results[i])
    for j in range(0, len(results[i])):
        if (results[i][j] > 0):
            w += 1
        elif(results[i][j] == 0):
            t += 1
        else:
            l += 1
    winrate = (1.0 * w) / len(results[i])
    tierate = (1.0 * t) / len(results[i])
    lossrate = (1.0 * l) / len(results[i])
#    lossratio = (1.0 * nloss / len(results[i]))
#    winrate = 1 - lossratio
    print("Win Rate: " + str(winrate * 100) + "%")
    print("Tie Rate: " + str(tierate * 100) + "%")
    print("Loss Rate: " + str(lossrate * 100) + "%")
    print("Total Score: " + str(sum[i]))
    if ((w + t) != 0):
        print("Average Score: " + str(1.0 * sum[i]/(w+t)))
    else:
        print("Average Score: N/A")
    print("-----------------------------")
      
print("")
print("-----------------------------")
print("End Simulation")
print("-----------------------------")
print("")


