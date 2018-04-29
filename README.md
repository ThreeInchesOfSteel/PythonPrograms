# PythonPrograms

Just a dump of the basic stuff I've made in Python

## Rock Paper Scissors

Currently:
- Takes in player input, generates AI input, compares and declares a winner
- Keeps track of the players current score
    
Possible improvements:
- Check player input is valid

## Hangman

Currently:
- Generates random word from preset list and creates a blank version
- Asks player for letter, checks if letter appears in word
- Replaces blank spaces with letter if correct, reduces lives by 1 if wrong
- Tracks previously guessed letters to stop player guessing same guess twice

Possible improvements:
- Generate a random word from another file
- Handle multiple words/phrases, e.g. "Iron Man" would be "---- ---"
- Print list of previously guessed letters after every guess
- MORE COMMENT LINES

## Fixtures Generator

Currently:
- Uses preset list of football teams (to generate list of fixtures so that every team plays each other twice, home and away)
- Generates fixtures in the form "Team A v Team B" for every team, then repeats for reverse fixtures "Team B v Team A"
- Randomises the order of the fixtures and prints them on separate lines

Possible improvements:
- Take a list of teams from a file, of potentially any length
- Structure fixtures into "rounds", where each team plays in a round only once
- Structure fixtures so that teams cannot play home/away in 3 consecutive rounds
- Structure fixtures so that teams from same cities/other criteria cannot all play at home in same round
- MORE COMMENT LINES

## Deck Of Cards

Currently:
- Defines individual playing cards and a deck of all 52 cards
- Two classes: One defining a single card, and one defining a deck
- Shuffles the full deck into a random order

Possible improvements:
- Implement into actual card games (Blackjack, Poker, etc)

## Blackjack

Currently:
- Uses DeckOfCards program to run a game of Blackjack
- User plays against the AI (the dealer)
- Aces are worth 11 points

Possible improvements:
- Allow for Aces to be worth **either** 1 or 11 points
