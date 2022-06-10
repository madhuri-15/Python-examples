#find a given number is prime or not.

from math import sqrt

def is_prime(num):
    
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            print("{} is not Prime Number.".format(num))
            break
    else:
        print("{} is Prime Number.".format(num))

        
num = 5
is_prime(num)
