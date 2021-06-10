from datetime import datetime

"""
Highly divisible triangular numberhttps://projecteuler.net/problem=755
https://projecteuler.net/problem=12
"""

def f(n):
    s = int(math.sqrt(n))
    f = []
    for i in range(2, s):
        if n % i == 0:
            f.append(i)

    a = len(f) - 1
    if f[a] * f[a] == n:
        a -= 1

    while a > -1:
        f.append(int(n / f[a]))
        a -= 1

    return f


inc = 3680
num = 6773040
div = []

start = datetime.now()

while len(div) < 500:
    inc += 1
    num += inc

    if num % 2 == 0:
        div = []
        div = f(num)


print(num)
print((datetime.now() - start))