#!/usr/bin/env python
import sys
import pdb

from collections import defaultdict
def foo():
	d = defaultdict(list)
	with open("names.txt", "r") as a:
		for line in a:
			arr=line.split()
			d[arr[0]].append(arr[1])
	for name in d:
		if len(d[name]) > 1:
			print(str(name) + ", " + "(" + str(len(d[name])) + "): " + str(d[name]))
	a.close()

foo()