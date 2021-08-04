# Enter a code
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = set([1, 3, 5, 7, 9, 11])
for i in L:
    if i in S:
        S.remove(i)
    else:
        S.add(i)
print(S)