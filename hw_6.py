# num = ('красный',',белый', 'желтый', 'синий', 'серый', 'черный')
# print(set(num))


# num1 = {'акназар','нурболот'}
# num2 = {'эдил','мелис'}
# num3 = num1.union(num2)
# print (num3)


# num = ['сумка', 'кроссовки', 'лего']
# num1 = ['телефон', 'чехол', 'машина']
# num2 = set(num) & set(num1)
# print(num2)


# num = {1,2,4,3,5,6}
# num.add(5)
# print(num)


# num1 = {'карона', 'машина', 'земля', 'телефон', 'телефизор'}
# num2 = {'кружка', 'земля', 'телефон'}
# num3 = {'карона'}
# resilt = set()

# print(num2.issubset(num1))
# print(num1.issubset(num3))

# list1 = set()
# list2 = frozenset()
# list1.add(3)
# print(list1)
# list2.add(1)
# print(list2)

# num = ('Красный','Зеленный', 'Желтый', 'Синий', 'Серый', 'Черный')
# print(frozenset(num))



# num1 = ['камри', 'мерседес', 'бмв']
# num2 = ['серый', 'красный', 'зеленный']
# num3 = frozenset(num1) & set(num2)
# print(num3)


# info1 = {33, 44, 4, 3, 56}
# info2 = {33, 44, 1, 56, 76}
# info3 = info1.difference(info2)
# print(info3)


# frozenset1 = 'ymaraliev'
# frozenset2 = {frozenset1}
# print(frozenset2)



# numbers1 = {2,6,4,9,7}
# numbers1.add(7)
# print(frozenset(numbers1))



# listt = (input('Введите число индекса'))
# listt = ["geeks","Osh","beksultan","Kudbuhan"]
# for num in listt:
#       if num == 'geeks':
#             print(f"{num} - 0")



# listt = ["geeks","bishkek","aknazar"]
# listt = (input('Введите индекса:'))
# if listt == ('geeks'):
#       print(1)
# elif listt == ('bishkek'):
#       print(2)
# elif listt == ('aknazar'):
#       print(3)
# else:
#       print("Ошибка такого текста нету")



# num = (input('Ввод строк'))
# print(type(num))





# info = {'name':'aknazar', 'age': 14, 'favorite color': 'черный','хобби':'играть футбол'}
# info = (input('введите key:'))
# if info == 'name':
#    print('aknazar')
# elif info == 'age':
#    print('14')
# elif info == 'favorite color':
#    print('черный')
# elif info == 'хобби':
#    print('играть фубтол')
# else :
#    print('Простите такого ключа нету')
   

# def sums (*args):
#     numbers = sum(args)
#     print(numbers)
# sums(4,3,5,6,4)



# def argument(*oil):
#     num =",".join(oil)
#     print(num)

# argument('Car','home','drink','eat')


# def num(*args):
#     info = 1
#     for i in args:
#         info *= i 
#     return info
# print(num(1,2,2,3,4,4))


# def num(**kwargs):
#     print(kwargs)
# num(name = 'aknazar')


# def list(*args):
#     list2 = []
#     for i in args:
#         i**=2
#         list2.append(i)
#     return list2
# print(list(1,2,3,9,8,5))