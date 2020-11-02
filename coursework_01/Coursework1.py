# Spellchecker 

import os, os.path
from os import path

print("\nHello, " + os.getlogin() +"\nWelcome to the Spellchecker! \n")

ok = 1     #variable used to control the while loop
while ok == 1:
	choice = input("What would you like to do? \nPress the number of the action you want to pursue: \n  1. Spell check a sentence. \n  2. Spell check a file. \n  To quit press 0.\n")

	if choice == "1":
		sentence = input(" Please enter the sentence you want to spellcheck: ")
		words = sentence.split(" ")
		ok = 0

	elif choice == "2":
		ok1 = 1			# another variable used for controlling the while loop 
		while ok1 == 1:
			file_name = input("Please enter the complete filename: ")
			exist = str(os.path.isfile(file_name))
			if exist == "False":
				choice1 = int(input("\nThe file you selected does not exist. \nPress the number of the action you want to pursue next: \n 1. Enter the filename again. \n 2. Return to main menu.\n"))
				if choice1 == 2:
					ok1 = 0
			elif exist == "True":
				ok1 = 0
				ok = 0 
	elif choice == "0":
	 	print("Goodbye!")
	 	ok = 0
	
	else:
		print("Invalid input. Try again!\n")
print("Done")		
				


			



						




		









	
	


	
	



