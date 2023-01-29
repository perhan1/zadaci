
from types import prepare_class


class BSCvor():

    def __init__(self, element, lijevo = None, desno = None):
        self.element = element
        self.lijevo = lijevo
        self.desno = desno
    
    def __str__(self):
        return str(self.element)


class BSP():

    def __init__(self, korijen = None):
        self.korijen = korijen


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
        novicvor = BSCvor(element)
        
        pokazivac = self.korijen                           
        roditeljpokazivaca = None                          

        while(pokazivac != None):            
            roditeljpokazivaca = pokazivac                 
            if(novicvor.element < pokazivac.element):
                pokazivac = pokazivac.lijevo
            else:
                pokazivac = pokazivac.desno
                                                           
        if (roditeljpokazivaca == None):
            self.korijen = novicvor                        
        else:
            if(novicvor.element < roditeljpokazivaca.element):
                roditeljpokazivaca.lijevo = novicvor       
            else:
                roditeljpokazivaca.desno = novicvor        
        
        print("Umetnut novi element:" + str(element))
  

    def posjeti(self, tekuci):                             
        print(str(tekuci.element), end=" ")     

    def inorder(self, korijen):                            
        if(korijen != None):
            self.inorder(korijen.lijevo)
            self.posjeti(korijen)
            self.inorder(korijen.desno)

    def preorder(self, korijen):                          
        if(korijen != None):
            self.posjeti(korijen)            
            self.preorder(korijen.lijevo)
            self.preorder(korijen.desno)

    def postorder(self, korijen):                         
        if(korijen != None):
            self.postorder(korijen.lijevo)
            self.postorder(korijen.desno)            
            self.posjeti(korijen)

    def visina(self, korijen):                            
        visinaLijevo = 0                                  
        visinaDesno = 0

        if(korijen != None):                 
            privremeniLijevo = korijen.lijevo             
            while(privremeniLijevo != None):
                visinaLijevo =+ 1
                privremeniLijevo = privremeniLijevo.lijevo
            
            prviremeniDesno = korijen.desno                
            while(prviremeniDesno != None):         
                visinaDesno =+ 1
                prviremeniDesno = prviremeniDesno.desno
            
            print("Lijeva visina je: " + str(visinaLijevo+1))   
            print("Desna visina je: " + str(visinaDesno+1))
            print("Visina stabla je: " + str(max(visinaDesno, visinaLijevo)+1))
        else:
            print("Stablo je prazno!")       
    
    def traziRekurzivno(self, pokazivac, x):                                
        if(self.korijen != None):
            if(pokazivac.element == x):
                return pokazivac
            else:
                trenutni = pokazivac
                if((x < trenutni.element) and (trenutni.lijevo != None)):   
                    print("Lijevo")
                    return self.traziRekurzivno(pokazivac.lijevo, x)
                if((x > trenutni.element) and (trenutni.desno != None)):    
                    print("Desno")
                    return self.traziRekurzivno(pokazivac.desno, x)
        else:
            print("Stablo prazno!")

    def traziIterativno(self, korijen, x):                                 
        while( (korijen != None) and (x != korijen.element) ):
            if(x < korijen.element):                                       
                korijen = korijen.lijevo
            else:
                korijen = korijen.desno                                    
        return korijen

    def brisiCvor(self, korijen, x):                                       
        privremeni = korijen
        roditelj = None

        while((privremeni != None) and ( x != privremeni.element)):        
            roditelj = privremeni
            if (x < privremeni.element):
                privremeni = privremeni.lijevo
            else:
                privremeni = privremeni.desno

        if(privremeni == None):                                           
            return False

        if(privremeni.lijevo == None):                                     
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
        del privremeni                                                     
        return True

   
    def minCvor(self, korijen):                                         
        if(korijen == None):
            print("Stablo je prazno!")
        while(korijen.lijevo != None):
            korijen = korijen.lijevo
        return korijen

    def maxCvor(self, korijen):                                         
        if(korijen == None):
            print("Stablo je prazno!")
        while(korijen.desno != None):
            korijen = korijen.desno
        return korijen

    
    