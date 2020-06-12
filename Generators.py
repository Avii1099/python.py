def ten():
    n=1
    while n<=10:
        num = n
        yield num
        n+=1
t = ten()
for i in t:
    print(i)

