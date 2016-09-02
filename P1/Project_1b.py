#AUTHOR: BABATUNDE IDAHOR
#COURSE: CS133
#TERM  : FALL 2015
#DATE  : 10/8/2015


#This program prints a table of powers.The program should 
#read three values: a base and two exponents, min and max.


print('Project_1: Question_2')
print('----------------------------------------------')
print('----------------------------------------------')


base=int(input('Enter base number: '))# Enter the base number.Base number must be an integer#
min =int(input('Enter min: ') )# Enter the min number.Min number must be an integer#
max=int(input('Enter max: '))# Enter the max number must be an integer#


for n in range(min, max+1, 1): #The program should print output values for base^n for min≤n≤max
    base**n
    print('' + str(base) +' ^ ' + str(n) +  ' = ' + str(base**n) )

print('--------All Done!---------')
    
