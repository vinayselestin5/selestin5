import random

while True:
	i=input("press 'r' to roll the dice'q' to quit!")
	if(i=='q'):
		print("bye!")
		exit()

	else:	
		print("you got",random.randint(1,6))