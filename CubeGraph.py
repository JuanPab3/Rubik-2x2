#================================ASPECTOS_TECNICOS==============================
import pygame as pg

pg.init()

win = pg.display.set_mode((600,500))
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





#====================================FUNCIONES==================================

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


#====================================CODIGO=====================================

#Todos los cuadros iniciaron de color blanco
s1 = Square(250,130,0)
s2 = Square(310,130,0)
s3 = Square(250,190,0)
s4 = Square(310,190,0)

s5 = Square(130,130,0)
s6 = Square(190,130,0)
s7 = Square(130,190,0)
s8 = Square(190,190,0)

s9 = Square(370,130,0)
s10 = Square(430,130,0)
s11 = Square(370,190,0)
s12 = Square(430,190,0)

s13 = Square(250,10,0)
s14 = Square(310,10,0)
s15 = Square(250,70,0)
s16 = Square(310,70,0)

s17 = Square(250,250,0)
s18 = Square(310,250,0)
s19 = Square(250,310,0)
s20 = Square(310,310,0)

s21 = Square(250,370,0)
s22 = Square(310,370,0)
s23 = Square(250,430,0)
s24 = Square(310,430,0)

#Lista compuesta por todos los cuadrados que conforman el cubo.
cube = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24]

"""
Posiciones arbitrarias generadas por mi.
 |
 |
 |
 v
"""
nc1 = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5] # Estado Inicial
nc2 = [0,0,0,0,1,4,1,4,3,2,3,2,3,3,1,1,2,2,4,4,5,5,5,5] # Front
nc3 = [0,0,1,4,1,4,5,5,3,2,0,0,3,3,1,1,2,2,4,4,3,2,5,5] # Down


pasos = [nc1,nc2,nc3] #Turnos

run = True
turno = 0

setCube(cube,pasos[turno])  #Se deja el cubo en Estado Inicial

font = pg.font.SysFont("VT323",24,False,False,None) #Para mejor experiencia instala hay que intalar la tipografía que está en la carpeta.

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
        setCube(cube,pasos[turno])

    if keys[pg.K_LEFT]:
        turno = turno - 1
        if (turno < 0):
            turno += 1
        setCube(cube,pasos[turno])

    text = font.render("Turno {}".format(1+turno),True, (255,255,255)) # Render del texto en la pantalla

    win.blit(text,(400,450))

    for i in cube:
        pg.draw.rect(win,i.color,(i.x,i.y,i.width,i.height))

    pg.display.update() # volver a cargar los datos para el nuevo frame


pg.quit() # Cerrar Pestaña
