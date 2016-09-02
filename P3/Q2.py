#AUTHOR: BABATUNDE IDAHOR
#COURSE: CS133
#TERM  : FALL 2015
#DATE  : 11/3/2015


##This program accepts a list of test scores and produces a histogram summarizing
##the data.


# Enter Input score here
num_of_values = int(input('Enter the number of test score you have: ')) # number of values to be entered by the user
test_score = list() # creates a list to store test_scores
start = 0


#This loop creates a list and stores/appends the values in test_score.
for i in range(start, num_of_values, 1):
    test_scoreEntered = float(input('Enter test score here: '))  # takes floating values
    test_scoreEntered = round(test_scoreEntered)  # returns the floating point value number rounded to zero after the decimal point 
    test_score.append(test_scoreEntered)
print('---------------All Done-------------------------- ' + '\n' + 'Data Entry so far ' + str(test_score))


# Creates a new dictionary and traverses the dictionary
dict_score = dict()
for i in test_score:
    if i not in dict_score:
        dict_score[i] = '*'
    else:
        dict_score[i] += '*'
        
print('----------------Histogram Result------------------')        
num = list(dict_score.keys())
num.sort()


# Displays the histogram #
for i in num:
    if i < 10 :
        print('v'+str(int(i)) + '   ' + dict_score[i])
    else:
        print('v'+str(int(i)) + '  ' + dict_score[i])
        
    


       



