import math

#return number of a reversed number
def R(A): return int(str(A)[::-1])

#return bool if a string is a palindrom
def isPalindrom(a): return a == a[::-1]

# factors of n
def f(n):
    s = int(math.sqrt(n))
    f = []
    for i in range(1, s+1):
        if n % i == 0:
            f.append(i)

    a = len(f) - 1
    if f[a] * f[a] == n:
        a -= 1

    while a > -1:
        f.append(int(n / f[a]))
        a -= 1

    return f

# prime factors of a
def pf(a):
    b = []
    c = f(a)
    for i in c:
        if len(f(i)) == 2:
            b.append(i)

    return b


# is 'a' a prime?
def prime(a):
    if len(f(a)) == 2:
        return True
    else:
        return False

#sign of x -fastest method
def isa(x):
    return bool(x > 0) - bool(x < 0)


#find primes until given number
def primes(n):
    sayi = [False] * n
    sayi[2] = True
    asal = []
    asal.append(2)

    for x in range(3, n-1, 2):
        if sayi[x] == False:
            asal.append(x)
            for y in range(x*2, n-1, x):
                sayi[y] = True

    return asal
