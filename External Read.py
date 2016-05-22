#Author: Gloria Ngan
#Date: 3/18/15


#CAN BE ENTERED DIRECTLY INTO THE SHELL.
def parseFile():
    #Allows Python to read an external file, and stores it in a variable called 'fid'.
    #The directory of the file must be inserted here, but use double slash.
    fid = open("O:\\Walker\\Computer Science\\Python\\words.txt")
    i=0
    while(i<10):
        #fid.readline()...built-in function that gets the first line of the doc.
        #This may return something like 'aa\n', a carriage return.

        #This will remove the weird shit.
        line = fid.readline()
        word = line.strip() 
        print word
        i=i+1

parseFile()
