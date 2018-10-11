
#dictionary
a=['1','2','3','4','5','6','7','8','9']

def print_board():
	print(a[0],a[1],a[2])
	print("---------")
	print(a[3],a[4],a[5])
	print("---------")
	print(a[6],a[7],a[8])

playerOverTurn = True
while True:
	print_board()
	p=input("chose an available place :")

	if(p in a):
		if(a[int(p)-1]=='x' or a[int(p)-1]=='O'):
			print("Place taken,choose another place...")
			continue

		else: 
			if playerOverTurn:
				print("player 1 >>")
				a[int(p)-1] = 'x'
				playerOverTurn = not playerOverTurn
			else:
				print("player 2 >>")
				a[int(p)-1] = 'O'
				playerOverTurn = not playerOverTurn
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("game over")
					exit()
				for i in range(3):
					if(a[i]==a[i+3] and a[i]==a[6]):
						print("gave over")
						exit()
#checking for diagonal (form left to right)
	if (a[0]==a[4] and a[0]==a[8]):
		print("game is over")
		if(a[4]=='X'):
			print("congratulations to player 1")
		else:
			print("congratulations to player 2")
		print_board()
		exit()

#checking for diagonal (form right to left)
	if (a[2]==a[4] and a[2]==a[6]):
		print("game is over")
		if(a[4]=='X'):
			print("congratulations to player 1")
		else:
			print("congratulations to player 2")
		print_board()
		exit()
	else:
		print("you entered invalid position")
		continue