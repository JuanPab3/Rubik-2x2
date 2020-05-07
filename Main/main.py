#================================ASPECTOS_TECNICOS==============================
from codificacion import codifica3 as cod3
from codificacion import decodifica3 as deco3

lC= []  #Lista de Caracteres

Ncuadros = 24   #Número de Cuadros
Ncolores = 6    #Número de Colores
Nturnos  = 14   #Número de Turnos

for i in range(Ncuadros):
    for j in range(Ncolores):
        for k in range(Nturnos):
            n = chr(255+cod3(i+1,j+1,k+1,Ncuadros+1,Ncolores+1,Nturnos+1))
            lC.append(n)
            cud,col,tur = deco3(ord(n)- 255,Ncuadros+1,Ncolores+1,Nturnos+1)
            print("(X{}-Y{}-Z{}) -> {}".format(i+1,j+1,k+1,n))
            print("{} -> (X{}-Y{}-Z{})\n".format(n,cud,col,tur))

#====================================FUNCIONES==================================

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
    pass

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
