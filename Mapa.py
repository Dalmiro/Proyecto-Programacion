import pilas

def Crear_Mapa():
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

	return mapa

pilas.ejecutar()
