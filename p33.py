a = int(input("國文 : "))
b = int(input("英文 : "))
c = int(input("微積分 : "))
d = int(input("體育 : "))
e = int(input("程式設計 : "))
sum1 = a+b+c+d+e
ans = round(sum1/5,2)
print("平均分數 : ",ans)

if a > b and a > c and a > d and a > e:
    print("最高分科目 : 國文 ",a)
elif b > a and b > c and b > d and b > e:
    print("最高分科目 : 英文 ",b)
elif c > a and c > b and c > d and c > e:
    print("最高分科目 : 微積分 ",c)
elif d > a and d > b and d > c and d > e:
    print("最高分科目 : 體育 ",d)
elif e > a and e > b and e > c and e > d:
    print("最高分科目 : 程式設計 ",e)

if a < b and a < c and a < d and a < e:
    print("最低分科目 : 國文 ",a)
elif b < a and b < c and b < d and b < e:
    print("最低分科目 : 英文 ",b)
elif c < a and c < b and c < d and c < e:
    print("最低分科目 : 微積分 ",c)
elif d < a and d < b and d < c and d < e:
    print("最低分科目 : 體育 ",d)
elif e < a and e < b and e < c and e < d:
    print("最低分科目 : 程式設計 ",e)                            

