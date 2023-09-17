import pyJPRed

#proširena pyJPRed struktura
class prosirenaJPRed(pyJPRed.JPRed):

    def SumaElemenata(self):
         if(self.jeLiPrazan()):
            print("Red je prazan! Suma elemenata je 0!")
         else:
            privremeni = self.pocetak
            suma = 0            
            while(privremeni != None):
                suma += int(privremeni.element)
                privremeni = privremeni.sljedeci
            suma *=suma
            print("Kvadrat suma elemenata reda je: " + str(suma))
  