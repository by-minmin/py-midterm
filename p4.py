x = int(input("輸入x座標 : "));
y = int(input("輸入y座標 : "));
c=0;

if x > 0 and y>0:
    c = x*x + y*y
    print("該點位於第一象限，離原點距離為根號",c)
elif x < 0 and y > 0:
    c = x*x + y*y
    print("該點位於第二象限，離原點距離為根號",c)
elif x < 0 and y < 0:
    c = x*x + y*y
    print("該點位於第三象限，離原點距離為根號",c)
elif x > 0 and y > 0:
    c = x*x + y*y
    print("該點位於第四象限，離原點距離為根號",c) 
elif x == 0 and y == 0:
    print("該點位於原點")                    
elif x == 0:
    if y > 0:
        c = x*x + y*y
        print("該點位於上半平面Y軸上，離原點距離為根號",c)
    if y < 0:
        c = x*x + y*y
        print("該點位於下半平面Y軸上，離原點距離為根號",c)
elif y == 0:
    if x > 0:
        c = x*x + y*y
        print("該點位於右半平面X軸上，離原點距離為根號",c)
    if x < 0:
        c = x*x + y*y
        print("該點位於左半平面X軸上，離原點距離為根號",c) 


    