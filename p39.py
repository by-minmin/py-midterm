a = int(input("輸入一個數: "))
for i in range(a+1):
        print(' '*(a-i)+'*'*(2*i-1))
for i in range(a,0,-1):
        print(' '*(a-i)+'*'*(2*i-1))
