import pyJPStek

#proširena pyJPStek struktura
class prosirenaJPStek(pyJPStek.JPStek):

    def aSredina(self):
         if(self.jeLiPrazan()):
            print("Stek je prazan! Nema elemenata za računanje aritmetičke sredine!")
         else:
            privremeni = self.vrh
            suma = 0            
            while(privremeni != None):
                suma += int(privremeni.element)
                privremeni = privremeni.sljedeci
            
            print("AS steka je: " + str( suma/self.duzina()))

    def SumaElemenata(self):
         if(self.jeLiPrazan()):
            print("Stek je prazan! Suma elemenata je 0!")
         else:
            privremeni = self.vrh
            suma = 0            
            while(privremeni != None):
                suma += int(privremeni.element)
                privremeni = privremeni.sljedeci
            print("Suma elemenata steka je: " + str(suma))
    
    def ProizvodElemenata(self):
         if(self.jeLiPrazan()):
            print("Stek je prazan!")
         else:
            privremeni = self.vrh
            proizvod = 1           
            while(privremeni != None):
                proizvod *= int(privremeni.element)
                privremeni = privremeni.sljedeci
            print("Proizvod elemenata steka je: " + str(proizvod))