import time
# ZADATAK: Modificirajte algoritam Shell sort prikazan na vježbama, tako da se ne koristi niz razmaka kao argument, 
#          nego je on ugrađen u algoritam logiku:“dijeljenje sa 3”.

# RJEŠENJE:
# Izmjeniti testni program
# 1. Inicirati novu proširenu strukturu
# 2. Dodati novokreiranu metodu

import pySortiranja

# Nova proširena pyGomila struktura
class prosirenoSortiranjeNizListe(pySortiranja.pySortiranjeNizListe):
    
    def modificiraniShellSort(self):
        start_time = time.time()
        
        # --- RJEŠENJE START ---
        # Potrebno je popuniti listu razmaka sa traženom logikom, te istu iskoristiti za standardni shell sort
        # Prvi element liste razamka je self.duzina/3, drugi element razmaka je (self.duzina/3)/3, treći element razmaka je ((self.duzina/3)/3)/3
        # Razmak popunajvamo sve dok je vrijednost novog razmaka < 1
        # Zadnji element mora biti 1
                
        ListaRazmaka = []                     # Lista razmaka, prazna

        r = self.duzina                       # Prvi, najveći element u listi razmaka

        while True:                           # Petlja koje se vrti dok god su dobiveni razmaci veći od 1            
            r = int(r/3)
            if(r) < 1:
                break
            ListaRazmaka.append(r)            # list.append(x) - Add an item to the end of the list. https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        
        ListaRazmaka.append(1)                # Dodajemo 1 na kraj liste

        print("Lista razmaka:")               # Ispis liste razamka
        print(*ListaRazmaka)

       # --- RJEŠENJE END ---

       # --- Standardni shell sort ---
        for i in range(0,len(ListaRazmaka)):  # Uzima razmak iz list. Potrebno je korigovari 
            h = ListaRazmaka[i]            
            for j in range(h, self.duzina):   # Selection sort grupe
                privremeni = self.Niz[j]
                k = j - h
                while((k >= 0) and (self.Niz[k] > privremeni)):
                    self.Niz[k+h] = self.Niz[k]
                    k = k-h
                self.Niz[k+h] = privremeni
        
        print("Lista sortirana za " + str(time.time() - start_time) + " sekundi")