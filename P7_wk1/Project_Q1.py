#AUTHOR: BABATUNDE IDAHOR
#COURSE: CS133
#TERM  : FALL 2015
#DATE  : 10/20/2015


#TITLE: This program lets a user type in an interger to produce the collatz Sequence
# starting with that integer and terminating when the sequence reaches 1.


print('Enter your collatze number here: ') # Ask for an input here.
num = int(input())

# This function definition calculates the collatz number entered by the user.
def collatz(num):
    if num%2 == 0:
        return num//2
    else:
        return 3 * num + 1


while num != 1:   # collatz sequence is terminated when the sequence reaches 1.
    num = collatz(num)    # collatz sequence is called recursively
    print(str(num))



