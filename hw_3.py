# class Computer:
#     def __init__(self,cpu,memory):
#         self.cpu=cpu
#         self.memory=memory

#     @property
#     def cpu(self):
#         return self.__cpu
    
#     @property
#     def memory(self):
#         return self.__memory
    



# class Computer:
#     def init(self, cpu, memory):
#         self.__cpu=cpu
#         self.__memory=memory
 

#     def __make_computations(self):
#         add=self.cpu+self.memory
#         sub=self.cpu-self.memory
#         mult=self.cpu*self.memory
#         div=self.cpu/self.memory
#         print(f'результаты: сложение {add}, вычитание {sub}, умножение {mult}, деление {div}')

#     def info(self):
#         self.__make_computations()

# computer=Computer(9,7)
# computer.info()


# class Computer:
#     def init(self, cpu, memory):
#         self.__cpu=cpu
#         self.__memory=memory

#     def get_cpu(self):
#         return print(self.__cpu)
     
#     def get_memory(self):
#         return print(self.__memory)
# computer=Computer(40,90)
# computer.get_cpu()
# computer.get_memory()
 

# class Laptop(Computer):
#     def init(self, cpu, memory,memory_card):
#         super().init(cpu, memory)
#         self.__memory_card=memory_card   

#     @property
#     def memory_card(self):
#         return self.__memory_card


#     def get_info(self):
#         return print(f'результат: {self.cpu}, результат: {self.memory}, результат: {self.memory_card}')
   

# laptop=Laptop(10,70,90)
# laptop.info()


# class PublicComputer:
#     def init(self,cpu,memory,memory_card):
#         self.cpu=cpu
#         self.memory=memory
#         self.memory_card=memory_card

# class SecurityComputer:
#     def init(self,cpu,memory,memory_card):
#         self._cpu=cpu
#         self._memory=memory
#         self._memory_card=memory_card

# class PrivateComputer:
#     def init(self,cpu,memory,memory_card):
#         self.__cpu=cpu
#         self.__memory=memory
#         self.__memory_card=memory_card

