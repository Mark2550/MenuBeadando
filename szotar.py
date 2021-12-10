import random


rendeles = []
megadottErtek =""
leves = []
ital = []
masodik = []
szotar = {}
try:
    with open("menu.txt", "r", encoding='utf-8') as file:
        leves = file.readline().strip().split(';')
        leves.remove("")
        masodik = file.readline().strip().split(';')
        masodik.remove("")
        ital = file.readline().strip().split(';')
        szotar[1] = leves
        szotar[2] = masodik
        szotar[3] = ital
    file.close()
except FileNotFoundError:
    print("A fájl nem található / hibás fájl!")
print(random.choices(list(szotar[1])))
