#================================ASPECTOS_TECNICOS==============================
from codificacion import deco_dict3 as decodic
from codificacion import decodifica3
from codificacion import codifica3
from random import randint as rint
from CubeGraph import RUBIC
from operator import *
#====================================CODIGO=====================================

Ncuadros = 24   #Número de Cuadros
Ncolores = 3    #Número de Colores
Nturnos  = 2    #Número de Turnos

max = 0
lC= []
for i in range(0,Ncuadros):
    for j in range(0,Ncolores):
        for k in range(0,Nturnos):
            cod_num = codifica3(i,j,k,Ncuadros,Ncolores,Nturnos)
            if (cod_num > max):
                max = cod_num
            n = chr(256+cod_num)
            lC.append(n)
            # cud,col,tur = decodifica3(ord(n)- 255,Ncuadros,Ncolores,Nturnos)
            #  print("(X{}-Y{}-Z{}) -> {}".format(i,j,k,n))
            # print("{} -> (X{}-Y{}-Z{})\n".format(n,cud,col,tur))
#====================================REGLAS=====================================

def lc():
    return lC

def Beta(i1:int, j1:int ,k1:int, i2:int ):
    """La siguiente notacion esta dada para realizar el cambio de color entre dos cuadros.

    Parameters
    ----------
    i1 : int
        posición turno n.
    j1 : int
        color actual.
    k1 : int
        turno n.
    i2 : int
        posición turno n.

    Returns
    -------
    type
        Description of returned object.

    """
    ant = chr(256+codifica3(i1, j1, k1,Ncuadros,Ncolores,Nturnos))
    cons = chr(256+codifica3(i2, j1, k1+1,Ncuadros,Ncolores,Nturnos))
#     print(f"(s{i1
#     reg = "({}Y{})".format(ant,cons)
    reg = "(-{}O{})".format(ant,cons)

    return reg



def basic_1():
    final = ""
    COLORES =  [0,0,1,1, # Front
                2,2,0,0, # Left
                1,1,0,0, # Right
                0,2,2,0, # Up
                0,0,2,2, # Down
                0,0,2,2] # Back
    L = []


    for i in range(0,len(COLORES)):
        # print(f's: {i}')
        # print(f'c: {COLORES[i]}')
        # print(f't: {0}')
        cod_num = codifica3(i,COLORES[i],0,Ncuadros,Ncolores,Nturnos)
        n = chr(256+cod_num)
        L.append(n)

    final += "({}Y{})".format(L[0],L[1])
    for i in range(2,len(L)):
        final = "(" + final
        final += "Y{})".format(L[i])

    return final


def regla2(k:int):
    """Movimiento tipo U (Up).

    Returns
    -------
    str

    """
    assert((k < Nturnos-1) and (k>=0)), f'Turno invalido, k debe ser mayor o igual a 0 y menor a {Nturnos-1}, se utilizó {str(k)}.'
    Un = "("
    # for k in range(0,Nturnos):
    for a in range(0,Ncolores):
        b1  = Beta(15,a,k,14)
        b2  = Beta(14,a,k,12)
        b3  = Beta(12,a,k,13)
        b4  = Beta(13,a,k,15)
        b5  = Beta(1,a,k,5)
        b6  = Beta(0,a,k,4)
        b7  = Beta(9,a,k,1)
        b8  = Beta(8,a,k,0)
        b9  = Beta(23,a,k,8)     # OG: 23->09
        b10 = Beta(22,a,k,9)    # OG: 23->09
        b11 = Beta(5,a,k,22)    # OG: 04->23
        b12 = Beta(4,a,k,23)    # OG: 05->23
        #======STAY THE SAME=====#
        b13 = Beta(6,a,k,6)
        b14 = Beta(7,a,k,7)
        b15 = Beta(2,a,k,2)
        b16 = Beta(3,a,k,3)
        b17 = Beta(10,a,k,10)
        b18 = Beta(11,a,k,11)
        b19 = Beta(16,a,k,16)
        b20 = Beta(17,a,k,17)
        b21 = Beta(18,a,k,18)
        b22 = Beta(19,a,k,19)
        b23 = Beta(20,a,k,20)
        b24 = Beta(21,a,k,21)
        Un += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
        Un += "O"

    Un = Un[0:-1]
    Un += ")"
    return Un


def regla2p(k:int):
    """Movimiento tipo U (Up).

    Returns
    -------
    str

    """
    assert((k < Nturnos-1) and (k>=0)), f'Turno invalido, k debe ser mayor o igual a 0 y menor a {Nturnos-1}, se utilizó {str(k)}.'
    Un = "("
    # for k in range(0,Nturnos):
    for a in range(0,Ncolores):
        b1  = Beta(0,a,k,0)
        b2  = Beta(1,a,k,1)
        b3  = Beta(5,a,k,5)
        b4  = Beta(4,a,k,4)
        b5  = Beta(8,a,k,8)
        b6  = Beta(9,a,k,9)
        b7  = Beta(12,a,k,12)
        b8  = Beta(13,a,k,13)
        b9  = Beta(14,a,k,14)     # OG: 23->09
        b10 = Beta(15,a,k,15)    # OG: 23->09
        b11 = Beta(22,a,k,22)    # OG: 04->23
        b12 = Beta(23,a,k,23)    # OG: 05->23
        #======STAY THE SAME=====#
        b13 = Beta(6,a,k,6)
        b14 = Beta(7,a,k,7)
        b15 = Beta(2,a,k,2)
        b16 = Beta(3,a,k,3)
        b17 = Beta(10,a,k,10)
        b18 = Beta(11,a,k,11)
        b19 = Beta(16,a,k,16)
        b20 = Beta(17,a,k,17)
        b21 = Beta(18,a,k,18)
        b22 = Beta(19,a,k,19)
        b23 = Beta(20,a,k,20)
        b24 = Beta(21,a,k,21)
        Un += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
        Un += "O"

    Un = Un[0:-1]
    Un += ")"
    return Un
