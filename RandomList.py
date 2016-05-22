#Author: Gloria Ngan
#Date: 3/26/15

print"--------------Randomizes Letters---------------"
import random
i=0
list1 = []
#Allows Python to generate random chars between ASCII 65-90(A-Z).
while i < 20:
    letter = chr(random.randint(65, 90))
    i = i+1
    list1 += letter
print list1

print""
print"----------------String to List-----------------"
s = "Hello World"
t = list(s)

print t

print""
print"-----------Break a String into Words------------"

wurd = "Robots are cooler than you."
list2 = wurd.split()    #split() function
print list2

print""
print"---------Joins List Elements into String----------"

roboList = ['Robots', 'are', 'cooler', 'than', 'you.']
delimiter = " "     #This is what is inserted between each list element.
print delimiter.join(roboList)
