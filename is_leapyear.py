#find a year is leap year or not.

def is_leap(year):

	if year%4 == 0 or (year%100 == 0 and year%400 == 0):
		print("{} is leap year".format(year))

	else:
		print("{} is not leap year".format(year))


year = 2020
is_leap(year)