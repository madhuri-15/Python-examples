#swap two numbers.

def swap(a, b):
    
    print("before swapping:")
    print("a =", a)
    print("b =", b)
    
    a, b = b, a
    
    print("after swapping:")
    print("a =", a)
    print("b =", b)


a = 2
b = 4
swap(a, b)