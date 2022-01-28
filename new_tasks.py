# from random import randint
# print (randint (1, 10))

# Семинар 1-2: примерный список задач
# 1.По двум заданным числам проверить является ли одно квадратом второго 

# def kvadrat(a,b):
#     if b * b == a: 
#         return a, 'квадрат', b
#     else:
#         return a, ' не является квадратом ', b

# print(kvadrat(3,9))

# 2.Найти максимальное из пяти чисел

# import random

# a = random.randint (0, 10)
# b = random.randint (0, 10)
# c = random.randint (0, 10)
# d = random.randint (0, 10)
# e = random.randint (0, 10)

# print (a, b, c, d, e)

# if a >= b and a >= c and a >= d and a >= e: print (a, 'максимальное число')
# elif b >= a and b >= c and b >= d and b >= e: print (b, 'максимальное число') 
# elif c >= a and c >= b and c >= d and c >= e: print (c, 'максимальное число')
# elif d >= a and d >= b and d >= c and d >= e: print (d, 'максимальное число')
# elif e >= a and e >= b and e >= c and e >= d: print (e, 'максимальное число')

# 3.Вывести на экран числа от -N до N

# def chislaN(N):
#     for i in range (-N, N+1):
#         print (i)

# chislaN(3)

# 4.Показать первую цифру дробной части числа

# def firstChislo(a):
#     if a % 2 == 0: 
#         return 'Сгенерированное число делится на 2 без остатка и дробной части.'
#     else: 
#         return 'Дробная часть =', a%10

# print (firstChislo(15))

# 5.Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# def kratno(b):
#     if b % 5 == 0 and b % 10 == 0:
#         print ( b, 'кратно 5 и 10')
#     else:
#         print (b, 'не кратно 5 и 10')

# def kratno2(a):
#     if a % 15 == 0 and a % 30 != 0:
#         print (a, 'число делится на 15 и не делится на 30')
#     else:
#         print ('По условию необходимо число, которое будет делиться на 15, но не на 30')

# kratno(50)
# kratno2(30)

# 6.Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# N = input ('Введите номер сегодняшнего дня - ')

# def nedelya(N):
#     if N == '1':
#         print ('Первый день недели - понедельник')
#     elif N == '2':
#         print ('Второй день недели - вторник')
#     elif N == '3':
#         print ('Третий день недели - среда')
#     elif N == '4':
#         print ('Четвертый день недели - четверг')
#     elif N == '5':
#         print ('Пятый день недели - пятница')
#     elif N == '6':
#         print ('Шестой день недели - суббота')
#     elif N == '7':
#         print ('Седьмой жень недели - воскресенье')
#     elif N < '1' or N > '7':
#         print ('Ваше число не подходит. Неделя от 1 до 7 дней.')

# nedelya(N)

# 7.Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# def TR (x, y, z):
#     return (not(x or y or z)) == ((not x) and (not y) and (not z)) 
# print (TR(0,0,0))
# print (' ')

# for x in range (0, 2):
#     for y in range (0, 2):
#         for z in range (0, 2):
#             print (TR(x,y,z))

# 8.Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

# X = input ('Введите число X: ')
# Y = input ('Введите число Y: ')

# def chetvert (X, Y):
#     if X>'0' and Y>'0': print ('1 четверть') 
#     elif X<'0' and Y>'0': print ('2 четверть')
#     elif X<'0' and Y<'0': print ('3 четверть')
#     elif X>'0' and Y<'0': print ('4 четверть')

# chetvert(X,Y)

# 9.Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

# a = input ('Введите число от 1 до 4, чтобы узнать диапозон четверти: ')

