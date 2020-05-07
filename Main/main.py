#================================ASPECTOS_TECNICOS==============================
from codificacion import codifica3 as cod3
from codificacion import decodifica3 as deco3

lC= []  #Lista de Caracteres

# Ncuadros = 24   #Número de Cuadros
# Ncolores = 6    #Número de Colores
# Nturnos  = 14   #Número de Turnos

Ncuadros = 24   #Número de Cuadros
Ncolores = 6    #Número de Colores
Nturnos  = 14   #Número de Turnos

for i in range(1,Ncuadros+1):
    for j in range(1,Ncolores+1):
        for k in range(1,Nturnos+1):
            n = chr(255+cod3(i,j,k,Ncuadros+1,Ncolores+1,Nturnos+1))
            lC.append(n)
            cud,col,tur = deco3(ord(n)- 255,Ncuadros+1,Ncolores+1,Nturnos+1)
            #  print("(X{}-Y{}-Z{}) -> {}".format(i,j,k,n))
            # pri nt("{} -> (X{}-Y{}-Z{})\n".format(n,cud,col,tur))

#====================================FUNCIONES==================================
def Beta(i1:int, j1:int ,k1:int, i2:int ):
    """La siguiente notacion esta dada para realizar el cambio de color entre dos cuadros.

    Parameters
    ----------
    i1 : int
        Description of parameter `i1`.
    j1 : int
        Description of parameter `j1`.
    k1 : int
        Description of parameter `k1`.
    i2 : int
        Description of parameter `i2`.

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


def regla1():
    """Ningun cuadro puede tener mas de un color.

    Returns
    -------
    str

    """
    pass

def regla2():
    """Movimiento tipo U (Up).

    Returns
    -------
    str

    """
    Un = "("
    for k in range(1,Nturnos):
        Un += "("
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
            Un += "({}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{}Y{})".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24)
        Un += ")O"
    Un = Un[0:-1]
    Un += ")"
    return Un

def regla3():
    """Movimiento tipo U’ (Up Inverted).

    Returns
    -------
    str

    """
    pass

def regla4():
    """Movimiento tipo F (Front).

    Returns
    -------
    str

    """
    pass

def regla5():
    """Movimiento tipo F’ (Front Inverted).

    Returns
    -------
    str

    """
    pass

def regla6():
    """MMovimiento tipo D (Down).

    Returns
    -------
    str

    """
    pass

def regla7():
    """Movimiento tipo D’ (Down Inverted).

    Returns
    -------
    str

    """
    pass

def regla8():
    """Movimiento tipo B (Back).

    Returns
    -------
    str

    """
    pass

def regla9():
    """Movimiento tipo B’ (Back Inverted).

    Returns
    -------
    str

    """
    pass

def regla10():
    """Movimiento tipo R (Right).

    Returns
    -------
    str

    """
    pass

def regla11():
    """Movimiento tipo R’ (Right Inverted).

    Returns
    -------
    str

    """
    pass

def regla12():
    """Movimiento tipo L (Left).

    Returns
    -------
    str

    """
    pass

def regla13():
    """Movimiento tipo L’ (Left Inverted) .

    Returns
    -------
    str

    """
    pass

def regla14():
    """Movimiento tipo N (Not move).

    Returns
    -------
    str

    """
    pass

def regla15():
    """Solo puede haber un movimiento por turno.

    Returns
    -------
    str

    """
    pass

def regla16(Nturnos:int):
    """Cubo solucionado en el turnon.

    Nturnos : int
        Numero total de túrnos.

    Returns
    -------
    str

    """
    pass

def regla17():
    """Integridad del cubo terminado.

    Returns
    -------
    str

    """
    pass



#====================================CODIGO=====================================

print(regla2())
print(len(regla2()))
