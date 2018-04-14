#Need this to generate AI choice
import random

#Three possible options
choices = ["R", "P", "S"]
#Used to determine when to end the game
playing = True
#Used to make a running tally of results
wins = 0
draws = 0
losses = 0

#Runs until the player decides to stop
while playing == True:
	
	#Asks player for their choice and picks a random choice for the AI from the choices list
	player_choice = raw_input("Make your choice [R/P/S]: ").upper()
	ai_choice = random.choice(choices)
	
	#Checks if its a tie
	if player_choice == ai_choice:
		print("Tie game!")
		draws += 1
	#Checks if the player has won	
	elif (player_choice == "R" and ai_choice == "S") or (player_choice == "P" and ai_choice == "R") or (player_choice == "S" and ai_choice == "P"):
		print("You're winner!")
		wins += 1
	#Otherwise the player has lost	
	else:
		print("You lose! Good day sir!")
		losses += 1
	#Asks if they want to continue	
	playon = raw_input("Would you like to play again? [Y/N]: ").upper()
	#If not then displays their record
	if playon == "N":
		playing = False
		record = [wins, draws, losses]
		print("Your record was {} wins, {} draws and {} losses".format(str(record[0]),str(record[1]),str(record[2])))
