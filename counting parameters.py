user=int(input("enter length of list"))
i=0
a=[]
while i<user:
    u=input("enter items:")
    a.append(u)
    i+=1
print(len(a))