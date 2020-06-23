# Codificacion y decodificacion de una tabla de Nf filas y Nc columnas

def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c
    assert ((f >= 0) and (f <= Nf - 1)),"Fila incorrecta! Debe ser un numero entre 0 y {}".format(Nf)
    assert ((c >= 0) and (c <= Nc - 1)),"Columna incorrecta! Debe ser un numero entre 0 y {}".format(Nc)
    n = Nc * f + c
    # print(u'Número a codificar:', n)
    return n

def decodifica(x, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    n = x
    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Caracter incorrecto! Debe estar entre 0 y {0}, se recibio {1}'.format(Nf * Nc - 1,n)
    f = int(n / Nc)
    c = n % Nc
    return f, c

def codifica3(f, c, o, Nf, Nc, No):
    # Funcion que codifica la fila f, columna c, y objeto o
    # print('f : '+str(f))
    # print('c : '+str(c))
    # print('o : '+str(o))
    # print('Nf: '+str(Nf))
    # print('Nc: '+str(Nc))
    # print('No: '+str(No))
    assert((f >= 0) and (f <= Nf - 1)), "Fila incorrecta! Debe ser un numero entre 0 y {}".format(str(Nf - 1))
    assert((c >= 0) and (c <= Nc - 1)), "Columna incorrecta! Debe ser un numero entre 0 y {}".format(str(Nc - 1))
    assert((o >= 0) and (o <= No - 1)), "Fila incorrecta! Debe ser un numero entre 0 y {}".format(str(No - 1))
    v1 = codifica(f, c, Nf, Nc)
    v2 = codifica(v1, o , Nf * Nc, No)
#     print(f'({f},{c},{o})->{v2}')
    return v2

def decodifica3(x, Nf, Nc, No):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    # print('x : '+str(x))
    # print('Nf: '+str(Nf))
    # print('Nc: '+str(Nc))
    # print('No: '+str(No))
    v1, o = decodifica(x, Nf * Nc, No)
    f, c = decodifica(v1, Nf, Nc)
#     print(f'{x}->({f},{c},{o})')
    return f, c, o

def deco_dict3(I:dict,Ncuadros:int,Ncolores:int,Nturnos:int):
    keys = I.keys()
    deco_list = []
    for i in keys:
#         print("i : "+i)
#         print('Ni: '+str(Ncuadros))
#         print('Nj: '+str(Ncolores))
#         print('Nk: '+str(Nturnos))
        cud,col,tur = decodifica3(ord(i)- 256,Ncuadros,Ncolores,Nturnos)
        lis = [cud,col,tur,I[i]]
        # str = "{}-{}-{}-{}".format(tur,cud,col,I[i])
        deco_list.append(lis)
    return deco_list
