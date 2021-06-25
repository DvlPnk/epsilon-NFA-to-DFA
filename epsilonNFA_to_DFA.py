###PROGRAMA: Conversión de un AFND-epsilon a AFD

def clausura(estado):
    conjunto = []
    for i in range(len(estado)):
        conjunto += [estado[i]]
    for i in range(0, n):
        for j in range(len(estado)):
            if (datos[i][0] == estado[j] and datos[i][1] == 'e'):
                conjunto += [datos[i][2]]
    conjunto = list(dict.fromkeys(conjunto))
    return conjunto


# Delta
def delta(estado, simbolo):
    conjunto = []
    for i in range(0, n):
        if (datos[i][0] == estado and datos[i][1] == simbolo):
            conjunto += [datos[i][2]]
    conjunto = list(dict.fromkeys(conjunto))
    return conjunto


def deltaAFD(estado, simbolo):
    qsiguiente = []
    n = len(Dtran)
    for i in range(n):
        if (Dtran[i][0] == estado and Dtran[i][1] == simbolo):
            qsiguiente = Dtran[i][2]
            return qsiguiente


def deltasombrero(estadoi, cadena):
    n = len(cadena)
    print("Ruta que sigue la cadena: ", cadena)
    print("Estado inicial: ", estadoi)
    base = clausura(estadoi)
    print("Paso 0: ", base)
    for i in range(n):
        deltapaso = []
        for k in range(len(base)):
            deltapaso += delta(base[k], cadena[i])
            deltapaso = list(dict.fromkeys(deltapaso))
        base = clausura(deltapaso)
        print("Paso ", i + 1, ": ", base)
    return base


def evaluarCadenaAFD(q0, cadena):
    q = q0
    print("Ruta que sigue la cadena: ", cadena)
    print("Estado inicial: ", q0)
    for i in range(len(cadena)):
        q = deltaAFD(q, cadena[i])
        print("Paso ", i + 1, ": ", q)
    return q


def estadosAceptacionAFD(estados, aceptacion):
    aceptacionD = []
    for j in range(len(aceptacion)):
        for k in range(len(estados)):
            for z in range(len(estados[k])):
                if aceptacion[j] == estados[k][z]:
                    if len(aceptacionD) == 0:
                        aceptacionD += [estados[k]]
                    else:
                        bandera = True
                        p = 0
                        for p in range(len(aceptacionD)):
                            if (aceptacionD[p] == estados[k]):
                                bandera = False
                        if (bandera):
                            aceptacionD += [estados[k]]
    return aceptacionD

print("PROGRAMA: Conversión de un AFND-epsilon a AFD\n")
print("===================================================================")
print("INGRESO DE DATOS")
s = int(input("Ingrese la cantidad de estados: "))
estados2=[]
for i in range(s):
    estados2+=input("Ingrese el estado " + str(i + 1) + ": ")
entrada = input("Ingrese el estado de entrada: ")
aceptacion = input("Ingrese los estados de aceptación: ")
aceptacion = aceptacion.split(" ")
p = int(input("Ingrese la cantidad de simbolos: "))
simbolo = []
for i in range(p):
    simbolo += [input("Ingrese el simbolo #" + str(i + 1) + ": ")]
print("Simbolos ingresados: ")
print(simbolo)
i = 0
datos = []
tran = []

print("--------------------------------------------------------")
n = int(input("Ingrese la cantidad de transiciones: "))
print("Ingrese las transiciones con el siguiente formato: \n Estado_Entrada Simbolo Estado_Salida\n -> En el caso de epsilon, escribir e en el simbolo")
while (i < n):
    tran = input("Ingrese la transicion #" + str(i + 1) + ": ")
    tran = tran.split(" ")
    datos.append(tran)
    i += 1
print("Tabla de transiciones AFND-e")
simboloepsilon=simbolo.copy()
simboloepsilon+='e'
for i in range(len(simboloepsilon)):
    print("\t",simboloepsilon[i],end="\t")
