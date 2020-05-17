#================================ASPECTOS_TECNICOS==============================
from codificacion import deco_dict3 as decodic
from codificacion import decodifica3 as deco3
from codificacion import codifica3 as cod3
from codificacion import lis_to_col
from random import randint as rint
from operator import *
from dpll import dpll
import FNC as fn

lC= []  #Lista de Caracteres

Ncuadros = 24   #Número de Cuadros
Ncolores = 6    #Número de Colores
Nturnos  = 2   #Número de Turnos

max = 0

for i in range(1,Ncuadros+1):
    for j in range(1,Ncolores+1):
        for k in range(1,Nturnos+1):
            cod_num = cod3(i,j,k,Ncuadros+1,Ncolores+1,Nturnos+1)
            if (cod_num > max):
                max = cod_num
            n = chr(255+cod_num)
            lC.append(n)
            cud,col,tur = deco3(ord(n)- 255,Ncuadros+1,Ncolores+1,Nturnos+1)
            #  print("(X{}-Y{}-Z{}) -> {}".format(i,j,k,n))
            # print("{} -> (X{}-Y{}-Z{})\n".format(n,cud,col,tur))

#====================================FUNCIONES==================================
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
        posición turno n+1.

    Returns
    -------
    type
        Description of returned object.

    """
    reg = ""
    ant = chr(255+cod3(i1, j1, k1,Ncuadros+1,Ncolores+1,Nturnos+1))
    cons = chr(255+cod3(i2, j1, k1+1,Ncuadros+1,Ncolores+1,Nturnos+1))
    reg += "({}>{})".format(ant,cons)

    return reg

def Upsilon(m, T):
    """Short summary.

    Parameters
    ----------
    m : type
        Turno actual.
    T : type
        Cara del cubo, de 1 a 6;

    Returns
    -------
    type
        Description of returned object.

    """
    list_y = "("
    string = ""
    count=1
    if(T==1):t=1
    elif(T==2):t=5
    elif(T==3):t=9
    elif(T==4):t=13
    elif(T==5):t=17
    elif(T==6):t=21

    for i in range(t,t+4):
        for j in range(1,7):
            Y = chr(255 + cod3(i,j,m,Ncuadros+1,Ncolores+1,Nturnos+1))
            string += Y
    for nch in range(1,len(string)+1):

        if(count<4):
            list_y += "{}Y".format(string[nch-1])

            count+=1
        elif(count==4):
            list_y += "{})O(".format(string[nch-1])
            count =1

    list_y = list_y[:len(list_y)-2]

    return list_y

def regla0():
    """Short summary.

    Returns
    -------
    type
        Description of returned object.

    """

    caras = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    l_final = []
    s_final = ""

    while (caras != []) :
        num = rint(0,len(caras)-1)
        temp = chr(255+cod3(caras[num], j, 1,Ncuadros+1,Ncolores+1,Nturnos+1))
        l_final.append(temp)
        caras.remove(caras[num])

    s_final += "({}Y{})".format(l_final[0],l_final[1])

    for i in range(2,len(l_final)):
        temp = "("
        temp += s_final
        temp += "Y{})".format(l_final[i])
        s_final = temp

    return s_final

def basic_0():
    final = ""
    COLORES =  [3,1,5,5,
                5,6,2,6,
                4,3,1,1,
                1,4,2,2,
                5,3,6,5,
                4,3,2,6]

    L = []


    for i in range(1,len(COLORES)+1):
        cod_num = cod3(i,COLORES[i-1],1,Ncuadros+1,Ncolores+1,Nturnos+1)
        n = chr(255+cod_num)
        L.append(n)

    final += "({}Y{})".format(L[0],L[1])
    for i in range(2,len(L)):
        final = "(" + final
        final += "Y{})".format(L[i])

    return final

def regla1():
    """Ningun cuadro puede tener mas de un color.

    Returns
    -------
    str

    """
    string= "("

    lista1=[]
    for N in range(1,Nturnos+1):
        for s in range(1,Ncuadros+1):
            for c in range(1,Ncolores+1):
                Y = chr(255 + cod3(s,c,N,Ncuadros+1,Ncolores+1,Nturnos+1))
                string += Y
    for i in range(Ncolores*4):
        k =i*6
        fin = "({}>-((({}O{})O({}O{}))O({}O{})))".format(string[k],string[k+1],string[k+2],string[k+3],string[k+4],string[k+5],string[k+5])
        lista1.append(fin)


    string="((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(lista1[0],lista1[1],lista1[2],lista1[3],lista1[4],lista1[5],lista1[6],lista1[7],lista1[8],lista1[9],lista1[10],lista1[11],lista1[12],lista1[13],lista1[14],lista1[15],lista1[16],lista1[17],lista1[18],lista1[19],lista1[20],lista1[21],lista1[22],lista1[23])

    return string

def regla2():
    """Movimiento tipo U (Up).

    Returns
    -------
    str

    """
    Un = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(16,j,k,15)
            b2 = Beta(15,j,k,13)
            b3 = Beta(13,j,k,14)
            b4 = Beta(14,j,k,16)
            b5 = Beta(2,j,k,6)
            b6 = Beta(1,j,k,5)
            b7 = Beta(10,j,k,2)
            b8 = Beta(9,j,k,1)
            b9 = Beta(24,j,k,10)
            b10 = Beta(23,j,k,9)
            b11 = Beta(6,j,k,24)
            b12 = Beta(5,j,k,23)

            b13 = Beta(7,j,k,7)
            b14 = Beta(8,j,k,8)
            b15 = Beta(3,j,k,3)
            b16 = Beta(4,j,k,4)
            b17 = Beta(11,j,k,11)
            b18 = Beta(12,j,k,12)
            b19 = Beta(17,j,k,17)
            b20 = Beta(18,j,k,18)
            b21 = Beta(19,j,k,19)
            b22 = Beta(20,j,k,20)
            b23 = Beta(21,j,k,21)
            b24 = Beta(22,j,k,22)
            Un += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Un += "O"

    Un = Un[0:-1]
    Un += ")"
    return Un

def regla3():
    """Movimiento tipo U’ (Up Inverted).

    Returns
    -------
    str

    """
    Ui = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(15,j,k,16)
            b2 = Beta(13,j,k,15)
            b3 = Beta(14,j,k,13)
            b4 = Beta(16,j,k,14)
            b5 = Beta(6,j,k,2)
            b6 = Beta(5,j,k,1)
            b7 = Beta(2,j,k,10)
            b8 = Beta(1,j,k,9)
            b9 = Beta(10,j,k,24)
            b10 = Beta(9,j,k,23)
            b11 = Beta(24,j,k,6)
            b12 = Beta(23,j,k,5)

            b13 = Beta(7,j,k,7)
            b14 = Beta(8,j,k,8)
            b15 = Beta(3,j,k,3)
            b16 = Beta(4,j,k,4)
            b17 = Beta(11,j,k,11)
            b18 = Beta(12,j,k,12)
            b19 = Beta(17,j,k,17)
            b20 = Beta(18,j,k,18)
            b21 = Beta(19,j,k,19)
            b22 = Beta(20,j,k,20)
            b23 = Beta(21,j,k,21)
            b24 = Beta(22,j,k,22)
            Ui += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Ui += "O"

    Ui = Ui[0:-1]
    Ui += ")"
    return Ui

def regla4():
    """Movimiento tipo F (Front).

    Returns
    -------
    str

    """
    Fn = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(1,j,k,2)
            b2 = Beta(2,j,k,4)
            b3 = Beta(4,j,k,3)
            b4 = Beta(3,j,k,1)
            b5 = Beta(9,j,k,18)
            b6 = Beta(11,j,k,17)
            b7 = Beta(18,j,k,8)
            b8 = Beta(17,j,k,6)
            b9 = Beta(8,j,k,15)
            b10 = Beta(6,j,k,16)
            b11 = Beta(15,j,k,9)
            b12 = Beta(16,j,k,11)

            b13 = Beta(5,j,k,5)
            b14 = Beta(7,j,k,7)
            b15 = Beta(10,j,k,10)
            b16 = Beta(12,j,k,12)
            b17 = Beta(13,j,k,13)
            b18 = Beta(14,j,k,14)
            b19 = Beta(19,j,k,19)
            b20 = Beta(20,j,k,20)
            b21 = Beta(21,j,k,21)
            b22 = Beta(22,j,k,22)
            b23 = Beta(23,j,k,23)
            b24 = Beta(24,j,k,24)
            Fn += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Fn += "O"

    Fn = Fn[0:-1]
    Fn += ")"
    return Fn

def regla5():
    """Movimiento tipo F’ (Front Inverted).

    Returns
    -------
    str

    """
    Fi = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(2,j,k,1)
            b2 = Beta(4,j,k,2)
            b3 = Beta(3,j,k,4)
            b4 = Beta(1,j,k,3)
            b5 = Beta(18,j,k,9)
            b6 = Beta(17,j,k,11)
            b7 = Beta(8,j,k,18)
            b8 = Beta(6,j,k,17)
            b9 = Beta(15,j,k,8)
            b10 = Beta(16,j,k,6)
            b11 = Beta(9,j,k,15)
            b12 = Beta(11,j,k,16)

            b13 = Beta(5,j,k,5)
            b14 = Beta(7,j,k,7)
            b15 = Beta(10,j,k,10)
            b16 = Beta(12,j,k,12)
            b17 = Beta(13,j,k,13)
            b18 = Beta(14,j,k,14)
            b19 = Beta(19,j,k,19)
            b20 = Beta(20,j,k,20)
            b21 = Beta(21,j,k,21)
            b22 = Beta(22,j,k,22)
            b23 = Beta(23,j,k,23)
            b24 = Beta(24,j,k,24)
            Fi += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Fi += "O"

    Fi = Fi[0:-1]
    Fi += ")"
    return Fi

def regla6():
    """MMovimiento tipo D (Down).

    Returns
    -------
    str

    """
    Dn = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(17,j,k,18)
            b2 = Beta(18,j,k,20)
            b3 = Beta(20,j,k,19)
            b4 = Beta(19,j,k,17)
            b5 = Beta(21,j,k,7)
            b6 = Beta(22,j,k,8)
            b7 = Beta(7,j,k,3)
            b8 = Beta(8,j,k,4)
            b9 = Beta(3,j,k,11)
            b10 = Beta(4,j,k,12)
            b11 = Beta(11,j,k,21)
            b12 = Beta(12,j,k,22)

            b13 = Beta(1,j,k,1)
            b14 = Beta(2,j,k,2)
            b15 = Beta(5,j,k,5)
            b16 = Beta(6,j,k,6)
            b17 = Beta(9,j,k,9)
            b18 = Beta(10,j,k,10)
            b19 = Beta(13,j,k,13)
            b20 = Beta(14,j,k,14)
            b21 = Beta(15,j,k,15)
            b22 = Beta(16,j,k,16)
            b23 = Beta(23,j,k,23)
            b24 = Beta(24,j,k,24)
            Dn += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Dn += "O"

    Dn = Dn[0:-1]
    Dn += ")"
    return Dn

def regla7():
    """Movimiento tipo D’ (Down Inverted).

    Returns
    -------
    str

    """
    Di = "("
    for k in range(1,Nturnos):
        Di += "("
        for j in range(1,Ncolores+1):
            b1 = Beta(18,j,k,17)
            b2 = Beta(20,j,k,18)
            b3 = Beta(19,j,k,20)
            b4 = Beta(17,j,k,19)
            b5 = Beta(7,j,k,21)
            b6 = Beta(8,j,k,22)
            b7 = Beta(3,j,k,7)
            b8 = Beta(4,j,k,8)
            b9 = Beta(11,j,k,3)
            b10 = Beta(12,j,k,4)
            b11 = Beta(21,j,k,11)
            b12 = Beta(22,j,k,12)

            b13 = Beta(1,j,k,1)
            b14 = Beta(2,j,k,2)
            b15 = Beta(5,j,k,5)
            b16 = Beta(6,j,k,6)
            b17 = Beta(9,j,k,9)
            b18 = Beta(10,j,k,10)
            b19 = Beta(13,j,k,13)
            b20 = Beta(14,j,k,14)
            b21 = Beta(15,j,k,15)
            b22 = Beta(16,j,k,16)
            b23 = Beta(23,j,k,23)
            b24 = Beta(24,j,k,24)
            Di += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Di += "O"

    Di = Di[0:-1]
    Di += ")"
    return Di

def regla8():
    """Movimiento tipo B (Back).

    Returns
    -------
    str

    """
    Bn = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(22,j,k,24)
            b2 = Beta(24,j,k,23)
            b3 = Beta(23,j,k,21)
            b4 = Beta(21,j,k,22)
            b5 = Beta(10,j,k,13)
            b6 = Beta(12,j,k,14)
            b7 = Beta(13,j,k,7)
            b8 = Beta(14,j,k,5)
            b9 = Beta(5,j,k,19)
            b10 = Beta(7,j,k,20)
            b11 = Beta(19,j,k,12)
            b12 = Beta(20,j,k,10)

            b13 = Beta(1,j,k,1)
            b14 = Beta(2,j,k,2)
            b15 = Beta(3,j,k,3)
            b16 = Beta(4,j,k,4)
            b17 = Beta(6,j,k,6)
            b18 = Beta(8,j,k,8)
            b19 = Beta(9,j,k,9)
            b20 = Beta(11,j,k,11)
            b21 = Beta(15,j,k,15)
            b22 = Beta(16,j,k,16)
            b23 = Beta(17,j,k,17)
            b24 = Beta(18,j,k,18)
            Bn += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Bn += "O"

    Bn = Bn[0:-1]
    Bn += ")"
    return Bn

def regla9():
    """Movimiento tipo B’ (Back Inverted).

    Returns
    -------
    str

    """
    Bi = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(24,j,k,22)
            b2 = Beta(23,j,k,24)
            b3 = Beta(21,j,k,23)
            b4 = Beta(22,j,k,21)
            b5 = Beta(13,j,k,10)
            b6 = Beta(14,j,k,12)
            b7 = Beta(7,j,k,13)
            b8 = Beta(5,j,k,14)
            b9 = Beta(19,j,k,5)
            b10 = Beta(20,j,k,7)
            b11 = Beta(12,j,k,19)
            b12 = Beta(10,j,k,20)

            b13 = Beta(1,j,k,1)
            b14 = Beta(2,j,k,2)
            b15 = Beta(3,j,k,3)
            b16 = Beta(4,j,k,4)
            b17 = Beta(6,j,k,6)
            b18 = Beta(8,j,k,8)
            b19 = Beta(9,j,k,9)
            b20 = Beta(11,j,k,11)
            b21 = Beta(15,j,k,15)
            b22 = Beta(16,j,k,16)
            b23 = Beta(17,j,k,17)
            b24 = Beta(18,j,k,18)
            Bi += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Bi += "O"

    Bi = Bi[0:-1]
    Bi += ")"
    return Bi

def regla10():
    """Movimiento tipo R (Right).

    Returns
    -------
    str

    """
    Un = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(9,j,k,10)
            b2 = Beta(10,j,k,12)
            b3 = Beta(12,j,k,11)
            b4 = Beta(11,j,k,9)
            b5 = Beta(24,j,k,20)
            b6 = Beta(22,j,k,18)
            b7 = Beta(20,j,k,4)
            b8 = Beta(18,j,k,2)
            b9 = Beta(4,j,k,16)
            b10 = Beta(2,j,k,14)
            b11 = Beta(16,j,k,24)
            b12 = Beta(14,j,k,22)

            b13 = Beta(1,j,k,1)
            b14 = Beta(3,j,k,3)
            b15 = Beta(5,j,k,5)
            b16 = Beta(6,j,k,6)
            b17 = Beta(7,j,k,7)
            b18 = Beta(8,j,k,8)
            b19 = Beta(13,j,k,13)
            b20 = Beta(15,j,k,15)
            b21 = Beta(17,j,k,17)
            b22 = Beta(19,j,k,19)
            b23 = Beta(21,j,k,21)
            b24 = Beta(23,j,k,23)
            Un += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Un += "O"

    Un = Un[0:-1]
    Un += ")"
    return Un

def regla11():
    """Movimiento tipo R’ (Right Inverted).

    Returns
    -------
    str

    """
    Ri = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(10,j,k,9)
            b2 = Beta(12,j,k,10)
            b3 = Beta(11,j,k,12)
            b4 = Beta(9,j,k,11)
            b5 = Beta(20,j,k,24)
            b6 = Beta(18,j,k,22)
            b7 = Beta(4,j,k,20)
            b8 = Beta(2,j,k,18)
            b9 = Beta(16,j,k,4)
            b10 = Beta(14,j,k,2)
            b11 = Beta(24,j,k,16)
            b12 = Beta(22,j,k,14)

            b13 = Beta(1,j,k,1)
            b14 = Beta(3,j,k,3)
            b15 = Beta(5,j,k,5)
            b16 = Beta(6,j,k,6)
            b17 = Beta(7,j,k,7)
            b18 = Beta(8,j,k,8)
            b19 = Beta(13,j,k,13)
            b20 = Beta(15,j,k,15)
            b21 = Beta(17,j,k,17)
            b22 = Beta(19,j,k,19)
            b23 = Beta(21,j,k,21)
            b24 = Beta(23,j,k,23)
            Ri += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Ri += "O"

    Ri = Ri[0:-1]
    Ri += ")"
    return Ri

def regla12():
    """Movimiento tipo L (Left).

    Returns
    -------
    str

    """
    Ln = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(5,j,k,6)
            b2 = Beta(6,j,k,8)
            b3 = Beta(8,j,k,7)
            b4 = Beta(7,j,k,5)
            b5 = Beta(1,j,k,17)
            b6 = Beta(3,j,k,19)
            b7 = Beta(17,j,k,21)
            b8 = Beta(19,j,k,23)
            b9 = Beta(21,j,k,13)
            b10 = Beta(23,j,k,15)
            b11 = Beta(13,j,k,1)
            b12 = Beta(15,j,k,3)

            b13 = Beta(2,j,k,2)
            b14 = Beta(4,j,k,4)
            b15 = Beta(9,j,k,9)
            b16 = Beta(10,j,k,10)
            b17 = Beta(11,j,k,11)
            b18 = Beta(12,j,k,12)
            b19 = Beta(14,j,k,14)
            b20 = Beta(16,j,k,16)
            b21 = Beta(18,j,k,18)
            b22 = Beta(20,j,k,20)
            b23 = Beta(22,j,k,22)
            b24 = Beta(24,j,k,24)
            Ln += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Ln += "O"

    Ln = Ln[0:-1]
    Ln += ")"
    return Ln

def regla13():
    """Movimiento tipo L’ (Left Inverted) .

    Returns
    -------
    str

    """
    Li = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(6,j,k,5)
            b2 = Beta(8,j,k,6)
            b3 = Beta(7,j,k,8)
            b4 = Beta(5,j,k,7)
            b5 = Beta(17,j,k,1)
            b6 = Beta(19,j,k,3)
            b7 = Beta(21,j,k,17)
            b8 = Beta(23,j,k,19)
            b9 = Beta(13,j,k,21)
            b10 = Beta(15,j,k,23)
            b11 = Beta(1,j,k,13)
            b12 = Beta(3,j,k,15)

            b13 = Beta(2,j,k,2)
            b14 = Beta(4,j,k,4)
            b15 = Beta(9,j,k,9)
            b16 = Beta(10,j,k,10)
            b17 = Beta(11,j,k,11)
            b18 = Beta(12,j,k,12)
            b19 = Beta(14,j,k,14)
            b20 = Beta(16,j,k,16)
            b21 = Beta(18,j,k,18)
            b22 = Beta(20,j,k,20)
            b23 = Beta(22,j,k,22)
            b24 = Beta(24,j,k,24)
            Li += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            Li += "O"

    Li = Li[0:-1]
    Li += ")"
    return Li

def regla14():
    """Movimiento tipo N (Not move).

    Returns
    -------
    str

    """
    N = "("
    for k in range(1,Nturnos):
        for j in range(1,Ncolores+1):
            b1 = Beta(1,j,k,1)
            b2 = Beta(2,j,k,2)
            b3 = Beta(3,j,k,3)
            b4 = Beta(4,j,k,4)
            b5 = Beta(5,j,k,5)
            b6 = Beta(6,j,k,6)
            b7 = Beta(7,j,k,7)
            b8 = Beta(8,j,k,8)
            b9 = Beta(9,j,k,9)
            b10 = Beta(10,j,k,10)
            b11 = Beta(11,j,k,11)
            b12 = Beta(12,j,k,12)

            b13 = Beta(13,j,k,13)
            b14 = Beta(14,j,k,14)
            b15 = Beta(15,j,k,15)
            b16 = Beta(16,j,k,16)
            b17 = Beta(17,j,k,17)
            b18 = Beta(18,j,k,18)
            b19 = Beta(19,j,k,19)
            b20 = Beta(20,j,k,20)
            b21 = Beta(21,j,k,21)
            b22 = Beta(22,j,k,22)
            b23 = Beta(23,j,k,23)
            b24 = Beta(24,j,k,24)
            N += "((((((((((((((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
            N += "O"

    N = N[0:-1]
    N += ")"
    return N

def regla15():
    """Solo puede haber un movimiento por turno.

    Returns
    -------
    str

    """
    string = "("
    temp =[]
    reglas = [regla2(),regla3(),regla4(),regla5(),regla6(),regla7(),regla8(),regla9(),regla10(),regla11(),regla12(),regla13(),regla14()]
    reglas_cop = [regla2(),regla3(),regla4(),regla5(),regla6(),regla7(),regla8(),regla9(),regla10(),regla11(),regla12(),regla13(),regla14()]
    largo = len(reglas)
    for j in range(len(reglas)):
        reglas_cop.pop(j)
        print(len(reglas_cop))
        mini = "({}>-((((((({})O({}))O(({})O({})))O(({})O({})))O(({})O({})))O(({})O({})))O(({})O({}))))".format(reglas[j],reglas_cop[0],reglas_cop[1],reglas_cop[2],reglas_cop[3],reglas_cop[4],reglas_cop[5],reglas_cop[6],reglas_cop[7],reglas_cop[8],reglas_cop[9],reglas_cop[10],reglas_cop[11],reglas_cop[11])
        temp.append(mini)
        reglas_cop = reglas.copy()
        print(len(reglas_cop))

    string = "(((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12])

    return string

def regla16(Nturnos:int):
    """Cubo solucionado en el turnon.

    Nturnos : int
        Numero total de túrnos.

    Returns
    -------
    str

    """
    string ="("
    for n in range(1,Nturnos+1):
        for S in range(1,Ncolores+1):
                string +="(" + Upsilon(n,S) + ")"
                if(S != 6):
                    string += "Y"
                else:
                    continue
        if(n!=Nturnos):
            string +="O"
        else:continue

    string += ")"
    #string = string[:len(string)-5]
    return string

def regla17():
    """Integridad del cubo terminado.

    Returns
    -------
    str

    """
    string = ""
    lista_sis=[]
    for N in range(1, Nturnos+1):
        sis= "(({}>{})Y({}>{}))".format(regla2(),regla2(),regla2(),regla2())
        lista_sis.append(sis)
    string = "({}Y{})".format(lista_sis[0],lista_sis[1])
    return sis



#====================================CODIGO=====================================

# reglas = [regla0(),regla1(),regla2(),regla3(),regla4(),regla5(),regla6(),regla7(),regla8(),regla9(),regla10(),regla11(),regla12(),regla13(),regla14(),regla15(),regla16(),regla17()]

formula  = regla15()
fFNC = fn.Tseitin(formula, lC)

# formula_de_la_muere  = "((((((((((((((((({0}Y{1})Y{2})Y{3})Y{4})Y{5})Y{6})Y{7})Y{8})Y{9})Y{10})Y{11})Y{12})Y{13})Y{14})Y{15})Y{16})Y{17})".format(reglas[0],reglas[1],reglas[2],reglas[3],reglas[4],reglas[5],reglas[6],reglas[7],reglas[8],reglas[9],reglas[10],reglas[11],reglas[12],reglas[13],reglas[14],reglas[15],reglas[16],reglas[17])
# print(formula_de_la_muere)
# fFNC = fn.Tseitin(formula_de_la_muere, lC)

#print(len(fFNC))
# print(fFNC)

# Se obtiene la forma clausal como lista de listas de literales
fClaus = fn.formaClausal(fFNC)
# print(fClaus)

#print(len(fClaus))
# print(regla2())
#

test = {}

test = dpll(fClaus,test)

#sat, dic = test

print(test)

#final = decodic(dic,Ncuadros,Ncolores,Nturnos)


#sorted(final, key=itemgetter(2))




# print(final)
with open("satisfacible.txt", "w") as f:
    for i in final:
        f.write("{} {} {} {}\n".format(i[0],i[1],i[2],i[3]))

file_list = []
with open("satisfacible.txt","r") as f:
    for line in f:
        file_list.extend([line.split()])

for l in file_list:
    # l[0] = "T{}".format(l[0])
    # l[1] = "S{}".format(l[1])
    # l[2] = "C{}".format(l[2])
    l[0] = "{}".format(l[0])
    l[1] = "{}".format(l[1])
    l[2] = "{}".format(l[2])

colores = lis_to_col(file_list,Nturnos,Ncuadros,Ncolores)

print(file_list)
