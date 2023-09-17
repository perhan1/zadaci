import pyCRed
import math

#proširena pyJPRed struktura
class prosirenaCRed(pyCRed.CRed):

    def KubAritmetickeSredine(self):
        suma = int(0)
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za kalkulaciju!.")
            return None
        else:
            i = self.pocetak
            while True:
               suma += int(self.Niz[i])
               i = (i +1) % self.kapacitet

               if (i == (self.kraj + 1) % self.kapacitet):
                    break
        arSredina = suma/self.duzina()
        print("Kub ASredine je: " + str(pow(arSredina,3)))
        
        
    def KorijenProizvoda(self):
        proizvod = int(1)
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za kalkulaciju!.")
            return None
        else:
            i = self.pocetak
            while True:
               proizvod *= int(self.Niz[i])
               i = (i +1) % self.kapacitet

               if (i == (self.kraj + 1) % self.kapacitet):
                    break
        print("Korijen proizvoda svih elemenata je: " + str(math.sqrt(proizvod)))
  