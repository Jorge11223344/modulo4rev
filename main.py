from clases import *
from datetime import datetime
"""
nombre = input("nombre de campaña : ")

fecha_inicio_str = input("Fecha de inicio (YYYY-MM-DD): ")
fecha_termino_str = input("Fecha de término (YYYY-MM-DD): ")

fecha_inicio = date.fromisoformat(fecha_inicio_str)
fecha_termino = date.fromisoformat(fecha_termino_str)

campana = Campana(nombre, fecha_inicio, fecha_termino)
"""
"""

c=Campana("tdtr","fuf","hgffyd")
c.agregar_anuncio()
print(c.anuncios)
"""
"""
a=Social(2,3,"tftr2","uyftf","frdd")

v = Video("ftf","ftf",25,"ftf")

d= Display(1,2,"fr","hfyrd","hgfytf")
print(a,v,d)


print(a.sub_tipo)
print(d.sub_tipo)
print(v.sub_tipo)
"""


#Se crea una instancia del anuncio con datos predefinidos
video = Video("http://video.mp4", "http://click.com", 10, "instream")

# Se crea un acapaña con nombre y fecha, en fecha se usa la misma fecha es solo para probar
campana = Campana("Campaña Inicial", datetime.today(), datetime.today())

## se accede directamente por enmascaramineto de nombre (name mangling), tomando la forma _nombreclase_anuncios
campana._Campana__anuncios = [video]  

try:
    #solicita al usuario un nuevo nombre
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    campana.nombre = nuevo_nombre


    # Solicita al usuario un nuevo subtipo
    nuevo_subtipo = input("Ingrese el nuevo subtipo del anuncio de video: ")
    campana.anuncios[0].sub_tipo = nuevo_subtipo

    #Muestra los nuevos datos de la campaña
    print("Datos modificados exitosamente.")
    print(campana)


    """
    Muetsra los errores si el nombre o subtipo es errado
    """

except (largoExcedidoError, SubTipoInvalidoError) as e:

    """
    Crea el archivo error.log en modo adjuntar
    """
    with open("error.log", "a", encoding="utf-8") as f:
        hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #escribe el error con fecha,hora,tipo de error y mensaje

        f.write(f"[{hora_actual}] {type(e).__name__}: {str(e)}\n")
    print("Ocurrió un error. Revisa el archivo error.log.")
 