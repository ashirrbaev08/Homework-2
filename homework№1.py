class car:

    def __init__(self,brand,year,color,volume,check=True):
        self.brand = brand
        self.color = color
        self.volume = volume
        self.check = check
        self.year = year

    def low_fuel(self):
        return f"{self.brand} - Залей бензин,запас хода 20 км"

    def fuel(self,fuel = "бензин залит запас топлива до 450 км"):
        self.check = False
        return f"{self.brand}-{fuel}"

    def check_info(self):
        if self.check:
            red_on = "чек горит"
        else:
            red_on = "чек не горит езжай смело!"

        return f"{self.brand},год выпуска:{self.year},цвет:{self.color},объем машины:{self.volume}, сейчас {red_on}"

car1 = car("Bmw","2017","Черный",volume="4.4")
car2 = car("Mercedec AMG","2015","черный","5.5")

print(car2.check_info())
print(car2.low_fuel())
print(car2.fuel())
print(car2.check_info())

print("\n",car1.low_fuel())
print(car1.fuel())










