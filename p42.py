a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

ans1 = ((-b)+((b**2-4*a*c)**0.5))/(2*a)
ans2 = ((-b)-((b**2-4*a*c)**0.5))/(2*a)

if (b**2)-(4*a*c) > 0:
    print("%d" %ans1,"%d" %ans2)
elif (b**2)-(4*a*c) < 0:
    print("0")
elif (b**2)-(4*a*c) == 0:
    print("%d" %ans1,)      