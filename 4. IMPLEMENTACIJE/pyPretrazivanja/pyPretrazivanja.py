import pyNizListe
import random

class pyPretrazivanjeNizListe(pyNizListe.NizLista):
    


    def sekvencijalnoPretrazivanje(self, kljuc):
        i = 0
        while(i < self.duzina):
            if(self.Niz[i] == kljuc):
                print("Tražena vrijednost " + str(kljuc) + " se nalazi na poziciji: " + str(i))
                return None
            else:
                i += 1
                print("Ispitivanje "+ str(i)+"!\n")
        if(i == self.duzina):                                                       
            print("Tražena vrijednost " + str(kljuc) + " nije pronađena!")


    def testUmetni(self, x):
        if(self.duzina == 0):   
            return True
        if(self.tekuci < self.duzina and x > self.Niz[self.tekuci]) or (self.tekuci == self.duzina and x < self.Niz[self.tekuci-1]):
            return False
        else:
            return True
    
    def testDodaj(self, x):
        if(self.duzina == 0):   
            return True
        if(x < self.Niz[self.duzina-1]): 
            return False
        else:
            return True

  
    def binarnoPretrazivanje(self, kljuc):
        vrh = self.duzina - 1           
        dno = 0                         
        while (vrh >= dno):
            srednji = int((vrh+dno)/2)   
            print("Srednji: " + str(srednji))
            if(kljuc == self.Niz[srednji]):
                print("Tražena vrijednost " + str(kljuc) + " se nalazi na poziciji: " + str(srednji))
                return None
            elif(self.Niz[srednji] < kljuc):
                dno = srednji + 1       
                print("Dno: " + str(dno))
            else:
                vrh = srednji - 1       
                print("Vrh: " + str(vrh))
        print("Tražena vrijednost " + str(kljuc) + " nije pronađena!")


    
    def interpolacijskoPretrazivanje(self,kljuc):
        vrh = self.duzina - 1           
        dno = 0                         
        while (vrh > dno):
            srednji = int(dno+((vrh-dno)*(kljuc-self.Niz[dno]))/(self.Niz[vrh]-self.Niz[dno]))              
            print("Srednji: " + str(srednji))
            if(srednji > self.duzina):                                                                      
                print("Index izvan raspona! Tražena vrijednost " + str(kljuc) + " nije pronađena!")
                return None
            if(kljuc == self.Niz[srednji]):
                print("Tražena vrijednost " + str(kljuc) + " se nalazi na poziciji: " + str(srednji))
                return None
            elif(self.Niz[srednji] < kljuc):
                dno = srednji + 1       
                print("Dno: " + str(dno))
            else:
                vrh = srednji - 1       
                print("Vrh: " + str(vrh))
        print("Tražena vrijednost " + str(kljuc) + " nije pronađena!")


    def popuniListuRand(self): 
        for i in range(100,200):        
            self.dodaj(random.randint(1,i))

    def popuniListuSortRand(self):
        k = 100
        for i in range(100,200):
            k = random.randint(1,10)+k
            
            if (self.testDodaj(int(k))):
                self.dodaj(int(k))

    def ModifikovanoBinarnoPretraživanje(self):
        if(self.duzina == 0):
            print("Niz je prazan.")
        else:
            vrh = self.duzina - 1
            self.tekuci = vrh
            self.izbaci()
        print("Maksimalan element je uklonjen.")