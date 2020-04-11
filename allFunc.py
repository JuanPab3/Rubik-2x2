""" Binary tree """
class BinaryTree:
    def __init__ (self, left, right):
        self.left = left
        self.right = right

## Binary tree functions

# Number of arists
def numAristas(btree):
    if btree.right == None:
        return 0
    else:
        return 2 + numAristas(btree.left) + numAristas(btree.right)

# High
def altura(btree):
    if btree.right == None:
        return 0
    else:
        return 1 + max(altura(btree.left) , altura(btree.right))

# Number of nodes
def numNodos(btree):
    if btree.right == None:
        return 1
    else:
        return 1 + numNodos(btree.left) + numNodos(btree.right)

""" Forms. Tree """
class Tree:
    def __init__(self, label, left, right):
        self.binaryConectives = ["Y", "O", ">", "="]
        self.label = label
        self.left = left
        self.right = right

## Forms. Tree functions

# negate a form.
def neg(t):
    return Tree("-", None, t)

# Number of atoms
def Atomos(t):
    if t.right == None:
        return {t.label}
    elif t.label == "-":
        return Atomos(t.right)
    elif t.label in t.binaryConectives:
        return Atomos(t.left).union(Atomos(t.right))

# subforms
def subforms(t):
    if t.right == None:
        return [t]
    elif t.label == "-":
        return [t] + subforms[t.right]
    elif t.label in t.binaryConectives:
        return [t] + subforms[t.left] + subforms[t.right]

# Substitution
def sust(b, a, ap):
    # ap = a'
    if a not in subforms(b):
        return b
    elif subforms(b) == subforms(a):
        return ap
    elif b.label == "-":
        return Tree("-", None, sust(b.right, a, ap))
    elif b.label in b. binaryConectives:
        return Tree(b.label, sust(b.left, a, ap), sust(b.right, a, ap))

# Conectives ocurrence
def numConect(t):
    if a.right == None:
        return 0
    elif a.label == "-":
        return 1 + numConect(t.right)
    elif a.label in a.binaryConectives:
        return 1 + numConect(t.left) + numConect(t.right)

# write a tree
def inorder(t):
    if t.right == None:
        return t.label
    elif t.label == "-":
        return t.label + inorder(t.right)
    elif t.label in t.binaryConectives:
        return "(" + inorder(t.left) + t.label + inorder(t.right) + ")"

# Ocurrence of propositional letters
def P(t):
    if t.right == None:
        return 1
    elif t.label == "-":
        return P(t.right)
    elif t.label in t.binaryConectives:
        return P(t.left) + P(t.right)

# Ocurrence of binary conectives
def C(t):
    if t.right == None:
        return 0
    elif t.label == "-":
        return C(t.right)
    elif t.label in t.binaryConectives:
        return 1 + C(t.left) + C(t.right)

# Value of an interpretation i in a form. t
def VI(t, i):
    if t.right == None:
        return i[t.label]
    elif t.label == "-":
        return 1 - VI(t.right, i)
    elif t.label == "Y":
        return VI(t.left, i) * VI(t.right, i)
    elif t.label == "O":
        return max(VI(t.left, i), VI(t.right, i))
    elif t.label == ">":
        return max(1 - VI(t.left, i), VI(t.right, i)) # p -> q = -p v q
    elif t.label == "=":
        return 1 - (VI(t.left, i) - VI(t.right, i))**2

# Returns a list of all the interpretations with the n propositional letters in Letters
def allInterps(letters):
    interps = []
    aux = {}

    for a in letters:
        aux[a] = 1

    interps.append(aux)

    for a in letters:
        interps_aux = [n for n in interps]

        for i in interps_aux:
            aux1 = {}

            for b in letters:
                if a == b:
                    aux1[b] = 1 - i[b]
                else:
                    aux1[b] = i[b]

            interps.append(aux1)

    return interps

# Get all the valid interpretations
def modInterps(t):
    # Get the letters
    letters = Atomos(t)
    interps = allInterps(letters)
    validInterps = []

    for i in interps:
        if VI(t,i) == 1:
            validInterps.append(i)

    return validInterps

# Check if a form. t is valid
def checkValid(t):
    letters = Atomos(t)
    if modInterps(t) == allInterps(letters):
        return True
    else:
        return False

# Check if a form. t is unsatisfactory
def checkUnsatisf(t):
    letters = Atomos(t)
    if modInterps(t) == []:
        return True
    else:
        return False
