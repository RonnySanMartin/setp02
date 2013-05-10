def j_valida(jugada):				#funcion que verifica si la jugada es valida
	juegos = ['r', 'p', 't']		#lista de jugadas validas
	for i in juegos:				#revision iterativa de si la jugada ingresa es valida
		if i == jugada.lower():
			return True				#true = valida
	return False					#false= invalida

def ganador_cachipun(jugada):
	victoria = {'p':'r', 'r':'t', 't':'p'}							#Diccionario con reglas de victoria
	if len(jugada) != 2:											#Verificacion cantidad de jugadores
		raise Exception("Número incorrecto de jugadores")										
	elif not j_valida(jugada[0][1]) or not j_valida(jugada[1][1]):	#Verificacion jugada valida
		raise Exception("Jugada no válida")
	elif jugada[0][1] == jugada[1][1]:								#Define al ganador	
		return str(jugada[0])
	elif victoria[jugada[0][1].lower()] == jugada[1][1].lower():
		return str(jugada[0])
	else:
		return str(jugada[1])
