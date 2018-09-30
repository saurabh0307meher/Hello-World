o1=input("ROCK/PAPER/SCISSOR?")
o2=input("ROCK/PAPER/SCISSOR??")

def compare(p1,p2):
    if(p1==p2):
        print("it is a tie")
    elif(p1=='rock'):
        if(p2=='scissor'):
            print("player 1 wins")
        else:
            print("player 2 wins")
    elif(p1=='scissor'):
        if(p2=='rock'):
            print("player 2 wins")
        else:
            print("player 1 wins")
    elif(p1=='paper'):
        if(p2=='rock'):
            print("player 1 wins")
        else:
            print("player 2 wins")
print (compare(o1,o2))
