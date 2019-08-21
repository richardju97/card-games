# dataMain.py

# set up type of bot
# run each game simulation
# write results to a csv file

import os, sys
import csv
sys.path.append("..")

import dataHelper as helper
from blackjack import BlackJack
from card import Deck

OUTPUT_FOLDER = os.path.join(os.getcwd(), "results")

NUM_SIMS = 100
simbots = 1 #number of bots in the name #TODO: should just be one bot
print("Select type of bot")
botType = int(input("1. Greedy AI \n2. Probability AI \n3. Perceptron \n4. Basic Strategy \n"))
botType = 4 #type of bot for each bot

report = open(os.path.join(OUTPUT_FOLDER, "sample.csv"), "a+")
report_writer = csv.writer(report)
report_writer.writerow(["Dealer First Card", "Player Start Hand", "Dealer End Hand", "Player End Hand", "Dealer Busted", "Player Busted", "Game Result"])

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
    report_writer.writerow([dealerFirstCard, playerStartHand, dealerEndHand, playerEndHand, dealerBusted, playerBusted, gameResult])

report.close()
