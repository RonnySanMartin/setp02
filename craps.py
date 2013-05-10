from random import *		#Libreria con randint funcion que retorna un entero aleatorio

"""
	Funcion craps
"""
def craps(reglas):
	jugando = True										#booleano que permite repetir lanzamientos
	lanzamiento_1 = (randint(1,6), randint(1,6))		#Primer lanzamiento
	print("Primer lanzamiento: " + str(lanzamiento_1))

	if lanzamiento_1 in reglas['ganas']:				#Victoria
		print("Felicitaciones, has ganado.")
	elif lanzamiento_1 in reglas['pierdes']:			#Perdida
		print("Lo siento, has perdido.")
	elif lanzamiento_1 in reglas['punto']:				#Punto
		puntaje_1 = lanzamiento_1[0] + lanzamiento_1[1]
		while jugando:											#Lanzamientos hasta que jugando sea False
			lanzamiento_2 = (randint(1,6),randint(1,6))
			puntaje_2 = lanzamiento_2[0] + lanzamiento_2[1]
			print("El juego continua...")
			print("Siguiente lanzamiento: " + str(lanzamiento_2))
			if puntaje_2 == 7:										#Perdida
				print("Lo siento, has perdido.")
				jugando = False
			elif puntaje_2 == puntaje_1:							#Victoria
				print("Felicitaciones, has ganado.")
				jugando = False


"""
	Ejecucion del programa
"""
dado = []
for i in range(13):			#Creacion de lista
	dado.append(set())

for j in range(6):			#Creacion de conjuntos
	for k in range(6):
		dado[j+k+2].add((j+1,k+1))

pierdes = dado[2]|dado[3]|dado[12]
ganas = dado[7]|dado[11]
punto = dado[4]|dado[5]|dado[6]|dado[8]|dado[9]|dado[10]

reglas = {"pierdes":pierdes, "ganas":ganas, "punto": punto}	#Reglas del juego, diccionario de conjuntos

craps(reglas)												#Llamada a la funcion para que se ejecute
