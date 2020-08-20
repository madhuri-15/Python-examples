## find a given number is Happy Number or not.;


def is_happy(num):
	"""is_happy(number)

	   This function returns whether a number is happy or not.

	   A Happy Number is a number which eventually reaches 1 when 
	   replaced by the sum of the square of each digit.
	"""
	def sum_sq(num):

		n = len(str(num))
		temp = num
		sum_ = 0
		while n > 0:
			re = temp % 10
			temp = temp // 10
			sum_ += re*re
			n -= 1

		if len(str(sum_)) == 1:
			if sum_ == 1:
				print("Happy Number")
			else:
				print('Unhappy Number')
		else:
			sum_sq(sum_)

	sum_sq(num)


num = 13
is_happy(num)
