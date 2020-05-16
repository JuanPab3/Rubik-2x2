# Codificacion y decodificacion de una tabla de Nf filas y Nc columnas

def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c
    assert ((f >= 1) and (f <= Nf)),"Fila incorrecta! Debe ser un numero entre 1 y {}".format(Nf)
    assert ((c >= 1) and (c <= Nc)),"Columna incorrecta! Debe ser un numero entre 1 y {}".format(Nc)
    n = Nc * (f - 1) + c
    # print(u'Número a codificar:', n)
    return n

def decodifica(x, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    n = x
    if ((n < 1) or (n > Nf * Nc)):
        print('Caracter incorrecto! Debe estar entre 1 y', Nf * Nc)
        return None
    else:
        n = n - 1
        f = int(n / Nc) + 1
        c = n % Nc + 1
        return f, c

def codifica3(f, c, o, Nf, Nc, No):
    # Funcion que codifica la fila f, columna c, y objeto o
    assert((f >= 1) and (f <= Nf)), "Fila incorrecta! Debe ser un numero entre 1 y {}".format(str(Nf))
    assert((c >= 1) and (c <= Nc)), "Columna incorrecta! Debe ser un numero entre 1 y {}".format(str(Nc))
    assert((o >= 1) and (o <= Nf)), "Fila incorrecta! Debe ser un numero entre 1 y {}".format(str(No))
    v1 = codifica(f + 1, c + 1, Nf, Nc)
    v2 = codifica(v1, o + 1, Nf * Nc, No)
    return v2

def decodifica3(x, Nf, Nc, No):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    v1, o = decodifica(x, Nf * Nc, No)
    f, c = decodifica(v1, Nf, Nc)
    return f-1, c-1, o-1

def deco_dict3(I:dict,Ncuadros:int,Ncolores:int,Nturnos:int):
    keys = I.keys()
    deco_list = []
    for i in keys:
        print("This I: {}".format(i))
        cud,col,tur = decodifica3(ord(i)- 255,Ncuadros+1+255,Ncolores+1+255,Nturnos+1+255)
        lis = [tur,cud,col,I[i]]
        # str = "{}-{}-{}-{}".format(tur,cud,col,I[i])
        deco_list.append(lis)
    return deco_list

def lis_to_col(lis:list,Nturnos:int,Ncuadros:int,Ncolores:int):
    color_list = []
    for k in range(0,Nturnos+1):
        temp = []
        for i in range(0,Ncuadros):
            temp.append([])
        color_list.append(temp)
    print("Size: {}".format(color_list))
    print("Size: {}".format(len(color_list[0])))
    print("{}".format(color_list[0]))

    for l in lis:
        t = int(l[0])
        s = int(l[1])
        c = int(l[2])
        vi = int(l[3])

        print("({},{},{})".format(t,s,c))
        if (t <= Nturnos and t >= 0):
            if (s <= Ncuadros and s >= 0):
                if (c <= Ncolores and c >= 0):
                    if (vi == 1):
                        color_list[t-1][s-1] = c
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

    return color_list
