#Spellchecker
		
import os, os.path, re, datetime, time
from os import path
from difflib import SequenceMatcher
from string import digits

print("\n┌ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ┐")   # formatting the menus with borders with Unicode characters
print("    Hello, " + os.getlogin() +"\n    Welcome to the Spellchecker!")
print("└ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ╍ ┘")


with open("EnglishWords.txt", 'r') as a:
    English_words_list = [(line.rstrip('\n')) for line in a]  #convert the file to list

words_changed = 0
words_added = 0

def wrong_word(words ,word):     # error spellcheck function
    global words_added
    global words_changed
    global correct
    global incorrect
    wrongword = word
    print("╳  This word is incorrectly spelt: " + wrongword + "  ╳ ")
    choice2 = input("\nWhat do you want to do?\n 1. Ignore.\n 2. Mark the word.\n 3. Add the word to the dictionary.\n 4. Suggest likely correct spelling.\n Press the number of the action you wish: \n")
    if choice2 == "1":
        print("  Word ignored!\n")
    elif choice2 == "2":
        words[i] = "?" + wrongword + "?"
        print("  Word marked!\n")
    elif choice2 == "3":
        f.close()
        with open("EnglishWords.txt", 'a') as f1:
            f1.write(wrongword + '\n')
        print("  Word added to the dictionary!\n")
        words_added += 1
        correct += 1
        incorrect -= 1
    elif choice2 == "4":
        max_sequence = 0 #variable which contains the highest score of the matcher
        for suggestion in English_words_list:
            score = SequenceMatcher(None, suggestion, wrongword).ratio()
            if score > max_sequence:
                max_sequence = score
                finalword = suggestion
        print("  The correct word may be: " + finalword + "\n")
        loop_4 = 1
        while loop_4 == 1:
            choice3 = input("What do you want to do?\n 1. Accept suggestion and replace the word.\n 2. Reject suggestion.\n")
            if choice3 == "1":
                words[i] = finalword
                words_changed += 1
                loop_4 = 0
                correct += 1
                incorrect -= 1
            elif choice3 == "2":
                words[i] == wrongword
                loop_4 = 0
                
                
            else:
                print("\nInvalid input! Try again!")
    else:
        print("\nInvalid input! Try again!")
        wrong_word(words, words[i])



with open("EnglishWords.txt", "r") as f:
    dictionary = f.readlines()
dictionary = [line.rstrip('\n') for line in open("EnglishWords.txt")]

