# Card_Game_War
#There is a deck of cards that is shuffled and spilt into 2 decks
#Each player gets a deck and then starts the game.
#To play each player shows the first card of their deck
#the player with the highest card wins the round
#Ace is the lowest card (acts like a 1) but if it is shown against a King then it is played like a 14
#The winner gets both cards into his final deck
#If a tie both players lose their cards into a Tie Dump Deck
#When one player is out of cards or the player does not want to play any more the game ends
#The player with the most card in their final's deck is declared the winner

#imports
import random
#Set Deck of cards AKA Main Deck
main_deck = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH']

#Randomize Main Deck
random.shuffle(main_deck)

#Declare players decks before hand
player1_deck = []
player2_deck = []

#Separate Main deck into Player's decks
while len(main_deck) !=0:
    player1_deck.append(main_deck[0])
    main_deck.remove(main_deck[0])
    player2_deck.append(main_deck[0])
    main_deck.remove(main_deck[0])

#Stating game rules
print "Hello!"
print "There is a deck of cards that is shuffled and spilt into 2 decks"
print "Each player gets a deck and then starts the game."
print "To play each player shows the first card of their deck"
print "the player with the highest card wins the round"
print "Ace is the lowest card (acts like a 1) but if it is shown agenst a King then it is played like a 14"
print "The winner gets both cards into his final deck"
print "If a tie both players lose their cards into a Tie Dump Deck"
print "When one player is out of cards or the player does not want to play any more the game ends"
print "The player with the most card in their final's deck is declared the winner"
print " "

#Declare Game Variables
player_continue_loop = 'YES' #For Unless the player wants to end early
player1_card_value = 0 #Value of cards when fighting
player2_card_value = 0
player1_final_deck = [] #Decks to show what each player has in the end
player2_final_deck = []
tie_dump = [] #For Cards that both players lose
number_of_turns = 0 #Turn counter

#Asking if you want to play
print "Do you want to start?"
player_continue_loop = raw_input("Yes or No?")
print " "

#Game While loop Begins
while len(player1_deck) != 0 and len(player2_deck) != 0 and player_continue_loop != 'no' and player_continue_loop != 'No':

#Prints the stats of the game
    print "Turn: " + str(number_of_turns)
    print "Your Card: "+ player1_deck[0]
    print "Your Cards Left: "+str(len(player1_deck))
    print "Your cards won: "+str(len(player1_final_deck))
    print " "
    print "CPU  Card: "+ player2_deck[0]
    print "CPU  Cards Left: "+str(len(player2_deck))
    print "CPU  cards won: "+str(len(player2_final_deck))
    print " "

#IF STATMENTS MAKING THE RULES TO SEE THE VALUE OF PLAYERS CARD
    if len(player1_deck) != 0:
        if player1_deck[0][0] == 'A' and player2_deck[0][0] == 'K':
             player1_card_value = 14
        elif player1_deck[0][0] == 'A' and player2_deck[0][0] != 'K':
            player1_card_value = 1
        elif player1_deck[0][0] == 'T':
            player1_card_value = 10
        elif player1_deck[0][0] == 'J':
            player1_card_value = 11
        elif player1_deck[0][0] == 'Q':
            player1_card_value = 12
        elif player1_deck[0][0] == 'K':
            player1_card_value = 13
        else:
            player1_card_value = int(player1_deck[0][0])
    if len(player2_deck) != 0:
        if player2_deck[0][0] == 'A' and player1_deck[0][0] == 'K':
             player2_card_value = 14
        elif player2_deck[0][0] == 'A' and player1_deck[0][0] != 'K':
            player2_card_value = 1
        elif player2_deck[0][0] == 'T':
            player2_card_value = 10
        elif player2_deck[0][0] == 'J':
            player2_card_value = 11
        elif player2_deck[0][0] == 'Q':
            player2_card_value = 12
        elif player2_deck[0][0] == 'K':
            player2_card_value = 13
        else:
            player2_card_value = int(player2_deck[0][0])

#IF STATMENTS TO SEE WHOS CARD IS MORE VALUABLE AND CALLING THE WINNER OF THE ROUND
    if player1_card_value > player2_card_value:
        player1_final_deck.append(player2_deck[0])
        player2_deck.remove(player2_deck[0])
        player1_final_deck.append(player1_deck[0])
        player1_deck.remove(player1_deck[0])
        print "You are the winner of the round!"
    if player1_card_value < player2_card_value:
        player2_final_deck.append(player1_deck[0])
        player1_deck.remove(player1_deck[0])
        player2_final_deck.append(player2_deck[0])
        player2_deck.remove(player2_deck[0])
        print "CPU is the winner of the round!"
    if player1_card_value == player2_card_value:
        tie_dump.append(player1_deck[0])
        tie_dump.append(player2_deck[0])
        player1_deck.remove(player1_deck[0])
        player2_deck.remove(player2_deck[0])
        print "It is a Tie! Both lose!"

#Turn keeper
    number_of_turns = number_of_turns +1
#Asking if you would like to keep playing
    print "Would you like to continue the game?"
    player_continue_loop = raw_input("Yes or No?")
    print " "

#End Game While Loop

#If Statments Declaring the Winner
if len(player1_final_deck) > len(player2_final_deck):
    print "YOU HAVE WON!!!!"
    print "Your cards won: " + str(len(player1_final_deck))
    print "CPU  cards won: " + str(len(player2_final_deck))
    print "Tie Dump pile: " + str(len(tie_dump))
if len(player1_final_deck) < len(player2_final_deck):
    print "CPU HAS WON!!!!"
    print "Your cards won: " + str(len(player1_final_deck))
    print "CPU  cards won: " + str(len(player2_final_deck))
    print "Tie Dump pile: " + str(len(tie_dump))
if len(player1_final_deck)  ==  len(player2_final_deck):
    print "IT\'S A TIE!!!!"
    print "Your cards won: " + str(len(player1_final_deck))
    print "CPU  cards won: " + str(len(player2_final_deck))
    print "Tie Dump pile: " + str(len(tie_dump))
