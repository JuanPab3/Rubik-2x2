# import Davis Putnam algorithm and functions
import copy

# return de complement of a literal
def complement(l):
    if "-" in l:
        lc = l[1]
    else:
        lc = "-" + l
    return lc

# return a list with all literals in the formula S
def getLits(S):
    lits = []
    for C in S:
        for l in C:

            if "-" in l:
                li = l[1]
            else:
                li = l
            if li not in lits:
                lits.append(li)
    return lits

# return C if C is an unit clause in the formula S, None otherwise
def hasUnit(S):
    lits = getLits(S)
    for l in lits:
        if [l] in S:
            return l
    return None

# if lit is a pure literal, remove the clause C in the formula S if lit is in C
def removeLit(S, lit):
    # if lit == None, S has not pure literal
    if lit == None:
        return S
    Saux = copy.deepcopy(S)
    for C in S:
        # print("C:", C)
        if lit in C:
            Saux.remove(C)
    return Saux

# if lit in C, remove C in S. Remove lit complement of all C in S
# if lit == None, lit will be an unit clause
def unitPropagation(S, lit = None):
    if lit == None:
        unit = hasUnit(S)
        # if S has not unit clauses, unitPropagation of S is S
        if unit == None:
            return S
    else:
        unit = lit
    #Saux = S.copy()
    Saux = copy.deepcopy(S)
    # print("Saux: ", Saux)
    Saux = removeLit(Saux, unit)
    # print("Saux: ", Saux)
    unitc = complement(unit)
    for C in Saux:
        if unitc in C:
            C.remove(unitc)
    return Saux

# add I[l] = 1 if l = p, or I[l] = 0 if l = -p
def addInterp(I, l):
    assert("" != l), u"error!"
    Iaux = copy.deepcopy(I)
    if "-" in l:
        Iaux[l[1]] = 0
    else:
        Iaux[l] = 1
    return Iaux

# subrutine unitPropagate
def unitPropagate(S, I):
    Saux = copy.deepcopy(S)
    Iaux = copy.deepcopy(I)
    unit = hasUnit(Saux)
    while ([] not in Saux) and (unit != None):
        Saux = unitPropagation(Saux)
        Iaux = addInterp(Iaux, unit)
        unit = hasUnit(Saux)
    return Saux, Iaux

# recursive rutine DPLL
def dpll(S,I):
    #1
    Saux = copy.deepcopy(S)
    Saux, Iaux = unitPropagate(Saux, I)
    #2
    if [] in Saux:
        return "Insatisfacible", {}
    #3
    if [] == Saux:
        return "Satisfacible", Iaux
    #4
    literals = getLits(Saux)
    lit = None # used in #9
    for l in literals:
        if l not in I:
            lit = l
            break
    #5
    S1 = unitPropagation(Saux, lit) # S'
    #6
    I1 = addInterp(Iaux, lit) # I'
    #7
    recu= dpll(S1, I1)
    if recu[0] == "Satisfacible":
        return "Satisfacible", recu[1]
    #8
    else:
        #9
        litc = complement(lit) # lit from #4
        S2 = unitPropagation(S, litc) # S''
        # 10
        I2 = Iaux.copy() # I''
        if "-" in lit:
            I2[lit] = 1
        else:
            I2[lit] = 0
        # print("I: {}\nI': {}\nI'':{}\n".format(I, I1, I2))
        return dpll(S2, I2)

# ------------------------ tests ------------------ #

# unitPropagate (diaps)

# S = [["p"],["-p", "q"],["-q", "r", "s"],["u", "-s", "r"],["r", "t"],["p", "s", "-t"],["-r", "u"]]
# print(unitPropagate(S, {}) # [['r', 's'], ['u', '-s', 'r'], ['r', 't'], ['-r', 'u']], {'p': 1, 'q': 1}

# dpll

# steps 1, 2 and 3

# print(dpll([["p"],["-p", "q", "-r"],["q"]], {}))

# steps 4, 5 , 6, 7

# S = [["p"],["-p", "q"],["-q", "r", "s"]]
# print(dpll(S, {}))

# all algorithm

## diaps
## S = [['p', '-q', 'r'], ['-p', 'q', '-r'], ['-p', '-q', 'r'], ['-p', '-q', '-r']]
## print(dpll(S,{}))

## taller
#1
S1 = [['p','q','r'],['-p','-q','-r'],['-p','q','r'],['-q','r'],['q','-r']]
print(dpll(S1,{})) # check
#2
S2 = [['p','q','r','-s'],['p','t','s'],['-p','-q'],['p','r','-q','-q']]
print(dpll(S2,{})) # check
S3 = [['p','q','-r'],['r','s','t'],['t'],['p','s'],['q','-p']]
print(dpll(S3,{})) # check
S4 = [['p','-q'],['-p','-q'],['q','r'],['-q','-r'],['-p','-r'],['p','-r']]
print(dpll(S4,{})) # check
S5 = [['-s','p', 'r'],['-p','s','-r'],['-p','-s'],['-p','-r']]
print(dpll(S5,{})) # check
