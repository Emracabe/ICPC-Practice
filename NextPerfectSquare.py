import math

def find_next_square(sq):
	return -1 if math.sqrt(sq) == 0 else (round(math.sqrt(sq)) + 1) ** 2 


print(find_next_square(int(input())))