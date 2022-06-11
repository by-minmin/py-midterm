a = int(input("請輸入西元年 : "))
b = a%12-3
if b ==1:
    print("rat")
elif b == 2:
    print("ox")
elif b == 3:
    print("tiger")
elif b == 4:
    print("rabbit")
elif b == 5:
    print("dragon")
elif b == 6:
    print("snake")
elif b == 7:
    print("horse")
elif b == 8:
    print("sheep")
elif b == 9:
    print("monkey")        
elif b == 10:
    print("rooster")
elif b == 11:
    print("dog")            
elif b == 0:
    print("pig")