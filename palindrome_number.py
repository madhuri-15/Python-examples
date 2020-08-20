
def palindrome_number(num):

	n = num
	num1 = 0

	while n != 0:
		re = n % 10
		n = n//10
		num1 = num1*10+ re

	if num == num1:
		print("Number is Palindrome Number.")

	else:
		print("Number is Not Palindrome Number.")

num = 121
palindrome_number(num)