#!/usr/bin/env python
import random
import sys
lives = 6
i = 0
underscore = []
selection = raw_input("Select easy, medium, or hard: ")



if selection == "easy":
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
			pos = easy.index(guess)
			underscore[pos] = guess
			for x in underscore:
				print x,
		else:
			print("That is not the correct letter.")
			print underscore
			lives = lives - 1
		i = i + 1
		print ("remaining lives " + str(lives))



elif selection == "medium":
 	medium = random.choice(open("medium_mode.txt").readline().split())
 	print(medium)
 	i = 0
 	while i < len(medium):
 		print("_"),
 		i = i + 1



elif selection == "hard":
 	hard = random.choice(open("hard_mode.txt").readline().split())
 	print(hard)
 	i = 0
 	while i < len(hard):
 		underscore.append("_")
		i = i + 1
	for x in underscore:
		print x,
	while 0 < lives:
		print hard
		guess = raw_input("LETTER: ")
		if guess in hard:
			pos = hard.index(guess)
			underscore[pos] = guess
			for x in underscore:
				print x,
		else:
			print("That is not the correct letter.")
			print underscore
			lives = lives - 1
		i = i + 1
		print ("remaining lives " + str(lives))
