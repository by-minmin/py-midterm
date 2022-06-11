a = int(input("請輸入變數n : "))
print(a, end=" ")

while a != 1 and a > 0 and a < 1000000:
    if a % 2 != 0:
        a = a * 3 + 1
        print("%d" %a , end=" ")
    elif a % 2 == 0:
        a = a / 2
        print("%d" %a , end=" ")    
