# NAME: BABATUNDE IDAHOR
# COURSE: CS 133
# PROJECT_5
# TERM: FALL 2015


# This program is generates a cellular Automata

print('Generate A Cellular Automata')

input_bitRule = ""
startState = ""

run_automata = True
while( run_automata ):
    input_bitRule = input('Enter your 8 bit rule: ') 
    startState = input('Enter your Start State: ')
    if( startState.isdigit() and input_bitRule.isdigit() and len(input_bitRule) == 8 ): #ensures the input bit rule is a 8bits.
        run_automata = False
    else:
        print("Try again!! enter only 0's and 1's as Check inputs_bits and startState ")


#Genrates the function 
def auto( input_startState ):
    lenght_bit = len(input_startState)
    hist = list()

    #--------CASE_1------------: (at the beginning)

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
    delimiter =''
    ans = delimiter.join(y)
    hist.append(ans)
##    print('All 3 cases resolve:')
##    print(hist)
##    print(y)
    return y
    
print('-------------------------------------------------------------')
#Functions test_run run the matches over the assigned bit.
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
    
print('========================OUTPUT================================')
hist = list()
hist.append(startState) # add initial startstate to the list
currentState = startState
y = auto( currentState )
temp = ''
for item in y:
    temp += test_run( item )
currentState = temp
hist.append( currentState )
##print(currentState)

while( currentState != startState ): # condition is true when currentstate is not equal to startState
    y = auto( currentState )
    temp = ''
    for item in y:
        temp += test_run(item)
    currentState = temp
    hist.append(currentState)
for item in hist:
    print(item )
# number of times the bits are generated.
print( 'Period: ' + str(len(hist)-1)    )

    



