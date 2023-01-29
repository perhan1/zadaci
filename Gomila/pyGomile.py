import ctypes

class maxTip():
    def prior(self,x,y):
        return x > y

class minTip():
    def prior(self,x,y):
        return x < y

class Gomila():
   
    # Metoda kreira niz kapaciteta k -- ctypes --za dodatni info pogledati pyNizListe
    def kreiraj_niz(self, k):
        return (ctypes.py_object * k)()

    # Iniciranje gomile
    def __init__(self, maxduzina, tip):
        self.kapacitet = maxduzina                              # kapacitet niza odnosno gomile
        self.velicina = 0                                       # trenutna veličina gomile
        self.elementi = self.kreiraj_niz(self.kapacitet)        # Niz u kojem čuvamo podatke
        self.tipPoretka = tip                                   # tip poretka - kalsa minTip ili maxTip
        self.duzinaNiza = 0                                     # broj elemenata prisutnih u nizu   

    # Ispistuje da li je čvor na indexu i list
    # Funkcija vraća true ako je čvor s indeksom i list, odnosno vrijednost false ako dotični čvor nije list.
    def jeLiList(self, i):
        return ((i >= self.velicina/2) and (i < self.velicina))
    
    # Pozicija lijevog djeteta
    def lijevoDijete(self, i):
        return int(2*i+1)

    # Pozicija desnog djeteta
    def desnoDijete(self, i):
        return int(2*i+2)

    # Pozicija roditelja
    def roditelj(self,i):
        return int((i-1)/2)

    # -----------------------------------
    # Izmjena pozicija
    def zamjeni (self, i , j):
        privremeni = self.elementi[i]
        self.elementi[i]=self.elementi[j]
        self.elementi[j]=privremeni

    # Popravljanje spuštanjem
    def popraviDole(self, i):
        while (self.jeLiList(i) != True):
            veci = self.lijevoDijete(i)
            dd = self.desnoDijete(i)           

            if ((dd < self.velicina) and (self.tipPoretka.prior(self.elementi[dd],self.elementi[veci]))):
                veci = dd
            if (self.tipPoretka.prior(self.elementi[i],self.elementi[veci])):
                return; 
            self.zamjeni(i,veci)
            i = veci
   
    # Popravljanje podizanjem
    def popraviGore(self, i):
        while ((i != 0) and (self.tipPoretka.prior(self.elementi[i],self.elementi[self.roditelj(i)]))):
            self.zamjeni(i,self.roditelj(i))
            i=self.roditelj(i)

    # Stvaranje gomile
    def stvoriGomilu(self):
        self.velicina=self.duzinaNiza
        for i in range(int(self.velicina/2-1),-1,-1):
            self.popraviDole(i)
        print("Gomila kreirana!") 

    # Umetanje u gomilu
    def umetniUGomilu(self, x):
        if (self.velicina > self.kapacitet-1):
            print("Gomila je puna")
        else:                                   
            self.elementi[self.velicina] = x
            self.velicina = self.velicina + 1 
            self.popraviGore(self.velicina-1)            
            print("Vrijednost " + str(x) + " umetnuta u gomilu!")

    # Izbacivanje prvog elementa
    def izbaciPrvi(self):
        if(self.velicina==0):
            print("\nGomila je prazna!\n")
        else:
            self.velicina = self.velicina - 1
            self.zamjeni(0,self.velicina)
            if (self.velicina!=0):
                self.popraviDole(0)                
            print("Prvi element izbačen!")
            return self.elementi[self.velicina]
    
    # Izbacivanje elementa na poziciji i
    def izbac(self, i):
        if ( (i < 0) or (i >= self.velicina-1)):
            print("\nPogresan indeks!\n")
        else:
            self.velicina = self.velicina - 1
            self.zamjeni(i,self.velicina)
            self.popraviGore(i)
            self.popraviDole(i)
            return self.elementi[self.velicina]
    
    # Promjena vrijednosti ključa
    def promjeniKljuc(self, i, x):
        if (self.tipPoretka.prior(x,self.elementi[i]) == False):
            print("Greska\n")
        else:
            self.elementi[i]=x
            self.popraviGore(i)
            print("Vrijednost promjenjena!\n")

     # Učitavanje u niz
    def ucitaj (self, n):
        self.velicina = 0
        for i in range(0,n):
           x = input("Unesite vrijednost elementa za dodavanje u početni niz?\n")            
           self.elementi[i] = int(x)
        self.duzinaNiza = n
        print("Niz učitan!")

    # Prikaz sadržaja niza
    def prikazi (self, n):
        for i in range (0,n):
            print(str(i)+": " + str(self.elementi[i]))

# UNZE PTF ASP 2021/2022 :: M.S. :: 12.01.2022

