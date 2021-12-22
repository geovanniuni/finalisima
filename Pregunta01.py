class Titulo:
    nombre= None
    autor= None
    isbn = None
    numeroReserva= None
    ejemplares=list()

    def __init__(self,nombrex,autorx,isbnx,numeroReservax):
        self.nombre=nombrex
        self.autor=autorx
        self.isbn= isbnx
        self.numeroReserva= numeroReservax

    
    def encontrar(self):
        print("Titulo Encontrado")
    
    def crear(self):
        print("Titulo creado")
    
    def destruir(self):
        print("Titulo destruido")
    
    def setEjemplar(self,ejemplarx):
        self.ejemplares.append(ejemplarx)
    
    def listarEjemplares(self):
        for i in self.ejemplares:
            i.caracteristicas()

class Libro(Titulo):
    tiempo= None
    
    def __init__(self, nombrex, autorx, isbnx, numeroReservax,tiempox=30):
        super().__init__(nombrex, autorx, isbnx, numeroReservax)
        self.tiempo=tiempox
    
class Revista(Titulo):
    tiempo= None
    
    def __init__(self, nombrex, autorx, isbnx, numeroReservax,tiempox=10):
        super().__init__(nombrex, autorx, isbnx, numeroReservax)
        self.tiempo=tiempox

class Ejemplar():
    id= None
    titulo=None
    prestamo=False
    reserva=False

    def __init__(self,idx,titulox):
        self.id=idx
        self.titulo=titulox
    
    def encontrar_titulo(self):
        self.titulo.encontrar()
    
    def crear(self):
        ejemplar_nuevo= Ejemplar(self.id,self.titulo)
        self.titulo.setEjemplar(ejemplar_nuevo)
    
    def destruir(self,idx):
        print("Ejemplar "+idx+ " destruido")
    
    def encontrar(self,idx):
        print("Ejemplar "+idx+ " encontrar")
    
    def prestar(self):
        self.prestamo=True
    def devolver(self):
        self.prestamo=False

    def reservar(self):
        self.reserva=True
    def quitarReserva(self):
        self.reserva=False

    def caracteristicas(self):
        print(self.id,end=" ")
        print(self.titulo.nombre,end=" ")
        print("Prestamo:",end=" ")
        print(self.prestamo,end=" ")
        print("Reserva:",end=" ")
        print(self.reserva)
    
class Prestamo:
    fecha=None
    ejemplar=None

    def __init__(self,ejemplarx):
        self.ejemplar=ejemplarx
    
    def crear(self):
        for i in self.ejemplar.titulo.ejemplares:
            if self.ejemplar.id== i.id:
                i.prestar()
    
    def destruir(self):
        for i in self.ejemplar.titulo.ejemplares:
            if self.ejemplar.id== i.id:
                i.devolver()

class Reserva:
    fecha=None
    ejemplar=None

    def __init__(self,ejemplarx):
        self.ejemplar=ejemplarx
    
    def crear(self):
         for i in self.ejemplar.titulo.ejemplares:
            if self.ejemplar.id== i.id:
                i.reservar()
    
    
    def destruir(self):
        for i in self.ejemplar.titulo.ejemplares:
            if self.ejemplar.id== i.id:
                i.quitarReserva()
      




rev1=Revista("Nature","Hardman",123456,535643)
ejem1Rev1=Ejemplar("00001",rev1)
ejem2Rev1=Ejemplar("00002",rev1)
ejem1Rev1.crear()
ejem2Rev1.crear()        
#rev1.listarEjemplares()

lib1=Libro("Grossman","Springer",54654434,23345436)
ejem1Lib1=Ejemplar("00003",lib1)
ejem2Lib1=Ejemplar("00004",lib1)
ejem1Lib1.crear()
ejem2Lib1.crear()        
#lib1.listarEjemplares()

prestamo1=Prestamo(ejem1Rev1)
prestamo2=Prestamo(ejem2Lib1)


reserva1=Reserva(ejem2Rev1)
reserva2=Reserva(ejem1Lib1)

prestamo1.crear()
prestamo2.crear()

reserva1.crear()
reserva2.crear()

lib1.listarEjemplares()
rev1.listarEjemplares()

    