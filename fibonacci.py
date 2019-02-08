fib_series=[1,1]
num=int(input("length of fibonacci?"))

if num>2:
    while num>2:
        fib_series.append(fib_series[-1]+fib_series[-2])
        num=num-1
    print(fib_series)
elif num==2:
    print([1,1])
else:
    print([1])