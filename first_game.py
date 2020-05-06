from random import randint
for x in range(1,6):
    guesNumber=int(input("Enter your gues between 1-5: "))
    randomNumber=randint(1,5)
    if guesNumber == randomNumber:
        print("You have own")
    else:
        print("you have lost")
        print("random number was: ",randomNumber)