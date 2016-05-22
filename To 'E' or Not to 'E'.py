#To 'E' or Not to 'E'.py
#Author: Gloria Ngan
#Date: 3/18/15

print"-----------Returns True if the input has no 'e'.-----------"
def hasNoE():
    #Allows Python to read the external file.
    fid = open("O:\\Walker\\Computer Science\\Python\\words.txt")
    i = 0
    #Loops program for 10 words.
    while(i < 10):
        print""
        #Parses document line by line and stores the words in a var.
        line = fid.readline()
        word = line.strip()
        #Returns a boolean value if 'e' is present.
        if(word.count('e') > 0):
            print">>" + word
            print"FALSE, this word has an 'e'."
        else:
            print">>" + word
            print"TRUE, the letter 'e' is not present."
        #Increments i.
        i = i+1
 
hasNoE()
