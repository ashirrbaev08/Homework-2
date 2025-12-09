class Hero:
    def __init__(self,name:str,lvl:int,hp:int):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def action(self):
        return f"{self.name} готов к бою"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP:{self.mp}"


class WarriorHero(MageHero):

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень:{self.lvl}"

class BankAccount:
    def __init__(self,name,balance:int,password:int,bank_name:str,lvl):
        self.name = name
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name
        self.lvl = lvl

    def check_login(self,password):
        if self.__password == password:
            return self.__password
        else:
            return f"Неверный пароль!"

    def info(self):
        return f"{self.name.name} {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.name.lvl * 10

    def  __str__(self):
        return f"{self.name.name}| Баланс:{self._balance} SOM"

    def __add__(self, other):
        return self._balance + other._balance

    def __eq__(self, other):
        if self.name.name == other.name.name and self.name.lvl == other.name.lvl:
            return "Герои считаются равными!"

        return f"Не равны"

mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)

acc1 = BankAccount(mage1, 5000, "1234","Simba","0")
acc2 = BankAccount(mage2, 3000, "0000","Simba","0")
acc3 = BankAccount(warrior, 2500, "1111","Simba","0")

print(mage1.action())
print(warrior.action())

print(acc1)
print(acc2)
# --- Классовые и статические методы ---
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

# --- Магические методы: __add__ ---
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

print("Сумма мага и воина:", acc1 + acc3)

# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False





from abc import ABC, abstractmethod

class SmsService(ABC):

    @abstractmethod
    def send_otp(self,phone):
        pass

class KGSms(SmsService):
    def send_otp(self,phone):
        sms = f"<text>Код: 1234</text><phone>{phone}</phone>"
        return sms

class RUSms(SmsService):
    def send_otp(self,phone):
        sms = {"text": "Код: 1234", f"{phone}": "{phone}"}
        return sms

sms = KGSms()
print("\n", sms.send_otp("+996777123456"))















