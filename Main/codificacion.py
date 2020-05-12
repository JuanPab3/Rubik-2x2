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