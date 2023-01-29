import pyNizListe
import random
import time
import cmath

# Sortitamo od najmanjeg prema najvećem

# Proširujemo osnovnu klasu NizListe sa metodama za sortiranje
class pySortiranjeNizListe(pyNizListe.NizLista):

# INSERTION Sort #
# Algoritam sortiranja umetanjem se temelji na međusobnom poređenju vrijednosti ključeva,
# pri čemu se u svakoj iteraciji održavaju sortirani i nesortirani dio niza. U svakom sljedećem
# koraku se iz nesortiranog dijela uzima jedan element i taj element se umeće na
# odgovarajuće mjesto u sortiranom dijelu. Prema tome, svakim novim korakom sortiranja,
# nesortirani dio niza se smanjuje, dok se sortirani dio niza postepeno povećava
    def insertionSort(self):
        start_time = time.time()
        
        for i in range (1, self.duzina):
            privremeni = self.Niz[i]
            j = i -1
            while ((j>= 0) and (self.Niz[j]>privremeni)):  # Poređenje sa sljedećim u listi i zamjena mjesta ukoliko je isti manji od trenutnog minimalnog(Pomjera se lijevo manji element)
                self.Niz[j+1] = self.Niz[j]
                j = j-1
            self.Niz[j+1]=privremeni
        
        print("Lista sortirana za " + str(time.time() - start_time) + " sekundi")


# Donald SHELL Sort #
# Algoritam Shell sort razdvaja početni niz na grupe, tako što se u svakoj grupi nalaze elementi koji su odvojeni jednakim razmakom u nizu.
# Zatim se svaka grupa sortira posebno primjenom osnovne varijante sortiranja umetanjem, nakon čega dobivamo niz sa većim stupnjem uređenosti u odnosu na početni niz.
# U zadnjem koraku, kada je ulazni niz „već gotovo sortiran“, primjenjujemo osnovnu varijantu sortiranja umetanjem.

    def shellSort(self):
        start_time = time.time()
        
        ListaRazmaka = [7,3,1]                # Lista razmaka

        for i in range(0,3):                  # Uzima razmak iz liste
            h = ListaRazmaka[i]   
            for j in range(h, self.duzina):   # Selection sort grupe
                privremeni = self.Niz[j]
                k = j - h
                while((k >= 0) and (self.Niz[k] > privremeni)):
                    self.Niz[k+h] = self.Niz[k]
                    k = k-h
                self.Niz[k+h] = privremeni
        
        print("Lista sortirana za " + str(time.time() - start_time) + " sekundi")

# SELECTION Sort #
# Pomjeranje podataka pri sortiranju obavlja se na način da se element direktno postavlja na njegovu konačnu poziciju u sortiranom nizu
# Sekvencijalnim pretraživanjem pronalazi najmanji element, koji se zatim premješta na prvu poziciju, dok se prethodni element s prve pozicije premješta na poziciju pronađenog minimalnog elementa.

    def selectionSort(self):
        start_time = time.time()
        
        if (self.duzina <= 0):
            print("Nema elemenata za sortiranje! Lista je prazna!")
        else:
            for i in range(0,self.duzina-1):
                minimalni = self.Niz[i]
                pozcijaminimalnog = i
                                
                for j in range(i+1,self.duzina):             # Pronalazak minimalnog elementa
                    if(self.Niz[j] < minimalni):
                        minimalni = self.Niz[j]
                        pozcijaminimalnog = j
                
                self.Niz[pozcijaminimalnog] = self.Niz[i]    # Korigujemo pozicije
                self.Niz[i] = minimalni
           
        print("Lista sortirana za " + str(time.time() - start_time) + " sekundi")

           
 


# BUBBLE Sort #
# Ovaj algoritam radi tako da više puta sekvencijalno prolazi kroz niz, pri čemu se pri svakom prolazu
# uspoređuje svaki element sa elementom koji se nalazi neposredno iza njega. Ako se nakon
# usporedbe utvrdi da susjedni elementi nisu u željenom poretku, onda elementi međusobno
# izmjenjuju svoje pozicije, što ima za posljedicu da se prema kraju niza postepeno pomjeraju
# elementi sa većim vrijednostima, ako je željeni poredak sortiranja rastući, ili da se prema
# kraju niza postepeno pomjeraju elementi sa manjim vrijednostima, ako je željeni poredak
# sortiranja opadajuć

    def bubbleSort(self):
        start_time = time.time()
        
        for i in range(self.duzina-1,0,-1):
            for j in range(1,i+1):
                if(self.Niz[j-1] > self.Niz[j]):
                    privremeni = self.Niz[j-1]
                    self.Niz[j-1]=self.Niz[j]
                    self.Niz[j] = privremeni

        print("Lista sortirana za " + str(time.time() - start_time) + " sekundi")



# MERGE Sort #

    # l - indeks prve pozicije ulaznog podniza
    # u - indeks zadnje pozicije ulaznog podniza
    # p - indeks zadnje pozicije prvog podniza
    # q - indeks prve pozicije drugog podniza
    # ulazni niz A[l..u] je podijeljen na podnizove A[l..p] i A[q..u].

    # Spajanje podnizova
    def Merge(self, l, p , q, u):        
        # Forsiramo int tip podataka za indekse u nizovima
        l = int(l)
        p = int(p)
        q = int(q)
        u = int(u)
        
        i = 0
        j = q-l
        k = l
        
        B = self.kreiraj_niz(u-l+1)
        for m in range(0,u-l+1):
            B[m] = self.Niz[l+m]
        
        while ((i <= p-l) and (j <= u-l)):
            if(B[i] < B[j]):
                self.Niz[k] = B[i]
                i+=1                
            else:
                self.Niz[k] = B[j]
                j+=1                
            k+=1

        while(i <= p-l):            
            self.Niz[k] = B[i]
            k+=1
            i+=1

        while(j <= u-l):           
            self.Niz[k] = B[j]
            k+=1
            j+=1

        del B

    # Merge Sort rekurzivno
    def MergeSort(self,l,u):
        # Forsiramo int tip podataka za indekse u nizovima
        l = int(l)
        u = int(u)

        if (u > l):
            p = (l+u-1)/2
            q = p + 1
            self.MergeSort(l,p)
            self.MergeSort(q,u)
            self.Merge(l,p,q,u)

    # Popuni listu nizom slučajnih brojeva
    def popuniListuRand(self): 
        for i in range(1,self.kapacitet):        
            self.dodaj(random.randint(1,1000))


# UNZE PTF ASP 2021/2022 :: M.S. :: 05.01.2021