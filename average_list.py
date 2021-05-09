# Python program to calculate average of numbers in a given list.


def average_of_list(list_):
	avg = sum(list_)/len(list_)
	return avg

list_ = [1, 2, 4, 5]

#to get list from user.
input_list = []

n = int(input('Total number of elements in a list: '))

for i in range(n):
	elem = int(input('enter a number: '))
	input_list.append(elem)

average = average_of_list(input_list))
print(average)


