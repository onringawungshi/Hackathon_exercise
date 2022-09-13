def divisible(a):
    i=0
    sum=""
    while i<len(a):
        sum=sum+str(a[i]%10)
        i+=1
    if int(sum)<=0:
        print(int(sum)%10)
    elif int(sum)%10==0:
        print("Yes",sum)
    elif int(sum)%10!=0:
        print("No",sum)      
divisible((80, 20, 60, 20, 80))