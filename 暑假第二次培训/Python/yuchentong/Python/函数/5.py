def func(l):
    if isinstance(l,list):
        sum1=0
        for i in l:
            if isinstance(i,int) or isinstance(i,float):
                sum1+=i
        return sum1
    elif isinstance(l,tuple):
        sum2=1
        for  i in l :
            if isinstance(i,int) or isinstance(i,float):
                sum2*=i
        return sum2

l=(0,1,2,3,'aaa','c',1)
print(func(l))