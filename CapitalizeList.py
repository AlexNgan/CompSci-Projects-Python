#Author: Gloria Ngan
#Date: 3/24/15

#Function which capitalizes all letters in a list.
def capitalizeAll(wordList):
    result = []     #Empty list to store capitals.
    
    for letter in wordList:
        #Capitalizes a letter and appends it into the new list.
        result.append(letter.upper())
    print result

#Original list of letters.
wordList = ['a','b','c','d','e']
capitalizeAll(wordList)
