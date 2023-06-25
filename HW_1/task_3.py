"""
Напишите программу, которая принимает на вход координаты точки (X и Y) и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Ввод: два значения типа <int>
Вывод: значение типа <int> либо значение типа <str>

Пример:

34
-30
4

2
4
1

-34
0
Точка на отрицательной части оси абсцисс
"""
quarter_number = int(input('Введите номер четверти: '))

if quarter_number == 1:
  print('x > 0 and y > 0')
elif quarter_number == 4:
  print('x > 0 and y < 0')
elif quarter_number == 2:
  print('x < 0 and y > 0')
elif quarter_number == 3:
  print('x < 0 and y < 0')
elif quarter_number < 1 or quarter_number > 4:
    print('Цифра введена некорректно')