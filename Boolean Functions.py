#Author: Gloria Ngan
#Date: 3/18/15

print""
print"-----------Boolean Function with Modulo-----------"

def  is_divisible(x, y):
    if(x % y == 0):
        return True
        print"True"
    else:
        return False
        print"False"
	
is_divisible(6, 4)
is_divisible(6, 3)

print"----------Boolean Function for Divisibility-----------"

def test_divisible(x,y):
    print""
    print"If x is",x,"and y is",y,"then:"
    if is_divisible(x,y):
        print 'x is divisible by y'
    else:
        print 'x is NOT divisible by y'

test_divisible(6,4)
test_divisible(6,3)

