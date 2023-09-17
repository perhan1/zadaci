import pyNizListe

# Nova klasa proširena pyNizLista - koja nasljeđuje sve od osnovne strukture
class prosirenaPyNizLista (pyNizListe.NizLista):

    def AritmetickaSredinaElemenata(self):
        suma = 0
        for i in range(0,self.duzina):
            suma += int(self.Niz[i])
        aritSr = suma/self.duzina
        print("Aritmetička sredina svih elemenata u listi je: " + str(aritSr))