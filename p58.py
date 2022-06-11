a = list()

for i in range(10):
    b = input("請輸入第{}個數字 : ".format(i+1))
    a.append(int(b))
max1 = sorted(a,reverse=True)
min1 = sorted(a,reverse=False)

print("最大的3個數字為 : ",max1[0],max1[1],max1[2])
print("最小的3個數字為 : ",min1[0],min1[1],min1[2])
