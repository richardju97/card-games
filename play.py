# play.py

from blackjack import BlackJack
from card import Deck

mydeck = Deck()
mydeck.shuffle()
bjgame = BlackJack(2, mydeck)
name = input("What is your name? ") #Prompts the user for a name
myplayer = bjgame.newplayer(name, 0)

print("What type of AI would you like to play against? ") # Select AI type
ai_type = int(input("1. Greedy AI \n2. Probability AI \n3. Perceptron \n"))
ai_name = input("What is the name of your AI?")
ai = bjgame.newplayer(ai_name, ai_type)

players = [myplayer, ai]

bjgame.start()

for p in players:
    playing = True
    while (playing):

        print(p.name + ", your current score is: " + str(p.getscore()))
        for mycard in p.cards:
            print(mycard)

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
        print("You lose")
    elif (p.getscore() == 21):
        print("Congrats, " + p.name + " you win!")
        break
    else:
        print("Final Score: " + str(p.getscore()))

print("Final Scores: \n")
for p in players:
    print(p.name + " " + str(p.getscore()))
 
