try:
    a = float(input("Введите число:"))
    while True:
        oper = input("Операция над числом: ").split()
        if oper[0]=="+":
            a+=float(oper[1])
        elif oper[0]=="-":
            a-=float(oper[1])
        elif oper[0]=="*":
            a*=float(oper[1])
        elif oper[0]=="":
            a=float(oper[1])
        elif oper[0]=="/":
            a/=float(oper[1])
        elif oper[0]=="%":
            a%=float(oper[1])
        elif oper[0]=="=":
            print(f"{a}")
            break
except ValueError:
    print("Неверный ввод")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
