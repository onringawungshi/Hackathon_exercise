l1=[7,2,4,3]
l2=[5,6,4]
i=0
s=''   
while i<len(l1):
    s=s+str(l1[i])
    i+=1
sum=''   
j=0
while j<len(l2):
    sum=sum+str(l2[j])
    j+=1
total=int(sum)+int(s)
a=str(total)
b=list(a)
d=[]
k=0
while k<len(a):
    d.append(int(a[k]))
    k+=1
print(d)



# l1=[2,4,8]
# l2=[5,6,2]
# i=-1
# s=''
# sum=''
# while i>-len(l1)-1:
#     s=str(s)+str(l1[i])
#     sum=str(sum)+str(l2[i])
#     i-=1
# total=int(s)+int(sum)
# a=str(total)
# b=list(a)
# d=[]
# k=-1
# while k>-len(a)-1:
#     d.append(int(a[k]))
#     k-=1
# print(d)