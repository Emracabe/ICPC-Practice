"""
	Problem: 
	Julie is x years older than her brother, and she is also y times as old as him.

		Given x and y calculate Julie's age using the function age(x, y).

		For example:

		age(6, 3) #returns 9
		Note also that x can be negative, and y can be a decimal.

		age(-15, 0.25) #returns 5
		That is, Julie is 15 years younger and 0.25 times the age of her brother.
"""

def calculateAge(x, y):
	return round(abs((x * y) / (y - 1)))

if __name__ == '__main__':

	x, y = map(float, input().rstrip().split())
	print(calculateAge(x, y))