menu_loop = 1
while menu_loop == 1:

    loop1 = 1     #variable used to control the while loop
    while loop1 == 1:
        print("╭ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄  ╮ ")
        choice = input("   What would you like to do? \n Press the number of the action you want to pursue: \n   1. Spell check a sentence. \n   2. Spell check a file. \n  To quit press 0.\n╰ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄  ╯\n")
        

        now = datetime.datetime.now()
        
        if choice == "1":
            sentence = input(" Please enter the sentence you want to spellcheck: ")
            new = re.sub("[^a-zA-Z]+", " ", sentence)      #removing any non-alpha characters
            remove_digits = str.maketrans('', '', digits)
            res = new.translate(remove_digits)             #removing any numeric characters
            res = res.lower()                              #converting uppercases in lowercases
            print("\n The sentence that is spellchecked is: " + res + "\n")
            words = res.split(" ")
            words = [i for i in words if i]    #removing potentially empty strings from the list after the removal of numeric characters above
            words_final = ''.join(words)
            
            loop1 = 0              #exit the loop
            incorrect = 0      # number of incorrect words
            correct = 0        # number of correct words
            
            start = time.time()
            for i in range(len(words)):
                found = 0
                for word_dict in dictionary:
                    if words[i] == word_dict:
                        found = 1
                        correct += 1
                if found == 0:
                    incorrect += 1
                    wrong_word(words, words[i])
            end = time.time()
            elapsed = end - start
            
        elif choice == "2":
            loop2 = 1
            while loop2 == 1:
                file_name = input("  Please enter the complete filename: ")
                exist = str(os.path.isfile(file_name))    #verify the existence of the file
                if exist == "False":
                    choice1 = input("\nThe file you selected does not exist. \nPress the number of the action you want to pursue next: \n 1. Enter the filename again. \n 2. Return to main menu.\n")
                    if choice1 == "2":
                        loop2 = 0
                    elif choice1 == "1":
                        loop2 = 1
                    else:
                        print("Invalid input. Try again!\n")
                elif exist == "True":
                    loop2 = 0
                    loop1 = 0
                    words = []
                    with open(file_name, "r") as file:
                        words = file.read().split()
                    words = ' '.join(words)
                    print("\nThe words in the given file are: " + words)
                    
                    correct = 0
                    incorrect = 0
                    
                    new = re.sub("[^a-zA-Z]+", " ", words)
                    remove_digits = str.maketrans('', '', digits)
                    res = new.translate(remove_digits)
                    res = res.lower()
                    print("\nThe words that are spellchecked are: ", res + "\n")
                    words = res.split(" ")
                    words = [i for i in words if i]
                    words_final = ''.join(words)
                    
                    start = time.time()
                    for i in range(len(words)):
                        found = 0
                        for word_dict in dictionary:
                            if words[i] == word_dict:
                                found = 1
                                correct += 1
                        if found == 0:
                            incorrect += 1
                            wrong_word(words, words[i])
                    end = time.time()
                    elapsed = end - start
           
                        
        elif choice == "0":
             print("Goodbye!")
             loop1 = 0
             menu_loop = 0
             
        else:
            print("\nInvalid input! Try again!\n")
        
        


    if choice != "0":
        print("Spellcheck completed! ✓\n")
        print("Summary Statistics: \n")
        print("  Total words: " +str(len(words)) + "\n")
        print("  Incorrect words: " + str(incorrect) + "\n")
        print("  Correct words: " + str(correct) + "\n")
        print("  Added words: " + str(words_added) + "\n")
        print("  Changed words: "+ str(words_changed) + "\n")
        print("  Time elapsed: " + str(elapsed) + "\n")
        print("  Current date and time: " + str(now) + "\n\n")
        
        Spellchecker_file = input("Please enter the filename where the spellcheck results and statistics will appear: ")
        Spellchecker_file = open(Spellchecker_file, 'w+')
        
        Spellchecker_file.write("Summary Statistics: \n\n")
        Spellchecker_file.write(" Total words: " +str(len(words)) + "\n")
        Spellchecker_file.write(" Incorrect words: " + str(incorrect) + "\n")
        Spellchecker_file.write(" Correct words: " + str(correct) + "\n")
        Spellchecker_file.write(" Added words: " + str(words_added) + "\n")
        Spellchecker_file.write(" Changed words: "+ str(words_changed) + "\n")
        Spellchecker_file.write(" Time elapsed: " + str(elapsed) + "\n")
        Spellchecker_file.write(" Current date and time: " + str(now) + "\n\n")
        words_string = ' '.join(words)
        words_not_marked = words_string.replace('?','')  # removing "?" from potentially marked words to output the original input in the results file
        Spellchecker_file.write(" The original (and processed) input was: " + words_not_marked + "\n")
        Spellchecker_file.write(" The new spellchecked sentence or file content is: " + words_string + "\n")
    

        loop = 1
        while loop == 1:
            final_choice = input(" \nCheck the results file you entered earlier to see more information.\n What would you like to do now? \n 1. Return to the main menu. \n 2. Quit.\n")
            if final_choice == "2":
                menu_loop = 0
                loop = 0
                print("Goodbye!")
            elif final_choice == "1":
                menu_loop = 1
                loop = 0
            else:
                print("Invalid input! Try again.")

        Spellchecker_file.close()

























