"""
	Funciones secundarias
"""

def ingreso(diccionario, palabra):
	try:
		diccionario[palabra] = diccionario[palabra] + 1	#Si la clave existe, se aumenta la frecuencia
	except:
		diccionario[palabra] = 1						#Sino, se crea un nuevo espacio con frecuencia 1

def depuracion_texto(texto):	
	
	texto = texto.lower()									
	a_eliminar = ['.', ',', ';', ':', '\"', '\'', '(', ')']	#arreglo con elementos a eliminar
	
	for i in a_eliminar:
		texto = texto.replace(i, '')	#Eliminacion de caracteres usando el arreglo
	texto = texto.replace('\n', ' ')
	texto = texto.replace('\t', ' ')
	
	return texto

"""
	Ejecucion del programa
"""

archivo = open("funes.txt", "r", encoding='utf-8')	#Apertura
texto = archivo.read()								#Lectura
archivo.close()										#Cierre
texto = depuracion_texto(texto)						#Limpieza (tener un texto sin mayusculas ni signos)
lista = texto.split()								#Cada palabra se lleva a una lista
dict_frecuencias = {}								#Diccionario con las frecuencias, se inicia vacio

for pal_lista in lista:
	ingreso(dict_frecuencias, pal_lista)			#Ingreso de palabras

frecuencia = max(dict_frecuencias.values())			#Buscamos mayor frecuencia

while frecuencia > 0:								#Impresion de datos desde la mayor frecuencia
	for i in dict_frecuencias:
		if dict_frecuencias[i] == frecuencia:
			print (i + ": " + str(frecuencia))
	frecuencia = frecuencia - 1