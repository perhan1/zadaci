import pyNizListe
import random

# Proširujemo osnovnu klasu NizListe sa metodama za pretraživanje
class pyPretrazivanjeNizListe(pyNizListe.NizLista):

# Sekvencijalno pretraživanje ostvaruje pronalaženje traženog elementa tako da se uspoređuje
# jedna po jedna vrijednost elemenata u nizu sa traženim ključem,
# počevši od prvog elementa u nizu, sve dok se traženi ključ ne pronađe
# ili dok se ne dođe do kraja niza. 
    def sekvencijalnoPretrazivanje(self, kljuc):
        i = 0
        while(i < self.duzina):
            if(self.Niz[i] == kljuc):
                print("Tražena vrijednost " + str(kljuc) + " se nalazi na poziciji: " + str(i))
                return None
            else:
                i += 1
                print("Ispitivanje "+ str(i)+"!\n")
        # U slučaju kada pretraga dođe do kraja liste, a element ne bude pronađen, while petlja će se prekinuti na način da se indeks i poveća na duzina + 1, što je raspon izvan definiranog niza
        if(i == self.duzina):                                                       
            print("Tražena vrijednost " + str(kljuc) + " nije pronađena!")

# Binarno i Interpolacijsko pretraživanje - podrazumijeva uređen niz sortiran u rastućem poretku
# Kako bi ispoštovali uređenost niza, definiramo funkcije koje će testirati i odbiti unos elemenata ukoliko oni nisu u rastućem poretku
# Da bi postigli ispravno funkcioniranje metoda, moramo predefinirati TIP PODATAKA - int

    # Test ispravnosti prije umetanja na tekuću poziciju
    def testUmetni(self, x):
        if(self.duzina == 0):   # Niz je prazan, sve vrijednosti su prihvatljive, element ne treba testirati
            return True
        if(self.tekuci < self.duzina and x > self.Niz[self.tekuci]) or (self.tekuci == self.duzina and x < self.Niz[self.tekuci-1]):
            # Unos elementa u "sredinu" liste - vrijednost mora biti manja od vrijednosti trenutnog tekućeg elementa jer se unosi na poziciju lijevo (prije) od pokazivača tekući.
            # Ukoliko se unos vrši na kraj liste, vrijednost novog elementa mora biti veća od pozicije tekući-1 (najveći, duzina-1 je tada ustvari kraj liste)
            return False
        else:
            return True
    
    # Test ispravnosti prije umetanja na kraj liste
    def testDodaj(self, x):
        if(self.duzina == 0):   # Niz je prazan, sve vrijednosti su prihvatljive, element ne treba testirati
            return True
        if(x < self.Niz[self.duzina-1]): # Novi element mora biti najveći u listi, tj. ne smije biti manji od krajnjeg elementa
            return False
        else:
            return True

    # Binarno pretraživanje - polovljenje veličine niza
    def binarnoPretrazivanje(self, kljuc):
        vrh = self.duzina - 1           # Definiramo indeks krajnjeg elementa u nizu
        dno = 0                         # Definiramo indeks početnog elementa u nizu
        while (vrh >= dno):
            srednji = int((vrh+dno)/2)   # Definiramo indeks razdvajanja niza (POLOVLJENJEM)
            print("Srednji: " + str(srednji))
            if(kljuc == self.Niz[srednji]):
                print("Tražena vrijednost " + str(kljuc) + " se nalazi na poziciji: " + str(srednji))
                return None
            elif(self.Niz[srednji] < kljuc):
                dno = srednji + 1       # Polovimo niz na način da odbacujemo sve elemente u lijevoj particiji niza
                print("Dno: " + str(dno))
            else:
                vrh = srednji - 1       # Polovimo niz na način da odbacujemo sve elemente u desnoj particiji niza
                print("Vrh: " + str(vrh))
        print("Tražena vrijednost " + str(kljuc) + " nije pronađena!")

    #Modifikovana metoda binarnoPretraživanje -> ModifikovanoBinarnoPretraživanje - izbacuje maksimalan element u sortiranom nizu
    def ModifikovanoBinarnoPretraživanje(self):
        if(self.duzina == 0):
            print("Niz je prazan.")
        else:
            vrh = self.duzina - 1
            self.tekuci = vrh
            self.izbaci()
        print("Maksimalan element je uklonjen.")

    # Interpolacijsko pretraživanje - traženi ključ porediti sa elementom koji je bliži traženoj vrijednosti čiju poziciju u konačnici određujemo interpolacijom
    def interpolacijskoPretrazivanje(self,kljuc):
        vrh = self.duzina - 1           # Definiramo indeks krajnjeg elementa u nizu
        dno = 0                         # Definiramo indeks početnog elementa u nizu
        while (vrh > dno):
            srednji = int(dno+((vrh-dno)*(kljuc-self.Niz[dno]))/(self.Niz[vrh]-self.Niz[dno]))              # Definiramo indeks razdvajanja niza (INTERPOLACIJOM)
            print("Srednji: " + str(srednji))
            if(srednji > self.duzina):                                                                      # Dogodi se matematički da je srednji izvan raspona indexa tj. dužine zadatog niza      
                print("Index izvan raspona! Tražena vrijednost " + str(kljuc) + " nije pronađena!")
                return None
            if(kljuc == self.Niz[srednji]):
                print("Tražena vrijednost " + str(kljuc) + " se nalazi na poziciji: " + str(srednji))
                return None
            elif(self.Niz[srednji] < kljuc):
                dno = srednji + 1       # Polovimo niz na način da odbacujemo sve elemente u lijevoj particiji niza
                print("Dno: " + str(dno))
            else:
                vrh = srednji - 1       # Polovimo niz na način da odbacujemo sve elemente u desnoj particiji niza
                print("Vrh: " + str(vrh))
        print("Tražena vrijednost " + str(kljuc) + " nije pronađena!")


    # Popuni listu nizom slučajnih brojeva
    def popuniListuRand(self): 
        for i in range(100,200):        
            self.dodaj(random.randint(1,i))

    # Popuni listu sortiranim nizom slučajnih brojeva
    def popuniListuSortRand(self):
        k = 100
        for i in range(100,200):
            k = random.randint(1,10)+k
            
            if (self.testDodaj(int(k))):
                self.dodaj(int(k))