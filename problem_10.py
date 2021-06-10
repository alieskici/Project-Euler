"""
Summation of primes
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

This is actually a fast prime number scan algorithm question
So we will use Eratosten formula
"""
"""
n = []
for i in range(2000001):
    n.append(False)

p = [2]
t = 2

for i in range(3, 2000001, 2):
    if n[i] == False:
        p.append(i)
        t += i
        for j in range(i*2, 2000001, i):
            n[j] = True

print(t)