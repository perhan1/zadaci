import pyBSP

# Nova klasa proširena pyNizLista - koja nasljeđuje sve od osnovne strukture
class prosirenaBSCvor (pyBSP.BSP):
    # zadatak: Napisati funkciju UmetniMaxRPo() koja pronalazi maksimalan clan slabla i vrsi rekurzivno umetanje
    # novo clana cija je vrijednost uvecana za jedan u odnosu na max element
    # te ispituje elemente na postorder nacin
    def UmetniMaxRPo(self, korijen):
        maxCvor = self.maxCvor(korijen)
        noviMaxCvor = maxCvor.element + 1
        self.umetniRekurzivno(korijen, noviMaxCvor)
        print("Postorder ispis: \n")
        self.postorder(korijen)