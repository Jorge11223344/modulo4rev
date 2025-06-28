from clases import *
from datetime import datetime
f= datetime.now()
fecha_actual = datetime.now()
#campana= Campana("campana1",fecha_actual ,f)




"""
c=Campana("tdtr","fuf","hgffyd")
c.agregar_anuncio()
print(c.anuncios)


a=Social(2,3,"tftr2","uyftf","frdd")

v = Video(12,"instream")

d= Display(1,2,"fr","hfyrd","hgfytf")
print(a,v,d)

a.sub_tipo = "facebook"

"""
if __name__ == "__main__":
    print("=== Creación de campaña ===")
    nombre = input("Nombre de la campaña: ")
    fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")
    fecha_termino = input("Fecha de término (AAAA-MM-DD): ")

    campana = Campana(nombre, fecha_inicio, fecha_termino)

    print("\n=== Agregar anuncios a la campaña ===")
    campana.agregar_anuncio()

    print("\n=== Resumen de campaña ===")
    print(campana)

    print("\n=== Tipos de formato disponibles ===")
    print(Campana.mostrar_formatos())  # método estático para ejemplo