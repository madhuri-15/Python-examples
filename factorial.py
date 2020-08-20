#find a factorial of a number without recursion.

def factorial(n):
	"""
	factorial(number)

	this function return a factorial of number 'n', 
	the factorial of number is a product of number from 1
	to that number.
	"""
    if n < 0:
    	return ("Factorial cannot be found for negative numbers.")
    
    if n == 0 or n == 1:
        return ("Factorial of {} is 1".format(n))
    
    if n > 0:
        
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
            
        return fact
    
#n = int(input("enter a number: "))


print(factorial(5))
print(factorial.__doc__)