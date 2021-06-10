
"""
Permuted multiples
https://projecteuler.net/problem=52
"""

from datetime import datetime
from itertools import permutations

a = []
for i in range(1, 10):
    a.append(str(i))

per = permutations(a, 6)
start = datetime.now()
for i in per:
    if i[0] == "1":
        numSTR1 = ""
        for j in i:
            numSTR1 += j

        for n in range(2, 7):
            numSTRX = str(int(numSTR1) * n)
            err = False
            for k in range(len(numSTRX)):
                if numSTR1.find(numSTRX[k]) == -1:
                    err = True
                    break
            if err == True:
                break
        if err == False:
            break
if err == False:
    print(numSTR1, end=' ')
    for i in range(2, 7):
        print(int(numSTR1)*i, end=' ')
print()
print(datetime.now() - start)