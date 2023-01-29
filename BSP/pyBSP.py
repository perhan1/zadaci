#####----------------------- OSNOVNA STRUKTURA -----------------------#####
# Definiramo BSCvor kao osnovni gradivni element strukture koji sadrži:
# Informacioni dio - element
# Pokazivač na lijevo stablo
# pokazivač na desno stablo
from types import prepare_class


class BSCvor():

    def __init__(self, element, lijevo = None, desno = None):
        self.element = element
        self.lijevo = lijevo
        self.desno = desno
    
    def __str__(self):
        return str(self.element)

######
# BSP bi mogli uraditi i sa podrškom za CHAR tip podataka, ali bi u tom slučaju za usporedbu morali korisiti ASCII vrijednosti za poređenje
# Radi jednostavnosti pristupa "forsiramo" tip podataka INT

# Definirama osnovnu klasu Binarnog Stabla Pretraživanja
class BSP():
    # Struktura se definira na način da se pokazivač korijen usmjeri na prvi BSCvor strukture 
    def __init__(self, korijen = None):
        self.korijen = korijen


#####-----------------------       METODE     -----------------------#####
    # Rekurzivno umetanje u BSP
    # pokazivač pokazuje na odgovarajući korijen stabla ili podstabla
    def umetniRekurzivno(self, pokazivac, x):
        if (pokazivac != None):
            if x <= pokazivac.element:
                if pokazivac.lijevo:
                    self.umetniRekurzivno(pokazivac.lijevo, x)
                else:
                    pokazivac.lijevo = BSCvor(x)
            else:
                if pokazivac.desno:
                    self.umetniRekurzivno(pokazivac.desno, x)
                else:
                    pokazivac.desno = BSCvor(x)
        else:
            self.korijen = BSCvor(x)
   
    def umetniIterativno(self, element):                     
        # Kreiramo novi čvor koji sadrži vrijednost za umetanje
        novicvor = BSCvor(element)
        
        pokazivac = self.korijen                           # prolazimo kroz stablo
        roditeljpokazivaca = None                          # pamtimo prethodni čvor kao roditelj, koji će biti i korijen novokreiranog stabla prilikom umetanja

        # Ukoliko je pokazivač popunjen vrijednošću, spuštamo se jedan nivo ispod
        while(pokazivac != None):            
            roditeljpokazivaca = pokazivac                 # U varijablu roditelja pamtimo prethodno podstablo
            if(novicvor.element < pokazivac.element):
                pokazivac = pokazivac.lijevo
            else:
                pokazivac = pokazivac.desno
                                                           # roditelj pokazivač je zapravo korijen ISPOD kojeg treba dodati novi element
        if (roditeljpokazivaca == None):
            self.korijen = novicvor                        # Ukoliko je roditelj pozicije u koju treba da se umetne novi element prazan, tada se radi o slučaju PRAZNOG Stabla i novi čvor se umeće na prvo mjesto
        else:
            if(novicvor.element < roditeljpokazivaca.element):
                roditeljpokazivaca.lijevo = novicvor       # Ako je vrijednost novog elementa manja - novi element se umeće lijevo
            else:
                roditeljpokazivaca.desno = novicvor        # Ako je vrijednost novog elementa veća - novi element se umeće desno     
        
        print("Umetnut novi element:" + str(element))
  

    def posjeti(self, tekuci):                             # Ispisuje (print) vriejdnost elementa za dati objekat bsp čvora
        print(str(tekuci.element), end=" ")     

    def inorder(self, korijen):                            # Ispis po INORDER redoslijedu
        if(korijen != None):
            self.inorder(korijen.lijevo)
            self.posjeti(korijen)
            self.inorder(korijen.desno)

    def preorder(self, korijen):                           # Ispis po PREORDER redoslijedu
        if(korijen != None):
            self.posjeti(korijen)            
            self.preorder(korijen.lijevo)
            self.preorder(korijen.desno)

    def postorder(self, korijen):                          # Ispis po POSTORDER redoslijedu
        if(korijen != None):
            self.postorder(korijen.lijevo)
            self.postorder(korijen.desno)            
            self.posjeti(korijen)

    def visina(self, korijen):                            # Ispisuje visinu stabla
        visinaLijevo = 0                                  
        visinaDesno = 0

        if(korijen != None):                 
            privremeniLijevo = korijen.lijevo             # Kalkulira lijevu "dubinu"
            while(privremeniLijevo != None):
                visinaLijevo =+ 1
                privremeniLijevo = privremeniLijevo.lijevo
            
            prviremeniDesno = korijen.desno               # Kalkulira desnu "dubinu"  
            while(prviremeniDesno != None):         
                visinaDesno =+ 1
                prviremeniDesno = prviremeniDesno.desno
            
            print("Lijeva visina je: " + str(visinaLijevo+1))   
            print("Desna visina je: " + str(visinaDesno+1))
            print("Visina stabla je: " + str(max(visinaDesno, visinaLijevo)+1))
        else:
            print("Stablo je prazno!")       
    
    def traziRekurzivno(self, pokazivac, x):                                # Rekurzivno pretraživanje
        if(self.korijen != None):
            if(pokazivac.element == x):
                return pokazivac
            else:
                trenutni = pokazivac
                if((x < trenutni.element) and (trenutni.lijevo != None)):   # Za manju vrijednost pretraga ide lijevo
                    print("Lijevo")
                    return self.traziRekurzivno(pokazivac.lijevo, x)
                if((x > trenutni.element) and (trenutni.desno != None)):    # Za veću vrijednost pretraga ide desno
                    print("Desno")
                    return self.traziRekurzivno(pokazivac.desno, x)
        else:
            print("Stablo prazno!")

    def traziIterativno(self, korijen, x):                                 # Iterativno pretraživanje
        while( (korijen != None) and (x != korijen.element) ):
            if(x < korijen.element):                                       # manje - lijevo
                korijen = korijen.lijevo
            else:
                korijen = korijen.desno                                    # veće - desno
        return korijen

    def brisiCvor(self, korijen, x):                                       # Brisanje čvora zadate vrijednosti x
        privremeni = korijen
        roditelj = None

        while((privremeni != None) and ( x != privremeni.element)):        # Pronalazimo čvor koji sadrži zadatu vrijednost
            roditelj = privremeni
            if (x < privremeni.element):
                privremeni = privremeni.lijevo
            else:
                privremeni = privremeni.desno

        if(privremeni == None):                                            # Ukoliko je privremeni prazan - tj. nije pronađen, nemamo šta brisati! 
            return False

        if(privremeni.lijevo == None):                                     # Kod hendla slučajeve restruktuiranja stabla nakon brisanja roditelja
            m = privremeni.desno
        else:
            if(privremeni.desno == None):
                m = privremeni.lijevo
            else:
                pm = privremeni
                m = privremeni.lijevo
                tmp = m.desno
                while(tmp != None):
                    pm = m
                    m = tmp
                    tmp = m.desno
                if(pm != privremeni):
                    pm.desno = m.lijevo
                    m.lijevo = privremeni.lijevo
                m.desno = privremeni.desno

        if(roditelj == None):
            korijen = m
        else:
            if(privremeni == roditelj.lijevo):
                roditelj.lijevo = m
            else:
                roditelj.desno = m
        del privremeni                                                     # brisanje čvora
        return True

   
    def minCvor(self, korijen):                                         # Zadnji element lijevo - minimum
        if(korijen == None):
            print("Stablo je prazno!")
        while(korijen.lijevo != None):
            korijen = korijen.lijevo
        return korijen

    def maxCvor(self, korijen):                                         # Zadnji element desno - maximum
        if(korijen == None):
            print("Stablo je prazno!")
        while(korijen.desno != None):
            korijen = korijen.desno
        return korijen

    
    