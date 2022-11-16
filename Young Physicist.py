"""
Author: Emmar Caber
Problem can be found in the link below:
    http://codeforces.com/problemset/problem/69/A
"""

N = int(input())

new_list = []
for i in range(N):
    new_list.append(list(map(int, input().split())))

sum_x = sum_y = sum_z = 0

for i in new_list:
    sum_x += i[0]
    sum_y += i[1]
    sum_z += i[2]
    
print("YES" if sum_x == 0 and sum_y == 0 and sum_z == 0 else "NO")