#================================ASPECTOS_TECNICOS==============================
from codificacion import codifica3 as cod3
from codificacion import decodifica3 as deco3
from random import randint as rint
import FNC as fn
from dpll import dpll

lC= []  #Lista de Caracteres

Ncuadros = 24   #Número de Cuadros
Ncolores = 6    #Número de Colores
Nturnos  = 14   #Número de Turnos

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



def regla1():
    """Ningun cuadro puede tener mas de un color.

    Returns
    -------
    str

    """
    string= ""
    fin="("
    for N in range(1,Nturnos+1):
        for s in range(1,Ncuadros+1):
            for c in range(1,Ncolores+1):
                Y = chr(255 + cod3(s,c,N,Ncuadros+1,Ncolores+1,Nturnos+1))
                string += Y
    for i in range(144):
        k =i*6
        fin += "({}>-({}O{}O{}O{}O{}))Y".format(string[k],string[k+1],string[k+2],string[k+3],string[k+4],string[k+5])
#        print(deco3(ord(string[k])- 255,Ncuadros+1,Ncolores+1,Nturnos+1)," > -  ",deco3(ord(string[k+5])- 255,Ncuadros+1,Ncolores+1,Nturnos+1))

    fin=fin[:len(fin)-1]
    fin+=")"
    return fin

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
    reglas = [regla2(),regla3(),regla4(),regla5(),regla6(),regla7(),regla8(),regla9(),regla10(),regla11(),regla12(),regla13(),regla14()]
    largo = len(reglas)
    for i in range(largo):
        regla = reglas.pop()
        cons = ""
        for j in reglas:
            cons+= j + "O"
        cons = cons[:len(cons)-1]
        string += "(({}>-({}))O la siguiente regla ".format(regla,cons )
        reglas.insert(0, regla)
        cons=""

    string= string[:len(string)-1]
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
        for S in range(1,7):
                string +="(" + Upsilon(n,S) + ")"
                if(S != 6):
                    string += "Y"
                else:
                    continue
        if(n!=Nturnos):
            string +="O"
        else:continue

    string += ")"
#    string = string[:len(string)-5]
    return string

def regla17():
    """Integridad del cubo terminado.

    Returns
    -------
    str

    """

    pass



#====================================CODIGO=====================================

#formula = "("+regla2()+"Y"+regla3()+"Y"+regla4()+"Y"+regla5()+"Y"+regla6()+"Y"+regla7()+"Y"+regla8()+"Y"+regla9()+"Y"+regla10()+"Y"+regla11()+"Y"+regla12()+"Y"+regla13()+"Y"+regla14()+")"
# formula  = regla2()
# fFNC = fn.Tseitin(formula, lC)

#print(len(fFNC))
# print(fFNC)
regla0()

# Se obtiene la forma clausal como lista de listas de literales
# fClaus = fn.formaClausal(fFNC)
# print(fClaus)

#print(len(fClaus))
# print(regla2())
#

# test = dpll(fClaus,{})

# print(test)
