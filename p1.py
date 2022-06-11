a = int(input("請輸入正整數 : "))
ans = []

for i in range(2,a):
    if a % i == 0 :
        print("No prime found")
        break
    elif i == a-1 :
        ans.append(i+1)
print(ans)        