#AUTHOR: BABATUNDE IDAHOR
#COURSE: CS133
#TERM  : FALL 2015
#DATE  : 10/20/2015



## This program convert an input value in base 10 to a user
## selectable base betweeen 2 and 16.


#--------  Input number and base as required ----------------#

print('Enter an integer number here: ')
num = int(input())

print('What base number do you want to convert to?: ')
base = int(input())

# declared string literals  
hex_numerals = '0123456789ABCDEF'



##-----------------------condition--------------------------#

k = 0
while(num // base ** k  > 0):
    k += 1
k = k - 1

answer =''

#--------------conversion--------------------------#
for n in range(k, -1, -1):
    msg = num // base ** n   #where msg is the most significant number
    answer = answer +  hex_numerals[msg]
    num = num % base ** n
    
print('---------------------')
print(answer)


       


    






