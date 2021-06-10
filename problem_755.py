# Project Euler Solutions by Ali Eskici
# Not Zeckendorf - 755

"""According to the given sigma formula, for f[i] <= n < f[i+1];
if we do iterations: s[n] = s[n - f[k]] - s[f[k+1] - n - 3] + 2**(k-1)
where k; It is the index of the Fibonacci number closest to n."""

n = 10**13

f = [1, 2]
while f[-1] < n:
    f.append(f[-2]+f[-1])

sT = [1, 2, 3, 5, 6]


def Findk(k):
    c = 0
    while k >= f[c]:
        c += 1
    return c-1


def s(n):
    d = 4
    while len(sT) < n:
        d += 1
        k = Findk(d)
        sT.append(sT[d - f[k]] - sT[f[k+1] - d - 3] + 2**(k-1))
    return sT[-1]


print(s(10**13))
