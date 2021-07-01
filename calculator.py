#Пишу Недо-калькулятор)
while True:
    print("Выбирай какое действие будет:")
    s = input("(+,*,/,-)")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("Сюда напиши первое число:"))
        y = float(input("Теперь сюда напиши второе число:"))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
    else:
        print("Неверный знак операции!")
