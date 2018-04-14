import random

words = ["BEAUTIFUL", "CHRISTMAS", "AUSTRALIA", "POLLUTION", "PINEAPPLE", "ADJECTIVE", "IRREGULAR", "SOMETHING", "DANGEROUS", "CHRISTIAN", "CHALLENGE", "HAPPINESS", "WEDNESDAY", "SECRETARY", "MASCULINE", "CONSONANT"]
answer = random.choice(words)
listanswer = [x for x in answer]
blankanswer = ["-" for letter in answer]
guessedletters = []

found = False

lives = 5
while lives > 0:
	found = False
	playerguess = raw_input("Guess a letter: ").upper()
	while playerguess in guessedletters:
		playerguess = input("Guess another letter you idiot").upper()
	guessedletters.append(playerguess)
	
	for idx, char in enumerate(answer):
		if playerguess == char:
			found = True
			blankanswer[idx] = playerguess
	
	if found == True:
		print("Correct! \n" + " ".join(blankanswer))
	else:
		lives -= 1
		print("Nope, not there. You have " + str(lives) + " lives remaining. \n" + " ".join(blankanswer))
	
	if blankanswer == listanswer:
		print("Congratulations! A winner is you!")
		break

if blankanswer != listanswer:
	print("You lose! Good day sir!")
