#find a given number is prime or not.

def is_prime(num):
    
    for i in range(2, num):
        if num % i == 0:
            print("{} is not Prime Number.".format(num))
            break
    else:
        print("{} is Prime Number.".format(num))

        
num = 5
is_prime(num)
