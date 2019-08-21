#dataHelper.py

from blackjack import BlackJack
import os

verbose = 0

def csvName(bot, seed):
    """return the name for the csv report based on the bot and the seed value in card.py"""
    botsDictionary = {1: "Greedy", 2: "Probability", 3: "Perceptron", 4: "Basic"}
    return "".join([botsDictionary.get(bot), "_", str(seed), ".csv"])

def play(player, bjgame, dealerFirstCard):
    """play one blackjack game and return the player's end hand, and dealer's end hand"""
    #bot plays
    playing = True
    while (playing):
        # edge case: what if player holds an ace and a small card
        # ceiling will be higher than it should because we can reduce the entire score by 10
        ceiling = 22 - player.getscore()
        decksize = 52 - len(player.cards)
        adjust = 0

        for mycard in player.cards:
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

        option = player.getMove(probability, dealerFirstCard)
        if (option == 1):
            bjgame.stand(player)
            playing = False
        elif (option == 2):
            bjgame.hit(player)
            if (verbose):
                print("Updated Score: " + str(player.getscore()))
        else:
            if (verbose):
                print("Please select a valid option!")
        if (player.getscore() > 21):
            playing = False

    if (verbose):
        for mycard in player.cards:
            print(mycard)

    #dealer plays
    if (player.getscore() <= 21):
        bjgame.startdealer()

def calcBusts(player, dealer):
    """returns whether the player busted, whether the dealer busted"""
    playerBusted = False
    dealerBusted = False
    if player.getscore() > 21:
        playerBusted = True
    if dealer.getscore() > 21:
        dealerBusted = True
    return playerBusted, dealerBusted

def getGameOutcome(player, bjgame):
    """returns whether the game is a win, lose, or tie for the player"""
    playerScore = player.getscore()
    dealerScore = bjgame.dealer.getscore()
    if playerScore > 21:
        return "lose"
    elif dealerScore > 21 or playerScore > dealerScore:
        return "win"
    elif playerScore < dealerScore:
        return "lose"
    else:
        return "tie"
