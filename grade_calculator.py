# Python program to calculate grade.
#
# take in the marks of 5 subjects.
# display the grade.


# grade A --> >= 70%
# grade B --> >= 60%
# grade C --> >= 40%
# grade F --> < 40%

#


def get_grade(mark_list):

	result = list(map(lambda x: x < 40, mark_list)) #to check if student pass in all subjects.
	if True in result:
		return "Grade F"

	total = 500
	marks_obtained = sum(mark_list)

	percentage = ( marks_obtained / total ) * 100

	if percentage >= 70:
		return "Grade A"

	elif percentage >= 60:
		return "Grade B"

	elif percentage >= 40:
		return "Grade C"

	elif percentage < 40:
		return "Grade F"


#marks for five subjects.
mark_list = [40, 65, 60, 76, 87]

#to get the user input.
mark_list = []
subjects = ['English', 'Marathi', 'Sanskrit', 'Mathematics', 'Science']

print("Enter the five subjects marks.")

for i in range(len(subjects)):
	marks = int(input('Please enter marks in "{}" out of 100: '.format(subjects[i])))
	mark_list.append(marks)

print(get_grade(mark_list))

