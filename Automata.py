import sys
import msvcrt
#Datos de almacenamiento
lista_identificadores=[]
lista_numerosEnteros=[]
lista_numerosReales=[]
lista_relaciones=[]
lista_operadores=[]
lista_coherencia=[]
contador=0
#Declaracion de variables
i=0
estado=0
with open(r'C:\Users\Intel\Desktop\Compiladores\prueba.py', 'r') as archivo:
    contenido = archivo.read()
entrada = ''.join(contenido.splitlines())
entrada=entrada.replace(" ","")
entrada=entrada+'#'
lista_tokens=[]
#Switch de palabras reservadas
def case0():
    global i, estado, contador,lista_relaciones, lista_operadores
    if entrada[i:i+6]=="inicio":
        estado=1
        i+=5
    elif entrada[i:i+7]=="declara":
        estado=2
        i+=6
    elif entrada[i:i+4]=="leer":
        estado=3
        i+=3
    elif entrada[i:i+7]=="mostrar":
        estado=4
        i+=6
    elif entrada[i:i+2]=="si" and not entrada[i+2].isalpha():
        estado=5
        i+=1 
    elif entrada[i:i+4]=="sino":
        estado=6
        i+=3 
    elif entrada[i:i+5]=="final":
        estado=7
        i+=4    
    elif entrada[i:i+4]=="real":
        estado=21
        i+=3
    elif entrada[i:i+6]=="entero":
        estado=22
        i+=5
    elif entrada[i:i+8]=="caracter":
        estado=23
        i+=7
    elif entrada[i].isalpha():
        estado=8
        contador=contador+1
    elif entrada[i].isdigit(): 
        estado=9
        contador=contador+1
    elif entrada[i]=='(':
        estado=15
    elif entrada[i]==')':
        estado=16
    elif entrada[i]==':':
        estado=17
    elif entrada[i]==';':
        estado=18
    elif entrada[i]=='<' or entrada[i]=='>' or entrada[i]=='=':
        estado=19
        lista_relaciones.append(entrada[i])
    elif entrada[i]=='+' or entrada[i]=='-' or entrada[i]=='/' or entrada[i]=='*':
        estado=20
        lista_operadores.append(entrada[i])
    elif entrada[i]==',':
        estado=24
    elif entrada[i]=='?':
        estado=25
    else:
        estado=10
    i=i+1
    return estado
def case1():
    return 1000
def case2():
    return 1100
def case3():
    return 1200
def case4():
    return 1300
def case5():
    return 1400
def case6():
    return 1500
def case7():
    return 1900
def case8():
    global i, estado, contador, lista_identificadores
    if entrada[i].isdigit() or entrada[i].isalpha():
        estado=8
        contador=contador+1
    else:
        estado=11
        lista_identificadores.append(entrada[i-contador:i])
        i=i-1
    i=i+1
    return estado
def case9():
    global i, estado, contador, lista_numerosEnteros
    if entrada[i].isdigit():
        estado=9
        contador=contador+1
    elif entrada[i]=='.':
        estado=12
        contador=contador+1
    else:
        estado=13
        numeroEntero=int(entrada[i-contador:i])
        lista_numerosEnteros.append(numeroEntero)
        i=i-1
    i=i+1
    return estado
def case10():
    print("Error se esperaba una palabra reservada, caracter reservado, numero o identificador")
    msvcrt.getch()
    return sys.exit()
def case11():
    return 1800
def case12():
    global i, estado, contador, lista_numerosReales
    if entrada[i].isdigit():
        estado=12
        contador=contador+1
    else:
        estado=14
        numeroReal=float(entrada[i-contador:i])
        lista_numerosReales.append(numeroReal)
        i=i-1
    i=i+1
    return estado
def case13():
    return 1700
def case14():
    return 1600
def case15():
    return 2200
def case16():
    return 2300
def case17():
    return 2000
def case18():
    return 2100
def case19():
    return 2500
def case20():
    return 2600
def case21():
    return 2700
def case22():
    return 2800
def case23():
    return 2900
def case24():
    return 3000
def case25():
    return 2400
