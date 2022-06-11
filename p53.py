a = int(input("請輸入n值 : "))
dict1={}

for i in range(a):
    na = input("請輸入姓名：")
    mail = input("請輸入電子郵件:")
    dict1[na]= mail

find = input("請輸入要查詢的電子郵件姓名 : ")
print(find," 電子郵件帳號為 ",dict1.get(find))     