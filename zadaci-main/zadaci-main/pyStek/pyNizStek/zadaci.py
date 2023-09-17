import pyNizStek

#prosirena pyNizStek struktura
class prosirenaNizStek(pyNizStek.NizStek):

    def ProizvodElemenata(self):
        if(self.jeLiPrazan()):
            print("Stek je prazan!")
        else:
            proizvod = 1    
            for i in range(self.vrh,-1,-1):
                proizvod = proizvod * int(self.Niz[i]) 
                i += 1
            print("Proizvod elemenata steka je: " + str(proizvod))

    