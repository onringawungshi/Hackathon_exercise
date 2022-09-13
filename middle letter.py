def middle_letter():
    i=0
    while i<len(a):
        if len(a)%2==0:
            return "''"
        else:
            b=len(a)//2
            return a[b]
        i+=1
us=str(input("enter word:"))
a=list(us)
print((middle_letter()))