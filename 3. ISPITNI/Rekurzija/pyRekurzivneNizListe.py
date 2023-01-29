import pyNizListe
import cmath

# Nova klasa proširena pyRekurzivneNizLista - koja nasljeđuje sve od osnovne strukture pyNizListe
class pyRekurzivneNizLista(pyNizListe.NizLista):

    
    # Izmjena pozicije elemenata
    def zamijeniti(self, i , j):
        priv = self.Niz[i]
        self.Niz[i] = self.Niz[j]
        self.Niz[j] = priv
    
    

    # Faktorijel novounesenog tekuceg elementa
    def tekuciFaktorijel(self, x):
        if x <= 1:
            return 1
        else: 
            return (x*self.tekuciFaktorijel(x-1))
    
    # -----------------------------------
    # ---------zadatak-vjezba------------
    # kreirati rekurzivni metod koji vraca kvadrat faktorijela novounesenog tekuceg elemente i ispisuje ga
    def KVtekuciFaktorijel(self, x):
        if self.tekuciFaktorijel(x)== 1:
            return 1
        else:
            y = pow(self.tekuciFaktorijel(x),2)
            return y
    
    #primjer zadatka preko rekurzivne funkcije tekuciFaktorijel()
    #def KVtekuciFaktorijel(self, x):
    #    temp = self.tekuciFaktorijel(x)
    #    temp = pow(temp, 2)
    #    print("Kvadrat faktorijela novounesenog tekućeg elementa je: " + str(temp))


    # Ispis permutacija elemenata
    def IspisiPermutacije(self, k ):
        if k == self.duzina - 1:
            self.prikazi()
        else:
            for i in range(k,self.duzina):
                self.zamijeniti(k,i)
                self.IspisiPermutacije(k+1)
                self.zamijeniti(k,i)

    # Ispis permutacije elementa od pozicije k do pozicije m
    def IspisiPermutacijeKdoM(self, k, m ):
        if k == m:
            self.prikazi()
        else:
            for i in range(k,m):
                self.zamijeniti(k,i)
                self.IspisiPermutacijeKdoM(k+1,m)
                self.zamijeniti(k,i)


