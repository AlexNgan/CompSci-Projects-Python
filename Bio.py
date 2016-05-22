# -*- coding: utf-8 -*-	
#Bio program

# %d is used for data
# %s is used for strings
# %r is used for raw data
#These allow vars to be inbedded within a string

my_name = 'Gloria Ngan'
my_age = 16 #your age
my_height = 63.5 #your height
my_eyes = 'brown' #color of your eyes
my_hair = 'black'  #color of your hair

print 'My name is %s.' % my_name
print 'I am %d years old.' % my_age
print 'I am %d inches tall.' % my_height
print 'My eyes are %s and my hair is %s.' % (my_eyes, my_hair)

print 'If I add %d and %d, I get %d.' % (
    my_age, my_height, my_age + my_height)

