# play.py

from blackjack import BlackJack
from card import Deck

mydeck = Deck()
mydeck.shuffle()

#Player initialization
bjgame = BlackJack(2, mydeck)
name = input("What is your name? ") #Prompts the user for a name
myplayer = bjgame.newplayer(name, 0)

#AI initialization
print("What type of AI would you like to play against? ") # Select AI type
ai_type = int(input("1. Greedy AI \n2. Probability AI \n3. Perceptron \n"))
ai = bjgame.newplayer("AI", ai_type)

players = [myplayer, ai]

nonatural = bjgame.start() #checks to see if the dealer has a natural 21 at the start of the game

if (nonatural):

    ############## PLAYER PHASE ################
    for p in players:

        playing = True

        #edge case: the player starts with a natural 21
        if (p.getscore() == 21):
            print("Wow! " + p.name + " got a natural 21! Your turn will now end. ")
            playing = False

        while (playing):

            print("---------------------------")
            print(p.name + ", your current score is: " + str(p.getscore()))
            print("---------------------------")
            for mycard in p.cards:
                print(mycard)
            print("---------------------------")

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
            print("You lose! You are now out of the game!")
        elif (p.getscore() == 21):
            print("Congrats, " + p.name + " you got to 21!")
        else:
            print("Final Score: " + str(p.getscore()))

        print("***************************")

    ########### DEALER PHASE ############
    dealerscore = bjgame.startdealer()


    ########### PRINT DEALER'S FINAL CARDS ############

    print("***************************")
    print("Dealer's Final cards: ")
    for mycard in bjgame.dealer.cards:
        print(mycard)
    print("Dealer's Final Score:")
    print(str(dealerscore))


    ########### FINAL COMPARISON BETWEEN DEALER'S SCORE AND PLAYER'S SCORE ##########

    if (dealerscore == 21): #If the dealer ends up with a 21
        for p in players:
            if (bjgame.comparescores(p.getscore()) == 0):
                print(p.name + ", you tied with the dealer with a score of 21!")
            elif (bjgame.comparescores(p.getscore()) == -1):
                print(p.name + ", you lose! Your score of " + str(p.getscore()) + " is less than 21.")

    elif (dealerscore > 21): # If dealer ends up with a score greater than 21
        print("The dealer busts!")
        for p in players:
            if (p.getscore() <= 21):
                print("Congrats, " + p.name + " you win!")
    else:   #If the dealer ends up with a score less than 21 and greater than 17
        for p in players:
            if (p.getscore() <= 21):
                if (bjgame.comparescores(p.getscore()) == 1):
                    print("Congrats, " + p.name + " you win! " + str(p.getscore()) + " is greater than " +
                        str(dealerscore))
                elif (bjgame.comparescores(p.getscore()) == 0):
                    print(p.name + " you have tied with the dealer!")
                else:
                    print(p.name + " you lose! Your score of " + str(p.getscore()) + " is less than " + str(dealerscore))
            else:
                print(p.name + ", you lose! Your score is greater than 21.") 
    print("GAME END.")

######## IF DEALER HAS A NATURAL 21 ###########
else: #IF the dealer has a natural 21, check to see if other players have natural 21
    for p in players:
        if (p.getscore() == 21):
            print("Wow! " + p.name + " also got a natural 21! You tie with the dealer! ")
        else:
            print("You lose! " + p.name + " did not have a natural 21. ")
    print("GAME END.")

  




