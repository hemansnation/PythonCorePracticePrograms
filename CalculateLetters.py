def sentence(s):
    a=0
    d=0
    for i in s:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            d += 1

    print("LETTERS : ", str(a)+" DIGITS : ", str(d))

a=input("Enter a sentence : ")
sentence(a)
