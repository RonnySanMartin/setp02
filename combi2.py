from itertools import * #Libreria con funcion combinations, funcion que retorna combinaciones

def combinatoria2(conjunto, k):
    return list(combinations(conjunto, k))  #Forza al objeto que retorna combinations a ser una lista, para retornar
