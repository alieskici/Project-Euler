
"""
Longest Collatz sequence
https://projecteuler.net/problem=14
"""

max = 0
num = 0
for i in range(333333, 1_000_000, 2):
    n = 3 * i + 1
    n /= 2
    proc = 3
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        proc += 1
    if proc > max:
        max = proc
        num = i
print(num)