print()
for i in range(len(estados2)):
    print(estados2[i],end= "\t")
    for j in range(len(simboloepsilon)):
        print(delta(estados2[i],simboloepsilon[j]),end="\t\t")
    print()


q0 = []
q0 = clausura([entrada])
q0.sort()
estados = [q0]
cont = 0
contq = 0
k = 0
q1 = []
Dtran = []
print("===================================================================")
print("###PROCEDIMIENTO###")
while (True):
    print("--------------------------------------------------------")
    for i in range(len(simbolo)):
        flag = 1
        del_U = []
        print("\nEstado q",contq," es: ", estados[k])
        print("Con el simbolo: ", simbolo[i])
        for j in range(len(estados[k])):
            del_U += delta(estados[k][j], simbolo[i])
            del_U = list(dict.fromkeys(del_U))
        q1 = clausura(del_U)
        q1.sort()
        print("Del_U es:")
        print(del_U)
        print("Q es: ")
        print(q1)
        Dtran += [[estados[k], simbolo[i], q1]]
        for j in range(len(estados)):
            if (estados[j] == q1):
                flag = 0
        if (flag == 1):
            estados += [q1]
            cont += 1
    k += 1
    contq += 1
    print("--------------------------------------------------------")
    if k > cont:
        break;
print("\nEstados: ")
for i in range(len(estados)):
    print("q",i,": ",estados[i])
print("\nEl Dtran AFD es: ")
contq2 = 0
cont2 = 0
for i in range (len(simbolo)):
    print("\t",simbolo[i], end= "\t")
print()
while(cont2 < (len(estados)*len(simbolo))):
    print("q",contq2,": ",end="\t")
    while(cont2 < (len(simbolo)*(contq2+1))):
        print(Dtran[cont2][2],end="\t")
        cont2 += 1
    print()
    contq2 += 1


# Evaluación de la cadena w en AFND-e
print("\n===================================================================")
print("EVALUAMOS UNA CADENA EN AFND-e: ")
print("-> Ingrese una cadena con los símbolos del alfabeto. Formato: aba ")
print("-> Para finalizar, pulsar Enter sin ingresar una cadena ")
while True:
    print("-------------------------------------------------------------------")
    w = input("Cadena: ")
    if w == "":
        break
    conjuntoCadena = deltasombrero([entrada], w)
    conjuntoCadena = set(conjuntoCadena)
    conjuntoAceptacion = set(aceptacion)
    interserccion = conjuntoAceptacion.intersection(conjuntoCadena)
    print("\nEl conjunto de estados de la cadena es: ", conjuntoCadena)
    print("El conjunto de estados de aceptacion es : ", conjuntoAceptacion)
    print("La interseccion de la cadena con los estados de aceptación es: ", interserccion)
    if interserccion != set():
        print("El AFND-e acepta la cadena w: ", w)
    else:
        print("El AFND-e NO acepta la cadena w: ", w)
# Evaluación de la cadena w en AFD
aceptacionAFD = estadosAceptacionAFD(estados, aceptacion)  # Conjunto de estados de acpetacion en AFD
inicial = q0
print("\n===================================================================")
print("EVALUAMOS UNA CADENA EN AFD")
print("-> Ingrese una cadena con los símbolos del alfabeto. Formato: aba ")
print("-> Para finalizar, pulsar Enter sin ingresar una cadena ")
while True:
    print("-------------------------------------------------------------------")
    w = input("Cadena: ")
    if w == "":
        break
    qresultante = evaluarCadenaAFD(inicial, w)
    print("El estado resultante es: ", qresultante)
    print("Los estados de aceptación son: ", aceptacionAFD)
    bandera2 = True
    for i in range(len(aceptacionAFD)):
        if qresultante == aceptacionAFD[i]:
            print("El AFD acepta la cadena w: ", w)
            bandera2 = False
            break
    if bandera2:
        print("El AFD NO acepta la cadena w: ", w)
        
print("FIN DEL PROGRAMA")

