import pyJPRed
import zadaci

# Ispis meni-a
print("      ** TESTNI PROGRAM ZA pyRed **")
print("-------------------Menu--------------------")
print("1. Dodaje element u red")
print("2. Ukloni element iz redaa")
print("3. Element na pocetku reda")
print("4. Prikazi sadrzaj reda")
print("5. Da li je red prazan?")
print("6. Da li je red pun?")
print("7. Potpuno brisanje reda!")
print("8. Suma reda")
print("99. Izlaz")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# Iniciranje JP Reda
Red = zadaci.prosirenaJPRed()

def menu(izbor):
    match izbor:
        case 1:
            x = input("Unesite vrijednost elementa za dodavanje u red?\n")
            Red.dodajURed(x)
        case 2:
            Red.izbaciIzReda()
        case 3:
            Red.elementNaCelu()
        case 4:
            Red.prikazi()
        case 5:        
            if(Red.jeLiPrazan()):
                print("Red je prazan!")
            else:
                print("Red NIJE prazan!")
        case 6:
            print("Kapacitet JPReda je \"neogranicen!\"")   
        case 7:
            Red.brisi()   
        case 8:
            Red.SumaElemenata()
        case 99:
            print("Program zavrsen!\n")
            exit()
        case _:
            print("Pogresan izbor. Molimo ponovite unos izbora!")


while (izbor):
    menu(izbor)
    unos_izbor = input("--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)

