#Author: Gloria Ngan

#Basic syntax: listName = [element1, element2, element3]

#Demonstrates basic functions of a list.
def listDemo():
    theList = ['A','B','C','D']
    print theList[0]    #Returns first element in list.

def isSorted():
    testNumList = [1,2,3,4]
    testCharList = ['b','c','d','a']
    x=0
    i=0
    while i<len(testNumList):
        if testNumList[x] < testNumList[x+1]:
            print "True"
            x +=1
        else:
            print"False"
isSorted()
listDemo()
