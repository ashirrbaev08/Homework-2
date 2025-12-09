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

class BankAccount(Hero):
    def __init__(self, name, lvl, hp, balance:int,password:int,bank_name):
        super().__init__(name, lvl, hp)
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def check_login(self,password):
        if password == self.__password:
            return self.__password
        else:
            return f"Неверный пароль!"

    def show_info(self):
        return f"{self.name},{self.lvl},{self.hp},{self._balance} "

    def get_bank_name(self):
        return f"название банка:{self.bank_name}"

    def bonus_for_level(self):
        return f"{self.lvl * 10} "

    def  __str__(self):
        return f"{self.name}| Баланс:{self._balance} SOM"

    def __add__(self, other):
        adding = self.name + other.name

    def __eq__(self, other):
        if self.name == other.name and self.lvl == self.lvl:
            return "Герои считаются равными!"
        else:
            return f"Не равны"











