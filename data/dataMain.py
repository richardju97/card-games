# dataMain.py

# set up type of bot
# run each game simulation
# write results to a csv file

import os, sys
sys.path.append("..")

import dataHelper as helper
from blackjack import BlackJack
from card import Deck

OUTPUT_FOLDER = os.path.abspath("/results")

NUM_SIMS = 1
simbots = 1 #number of bots in the name #TODO: should just be one bot
print("Select type of bot")
botType = int(input("1. Greedy AI \n2. Probability AI \n3. Perceptron \n4. Basic Strategy \n"))
botType = 4 #type of bot for each bot

for sim in range(NUM_SIMS):
    # initialize variables for csv file
    dealerFirstCard = 0
    playerStartHand = 0
    dealerEndHand = 0
    playerEndHand = 0
    dealerBusted = False
    playerBusted = False
    gameResult = "" # win/lose/tie

    # create Game and player and start
    mydeck = Deck()
    mydeck.shuffle()
    bjgame = BlackJack(1, mydeck, 0)
    player = bjgame.newplayer("Simulation #" + str(sim+1) + " Bot Type " + str(botType), botType)
    bjgame.start()

    dealerFirstCard = (lambda card: card.getnumber() if card.getnumber() < 10 else 10)(bjgame.getdealerfirstcard())
    playerStartHand = player.getscore()

    #play game
    helper.play(player, bjgame, dealerFirstCard)

    playerEndHand = player.getscore()
    dealerEndHand = bjgame.dealer.getscore()
    playerBusted, dealerBusted = helper.calcBusts(player, bjgame.dealer)
    gameResult = helper.getGameOutcome(player, bjgame)

    print("\n dealer first card: " + str(dealerFirstCard),
          "\n player start hand: " + str(playerStartHand),
          "\n dealer end hand: " + str(dealerEndHand),
          "\n player end hand: " + str(playerEndHand),
          "\n dealer busted: " + str(dealerBusted),
          "\n player busted: " + str(playerBusted),
          "\n game result: " + gameResult)


