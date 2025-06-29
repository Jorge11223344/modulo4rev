from abc import ABC, abstractmethod
from error import largoExcedidoError, SubTipoInvalidoError

class Anuncio(ABC):
    """
    Clase abstracta actua como clase padre de las clases social,video y Display
    """


    def __init__(self,ancho: int,alto:int,url_archivo:str,url_click:str,sub_tipo:str):
        self.__ancho = ancho if ancho > 0 else 1  ## esto es una forma de filtrar en la misma linea, se evita el validador que debería realizarse en otro archivo
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

# Se encapculan los atributos con getter y setters, como lo solicita el desafio

    @property
    def ancho(self)->int:
        return self.__ancho
    
    @ancho.setter
    def ancho(self,ancho:int):
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self,alto:int):
        self.__alto = alto

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self,url_archivo:str):
        self.__url_archivo = url_archivo

    @property
    def url_click(self):
        return self.__url_click
    
    @url_click.setter
    def url_click(self,url_click:str):
        self.__url_click = url_click

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self,sub_tipo:str):


       # si la instancia actual que es self(==) es igual a una instacia de video y self.subtipo == video
       #  o de social
       #  o de display.
        if (isinstance(self,Video) and sub_tipo in Video.SUB_TIPOS or isinstance(self,Social) and sub_tipo in Social.SUB_TIPOS or isinstance(self,Display) and sub_tipo in Display.SUB_TIPOS):
            self.__sub_tipo=sub_tipo
        else:
            raise SubTipoInvalidoError("Error de tipo invalido.")
    
           
    @staticmethod
    def mostrar_formatos():

        """
        Muestra los subtipos que existen en cada formato
        """

        clases_anuncio = [Video,Display,Social]
        for i, clase in enumerate(clases_anuncio,start=1):## parte de 1 el indice
            print(f"FORMATO {i}:{clase.FORMATO}")
            for subtipo in clase.SUB_TIPOS:
                print(f"- {subtipo}")

    
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass





    


class Campana:

    """
    Representa una campaña publicitaria con un conjunto de anuncios
    """



    def __init__(self,nombre:str,fecha_inicio,fecha_termino):
       
        self.__nombre =nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.componer_anuncio()]

    def componer_anuncio(self):

        """
        Crea un anuncio solicitando datos al usuario
        """

        opcion = int(input("que tipo de anuncio quiere 1-para video 2_para display, 3-para social"))
        if opcion == 1:
            url_archivo = input("URL del archivo del video: ")
            url_click = input("URL de clic del video: ")
            duracion = int(input("Duración del video: "))
            sub_tipo = input("Subtipo de video (instream / outstream): ")
            new_anuncio = Video(url_archivo, url_click, duracion, sub_tipo)

        elif opcion == 2:
            ancho = int(input("Ancho del display: "))
            alto = int(input("Alto del display: "))
            url_archivo = input("URL del archivo: ")
            url_click = input("URL del clic: ")
            sub_tipo = input("Subtipo del display (tradicional / native): ")
            new_anuncio = Display(ancho, alto, url_archivo, url_click, sub_tipo)

        elif opcion == 3:
            ancho = int(input("Ancho del anuncio social: "))
            alto = int(input("Alto del anuncio social: "))
            url_archivo = input("URL del archivo: ")
            url_click = input("URL del clic: ")
            sub_tipo = input("Subtipo social (facebook / linkedin): ")
            new_anuncio = Social(ancho, alto, url_archivo, url_click, sub_tipo)
        else:
            print("No se creo ningun anuncio")
            return None
        return new_anuncio

    def agregar_anuncio(self):  

        """
        Permite al usuario agregar multiples anuncios 
        """

        while True:
            try:
                continuar = input("¿Desea agregar un nuevo anuncio? (s/n): ").lower()
                if continuar != 's':
                    break

                nuevo_anuncio = self.componer_anuncio()
                if nuevo_anuncio:
                    self.__anuncios.append(nuevo_anuncio)
                else:
                    print("No se creó ningún anuncio.")
            except Exception as e:
                print(f"Error al agregar anuncio: {e}")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre:str):
        if len(nombre) <= 250:
            self.__nombre = nombre
        else:
            raise  largoExcedidoError("el largo del texto supera los 250 caracteres")

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio


    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

       
    @property
    def anuncios(self):
        return self.__anuncios
    
    def __repr__(self):

        """
        Muestra resumen con cantidad de anuncios según tipo
        """



        contador = {"Video": 0, "Display": 0, "Social": 0}

        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                contador["Video"] += 1
            elif isinstance(anuncio, Display):
                contador["Display"] += 1
            elif isinstance(anuncio, Social):
                contador["Social"] += 1

        return (
            f"Nombre de la campaña: {self.nombre}\n"
            #f"Desde : {self.fecha_inicio} hasta el {self.fecha_termino}\n "
            f"Anuncios: {contador['Video']} Video, "
            f"{contador['Display']} Display, "
            f"{contador['Social']} Social"
        )






class Video(Anuncio):

    """
    Anuncio tipo video
    
    """


    FORMATO:str = "Video"
    SUB_TIPOS:tuple = ("instream", "outstream")  ## Parentesis redondo para especificar una tupla

    def __init__(self,url_archivo:str, url_click:str, duracion:int, sub_tipo:str):
        super().__init__(1,1,url_archivo,url_click,sub_tipo)

        self.__duracion:int = duracion if duracion > 0 else 5
        

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self,duracion:int):
        self.__duracion = duracion if duracion >0 else 5

    
    def comprimir_anuncio(self):
        print("Compresion de video no implementado aun")

    
    def redimensionar_anuncio(self):
        print("Recorte de video no implementado")

    def __repr__(self):
        return f"{Video.FORMATO} -{self.duracion} mins "

class Display(Anuncio):

    """
    Anuncio tipo Display o imagen
    """


    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")  ## Parentesis redondo para especificar una tupla
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_click:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)


    def comprimir_anuncio(self):
        print("Compresión de anuncios Display  no implementada aun")

    
    def redimensionar_anuncio(self):
        print("Redimensionamineto de anuncios Display no implementado aún")

    def __repr__(self):
        return f"{Display.FORMATO}"

class Social(Anuncio):

    """
    Anuncio tipo redes sociales
    """


    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")  ## Parentesis redondo para especificar una tupla

    def __init__(self, ancho:int, alto:int, url_archivo:str, url_click:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):
        print("compresion de anuncio de redes sociales no imlementada aún")

    
    def redimensionar_anuncio(self):
        print("Redimensionamineto de anuncios de redes sociales no implementada aún")

    def __repr__(self):
        return f"{Social.FORMATO}"





