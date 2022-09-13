user=int(input("enter no. of players:"))
amount=1000
a=[]
i=0
while i<user:
    u=int(input("enter no."))
    a.append(u)
    i+=1
j=0
while j<len(a):
    m,s=0,a[j]
    if m<a[j]:
        m=a[j]
    elif a[j]<s and m>s:
        s=a[j]
        a.remove(s)
    amount=amount+1000
    j+=1