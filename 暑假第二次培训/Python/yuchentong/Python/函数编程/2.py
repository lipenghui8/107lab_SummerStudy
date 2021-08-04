def upp(s):
    l=s[0].upper()+s[1:].lower()
    return l
names=['alice', 'BOB', 'CanDY']
for s in map(upp,names):
    print(s)