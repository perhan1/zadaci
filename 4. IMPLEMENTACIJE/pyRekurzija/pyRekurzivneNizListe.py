import pyNizListe

class pyRekurzivneNizLista(pyNizListe.NizLista):

    
    def zamijeniti(self, i , j):
        priv = self.Niz[i]
        self.Niz[i] = self.Niz[j]
        self.Niz[j] = priv
    

    def IspisiPermutacije(self, k ):
        if k == self.duzina - 1:
            self.prikazi()
        else:
            for i in range(k,self.duzina):
                self.zamijeniti(k,i)
                self.IspisiPermutacije(k+1)
                self.zamijeniti(k,i)

  
    def IspisiPermutacijeKdoM(self, k, m ):
        if k == m:
            self.prikazi()
        else:
            for i in range(k,m):
                self.zamijeniti(k,i)
                self.IspisiPermutacijeKdoM(k+1,m)
                self.zamijeniti(k,i)


