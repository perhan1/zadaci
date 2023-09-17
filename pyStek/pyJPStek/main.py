import zadaci

# Ispis meni-a
print("      ** TESTNI PROGRAM ZA pyStek **")
print("-------------------Menu--------------------")
print("1. Dodaje element na stek")
print("2. Ukloni element sa steka")
print("3. Element na vrhu steka")
print("4. Prikazi sadrzaj steka")
print("5. Da li je stek prazan?")
print("6. Da li je stek pun?")
print("7. Potpuno brisanje steka!")
print("8. Aritmetička sredina steka")
print("9. Suma steka")
print("10. Proizvod steka")
print("99. Izlaz")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# Iniciranje JP Steka
Stek = zadaci.prosirenaJPStek()

# case petlja za definiranje opcija u meniju
def menu(izbor):
    match izbor:
        case 1:
            x = input("Unesite vrijednost elementa za dodavanje na stek?\n")
            Stek.dodajNaStek(x)
        case 2:
            Stek.ukloniSaSteka()
        case 3:
            Stek.elementNaVrhu()
        case 4:
            Stek.prikazi()
        case 5:                     
            if(Stek.jeLiPrazan()):
                print("Stek je prazan!")
            else:
                print("Stek NIJE prazan!")
        case 6:
            print("Kapacitet JPSteka je \"neograničen!\"")             
        case 7:
            Stek.brisi()
        case 8:
            Stek.aSredina()
        case 9:
            Stek.SumaElemenata()
        case 10:
            Stek.ProizvodElemenata()
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")


while (izbor):
    menu(izbor)
    unos_izbor = input("--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)

