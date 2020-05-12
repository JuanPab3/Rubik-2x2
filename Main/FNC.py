
def enFNC(A):
    assert(len(A)==5 or len(A)==8), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    if "-" in A:
        q = A[-1]
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[4]
        r = A[6]
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[4]
        r = A[6]
        B = "-"+q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[4]
        r = A[6]
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')
    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256+100000,256+100000*2)]
    # letrasProposicionalesB = ['A', 'B', 'C', 'D', 'E', 'F']
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    assert("Y" not in letrasProposicionalesA),"existe una Y en Letras A"
    assert("Y" not in letrasProposicionalesB),"existe una Y en Letras B"
    L=[]
    Pila=[]
    I=-1
    s=A[0]

    while len(A)>0:
        if (s in letrasProposicionalesA or s in letrasProposicionalesB) and len(Pila)!=0 and Pila[-1]=='-': #Si s es un átomo y Pila no vacía y Pila[-1] = ’¬’
            I+=1
            Atomo = letrasProposicionalesB[I]
            Pila=Pila[0:-1]
            Pila.append(Atomo)
            L.append("{}==-{}".format(Atomo,s))
            A=A[1:]
            if len(A)>0:
                s=A[0]
        elif s==")":
            w=Pila[-1]
            u=Pila[-2]
            v=Pila[-3]
            print("esta es W",w,"esta es V",v)
            assert((w!="Y") and(v!="Y")),"se encontró una Y"
            Pila=Pila[:len(Pila)-4]
            I+=1
            Atomo=letrasProposicionalesB[I]
            L.append("{}==({}{}{})".format(Atomo,v,u,w))

            s= Atomo
        else:
            Pila.append(s)
            A=A[1:]
            if len(A)>0:
                s=A[0]
    B=""
    if I<0:
        Atomo=Pila[-1]
    else:
        Atomo=letrasProposicionalesB[I]

    for x in L:
        y=enFNC(x)
        print("this ",y, "and X:", x)
        B+="Y"+y

    B = Atomo+B
    return B

def Clausula(C):
    L=[]
    while len(C)>0:
        s=C[0]
        if s=="-":
#            print(s,"  ", C)
            L.append(s+C[1])
            C=C[3:]
        else:
            L.append(s)
            C=C[2:]
    return L

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC y sin paréntesis
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    L=[]
    i=0
    while len(A)>0:
        if i>=len(A):
            L.append(Clausula(A))
            A=[]
        else:
            if A[i]=="Y":
#                print(A)
                L.append(Clausula(A[:i]))
                A=A[i+1:]
                i=0
            else:
                i+=1
    return L
