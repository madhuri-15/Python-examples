# Python program to reverse given number.

def reverse_num(num):
	
	count = len(str(num))
	rev_num = 0
	
	while count > 0:
		re = num % 10
		rev_num = re + rev_num * 10
		num = num//10
		count -= 1

	return rev_num
		

n = 1234
print(reverse_num(n)) 

#OUTPUT:
#4321
