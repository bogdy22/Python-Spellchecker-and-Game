# Spellchecker

import os, os.path, re, datetime
import time
from os import path
from difflib import SequenceMatcher

print("\nHello, " + os.getlogin() +"\nWelcome to the Spellchecker! \n")

with open("EnglishWords.txt", 'r') as a:
    English_words_list = [(line.rstrip('\n')) for line in a]

words_changed = 0
words_added = 0


def wrong_word(words ,word, correct, incorrect):
    global words_added
    global words_changed
    wrongword = word
    print("This word is incorrectly spelt: " + wrongword)
    choice2 = input("What do you want to do?\n 1. Ignore.\n 2. Mark the word.\n 3. Add the word to the dictionary.\n 4. Suggest likely correct spelling.\n Press the number of the action you wish: \n")
    if choice2 == "1":
        print("Word ignored")
    elif choice2 == "2":
        print("?" + wrongword + "?")
    elif choice2 == "3":
        f.close()
        with open("EnglishWords.txt", 'a') as f1:
            f1.write(wrongword + '\n')
            f1.close()
        print("Word added to the dictionary!")
        words_added += 1
    elif choice2 == "4":
        max_sequence = 0 #variable which contains the highest score of the matcher
        for suggestion in English_words_list:
            score = SequenceMatcher(None, suggestion, wrongword).ratio()
            if score > max_sequence:
                max_sequence = score
                finalword = suggestion
        print("The correct word may be: " + finalword + "\n")
        choice3 = input("What do you want to do?\n 1. Accept suggestion and replace the word.\n 2. Reject suggestion.\n")
        if choice3 == "1":
            words[i] = finalword
            words_changed += 1
        elif choice3 == "2":
            words[i] == wrongword
        else:
            print("Invalid input!. Try again!")
    
        

ok = 1     #variable used to control the while loop
while ok == 1:
    choice = input("What would you like to do? \nPress the number of the action you want to pursue: \n  1. Spell check a sentence. \n  2. Spell check a file. \n  To quit press 0.\n")

    now = datetime.datetime.now()
    
    
    if choice == "1":
        sentence = input(" Please enter the sentence you want to spellcheck: ")
        words = sentence.split(" ")
        new = re.sub("[^a-zA-Z]+", " ", sentence)
        print(new.lower())
        ok = 0 #exit the loop
        incorrect = 0
        correct = 0
        
        with open("EnglishWords.txt", "r") as f:
        	dictionary = f.readlines()
        dictionary = [line.rstrip('\n') for line in open("EnglishWords.txt")]
        
        import time
        start = time.time()
        for i in range(len(words)):
            found = 0
            for word_dict in dictionary:
                if words[i] == word_dict:
                    found = 1
                    correct += 1
            if found == 0:
                incorrect += 1
                wrong_word(words, words[i], correct, incorrect)
#       incorrect = len(words) - correct
#       print(correct, incorrect)
        end = time.time()
        elapsed = end - start
        
    elif choice == "2":
        ok1 = 1            # another variable used for controlling the while loop
        while ok1 == 1:
            file_name = input("Please enter the complete filename: ")
            exist = str(os.path.isfile(file_name))
            if exist == "False":
                choice1 = input("\nThe file you selected does not exist. \nPress the number of the action you want to pursue next: \n 1. Enter the filename again. \n 2. Return to main menu.\n")
                if choice1 == "2":
                    ok1 = 0
                elif choice1 == "1":
                	ok1 = 1
                else:
                	print("Invalid input. Try again!")
            elif exist == "True":
                ok1 = 0
                ok = 0
                with open(file_name, "r") as file:
                	for line in file:
                		for word in line.split():
                			print(word) #just for verification for now
    elif choice == "0":
         print("Goodbye!")
         ok = 0

    else:
        print("Invalid input. Try again!\n")
print("Current date and time: " + str(now))
print("\nThe new sentence is: " + ' '.join(words))
print("incorrect words: " + str(incorrect))
print("correct words: " + str(correct))
print("Added: " + str(words_added))
print("changed: "+ str(words_changed))
print("Total words: " +str(len(words)))
print("Time elapsed: ", elapsed)

print("Done")














































