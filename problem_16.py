# Project Euler Solutions by Ali Eskici
# github.com/alieskici
import time, os
os.system('cls')

"""
Power digit sum
https://projecteuler.net/problem=16
"""

a = str(2**1000)
b=0
for i in range(len(a)):
    b += int(a[i])
print(b)