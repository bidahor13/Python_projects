# NAME: BABATUNDE IDAHOR
# COURSE: CS 133
# PROJECT 4
# TERM: FALL 2015

#TITLE: This program is used to  play Rock-Paper-Scissors game with a user.

import random

# Function definition starts the game.
def playGame():
    print("You are playing Rock Paper Scisscors " + '\n' + '-------------------------------------')
    print ('')
    rand_Choice  = 1,2,3  # Random generated choices.
    score = [0,0,0] 
    index = 0
    while True:
        print("Lets Play!! :")
        print('-----------------------------------------------------')
        while True:
            human_Choice = input("Human!!! Input your choice here as 'rock', 'paper' or 'scissors' : ") 
            if (human_Choice.lower() == 'rock') :
                human_Choice  = 1
                break
            elif human_Choice.lower() == 'scissors' :
                human_Choice =  2
                break
            elif human_Choice.lower() == 'paper':
                human_Choice =  3
                break
            else:
                print(" Ops!! That is an invalid option in this game ")
                print(' Try again!  ')
                continue

        # Generates a random choice and checks if it matches the input from the player.
        compChoice  = random.choice(rand_Choice) 
        if human_Choice == compChoice: # compChoice is the choice from the computer.
            print(' ----Draw ---!')
            score[2] = score[2] + 1 #keeps track of the scores for each draw . 

        elif (human_Choice == 1 and compChoice == 2) or (human_Choice == 2 and compChoice == 3) or (human_Choice == 3 and compChoice == 1):
            print('You win! ')
            score[0] = score[0] + 1 #keeps track of the scores for each win. 
        else:
            print(' Ops! You lose ')
            score[1] = score[1] + 1  #keeps track of the scores for each lose. 

       # Loops to displays the curent score.  
        while True:
            answer = input('Do you want to play again? : ')
            if answer == 'yes' :
                print('Current score: Human - ',score[0],' Computer - ',  score[1] , " Draw's - ", score[2] )
                index = 0
                break
            elif answer == 'no' :
                print('Thanks for playing! Here is the final score: Human - ',score[0],' Computer - ',  score[1], " Draw's - ", score[2])
                index = 1
                break
            else:
                print(' ')
                print("---- Not the right response: Enter 'yes' or 'no' ---- ")
                continue
        if index == 0:
            continue
        else:
            break

playGame()
