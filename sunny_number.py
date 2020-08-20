## check whether a given number is sunny Number or not.;


def is_sunny(num):
	"""is_sunny(number)

	   This function returns whether a number is sunny or not.

	   A number N is called sunny number if the square root of the number
	   N+1 is an integer number.
	   for example: 24 is Sunny number because 24 + 1 = 25 has square root
	   of 5 which is an integer.
	"""
	import math as m
	
	temp = num + 1
	sqrt = m.sqrt(temp)
	
	if int(sqrt) == sqrt:
		print('Sunny Number.')
	else:
		print('Not Sunny Number.')
	
num = 3
is_sunny(num)
