import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([0, -1, 1])
youstr = input("Enter your choice: ")
youdict = {"snake": 1,"water": -1,"gun": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youdict[youstr]

#by now we have 2 numbers(variables), computer and you

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
 
if(computer==you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("You won!")

    elif(computer == -1 and you ==0):
        print("You loose!")
    
    elif(computer == 1 and you == -1):
        print("You loose!")

    elif(computer == 1 and you == 0):
        print("You won!")
    
    elif(computer == 0 and you == -1):
        print("You win!")

    elif(computer == 0 and you == 1):
        print("You loose!")

    else:
        print("Something went wrong")