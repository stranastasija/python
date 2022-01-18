# print ('hello world')  вывод 

# a = 123
# b = 1.23
# # print (type(a))
# # print (b)

# s = 'hello world'
# # print (s)   
#                                 0 1 2
# print ('{1} - {2} - {0}'.format(a,b,s))
# print (f'{a} - {b} - {s}')

# list = [1,2,3]
# print (list)

# print ('Введите a')
# a = int(input())
# print ('Введите b')
# b = int(input())
# print (a, b, a+b)

# a = [1, 2] 
# b = [2, 3]
# print (a==b)

# a = 1 < 3 < 5
# print (a)

# f = 1 > 2 or 4 < 6
# t = [1, 2, 3, 4]
# print (f)
# print (not 2 in t)

# f = [1, 2, 3, 4]
# is_odd = f[0] % 2 == 0
# print (is_odd)


# a = int (input('a = '))
# b = int (input('b = '))
# if a > b:
#     print (a)
# else:
#     print (b)

# username = input ('Введите свое имя: ')
# if username == 'Маша':
#     print ('Привет, дорогая Маша!')
# elif username == 'Настя':
#     print ('Ура, Настя, привет!')
# elif username == 'Ильнар':
#     print ('Ильнар - топ')
# else:
#     print ('Привет, ', username)

                    # перевернутое число
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print ('Пожалуй')
#     print ('хватит ')
# print (inverted)

# цикл со "счетчиком" i
# list = [1,3,6,2,10]
# for i in list:
#     print (i**2)

# range (10) - выводит все числа от 0 до 9, 
# range (1, 9, 2) - выводит все числа от 1 до 9 с приращением на 2, т.е. 1 3 5 7
# for i in range(1, 9, 2):
#     print (i)
# 
#  функция
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return 

arg = 2.3
print (f(arg))
print (type(f(arg)))        