def switch_case(i):
    switch_dict={
        0: case0,
        1: case1,
        2: case2,
        3: case3,
        4: case4,
        5: case5,
        6: case6,
        7: case7,
        8: case8,
        9: case9,
        10: case10,
        11: case11,
        12: case12,
        13: case13,
        14: case14,
        15: case15,
        16: case16,
        17: case17,
        18: case18,
        19: case19,
        20: case20,
        21: case21,
        22: case22,
        23: case23,
        24: case24,
        25: case25,
    }
    return switch_dict.get(i)()
#Lector de entrada y devolucion de tokens
while i!=len(entrada)-1:
    estado=0
    contador=0
    while True:
        proceso = switch_case(estado)
        if proceso in {1, 2, 3, 4, 5, 6, 7, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}:
            break
    resultado = switch_case(estado)
    lista_tokens.append(resultado)
print(lista_tokens)
#Analizador sintactico
pasos=0
es=0
#Identificador
def identificador():
    global pasos, es
    if lista_tokens[pasos]==2100:
        return pasos
    if lista_tokens[pasos]==3000:
        pasos=pasos+1
    else:
        print("error se esperaba una coma")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos]==1800:
        pasos=pasos+1
    else:
        print("error se esperaba un identificador")
        msvcrt.getch()
        return sys.exit()
    identificador()
#Expresion
def expresion():
    global pasos, es
    if lista_tokens[pasos]==2200:
        pasos=pasos+1
    else:
        print("error se esperaba un parentesis")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos] in {1800, 1700, 1600}:
        pasos=pasos+1
    else:
        print("error se esperaba una variable")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos]==2600:
        pasos=pasos+1
        if lista_tokens[pasos] in {1800, 1700, 1600}:
            pasos=pasos+1
        else:
            print("error se esperaba una variable")
            msvcrt.getch()
            return sys.exit()
    if lista_tokens[pasos]==2300:
        pasos=pasos+1
    else:
        print("error se esperaba un parentesis")
        msvcrt.getch()
        return sys.exit()    
    if lista_tokens[pasos]==2600:
        pasos=pasos+1
        expresion()
    if lista_tokens[pasos]==2100:
        return pasos
    else:
        print("error se esperaba ';' ")
        msvcrt.getch()
        return sys.exit()
#Accion
def cas0():
    global pasos, es
    if lista_tokens[pasos]==1100:
        es=1
    elif lista_tokens[pasos]==1200:
        es=2
    elif lista_tokens[pasos]==1800:
        es=3
    elif lista_tokens[pasos]==1300:
        es=4
    elif lista_tokens[pasos]==1400:
        es=5
    else:
        print("error se esperaba declaración, lectura, operación, escritura, condición> ")
        msvcrt.getch()
        return sys.exit()
    pasos = pasos + 1
    return es
#declaracion
def cas1():
    global pasos, es,lista_coherencia
    if lista_tokens[pasos] in {2700, 2800, 2900}:
        pasos = pasos + 1
    else:
        print("error se esperaba que fuera real, entero o caracter")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos]==2000:
        pasos = pasos + 1
    else:
        print("error se esperaba ':' ")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos]==1800:
        pasos=pasos+1
    else:
        print("error se esperaba un identificador")
        msvcrt.getch()
        return sys.exit()
    identificador()
    if lista_tokens[pasos]==2100:
        pasos = pasos + 1
        es=21
    else:
        print("error se esperaba ';' ")
        msvcrt.getch()
        return sys.exit()
    lista_coherencia.append(1)
    return es
#lectura
def cas2():
    global pasos,es,lista_coherencia
    if lista_tokens[pasos]==1800:
        pasos=pasos+1
    else:
        print("error se esperaba un identificador")
        msvcrt.getch()
        return sys.exit()
    identificador()
    if lista_tokens[pasos]==2100:
        pasos = pasos + 1
        es=22
    else:
        print("error se esperaba ';' ")
        msvcrt.getch()
        return sys.exit()
    lista_coherencia.append(2)
    return es
