class Animal:

    def __init__(self,name:str,age:int,health:int):
        self.name = name
        self.age = age
        self.health = health

    def info(self):
        return f"{self.name},{self.age} лет,здоровье {self.health}"

    def use_ability(self):
        return f"использует базовую способность"

class Flyable:

    def use_ability(self):
        get = super().use_ability()
        ability = "летает"
        return ability + "," + get

class Swimmable:
    def use_ability(self):
        get = super().use_ability()
        ability = "плавает"
        return ability + "," + get

class Invisible:

    def use_ability(self):
        get = super().use_ability()
        ability = "становится невидимым"
        return ability + "," + get

class Duck(Flyable,Swimmable,Animal):
    pass

class Bat(Flyable,Invisible,Animal):
    pass

class Frog(Swimmable,Animal):
    pass

class Phoenix(Flyable,Invisible,Animal):
    pass

class Zoo():
    def __init__(self):
        self.animals = []

    def add_animal(self,animal):
        self.animals.append(animal)

    def show_all(self):
        for a in self.animals:
            print(a.info())

    def perform_show(self):
        for a in self.animals:
            print(a.info(),a.use_ability())

duck = Duck("Дональд", 3, 80)
bat = Bat("Бэтти", 5, 60)
frog = Frog("Кермит", 2, 50)
phoenix = Phoenix("Феникс", 100, 200)

zoo = Zoo()
zoo.add_animal(duck)
zoo.add_animal(bat)
zoo.add_animal(frog)
zoo.add_animal(phoenix)
print("=== Информация о животных ===")
zoo.show_all()
print("\n=== Шоу суперспособностей ===")
zoo.perform_show()

print("\nMRO для Duck:", Duck.__mro__)

print("MRO для Phoenix:", Phoenix.__mro__)