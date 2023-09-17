import pyJPListe
import math

# nova klasa proširena pyJPLista - nasljeđuje sve metode od pyJPListe

class prosirenaJPLista(pyJPListe.JPlista):
  
    def AritmetickaSredina(self):
        sum = int(0)
        privremeni = self.pocetak
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna. Nemoguće izračunati aritmetičku sredinu!")
        else:
             while(privremeni != None):
                 sum += int(privremeni.element)
                 privremeni = privremeni.sljedeci
        aritsredina = sum/(self.lduzina + self.dduzina)
        print("Aritmetička sredina svih elemenata u listi je: " + str(aritsredina))

    def KvadratAritSredine(self):
        sum = int(0)
        privremeni = self.pocetak
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna. Nemoguće izračunati kvadrat aritmetičke sredine!")
        else:
             while(privremeni != None):
                 sum += int(privremeni.element)
                 privremeni = privremeni.sljedeci
        aritsredina = sum/(self.lduzina + self.dduzina)
        print("Kvadrat aritmetičke sredine svih elemnata u listi je: " + str(math.pow(aritsredina,2)))


    def KubSume(self):
        sum = int(0)
        privremeni = self.pocetak
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna. Nemoguće izračunati kub sume elemenata liste!")
        else:
             while(privremeni != None):
                 sum += int(privremeni.element)
                 privremeni = privremeni.sljedeci
        kubSume = math.pow(sum,3)
        print("Kub sume svih elemenata u listi je: " + str(kubSume))
    
    def KorijenProizvoda(self):
        proizvod = int(1)
        privremeni = self.pocetak
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna. Nemoguće izračunati korijen proizvoda elemenata liste!")
        else:
             while(privremeni != None):
                 proizvod *= int(privremeni.element)
                 privremeni = privremeni.sljedeci
        korijenProizvoda = math.sqrt(proizvod)
        print("Korijen proizvoda svih elemenata u listi je: " + str(korijenProizvoda))
    

    def DodajSumuNaKraj(self):
        sum = int(0)
        privremeni = self.pocetak
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna.")
        else:
            while(privremeni != None):
                sum += int(privremeni.element)
                privremeni = privremeni.sljedeci
        self.dodaj(sum)
        self.prikazi()

    def DodajElUSredinu(self,x):
        privremeni = self.pocetak
        i = int(0)
        while privremeni != None:
            privremeni = privremeni.sljedeci
            i += 1
        if i % 2 == 0:
            self.idiNaPoziciju(int(i/2))
            self.umetni(x)
            print("Sljedeći element je umetnut u sredinu liste: " + str(x))
        else:
            self.idiNaPocetak()
