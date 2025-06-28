from abc import ABC, abstractmethod
from error import largoExcedidoError, SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self,ancho,alto,url_archivo,url_click,sub_tipo):
        self.__ancho = ancho if ancho > 0 else 1  ## esto es una forma de filtrar en la misma linea, se evita el validador que debería realizarse en otro archivo
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self,ancho):
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self,alto):
        self.__alto = alto

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self,url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_click(self):
        return self.__url_click
    
    @url_click.setter
    def url_click(self,url_click):
        self.__url_click = url_click

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self,sub_tipo):
       # si la instancia actual que es self(==) es igual a una instacia de video y self.subtipo == video
       #  o de social
       #  o de display.
        if (isinstance(self,Video) and sub_tipo in Video.SUB_TIPOS or isinstance(self,Social) and sub_tipo in Social.SUB_TIPOS or isinstance(self,Display) and sub_tipo in Display.SUB_TIPOS):
            self.__sub_tipo=sub_tipo
        else:
            raise SubTipoInvalidoError("Error de tipo invalido.")
    
           
####################################################################################


    @staticmethod
    def mostrar_formatos():
        clases_anuncio = [Video,Display,Social]
        for i, clase in enumerate(clases_anuncio,start=1):## parte de 1 el indice
            print(f"FORMATO {i}:{clase.FORMATO}")
            for subtipo in clase.SUB_TIPOS:
                print(f"- {subtipo}")

    
    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass





    


class Campana:
    def __init__(self,nombre,fecha_inicio,fecha_termino):
       
        self.__nombre =nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.componer_anuncio()]

    def componer_anuncio(self):

        opcion = int(input("que tipo de anuncio quiere 1-para video 2_para display, 3-para social"))
        if opcion ==1:
            duracion = int(input("cual es la duracion del video minimo 5 minutos"))
            new_anuncio = Video(duracion)
        elif opcion ==2:
            new_anuncio = Display()
        elif opcion ==3:
            new_anuncio = Social()

        return new_anuncio

    def agregar_anuncio(self):        
        while True:
            try:
                opcion = int(input("que tipo de anuncio quieres 1 para video 2 para diplay y 3 para social"))
                if opcion ==1:
                    duracion =int(input("cual esla duracion del video minimo es 5 minutos"))
                    new_anuncio = Video(duracion)
                elif opcion == 2:
                    new_anuncio = Display()
                elif opcion == 3:
                    new_anuncio = Social()
                else:
                    break
                self.__anuncios.append(new_anuncio)

            except Exception as e:
                pass

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
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
        return f"nombre de campana  :{self.nombre} - {self.__anuncios}"






class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")  ## Parentesis redondo para especificar una tupla

    def __init__(self,duracion, subtipo):
        self.ancho =1
        self.alto = 1
        self.__duracion = duracion if duracion > 0 else 5
        self.sub_tipo = subtipo

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self,duracion):
        self.__duracion = duracion

    
    def comprimir_anuncio():
        print("Compresion de video no implementado aun")

    
    def redimensionar_anuncio():
        print("Recorte de video no implementado")

    def __repr__(self):
        return f"{Video.FORMATO} -{self.duracion}"

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")  ## Parentesis redondo para especificar una tupla
    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)


    def comprimir_anuncio():
        print("Compresión de anuncios Display  no implementada aun")

    
    def redimensionar_anuncio():
        print("Redimensionamineto de anuncios Display no implementado aún")

    def __repr__(self):
        return f"{Display.FORMATO}"

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")  ## Parentesis redondo para especificar una tupla

    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio():
        print("compresion de anuncio de redes sociales no imlementada aún")

    
    def redimensionar_anuncio():
        print("Redimensionamineto de anuncios de redes sociales no implementada aún")

    def __repr__(self):
        return f"{Social.FORMATO}"





