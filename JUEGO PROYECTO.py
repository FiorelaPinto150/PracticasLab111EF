import numpy as np
#JUGADOR N°1------------------------------------------------------------------------------------------------------------------
print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("                           HUNDIR LA FLOTA")
print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("OOJOOOO")

print("NOTA:ES MUY IMPORTANTE COMPLETAR FILAS PRIMERO Y DESPUES COLUMNAS O UNA DE ESTAS SOLAMENTE EL NO HACER CASO DE ESTE ORDEN PROVOCARA ERRORES EN EL PROGRAMA ")
lista_de_listas =[[0,1,2,3,4,5,6,7,8,9,10],[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print("LAS COORDENADAS PRIMERO LLEVAN EL NUMERO DE FILA Y DESPUES EL DE COLUMNA COLOCAR EN ESTE ORDEN ")
lista_de_listas2 =[["1,1", "1,2", "1,3", "1,4", "1,5", "1,6", "1,7", "1,8", "1,9", "1,10"],["2,1", "2,2", "2,3", "2,4", "2,5", "2,6", "2,7", "2,8", "2,9", "2,10"],["3,1", "3,2", "3,3", "3,4", "3,5", "3,6", "3,7", "3,8", "3,9", "3,10"],["4,1", "4,2", "4,3", "4,4", "4,5", "4,6", "4,7", "4,8", "4,9", "4,10"],["5,1", "5,2", "2,3", "5,4", "5,5", "5,6", "5,7", "5,8", "5,9", "5,10"],["6,1", "6,2", "6,3", "6,4", "6,5", "6,6", "6,7", "6,8", "6,9", "6,10"],["7,1", "7,2", "7,3", "7,4", "7,5", "7,6", "7,7", "7,8", "7,9", "7,10"],["8,1", "8,2", "8,3", "8,4", "8,5", "8,6", "8,7", "8,8", "8,9", "8,10"],["9,1", "9,2", "9,3", "9,4", "9,5", "9,6", "9,7", "9,8", "9,9", "9,10"],["10,1", "10,2", "10,3", "10,4", "10,5", "10,6", "10,7", "10,8", "10,9", "10,10"]]
matriz_jugador1=np.array(lista_de_listas)
matriz2=matriz_jugador1
lista25=[[0,1,2,3,4,5,6,7,8,9,10],[1,1,1,1,1,1,0,2,2,2,2],[2,0,0,0,0,0,0,0,2,0,0],[3,0,3,3,3,0,0,0,2,0,0],[4,0,0,0,0,0,0,0,2,0,0],[5,0,4,0,3,3,3,0,0,0,0],[6,0,0,0,0,0,0,0,0,0,0],[7,0,0,0,4,0,3,3,3,0,0],[8,0,0,0,0,0,0,0,0,0,0],[9,0,0,0,4,0,0,0,0,0,0],[10,0,0,0,0,0,4,0,0,0,0]]
matriz_jugador2=np.array(lista25)
matrizAuxiliar=np.array(lista_de_listas2)
c=0
d=0
print("Posiciones de una matriz")
print(matrizAuxiliar)
print("Recuerde que puede seleccionar:\n1)1 Portaviones\n2)2 Buques\n2)3 Submarinos\n4)4 Lanchas")

pregunta=input("Ingrese primeramente a las filas con F (recuerde que ya no regresaras a filas si pasa esta opcion)\ningrese C para las columnas presione 000 para salir de filas y columnas :     ").lower()
#JUGADOR N°1
#while verifica variable pregunta

def jugador1_func(matriz1,matriz2):
    import numpy as np
    c1=np.equal(matriz1,matriz2)
    c=0
    for i in range(0,2):#fila
        for j in range(0,3):#columna
            dato=c1[i,j]
            if dato==True:
                c=c+1
    return c


def pregunta1(varia):
    if varia=="000"or varia==000:
        pregunta=input("Ingresa C para columnas saliste de las filas ya no podras regresar:").lower()
def pregunta2(varia2):
    if varia2==0000:
        resultado=jugador1_func(matriz_jugador1,matriz_jugador2)
        print("Estos son los puntos que acumulaste y el numero de veces que hundiste la flota del enemigo :)",resultado)


while pregunta=="f":
    flota1=int(input("Ingrese una de  las opciones del tipo de flota:"))#numeros que dependen del tipo de flota
    if flota1==000:
        pregunta1(flota1)
    #transformaremos las coordenadas en caracteres y despues una lista
    # coordenadas para filas
    text = input("Ingrese las coordenadas:")
    if text=="000" :
        pregunta1(text)
    listaCoordenadas = []
    indice = 0
    al = 2
    el = 5
    il = 8
    ol = 11
    ul = 14
    c_lista = 0
    c0 = 0
    def diez(listaCoordenadas):  # funcion para convertir las coordenadas de 10 en un entero sin alterar el resultado
        al = 2
        el = 5
        il = 8
        ol = 11
        ul = 14
        c_lista = 0
        clo = 1
        listaCoordenadas2 = []
        for x in range(0, len(listaCoordenadas)):
            if x == al or x == el or x == il or x == ol or x == ul:
                c_lista = c_lista + 1
                clo = c_lista * 2
                listaCoordenadas2.append(listaCoordenadas[x])
        ola = listaCoordenadas2[-1]
        if ola == 1:
            listaCoordenadas2.pop()
            listaCoordenadas2.insert(-1, 10)
            listaCoordenadas2.sort()
        for i in range(0, clo):
            if i % 2 == 0:
                listaCoordenadas2.insert(i, 10)
        return listaCoordenadas2
#CONVERTIR LAS COORDENADAS EN LISTA SIN CAMBIOS=>
    while indice < len(text):
        letra = text[indice]
        indice += 1
        if letra != "," and letra != " ":
            listaCoordenadas.append(letra)
            listaCoordenadas = list(map(int, listaCoordenadas))
        if letra == "0":
            c0 = 1
    if c0 == 1:
        listaCoordenadas = diez(listaCoordenadas)

    numero_fila=listaCoordenadas[0]#numero filaaaaaaaaaaaaaaaaaa
    #obtener la fila de la matriz
    listaposionfila=[]
    for f in range(len(listaCoordenadas)):
        if f%2!=0:
            listaposionfila.append(listaCoordenadas[f])
    cuenta=len(listaposionfila)
    cp=0
    cb=0
    cs=0
    cl=0
    f1=numero_fila
    fila=matriz_jugador1[f1]#sacamos fila de la matriz original
    lista=fila.tolist()#convertimos a lista
    if flota1==1 and cuenta==5:#variable flota sera aquel numero que indiique el tipo de flota y cuenta sera el tamaño de nuestra anterior matriz colun que nos dira cuantas coordenadas debemos llegar a tener si queremos ingresar a esa flota
        cp=cp+1
        if cp==1:
            for k in range(0,len(listaposionfila)):#nos guiaremos por el tamaño de colun para dar a "x" el valor de la posicion en donde debe reeplazar el "0" por uno de los numeros segun la condicion
                x=listaposionfila[k]
                y=1
                lista.pop(x)
                lista.insert(x,y)
            matriz_jugador1=np.delete(matriz_jugador1,f1,axis=0)#para no alterar cada la matriz eliminaremos la fila en la que debemos llenar con diferentes digitos
            matriz_jugador1=np.insert(matriz_jugador1,f1,lista,axis=0)#en este paso reemplazaremos la lista en la matriz quedando solo el cambio en el llenado de digitos
            #NOTA!!!!!!!!!!!!!!!!!!!!!!!!TIENE EL MISMO PROCEDIMIENTO CADA UNO DE LOS IFs
            print(matriz_jugador1)

    if flota1==2 and cuenta==4:
        cb=cb+1
        if cb<=2:
            for k in range(0,len(listaposionfila)):
                x=listaposionfila[k]
                y=2
                lista.pop(x)
                lista.insert(x,y)
            matriz_jugador1=np.delete(matriz_jugador1, f1, axis=0)
            matriz_jugador1=np.insert(matriz_jugador1, f1, lista, axis=0)
            print(matriz_jugador1)
    if flota1==3 and cuenta==3:
        cs=cs+1
        if cs<=3:
            for k in range(0,len(listaposionfila)):
                x=listaposionfila[k]
                y=3
                lista.pop(x)
                lista.insert(x,y)
            matriz_jugador1=np.delete(matriz_jugador1, f1, axis=0)
            matriz_jugador1=np.insert(matriz_jugador1, f1, lista, axis=0)
            print(matriz_jugador1)
    if flota1==4 and cuenta==1:
        cl=cl+1
        if cl<=4:
            for k in range(0,len(listaposionfila)):
                x=listaposionfila[k]
                y=4
                lista.pop(x)
                lista.insert(x,y)
            matriz_jugador1=np.delete(matriz_jugador1, f1, axis=0)
            matriz_jugador1=np.insert(matriz_jugador1, f1, lista, axis=0)
            print(matriz_jugador1)

#columna jugador 3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

while pregunta == "c":
    flota2 = int(input("Ingrese una de  las opciones del tipo de flota(INGRESE 0000 PARA TERMINAR EL LLENADO):"))
    if flota2==0000:
        pregunta2(flota2)
    text2 = input("Ingrese las coordenadas:")
    indice = 0
    al = 2
    el = 5
    il = 8
    ol = 11
    ul = 14
    c_lista = 0
    c0 = 0
    def diez1(listaCoordenadas):  # funcion para convertir las coordenadas de 10 en un entero sin alterar el resultado
        c_lista = 0
        clo = 1
        listaCoordenadas2 = []
        numeromasrepite = listaCoordenadas[1]
        for x in range(0, len(listaCoordenadas)):
            if x % 2 == 0:
                listaCoordenadas2.append(listaCoordenadas[x])
                c_lista = c_lista + 1  #############3
                clo = c_lista * 2  ##############33
        listaCoordenadas2.pop()
        ola = listaCoordenadas2[-1]  #####
        if ola == 1:
            listaCoordenadas2.pop()
            listaCoordenadas2.insert(-1, 10)
            listaCoordenadas2.sort()
        for i in range(0, clo):
            if i % 2 != 0:
                listaCoordenadas2.insert(i, numeromasrepite)
        listaCoordenadas2.pop()
        return listaCoordenadas2


    def diez2(listaCoordenadas):
        contadorlista = 0
        listaCoordenadas2 = []
        numeromasrepite = listaCoordenadas[1]  ##########################
        for x in range(0, len(listaCoordenadas)):
            if x % 3 == 0:
                listaCoordenadas2.append(listaCoordenadas[x])
        ola2 = listaCoordenadas2[-1]
        if ola2 == 0:
            listaCoordenadas2.pop()
        print(listaCoordenadas2)
        ola = listaCoordenadas2[-1]
        if ola == 1:
            listaCoordenadas2.pop()  ##################################################################
            listaCoordenadas2.insert(ola, 10)
            listaCoordenadas2.sort()

        for z in range(len(listaCoordenadas2)):
            contadorlista = contadorlista + 1
        contadorlista = contadorlista * 2

        for i in range(0, contadorlista):
            if i % 2 != 0:
                listaCoordenadas2.insert(i, 10)
        return listaCoordenadas2


    while indice < len(text2):
        letra = text2[indice]
        indice += 1
        if letra != "," and letra != " ":
            listaCoordenadas.append(letra)
            listaCoordenadas = list(map(int,listaCoordenadas))
        if letra == "0":
            c0 = c0 + 1

    if c0 == 1:
        listaCoordenadas = diez1(listaCoordenadas)

    if c0 > 1:
        listaCoordenadas = diez2(listaCoordenadas)


    numero_columna=listaCoordenadas[0]  # numero filaaaaaaaaaaaaaaaaaa
    # obtener la fila de la matriz
    listaCoordenadasColumnas= []
    for h in range(0,len(listaCoordenadas)):
        if h%2==0:
            listaCoordenadasColumnas.append(listaCoordenadas[h])
    cuenta=len(listaCoordenadasColumnas)




   #matriz remplazo333333333333333333333333333333333333333333333333333333333333333333333333333333333
    cp=0
    cb=0
    cs=0
    cl=0
    f2=numero_columna
    fila2=matriz_jugador1[:, f2]#sacamos columna de la matriz
    lista2=fila2.tolist()#convertimos a lista
    if flota2==1 and cuenta==5:
        cp=cp+1
        if cp==1:
            for k in range(0,len(listaCoordenadasColumnas)):
                x=listaCoordenadasColumnas[k]
                y=1
                lista2.pop(x)
                lista2.insert(x,y)
            matriz_jugador1 = np.delete(matriz_jugador1, f2, axis=1)
            matriz_jugador1= np.insert(matriz_jugador1, f2, lista2, axis=1)
            print(matriz_jugador1)
    if flota2==2 and cuenta==4:
        cb=cb+1
        if cb<=2:
            for k in range(0,len(listaCoordenadasColumnas)):
                x =listaCoordenadasColumnas[k]
                y = 2
                lista2.pop(x)
                lista2.insert(x, y)
            matriz_jugador1= np.delete(matriz_jugador1, f2, axis=1)
            matriz_jugador1= np.insert(matriz_jugador1, f2, lista2, axis=1)
            print(matriz_jugador1)
    if flota2==3 and cuenta==3:
        cs=cs+1
        if cs<=3:
            for k in range(0,len(listaCoordenadasColumnas)):
                x =listaCoordenadasColumnas[k]
                y =3
                lista2.pop(x)
                lista2.insert(x, y)
            matriz_jugador1= np.delete(matriz_jugador1, f2, axis=1)
            matriz_jugador1= np.insert(matriz_jugador1, f2, lista2, axis=1)
            print(matriz_jugador1)
    if flota2==4 and cuenta==1:
        cl=cl+1
        if cl<=4:
            for k in range(0,len(listaCoordenadasColumnas)):
                x =listaCoordenadasColumnas[k]
                y = 4
                lista2.pop(x)
                lista2.insert(x, y)
            matriz_jugador1= np.delete(matriz_jugador1, f2, axis=1)
            matriz_jugador1= np.insert(matriz_jugador1, f2, lista2, axis=1)
            print(matriz_jugador1)
print(matriz_jugador1)



