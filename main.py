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
video = Video("http://video.mp4", "http://click.com", 10, "instream")
campana = Campana("Campaña Inicial", datetime.today(), datetime.today())
campana._Campana__anuncios = [video]  # Forzar que tenga solo 1 anuncio (opcional si ya tiene uno)

try:
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    campana.nombre = nuevo_nombre

    nuevo_subtipo = input("Ingrese el nuevo subtipo del anuncio de video: ")
    campana.anuncios[0].sub_tipo = nuevo_subtipo

    print("Datos modificados exitosamente.")
    print(campana)

except (largoExcedidoError, SubTipoInvalidoError) as e:
    with open("error.log", "a", encoding="utf-8") as f:
        f.write(f"[ERROR] {type(e).__name__}: {str(e)}\n")
    print("Ocurrió un error. Revisa el archivo error.log.")
 