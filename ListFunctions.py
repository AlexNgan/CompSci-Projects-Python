#Author: Gloria Ngan
#Date: 3/24/15

print"-----------------Append Function-----------------"
fid = open("O://Walker//Computer Science//Python//words.txt")

wordList = []
i=0

while i < 20:
    word = fid.readline()
    i = i+1
    #wordList += word
    wordList.append(word)   #append() adds characters or words
                            #onto the end of word
for word in wordList:
    print word

print"-----------------Extend Function-----------------"
#Lists to work with.
list1 = ['d','e']
list2 = ['a','b','c']
list3 = ['d','a','c','b']
print"Original lists:"
print"1 -",list1
print"2 -",list2
print"3 -",list3

print list1 + list2

list3.sort()        #Alphabetizes lists.
print list3

list1.extend(list2)     #Concatenates the lists and stores it all as 'list1'.

print list1

print"-----------------Sum Function-----------------"
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = range(1,10)   #Prints numbers from 1st to 10th index.
print numbers

print sum(numbers)      #sum() adds all the elements in the list.
