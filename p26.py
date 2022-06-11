a = 0

while a == 0 :
    s1 = str(input("要檢測的字串(end 結束) : "))
    s1.split(" ")
    if a == "end" or a == "END":
        break
    else:
        p1 = str(input("檢測的單一字元 : "))
        p2 = s1.count(p1)
        print("字元 ",p1," 出現次數為 ",p2)