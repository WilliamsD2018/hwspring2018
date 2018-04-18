import random

beginning = 1
end = 9
rollRange1 = (beginning,end)
rollRange2 = (beginning,end)
rollRange3 = (beginning, end)
score1 = 0
score2 = 0
score3 = 0
rollResult1 = rollRange1
rollResult2 = rollRange2
rollResult3 = rollRange3
Rutime = 2
def roll(beginning,end):
	return random.randint(beginning,end)

def roundWinner(rollResult1,rollResult2,rollResult3):
	if(rollResult1 > rollResult2 and rollResult1 > rollResult3):
		return "Player 1 Wins the Round"
	elif(rollResult2 > rollResult1 and rollResult2 > rollResult3):
		return "Player 2 Wins the Round"
	elif(rollResult3 > rollResult1 and rollResult3 > rollResult2):
		return "Player 3 Wins the Round"
	else:
		return "Tie and Re-roll"

def gameWinner(score1,score2,score3):
	if(score1 > score2 and score1 > score3):
		return "Player 1 Wins the Game"
	elif(score2 > score1 and score2 > score3):
		return "Player 2 Wins the Game"
	elif(score3 > score1 and score3 > score2):
		return "Plyer 3 Wins the Game"
	elif(score1 == score2):
		return "Tie Breaker"
	elif(score1 == score3):
		return "Tie Breakerr"
	elif(score2 == score3):
		return "Tie Breaker"
	else:
		return "Nobody Wins"

Runtime = 2

while(Runtime >= 0):
	rollResult1 = roll(beginning,end)
	rollResult2 = roll(beginning,end)
	rollResult3 = roll(beginning,end)
	rollWin = roundWinner(rollResult1,rollResult2,rollResult3)
	if(rollResult1 > rollResult2 and rollResult1 > rollResult3):
		score1 += 1
	if(rollResult2 > rollResult1 and rollResult1 > rollResult3):
		score2 += 1
	if(rollResult3 > rollResult2 and rollResult3 > rollResult1):
		score3 += 1
	gameWin = gameWinner(score1,score2,score3)
	if(gameWin != "Tie Breaker"):
		Runtime -= 1
	print(rollResult1,rollResult2,rollResult3,rollWin)

print(gameWin)
