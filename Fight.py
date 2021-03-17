import random

# options = [1, 2]

# whostarts = random.choice(options)

class Player:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

def choosePlayerOption(player1,player2):
    attackprotect = int(input(f"\nIt's {player1.name}'s turn, do you want to attack {player2.name}(1) or proect yourself(2)?\n"))
    Bonus = 5
    attackDamage = random.randrange(5, 16)
    defense = random.randrange(8)
    
    if attackprotect == 1:
        attackDamage += Bonus
        attackDamage -= defense
        player2.health -= attackDamage
        if attackDamage <= 0:
            print(f"\nYour attack was too weak! {player2.name}'s health is still on {player2.health}HP.")
            attackDamage = random.randrange(5, 16)
            defense = random.randrange(8)
            attackDamage -= defense
            player1.health -= attackDamage
            print(f"\n{player2.name} started a counter attack! you now have a health of {player1.health}HP.")

        else:
            print(f"\n{player2.name} got hit and now has a health of {player2.health}HP.")
            attackDamage = random.randrange(5, 16)
            defense = random.randrange(8)
            attackDamage -= defense
            player1.health -= attackDamage
            print(f"\n{player2.name} started a counter attack! you now have a health of {player1.health}HP.")

    if attackprotect == 2:
        defense += Bonus
        attackDamage -= defense
        player2.health -= attackDamage
        if attackDamage <= 0:
            print(f"\nYour attack was too weak! {player2.name}'s health is still on {player2.health}HP.")
            attackDamage = random.randrange(5, 16)
            defense = random.randrange(8)
            attackDamage -= defense
            player1.health -= attackDamage
            print(f"\n{player2.name} started a counter attack! you now have a health of {player1.health}HP.")

        else:
            print(f"\n{player2.name} got hit and now has a health of {player2.health}HP.")
            attackDamage = random.randrange(5, 16)
            defense = random.randrange(8)
            attackDamage -= defense
            player1.health -= attackDamage
            print(f"\n{player2.name} started a counter attack! you now have a health of {player1.health}HP.")

def gamestart():
    
    Player1 = Player(input("\nWhat is your name player1:\n"))

    Player2 = Player(input("What is your name player2:\n"))
    
    while Player1.health >=0 and Player2.health >=0:

        # if whostarts == options[0]:   
        choosePlayerOption(Player1, Player2)
        if Player2.health <=0:
            print(f"\n{Player1.name} has won the 1v1 with a health of {Player1.health}HP!")
        choosePlayerOption(Player2, Player1)
        # if whostarts == options[1]:
        if Player1.health <=0:
            print(f"\n{Player2.name} has won the 1v1 with a health of {Player2.health}HP!")
        


startgame = int(input("\nDo you want to play a 1v1?\nyes(1) no(2)\n"))

if startgame == 1:
    gamestart()

if startgame == 2:
    exit()