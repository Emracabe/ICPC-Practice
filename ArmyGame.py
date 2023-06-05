import math
import os
import random
import re
import sys

def gameWithCells(n, m):
	if n == 1 and m == 1:
		return 1
	else:
		return math.ceil(n / 2) * math.ceil(m / 2)

if __name__ == '__main__':

	rows, columns = map(int, input().rstrip().split()) # 2 2

	print(gameWithCells(rows, columns)) 