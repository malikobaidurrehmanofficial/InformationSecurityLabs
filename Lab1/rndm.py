import random

randomNumber=random.randint(1,9)

choice=int(input("Guess any number between 1 and 9 "))

lpp=True
while lpp!=False:
    choice=int(input("Guess any number between 1 and 9 "))
    if(choice==randomNumber):
        print("Congratulation your guess was right , if you want to play again press 1 otherwise 0")
        choice=int(input())
        if choice==0:
            lpp=False

        else:
            choice=random.randint(1,9)

    elif choice>randomNumber:
        print("The number you guessed is greater ")

    else:
        print("The number you guessed is short")

    




