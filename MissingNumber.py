"""
	Problem:
	Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the missing number.
"""

def missing_number(arr):
	arr.sort()

	for i in range(len(arr)):
		if arr[i] + 1 != arr[i + 1]:
			return arr[i] + 1

print(missing_number(list(map(int, input().split()))))