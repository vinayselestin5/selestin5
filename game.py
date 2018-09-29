#snake and ladder
import random
count=0
#def my roll():
# return random.radaint(1,6)
while(count<=100):
	n=input(" press r to roll the dice :")
	if(n=='r'):
		r=random.randint(1,6)
		
		print("i got",r)
	

		if(count==8):
			count=37
			print("i got the ladder")
		elif(count==13):
			count=34
			print("i got the ladder")
		elif(count==40):
			count=68
			print("i got the ladder")
		elif(count==52):
			count=81
			print("i got the ladder")
		elif(count==76):
			count=97
			print("i got the ladder")
		elif(count==11):
			count=2
			print("sorry,u got a snake")
		elif(count==25):
			count=4
			print("sorry,u got a snake")
		elif(count==38):
			count=9
			print("sorry,u got a snake")
		elif(count==65):
			count46
			print("sorry,u got a snake")
		elif(count==89):
			count=70
			print("sorry,u got a snake")
		elif(count==93):
			count=64
			print("sorry,u got a snake")

		elif(count==100):
			print("you won the game")
			exit()
		elif(count==95 and r>5):
			print(" invalid input")	
		elif(count==96 and r>4):
			print(" invalid input")
		elif(count==97 and r>3):
			print(" invalid input")
		elif(count==98 and r>2):
			print(" invalid input")
		elif(count==99 and r>1):
			print(" invalid input")
		else:
			count=count+r
			print("new position is",count)
		


