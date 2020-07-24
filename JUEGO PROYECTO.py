import numpy as np
#JUGADOR N°1------------------------------------------------------------------------------------------------------------------
print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("                           HUNDIR LA FLOTA")
print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")

lista_de_listas =[[0,1,2,3,4,5,6,7,8,9,10],[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
lista_de_listas2 =[["1,1", "1,2", "1,3", "1,4", "1,5", "1,6", "1,7", "1,8", "1,9", "1,10"],["2,1", "2,2", "2,3", "2,4", "2,5", "2,6", "2,7", "2,8", "2,9", "2,10"],["3,1", "3,2", "3,3", "3,4", "3,5", "3,6", "3,7", "3,8", "3,9", "3,10"],["4,1", "4,2", "4,3", "4,4", "4,5", "4,6", "4,7", "4,8", "4,9", "4,10"],["5,1", "5,2", "2,3", "5,4", "5,5", "5,6", "5,7", "5,8", "5,9", "5,10"],["6,1", "6,2", "6,3", "6,4", "6,5", "6,6", "6,7", "6,8", "6,9", "6,10"],["7,1", "7,2", "7,3", "7,4", "7,5", "7,6", "7,7", "7,8", "7,9", "7,10"],["8,1", "8,2", "8,3", "8,4", "8,5", "8,6", "8,7", "8,8", "8,9", "8,10"],["9,1", "9,2", "9,3", "9,4", "9,5", "9,6", "9,7", "9,8", "9,9", "9,10"],["10,1", "10,2", "10,3", "10,4", "10,5", "10,6", "10,7", "10,8", "10,9", "10,10"]]
matriz_jugador1=np.array(lista_de_listas)
matriz2=np.array(lista_de_listas2)
c=0
d=0

print("Posiciones de una matriz")
print(matriz2)
print("Recuerde que puede seleccionar:\n1)1 Portaviones\n2)2 Buques\n2)3 Submarinos\n4)4 Lanchas")

jugador1=input("Ingrese la contraseña de su juego:")
jugador2=input("Ingrese la contraseña de su juego:")

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
    fila=matriz_jugador1[f1]#sacamos fila de la matriz
    lista=fila.tolist()#convertimos a lista
    if flota1==1 and cuenta==5:
        cp=cp+1
        if cp==1:
            for k in range(0,len(colun)):
                x=colun[k]
                y=5
                lista.pop(x)
                lista.insert(x,y)
            matriz_jugador1=np.delete(matriz_jugador1,f1,axis=0)
            matriz_jugador1=np.insert(matriz_jugador1,f1,lista,axis=0)
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
    pregunta=input("Ingrese las Flotas que desee en las filas(ya no regresara a esta opcion)caso contrario para las columnas ingresar NO:")
    key = jugador1
    t = 0
    password = ""
    while password != key and t <= 3:
        t = t + 1
        password = input("Introduce la contraseña: ")
        print("Contraseña correcta")




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
        key = jugador1
        t = 0
        password = ""
        while password != key and t <= 3:
            t = t + 1
            password = input("Introduce la contraseña: ")
            print("Contraseña correcta")



#JUGADOR N°2-------------------------------------------------------------------------------------------------------------------------------------------------------



matriz_jugador2=np.array(lista_de_listas)
matriz2=np.array(lista_de_listas2)
c=0
d=0
print(matriz)
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
    key = jugador2
    t = 0
    password = ""
    while password != key and t <= 3:
        t = t + 1
        password = input("Introduce la contraseña: ")
        print("Contraseña correcta")




if matriz_jugador1==matriz_jugador2:
    print


