# NAME: BABATUNDE IDAHOR
# COURSE: CS 133
# PROJECT_5


print('Generate A Cellular Automata')

input_bitRule = ""
input_startState = ""

input_bitRule = input('Enter your 8 bit rule: ') 
input_startState = input('Enter your Start State: ') note
lenght_bit = len(input_startState)
hist = list()

while hist[-1] == input_startState:

#--------CASE_1--------: (at the beginning)

i = 0
slice_left = input_startState[-1]
slice_right = input_startState[i:i+2]

first_section = slice_left + slice_right #Appends the the slice_left and slice_right -
y =list()
y.append(first_section)
#print(y)    

#--------CASE_2------------:(at the middle )moves to the next bit and checks for the L and R neighbour -
i = 1
#x= list()
for i in range(1,lenght_bit-1):
    second_section =  input_startState[i-1:i+2]
    y.append(second_section)
    #print(x)

#-------CASE_3------------: at the end
i = 0
slice_left = input_startState[-2:]
slice_right = input_startState[i]
third_section = slice_left + slice_right #Appends the slice_left and slice_right -
#x= list()
y.append(third_section)
print(y)


print('--------------Function definition ---------------')
def test_run( item ):
    if item == '000':
        return input_bitRule[0]
    elif item == "001":
        return input_bitRule[1]
    elif item == "010":
        return input_bitRule[2]
    elif item == "011":
        return input_bitRule[3]
    elif item == "100":
        return input_bitRule[4]
    elif item == "101":
        return input_bitRule[5]
    elif item == "110":
        return input_bitRule[6]
    elif item == "111":
        return input_bitRule[7]

result = list()
for item in y:
    result.append( test_run( item ) )
    delimiter =''
    ans = delimiter.join(result)
    hist.append(ans)
    print(hist)
print('==================================================')


    




### A function that would look at the neighborhood 
##for i in range(startState, len(input_bitRule)):
##    if 


##def match_function( ):
    
        
   
##    row_list.append(input_row)
##    start_list.append(input_startState)

##    row_list.split(',')
##    start_list.split(',')

##def run_fxn(startState):
##    for i in range(0, len(row_list)):
