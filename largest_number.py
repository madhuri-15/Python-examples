#find a largest number from List.

def largest_num(list_):
    
    list_.sort()      #sort list in an ascending order.
    return list_[-1]  #so last number is largest number among the list.

list_ = []
n = 5
for i in range(n):
    num = int(input("enter element: "))
    list_.append(num)

print("largest number among the list is: ",largest_num(list_))