# verbose = 0
#
# simnum = 0
# nwins = 0
# nloss = 0
# nties = 0
# sum = []
# results = []
# # for i in range(0, simbots):
# #     results.append([])
# #     sum.append(0)
# # print(results)
#
# #Keeps track of all the dealer starting values
# dstart = []
#
# #Keeps track of all the dealer ending values
# dend = []
#
#
# #dictionary keeping track of the value of the card the dealer shows, keeps track of how many times it appears
# d1 = {
#     1 : 0,
#     2 : 0,
#     3 : 0,
#     4 : 0,
#     5 : 0,
#     6 : 0,
#     7 : 0,
#     8 : 0,
#     9 : 0,
#     10 : 0
# }
#
# #dictionary keeping track of the value of the card the dealer shows, keeps track of how many times the dealer busts with starting value of that card
# d2 = {
#     1 : 0,
#     2 : 0,
#     3 : 0,
#     4 : 0,
#     5 : 0,
#     6 : 0,
#     7 : 0,
#     8 : 0,
#     9 : 0,
#     10 : 0
# }
#
#
# for simnum in range(MAX_SIMS):
# #    print(simnum)
#     if (verbose):
#         print("")
#     mydeck = Deck()
#     mydeck.shuffle()
#     bjgame = BlackJack(1, mydeck, 0)
#
#     myplayers = []
#     for i in range(0, simbots):
#         myplayers.append(bjgame.newplayer("Simulation #" + str(simnum+1) + " Bot Type " + str(botType[i]),botType[i]))
#
#     bjgame.start()
#
# #    myscore = 0
#     i = 0
#     for myplayer in myplayers:
#         playing = True
#         while (playing):
#
#             if (verbose):
#                 print("Your current score is: " + str(myplayer.getscore()))
#                 for mycard in myplayer.cards:
#                     print(mycard)
#
# # edge case: what if player holds an ace and a small card
# # ceiling will be higher than it should because we can reduce the entire score by 10
#
#             ceiling = 22 - myplayer.getscore()
#             decksize = 52 - len(myplayer.cards)
#             adjust = 0
#
#             for mycard in myplayer.cards:
#                 if (mycard.getnumber() >= ceiling):
#                     adjust += 1
#
#             if (ceiling >= 11):
#                 probability = 0
#             else:
#                 probability = ((13 - ceiling + 1.0) * 4 - adjust) / decksize
#
#             if (verbose):
#                 print("Probability of losing: " + str(probability * 100) + "%")
#
#             if (verbose):
#                 print("Select an option:")
#     #        option = int(input("1. Stand \n2. Hit \n"))
#
#             option = myplayer.getMove(probability)
#
# #           option = random.randint(1, 3)
#             if (option == 1):
#                 bjgame.stand(myplayer)
#                 playing = False
#             elif (option == 2):
#                 bjgame.hit(myplayer)
#                 if (verbose):
#                     print("Updated Score: " + str(myplayer.getscore()))
#             else:
#                 if (verbose):
#                     print("Please select a valid option!")
#
#             if (myplayer.getscore() > 21):
#                 playing = False
#
#         if (verbose):
#             for mycard in myplayer.cards:
#                 print(mycard)
#         i += 1
#
#     dealerfirstcard = bjgame.getdealerfirstcard().getnumber()
#     if (dealerfirstcard > 10):
#         dealerfirstcard = 10
#     dstart.append(dealerfirstcard)
#     d1[dealerfirstcard] = d1[dealerfirstcard] + 1
#     dealerscore = bjgame.startdealer()
#     dend.append(dealerscore)
#     if (dealerscore > 21):
#         d2[dealerfirstcard] = d2[dealerfirstcard] + 1
#
# #        print(dealerscore)
#
#     i = 0
#     for myplayer in myplayers:
# #        if (myplayer.getscore() > 21):
# #            if (verbose):
# #                print("You lose")
# #            results[i].append(-1)
# #            nloss += 1
# #        else:
# #            if (verbose):
# #                print("Final Score: " + str(myplayer.getscore()))
# #            results[i].append(myplayer.getscore())
# #            nwins += 1
# #            sum[i] += myplayer.getscore()
#         r = bjgame.comparescores(myplayer.getscore())
#         if (r == -1):
#             if (verbose):
#                 print("You Lose")
#             results[i].append(-1)
#             nloss += 1
#         elif (r == 1):
#             if (verbose):
#                 print("Final Score: " + str(myplayer.getscore()))
#             results[i].append(myplayer.getscore())
#             nwins += 1
#             sum[i] += myplayer.getscore()
#         else:
#             if (verbose):
#                 print("Tie")
#             results[i].append(0)
#             nties += 1
#             sum[i] += myplayer.getscore()
#
#         if (verbose):
#             print("")
#
#         i += 1
#
# totalresults = 0
# for i in range(0, len(results)):
#     totalresults += len(results[i])
#
# if ((nwins + nloss + nties) != totalresults):
#     print("")
#     print("ERROR")
#     print("")
#
# print("-----------------------------")
# print("Simulation Results")
# for i in range(0, simbots):
#     print("-----------------------------")
#     print("Bot Type: " + str(botType[i]))
#     print("Games Played: " + str(MAX_SIMS))
#     w = 0
#     t = 0
#     l = 0
#     print(results[i])
#     for j in range(0, len(results[i])):
#         if (results[i][j] > 0):
#             w += 1
#         elif(results[i][j] == 0):
#             t += 1
#         else:
#             l += 1
#     winrate = (1.0 * w) / len(results[i])
#     tierate = (1.0 * t) / len(results[i])
#     lossrate = (1.0 * l) / len(results[i])
# #    lossratio = (1.0 * nloss / len(results[i]))
# #    winrate = 1 - lossratio
#     print("Win Rate: " + str(winrate * 100) + "%")
#     print("Tie Rate: " + str(tierate * 100) + "%")
#     print("Loss Rate: " + str(lossrate * 100) + "%")
#     print("Total Score: " + str(sum[i]))
#     if ((w + t) != 0):
#         print("Average Score: " + str(1.0 * sum[i]/(w+t)))
#     else:
#         print("Average Score: N/A")
#     print("-----------------------------")
#
#     print("Probability the dealer busts given first card value: ")
#
#     bustprobabilities = []
#     for key in d1.keys():
#         print(str(key) + ": " + str(d2[key]/d1[key]))
#         bustprobabilities.append(d2[key]/d1[key])
