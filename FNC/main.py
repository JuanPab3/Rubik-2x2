
import FNC as fn
letrasProposicionalesA = ['p', 'q', 'r', 's', 't']
# # Formula a la cual encontrar su forma clausal
# formula = "-p"
# formula = "(pYq)"
# formula = "(pOq)"
# formula = "(((-pOq)O(p>-q))>-((p>(rY(sO-t)))>-q))"
# formula = "(((-pOq)O(p>-q))>-((q>(rY(sO-t)))>-p))"
formula = "((p>(rY(sO-t)))>-q)"

# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
fFNC = fn.Tseitin(formula, letrasProposicionalesA)

# Se obtiene la forma clausal como lista de listas de literales
fClaus = fn.formaClausal(fFNC)

a = "[['M'],['-A','-p'],['A','p'],['-A','B'],['-q','B'],['A','q','-B'],['-C','-q'],['C','q'],['p','D'],['-C','D'],['-p','C','-D'],['-B','E'],['-D','E'],['B','D','-E'],['-F','-t'],['F','t'],['-s','G'],['-F','G'],['s','F','-G'],['r','-H'],['G','-H'],['-r','-G','H'],['p','I'],['-H','I'],['-q','H','-I'],['-J','-p'],['J','p'],['I','K'],['-J','K'],['-I','J','-K'],['-L','-K'],['L','K'],['E','M'],['-L','M'],['-E','L','-M']]"
b = "[['M'],['-A','-p'],['A','p'],['-A','B'],['-q','B'],['A','q','-B'],['-C','-q'],['C','q'],['p','D'],['-C','D'],['-p','C','-D'],['-B','E'],['-D','E'],['B','D','-E'],['-F','-t'],['F','t'],['-s','G'],['-F','G'],['s','F','-G'],['r','-H'],['G','-H'],['-r','-G','H'],['q','I'],['-H','I'],['-q','H','-I'],['-J','-p'],['J','p'],['I','K'],['-J','K'],['-I','J','-K'],['-L','-K'],['L','K'],['E','M'],['-L','M'],['-E','L','-M']]"
c = "{}".format(fClaus)
# Imprime el resultado en consola
# print(fClaus)
print(a)
print(b)
print(c)
