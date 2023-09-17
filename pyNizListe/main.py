    import pyNizListe
import zadatak1 # Importujemo novi prošireni py kod

print("     ** TESTNI PROGRAM ZA pyNizListe **")
print("-------------------Menu--------------------")
print("1. Idi na prethodni")
print("2. Idi na sljedeći")
print("3. Idi na početak")
print("4. Idi na kraj")
print("5. Idi na poziciju")
print("6. Dodavanje elementa na kraj liste")
print("7. Umetanje elementa na tekuću poziciju")
print("8. Izbacivanje tekućeg elementa")
print("9. Ispis vrijednost tekućeg elementa")
print("10. Prikaži sadržaj liste")
print("11. Prikaži kvadrat sume svih elemenata liste") # Dodajemo proširenu metodu kvadrat sume
print("12. Prikaži aritmetičku sredinu svih elemenata liste") # Dodajemo proširenu metodu aritmetička sredina
print("13. Prikaži sumu svih elemenata liste") # Dodajemo proširenu metodu suma
print("14. Prikaži kub aritmetičke sredine svih elemenata liste") # Dodajemo proširenu metodu aritmetička sredina
print("15. Prikaži proizvod svih elemenata liste") # Dodajemo proširenu metodu suma
print("16. Dodaj sumu svih elemenata u sredinu liste") # Dodajemo proširenu metodu koja dodaje sumu u sredinu liste
print("99. Izlaz")
unos_izbora = input("------------Izaberite opciju?-------------\n")
izbor = int(unos_izbora)

k = 10
Lista = zadaci.prosirenaPyNizLista(k) # Moramo inicirati proširenu strukturu kao Listu

def menu(izbor):
    match izbor:
        case 1:
            Lista.idiNaPrethodni()
        case 2:
            Lista.idiNaSljedeci()
        case 3:
            Lista.idiNaPocetak()
        case 4:
            Lista.idiNaKraj()
        case 5:
            pozicija = input("Unesite poziciju za dislokaciju pokazivača tekući!\n")
            Lista.idiNaPoziciju(int(pozicija))
        case 6:
            x = input("Unesite vrijednost elementa!\n")
            Lista.dodaj(x)
        case 7:
            x = input("Unesite vrijednost elementa!\n")
            Lista.umetni(x)
        case 8:
            Lista.izbaci()
        case 9:
            Lista.ispisiTekuci()
        case 10:
            print("** ELEMENTI U LISTI **")
            Lista.prikazi()
        case 11: # Dodajemo novi case izbor za proširenu metodu
            Lista.KvadratSumeElemenata()
        case 12: # Dodajemo novi case izbor za proširenu metodu
            Lista.AritmetickaSredinaElemenata()
        case 13: # Dodajemo novi case izbor za proširenu metodu
            Lista.SumaElemenata()
        case 14: # Dodajemo novi case izbor za proširenu metodu
            Lista.KubAritmetickeSredineElemenata()
        case 15: # Dodajemo novi case izbor za proširenu metodu
            Lista.ProizvodElemenata()
        case 16: # Dodajemo novi case izbor za proširenu metodu
            Lista.DodajSumuUSredinu()
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")

while (izbor):    
    menu(izbor)
    unos_izbora = input("------------Izaberite opciju?-------------\n")
    izbor = int(unos_izbora)