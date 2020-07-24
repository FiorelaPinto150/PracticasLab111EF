import numpy as np
#JUGADOR N°1------------------------------------------------------------------------------------------------------------------
print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("                           HUNDIR LA FLOTA")
print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("OOJOOOO")
print("NOTA:ES MUY IMPORTANTE COMPLETAR FILAS PRIMERO Y DESPUES COLUMNAS O UNA DE ESTAS SOLAMENTE EL NO HACER CASO DE ESTE ORDEN PROVOCARA ERRORES EN EL PROGRAMA ")
lista_de_listas =[[0,1,2,3,4,5,6,7,8,9,10],[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
lista_de_listas2 =[["1,1", "1,2", "1,3", "1,4", "1,5", "1,6", "1,7", "1,8", "1,9", "1,10"],["2,1", "2,2", "2,3", "2,4", "2,5", "2,6", "2,7", "2,8", "2,9", "2,10"],["3,1", "3,2", "3,3", "3,4", "3,5", "3,6", "3,7", "3,8", "3,9", "3,10"],["4,1", "4,2", "4,3", "4,4", "4,5", "4,6", "4,7", "4,8", "4,9", "4,10"],["5,1", "5,2", "2,3", "5,4", "5,5", "5,6", "5,7", "5,8", "5,9", "5,10"],["6,1", "6,2", "6,3", "6,4", "6,5", "6,6", "6,7", "6,8", "6,9", "6,10"],["7,1", "7,2", "7,3", "7,4", "7,5", "7,6", "7,7", "7,8", "7,9", "7,10"],["8,1", "8,2", "8,3", "8,4", "8,5", "8,6", "8,7", "8,8", "8,9", "8,10"],["9,1", "9,2", "9,3", "9,4", "9,5", "9,6", "9,7", "9,8", "9,9", "9,10"],["10,1", "10,2", "10,3", "10,4", "10,5", "10,6", "10,7", "10,8", "10,9", "10,10"]]
matriz_jugador1=np.array(lista_de_listas)
matriz2=matriz_jugador1
matriz_jugador2=matriz_jugador1
matrizAuxiliar=np.array(lista_de_listas2)
c=0
d=0
print("Posiciones de una matriz")
print(matrizAuxiliar)
print("Recuerde que puede seleccionar:\n1)1 Portaviones\n2)2 Buques\n2)3 Submarinos\n4)4 Lanchas")
jugador1=input("Ingrese la contraseña de su juego JUGADOR 1:")
jugador2=input("Ingrese la contraseña de su juego JUGADOR 2:")
pregunta=input("Ingrese primeramente a las filas con SI (recuerde que ya no regresaras a filas si pasa esta opcion),ingrese NO para las columnas:     ").lower()
#JUGADOR N°1
#while verifica variable pregunta
key = jugador1
t = 0
password = ""
while password != key and t <= 3:
    t = t + 1
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")
correcta1=1
if correcta1==1:
    while pregunta == "si":
        flota1 = int(input("Ingrese una de  las opciones del tipo de flota:"))#numeros que dependen del tipo de flota
        #transformaremos las coordenadas en caracteres y despues una lista
        text = input("Ingrese las coordenadas:")
        listaCoordenadas = []
        indice = 0
        while indice < len(text):
            letra = text[indice]
            indice += 1
            if letra != "," and letra != " ":
                listaCoordenadas.append(letra)
                listaCoordenadas = list(map(int, listaCoordenadas))
        # la lista de las coordenadas
        # cuenta cuantas posiciones pares y impares tiene la listacoordenadas
        file = []
        colun = []
        indicefila = 0
        indicecolumna = 0
        for i in range(0, len(listaCoordenadas)):
            if i % 2 == 0:
                numero_fila = listaCoordenadas[i]
                aux1 = listaCoordenadas[i]
                file.append(aux1)#crea una lista con todos los valores que no se repitan para crear un vector que nos ayudara a saber las posiciones debe ocupar cada flota
            if i % 2 != 0:
                numero_columna = listaCoordenadas[i]
                aux3 = listaCoordenadas[i]
                colun.append(aux3)#misma logica que crear una lista con las posiciones en las que se debe insertar las flotas
        cuenta = len(colun)  # cuenta de el tamaño de colun
    #Ahora empezaremos a verificar en que fila sera destinadas las flotas y en que posiciones
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
                for k in range(0,len(colun)):#nos guiaremos por el tamaño de colun para dar a "x" el valor de la posicion en donde debe reeplazar el "0" por uno de los numeros segun la condicion
                    x=colun[k]
                    y=5
                    lista.pop(x)
                    lista.insert(x,y)
                matriz_jugador1=np.delete(matriz_jugador1,f1,axis=0)#para no alterar cada la matriz eliminaremos la fila en la que debemos llenar con diferentes digitos
                matriz_jugador1=np.insert(matriz_jugador1,f1,lista,axis=0)#en este paso reemplazaremos la lista en la matriz quedando solo el cambio en el llenado de digitos
                #NOTA!!!!!!!!!!!!!!!!!!!!!!!!TIENE EL MISMO PROCEDIMIENTO CADA UNO DE LOS IFs
        if flota1==2 and cuenta==4:
            cb=cb+1
            if cb<=2:
                for k in range(0,len(colun)):
                    x = colun[k]
                    y = 4
                    lista.pop(x)
                    lista.insert(x, y)
                matriz_jugador1 = np.delete(matriz_jugador1, f1, axis=0)
                matriz_jugador1 = np.insert(matriz_jugador1, f1, lista, axis=0)
        if flota1==3 and cuenta==3:
            cs=cs+1
            if cs<=3:
                for k in range(0,len(colun)):
                    x = colun[k]
                    y = 3
                    lista.pop(x)
                    lista.insert(x, y)
                matriz_jugador1 = np.delete(matriz_jugador1, f1, axis=0)
                matriz_jugador1 = np.insert(matriz_jugador1, f1, lista, axis=0)
        if flota1==4 and cuenta==1:
            cl=cl+1
            if cl<=4:
                for k in range(0,len(colun)):
                    x = colun[k]
                    y = 1
                    lista.pop(x)
                    lista.insert(x, y)
                matriz_jugador1 = np.delete(matriz_jugador1, f1, axis=0)
                matriz_jugador1 = np.insert(matriz_jugador1, f1, lista, axis=0)
        #ESTA CONTRASEÑA AYUDARA A QUE EL OTRO JUGADOR NO interceda en el juego y la tabla del otro jugador
        pregunta=input("Ingrese las Flotas que desee en las filas(ya no regresara a esta opcion)caso contrario para las columnas ingresar NO:")




    while pregunta == "no":
        flota2 = int(input("Ingrese una de  lasopciones del tipo de flota:"))
        text = input("Ingrese las coordenadas:")
        listaCoordenadas = []
        indice = 0
        while indice < len(text):
            letra = text[indice]
            indice += 1
            if letra != "," and letra != " ":
                listaCoordenadas.append(letra)
                listaCoordenadas = list(map(int, listaCoordenadas))
        # la lista de las coordenadas
        # cuentacuantas posiciones pares y impares tiene la listacoordenadas
        file = []
        colun = []
        indicefila = 0
        indicecolumna = 0
        for i in range(0, len(listaCoordenadas)):
            if i % 2 == 0:
                numero_fila = listaCoordenadas[i]
                aux1 = listaCoordenadas[i]
                file.append(aux1)
            if i % 2 != 0:
                numero_columna = listaCoordenadas[i]
                aux3 = listaCoordenadas[i]
                colun.append(aux3)
        cuenta = len(colun)  # cuenta de colun


        listaCoordenadas = []
        indice = 0
        while indice < len(text):
            letra = text[indice]
            indice += 1
            if letra != "," and letra != " ":
                listaCoordenadas.append(letra)
                listaCoordenadas = list(map(int, listaCoordenadas))
        # la lista de las coordenadas
        # cuentacuantas posiciones pares y impares tiene la listacoordenadas
        file = []
        colun = []
        indicefila = 0
        indicecolumna = 0
        for i in range(0, len(listaCoordenadas)):
            if i % 2 == 0:
                numero_fila = listaCoordenadas[i]
                aux1 = listaCoordenadas[i]
                file.append(aux1)
            if i % 2 != 0:
                numero_columna = listaCoordenadas[i]
                aux3 = listaCoordenadas[i]
                colun.append(aux3)
        cuenta = len(colun)  # cuenta de colun

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
                for k in range(0,len(file)):
                    x=file[k]
                    y=5
                    lista2.pop(x)
                    lista2.insert(x,y)
                matriz_jugador1 = np.delete(matriz_jugador1, f2, axis=1)
                matriz_jugador1= np.insert(matriz_jugador1, f2, lista2, axis=1)
        if flota2==2 and cuenta==4:
            cb=cb+1
            if cb<=2:
                for k in range(0,len(file)):
                    x =file[k]
                    y = 4
                    lista2.pop(x)
                    lista2.insert(x, y)
                matriz_jugador1= np.delete(matriz_jugador1, f2, axis=1)
                matriz_jugador1= np.insert(matriz_jugador1, f2, lista2, axis=1)
        if flota2==3 and cuenta==3:
            cs=cs+1
            n3=3
            if cs<=3:
                x = file[k]
                y = 3
                lista2.pop(x)
                lista2.insert(x, y)
            matriz_jugador1 = np.delete(matriz_jugador1, f2, axis=1)
            matriz_jugador1 = np.insert(matriz_jugador1, f2, lista2, axis=1)
        if flota2==4 and cuenta==1:
            cl=cl+1
            n=1
            if cl<=4:
                x = colun[k]
                y = 1
                lista2.pop(x)
                lista2.insert(x, y)
        matriz_jugador1 = np.delete(matriz_jugador1, f2, axis=1)
        matriz_jugador1 = np.insert(matriz_jugador1, f2, lista2, axis=1)
        pregunta=input("Ingrese las Flotas que desee en las Columnas:")


#EN ESTA PARTE COMPARAREMOS LAS MATRICES DEL CONTRINCANTE PARA VERIFICAR CUANTAS FLOTAS PUEDE PERDER A MEDIDA QUE PASE EL JUEGO

#JUGADOR N°2-------------------------------------------------------------------------------------------------------------------------------------------------------
#misma analogia que jugador1

key2 = jugador2
f=0
password2 = ""
while password2 != key2 and f<= 3:
    f = f + 1
    password2 = input("Introduce la contraseña: ")
print("Contraseña correcta")
correcta2=0
if correcta2==0:
    matriz_jugador2=np.array(lista_de_listas)
    matriz2=np.array(lista_de_listas2)
    c=0
    d=0
    print(matriz2)
    print()
    print(matriz2)
    print("Recuerde que puede seleccionar:\n1)1 Portaviones\n2)2 Buques\n2)3 Submarinos\n4)4 Lanchas")

    pregunta=input("Ingrese primeramente a las filas con SI (recuerde que ya no regresaras a filas si pasa esta opcion),ingrese NO para las columnas:     ").lower()

    while pregunta == "si":
        flota1 = int(input("Ingrese una de  lasopciones del tipo de flota:"))
        text = input("Ingrese las coordenadas:")
        listaCoordenadas = []
        indice = 0
        while indice < len(text):
            letra = text[indice]
            indice += 1
            if letra != "," and letra != " ":
                listaCoordenadas.append(letra)
                listaCoordenadas = list(map(int, listaCoordenadas))
        # la lista de las coordenadas
        # cuentacuantas posiciones pares y impares tiene la listacoordenadas
        file = []
        colun = []
        indicefila = 0
        indicecolumna = 0
        for i in range(0, len(listaCoordenadas)):
            if i % 2 == 0:
                numero_fila = listaCoordenadas[i]
                aux1 = listaCoordenadas[i]
                file.append(aux1)
            if i % 2 != 0:
                numero_columna = listaCoordenadas[i]
                aux3 = listaCoordenadas[i]
                colun.append(aux3)
        cuenta = len(colun)  # cuenta de colun

        cp=0
        cb=0
        cs=0
        cl=0
        f1=numero_fila
        fila=matriz_jugador2[f1]#sacamos fila de la matriz
        lista=fila.tolist()#convertimos a lista
        if flota1==1 and cuenta==5:
            cp=cp+1
            if cp==1:
                for k in range(0,len(colun)):
                    x=colun[k]
                    y=5
                    lista.pop(x)
                    lista.insert(x,y)
                matriz_jugador2=np.delete(matriz_jugador2,f1,axis=0)
                matriz_jugador2=np.insert(matriz_jugador2,f1,lista,axis=0)
        if flota1==2 and cuenta==4:
            cb=cb+1
            if cb<=2:
                for k in range(0,len(colun)):
                    x = colun[k]
                    y = 4
                    lista.pop(x)
                    lista.insert(x, y)
                matriz_jugador2 = np.delete(matriz_jugador2, f1, axis=0)
                matriz_jugador2 = np.insert(matriz_jugador2, f1, lista, axis=0)
        if flota1==3 and cuenta==3:
            cs=cs+1
            if cs<=3:
                for k in range(0,len(colun)):
                    x = colun[k]
                    y = 3
                    lista.pop(x)
                    lista.insert(x, y)
                matriz_jugador2 = np.delete(matriz_jugador2, f1, axis=0)
                matriz_jugador2 = np.insert(matriz_jugador2, f1, lista, axis=0)
        if flota1==4 and cuenta==1:
            cl=cl+1
            if cl<=4:
                for k in range(0,len(colun)):
                    x = colun[k]
                    y = 1
                    lista.pop(x)
                    lista.insert(x, y)
                matriz_jugador2= np.delete(matriz_jugador2, f1, axis=0)
                matriz_jugador2= np.insert(matriz_jugador2, f1, lista, axis=0)
        pregunta=input("Ingrese las Flotas que desee en las filas(ya no regresara a esta opcion)caso contrario para las columnas ingresar NO:")
        key = jugador2
        t = 0
        password = ""
        while password != key and t <= 3:
            t = t + 1
            password = input("Introduce la contraseña: ")
        print("Contraseña correcta")
        correcta2=0

    while pregunta == "no":
        flota2 = int(input("Ingrese una de  lasopciones del tipo de flota:"))
        text = input("Ingrese las coordenadas:")
        listaCoordenadas = []
        indice = 0
        while indice < len(text):
            letra = text[indice]
            indice += 1
            if letra != "," and letra != " ":
                listaCoordenadas.append(letra)
                listaCoordenadas = list(map(int, listaCoordenadas))
        # la lista de las coordenadas
        # cuentacuantas posiciones pares y impares tiene la listacoordenadas
        file = []
        colun = []
        indicefila = 0
        indicecolumna = 0
        for i in range(0, len(listaCoordenadas)):
            if i % 2 == 0:
                numero_fila = listaCoordenadas[i]
                aux1 = listaCoordenadas[i]
                file.append(aux1)
            if i % 2 != 0:
                numero_columna = listaCoordenadas[i]
                aux3 = listaCoordenadas[i]
                colun.append(aux3)
        cuenta = len(colun)  # cuenta de colun


        listaCoordenadas = []
        indice = 0
        while indice < len(text):
            letra = text[indice]
            indice += 1
            if letra != "," and letra != " ":
                listaCoordenadas.append(letra)
                listaCoordenadas = list(map(int, listaCoordenadas))
        # la lista de las coordenadas
        # cuentacuantas posiciones pares y impares tiene la listacoordenadas
        file = []
        colun = []
        indicefila = 0
        indicecolumna = 0
        for i in range(0, len(listaCoordenadas)):
            if i % 2 == 0:
                numero_fila = listaCoordenadas[i]
                aux1 = listaCoordenadas[i]
                file.append(aux1)
            if i % 2 != 0:
                numero_columna = listaCoordenadas[i]
                aux3 = listaCoordenadas[i]
                colun.append(aux3)
        cuenta = len(colun)  # cuenta de colun

        cp=0
        cb=0
        cs=0
        cl=0
        f2=numero_columna
        fila2=matriz_jugador2[:, f2]#sacamos columna de la matriz
        lista2=fila2.tolist()#convertimos a lista
        if flota2==1 and cuenta==5:
            cp=cp+1
            if cp==1:
                for k in range(0,len(file)):
                    x=file[k]
                    y=5
                    lista2.pop(x)
                    lista2.insert(x,y)
                matriz_jugador2 = np.delete(matriz_jugador2, f2, axis=1)
                matriz_jugador2= np.insert(matriz_jugador2, f2, lista2, axis=1)
        if flota2==2 and cuent2==4:
            cb=cb+1
            if cb<=2:
                for k in range(0,len(file)):
                    x =file[k]
                    y = 4
                    lista2.pop(x)
                    lista2.insert(x, y)
                matriz_jugador2= np.delete(matriz_jugador2, f2, axis=1)
                matriz_jugador2= np.insert(matriz_jugador2, f2, lista2, axis=1)
        if flota2==3 and cuenta==3:
            cs=cs+1
            n3=3
            if cs<=3:
                x = file[k]
                y = 3
                lista2.pop(x)
                lista2.insert(x, y)
            matriz_jugador2= np.delete(matriz_jugador2, f2, axis=1)
            matriz_jugador2 = np.insert(matriz_jugador2, f2, lista2, axis=1)
        if flota2==4 and cuenta==1:
            cl=cl+1
            n=1
            if cl<=4:
                x = colun[k]
                y = 1
                lista2.pop(x)
                lista2.insert(x, y)
        matriz_jugador2 = np.delete(matriz_jugador2, f2, axis=1)
        matriz_jugador2= np.insert(matriz_jugador2, f2, lista2, axis=1)
        pregunta=input("Ingrese las Flotas que desee en las Columnas:")

print(matriz_jugador1)
print(matriz_jugador2)

def jugador1_func(metrix1):
    p=0
    d=0
    s=0
    l=0
    cuenta=0
    if cuenta<5:
        a,b=map(int,input("Ingrese la coordenada para hundir a su contrincante").split())
        dat=metrix1[a,b]
        if dat==1:
            p=p+1
            if p==1:
                print("Hundieron tu portaviones!!!")
                cuenta=cuenta+1
        if dat==2:
            d=d+1
            if d==2 or d==4:
                print("hundieron tu buque")
                if d == 9:
                    print("Hundieron todos tus Buques!!!")
                    cuenta = cuenta + 1
        if dat == 3:
            s=s+1
            if s==3 or s==6 or s==9:
                print("Hundieron tu Submarino")
                if s==9:
                    print("Hundieron todos tus Submarinos!!!")
                    cuenta = cuenta + 1
        if dat == 4:
            l=l+1
            if l==1 or l==2 or l==3 or l==4:
                print("Hundieron tu Lancha")
                if l==4:
                    print("Hundieron todas tus Lanchas!!!")
                    cuenta = cuenta + 1
    else:
        print("GAME OVER")
jugador1_func(matriz_jugador2)
def jugador2_func(matrix2):
    w = 0
    o = 0
    h = 0
    n = 0
    cuenta2 = 0
    if cuenta2 < 5:
        z,ñ= map(int, input("Ingrese la coordenada para hundir a su contrincante").split())
        dat2= matrix2[z,ñ]
        if dat == 1:
            w =w+1
            if w == 1:
                print("Hundieron tu portaviones!!!")
                cuenta2 = cuenta2 + 1
        if dat2== 2:
            h = h+ 1
            if h == 2 or h == 4:
                print("hundieron tu buque")
                if h == 9:
                    print("Hundieron todos tus Buques!!!")
                    cuenta2 = cuenta2 + 1
        if dat2== 3:
            n = n + 1
            if s == 3 or s == 6 or s == 9:
                print("Hundieron tu Submarino")
                if n == 9:
                    print("Hundieron todos tus Submarinos!!!")
                    cuenta2 = cuenta2 + 1
        if dat2== 4:
            o= o + 1
            if o == 1 or o == 2 or o== 3 or o == 4:
                print("Hundieron tu Lancha")
                if l == 4:
                    print("Hundieron todas tus Lanchas!!!")
                    cuenta2= cuenta2 + 1
    else:
        print("GAME OVER")
jugador2_func(matrix_jugador1)

