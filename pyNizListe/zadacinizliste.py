import pyNizListe

# Nova klasa proširena pyNizLista - koja nasljeđuje sve od osnovne strukture
class prosirenaPyNizLista (pyNizListe.NizLista):
    
    # Rješenje zadatka se kodira kao proširena metoda
  
    def KvadratSumeElemenata(self):
        sum = 0
        for i in range(0,self.duzina):
             sum += int(self.Niz[i])
        suma1 = sum*sum
        print("Kvadrat sume svih elemenata u listi je: " + str(suma1))
    
    def AritmetickaSredinaElemenata(self):
        suma = 0
        for i in range(0,self.duzina):
            suma += int(self.Niz[i])
        aritSr = suma/self.duzina
        print("Aritmetička sredina svih elemenata u listi je: " + str(aritSr))
    
    def SumaElemenata(self):
        suma = 0
        for i in range(0,self.duzina):
            suma += int(self.Niz[i])
        print("Suma svih elemenata u listi je: " + str(suma))

    def KubAritmetickeSredineElemenata(self):
        suma = 0
        for i in range(0,self.duzina):
            suma += int(self.Niz[i])
        aritSr = suma/self.duzina
        KubArSr = aritSr*aritSr*aritSr
        print("Aritmetička sredina svih elemenata u listi je: " + str(KubArSr))
    
    def ProizvodElemenata(self):
        proizvod = 1
        for i in range(0,self.duzina):
            proizvod *= int(self.Niz[i])
        print("Proizvod svih elemenata u listi je: " + str(proizvod))

    def DodajSumuUSredinu(self):
        sum = 0
        for i in range(0,self.duzina):
            sum += int(self.Niz[i])
        if self.duzina % 2 == 0:
            srListe = int(self.duzina/2)
            temp = self.kreiraj_niz(self.duzina+1)
            for i in range(0,srListe):
                temp[i] = int(self.Niz[i])
            temp[srListe] = sum
            for i in range(srListe+1,self.duzina):
                temp[i] = int(self.Niz[i])
            self.Niz = temp
            print("Suma je dodana u sredinu liste.")
        else: 
            self.dodaj(sum)
            print("Suma je dodana na kraj liste.")
