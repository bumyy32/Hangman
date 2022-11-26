# Print the hangman
def print_hangman(guesses, word):
    if guesses == 0:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 1:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 2:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|     |")
        print("|     |")
        print("|")
        print("|________")
    elif guesses == 3:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|    \|")
        print("|     |")
        print("|")
        print("|________")
    elif guesses == 4:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|    \|/")
        print("|     |")
        print("|")
        print("|________")
    elif guesses == 5:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|    \|/")
        print("|     |")
        print("|    /")
        print("|________")
    elif guesses == 5:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|    \|/")
        print("|     |")
        print("|    / \ ")
        print("|________")
        print("\n")
        print("THE WORD WAS: " +word)
        print('\n')
        print("YOU LOSE! WOULD YOU LIKE TO TRY AGAIN??")
        print("Type y for yes or n for no: ")
        again = input()
        again = again.lower()
        if again == "y":
            hangman()
        else:
            print("Thanks for playing, hope u enjoyed :D ")


    def select_word():
        file = open("words.txt")
        
