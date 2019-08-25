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
                dealerFirstCard = row[0]
                playerStartHand = row[1]
                dealerEndHand = row[2]
                playerEndHand = row[3]
                dealerBusted = row[4]
                playerBusted = row[5]
                gameResult = row[6]
                testGameBasic(int(playerEndHand), int(dealerEndHand), toBool(playerBusted), toBool(dealerBusted), gameResult, line_count)
            line_count += 1

for file in os.listdir(os.getcwd()):
    print(file)
    if file.split("_")[0] == "Basic":
        testBasicStrategyBot(file)
