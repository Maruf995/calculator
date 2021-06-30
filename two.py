#Пишу Недо-калькулятор)
a_num = int(input("Короче, напиши сюда первое число:"))
print("Выбирай какое действие будет:")
c_input = input("(+,*,/,-)")
b_num  = int(input("Теперь сюда напиши второе число:"))
if c_input == '+':
    print(a_num + b_num)
if c_input == '-':
    print(a_num - b_num)
if c_input == '*':
        print(a_num * b_num)
if c_input == '/':
            print(a_num / b_num)
input()