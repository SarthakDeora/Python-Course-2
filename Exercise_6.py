# Stone Paper Scissors 
# Have to play 10 times
import random
i = 0
loose = 0
won = 0

print("********Play Stone Paper Scissors********")
while i != 11:
    list1 = ["Stone", "Paper", "scissors"]
    Options = random.choice(list1)
    a = input("What do u choose(s=Stone, p=paper, c=scissors):\n")
    if a == "s":# If u choose Stone  


        if Options == "Stone":
            
            print("its a tie try again!")
            # print(won, loose)
        elif Options == "Paper":
            print("Sad U lost")
            i+=1
            loose+=1
            # print(won, loose)
        elif Options == "scissors":
            print("U won!!!")
            won+=1
            print(won)
            i+=1
            # print(won, loose)
    elif a == "p": # If u choose paper
        if Options == "Stone":
            print("U won!!!")
            i+=1
            won+1
            print(won)
            # print(won, loose)
        elif Options == "Paper":
            print("its a tie try again!")
            # print(won, loose)
        elif Options == "scissors":
            print("Sad U lost")
            loose+=1
            i+=1
            
            # print(won, loose)
    elif a == "c": # if u choose scissors
        if Options == "Stone":
            print("Sad U lost")
            i+=1
            loose+=1
            # print(won, loose)
        elif Options == "Paper":
            print("U won!!!")
            i+=1
            won+=1
            print(won)
            # print(won, loose)
        elif Options == "scissors":
            print("its a tie try again!")
            # print(won, loose)
if won>loose:
    print("Congrats u won!!!!")
elif won == loose:
    print("Its a tieee!!!")
else:
    print("U lost u looser!!")


