##!/usr/bin/env python
#true, false, and nil/none
from random import choice
number = 10
while number > 0:
	def op(price,price1,price2):
		if price1 == 'or':
			return price or price2
		if price1 == '==':
			return price == price2
		if price1 == '!=':
			return price != price2
		if price1 == 'and':
			return price and price2
	price = choice(list(set([False, True, True, None, True, None, None, False, False, None, True, False])))
	price1= choice(list(set(['or', 'or', 'or', '==', '!=', '==', 'and', '==', '!=', 'and', '!=', 'and'])))
	price2= choice(list(set([False, False, None, None, True, True, False, True, None, False, True, None])))
	price00 = str(price)
	price02 = str(price2)
	print price00 + ' ' + price1 + ' ' + price02 + ' => ' + str(op(price,price1,price2))
	number = number - 1
