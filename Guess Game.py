import random as r 

x = r.randint(0, 9)

for i in range(4):
    y = int(input("Enter the guess number between 0 and 9: "))
    if y > x:
        print("Enter a smaller value")
    elif y < x:
        print("Enter a greater value")
    else:
        print("You guessed it RIGHT!! Hurray You WON")
        break
else:
    print("You did not guess correctly. The correct number was:", x)
