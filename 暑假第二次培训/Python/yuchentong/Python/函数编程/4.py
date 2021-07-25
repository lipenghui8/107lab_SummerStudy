import _functools
import math
def issqrt(n):
    m=int(math.sqrt(n))
    return n==m*m
for item in filter(issqrt,range(1,101)):
    print(item)