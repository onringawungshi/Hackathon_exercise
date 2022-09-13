def fun(a,b):
    a1=list(a)
    b1=list(b)
    a1.sort()
    b1.sort()
    if len(a1)==len(b1):
        i=0
        while i<len(a1):
          if a1[i]==b1[i]:
            i+=1
            return True
        else:
            return False
    else:
        print("not same lenght")
print(fun("typhoon","opython"))