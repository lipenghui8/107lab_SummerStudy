def average(*args):
    if len(args)==0:
        return 0
    else:
        sum = 0
        for item in args:
            sum += item
        avg = sum / len(args)
        return avg
print(average())
print(average(1,2,3,4,5))