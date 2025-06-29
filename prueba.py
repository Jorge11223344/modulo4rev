from datetime import datetime
from clases import *

camp = Campana("Campaña Invierno", datetime.today(), datetime.today())
camp.agregar_anuncio()

print(camp)
Anuncio.mostrar_formatos()

