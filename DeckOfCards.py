#Need this to shuffle the deck
import random

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
		

        
card1 = Card(12, "Spades") #Tests a single card, and reveals it, prints the value, then the suit
card1.reveal()
print(card1.value)
print(card1.suit)

deck1 = Deck() #Tests a new deck, prints the entire deck (ordered), shuffles it, then prints it again (randomised)
deck1.revealDeck()
deck1.shuffle()
deck1.revealDeck()
