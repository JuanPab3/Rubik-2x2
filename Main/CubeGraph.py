#================================ASPECTOS_TECNICOS==============================
import pygame as pg
from pygame.locals import *


turnosMax = 4
pg.init()

# dimenciones
x = 1280
y = 720

win = pg.display.set_mode((x,y))
pg.display.set_caption("Rubik Cube 2X2")

#=====================================CLASES====================================

class Square:


    def __init__(self,x,y,color):
        """Este elemento representa un cudro del cubo Rubik.

        Parameters
        ----------
        x : int
            Posición en el eje x (en el graficador).
        y : int
            Posición en el eje y (en el graficador).
        color : int
            Indice del color del cubo, esté luego representa un elemento de la
            lista 'self.colores'.

        """


        self.colores = [(255,255,255),(0,159,215,84),(0,217,157,85),(104,0,213,84),(252,61,85,99),(255,172,0,100)]
        self.x = x
        self.y = y
        self.height = 40
        self.width = 40
        self.color = self.colores[color]

    def setColor(self, color):
        """Cambia el color de un cuadro por otro.

        Parameters
        ----------
        color : int

        Indice del nuevo valor de color.
        """
        self.color = self.colores[color]

    def setSize(self,v:float):
        """Cambia el color de un cuadro por otro.

        Parameters
        ----------
        v : float

        Valor del nuevo height y width.
        """
        self.height = v
        self.width = v

class TurnDic:
    """Short summary.

    Parameters
    ----------
    square : int
        El cuadrado que se esta representando en esa interpretación.
    color : int
        El color que se esta representando en esa interpretación.
    turn : int
        El turno que se esta representando en esa interpretación.


    Attributes
    ----------
    dirS : type
        Dicionario con todos los cuadrados.
    dirC : type
        Dicionario con todos los colores.
    dirT : type
        Dicionario con todos los turnos.
    """

    def __init__(self, square:int, color:int, turn:int ): #O(turn)
        self.dirS = {"s1":0,"s2":0,"s3":0,"s4":0,"s5":0,"s6":0,"s7":0,"s8":0,"s9":0,"s10":0,"s11":0,"s12":0,"s13":0,"s14":0,"s15":0,"s16":0, "s17":0,"s18":0,"s19":0,"s20":0,"s21":0,"s22":0,"s23":0,"s24":1}
        self.dirC = {"c1":0,"c2":0,"c3":0,"c4":0,"c5":0,"c6":0}
        self.dirT = {}

        for i in range(1,turnosMax+1):
            self.dirT["t{}".format(i)] = 0

        self.dirS["s{}".format(square)]= 1
        self.dirC["c{}".format(color)] = 1
        self.dirT["t{}".format(turn)]  = 1


#====================================FUNCIONES==================================



def creador_turnos(J:list,Ncuadros:int,Ncolores:int,Nturnos:int):
    """Crear lista de tirno a partir de lista de diccionarios

    Parameters
    ----------
    J : list
        Lista de tres valores, cada uno representando el cuadro, el color y
        el turno respectivamente.

    Returns
    -------
    list
        Lista de lista que contiene los colores de los cuadros por cada turno.

    """
    pasos = []
    for k in range(Nturnos):
        temp = []
        for i in range(Ncuadros):
            temp.append(0)
        pasos.append(temp)

    for l in J:
        s = l[0]
        c = l[1]
        t = l[2]

        # print("({},{},{})".format(t,s,c))
        if (t <= Nturnos and t >= 1):
            if (s <= Ncuadros and s >= 1):
                if (c <= Ncolores and c >= 1):
                    pasos[t-1][s-1] = c-1
                else:
                    pass
            else:
                pass
        else:
            pass

    return pasos



