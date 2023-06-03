def find_short(s):
	return min([len(string) for string in s.split()])

string = input()
print(find_short(string))