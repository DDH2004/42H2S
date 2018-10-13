#!/usr/bin/env python

#By adevaras
#

import sys
import pdb
from collections import defaultdict

def foo():
	d = defaultdict(list)
	with open("capitols.txt", "r") as a:
		for line in a:
			arr=line.split()
			d[arr[0]].append(arr[1])
	a.close()
foo()

country = raw_input('Ready: ')
print(country)