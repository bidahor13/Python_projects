#BABATUNDE IDAHOR
#PROJECT_4
#COURSE : CS133
#TERM: FALL 2015


##This program translates an English word or phrase and translate it into Pig Latin using a Pig Latin translator. 

print ('Welcome to the Pig Latin Converter')


playAgain = 'yes'
while playAgain.lower() == 'yes':
    try: #Exception handler
        phrase = input("Enter an English word or phrase: ")
        print('------------------ OUTPUT ----------------------------------'+ '\n')
        

        wordList =list() #creates the 1st new list
        wordList2 = list() #creates the 2nd new list
        symbol = "!@#$%^&*()?." #stores special symbol
        latin_suffix ='AY' # latin suffix to be added to the end of the word.
        
        wordList.append(phrase) # adds the word to the list
        split_word = phrase.split(' ') # separates each word
        
        display='' #used to convert string of words in the list into a string.
        
        
        # Loops over the list of each word appending the letters AY to each letter.
        for i in range(0, len(split_word)):
            wordList2 = split_word[i]
            oldWord = wordList2
            new_word = oldWord
            for s in symbol:
                new_word = new_word.strip(s)

            new_word = new_word[1:] + new_word[0] + latin_suffix    # Word or phrase arrangement
            if not new_word.isalpha():
                raise Exception("Not a valid input!! Only words or phrases are allowed") # return the exceptions to the user.
            
     # appends the symbols back to phrase or word.
            for s in symbol:
                if s in oldWord:
                    new_word = new_word + s
            
            new_word = new_word + ' '
            display +=  new_word
        
        # prints out the phrases or word in uppper case
        print('English Word:   '+ phrase.upper()+'.')
        print('Pig Latin Word: '+ display.upper()+'.' )
    except Exception as e:
        print(e)

    playAgain = ""
    while(playAgain != "yes" and playAgain != "no"):
        playAgain = input("Play Again..? :  ").lower()