# def chetvert (a):
#     if a == '1': print ('Диапозон 1 четверти: X: от 0 до +бесконечности, Y: от 0 до +бесконечности.')
#     elif a =='2': print ('Диапозон 2 четверти: X: от -бесконечности до 0, Y: от 0 до +бесконечности.')
#     elif a == '3': print ('Диапозон 3 четверти: X: от -бесконечности до 0, Y: от -бесконечности до 0.')
#     elif a == '4': print ('Диапозон 4 четверти: X: от 0 до +бесконечности, Y: от -бесконечности до 0.')
#     elif a < '1' or a > '4': print ('Таких четвертей не существует.')

# chetvert(a)

# 10.Найти расстояние между двумя точками пространства

# import math
# def rasstoyanie (D, A, B):
#     distance = 0;
#     if (D == 2):
#         distance = math.sqrt(math.pow((B[0] - A[0]), 2) + math.pow((B[1] - A[1]), 2));
#     if (D == 3):
#         distance = math.sqrt(math.pow((B[0] - A[0]), 2) + math.pow((B[1] - A[1]), 2) + math.pow((B[2] - A[2]), 2));
#     return distance;

# A = {1, 6, 9};
# B = {8, 2, 0};
# print(rasstoyanie(2, A, B));


# from random import randint
# import math

# def coordinat (ose, left, right):
#     return [randint (left, right) for i in range (ose)]

# def rasstoyanie (a, b):
#     return round (math.sqrt (sum((x-y)**2 for x,y in zip(a,b))), 3)

# # колтчество осей координат
# ose = 3    
# left = -10
# right = 10

# A = coordinat (ose, left, right)
# B = coordinat (ose, left, right)

# print (f'A {A}, B {B}')
# print (f'Расстояние: {rasstoyanie(A, B)}')

# Семинар 3-4: примерный список задач
# 11.Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

# def mnozhestvo (N):
#     mn = []
#     for i in range (N):
#         if i == 0:
#             mn.append(1)
#         elif i % 2 != 0:
#             mn.append (-3**i)
#         else:
#             mn.append (3**i)
#     return mn

# print(mnozhestvo(6))

# 12.Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.



# 13.Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.

# def stroka (one, two):
#     if two in one:
#         count = 0
#         setting = ''
#         for i in range (len (one) - len (two) + 1):
#             for j in range (len (two)):
#                 setting = setting + one [i+j]
#             if setting == two:
#                 count += 1
#             setting = ''
#         return count, ' раз повтор строки' 
#     else:
#         return 'Строки, которую Вы ищете, нет в изначальной строке.'

# one = input('Введите изначальную строку: ')
# two = input ('Введите строку, которую будете искать: ')

# print (stroka (one, two))

# 14/0. Посчитать сумму цифр в натуральном числе.

# import random
# x = random.randint (100, 1000)

# def sum (N):
#     print (N)
#     a = str (N)
#     res = 0
#     for i in range (0, len(a)):
#         res += int (a[i])
#     return res

# print (sum (x))

# 14.Подсчитать сумму цифр в вещественном числе.

# x = 40.195

# def sum (N):
#     print (N)
#     a = str (N)
#     res = 0
#     for i in a:
#         if i != '.':
#             res += int(i)
#     return res

# print (sum (x))

# 15.Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# def pr (N):
#     x = 1
#     result = []
#     for i in range (1, N+1):
#         x = i*x
#         result.append(x)
#     return result

# print (pr(5))

# 16.Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму



# 17.Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число



# 18.Реализовать алгоритм перемешивания списка. 
# Один список, в котором между собой будут меняться элементы.

# from random import *

# # array = [randint(1, 10) for i in range (10)]    здесь числа в перемешку
#                                                 # здесь числа по порядку от 0 до 9
# array = [i for i in range(10)]                  
# print (array)

# def algoritm (x):
#     for i in range (len (x) - 1):
#         number = x[i]
#         index = randint (i+1, len (x) - 1)
#         x[i] = x[index]
#         x[index] = number
#     return x

# print (algoritm(array))

# 19.Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

# import datetime

# def random ():
#     return datetime.datetime.now().microsecond%10

# print (random())

# 20.Определить, присутствует ли в заданном списке строк, некоторое число 


