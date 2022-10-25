print("Welcome to Evens or Odds, where we can magically tell you what your number is.")

while True:
    try:
        x = int(input("What number are you thinking of?\n"))
        if x % 2 == 0:
            print("That's an even!\n")
            continue
        elif x % 2 != 0:
            print("That's an odd!\n")
            continue
        elif x == "break":
            break
    except ValueError:
        print('Please enter an integer\n')