def reverseArray(a):
	print(*a[::-1])

arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))

reverseArray(arr)