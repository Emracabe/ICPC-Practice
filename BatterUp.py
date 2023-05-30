x = int(input())
y = list(map(int, input().split()))

z = y.count(-1)

print(sum(y)/(x - z))
