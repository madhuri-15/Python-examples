#This a simple calculator.

def calculator():
	"""caluculator()

	this is simple calculator which performs addition,
	subtraction, multiplication, and division of
	two numbers.

	"""

	def addition(a, b):
		return a + b

	def subtraction(a, b):
		return a - b

	def multiplication(a, b):
		return a * b

	def division(a, b):
		return a / b

	
	a = int(input("First Number is: ")) #first number
	b = int(input("Second Number is: ")) #second number

	print("Select the Operation:")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	
	op = int(input("Type here 1/2/3/4 = "))
            
	if op == 1:
		print("{} + {} = {}".format(a, b, addition(a, b)))

	elif op == 2:
		print("{} - {} = {}".format(a, b, subtraction(a, b)))

	elif op == 3:
		print("{} * {} = {}".format(a, b, multiplication(a, b)))

	elif op == 4:
		print("{} / {} = {}".format(a, b, division(a, b)))

calculator() #function call.

