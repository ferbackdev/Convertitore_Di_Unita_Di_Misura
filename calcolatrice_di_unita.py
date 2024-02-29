from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class CalcolatriceDiUnita():
    ################# colori ###############
    co0 = "#444466"  
    co1 = "#feffff"  
    co2 = "#6f9fbd"  
    co3 = "#3f3f3f"
    sfondo = "#484f60" 
    #######################################
    def __init__(self, root=Tk()):
        self.root = root
        self.root.title("Calcolatrice di unità")
        self.root.geometry('800x260')
        self.root.configure(bg='lightgray')
        self.root.resizable(width=False, height=False)
        #------------ aplicando estilo ----------------
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        
        # 3 frame
        self.frame1 = Frame(self.root, width=460, height=50, bg="lightgray", pady=0, padx=3, relief="flat")
        self.frame1.grid(row=0, column=0, columnspan= 3)
        
        self.l_title = Label(self.frame1, text="Calcolatrice di Unità di Misura", 
                           height=1, padx=0, relief="flat", anchor="center", justify="center",
                           font=('Ivy 18 bold'), bg='lightgray', fg=self.co3)
        self.l_title.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        self.unita = {
            'Peso':[{'kg':1000},{'hg':100},{'dag':10},{'g':1},{'dg':0.1},{'cg':0.01},{'mg':0.001}],
            'Lunghezza':[{'km':1000},{'hm':100},{'dam':10},{'m':1},{'dm':0.1},{'cm':0.01},{'mm':0.001}],
            'Tempo':[{'s':1},{'min':60},{'h':3600},{'gg':86400},{'m':2592000},{'a':31536000}],
            'Area':[{'km²':1000000},{'hm²':10000},{'dam²':100},{'m²':1},{'dm²':0.01},{'cm²':0.0001},{'mm²':0.000001}],
            'Quantita':[{'km³':1000000000},{'hm³':1000000},{'dam³':1000},{'m³':1},{'dm³':0.001},{'cm³':0.000001},{'mm³':0.000000001}],
            'Velocita':[{'km/h': 1000/3600},{'m/s':1},{'m/min':1/60},{'cm/s':0.01},{'mm/s':0.001}],
            'Temperatura':[{'°C':1},{'°F':1.8},{'K':1}],
            'Energia':[{'J':1},{'kJ':1000},{'cal':4.184},{'kcal':4184},{'Wh':3600},{'kWh':3600000}],
            'Pressione':[{'Pa':1},{'hPa':100},{'atm':101325},{'bar':100000},{'psi':6894.7572931783}]
        }
        
        self.frame2 = Frame(self.root, width=460, height=70, bg="lightgray", pady=1, padx=3, relief="flat",)
        self.frame2.grid(row=1, column=0, columnspan= 3, sticky=NSEW)
        # bottone e immagine per Peso
        self.img_0 = Image.open('images/peso.png')
        self.img_0 = self.img_0.resize((50, 50))
        self.img_0 = ImageTk.PhotoImage(self.img_0)
        self.b_0 = Button(self.frame2, text="Peso", width=150, height=50, 
                     image=self.img_0, compound=LEFT, anchor="nw", relief=FLAT, 
                     overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold'))
        self.b_0.grid(row=1, column=0,  sticky=NSEW, pady=5, padx=5)
        
        # bottone e immagine per Tempo
        self.img_1 = Image.open('images/tempo.png')
        self.img_1 = self.img_1.resize((50, 50))
        self.img_1 = ImageTk.PhotoImage(self.img_1)
        self.b_1 = Button(self.frame2, text="Tempo", width=150, height=50, 
                          image=self.img_1, compound=LEFT, anchor="nw", relief=FLAT, 
                          overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold') )
        self.b_1.grid(row=1, column=1,  sticky=NSEW, pady=5, padx=5)
        
        # bottone e immagine per Lunghezza
        self.img_2 = Image.open('images/lunghezza.png')
        self.img_2 = self.img_2.resize((45, 45))
        self.img_2 = ImageTk.PhotoImage(self.img_2)
        self.b_2 = Button(self.frame2, text="Lunghezza", width=150, height=50, 
                          image=self.img_2, compound=LEFT, anchor="nw", relief=FLAT, 
                          overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold') )
        self.b_2.grid(row=1, column=2,  sticky=NSEW, pady=5, padx=5)
        # bottone e immagine per Area
        self.img_3 = Image.open('images/area.png')
        self.img_3 = self.img_3.resize((50, 50))
        self.img_3 = ImageTk.PhotoImage(self.img_3)
        self.b_3 = Button(self.frame2, text="Área", width=150, height=50, 
                          image=self.img_3, compound=LEFT, anchor="nw", relief=FLAT, 
                          overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold') )
        self.b_3.grid(row=2, column=0,  sticky=NSEW, pady=5, padx=5)
        # bottone e immagine per Quantità
        self.img_4 = Image.open('images/quantita.png')
        self.img_4 = self.img_4.resize((50, 50))
        self.img_4 = ImageTk.PhotoImage(self.img_4)
        self.b_4 = Button(self.frame2, text="Quantita", width=150, height=50, 
                          image=self.img_4, compound=LEFT, anchor="nw", relief=FLAT, 
                          overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold') )
        self.b_4.grid(row=2, column=1,  sticky=NSEW, pady=5, padx=5)
        # bottone e immagine per Velocità
        self.img_5 = Image.open('images/velocita.png')
        self.img_5 = self.img_5.resize((50, 50))
        self.img_5 = ImageTk.PhotoImage(self.img_5)
        self.b_5 = Button(self.frame2, text="Velocita", width=150, height=50, 
                          image=self.img_5, compound=LEFT, anchor="nw", relief=FLAT, 
                          overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold') )
        self.b_5.grid(row=2, column=2,  sticky=NSEW, pady=5, padx=5)
        # bottone e immagine per Temperatura
        self.img_6 = Image.open('images/temperature.png')
        self.img_6 = self.img_6.resize((50, 50))
        self.img_6 = ImageTk.PhotoImage(self.img_6)
        self.b_6 = Button(self.frame2, text="Temperatura", width=150, height=50, 
                          image=self.img_6, compound=LEFT, anchor="nw", relief=FLAT, 
                          overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold') )
        self.b_6.grid(row=3, column=0,  sticky=NSEW, pady=5, padx=5)
        # bottone e immagine per Energia
        self.img_7 = Image.open('images/energia.png')
        self.img_7 = self.img_7.resize((50, 50))
        self.img_7 = ImageTk.PhotoImage(self.img_7)
        self.b_7 = Button(self.frame2, text="Energia", width=150, height=50, 
                          image=self.img_7, compound=LEFT, anchor="nw", relief=FLAT, 
                          overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold') )
        self.b_7.grid(row=3, column=1,  sticky=NSEW, pady=5, padx=5)
        # bottone e immagine per Pressione
        self.img_8 = Image.open('images/pressione.png')
        self.img_8 = self.img_8.resize((50, 50))
        self.img_8 = ImageTk.PhotoImage(self.img_8)
        self.b_8 = Button(self.frame2, text="Pressione", width=150, height=50, 
                          image=self.img_8, compound=LEFT, anchor="nw", relief=FLAT, 
                          overrelief=SOLID, bg=self.co2, fg=self.co0, font=('Ivy 12 bold') )
        self.b_8.grid(row=3, column=2,  sticky=NSEW, pady=5, padx=5)
                
        self.frame3 = Frame(self.root, width=240, height=50, bg="lightgray", pady=3, padx=2, relief="flat")
        self.frame3.grid(row=0, column=3, columnspan=3, sticky=NSEW)
        self.l_unita = Label(self.frame3,width=23, text="", anchor=CENTER, 
                             height=2,pady=0, padx=0, relief="groove", 
                             font=('Ivy 15 bold'), bg=self.co2, fg=self.co1)
        self.l_unita.grid(row=0, column=3)
        
        
        self.frame4 = Frame(self.root, width=280, height=198, bg="lightgray",relief="flat")
        self.frame4.grid(row=1, column=3, rowspan=5, columnspan=3, sticky=NW, pady=5, padx=5)
        
        self.l_da = Label(self.frame4,text="Da", height=1, width=14, relief="groove", 
                          font=('Ivy 12 bold'), bg=self.co0, fg=self.co1)
        self.l_da.grid(row=1, column=0,columnspan=4, padx=5, pady=5, sticky=NSEW)    
        self.c_da = ttk.Combobox(self.frame4, width=15,justify='center', font=('Ivy 8 bold'))
        self.c_da.grid(row=1, column=4, columnspan=2, padx=5, pady=5)
        
        self.l_a = Label(self.frame4, text="A", height=1, width=14, relief="groove", 
                         font=('Ivy 12 bold'), bg=self.co0, fg=self.co1)
        self.l_a.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=NSEW) 
        self.c_a = ttk.Combobox(self.frame4, width=15, justify='center',font=('Ivy 8 bold'))
        self.c_a.grid(row=2, column=4, columnspan=2, padx=5, pady=5)
       
        self.l_valore = Label(self.frame4, text="Valore",height=1, relief="groove", 
                              font=('Ivy 12 bold'), bg=self.co0, fg=self.co1)
        self.l_valore.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=NSEW)
        self.e_valore = Entry(self.frame4, width=15, justify='center', font=('Ivy 9 bold'))
        self.e_valore.grid(row=3, column=4, columnspan=2, padx=5, pady=5)
        
        self.b_calcola = Button(self.frame4, text="Calcola", width=5, height=1, state='disabled',
                                relief="groove", font=('Ivy 12 bold'), bg=self.co2, fg=self.co1)
        self.b_calcola.grid(row=4, column=4, columnspan=3, padx=5, pady=5, sticky=NSEW)
        self.b_reset = Button(self.frame4, text="Reset", width=5, height=1, state='disabled',
                                relief="groove", font=('Ivy 12 bold'), bg=self.co2, fg=self.co1)
        self.b_reset.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky=NSEW)
        
        self.l_risultato = Label(self.frame4, text="Risultato", anchor=NW,
                                    height=1,pady=0, padx=3, relief="groove", 
                                    font=('Ivy 12 bold'), bg=self.co0, fg=self.co1)
        self.l_risultato.grid(row=5, column=0, columnspan=2, padx=5, pady=15, sticky=NSEW)
        self.e_risultato = Entry(self.frame4, width=5, font=('Ivy 12 bold'), justify='center', state='readonly')
        self.e_risultato.grid(row=5, column=2, columnspan=4, padx=5, pady=15, sticky=NSEW)
        
        self.e_valore.bind("<KeyRelease>", self.attiva_calcola)
        self.b_calcola.bind("<Button-1>", self.calcola)
        self.b_reset.bind("<Button-1>", self.reset)   
        self.b_0.bind("<Button-1>", self.peso) 
        self.b_1.bind("<Button-1>", self.tempo)
        self.b_2.bind("<Button-1>", self.lunghezza)
        self.b_3.bind("<Button-1>", self.area)
        self.b_4.bind("<Button-1>", self.quantita)
        self.b_5.bind("<Button-1>", self.velocita)
        self.b_6.bind("<Button-1>", self.temperatura)
        self.b_7.bind("<Button-1>", self.energia)      
        self.b_8.bind("<Button-1>", self.pressione)
        
    def control_button(self):
        #se il bottone * è stato premuto, gli altri devono avere il colore di default 
        if self.l_unita.cget("text") == "Peso":
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "Tempo":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "Lunghezza":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "Area":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "Quantita":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "Velocita":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "Temperatura":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "Energia":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "Pressione":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
        elif self.l_unita.cget("text") == "":
            self.b_0.config(bg=self.co2, fg=self.co0)
            self.b_1.config(bg=self.co2, fg=self.co0)
            self.b_2.config(bg=self.co2, fg=self.co0)
            self.b_3.config(bg=self.co2, fg=self.co0)
            self.b_4.config(bg=self.co2, fg=self.co0)
            self.b_5.config(bg=self.co2, fg=self.co0)
            self.b_6.config(bg=self.co2, fg=self.co0)
            self.b_7.config(bg=self.co2, fg=self.co0)
            self.b_8.config(bg=self.co2, fg=self.co0)
             
    def attiva_calcola(self, event=None):
        self.b_calcola.config(state='normal')
        self.b_reset.config(state='normal')
        
    def peso(self, event=None):
        self.l_unita.config(text="Peso")
        self.b_0.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg'])
        self.c_a.config(values=['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def tempo(self, event=None):
        self.l_unita['text'] = "Tempo"
        self.b_1.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['s', 'min', 'h', 'gg', 'm', 'a'])
        self.c_a.config(values=['s', 'min', 'h', 'gg', 'm', 'a'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def lunghezza(self, event=None):
        self.l_unita['text'] = "Lunghezza"
        self.b_2.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'])
        self.c_a.config(values=['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def area(self, event=None):
        self.l_unita['text'] = "Area"
        self.b_3.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['km²', 'hm²', 'dam²', 'm²', 'dm²', 'cm²', 'mm²'])
        self.c_a.config(values=['km²', 'hm²', 'dam²', 'm²', 'dm²', 'cm²', 'mm²'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def quantita(self, event=None):
        self.l_unita['text'] = "Quantita"
        self.b_4.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['km³', 'hm³', 'dam³', 'm³', 'dm³', 'cm³', 'mm³'])
        self.c_a.config(values=['km³', 'hm³', 'dam³', 'm³', 'dm³', 'cm³', 'mm³'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def velocita(self, event=None):
        self.l_unita['text'] = "Velocita"
        self.b_5.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['km/h', 'm/s', 'm/min', 'cm/s', 'mm/s'])
        self.c_a.config(values=['km/h', 'm/s', 'm/min', 'cm/s', 'mm/s'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def temperatura(self, event=None):
        self.l_unita['text'] = "Temperatura"
        self.b_6.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['°C', '°F', 'K'])
        self.c_a.config(values=['°C', '°F', 'K'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def energia(self, event=None):
        self.l_unita['text'] = "Energia"
        self.b_7.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['J', 'kJ', 'cal', 'kcal', 'Wh', 'kWh'])
        self.c_a.config(values=['J', 'kJ', 'cal', 'kcal', 'Wh', 'kWh'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def pressione(self, event=None):
        self.l_unita['text'] = "Pressione"
        self.b_8.config(bg=self.co3, fg=self.co1)
        self.c_da.config(values=['Pa', 'hPa', 'atm', 'bar', 'psi'])
        self.c_a.config(values=['Pa', 'hPa', 'atm', 'bar', 'psi'])
        # setto il valore di default
        self.c_da.current(0)
        self.c_a.current(1)
        self.control_button()
        
    def calcola(self, event):
        try:
            da = self.c_da.get()
            a = self.c_a.get()
            valore = float(self.e_valore.get())
            #get label text
            l_unita = self.l_unita.cget("text")
            if da == a:
                risultato = valore
            else:
                #posizione di da e a nel dizionario
                pos_da = [i for i, d in enumerate(self.unita[l_unita]) if da in d][0]
                pos_a = [i for i, d in enumerate(self.unita[l_unita]) if a in d][0]
                if l_unita == 'Temperatura':
                    if da == '°C':
                        if a == '°F':
                            risultato = (valore * 1.8) + 32
                        elif a == 'K':
                            risultato = valore + 273.15
                    elif da == '°F':
                        if a == '°C':
                            risultato = (valore - 32) / 1.8
                        elif a == 'K':
                            risultato = (valore + 459.67) / 1.8
                    elif da == 'K':
                        if a == '°C':
                            risultato = valore - 273.15
                        elif a == '°F':
                            risultato = (valore * 1.8) - 459.67                      
                else:
                    risultato = valore * list(self.unita[l_unita][pos_da].values())[0] / list(self.unita[l_unita][pos_a].values())[0]
                    risultato = round(risultato, 6) # arrotondo a 6 decimali
                    

            #aggiorno il risultato
            self.e_risultato.config(state='normal')
            self.e_risultato.delete(0, END)
            self.e_risultato.insert(0, risultato)
            self.e_risultato.config(state='readonly')

        except:
            pass
        
    def reset(self, event):
        self.c_da.current(0)
        self.c_a.current(0)
        self.e_valore.delete(0, END)
        self.e_risultato.delete(0, END)
        self.l_unita.config(text="")
        self.b_calcola.config(state='disabled')
        self.b_reset.config(state='disabled')
        self.control_button()
        
        
if __name__ == "__main__":
    app = CalcolatriceDiUnita()
    mainloop()