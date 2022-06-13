import random
#from limited import new

RPC = {"R":"Rock", "P":"Paper", "S":"Scissors"}


#print(var)

def newfunction():

    nolist = ["rock", "paper", "scissors"]

    var = random.choice(nolist)

    originalChoice = input("choose an option:  ")
    print (originalChoice)

    #print(originalChoice)

    #aiComputer = random.choice(nolist)

    #mylist = {'Rock': 0, 'Paper': 1, 'Scissors': 2}

    #print(aiComputer)


    
   
    if originalChoice == ('rock') and var == "rock":
        print("Player({}): CPU({}) \n It was a tie, try again!".format(originalChoice, var))
        newfunction()
    elif originalChoice == ('rock') and var == "paper":
        print("Player({}): CPU({}) \n CPU Wins!".format(originalChoice, var))
    elif originalChoice == ('rock') and var == "scissors":
        print("Player({}): CPU({}) \n Player Wins!!!!".format(originalChoice, var))
    elif originalChoice == ('paper') and var == "rock":
        print("Player({}): CPU({}) \n Player Wins!!!!".format(originalChoice, var))
    elif originalChoice == ('paper') and var == "paper":
        print("Player({}): CPU({}) \n It was a tie, try again!".format(originalChoice, var))
        newfunction()
    elif originalChoice == ('paper') and var == "scissors":
        print( "Player({}): CPU({}) \n CPU Wins!".format(originalChoice, var))
    elif originalChoice == ('scissors') and var == "rock":
        print( "Player({}): CPU({}) \n CPU Wins!".format(originalChoice, var))
    elif originalChoice == ('scissors') and var == "paper":
        print( "Player({}): CPU({}) \n Player Wins!!!!".format(originalChoice, var))
    elif originalChoice == ('scissors') and var == "scissors":
        print("Player({}): CPU({}) \n It was a tie, try again!".format(originalChoice, var))
        newfunction()

    else:
        print("Error Invalid Option, Try Again")
        newfunction()

newfunction()