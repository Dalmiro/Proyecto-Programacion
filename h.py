import pilas
import Mapa 


class Pollo(pilas.actores.Actor):
	def __init__(self):
		pilas.actores.Actor.__init__(self)
		self.imagen = pilas.imagenes.cargar_grilla("GalloAdelante.png", 5)
		self.aprender(pilas.habilidades.MoverseConElTeclado)
		self.hacer(Esperando(self))
	
	def actualizar(self):
	    if pilas.mundo.control.izquierda:
	        self.x -= 5
	        self.espejado = True
	    elif pilas.mundo.control.derecha:
	        self.x += 5
	        self.espejado = False



class Esperando(pilas.Comportamiento):
    "Un actor en posicion normal o esperando a que el usuario pulse alguna tecla."

    def iniciar(self, receptor):
        self.receptor = receptor
        self.receptor.definir_cuadro(4)

    def actualizar(self):
        if pilas.mundo.control.izquierda:
            self.receptor.hacer(Caminando())
        elif pilas.mundo.control.derecha:
            self.receptor.hacer(Caminando())

        if pilas.mundo.control.arriba:
            self.receptor.hacer(Saltando())
 

pilas.iniciar()



pilas.fondos.Espacio()
#Crear Pollo-Grilla
#grilla = pilas.imagenes.cargar_grilla("GalloAdelante.png", 5)
#Pollo = pilas.actores.Animacion(grilla, ciclica=True)
#Pollo.x=0
#Pollo.y=-127
#Crear Pollo Comun
class Pollo(pilas.actores.Actor):
	def __init__(self):
		pilas.actores.Actor.__init__(self)
		self.imagen = pilas.imagenes.cargar_grilla("GalloAdelante.png", 5)
		self.aprender(pilas.habilidades.MoverseConElTeclado)
		self.hacer(Esperando(self))
	
	def actualizar(self):
	    if pilas.mundo.control.izquierda:
	        self.x -= 5
	        self.espejado = True
	    elif pilas.mundo.control.derecha:
	        self.x += 5
	        self.espejado = False

Pollo=Pollo()
Pollo.y=-130

#Habilidades
Pelota.aprender(pilas.habilidades.Arrastrable)
Pelota.aprender(pilas.habilidades.SeMantieneEnPantalla)
Pollo.aprender(pilas.habilidades.MoverseConElTeclado)
Pollo.aprender(pilas.habilidades.SeMantieneEnPantalla)


mapa=Crear_Mapa()
pilas.ejecutar()
