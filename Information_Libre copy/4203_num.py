#!/usr/bin/env python
#numbers and casting
raw = raw_input("")
numbers0 = raw.split(" ")
numbers1 = int(numbers0 [0])
numbers2 = int(numbers0 [1])
print (str(numbers1) + " divided by " + str(numbers2) + " equals " + str(numbers1/numbers2) + " remainder " + str(numbers1%numbers2))
a = 10
b = 56.99
c = complex(2, 3)
d = long(-1/2)

def printnum(name,num):
	print ("Variable " + name + " contains: " + str(num) + " which is type of: " + type(num).__name__)

printnum("a", a)
printnum("b", b)
printnum("c", c)
printnum("d", d)