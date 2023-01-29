import pySortiranja

# Prikaz izbornika
print("      ** TESTNI PROGRAM ZA pySortiranja **")
print("------------------------Menu------------------------")
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
print("-----------Osnovni algoritmi sortiranja-------------")
print("11. Insertion sort")
print("12. Shell sort")
print("13. Selection sort")
print("14. Bubble sort")
print("-----Napredni (efikasniji) algoritmi sortiranja-----")
print("15. Merge sort")
print("16. Popuni listu test nizom brojeva")
print("99. Izlaz")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
if (unos_izbor.isnumeric()):
    izbor = int(unos_izbor)
else:
    izbor = int(99999)    

# Iniciranje objekata Liste sa kapacitetom k
k = 5000
Lista = pySortiranja.pySortiranjeNizListe(k)

# Funkcija izbornika
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
            Lista.insertionSort()
        case 12:
             Lista.shellSort()
        case 13:
             Lista.selectionSort()
        case 14:
             Lista.bubbleSort()
        case 15:
            Lista.MergeSort(0, Lista.duzina-1)
            print("Sortirano!")
        case 16:
             Lista.popuniListuRand()
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")

# Petlja, while, dok god postoji unos izbora
while (izbor):
    menu(izbor)
    unos_izbor = input("--------------Izaberite opciju?---------------\n")
    if (unos_izbor.isnumeric()):
        izbor = int(unos_izbor)

# UNZE PTF ASP 2021/2022 :: M.S. :: 05.01.2022