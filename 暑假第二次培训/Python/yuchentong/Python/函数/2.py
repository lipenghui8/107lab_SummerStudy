def square_of_sum(l):
    result=0
    for i in l:
        result+=i*i
    return result
l=[1,2,3,4,5,6,7,8,9,10]
print(square_of_sum(l))