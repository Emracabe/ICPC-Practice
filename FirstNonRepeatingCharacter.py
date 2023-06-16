"""
	Description:
		Write a function named first_non_repeating_letter that takes a string input, 
		and returns the first character that is not repeated anywhere in the string.

		For example, if given the input 'stress', the function should return 't', 
		since the letter t only occurs once in the string, and occurs first in the string.

		As an added challenge, upper- and lowercase letters are considered the same character, 
		but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

		If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""

def first_non_repeating_letter(s):
    # Count the occurrences of each character
    char_count = {}
    for char in s:
        # Consider case-insensitivity by converting to lowercase
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1

    # Find the first non-repeating character with the correct case
    for char in s:
        char_lower = char.lower()
        if char_count[char_lower] == 1:
            return char

    return ""  # Return an empty string if all characters are repeating or the input string is empty


if __name__ == '__main__':
	text = input()

	print(first_non_repeating_letter(text))

"""
	CLEVER SOLUTIONS:

	def first_non_repeating_letter(string):
	    string_lower = string.lower()
	    for i, letter in enumerate(string_lower):
	        if string_lower.count(letter) == 1:
	            return string[i]
	            
	    return ""

	def first_non_repeating_letter(string):
	    s = string.lower()
	    
	    for i in string:
	        if s.count(i.lower()) == 1:
	            return i
	    return ''

"""