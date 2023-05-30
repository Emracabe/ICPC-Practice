"""
	Problem:
	Write a function that checks whether a given string is a palindrome. 
	A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
"""

def palindrome_checker(string):
	return string == string[::-1]

print("true" if palindrome_checker(input()) else "false")