l=[]
o=[]
z=[]
sum=0
for i in range(900,1000):
    l.append(i)
for a in range(0,100):
    for b in range(a+1,100):
        n=l[a]*l[b]
        z.append(n)
for j in range(0,len(z)):
        c = ''.join(reversed(str(z[j])))
        if c==str(z[j]):
            o.append(c)
print("largest palindrome made from the product of two 3-digit numbers : ")
print(o)
print(max(o))
