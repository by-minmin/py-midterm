a = float(input("請輸入路程公里數(km) : "))

if a > 1.5:
    if a-1.5 <= 0.25:
        print("所需車資為 : ",75+5)
    elif a-1.5 > 0.25:
        if (a-1.5)%0.25 != 0 :
            m = (a-1.5) // 0.25 + 1 
            print("%d" % (m*5+75))
        else:
            m = (a-1.5) // 0.25 
            print("%d" % (m*5+75))
else:
    print("所需車資為 : ",75)