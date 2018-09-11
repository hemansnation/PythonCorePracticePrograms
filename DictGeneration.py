def dic(a):
    d={}
    for i in range(1,a+1):
        d[i]=i*i
    return d

n=int(input("Enter a number : "))
print(dic(n))
