'''
	Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

	EXAMPLES:
		pig_it('Pig latin is cool') # igPay atinlay siay oolcay
		pig_it('Hello world !')     # elloHay orldway !
'''

def formatter(text):
	if len(text) == 1 and text.upper() in ['A', 'E', 'I', 'O', 'U']:
		return f"{text}ay"
	elif len(text) == 1:
		return text
	return f"{text[1:]}{text[0]}ay"

def pig_it(text):
	text_array = text.split()
	pig_array = list(map(formatter, text_array))
	return ' '.join(pig_array)

if __name__ == '__main__':
	text = input()

	print(pig_it(text))


'''
	CLEVER SOLUTIONS:
	def pig_it(text):
	    lst = text.split()
	    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
'''