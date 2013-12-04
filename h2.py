#! /usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------
import pilas
from pilas.comportamientos import Comportamiento

def CrearMapa():
	mapa= pilas.actores.Mapa(filas=15, columnas=20)
	mapa.pintar_bloque(14, 0, 0)
	mapa.pintar_bloque(14, 1, 1)
	mapa.pintar_bloque(14, 2, 1)
	mapa.pintar_bloque(14, 3, 1)
	mapa.pintar_bloque(14, 4, 1)
	mapa.pintar_bloque(14, 5, 1)
	mapa.pintar_bloque(14, 6, 1)
	mapa.pintar_bloque(14, 7, 1)
	mapa.pintar_bloque(14, 8, 1)
	mapa.pintar_bloque(14, 9, 1)
	mapa.pintar_bloque(14, 10, 1)
	mapa.pintar_bloque(14, 11, 1)
	mapa.pintar_bloque(14, 12, 1)
	mapa.pintar_bloque(14, 13, 1)
	mapa.pintar_bloque(14, 14, 1)
	mapa.pintar_bloque(14, 15, 1)
	mapa.pintar_bloque(14, 16, 1)
	mapa.pintar_bloque(14, 17, 1)
	mapa.pintar_bloque(14, 18, 1)
	mapa.pintar_bloque(14, 19, 2)

#	mapa.pintar_bloque(8, 6, 0, True)
#	mapa.pintar_bloque(8, 7, 1, True)
#	mapa.pintar_bloque(8, 8, 1, True)
#	mapa.pintar_bloque(8, 9, 1, True)
#	mapa.pintar_bloque(8, 10, 1, True)
#	mapa.pintar_bloque(8, 11, 2, True)

#Otra forma
#	for columnas in range(0,20):
#		mapa.pintar_bloque(14,columnas,1)

	pilas.fondos.Espacio()
	return mapa



pilas.iniciar()

teclas={pilas.simbolos.a: 'izquierda', pilas.simbolos.d: 'derecha', pilas.simbolos.w: 'arriba'
}
mandos=pilas.control.Control(pilas.escena_actual(),teclas)

vel=1

class Pollo(pilas.actores.Actor):
	def __init__(self):
		pilas.actores.Actor.__init__(self)
		self.imagen = pilas.imagenes.cargar_grilla("GalloAdelante.png", 4)
		self.aprender(pilas.habilidades.MoverseConElTeclado,control=mandos)
		self.hacer(Esperando())
		self.aprender(pilas.habilidades.SeMantieneEnPantalla)
	def definir_cuadro(self, indice):
		self.imagen.definir_cuadro(indice)
		
class Esperando(Comportamiento):

	def iniciar(self, receptor):
		self.receptor = receptor
		self.receptor.definir_cuadro(1)

	def actualizar(self):
		if mandos.izquierda:
			self.receptor.hacer(Caminando())
		elif mandos.derecha:
			self.receptor.hacer(Caminando())
		if mandos.arriba:
			self.receptor.hacer(Saltando())

			
	def definir_cuadro(self, indice):
		self.imagen.definir_cuadro(indice)


	


	if mandos.arriba:
			if not self.receptor.espejado:
				self.receptor.espejado=True
			self.receptor.x-=vel


class Saltando(Comportamiento):
	def __init__(self):
		self.dy = 10
		
	def iniciar(self, receptor):
		self.receptor = receptor
		self.receptor.definir_cuadro(0)
		self.origen = self.receptor.y
		
	def actualizar(self):
		self.receptor.y += self.dy
		self.dy -= 0.3

		if self.receptor.y < self.origen:
		    self.receptor.y = self.origen
		    self.receptor.hacer(Esperando())

		if pilas.mundo.control.izquierda:
		    self.receptor.x -= VELOCIDAD
		elif pilas.mundo.control.derecha:
		    self.receptor.x += VELOCIDAD

class Caminando(Comportamiento):
	def iniciar(self,receptor):
		self.receptor=receptor
		self.cuadros=[0,1,1,1,2,2,2,3,3,3]
		self.paso=0

	def actualizar(self):
		self.avanzar_animacion()


		if mandos.izquierda:
			if not self.receptor.espejado:
				self.receptor.espejado=True
			self.receptor.x-=vel
		elif mandos.derecha:
			if self.receptor.espejado:
				self.receptor.espejado=False
			self.receptor.x+=vel

		else:
			self.receptor.hacer(Esperando())


	def avanzar_animacion(self):
		self.paso=self.paso+1
		if self.paso>=len(self.cuadros):
			self.paso=0

		self.receptor.definir_cuadro(self.cuadros[self.paso])	# define que el cuadro es el paso :F
		
	def definir_cuadro(self, indice):
		self.imagen.definir_cuadro(indice)

pollo=Pollo()
mapa=CrearMapa()
pilas.ejecutar()



