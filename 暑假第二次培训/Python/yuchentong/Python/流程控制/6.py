sum=0
i=1
while True:
    if i%2==0:
        sum+=i
    i+=1
    if i>=1000:
        break
print(sum)