def setCube(listaR,listaC):
    """Cambia los colores de cada elemento del cubo.

    Parameters
    ----------
    listaR : list
        Lista que contiene a todos los cuadros del cubo.
    listaC : type
        Lista que contiene los colores que se les asignaran a las posiciones
        de los elementos en ListaR.
    """
    for i in range(0,24):
        listaR[i].setColor(listaC[i])


#===============================ESTRUCTURA_CUBO================================

#Todos los cuadros iniciaron de color blanco

pex = (1.5*x/3) - 60 #Pos. estandart en x
pey = y/12 #Pos. estandart en x

s1 = Square(pex,130+pey,0)
s2 = Square(pex+60,130+pey,0)
s3 = Square(pex,190+pey,0)
s4 = Square(pex+60,190+pey,0)

s5 = Square(pex-120,130+pey,0)
s6 = Square(pex-60,130+pey,0)
s7 = Square(pex-120,190+pey,0)
s8 = Square(pex-60,190+pey,0)

s9 = Square(pex+120,130+pey,0)
s10 = Square(pex+180,130+pey,0)
s11 = Square(pex+120,190+pey,0)
s12 = Square(pex+180,190+pey,0)

s13 = Square(pex,10+pey,0)
s14 = Square(pex+60,10+pey,0)
s15 = Square(pex,70+pey,0)
s16 = Square(pex+60,70+pey,0)

s17 = Square(pex,250+pey,0)
s18 = Square(pex+60,250+pey,0)
s19 = Square(pex,310+pey,0)
s20 = Square(pex+60,310+pey,0)

s21 = Square(pex,370+pey,0)
s22 = Square(pex+60,370+pey,0)
s23 = Square(pex,430+pey,0)
s24 = Square(pex+60,430+pey,0)

#Lista compuesta por todos los cuadrados que conforman el cubo.
cube = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24]

#===============================================================================

def RUBIC(movimientos:list,Ncuadros:int,Ncolores:int,Nturnos:int):

    pasos = creador_turnos(movimientos,Ncuadros,Ncolores,Nturnos)
    run = True
    turno = 0
    setCube(cube,pasos[turno])  #Se deja el cubo en Estado Inicial

    font1 = pg.font.SysFont("VT323",24,False,False,None) #Para mejor experiencia instala hay que intalar la tipografía que está en la carpeta.
    font2 = pg.font.SysFont("VT323",70,False,False,None) #Para mejor experiencia instala hay que intalar la tipografía que está en la carpeta.

    b_ms = pg.mixer
    b_ms.music.load("tetris.wav")
    b_ms.music.play(-1)

    while  run:

        pg.time.delay(120) # Tiempo en ms para entre frames

        for event in pg.event.get():
            if event.type == pg.QUIT: # Salir del loop
                run = False;

        win.fill((0,0,0)) # Redefinición del espacio

        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            turno = turno + 1
            if (turno >= len(pasos)):
                turno -= 1

        if keys[pg.K_LEFT]:
            turno = turno - 1
            if (turno < 0):
                turno += 1

        if keys[pg.K_DOWN]:
            turno = 0

        if keys[pg.K_UP]:
            turno = len(pasos) - 1

        if keys[pg.K_q]:
            run = False

        setCube(cube,pasos[turno])

        texta = font2.render("Rubik 2x2",True, (255,255,255)) # Render del texto en la pantalla
        text = font2.render("Turno {}".format(1+turno),True, (255,255,255)) # Render del texto en la pantalla

        pxa = x/2 - (texta.get_size()[0]/7)*4
        pya = y/2 + texta.get_size()[1]*2.5

        pxb = x/2 - (texta.get_size()[0]/7)*3.2
        pyb = y/2 + texta.get_size()[1]*3.5

        win.blit(texta,(pxa,pya))
        win.blit(text,(pxb,pyb))

        for i in cube:
            pg.draw.rect(win,i.color,(i.x,i.y,i.width,i.height))

        pg.display.update() # volver a cargar los datos para el nuevo frame


    pg.quit() # Cerrar Pestaña


# RUBIC(pasos)
