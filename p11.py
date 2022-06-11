m = int(input("輸入月 : "))
d = int(input("輸入日 : "))

if m > 12 or d > 31 or d < 1:
    print("輸入有誤!")
else:
    if m == 1:
        if d <= 20:
            print("星座為 魔羯 ")
        else:
            print("星座為 水瓶 ")
    elif m == 2:
        if d <= 18:
            print("星座為 水瓶 ")
        else:
            print("星座為 雙魚 ") 
    elif m == 3:
        if d <= 20:
            print("星座為 雙魚 ")
        else:
            print("星座為 牡羊 ")
    elif m == 4:
        if d <= 20:
            print("星座為 牡羊 ")
        else:
            print("星座為 金牛 ")
    elif m == 5:
        if d <= 21:
            print("星座為 金牛 ")
        else:
            print("星座為 雙子 ")
    elif m == 6:
        if d <= 21:
            print("星座為 雙子 ")
        else:
            print("星座為 巨蟹 ")
    elif m == 7:
        if d <= 22:
            print("星座為 巨蟹 ")
        else:
            print("星座為 獅子 ")
    elif m == 8:
        if d <= 23:
            print("星座為 獅子 ")
        else:
            print("星座為 處女 ")
    elif m == 9:
        if d <= 23:
            print("星座為 處女 ")
        else:
            print("星座為 天秤 ")
    elif m == 10:
        if d <= 23:
            print("星座為 天秤 ")
        else:
            print("星座為 天蠍 ")
    elif m == 11:
        if d <= 22:
            print("星座為 天蠍 ")
        else:
            print("星座為 射手 ")
    elif m == 12:
        if d <= 21:
            print("星座為 射手 ")
        else:
            print("星座為 魔羯 ")                                                                                              

            