#operacion
def cas3():
    global pasos,es,lista_coherencia
    if lista_tokens[pasos]==2500:
        pasos=pasos+1
    else:
        print("error se esperaba una relacion")
        msvcrt.getch()
        return sys.exit()
    expresion()
    if lista_tokens[pasos]==2100:
        pasos = pasos + 1
        es=23
    else:
        print("error se esperaba ';' ")
        msvcrt.getch()
        return sys.exit()
    lista_coherencia.append(3)
    return es
#escritura
def cas4():
    global pasos,es,lista_coherencia
    if lista_tokens[pasos]==1800:
        pasos=pasos+1
    elif lista_tokens[pasos]==2400:
        pasos=pasos+1
    else:
        print("error se esperaba un identificador o un valor vacio ")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos]==2100:
        pasos = pasos + 1
        es=24
    else:
        print("error se esperaba ';' ")
        msvcrt.getch()
        return sys.exit()
    lista_coherencia.append(5)
    return es
#condicion
def cas5():
    global pasos,es,lista_coherencia
    lista_coherencia.append(4)
    if lista_tokens[pasos]==2200:
        pasos=pasos+1
    else:
        print("error se esperaba parentesis")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos] in {1600, 1700, 1800}:
        pasos = pasos + 1
    else:
        print("error se esperaba que fuera real, entero o caracter")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos]==2500:
        pasos=pasos+1
    else:
        print("error se esperaba que fuera una relacion")
        msvcrt.getch()
        return sys.exit()    
    if lista_tokens[pasos] in {1600, 1700, 1800}:
        pasos = pasos + 1
    else:
        print("error se esperaba que fuera real, entero o caracter")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos]==2300:
        pasos=pasos+1
        es=0
        while(True):
            acto=switch_cas(es)
            if acto in {21, 22, 23, 24, 25}:
                break
    else:
        print("error se esperaba parentesis")
        msvcrt.getch()
        return sys.exit()
    if lista_tokens[pasos]==1500:
        pasos=pasos+1
        es=0
        while(True):
            acto=switch_cas(es)
            if acto in {21, 22, 23, 24, 25}:
                break
    else:
        print("error se esperaba un sino")
        msvcrt.getch()
        return sys.exit()  
    pasos = pasos - 1  
    if lista_tokens[pasos]==2100:
        pasos = pasos + 1
        es=25
    else:
        print("error se esperaba ';' ")
        msvcrt.getch()
        return sys.exit()
    return es
def cas21():
    global es
    return es
def cas22():
    global es
    return es
def cas23():
    global es
    return es
def cas24():
    global es
    return es
def cas25():
    global es
    return es
def switch_cas(pasos):
    switch_dic={
        0: cas0,
        1: cas1,
        2: cas2,
        3: cas3,
        4: cas4,
        5: cas5,
        21: cas21,
        22: cas22,
        23: cas23,
        24: cas24,
        25: cas25,
    }
    return switch_dic.get(pasos)()
def cuerpo():
    global es
    while(pasos!=len(lista_tokens)-1):
        es=0
        while(True):
            acto=switch_cas(es)
            if acto in {21, 22, 23, 24, 25}:
                break
    if lista_tokens[pasos]!=1900:
        cuerpo()
def programa():
    global pasos, es
    if lista_tokens[pasos]==1000:
        pasos = pasos + 1
        if(lista_tokens[-1]==1900):
            cuerpo()
            print("Todo esta bien declarado")
        else:
            print("error se esperaba que diera fin al programa")
            msvcrt.getch()
            return sys.exit()
    else:
        print("error se esperaba que iniciara el programa")
        msvcrt.getch()
        return sys.exit()
programa()

#Analizador semantico
def coherencia():
    global lista_coherencia
    a=0
    error=0
    len(lista_coherencia)
    while a!=len(lista_coherencia)-1:
        if(lista_coherencia[a]>lista_coherencia[a+1]):
            error=1    
        a=a+1
    if error==1:
        print("El orden de las acciones esta mal")
        msvcrt.getch()
        return sys.exit()
    else:
        print("El orden de las acciones esta bien establecido")
coherencia()

print(lista_identificadores)
print(lista_relaciones)
print(lista_operadores)
print(lista_numerosEnteros)
print(lista_numerosReales)
print(lista_coherencia)