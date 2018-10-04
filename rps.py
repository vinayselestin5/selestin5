#dictionary
import random
a={1:'r',2:'p',3:'s'}
while(True):
	c=a[random.randint(1,3)]
	user_input=input("enter rock papaer scissor")
	print("computer puts ",c)
	#condition
	if(user_input=='r'and c=='s' or user_input=='p' and c=='r'or user_input=='p' and c=='r' ):
		print ("you won")

	else:
		print("computer loses")
	t=input("PRINT Q TO EXIT")
	if(t=='q'):
		exit()
