L = input("输入身份证前14位：")
C1_5 = eval(L[0])*7 + eval(L[1])*9 + eval(L[2])*10 + eval(L[3])*5 + eval(L[4])*8
C6_10 = eval(L[5])*4 + eval(L[6])*2 + eval(L[7])*1 + eval(L[8])*6 + eval(L[9])*3
C11_14 = eval(L[10])*7 + eval(L[11])*9 + eval(L[12])*10 + eval(L[13])*5
L2 = C1_5 + C6_10 + C11_14
duiying = ['1','0','X','9','8','7','6','5','4','3','2']
count = 0
sex = input("请输入性别（男/女）：")

def change(n):
    return "{:0>3}".format(n)

def change2(n):
    global duiying
    return duiying[n]


for i in range(1000):
    t = change(i)
    if sex == "女":
        if eval(t[2]) % 2 == 0:
            sum = L2 + eval(t[0])*8 + eval(t[1])*4 + eval(t[2])*2
            C18 = change2(sum%11)
            print("{:0>3}".format(i)+C18, end = " ")
            count += 1
    elif sex == "男":
        if eval(t[2]) % 2 == 1:
            sum = L2 + eval(t[0])*8 + eval(t[1])*4 + eval(t[2])*2
            C18 = change2(sum%11)
            print("{:0>3}".format(i)+C18, end = " ")
            count += 1
print("\n")
print("共{}个".format(count))
