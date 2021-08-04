# Enter a code
from functools import reduce

def calc_prod(list_):
    def lay_prod():
        return reduce(lambda d,n:d*n,list_,1)
    
    return lay_prod

f = calc_prod([1,2,3,4])
print(f())