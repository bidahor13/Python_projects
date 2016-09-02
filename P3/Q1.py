#AUTHOR: BABATUNDE IDAHOR
#COURSE: CS133
#TERM  : FALL 2015
#DATE  : 11/3/2015


#This program  checks if two user input strings are anagrams of each other.

print('Project_3: Q1')
print('----------------------------------------------')
print('----------------------------------------------')


#Input values
word1 = str(input('Please enter first word: '))
word2 = str(input('Please enter secord word: '))

# Go through the list and check if word1 matches word2.
word1a = word1.lower() # converts the string to a lower case
word2b = word2.lower()

#convert to a list
word1_list = list(word1a)
word2_list = list(word2b)

#Sorts the existing list
word1_list.sort()
word2_list.sort()

#Loop removes the white spaces from the sorted list.
while ' ' in word1_list:
    word1_list.remove(' ')

while ' ' in word2_list:
    word2_list.remove(' ')


# checks for anagrams
if word1_list == word2_list:
    print( '\n'+ "Yes it's an Anagram!")
    print('\n' + '------------------------PROOF------------------')
    print(word1_list)
    print(word2_list)
else:
    print( 'hmm!! - No, they are not Anagrams' )
    print(word1_list)
    print(word2_list)

print('------------------------All Done!----------------')
