# test.py
# parse result files to ensure game results are correct and bots are correct

import os
import csv

def testGameBasic(playerScore, dealerScore, playerBusted, dealerBusted, gameResult, line_count):
    """test the basics of blackjack game win/lose. playerScore/dealerScore/line_count are integers, while the rest are strings"""
    testBust = lambda score: True if score > 21 else False
    assert playerBusted == testBust(playerScore), "playerBusted should be " + str(testBust(playerScore)) + " in line " + str(line_count)
    assert dealerBusted == testBust(dealerScore), "dealerBusted should be " + str(testBust(dealerScore)) + " in line " + str(line_count)
    testResult = lambda playerScore, dealerScore: "lose" if playerBusted or (playerScore < dealerScore and not dealerBusted) \
                                                         else ("win" if playerScore > dealerScore or dealerBusted else "tie")
    assert gameResult == testResult(playerScore, dealerScore), "game result should be " + testResult(playerScore, dealerScore) + " in line " + str(line_count)

def testBasicStrategyBot(file):
    """parses csv file for Basic Strategy Bot and checks if output of game is valid"""
    toBool = lambda str: True if str == "True" else False
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print("processing row: " + str(row))
            if line_count != 0 and len(row) > 0:
                dealerFirstCard = int(row[0])
                playerStartHand = int(row[1])
                dealerEndHand = int(row[2])
                playerEndHand = int(row[3])
                dealerBusted = toBool(row[4])
                playerBusted = toBool(row[5])
                gameResult = row[6]
                testGameBasic(playerEndHand, dealerEndHand, playerBusted, dealerBusted, gameResult, line_count)
                if dealerFirstCard >= 7:
                    assert playerEndHand >= 17, "player end hand should be >= 17, because dealer start card is " + str(dealerFirstCard)
                elif 4 <= dealerFirstCard <= 6:
                    assert playerEndHand >= 12, "player end hand should be >= 12, because dealer start card is " + str(dealerFirstCard)
                elif 1 <= dealerFirstCard <= 2:
                    assert playerEndHand >= 13, "player end hand should be >= 13, because dealer start card is " + str(dealerFirstCard)
            line_count += 1

for file in os.listdir(os.getcwd()):
    print(file)
    if file.split("_")[0] == "Basic":
        testBasicStrategyBot(file)
