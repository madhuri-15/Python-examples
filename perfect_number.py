# to find a number is perfect number or not.
#


def is_perfect(num):
	"""
	is_perfect(number)
	
	returns a number is Perfect number or Not.
	
	sum of factors of a number is equal to number itself,
	that number is called the perfect number.
	"""
	
	factors = []
	for i in range(1, num):
		if num % i == 0:
			factors.append(i)

	sum_ = sum(factors)

	if num == sum_:
		print("The {} is perfect number.".format(num))
	else:
		print("The {} is not perfect number.".format(num))

num = 6
is_perfect(num)
