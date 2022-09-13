def battery(user):
    if user<=15:
        print("Yes,your battery is low")
    else:
        print("No")
battery(int(input("enter battery percent.")))
