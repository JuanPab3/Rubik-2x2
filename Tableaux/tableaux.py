#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
global listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	p = letrasProposicionales[0] # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE
	return Tree(p, None, None) # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
    for i in l:
        if i[0] == "-" :
            for j in l:
                if len(j)== 1 and i[1]== j:
                    return True
    return False




def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
    if f.right == None:
        return True
    elif f.label == "-" and f.right.label not in [">","-","Y","O"]:
        return es_literal(f.right)
    elif f.left != None:
        return False
    else: return False




def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	return False

def clasifica_y_extiende(hoja:list; f:Tree):
	tipo = ""
	listaHojas = []
	#===TIPO_ALFA===#
		if (f.label == '-') and (f.right.label == '-'):
		tipo = "ALFA1"
	elif (f.label == 'Y'):
		tipo = "ALFA2"
	elif (f.label == '-') and (f.right.label == 'O'):
		tipo = "ALFA3"
	elif (f.label == '-') and (f.right.label == '>'):
		tipo = "ALFA4"
	#===TIPO_OMEGA===#
	elif (f.label == '-') and (f.right.label == 'Y'):
		tipo = "OMEGA1"
	elif (f.label == 'O'):
		tipo = "OMEGA2"
	elif (f.label == '>'):
		tipo = "OMEGA3"
	#===CONVERSIÓN===#
	if   (tipo == "ALFA1"):
		aux1 = [f.right]
		listaHojas.remove(hoja)
		listaHojas.append(aux1)
	elif (tipo == "ALFA2"):
		aux1 = [f.right]
		aux2 = [f.left]
		listaHojas.remove(hoja)
		listaHojas.append(aux1)
		listaHojas.append(aux2)
	elif (tipo == "ALFA3"):
		aux1 = [Tree('-',None,f.right)]
		aux2 = [Tree('-',None,f.left)]
		listaHojas.remove(hoja)
		listaHojas.append(aux1)
		listaHojas.append(aux2)
	elif (tipo == "ALFA4"):
		aux1 = [f.right]
		aux2 = [Tree('-',None,f.left)]
		listaHojas.remove(hoja)
		listaHojas.append(aux1)
		listaHojas.append(aux2)
	elif (tipo == "OMEGA1"):
		aux1 = [Tree('-',None,f.right)]
		aux2 = [Tree('-',None,f.left)]
		listaHojas.remove(hoja)
		listaHojas.append(aux1)
		listaHojas.append(aux2)
		aux1 = [f.right]
		aux2 = [f.left]
		listaHojas.remove(hoja)
		listaHojas.append(aux1)
		listaHojas.append(aux2)
	elif (tipo == "OMEGA3"):
		aux1 = [Tree('-',None,f.right)]
		aux2 = [f.left]
		listaHojas.remove(hoja)
		listaHojas.append(aux1)
		listaHojas.append(aux2)

def Tableaux(f):
	# Algoritmo de creacion de tableau a partir de lista_hojas

	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas # acá se incluiran las hojas con 0

	A = string2Tree(f)
	listaHojas = [[A]]

	while (len(listaHojas)>0):
		hoja = listaHojas[0]
		f = no_literales(hoja)
		# f == none si hojas solo contiene literales
		if f == none:
			if par_complementario(hoja):
				listaHojas.remove(hoja)
			else:
				listaInterpsVerdaderas.append(hoja)
				listaHojas.remove(hoja)
		else:
			clasifica_y_extiende(f)

	return listaInterpsVerdaderas
