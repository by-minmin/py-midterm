a = int(input("小狗可能跑到的地方 : "))
c = 0

for i in range(a):
    km = int(input("與家的距離 : "))
    if a >= 2 and a <= 10 :
        if km % 9 == 0 or km % 11 == 0:
            c = c + 1
            print("第 ",c," 個點",km)     