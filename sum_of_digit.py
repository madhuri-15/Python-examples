
def sum_of_digit(num):

	if len(str(num)) > 1:

		total = 0
		while num > 0:
			re = num % 10
			total = total + re
			num = num // 10

		return total

	else:
		return num


num = 45

print(sum_of_digit(num))