import string

fruit = "orange"

print"----------While Loop-----------"
index = 0
while index < len(fruit):    # len() gets length of a string
    letter = fruit[index]
    print letter
    index += 1               # incrementation is weird
print""

print"----------For Loop-----------"
res = ""
for char in fruit:
    res += char
    print res
print""

print"----------While Loop-----------"
message = raw_input("What is the message?")
for symbol in message:
    if symbol.isalpha():
        print"The symbol %r is alphabetical." % symbol
    if symbol.isupper():
        print"The symbol %r is uppercase." %symbol
    if symbol.islower():
        print"The symbol %r is lowercase." %symbol
print""
print"The ASCII number is %d." %ord("A")
print"The character associated with that ord is %s." %chr(ord("A"))
