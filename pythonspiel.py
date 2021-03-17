import random

def Startgame():
    
    Nummer = random.randrange(0, 100)
    Guessednummer = -1
    Tries = 0
    
    while Nummer != Guessednummer:
        
        Guessednummer = int(input("Guess the number:\n"))

        if Nummer > Guessednummer:
            print("The guessed number is not corect, the number has to be higher!")

        if Nummer < Guessednummer:
            print("The guessed number is not corect, the number has to be lower!")
        
        Tries +=1

    print(f"\nYou won!\nYour tries:{Tries}\n")

    Nochmalspielen = int(input("Do you wan't to play again?\nyes(1) no(2)\n"))

    if Nochmalspielen == 1:
        Startgame()

    if Nochmalspielen == 2:
        exit()

Startgame()