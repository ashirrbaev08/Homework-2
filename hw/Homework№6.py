import pandas as pd
from colorama import Fore,Back,Style
data = {
    "Имя": ["Bektur","Kasym","Aigerim","Aizat"],
    "Баллы":[95,66,59,79]
}

table = pd.DataFrame(data)

print(Fore.CYAN+"Таблица студентов:"+Style.RESET_ALL)
print(table)

print(Fore.RED+"\nСтатистика по балам:"+Style.RESET_ALL)
print("\nСредний балл:",table["Баллы"].mean())
print("Максимальный балл:",table["Баллы"].max())
print("Минимальный балл:",table["Баллы"].min())
print("Количество студентов:",table["Имя"].count())
print("Сумма всех баллов:",table["Баллы"].sum())

# В этом коде я использовал библиотеки Pandas и Colorama.
# Библиотека Pandas предназначена для работы с таблицами (данными).
# Библиотека Colorama используется для раскрашивания текста в консоли,
# то есть для того, чтобы вывод выглядел более красивым и наглядным.
