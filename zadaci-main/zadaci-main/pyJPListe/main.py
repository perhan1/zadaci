import zadaci

#meni
print("     ** TESTNI PROGRAM ZA pyJPListe **")
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
print("11. Ispiši vrijednost aritmetičke sredine elemenata liste")
print("12. Ispiši kvadrat aritmetičke sredine elemenata liste")
print("13. Ispiši kub sume elemenata liste")
print("14. Ispiši korijen proizvoda elemenata liste")
print("15. Dodaj sumu na kraj liste")
print("16. Dodaj element u sredinu liste")
print("99. Izlaz")
unos_izbora = input("------------Izaberite opciju?-------------\n")
izbor = int(unos_izbora)


Lista = zadaci.prosirenaJPLista()


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
        case 11:
            Lista.AritmetickaSredina()
        case 12:
            Lista.KvadratAritSredine()
        case 13:
            Lista.KubSume()
        case 14:
            Lista.KorijenProizvoda()
        case 15:
            Lista.DodajSumuNaKraj()
        case 16:
            x = input("Unesite vrijednost elementa!\n")
            Lista.DodajElUSredinu(x)
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")


while (izbor):    
    menu(izbor)
    unos_izbora = input("------------Izaberite opciju?-------------\n")
    izbor = int(unos_izbora)