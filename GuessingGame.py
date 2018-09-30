import random
guess=random.randint(0,100)
n=0
while (n!=guess):
    n=int(input("Enter a from 1-100 number"))
    if(n==guess):
        print("You have found the nuber")
    elif(n<guess):
        print("it is less")
    else:
        print("it is more")
    
