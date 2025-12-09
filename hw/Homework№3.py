class Product:
    def __init__(self,name,price,discount=0):
        self.name = name
        self._price = price
        self.__discount = discount

        if 0 <= discount <= 50:
            self.__discount = discount
        else:
            self.__discount = 0

    def get_price(self):
        return self._price * (1 - self.__discount / 100)

    def set_discount(self,percent:int):
        if 0 <= percent <= 50:
            self.__discount = percent

    def apply_extra_discount(self,secret_code):
        if secret_code == "VIP123":
            return self.get_price() * 0.95
        else:
            return "Неверный код"

product = Product("Iphone",1000,10)


print("Цена со скидкой:",product.get_price())
product.set_discount(50)
print("Цена после измения скидки:",product.get_price())
print("Цена после VIP:",product.apply_extra_discount("beka"))
print("Итоговая цена:",product.apply_extra_discount("VIP123"))




# № Второе задание

from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self,amount:int):
        pass

    @abstractmethod
    def refund(self,amount:int):
        pass

class CardPayment(PaymentMethod):
    def pay(self,amount:int):
        return f'Оплата картой:{amount}'
    def refund(self,amount):
        pass

class CashPayment(PaymentMethod):
    def pay(self,amount:int):
       return f"Оплата наличными:{amount}"
    def refund(self,amount:int):
        pass
class CryptoPayment(PaymentMethod):

    def pay(self,amount:int):
         return {"type": "crypto", "amount": f"{amount}", "currency": "USDT"}
    def refund(self,amount):
        pass

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        return self.payment_method.pay(amount)

processor = PaymentProcessor(CardPayment())
processor.process(100)
processor = PaymentProcessor(CashPayment())
processor.process(50)
processor = PaymentProcessor(CryptoPayment())
processor.process(200)