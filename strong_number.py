

def is_strong(num):
	"""
	is_strong(number)
	
	returns a number is strong number or not.
	
	'strong number' is number whose sum of factorial
	of digits is equal to original number.
	
	"""
	def factorial(n):
		
		fact = 1
		for i in range(1, n+1):
			fact = fact * i
		return fact

	sum_ = 0
	n = len(str(num))
	temp = num

	while n > 0:
		re = temp % 10
		temp = temp // 10
		sum_ = sum_ + factorial(re)
		n -= 1

	if num == sum_:
		print("Strong number.")
	else:
		print("Not Strong number.")


num = 145
is_strong(num)
