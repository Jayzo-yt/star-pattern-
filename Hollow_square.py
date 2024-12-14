def Hollow_square(x):
    for i in range(x):
        if i==0 or i==x-1:
            print("*"*x)
        else:
            print("*"+" "*(x-2)+"*")

Hollow_square(int(input("Enter the size : ")))