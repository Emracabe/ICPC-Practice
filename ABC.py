'''
ABC
'''
numbers = sorted(map(int, input().split()))
orders = list(input())
order_dict = {
	'A': 0, 
	'B': 1,
	'C': 2
}
print(' '.join([str(numbers[order_dict[o]]) for o in orders]))
