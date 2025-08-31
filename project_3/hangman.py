import random

list = ["apple", "banana", "potato", "onion", "mango"]

def hangman():
    word = random.choice(list)
    turns = 10
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    guessmade = ""


    while len(word) > 0 or turns > 0:
        main = ""
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else: 
                main = main +"_"+" "
        if main == word:
            print(main)
            print("You won!")
            break

        print("Guess the word :- "+ main)
        guess = input()
        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  ---------  ")
            if turns == 8:
                print("8 turns left")
                print("  ---------  ")
                print("      o      ")
            if turns == 7:
                print("7 turns left")
                print("  ---------  ")
                print("      o      ")
                print("      |      ")
            if turns == 6:
                print("6 turns left")
                print("  ---------  ")
                print("      o      ")
                print("      |      ")
                print("     /       ")
            if turns == 5:
                print("5 turns left")
                print("  ---------  ")
                print("      o      ")
                print("      |      ")
                print("     / \     ")
            if turns == 4:
                print("4 turns left")
                print("  ---------  ")
                print("    \ o      ")
                print("      |      ")
                print("     / \     ")
            if turns == 3:
                print("3 turns left")
                print("  ---------  ")
                print("    \ o /    ")
                print("      |      ")
                print("     / \     ")
            if turns == 2:
                print("2 turns left")
                print("  ---------  ")
                print("    \ o /|   ")
                print("      |      ")
                print("     / \     ")
            if turns == 1:
                print("Last chance for you, take a breathe")
                print("  ---------  ")
                print("      o \|_  ")
                print("      |      ")
                print("     / \     ")
            if turns == 0:
                print("You loose!!")
                print("  ---------  ")
                print("      o \|_  ")
                print("     /|\     ")
                print("     / \     ")
                print("You let a kind man die!")
                break
        

name = input("Enter your name :- \n")
print("welcome "+name)
print("---------------")
print("try to guess the word within 10 attempts")
hangman()

        
