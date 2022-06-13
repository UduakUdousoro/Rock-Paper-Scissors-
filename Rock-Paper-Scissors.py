import random 

print("Welcome\n Here are the rules of the Game:")
print("\n Rock wins Sissors.\n Sissors wins Paper.\n Paper wins Rock.\n")
print("R = rock.\nS = sissors.\nP = paper")


def rockPaperScissors():
	choices = ["R","P","S"]
	player = input("Choose an option: R, S, P\n").upper()
	while player not in choices:
		print("Invalid Option")
		player= input("Choose an option: R, S, P\n").upper()
	computer = random.choice(choices)
	RPSdict ={"R":"Rock", "P":"Paper", "S":"Scissors"}
	print ("You chose: ", player, "comuputer chose: ", computer)
	print ("User(" + RPSdict[player] + ") : CPU(" + RPSdict[computer] + ")")
	if player == computer:
		print("It's a tie. we go again")
		return(rockPaperScissors())
	if player == "R" and computer== "S":
		print("player WINS! ")
	if player == "S" and computer== "R":
		print("computer WINS! ")
	if player == "P" and computer== "R":
		print("player WINS! ")
	if player == "R" and computer== "P":
		print("computer WINS! ")
	if player == "S" and computer== "P":
		print("player WINS! ")
	if player == "P" and computer== "S":
		print("computer WINS! ")

rockPaperScissors()