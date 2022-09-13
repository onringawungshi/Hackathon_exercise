def pretty():
    user=int(input("enter starter no.:"))
    user1=int(input("enter ending no.:"))
    c=0
    while user<=user1:
        if user%10==2 or user%10==3 or user%10==9:
            c+=1
        user=user+1
    print(c)
pretty()