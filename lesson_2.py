# class Car:
#     def __init__(self,model,color):
#         self.model = model
#         self.color = color

#     def info(self):
#         print(self.model, self.color)

#     mers = ('mersedes - cls','black')
#     mers.info()

# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def proccess_payment(self, amount):
#         pass 

# class CreditCardPayment(Payment):
#     def proccess_payment(self, amount):
#         print(f'Обработка по кредитной карте, на сумму {amount}$')
    
# class PayPalPayment(Payment):
#     def proccess_payment(self, amount):
#         print(f'Обработка по PayPal, на сумму {amount}$')
    
# def make_payment(payment_method, amount):
#     payment_method.proccess_payment(amount)
    

# credit_card_payment = CreditCardPayment()
# paypal = PayPalPayment()

# make_payment(credit_card_payment, 100)
# make_payment(paypal, 200)
