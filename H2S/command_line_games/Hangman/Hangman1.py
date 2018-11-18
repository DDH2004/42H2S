#!/usr/bin/env python
import random

import sys
i = 0
underscore = []
selection = raw_input("Select easy, medium, or hard: ")


if selection == "easy":
	lives = 6
	easy = random.choice(open("easy_mode.txt").readline().split())
	i = 0
	while i < len(easy):
		underscore.append("_")
		i = i + 1
	for x in underscore:
		print x,
	while 0 < lives:
		print easy
		guess = raw_input("LETTER: ")
		if len(guess) > 1:
			print("1 letter only.")
			for x in underscore:
				print x,
			lives = lives - 1
		elif guess in easy:
			correctLetters = 0
			for i in range(len(easy)):
				if easy[i] == guess:
					underscore[i] = guess
			for i in range(len(easy)):
				if easy[i] == underscore[i]:
					correctLetters += 1
			if (correctLetters == len(easy)):
				print("You win")
				break
			for x in underscore:
				print x,
		else:
			print("That is not the correct letter.")
			print underscore
			lives = lives - 1
		i = i + 1
		print ("remaining lives " + str(lives))
	if 0 == lives:
		print("You ran out of lives")
		print("The word was: " + easy)



elif selection == "medium":
 	medium = random.choice(open("medium_mode.txt").readline().split())
 	print(medium)
 	i = 0
 	while i < len(medium):
 		print("_"),
 		i = i + 1



elif selection == "hard":
	lives = 10
	hard = random.choice(open("hard_mode.txt").readline().split())
	i = 0
	while i < len(hard):
		underscore.append("_")
		i = i + 1
	for x in underscore:
		print x,
	while 0 < lives:
		print hard
		guess = raw_input("LETTER: ")
		if len(guess) > 1:
			print("1 letter only.")
			for x in underscore:
				print x,
			lives = lives - 1
		elif guess in hard:
			correctLetters = 0
			for i in range(len(hard)):
				if hard[i] == guess:
					underscore[i] = guess
			for i in range(len(hard)):
				if hard[i] == underscore[i]:
					correctLetters += 1
			if (correctLetters == len(hard)):
				print(hard)
				print("You win")
				break
			for x in underscore:
				print x,
		else:
			print("That is not the correct letter.")
			for x in underscore:
				print x
			lives = lives - 1
		i = i + 1
		print ("remaining lives " + str(lives))
	if 0 == lives:
		print("You ran out of lives")
		print("The word was: " + hard)
