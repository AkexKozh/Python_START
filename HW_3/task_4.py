"""
Написать программу по переводу целого числа из десятичной системы счисления в двоичную.

Ввод: значение типа <int>
Вывод: значение типа <int>

Примеры:
45
101101

3
11

2
10
"""



num = int(input("Введите целое десятичное число: "))
double_num = ''
while num > 0:
    double_num = str(num % 2) + double_num
    num //= 2
print(f"Введенное число в двоичной системе: {double_num}")