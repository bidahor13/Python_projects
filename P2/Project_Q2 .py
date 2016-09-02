#AUTHOR: BABATUNDE IDAHOR
#COURSE: CS133
#TERM  : FALL 2015
#DATE  : 10/20/2015

#----------Guess the Number Game--------------------#

import random

print("Do you want to play a Guessing game: enter 'yes' or 'no' ")
ans = str(input().lower())

print('Enter any number of your choice between 1 and 10')


#--------------------- Process------------------------#
randNum = random.randint(0,10) # populates a random number
while ans == 'yes':
##   randNum = random.randint(0,10)
   print('Enter a number: ' )
   gNum = int(input())
   if gNum < randNum :
      print('too low, Try again!')
      
   elif gNum > randNum :
      print('too high, Try again')
      
   elif gNum == randNum:
      print('YAY!!.......Congratulation!!' )
      print('---------------------------')
      randNum = random.randint(0,10)
      
      
#--------- Restarts the game--------------------------#
      print('Do you want to play again?' )
      ans = str(input())
      while ans == 'yes':
         break

# -------output if the player exits from the game-----#      
print('Alright, maybe some other time!!')
   



        
        
        



