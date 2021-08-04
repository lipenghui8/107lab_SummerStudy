class Fib():
    def __init__(self):
        pass
    def __call__(self, num):
        a=0
        b=1
        li=[0,1]
        i=2
        while i<10:
            c=a
            a=b
            b=c+b
            li.append(b)
            i+=1
        return li
f=Fib()
print(f(10))