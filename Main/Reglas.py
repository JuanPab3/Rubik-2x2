from codificacion import deco_dict3 as decodic
from codificacion import decodifica3 as deco3
from codificacion import codifica3 as cod3
from codificacion import lis_to_col
from random import randint as rint
from CubeGraph import RUBIC
from operator import *



Ncuadros = 24   #Número de Cuadros
Ncolores = 6    #Número de Colores
Nturnos  = 2   #Número de Turnos

max = 0
lC= []
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
    reg += "(-{}O{})".format(ant,cons)

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
    lista= []
    lista2 =[]
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
            lista.append( Y)

    lista2.append("((({}Y{})Y{})Y{})".format(lista[0],lista[1],lista[2],lista[3]))
    lista2.append("((({}Y{})Y{})Y{})".format(lista[4],lista[5],lista[6],lista[7]))
    lista2.append("((({}Y{})Y{})Y{})".format(lista[8],lista[9],lista[10],lista[11]))
    lista2.append("((({}Y{})Y{})Y{})".format(lista[12],lista[13],lista[14],lista[15]))
    lista2.append("((({}Y{})Y{})Y{})".format(lista[16],lista[17],lista[18],lista[19]))
    lista2.append("((({}Y{})Y{})Y{})".format(lista[20],lista[21],lista[22],lista[23]))
    string = "((((({}O{})O{})O{})O{})O{})".format(lista2[0],lista2[1],lista2[2],lista2[3],lista2[4],lista2[5])



    return string

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
                4,3,6,5,
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
    equivalencias = ["(A={})".format(regla2()),
    "(B={})".format(regla3()),
    "(C={})".format(regla4()),
    "(D={})".format(regla5()),
    "(E={})".format(regla6()),
    "(F={})".format(regla7()),
    "((-GO{0})Y({0}>G))".format(regla8()),
    "(H={})".format(regla9()),
    "(I={})".format(regla10()),
    "(J={})".format(regla11()),
    "(K={})".format(regla12()),
    "(L={})".format(regla13()),
    "(M={})".format(regla14())]
    #    "(G={})".format(regla8()),
    letras=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
    equivalencias_= equivalencias.copy()
    itoria = "(((((((((((({}Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})Y{})".format(equivalencias[0],equivalencias[1],equivalencias[2],equivalencias[3],equivalencias[4],equivalencias[5],equivalencias[6],equivalencias[7],equivalencias[8],equivalencias[9],equivalencias[10],equivalencias[11],equivalencias[12])
    largo = len(reglas)
    for j in range(len(reglas)):
        equivalencias.pop(j)
        #        (-((((((((((({}O{})O{})O{})O{})O{})O{})O{})O{})O{})O{})O{}))
        negacion = "(-(((((((((({}O{})O{})O{})O{})O{})O{})O{})O{})O{})O{})O{}))".format(equivalencias[0],equivalencias[1],equivalencias[2],equivalencias[3],equivalencias[4],equivalencias[5],equivalencias[6],equivalencias[7],equivalencias[8],equivalencias[9],equivalencias[10],equivalencias[11])

        mini = "(({}>{})Y{})".format(reglas[j],negacion,itoria)
        #       ({}>-((((((((((({}O{})O{})O{})O{})O{})O{})O{})O{})O{})O{})O{}))
        temp.append(mini)
        reglas_cop = reglas.copy()
        equivalencias = equivalencias_.copy()


    string = "(((((((((((({}O{})O{})O{})O{})O{})O{})O{})O{})O{})O{})O{})O{})".format(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12])

    return string

def regla16(Nturnos:int):
    """Cubo solucionado en el turnon.

    Nturnos : int
        Numero total de túrnos.

    Returns
    -------
    str

    """
    string = ""
    forms = []
    for n in range(1,Nturnos+1):
        for S in range(1,Ncolores+1):
                forms.append( Upsilon(n,S) )

    string += "({}Y{})".format(forms[0],forms[1])

    for i in range(2,len(forms)):
        temp = "("
        temp += string
        temp += "Y{})".format(forms[i])
        string = temp

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
        sis= "(({}>{})Y({}>{}))".format(regla16(N),regla14(),regla14(),regla16(N))
        lista_sis.append(sis)
    string += "({}Y{})".format(lista_sis[0],lista_sis[1])
    print(len(lista_sis))
    if(len(lista_sis)>2):
        for i in range(2,len(lista_sis)):
            temp = "("
            temp += string
            temp += "Y{})".format(lista_sis[i])
            string = temp


    return string
