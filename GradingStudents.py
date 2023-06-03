import math
import os
import random
import re
import sys

def nearestMultipleFive(number):
	return math.ceil(number / 5) * 5

def gradingStudents(grades):
	final_grades = []

	# loop through the grades list
	for grade in grades:

		# check first, if the grade is below 38
		if grade < 38:
			final_grades.append(grade)
		elif nearestMultipleFive(grade) - grade < 3:
			final_grades.append(nearestMultipleFive(grade))
		else:
			final_grades.append(grade)

	return final_grades


if __name__ == '__main__':
	grades_count = int(input().strip())

	grades = []

	for _ in range(grades_count):
		grades_item = int(input().strip())
		grades.append(grades_item)

	result = gradingStudents(grades)

	print(*result, sep='\n')