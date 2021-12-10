import random

class Etel():
    menuAr = 1590
    def __init__(self, leves, masodik, ital):
        self.leves = leves
        self.masodik = masodik
        self.ital = ital

# class Ital(Etel):
# class Leves(Etel):
# class Masodik(Etel):


def menu_opciok(): #A program menüjének kiiratása
     print("Válasszon az alábbi lehetőségek közül: "
    "\n\t 0 - Kilépés"
    "\n\t 1 - Menü igénylése"
    "\n\t 2 - Rendelés"
    "\n\t 3 - Rendelés/menü mentése"    )

def adatok_Betoltese(filepath: str) -> dict: #Adatok betöltése
    leves = []
    ital = []
    masodik = []
    szotar = {}
    try:
        with open("menu.txt", "r", encoding='utf-8') as file:
            leves = file.readline().strip().split(';')
            masodik = file.readline().strip().split(';')
            ital = file.readline().strip().split(';')
            masodik.remove("")
            leves.remove("")
            szotar[1] = leves
            szotar[2] = masodik
            szotar[3] = ital
        file.close()
        return szotar
    except FileNotFoundError:
            print("A fájl nem található / hibás fájl!")

def random_menu(adatok: dict) -> list:  #Véletlenszerű "napi menü" összeállátása
    menu = []
    menu.append(random.choices(list(adatok[1])))
    menu.append(random.choices(list(adatok[2])))
    menu.append(random.choices(list(adatok[3])))
    return menu

def Rendeles(adatok: dict) -> list:
    rendeles = []
    megadottErtek =""
    i=0
    print("Válasszon levest: ")
    for adat in adatok[1]:
        i += 1
        print(f"{i}: {adat}")
    try:
        megadottErtek = int(input())
        if megadottErtek == 1:
            rendeles.append(adatok[1][i])
        elif megadottErtek == 2:
            rendeles.append(adatok[1][i])
        elif megadottErtek == 3:
            rendeles.append(adatok[1][i])
        elif megadottErtek == 4:
            rendeles.append(adatok[1][i])
    except ValueError:
        print("Hibás érték")

    i=0
    print("Válasszon másodikat: ")
    for adat in adatok[2]:
        i += 1
        print(f"{i}: {adat}")
    try:
        megadottErtek = int(input())
        if megadottErtek == 1:
            rendeles.append(adatok[2][i])
        elif megadottErtek == 2:
            rendeles.append(adatok[2][i])
        elif megadottErtek == 3:
            rendeles.append(adatok[2][i])
        elif megadottErtek == 4:
            rendeles.append(adatok[2][i])
    except ValueError:
        print("Hibás érték")

    i=0
    print("Válasszon italt: ")
    for adat in adatok[3]:
        i += 1
        print(f"{i}: {adat}")
    try:
        megadottErtek = int(input())
        if megadottErtek == 1:
            rendeles.append(adatok[3][i])
        elif megadottErtek == 2:
            rendeles.append(adatok[3][i])
        elif megadottErtek == 3:
            rendeles.append(adatok[3][i])
        elif megadottErtek == 4:
            rendeles.append(adatok[3][i])
    except ValueError:
        print("Hibás érték")

    return rendeles


def adatok_Mentese(lista: list, sorszam: int): #Adatok mentése fájlba
    file = open("mentett_menu.txt", "w")
    file.write(sorszam)
    file.write(": \t")
    for adat in lista:
        file.write(adat)
        file.write("\t")
    file.write("\n")
    file.close()

menu=""
fajl_nev = "menu.txt"
adatok = {}
mentes = []
sorszam = 1
adatok = adatok_Betoltese(fajl_nev)
while menu != "0":  #Főmenü futtatása, adatokat előre betölti
    menu_opciok()
    menu = input()
    if menu == "1":
        mentes = random_menu(adatok)
        print("A rendelt menü: \t",random_menu(adatok))
    elif menu == "2":
        mentes = Rendeles(adatok)
    elif menu == "3":
        adatok_Mentese(mentes, sorszam)
        sorszam += 1

print("A program bezárult")