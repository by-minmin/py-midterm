a = int(input("輸入月租費型式 : "))
b = int(input("輸入通話時間 : "))
if a == 386:
    if b <386/0.08:
        print("通話費為 : ",a)
    elif b >386/0.08 and b<=(386/0.08*2):
        print("通話費為 : ",b*0.08*0.8)
    else:
        print("通話費為 : ",round(b*0.08*0.7,0))