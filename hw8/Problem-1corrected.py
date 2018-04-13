import random

def roll(beginning, end):
	return random.randint(beginning, end)







def RoundWinner(score1, score2):
	if(score1 > 1):
		return "player1"
	elif(score2 > 1):
		return "player2"
	else:
		return "tie"


def GameWinner(rollresult1, rollresult2):
	if(rollresult1 > rollresult2):
		return "Plyer 1 is the Winner"
	elif(rollresult2 > rollresult1):
		return "Player 2 is the winner"
	else:
		return "Nobody Wins"


beginning = 1
end = 6
score1=0
score2=0
rollresult1=0
rollresult2=0
range1=(beginning, end)
range2=(beginning, end)
Runtime = 2





while(Runtime):
	score1 = roll(beginning, end)
	score2 = roll(beginning, end)
	RollWinner = RoundWinner(rollresult1, rollresult2)
	if(score1 > score2):
		rollresult1 +=1
	elif(score2 > score1):
		rollresult2 += 1
	Runtime -=1
	print(score1,score2,RollWinner)

	Winner = GameWinner(rollresult1,rollresult2)

	print(GameWinner)
