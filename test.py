import random
#from limited import new

RPC = {"R":"Rock", "P":"Paper", "S":"Scissors"}


#print(var)

def newfunction():

    nolist = ["rock", "paper", "scissors"]

    var = random.choice(nolist)

    originalChoice = input(("choose R, P or S:  "))
    print (originalChoice)

    #print(originalChoice)

    #aiComputer = random.choice(nolist)

    mylist = {"R":["Rock", "r"], "P":["Paper", "p"], "S":["Scissors", "s"]}

    #print(aiComputer)


    
   
    if originalChoice in (mylist["R"]) and var == "rock":
        print("Player({}): CPU({}) \n It was a tie, try again!".format(mylist["R"], var))
        newfunction()
    elif originalChoice in (mylist["R"]) and var == "paper":
        print("Player({}): CPU({}) \n CPU Wins!".format(mylist["R"], var))
    elif originalChoice in (mylist["R"]) and var == "scissors":
        print("Player({}): CPU({}) \n Player Wins!!!!".format(mylist["R"], var))
    elif originalChoice in (mylist["P"]) and var == "rock":
        print("Player({}): CPU({}) \n Player Wins!!!!".format(mylist["P"], var))
    elif originalChoice in (mylist["P"]) and var == "paper":
        print("Player({}): CPU({}) \n It was a tie, try again!".format(mylist["P"], var))
        newfunction()
    elif originalChoice in (mylist["P"]) and var == "scissors":
        print( "Player({}): CPU({}) \n CPU Wins!".format(mylist["P"], var))
    elif originalChoice in (mylist["S"]) and var == "rock":
        print( "Player({}): CPU({}) \n CPU Wins!".format(mylist["S"], var))
    elif originalChoice in (mylist["S"]) and var == "paper":
        print( "Player({}): CPU({}) \n Player Wins!!!!".format(mylist["S"], var))
    elif originalChoice in (mylist["S"]) and var == "scissors":
        print("Player({}): CPU({}) \n It was a tie, try again!".format(mylist["S"], var))
        newfunction()

    else:
        print("Error Invalid Option, Try Again")
        newfunction()

newfunction()