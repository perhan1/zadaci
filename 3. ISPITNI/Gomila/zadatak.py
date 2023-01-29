# ZADATAK: Prošiti strukturu Gomila sa metodom koja će izračunati Kub sume elemenata gomile

# RJEŠENJE:
# Izmjeniti testni program
# 1. Inicirati novu proširenu strukturu
# 2. Dodati novokreiranu metodu

import pyGomile

# Nova proširena pyGomila struktura
class prosirenaGomila(pyGomile.Gomila):
    
    def kubSume(self, n): # Parametar n - veličina gomile
        if(self.velicina==0):
            print("\nGomila je prazna!\n")
        else:            
            suma = int(0)            
            for i in range (0,n):
                suma = suma + int(self.elementi[i])
            
            print("Kub sume elemenata gomile je: " + str(suma*suma*suma))