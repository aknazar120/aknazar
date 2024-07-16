# class MagicCalculator:
#     def __init__(self, number_1, number_2):
#         self.number_1 = number_1
#         self.number_2 = number_2
    
#     def __add__(self, other):
#         return self.number_1 + other.number_1, self.number_2 + other.number_2
    
#     def __sub__(self, other):
#         return self.number_1 - other.number_1, self.number_2 - other.number_2
    
#     def __mul__(self, other):
#         return self.number_1 * other.number_1, self.number_2 * other.number_2
    
#     def __truediv__(self, other):
#         if other.number_1 != 0 and other.number_2 != 0:
#             return self.number_1 / other.number_1, self.number_2 / other.number_2
#         else:
#             raise ("Ошибка!")
    
#     def __floordiv__(self, other):
#         if other.number_1 != 0 and other.number_2 != 0:
#             return self.number_1 // other.number_1, self.number_2 // other.number_2
#         else:
#             raise ("Ошибка!")
        
# num = MagicCalculator(40,20)
# num_2 = MagicCalculator(50,3)
# print(num + num_2)
# print(num - num_2)
# print(num * num_2)
# print(num / num_2)
# print(num // num_2)



# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def __lt__(self, other):
#         return self.year < other.year
    
#     def __le__(self, other):
#         return self.year <= other.year
    
#     def __gt__(self, other):
#         return self.year > other.year
    
#     def __ge__(self, other):
#         return self.year >= other.year
    
#     def __eq__(self, other):
#         return self.year == other.year
    
#     def __ne__(self, other):
#         return self.year != other.year
    
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
    
# num = Book("Мастер и Маргарита","Михаил Булгаков",1929)
# num1 = Book("Собачье сердце","Михаил Буков",1925)
# num2 = Book("Мертвые души","Николай Гоголь",1842)

# num.__str__()
# num1.__str__()
# num2.__str__()

# print(num > num1 > num2)
# print(num < num1 < num2)
# print(num == num1 == num2)
# print(num != num1 != num2)
# print(num >= num1 >= num2)
# print(num <= num1 <= num2)