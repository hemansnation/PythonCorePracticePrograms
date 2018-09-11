def freq(a):
    c={}
    sentence=a.split()
    for w in sentence:
        if w in c:
            c[w] += 1
        else:
            c[w] = 1
    for w in c:
        print(str(w)+" : "+str(c[w]))


s=input("Enter a sentence : ")
freq(s)

