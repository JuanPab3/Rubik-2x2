#================================ASPECTOS_TECNICOS==============================
from codificacion import deco_dict3
from dpll import dpll
from Reglas import *
import FNC as fn
#====================================CODIGO=====================================


#reglas = [basic_0(),regla1(),regla2(),regla3(),regla4(),regla5(),regla6(),regla7(),regla8(),regla9(),regla10(),regla11(),regla12(),regla13(),regla14(),regla15(),regla16(Nturnos),regla17()]
#"({}Y{})".format(#regla2(),basic_0())
formula  = "({}Y{})".format(regla2(1),basic_1())
#formula = regla2()
#formula  = basic_1()

formula = formula.replace("(","")
formula = formula.replace(")","")
# print(formula)

# print("inicio a Tseiting")
# fFNC = fn.Tseitin(formula, lC)

# formula_de_la_muere  = "((((((((((((((((({0}Y{1})Y{2})Y{3})Y{4})Y{5})Y{6})Y{7})Y{8})Y{9})Y{10})Y{11})Y{12})Y{13})Y{14})Y{15})Y{16})Y{17})".format(reglas[0],reglas[1],reglas[2],reglas[3],reglas[4],reglas[5],reglas[6],reglas[7],reglas[8],reglas[9],reglas[10],reglas[11],reglas[12],reglas[13],reglas[14],reglas[15],reglas[16],reglas[17])
# fFNC = fn.Tseitin(formula_de_la_muere, lC)

# print(len(fFNC))
#print(fFNC)

# Se obtiene la forma clausal como lista de listas de literales
# print("inicio a Clausal")
fClaus = fn.formaClausal(formula)
# print(fClaus)

#print(len(fClaus))
# print(regla2())
#

test = {}
print("inicio a DPLL")
test = dpll(fClaus,test)

sat, dic = test

# print(test)

final = deco_dict3(dic,Ncuadros,Ncolores,Nturnos)


sorted(final, key=itemgetter(2))


# print	(final)
with open("satisfacible.txt", "w") as f:
    for i in final:
        if (i[3] == 1):
            f.write("{} {} {}\n".format(i[0],i[1],i[2]))

file_list = []
with open("satisfacible.txt","r") as f:
    for line in f:
        file_list.extend([line.split()])

for l in file_list:
    # l[0] = "T{}".format(l[0])
    # l[1] = "S{}".format(l[1])
    # l[2] = "C{}".format(l[2])
    l[0] = int(l[0])
    l[1] = int(l[1])
    l[2] = int(l[2])

RUBIC(file_list,Ncuadros,Ncolores,Nturnos)
