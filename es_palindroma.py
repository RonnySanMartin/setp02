def es_palindroma(texto):
	lista_original = list(texto)
	lista_reversa = list(texto)
	lista_reversa.reverse()				#Creacion de lista invertida

	if lista_reversa == lista_original:	#Vemos si la lista invertida es igual a la original
		return True
	return False
