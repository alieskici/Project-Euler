
"""
Triangular, pentagonal, and hexagonal
https://projecteuler.net/problem=45
"""

from datetime import datetime

# t +1, p +3, h +4
t = 40755
dt = 286

p = 40755
dp = 496

h = 40755
dh = 573

found = False

start = datetime.now()

while found == False:
    h += dh
    while True:
        if p < h:
            p += dp
            if p == h:
                while True:
                    if t < h:
                        t += dt
                        if t == h:
                            print(t)
                            found = True
                            break

                        dt += 1
                    if t > h:
                        break
            dp += 3
        if p > h:
            break
        if found:
            break
    if found:
        break
    dh += 4

print(datetime.now() - start)