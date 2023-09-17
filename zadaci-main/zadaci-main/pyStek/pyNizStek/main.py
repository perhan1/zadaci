import pyNizStek
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
print("8. Proizvod elemenata steka")
print("99. Izlaz")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# Inicijalizacija Niz Steka
k = 10
#Stek = pyNizStek.NizStek(k)
Stek = zadaci.prosirenaNizStek(k)

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
            print("Vrh: " + str(Stek.vrh))
            print("Kapacitet: " + str(Stek.kapacitet))          
            if(Stek.jeLiPrazan()):
                print("Stek je prazan!")
            else:
                print("Stek NIJE prazan!")
        case 6:
            print("Vrh: " + str(Stek.vrh))
            print("Kapacitet: " + str(Stek.kapacitet))  
            if(Stek.jeLiPun()):
                print("Stek je pun!")
            else:
                print("Stek NIJE pun!")   
        case 7:
            Stek.brisi()   
        case 8:
            Stek.ProizvodElemenata()
        case 99:
            print("Program zavrsen!\n")
            exit()
        case _:
            print("Pogresan izbor. Molimo ponovite unos izbora!")

# while petlja za kontinuiran odabir opcija u meniju
while (izbor):
    menu(izbor)
    unos_izbor = input("--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)

