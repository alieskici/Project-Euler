
"""
Double-base palindromes
https://projecteuler.net/problem=36
"""
# find primes until 1 million
# Eratosten Method

def P(a): return a == a[::-1]


until = 1_000_000
t = 0
for i in range(until):
    if P(str(i)):
        if P(bin(i)[2:]):
            t += i
print(t)