def lenfun():
    i=0
    c=0
    while i<len(b):
        c+=1
        i+=1
    return c
user=int(input("enter numbers:"))
a=str(user)
b=list(a)
print(lenfun())