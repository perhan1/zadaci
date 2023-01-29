import pyPretrazivanja

print("      ** TESTNI PROGRAM ZA pyPretraživanja **")
print("-------------------Menu--------------------")
print("1. Idi na početak")
print("2. idi na kraj")
print("3. Idi na prethodni")
print("4. Idi na sljedeći")
print("5. Idi na poziciju")
print("6. Dodavanje elemenata na kraj liste")
print("7. Umetanje elmenta na tekuću poziciju")
print("8. Izbacivanje tekućeg elementa")
print("9. Ispis vrijednosti tekućeg elementa")
print("10. Prikaz sadržaja liste")
print("--------------Pretraživanja---------------")
print("11. *Sekvencijalno pretrazivanje niza")
print("12. SORTIRANO dodavanje elemenata na kraj liste (*INT)")
print("13. SORTIRANO umetanje elmenta na tekuću poziciju (*INT)")
print("14. *Binarno pretrazivanje niza")
print("15. *Interpolacijsko pretrazivanje niza")
print("16. *Sekvencijalno pretrazivanje niza (*INT)")
print("17. Popuni listu test nizom")
print("18. Popuni listu sortiranim test nizom (*INT)")
print("19. Poništi listu!")
print("99. Izlaz")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)


k = 100
Lista = pyPretrazivanja.pyPretrazivanjeNizListe(k)

def menu(izbor):
    match izbor:
        case 1:
            Lista.idiNaPocetak()
        case 2:
            Lista.idiNaKraj()
        case 3:
            Lista.idiNaPrethodni()
        case 4:
            Lista.idiNaSljedeci()
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
        case 11:
            kljuc = input("Unesite ključnu vrijednost za pretragu!\n")
            Lista.sekvencijalnoPretrazivanje(kljuc)
        case 12:
            x = input("Unesite vrijednost elementa!\n")
            if (Lista.testDodaj(int(x))):
                Lista.dodaj(int(x))
            else:
                print("Element nije unesen!\nData vrijednost narušava rastući poredak liste.")
        case 13:
            x = input("Unesite vrijednost elementa!\n")
            if (Lista.testUmetni(int(x))):
                Lista.umetni(int(x))
            else:
                print("Element nije unesen!\nData vrijednost narušava rastući poredak liste.")
        case 14:
            kljuc = input("Unesite ključnu vrijednost za pretragu!\n")
            Lista.binarnoPretrazivanje(int(kljuc))
        case 15:
            kljuc = input("Unesite ključnu vrijednost za pretragu!\n")
            Lista.interpolacijskoPretrazivanje(int(kljuc))   
        case 16:
            kljuc = input("Unesite ključnu vrijednost za pretragu!\n")
            Lista.sekvencijalnoPretrazivanje(int(kljuc))  
        case 17:
            Lista.popuniListuRand()
        case 18:
            Lista.popuniListuSortRand()
        case 19:
            Lista.duzina = 0
            Lista.tekuci = 0
            print("Sadržaj liste poništen!")
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")


while (izbor):
    menu(izbor)
    unos_izbor = input("--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)
