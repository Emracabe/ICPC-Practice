"""
	Write a function that checks whether two strings are anagrams of each other. 
	Anagrams are strings formed by rearranging the letters of another string.
"""

def anagram_checker(first_string, second_string):

	for letters in first_string:
		if letters not in second_string:
			return "false"

	return "true"

iput = input().split()
print(anagram_checker(iput[0], iput[1]))