import ctypes

class NizLista():
    
    def kreiraj_niz(self, k):
        return (ctypes.py_object * k)()
    
    # Iniciranje liste sa predodređenim kapacitetom
    def __init__(self, kapacitet):
        self.kapacitet = kapacitet
        self.duzina = 0
        self.tekuci = 0
        self.Niz = self.kreiraj_niz(self.kapacitet)
    
    # Pozicioniranje na početak
    def idiNaPocetak(self):
        self.tekuci = 0
        print("Pokazivač tekući postavljen na POČETAK liste!")
    
    # Pozicioniranje na kraj
    def idiNaKraj(self):
        self.tekuci = self.duzina
        print("Pokazivač tekući postavljen na KRAJ liste!")

    # Pozicioniranje na sljedeći
    def idiNaSljedeci(self):
        if(self.tekuci < self.duzina):
            self.tekuci += 1
            print("Pokazivač tekući postavljen na SLJEDEĆI ELEMENT liste!")
        else:
            print("Pokazivač tekući je na kraju liste!")

    # Pozicioniranje na prethodni
    def idiNaPrethodni(self):
        if(self.tekuci != 0):
            self.tekuci -= 1
            print("Pokazivač tekući postavljen na PRETHODNI ELEMENT liste!")
        else:
            print("Pokazivač tekući je na početku liste!")

    # Pozicioniranje na proizvoljnu poziciju
    def idiNaPoziciju(self, pozicija):
        if((pozicija < 0) or (pozicija > self.duzina)):
            print("Zadata pozicija je izvan raspona!")
        else:
            self.tekuci = pozicija
            print("Pokazivač tekući postavljen na poziciju:" + str(pozicija))

    # Dodavanje elementa na kraj liste
    def dodaj(self,x):
        if(self.duzina < self.kapacitet):
            self.Niz[self.duzina] = x
            self.duzina += 1
            print("Uspješno dodan element!")
        else:
            print("Kapacitet popunjen!")

    # Dužina lijeve particije
    def lDuzina(self):
        return self.tekuci

    # Dužina desne particije
    def dDuzina(self):
        return self.duzina - self.tekuci
    
    # Umetanje lementa na tekuću poziciju
    def umetni(self, x):
        if(self.duzina < self.kapacitet):
            for i in range(self.duzina,self.tekuci,-1): 
                self.Niz[i] = self.Niz[i-1]             
            self.Niz[self.tekuci] = x
            self.duzina += 1
            print("Uspješno umetnut element " + str(x) + " na poziciju pokazivača " + str(self.tekuci))
        else:
            print("Kapacitet popunjen!")

    # Izabcivanje/Brisanje tekućeg elementa - vrijednost elementa sa desne strane od indeksa pokazivača tekući
    def izbaci(self):
        if (self.dDuzina() <= 0):
            print("nema elemenata za izbacivanje/brisanje! Tekući na kraju liste!")
        else:
            izbacei = self.Niz[self.tekuci]
            for i in range (self.tekuci,self.duzina-1): 
                self.Niz[i] = self.Niz[i+1]             
            self.duzina -= 1
            print("izvršeno je izbacivanje elementa vrijednosti: " + str(izbacei))

    # Ispis tekućeg elementa
    def ispisiTekuci(self):
        if (self.dDuzina() <= 0):
            print("Nema elemenata za ispis! Pokazivač je na kraju liste!")
        else:
            print("Vrijednost elementa na tekućoj poziciji je: " + str(self.Niz[self.tekuci]))

    
    # Prikazivanje/Ispis svih elemenata liste
    def prikazi(self):
        print("Dužina liste:" + str(self.duzina))
        #py doc --> range(start, stop, step)
        for i in range(0,self.duzina):
            print("Element " + str(i+1) + " - pozicija(" + str(i) + ") :" + str(self.Niz[i]))



