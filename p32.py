m = input("小明身上有幾元 : ")
d = int(input("販賣機有幾種飲料 :"))
c = 0

for i in range(d):
    p = input("輸入價錢 : ")
    if m >= p :
        c = c + 1
print(c)            