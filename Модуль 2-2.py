# Практическoе задание 2-1 : Условная конструкция. Операторы if, elif, else
print('*************')
print()
print('Практическoе задание 2-1 : Условная конструкция. Операторы if, elif, else')
print('*************')
print()

# ЗАДАНИЕ  -  применить навыки создания условных конструкций и знания операторов if, else, elif / and, or, not
print(' Введите последовательно любые три  целых числа')
print()
# Организуем ввод чисел с клавиатуры
first = int (input('Введите 1-е целое число: '))
second = int (input('Введите 2-е целое число: '))
third = int (input('Введите 2-е целое число: '))

# проверяем условие совпадения всех чисел
if first == second and  first == third:
     print('Итого совпадений : ', 3)
# Проверяем совпадение второго с первым или второго с третьим
elif second == first or second == third:
    print('Итого совпадений : ', 2)
# Проверяем совпадение третье с первым или вторым
elif  third == second or third == first:
    print('Итого совпадений : ', 2)
else:
    print('Итого совпадений : ', 0)





