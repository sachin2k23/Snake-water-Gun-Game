import random


Computer = random.choice([-1, 0, 1])
yourstr = input("Enter Your Choice:")
yourDict = {"s":1 , "w" :0 , "g": -1}
reverseDict = { 1 : "Snake", 0: "Water" , -1 : "Gun"}

you = yourDict[yourstr]

print(f"You have Entered {reverseDict[you]} and Computer has Entered {reverseDict[Computer]}")

if(Computer  == you):
    print("It's a Draww!!")

else:
    if(Computer == 1 and you == 0):
        print("You Loose!!")
    elif(Computer == 0 and you == 1):
        print("you Win!!!")
    elif(Computer == 1 and you == -1):
        print("you Win!!!")
    elif(Computer == -1 and you == 1):
        print("you Loose!!!")
    elif(Computer == 0 and you == -1):
        print("you Loose!!!")
    elif(Computer == -1 and you == 0):
        print("you Win!!!")
    else:
        print("Something is Wrong----")
