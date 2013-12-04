#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
import pilas
from pilas.comportamientos import Comportamiento
import random

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

	return mapa



pilas.iniciar()


teclas={pilas.simbolos.a: 'izquierda', pilas.simbolos.d: 'derecha', pilas.simbolos.w: 'arriba'}
mandos=pilas.control.Control(pilas.escena_actual(),teclas)

vel=3

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
		if pilas.mundo.control.izquierda:
			self.receptor.hacer(Caminando())
		elif pilas.mundo.control.derecha:
			self.receptor.hacer(Caminando())
		if pilas.mundo.control.arriba:
			self.receptor.hacer(Saltando())

			
	def definir_cuadro(self, indice):
		self.imagen.definir_cuadro(indice)



	if pilas.mundo.control.arriba:
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
		    self.receptor.x -= 3
		elif pilas.mundo.control.derecha:
		    self.receptor.x += 3

class Caminando(Comportamiento):
	def iniciar(self,receptor):
		self.receptor=receptor
		self.cuadros=[0,1,1,1,2,2,2,3,3,3]
		self.paso=0

	def actualizar(self):
		self.avanzar_animacion()

		if pilas.mundo.control.izquierda:
			if not self.receptor.espejado:
				self.receptor.espejado=True
			self.receptor.x-=vel
		elif pilas.mundo.control.derecha:
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

class EscenaMenu(pilas.escena.Base):

	def __init__(self):
		pilas.escena.Base.__init__(self)

	def iniciar(self):

		pilas.fondos.Espacio()

		menu = [('Jugar', self.jugar),('Controles',self.controles),('Salir', self.salir)]

		self.menu = pilas.actores.Menu(menu,y =-100)

	def controles(self):
		pass
		#        pilas.cambiar_escena(EscenaAyuda())

	def jugar(self):
		pilas.cambiar_escena(Juego())

	def salir(self):
		import sys
		sys.exit(0)

class Juego(pilas.escena.Base):

	def __init__(self):
		pilas.escena.Base.__init__(self)

	def iniciar(self):
		bomba=BombaConMovimiento(y=0, x=0)
		self.musica=pilas.musica.cargar("MusicaJuego.mp3")
		pilas.fondos.Fondo("Maestruli.jpg")
		self.musica.reproducir(repetir = True)
		pollo=Pollo()
		pollo.y=-130
		pollo.x=0
		pilas.avisar("Bienvenido al PolloStruli")
		mapa=CrearMapa()
		pilas.eventos.actualizar.conectar(self.actualizador)
		self.contador=0

	def actualizador(self,actor):
		if self.contador==25:
			pilas.avisar("asdgas")
			bomba=BombaConMovimiento(y=250, x=random.randint(-300,300))
			self.contador=0
		self.contador+=1

class BombaConMovimiento(pilas.actores.Bomba):

	def __init__(self, x=0, y=0):

		pilas.actores.Bomba.__init__(self, x, y)

	def actualizar(self):

		self.y -= 3


pilas.cambiar_escena(EscenaMenu())
pilas.ejecutar()
