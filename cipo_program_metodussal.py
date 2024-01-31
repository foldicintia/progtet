from Cipo import Cipo


def pldlista():
    peldany1 = Cipo("Nike", 42)
    peldany2 = Cipo("Adidas", 41)
    peldany3 = Cipo("Adidas", 45)

    cipok = []
    cipok.append(peldany1)
    cipok.append(peldany2)
    cipok.append(peldany3)
    return cipok


def listakiir(lista):
    for i in range(0, len(lista), 1):
        nev: str = lista[i].nev
        meret: int = lista[i].meret
        print(f"{nev} ({meret})")

# Rövid verzió
# listakiir(pldlista())

# Ez a hosszú verzió
cipok_lista=pldlista()   #mindenhol 
listakiir(cipok_lista)


def osszegzes_tetele(cipok):       #összegzés tétele
    ossz: int = 0
    for i in range(0, len(cipok), 1):  
        ossz += cipok[i].meret         

    atlag = ossz / len(cipok)
    print(round(atlag, 3))

osszegzes_tetele(cipok_lista)


def maximum_kivalasztas(cipok):    #maximum kiválasztás tétele
    print("Milyen márkájú a legnagyobb méretű cipő?", end="")
    legnagyobb_index=0
    for i in range(0,len(cipok),1):
        if cipok[legnagyobb_index].meret < cipok[i].meret:
            legnagyobb_index=i
    return legnagyobb_index

legnagyobb_index=maximum_kivalasztas(cipok_lista)
print(f"A legnagyobb méretű cipő márkája: {cipok_lista[legnagyobb_index].nev}")


def megszamlalas_tetele(cipok):     #megszámlalas tétele
    print("Hány darab Adidas márkájú cipő van?:", end="")
    db=0
    for i in range(0, len(cipok),1):
        if cipok[i].nev == "Adidas":
            db+=1
    return db

db=megszamlalas_tetele(cipok_lista)
print(f"{db} db Adidas márkájú cipő van.")


def eldontes_tetele(cipok):
    van_nagyobb: bool = False       #eldöntés tétele

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True

    if van_nagyobb == True:
        print("Van 42-nél nagyobb Adidas cipő.")
    else:
        print("Nincs 42-nél nagyobb Adidas cipő.")                                          

eldontes_tetele(cipok_lista)
