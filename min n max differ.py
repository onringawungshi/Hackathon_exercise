def min_max(a):
    j=0
    m,s=0,a[j]
    while j<len(a):
        if m<a[j]:
            m=a[j]
        elif a[j]<s and m>s:
            s=a[j]
        j+=1
    b=m-s
    return b
print(min_max([12,34,45,67,89]))