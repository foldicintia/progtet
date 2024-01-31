from Cipo import Cipo

peldany1 = Cipo("Nike", 42)
peldany2 = Cipo("Adidas", 41)
peldany3 = Cipo("Adidas", 45)

cipok = []
cipok.append(peldany1)
cipok.append(peldany2)
cipok.append(peldany3)

for i in range(0, len(cipok), 1):
    nev: str = cipok[i].nev
    meret: int = cipok[i].meret
    print(f"{nev} ({meret})")


def meret_atlag():       #összegzés tétele
    ossz: int = 0
    for i in range(0, len(cipok), 1):  
        ossz += cipok[i].meret         

    atlag = ossz / len(cipok)
    print(round(atlag, 3))


meret_atlag()

def legnagyobb_markaju(cipok):    #maximum kiválasztás tétele
    print("Milyen márkájú a legnagyobb méretű cipő?", end="")
    legnagyobb_index=0
    for i in range(0,len(cipok),1):
        if cipok[legnagyobb_index].meret < cipok[i].meret:
            legnagyobb_index=i
    return legnagyobb_index

legnagyobb_index=legnagyobb_markaju(cipok)
print(f"A legnagyobb méretű cipő márkája: {cipok[legnagyobb_index].nev}")

def adidas_db(cipok):     #megszámlalas tétele
    print("Hány darab Adidas márkájú cipő van?:", end="")
    db=0
    for i in range(0, len(cipok),1):
        if cipok[i].nev == "Adidas":
            db+=1
    return db

db=adidas_db(cipok)
print(f"{db} db Adidas márkájú cipő van.")

def nagyobb_42_adidas():
    van_nagyobb: bool = False       #eldöntés tétele

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True

    if van_nagyobb == True:
        print("Van 42-nél nagyobb Adidas cipő.")
    else:
        print("Nincs 42-nél nagyobb Adidas cipő.")                                          


nagyobb_42_adidas()
