"""
Largest palindrome product
https: // projecteuler.net / problem = 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def P(a): return a == a[::-1]

enb = 0
n = ""
s = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        s = i*j
        n = str(s)
        if P(n):
            if s > enb:
                enb = s
    if P(n):
        break
print(enb)