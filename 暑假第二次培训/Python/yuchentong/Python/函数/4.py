def sum1(num):
    i=1
    suma=0
    while i<=num:
        suma+=i
        i+=1
    return suma
def sum2(num):
    if num==1:
        return 1
    return num+sum2(num-1)

num=100
print(sum1(num))
print(sum2(num))
