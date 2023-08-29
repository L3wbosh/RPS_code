#IMPORTS
import random
import time
import math
#GAME STUFF
Pscore = 0
playerWins = 0
playerLosses = 0
botWins = 0
botLosses = 0
ties = 0
Bscore = 0
rounds = 0
criteriaA = 0
criteriaB = 0
playerLog = []
botLog = []
predictions = []
alternative = False
winLose = False
setPrediction = False
rockUsed = False
paperUsed = False
scissorsUsed = False
def game():
    #####PLAYER#####
    #GLOBALS
    global Pscore
    global playerWins
    global playerLosses
    global botWins
    global botLosses
    global ties
    global Bscore
    global rounds
    global playerLog
    global botLog
    global prediction
    global choice
    global botChoice
    global criteriaA
    global criteriaB
    #Criteria
    criteriaA += 1
    criteriaB += 1
    #PLAYER STUFF
    choices = ["rock" , "paper" , "scissors"]
    choice = str(input("\nRock, Paper or Scissors   "))
    while choice not in choices:
        choice = str(input("\nRock, Paper or Scissors   "))
    print("\nCHECK 1 DONE :3")
    playerLog.append(choice)
    print("\nSooooo current log contents:" , playerLog)
    #####BOT#####
    if alternative == False or rounds < 3:
        #BOT STUFF
        selection = random.randint(1,100)
        if selection <= 35:
            botChoice = "rock"
        if selection > 35 and selection <= 65:
            botChoice = "paper"
        if selection > 65 and selection <= 100:
            botChoice = "scissors"
    if alternative == True:
        #WIN-LOSE
        #####WIN-LOSE#####
        print("\nOoh I bet you'll do the same thing!")
        if playerWins > 0 and botLosses == 0:
            if choice == "rock":
                prediction = "rock"
                setPrediction = True
            if choice == "paper":
                prediction = "paper"
                setPrediction = True
            if choice == "scissors":
                prediction = "scissors"
                setPrediction = True
        print("Okay so criteriaA is currently equal to" , criteriaA)
        print("Okay so criteriaB is currently equal to" , criteriaB)
        if playerLosses == criteriaA and botWins == criteriaB:
            print("\nOoh I bet you'll switch")
            if choice == "rock":
                options = ["paper" , "scissors"]
                prediction = random.choice(options)
                print("\nI bet you'll use" , prediction)
            if choice == "paper":
                options = ["rock" , "scissors"]
                prediction = random.choice(options)
                print("\nI bet you'll use" , prediction)
            if choice == "scissors":
                options = ["rock" , "paper"]
                prediction = random.choice(options)
                print("\nI bet you'll use" , prediction)
            predictions.append(prediction)
def interactions():
    #GLOBALS
    global choice
    global botChoice
    global Pscore
    global Bscore
    global playerWins
    global playerLosses
    global botWins
    global botLosses
    global ties
    #INTERACTIONS - PLAYER
    if choice == "rock" and botChoice == "scissors":
        Pscore += 1
        playerWins += 1
        botLosses += 1
        print("\nThe player wins!")
        print("\nSCORES ARE HERE!     PLAYER:" , Pscore , "BOT:" , Bscore)
    if choice == "paper" and botChoice == "rock":
        Pscore += 1
        playerWins += 1
        botLosses += 1
        print("\nThe player wins!")
        print("\nSCORES ARE HERE!     PLAYER:" , Pscore , "BOT:" , Bscore)
    if choice == "scissors" and botChoice == "paper":
        Pscore += 1
        playerWins += 1
        botLosses += 1
        print("\nThe player wins!")
        print("\nSCORES ARE HERE!     PLAYER:" , Pscore , "BOT:" , Bscore)
    #INTERACTIONS - BOT
    if botChoice == "rock" and choice == "scissors":
        Bscore += 1
        botWins += 1
        playerLosses += 1
        print("\nThe bot wins!")
        print("\nSCORES ARE HERE!     PLAYER:" , Pscore , "BOT:" , Bscore)
    if botChoice == "paper" and choice == "rock":
        Bscore += 1
        botWins += 1
        playerLosses += 1
        print("\nThe bot wins!")
        print("\nSCORES ARE HERE!     PLAYER:" , Pscore , "BOT:" , Bscore)
    if botChoice == "scissors" and choice == "paper":
        Bscore += 1
        botWins += 1
        playerLosses += 1
        print("\nThe bot wins!")
        print("\nSCORES ARE HERE!     PLAYER:" , Pscore , "BOT:" , Bscore)
    #INTERACTIONS - TIE
    if choice == botChoice:
        ties += 1
        print("\nTie")
        print("\nSCORES ARE HERE!     PLAYER:" , Pscore , "BOT:" , Bscore)
