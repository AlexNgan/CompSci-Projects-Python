#Author: Gloria Ngan
#Date: 3/17/15

import math #Need this for advanced arithmetic operations

#When using the trig functions, Python expects input in radians.
#degrees = 180/pi * rad

#This function takes a parameter, the variable 'thing'. 
def printTwice(thing):
    print thing, thing

#The argument is the value of the variable being passed as a parameter.
#Here, the arguments are "Spam".
printTwice("Spam")
printTwice("Spam" * 4)

def catTwice(part1, part2):
    cat = part1 + part2     #This will result in an error; cat is a local
    printTwice(cat)         #variable and can't be passed outside.

def baberhamLincoln():      
    speech1 = "Fourscore and seven "
    speech2 = "years ago."
    printTwice(speech1 + speech2)

baberhamLincoln()
