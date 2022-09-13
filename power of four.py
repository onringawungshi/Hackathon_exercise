def power_four(user):
    if user%4**2==0:
        return True
    elif user==1:
        return True
    else:
        return False
print(power_four(int(input("enter number:"))))