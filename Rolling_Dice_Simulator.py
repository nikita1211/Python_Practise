#Rolling dice Simulator

import random

def dice_roll():
	print ("Rolling the dice...And the number is ")
	print (random.randint(1, 6))

while True:
	choice = int(input("Do you want to roll the Dice (1/0)"))
	if choice==1:
		dice_roll()
	else:
		break	
	
