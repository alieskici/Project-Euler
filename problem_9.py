
"""
Special Pythagorean triplet
https://projecteuler.net/problem=9
"""

#first values can be max:
a = 332
b = 333
c = 335

for i in range(332):
    a -= 1
    b = a

    while True:
        b += 1
        c = 1000 - (a + b)
        if b < c:
            if a ** 2 + b ** 2 == c ** 2:
                print(a*b*c)
                break
        else:
            break