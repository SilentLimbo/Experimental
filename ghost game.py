##Three doors appear ahead of you
##A ghost is behind a door
##Which door do you open? 1, 2, or 3
import random
reset = 'y'

print("It is Halloween, your friends decide to take you to a haunted house to play a game.")
print("As you enter the haunted house, you come across a room with 3 doors.")
print("You notice a sign in the middle of the room\n")
sign = input("Do approach and read the sign? ('y' for yes, 'n' for no): ")
if sign == 'y':
    print()
    print("You approach the sign cautiously, it reads: \n")
    print("BEWEAR, THERE IS A GHOST BEHIND ONE OF THESE DOORS!")
    print("You may only select one door to pass through to get out of this house.\n")    
elif sign == 'n':
    print("You shrug your shoulders and walk past the sign. Heading closer to the doors.\n")
else:
    print("-_-... Listen to directions next time, yeah?\n")
while reset == 'y':
    numDoor = random.randint(1, 3)
    counter = 0
    brave = 1

    while brave:
        if counter < numDoor:
            ghost = random.randint(1, 3)
            door = int(input("Pick a door (1, 2, or 3): "))
        else:
            brave = 0
            break
        if door == ghost:
            print("BOOOOOOOOOOOO!")
            print("Oh no you have encountered a ghost... is this the end!?")
            print("Game Over!")
            brave = 0
        else:
            print("Bing Pong! You picked a safe door!")
            print("congratz... on to the next!\n")
            counter += 1
            
    if counter == numDoor:
        print("Congragulations, you made it out of the house alive!")
        if counter == 1:
            print("You successfully passed through% d door" % counter)
        else:
            print("You successfully passed through% d doors" % counter)
    else:
        print("Unfortunate, better luck next time :)")
        if counter == 1:
            print("You successfully passed through% d door" % counter)
        else:
            print("You successfully passed through% d doors" % counter)

    print()
    reset = input("would you like to play again? ('y' for yes, 'n' for no): ")

