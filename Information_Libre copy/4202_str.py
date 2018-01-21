#!/usr/bin/env python
#This is strings
phrase = raw_input("")
def foo(s):
    ret = ""
    i = False  # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i   
    return ret
def ast(s):
	ret = ""
	for char in s:
		if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
			ret += '*'
		else:
			ret += char
	return ret
def check_parentheses (s):
	openbracket = 0
	closebracket = 0
	for char in s:
		if char == '(':
			openbracket = openbracket + 1
		elif char == ')':
			closebracket = closebracket + 1
	if openbracket == closebracket:
		print ("Balanced? True")
	else:
		print ("Balanced? False")
newphrase = foo(phrase)
print newphrase
print ast(newphrase)
check_parentheses (phrase)



