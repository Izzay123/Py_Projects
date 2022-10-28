#Rock paper scissors
from random import randint

hand = ['Rock', 'Paper', 'Scissors']

hands = hand[randint(0,2)]
mix = hands.lower()
usr = False

player = 0
computer = 0

while usr == False:
    user = input("Rock, Paper, or Scissors??")
    usr = user.lower()
    if usr == mix:
        print('Tie, go again!')
    elif usr == "rock":
        if mix == "paper":
            print("You lose!", mix, "covers", usr)
            computer += 1
        else:
            print("You win!", usr, "smashes", mix)
            player += 1
    elif usr == "paper":
        if mix == "Scissors":
            print("You lose!", mix, "cut", usr)
            computer += 1
        else:
            print("You win!", usr, "covers", mix)
            player += 1
    elif usr == "scissors":
        if mix == "rock":
            print("You lose...", mix, "smashes", usr)
            computer += 1
        else:
            print("You win!", usr, "cut", mix)
            player += 1
    elif usr == 'break':
        print("Thanks for playing!")
        print(f"Final score was Computer: {computer}, Player: {player}!")
        break
    else:
        print("That's not a valid play. Check your spelling!")
    usr = False
    hands = hand[randint(0,2)]
    mix = hands.lower()
    
#There's got to be an easier way to set user input to an input value and compare for less code. 
# Calling a .lower method on the list and comparison input would help too --done
#added scorekeeping.