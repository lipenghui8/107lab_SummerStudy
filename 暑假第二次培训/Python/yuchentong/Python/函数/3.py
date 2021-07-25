def sub_sum(l):
    sum1=0
    sum2=0
    i=0
    for m in l:
        if i%2==0:
            sum2+=m
        else:
            sum1+=m
        i+=1
    return sum1,sum2

l=[1,2,3,4,5,6,7,8,9,10,11,12]
sum1,sum2=sub_sum(l)
print(sum1,sum2)