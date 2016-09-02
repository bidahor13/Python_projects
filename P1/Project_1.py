#AUTHOR: BABATUNDE IDAHOR
#COURSE: CS133
#TERM  : FALL 2015
#DATE  : 10/8/2015

#This program shows the comparison of the balance of a bank account
#over time between simple, monthly and daily methods of compounding interest.

print('Project_1: Question_1')
print(' Calculate the simple, monthly and daily methods of compounding interest ' )
print('----------------------------------------------')
print('----------------------------------------------')


#*******Enter data where n is the number of years **************

n = int(input('Enter years:')) 
Initial_balance = float(input('Enter Initial_balance:'))
int_rate =  float(input('Enter Interest Rate:'))
simple_balance= mon_balance = daily_balance = Initial_balance


print('========== RESULTS =================================================================================================================')

# ****** Defined rates *****************************************

monthly_rate = int_rate/12 # generates the monthly rate
daily_rate = int_rate/365 # generates theyearly rate

#**************Range Calculation *****************************

for i in range(n):
   simple_balance += (simple_balance * int_rate)#yearly loop
   for j in range (12):
       mon_balance += (mon_balance *monthly_rate)#monthly loop
   for k in range(365):
       daily_balance += (daily_balance * daily_rate)#daily loop
   print ('Year: %d, Simple_balance $%8.2f cent, Monthly_Balance $%8.2f cent, Daily_Balance $%8.2f cent' %((i+1),simple_balance,mon_balance,daily_balance))

print ('---All Done---')



