u=int(input("enter no.of chocolate you need:"))
u1=int(input("enter no. of chocolate you have:"))
if u>=u1:
    u2=int(input("enter cost of one chocolate:"))
    a=u-u1
    print(a*u2)
else:
    print("You have enough chocolate")