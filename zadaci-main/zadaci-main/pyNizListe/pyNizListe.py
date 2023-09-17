import ctypes

class NizLista():
    
    def kreiraj_niz(self, k):        
        return (ctypes.py_object * k)( )

    def __init__(self, kapacitet): 
        self.kapacitet = kapacitet
        self.duzina = 0
        self.tekuci = 0
        self.Niz = self.kreiraj_niz(self.kapacitet)

    def idiNaPocetak(self):
        self.tekuci = 0
        print("Pokazivač tekući postavljen na POČETAK liste!")

    def idiNaKraj(self):
        self.tekuci = self.duzina
        print("Pokazivač tekući postavljen na KRAJ liste!")

    def idiNaSljedeci(self):
        if(self.tekuci < self.duzina):
            self.tekuci += 1
            print("Pokazivač tekući postavljen na SLJEDEĆI ELEMENT liste!")
        else:
            print("Pokazivač tekući je na kraju liste!")

    def idiNaPrethodni(self):
        if(self.tekuci != 0):
            self.tekuci -= 1
            print("Pokazivač tekući postavljen na PRETHODNI ELEMENT liste!")
        else:
            print("Pokazivač tekući je na početku liste!")

    def idiNaPoziciju(self, pozicija):        
        if((pozicija < 0) and (pozicija > self.duzina)):
            print("Zadata pozicija izvan raspona!")            
        else:
            self.tekuci = pozicija
            print("Pokazivač tekući postavljen na poziciju:" + str(pozicija))

    def dodaj(self,x):
        if (self.duzina < self.kapacitet):
            self.Niz[self.duzina] = x
            self.duzina += 1
            print("Uspješno dodan element!")
        else:
            print("Kapacitet popunjen!")

    def umetni(self,x):
        if (self.duzina < self.kapacitet):
            for i in range(self.duzina,self.tekuci,-1):
                self.Niz[i] = self.Niz[i-1]           
            self.Niz[self.tekuci] = x
            self.duzina += 1
            print("Uspješno umetnut element " + str(x)+ "na poziciju pokazivača " + str(self.tekuci))

    def lDuzina(self):
        return self.tekuci

    def dDuzina(self):
        return self.duzina - self.tekuci

    def izbaci(self):
        if (self.dDuzina() <= 0):
            print("Nema elemenata za izbacivanje/brisanje!")
        else:
            izbaceni = self.Niz[self.tekuci]
            for i in range(self.tekuci,self.duzina,-1):
                self.Niz[i] = self.Niz[i-1]     
            self.duzina -= 1
            print("Izvršeno izbacivanje elementa vrijednosti: " + str(izbaceni))

    def ispisiTekuci(self):
        if (self.dDuzina() <= 0):
            print("Nema elemenata za ispis! Pokazivač je na kraju liste")
        else:
            print("Vrijednost elementa na tekućoj poziciciji je: ", self.Niz[self.tekuci])

    def prikazi(self):
        print("Dužina liste:" + str(self.duzina))
        for i in range(0,self.duzina):
             print("Element "+ str(i+1) + " - pozicija("+ str(i) + ") :" + str(self.Niz[i]))