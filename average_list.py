# Python program to calculate average of numbers in a given list.

def avg_list(list_):
    
    return sum(list_)/len(list_)

list_ = [1, 2, 4, 5]

#to get list from user.
input_list = []
n = 10 #int(input('Total number of elements in a list: '))
for i in range(10):
	elem = int(input('enter a number: '))
	input_list.append(elem)


print(avg_list(input_list))
