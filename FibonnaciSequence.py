"""
	Problem: 
		Write a function that generates the Fibonacci sequence up to a given number n. 
		The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
"""

n = int(input())

def generate_fibonacci_sequence(n):
	sequence = [0, 1]

	for i in range(n):
		sequence.append(sequence[i] + sequence[i + 1])

		if (sequence[-1] > n):
			sequence.pop()
			break

	return sequence



print(generate_fibonacci_sequence(n))