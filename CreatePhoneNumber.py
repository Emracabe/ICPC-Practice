def create_phone_number(n):
	code = ''.join([str(number) for number in n[:3]])
	first = ''.join([str(number) for number in n[3:6]])
	second = ''.join([str(number) for number in n[6:]])
	return f"({code}) {first}-{second}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))