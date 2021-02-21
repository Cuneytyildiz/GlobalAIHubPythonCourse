from random import choice
class Hangman():

    def __init__(self):
        print("-----HANGMAN-----")
        print("\nRemember, you have 3 chances!\nGood Luck!")

    def Words(self):
        words = ["python","globalaihub","programming","computer"]
        rndword = choice(words)
        return rndword
    
    def Start(self,w):
        turns = 3
        guess=[]
        while turns != 0:
            print(f"\nYour Remaining Right : {turns}\n")
            for letter in w:
                if letter in guess:
                    print(letter,end=" ")
                else:
                    print("___",end=" ")
            
            letter = input("\tGuess a Letter : ")
            if letter in w:
                print("You Guessed Right!")
                guess.append(letter)
            else:
                print("You Guessed Wrong!")
                turns -= 1
            
            if set(w) == set(guess):
                print("\n-----Congratulations!-----\nYou won!")
                break
        
        if turns == 0:
            choice = input("\n-----You Lose...-----")
            
while True:

    choose = input("Do you want to play ? ( Y / N ) :")

    if choose == 'Y' or choose == 'y':
        game = Hangman()
        newgame = game.Words()
        game.Start(newgame)

    else:
        print("Goodbye !!!")
        break