##rock paper and scissors game

import random

player = 0
computer = 0
play = 1
print("score is:", player, "v.s.", computer)

while play:
    enemy = random.randint(0, 2)
    choice = int(input("Enter 0 for scissors, 1 for rock, or 2 for paper: "))
    
    if choice == enemy:
        print("Draw")
    elif choice == 1 and enemy == 0:
        print("win")
        player += 1
    elif choice == 2 and enemy == 0:
        print("lose")
        computer += 1
    elif choice == 0 and enemy == 1:
        print("lose")
        computer += 1
    elif choice == 2 and enemy == 1:
        print("win")
        player += 1
    elif choice == 0 and enemy == 2:
        print("win")
        player += 1
    elif choice == 1 and enemy == 2:
        print("lose")
        computer += 1
    print("score is:", player, "v.s.", computer)
    if player == computer + 2 or computer == player + 2:
        play = 0
print()
if player > computer:
    print("You win")
else:
    print("You lost")
