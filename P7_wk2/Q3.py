# NAME: BABATUNDE IDAHOR
# COURSE: CS 133
# PROJECT 4
# TERM: FALL 2015

#TITLE: This program compares two files and creates a third file containing a list of all the
#       words found in both files.


import string

def process_file(filename1): # defined function 1
    file_List = list()
    fp = open(filename1) 
    for line in fp:   #loops through the file
        process_line(line, file_List) # call the function2 here
    fp.close()
    return file_List

    
def process_line(line, file_List):  # function 2 goes through the file 
    line = line.replace('-', ' ') # anywhere with a '-' replace with a space ' '
    line = line.replace(',', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace) # removes all whitepaces and a punctions
        word = word.lower()  # converst a words in the list to lower case
        if word not in file_List:
            file_List.append(word)


            
list1 =  process_file('file1.txt') # reads the file1 
list2 =  process_file('file2.txt')  # reads the file2
list3 = list() # stores it as a list for easy access.
for item in list1:  #Loop through the list1
    if item in list2: # Checks if the word exist file2
        list3.append(item)

list3.sort() # sorts the list       

# Writes the words to a new file called file3.txt
fp =  open("file3" ,  'w') 
for item in list3:
    fp.write(item)
    fp.write('\n')

fp.close()









##with open('file1.txt', 'r') as file1:
##    with open('file2.txt', 'r') as file2:
##        same = set(file1).intersection(file2)
##
##same.discard('\n')
##
##with open('Output_file.txt', 'w') as file_out:
##    for line in same:
##        file_out.write(line)
