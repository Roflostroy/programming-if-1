#1
print('Задание 1')
a,b = float(input("Введите a: ")), float(input("Введите b: "))
if a>=0:
    print(round(a**2, 4))
    if b>=0:
        print(round(b**2, 4))
#2
print('Задание 2')
x,y = int(input("Введите x: ")), int(input("Введите y: "))
if x > 0 and y > 0:
    print("Четверть 1")
elif x > 0 and y < 0:
    print("Четверть 4")
elif x < 0 and y < 0:
    print("Четверть 3")
elif x < 0 and y > 0:
     print("Четверть 2")
elif x == 0 and y  == 0:
    print('начало координат')
elif y == 0 and x != 0:
    print('Ось OX')
elif x == 0 and y != 0:
    print('Ось OY')
#3
print('Задание 3')
x = int(input("Введите x: "))
if x > 999 or x < 1:
    print("Ошбика условия")
else:
    if x % 2 == 0:
        print('Число чётно')
    else:
        print('Число нечётно')
    if x < 10:
        n = 1
    elif x < 100:
        n = 2
    else:
        n = 3
    print("Цифр: ",n)
    
