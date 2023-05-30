def prime_number_checker(n):
	for i in range(2, n):
		# print(i)
		if n % i == 0:
			return "false"

	return "true"

n = int(input())

print(prime_number_checker(n))