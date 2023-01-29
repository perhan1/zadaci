import pyRekurzivneNizListe 

# Prikaz izbornika 
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
print("99. Izlaz")
print("-----------------Rekurzija------------------")
print("11. Ispis permutacija")
print("12. Ispis permutacija k do m")
print("13. Ispisi faktorijel novounesenog elementa na tekucu poziciju")
print("14. Ispisi kvadrat faktorijela novounesenog elementa na tekucu poziciju")
print("----Izaberi meni opciju------>")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# Iniciranje objekata Liste sa kapacitetom k
k = 10
Lista = pyRekurzivneNizListe.pyRekurzivneNizLista(k)

# Definicija logike izbornika za pojedine funkcije strukture
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
        case 99:
            print("Program završen!\n")
            exit()
        
        # Dopunske funkcije vezane za rekurziju START
        case 11:
            Lista.IspisiPermutacije(0)
        case 12:
            k = input("Unesite n: \n")
            m = input("Unesite k: \n")
            print("Permutacije: \n")
            Lista.IspisiPermutacijeKdoM(int(k),int(m)) 
        case 13:
            x = input("Dodaj element na tekuću poziciju!\n")
            Lista.dodaj(int(x))
            print("Faktorijel tekućeg elementa je: \n")
            print(Lista.tekuciFaktorijel(int(x)))
        
        case 14:
            x = input("Dodaj element na tekuću poziciju!\n")
            Lista.dodaj(int(x))
            print("Kvadrat faktorijela tekućeg elementa je: \n")
            print(Lista.KVtekuciFaktorijel(int(x)))
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")

# Petlja, while, dok god postoji unos izbora
while (izbor):
    menu(izbor)
    unos_izbor = input("--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)
