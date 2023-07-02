"""
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.
"""

def add_bin(a, b):
  return bin(a + b)[2:]

print(add_bin(map(int, input().split())))
