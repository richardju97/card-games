# sim.py

from blackjack import BlackJack
from card import Deck
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import random

MAX_SIMS = 1000
simbots = 10
simtype = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
assert (simbots == len(simtype)), "Declared number of bots must be equal to number of selected bots"

verbose = 0
numdecks = 4

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
    mydeck = Deck(numdecks)
    mydeck.shuffle()
    bjgame = BlackJack(1, mydeck)

    myplayers = []
    for i in range(0, simbots):
        myplayers.append(bjgame.newplayer("Simulation #" + str(simnum+1) + " Threshold=" + str(thresholds[i]),simtype[i], aux=thresholds[i]))

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
            decksize = numdecks*52 - len(myplayer.cards)
#            print("mydeck = " + str(len(mydeck)))
            adjust = 0

            for mycard in myplayer.cards:
                if (mycard.getnumber() >= ceiling):
                    adjust += 1

            if (ceiling >= 11):
                probability = 0
            else:
                probability = ((13 - ceiling + 1.0) * (4 * numdecks) - adjust) / decksize

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
            if (myplayer.getscore() <= 21):
                results[i].append(-1)
            else:
                results[i].append(-2)
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

rates = []
#for i in range(0, simbots):
#    results.append([])
print("-----------------------------")
print("Simulation Results")
for i in range(0, simbots):
    if (verbose):
        print("-----------------------------")
#    print("Bot Type: " + str(simtype[i]))
    if (verbose):
        print("Threshold=" + str(thresholds[i]))
        print("Games Played: " + str(MAX_SIMS))
    w = 0
    t = 0
    l = 0
    s = 0
    if (verbose):
        print(results[i])
    for j in range(0, len(results[i])):
        if (results[i][j] > 0):
            w += 1
            s += 1
        elif(results[i][j] == 0):
            t += 1
            s += 1
        else:
            l += 1
            if (results[i][j] == -1):
                s += 1
    winrate = (1.0 * w) / len(results[i])
    tierate = (1.0 * t) / len(results[i])
    lossrate = (1.0 * l) / len(results[i])
    survrate = (1.0 * s) / len(results[i])
    rates.append([winrate, tierate, lossrate, survrate])
#    lossratio = (1.0 * nloss / len(results[i]))
#    winrate = 1 - lossratio
    if (verbose):
        print("Win Rate: " + str(winrate * 100) + "%")
        print("Tie Rate: " + str(tierate * 100) + "%")
        print("Loss Rate: " + str(lossrate * 100) + "%")
        print("Survival Rate: " + str(survrate * 100) + "%")
        print("Total Score: " + str(sum[i]))
        if ((w + t) != 0):
            print("Average Score: " + str(1.0 * sum[i]/(w+t)))
        else:
            print("Average Score: N/A")
        print("-----------------------------")

for i in range(0, simbots):
    print(str(thresholds[i]) + ": " + str(rates[i]))

print("")
print("-----------------------------")
print("End Simulation")
print("-----------------------------")
print("")


### DATA VISUALIZATION ### 

rates = np.asarray(rates)

df = pd.DataFrame(rates, index=thresholds, columns=['winrate', 'tierate', 'lossrate', 'survrate'])
print(df)

#lines = df.plot.line()
winrateonly = plt.figure(1)
sns.lineplot(data=df.loc[:,['winrate']], marker = 'o')
plt.xticks(np.arange(0.1,1.1,step=0.1))

everything = plt.figure(2)
sns.lineplot(data=df)
plt.xticks(np.arange(0.1,1.1,step=0.1))
plt.show()



