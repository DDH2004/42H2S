#!/usr/bin/env python
number = int(10)
print("The secret word begins with a j.")
while number > 0:
	guess = raw_input("GUESS: ")
	if guess == "jokes":
		print "Good Job! You are one with the Source." 
		exit()
	if len(guess) == 0:
		print "You wasted a guess =P"
		number - 1 
	if number == 0:
			print "Sorry, you have run out of guesses."
	if len(guess) > 5 or len(guess) < 5 and len(guess) != 0 and len(guess) != "jokes":
		print "0, 1, 2, 3, 4 that's how we count to five!"
		number - 1
		if number == 0:
			print "Sorry, you have run out of guesses."
	if len(guess) == 5 and (guess) [0] != "j":
		print "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		number - 1
	if number == 0:
			print "Sorry, you have run out of guesses."
	if len(guess) == 5 and (guess) [0] == "j" and guess != "jokes":
		number - 1
		print("Wrong! You have " + str(number - 1) + " guesses left.")
	number-=1
	




