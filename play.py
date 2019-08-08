# play.py

from blackjack import BlackJack
from card import Deck

mydeck = Deck()
mydeck.shuffle()
bjgame = BlackJack(1, mydeck)
name = input("What is your name? ") #Prompts the user for a name
myplayer = bjgame.newplayer(name)
bjgame.start()

playing = True
while (playing):

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

    print("Probability of losing: " + str(probability * 100) + "%")

    print("Select an option:")
    option = myplayer.getMove(probability)
#    print(option)

    if (option == 1):
        bjgame.stand(myplayer)
        playing = False
    elif (option == 2):
        bjgame.hit(myplayer)
        print("Updated Score: " + str(myplayer.getscore()))
    else:
        print("Please select a valid option!")
    
    if (myplayer.getscore() >= 21):
        playing = False

for mycard in myplayer.cards:
    print(mycard)

if (myplayer.getscore() > 21):
    print("You lose")
elif (myplayer.getscore() == 21):
    print("Congrats, you win!")
else:
    print("Final Score: " + str(myplayer.getscore()))
