def clausura(estado):
    conjunto = []
    for i in range (len(estado)):
        conjunto += [estado[i]]
    for i in range (0, n):
        for j in range (len(estado)):
            if(datos[i][0] == estado[j] and datos[i][1]=='e'):
                conjunto+=[datos[i][2]]
    conjunto = list(dict.fromkeys(conjunto))
    return conjunto
#Delta
def delta(estado, simbolo):
    conjunto = []
    for i in range (0, n):
        if(datos[i][0] == estado and datos[i][1]==simbolo):
            conjunto+=[datos[i][2]]
    conjunto = list(dict.fromkeys(conjunto))
    return conjunto
n=int(input("Ingrese la cantidad de transiciones: "))
s=int(input("Ingrese la cantidad de estados: "))
entrada = input("Ingrese el estado de entrada: ")
p=int(input("Ingrese la cantidad de simbolos: "))

simbolo = []
for i in range (p):
    simbolo += [input("Ingrese el simbolo #" + str(i+1) + ": " )]
print(simbolo)
i=0
datos=[]
tran=[]
print("Ingrese las trancisiones con el siguiente formato: \nEstado_Entrada Simbolo Estado_Salida\nEn el caso de epsilon, escribir e en el simbolo")
while(i<n):
    tran = input("Ingrese la transicion #" + str(i+1) + ": ")
    tran = tran.split(" ")
    datos.append(tran)
    i+=1
q0 = []
q0 = clausura([entrada])
estados = [q0]
cont = 0
k=0
q1 = []
Dtran = []
print("###~Procedimiento~###")
while(True):
    for i in range (len(simbolo)):
        flag = 1
        del_U=[]
        print("\nEstado: ")
        print(estados[k])
        print("Con el simbolo: ")
        print(simbolo[i])
        for j in range (len(estados[k])):
            del_U+=delta(estados[k][j], simbolo[i])
            del_U = list(dict.fromkeys(del_U))
        q1 = clausura(del_U)
        print("Del_U es:")
        print (del_U)
        print("Q es: ")
        print(q1)
        Dtran += [[estados[k], simbolo[i], q1]]
        for j in range (len(estados)):
            if(estados[j] == q1):
                flag=0
        if(flag==1):
            estados+=[q1]
            cont+=1
    k+=1
    if k>cont:
        break;
print("\nEstados: ")
print(estados)
print("El Dtran es: ")
print(Dtran)
