import random
user1 = 0
user2 = 0

def Round_winner(
while user1 < 2 and user2 < 2:
	turn1 = random.randint(1,6)
	turn2 = random.randint(1,6)
	if turn1 > turn2:
		print("user 1 is the winner of the round")
		user1 += 1
		print(turn1)
	elif turn2 > turn1:
		print("user 2 is the winner of the round")
		user2 +=1
		print(turn2)
	elif turn1 == turn2:
		print("Draw")

print("Result")
print(user1, user2)
if user1 > user2:
	print("user1 wins")
elif(user2 > user1):
	print("user2 wins")