#####STATS#####
print("\nOkay. We're gonna study what you use most :3")
print("\nIt's round " , rounds)
print("\nAlright, you've won" , Pscore , "rounds out of" , rounds)
print("\nAlright, I've won" , Bscore , "rounds out of" , rounds)
print("\nPlayer wins:  " , playerWins)
print("\nPlayer losses:  " , playerLosses)
print("\nBot wins:  " , botWins)
print("\nBot losses:  " , botLosses)
print("\nTies:  " , ties)
#RATES
if playerWins == rounds:
    print("\nI have a 100% win rate")
if playerLosses == rounds:
    print("\nI have a 100% loss rate")
if botWins == rounds:
    print("\nBot has a 100% win rate")
if botLosses == rounds:
    print("\nBot has a 100% loss rate")
#ROUND 1
rounds += 1
print("\nRound" , rounds , "start!")
game()
interactions()
setPrediction = False
if setPrediction == True and choice == prediction:
    print("Aha! I was correct!")
    winLose = True
if setPrediction == True and choice != prediction:
    print("Oh I was wrong!")
#Round 2
rounds += 1
print("\nRound" , rounds , "start!")
game()
interactions()
if setPrediction == True and choice == prediction:
    print("Aha! I was correct!")
    winLose = True
else:
    print("Oh I was wrong!")
#Round 3
rounds += 1
print("\nRound" , rounds , "start!")
game()
interactions()
if setPrediction == True and choice == prediction:
    print("Aha! I was correct!")
    winLose = True
else:
    print("Oh I was wrong!")
def usingLog():
    #Globals
    global playerLog
    global botLog
    global rockUsed
    global paperUsed
    global scissorsUsed
    #Player stuff
    if rounds >= 2:
        #Bools
        if rockUsed == False:
            Pcount = playerLog.count("paper")
            Scount = playerLog.count("scissors")
            counts = [Pcount , Scount]
            if Pcount > Scount:
                throwOrder = ["paper" , "scissors"]
            if Scount > Pcount:
                throwOrder = ["scissors" , "paper"]
            if Pcount == Scount:
                print("")
        if paperUsed == False:
            Rcount = playerLog.count("rock")
            Scount = playerLog.count("scissors")
            counts = [Rcount , Scount]
        if scissorsUsed == False:
            Rcount = playerLog.count("rock")
            Pcount = playerLog.count("paper")
            counts = [Rcount , Pcount]
        if rockUsed == True and paperUsed == True and scissorsUsed == True:
            allUsed = True
            print("Hey! All used = True!")
            Rcount = playerLog.count("rock")
            Pcount = playerLog.count("paper")
            Scount = playerLog.count("scissors")
            counts = [Rcount , Pcount , Scount]
        print(counts)
        playerLog.sort()
        logLength = len(playerLog)
        playerLog.reverse()
        print("Soo log length is..." , logLength)
        if logLength == 2:
            highest = playerLog.pop(0)
            lowest = playerLog.pop(0)
        if logLength == 3:
            highest = playerLog.pop(0)
            middle = playerLog.pop(0)
            lowest = playerLog.pop(0)
        #Nonsense
usingLog()
#Round 4






















