choice = float(raw_input("Would you like to enter a entire game(1) or  play by play(2):  "))

if(choice == 2):
	print("Good")
if(choice == 1):
	print("Enter your entire game separated by a coma")
	game = []
	score = (raw_input("what was your score in the last games"))
	game.append(score)

	print(game)

	print("The result of your game is")
	print(game,sum(game))
