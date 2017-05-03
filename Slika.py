
from tkinter import *

from ScapeGoat import *
from ScapeGoatTree import *
class Slika():
    def __init__(self,master,sirina=800,visina=800,drevo=ScapeGoat()):

        self.visina=visina
        self.sirina=sirina
        self.drevo=drevo
        
        self.dodajam = IntVar(master, value=0)
        self.dodajam.trace("w", self.nastavi)

        self.b = IntVar(master, value=self.dodajam.get())
        polje_b = Label(master, textvariable=self.b)
        polje_b.pack()
        
        polje_a = Entry(master, textvariable=self.dodajam)
        polje_a.pack()

        frame = Frame(master) # Ta okvir je vsebovan v master-ju
        frame.pack()


        gumb_povecaj = Button(frame, text="dodaj", command=self.vstavi)
        gumb_povecaj.pack()


        
        self.platno=Canvas(master, width=self.sirina, height=self.visina)
        self.platno.pack()
        
        


 

        self.kordinate=[]
        #funkcija miske
        self.platno.bind("<Button-1>", self.zbrisi)

        
        
        

     #miska   
    def zbrisi(self, event):
        '''Nariši krogec, kjer trenutno stoji miška.'''
        self.platno.create_oval(event.x-5, event.y-5, event.x+5, event.y+5)
        brisan=None
        for x in self.kordinate:
            if abs(event.x-x[0])<20 and abs(event.y-x[1])<20:
                brisan=x[2]
        if brisan!=None:
            self.drevo.remove(brisan)
            self.kordinate=self.drevo.kordinate()
            self.narisi()
            
            
    def nastavi(self,name, index, mode):
        try:
            self.b.set(self.dodajam.get())
            
        except:

            self.b.set(0)


    def vstavi(self):
        
        try:
            k=self.dodajam.get()
        except:
            k=0
        self.drevo.insert(k)
        self.kordinate=self.drevo.kordinate()
        self.narisi()

     
    
        
    def narisi(self):
        self.platno.delete("all")
        for x in self.kordinate:
            self.platno.create_text(x[0], x[1], text=str(x[2]))
            if x[3]==True:
                self.platno.create_line(x[0],x[1],x[0]-x[5],x[1]+100)
            if x[4]==True:
                self.platno.create_line(x[0],x[1],x[0]+x[5],x[1]+100)            
root = Tk()

aplikacija = Slika(root,800,800,ScapeGoatTree())

#Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha

# delovati, ko okno zapremo.
root.mainloop()
