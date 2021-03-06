#Need this to shuffle the deck
import random
#Need this to slow down text
import time

#Class defining a single Card, with a value (1-13) and a suit
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    #Prints the name of the card, and changes it's name if its a face card
    def reveal(self):
        facecards = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if self.value in facecards:
            valname = facecards[self.value]
        else:
            valname = self.value
        print(("{} of {}").format(valname, self.suit))
        
#Class defining a deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    #Populates the empty list of cards with every possible card
    def build(self):
        for a in range(1,14):
            for b in ["Clubs", "Diamonds","Hearts","Spades"]:
                self.cards.append(Card(a,b))
    
    #Reveals each card in the deck using reveal method in Card class (IS THIS EVEN NEEDED?)
    def revealDeck(self):
        for i in self.cards:
            i.reveal()

    #Shuffles the deck (Uses Fisher-Yates algorithm)
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    #Draws the last card from the deck (should be shuffled first to ensure card is random)
    def draw(self):
        return self.cards.pop()

def evaluator(hand):
    '''Determines the value of a hand
	if hand contains Aces, runs the aces_eval function'''

    points = num_of_aces = 0
    for a in range(0,len(hand)):
        if hand[a].value in [11,12,13]:
            points += 10
        elif hand[a].value == 1:
            num_of_aces += 1
        else:
            points += hand[a].value
    if num_of_aces == 0:
        return points
    else:
        return aces_eval(points, num_of_aces)
    
def aces_eval(points, num_of_aces):
    '''Determines possible hand values if hand contains Aces'''
    
    max = 0
    possible_pts = []
	#Adds each possible hand value to list
    for b in range(0, num_of_aces+1):
        possible_pts.append(points + num_of_aces + b*10)
    
	#Looks for the highest possible value under 22
    for c in possible_pts:
        if c < 22 and c > max:
            max = c
    
	#If none of the possible values are under 22, sets the max = 22 to trigger bust
    if max == 0:
        max = 22
    
    return max

#Asks player if they want to play before entering game loop
play = False
print("Welcome to Blackjack!")
playgame = raw_input("Would you like to play a game? [Y/N] ").upper()
if playgame == "Y":
    play = True

while play == True:
    #Inner loop to run through game, so when broken, the endgame code is always run on the outer loop
    while True:
    
        newdeck = Deck()
        newdeck.shuffle()
        
        #Draws 2 cards for the player and the dealer
        playerhand = []
        for a in range(0,2):
            newcard = newdeck.draw()
            playerhand.append(newcard)
                
        dealerhand = []
        for a in range(0,2):
            newcard = newdeck.draw()
            dealerhand.append(newcard)
            
        #Determines the value of each hand and assigns it to playerpts/dealerpts
        playerpts = evaluator(playerhand)
        dealerpts = evaluator(dealerhand)
        
        #Checks if either player has Blackjack, and if so, ends the game
        if playerpts == 21:
            print("Blackjack! You win!")
            break
        
        if dealerpts == 21:
            print("Dealer has Blackjack. You lose.")
            break
            
        #Reveals one of the dealer's cards
        print("The dealer has:\nX")
        time.sleep(1)
        dealerhand[0].reveal()  
            
        #While the player has a valid hand and hasn't chosen to stick
        while playerpts < 22:
        
            print("You have:")
            for a in range(0,len(playerhand)):
                time.sleep(1)
                playerhand[a].reveal()
            
            #Asks if they want to Stick or Twist. If Twist, new card is drawn and added to player's hand
            sticktwist = raw_input("Would you like to Stick or Twist? [S/T] ").upper()
            if sticktwist == "S":
                break
            elif sticktwist == "T":
                newcard = newdeck.draw()
                playerhand.append(newcard)
                print("You have drawn:")
                time.sleep(1)
                newcard.reveal()
            
            #Checks if player has bust and declares them a loser if so
            playerpts = evaluator(playerhand)
            if playerpts > 21:
                print("You're bust! You lose.")
         
        #Checks again if player has bust to allow it to break the loop if so
        if playerpts > 21:
            break
        
        #Now that the player's turns are over, both the dealer's cards are revealed
        print("The dealer has:")
        for a in range(0,len(dealerhand)):
            time.sleep(1)
            dealerhand[a].reveal()
        
        #If the dealer has less than 17 points, they must draw a card. Otherwise they Stick
        while dealerpts < 17:
        
            newcard = newdeck.draw()
            dealerhand.append(newcard)
            time.sleep(1)
            newcard.reveal()
            dealerpts = evaluator(dealerhand)
         
        #Checks if dealer has now bust, and breaks the loop if so
        if dealerpts > 21:
            print("Dealer is bust! You win!")
            break
        
        #If neither player or dealer has bust by now, a final comparison of scores to determine the winner, and ends the inner loop
        if playerpts > dealerpts:
            print("You win!")
        elif playerpts < dealerpts:
            print("You lose.")
        else:
            print("Tie game!")
        break
    
    #Reveals player's and dealer's final hands
    time.sleep(1)
    print("You had: ")
    time.sleep(1)
    for a in range(0,len(playerhand)):
        playerhand[a].reveal()
    time.sleep(1)
    print("The dealer had:")
    time.sleep(1)
    for a in range(0,len(dealerhand)):
        dealerhand[a].reveal()
    
    #Asks player for another game. If not, then outer loop ends and the game ends
    time.sleep(1)
    playagain = raw_input("Would you like to play again? [Y/N] ").upper()
    if playagain == "N":
        print("Goodbye!")
        play = False
    
