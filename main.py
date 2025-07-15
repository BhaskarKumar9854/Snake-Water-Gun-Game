import random
# We all have played Snake , Water,Gun Game in our Childhood.
# This is a simple implementation of that game in Python.



print("Welcome to the Water, Gun, Snake game!")
computer = random.choice([-1,0,1])
youstr= input("Enter your choice (-1 for water, 0 for gun, 1 for snake): ")
youDict={"s":1,"g":0,"w":-1}
reverseDict = {1:"Snake", 0:"Gun", -1:"Water"}

if youstr in youDict:
    you = youDict[youstr]
else:
    print("Invalid input! Please enter 's', 'g', or 'w'.")
    exit()


print(f"You chose: {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a tie!")

else:
    if(computer ==-1 and you == 1):
        print("You win! Gun beats Water.")

    elif(computer == 0 and you == -1):
        print("You win! Water beats Gun.")
    elif(computer == 1 and you == 0):
        print("You win! Snake beats Gun.")
    elif(computer == -1 and you == 0):
        print("You lose! Gun beats Water.")
    elif(computer == 0 and you == 1):
        print("You lose! Water beats Gun.")
    elif(computer == 1 and you == -1):
        print("You lose! Snake beats Water.")
    else:
        print("Invalid input, please try again.")
