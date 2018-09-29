import random

while True:
	i=input("enter 'n' to quit")
	if(i=='n'):
		print("bye!")
		exit()

	else:	
		print("you got",random.randint(1,6))