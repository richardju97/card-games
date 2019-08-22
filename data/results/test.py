# test.py
# parse result files to ensure game results are correct and bots are correct

import os
import csv

def testBasic(playerScore, dealerScore, playerBusted, dealerBusted, gameResult, line_count):
    """test the basics of blackjack game win/lose. playerScore/dealerScore/line_count are integers, while the rest are strings"""
    testBust = lambda score: "True" if score > 21 else "False"
    print("player score: " + str(playerScore), ", test bust result: " + str(testBust(playerScore)), ", player busted: " + str(playerBusted))
    print("testBust == playerBusted ? " + str(testBust(playerScore) == playerBusted))
    assert playerBusted == testBust(playerScore), "playerBusted should be " + str(testBust(playerScore)) + " in line " + str(line_count)
    assert dealerBusted == testBust(dealerScore), "dealerBusted should be " + str(testBust(dealerScore)) + " in line " + str(line_count)

    testResult = lambda playerScore, dealerScore: "lose" if playerScore > 21 or (playerScore < dealerScore and dealerScore <= 21) \
                                                         else ("win" if playerScore > dealerScore else "tie")
    assert gameResult == testResult(playerScore, dealerScore), "game result should be " + testResult(playerScore, dealerScore) + " in line " + str(line_count)

def testBasicStrategyBot(file):
    """parses csv file for Basic Strategy Bot and checks if output of game is valid"""
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print("processing row: " + str(row))
            if line_count != 0 and len(row) > 0:
                dealerFirstCard = row[0]
                playerStartHand = row[1]
                dealerEndHand = row[2]
                playerEndHand = row[3]
                dealerBusted = row[4]
                playerBusted = row[5]
                gameResult = row[6]
                testBasic(int(playerEndHand), int(dealerEndHand), playerBusted, dealerBusted, gameResult, line_count)
            line_count += 1

for file in os.listdir(os.getcwd()):
    print(file)
    if file.split("_")[0] == "Basic":
        testBasicStrategyBot(file)
