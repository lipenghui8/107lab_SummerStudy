i=0
sum=0
while i<1000:
    if(i%2!=0):
        i+=1
        continue
    sum+=i
    i+=1
print(sum)
