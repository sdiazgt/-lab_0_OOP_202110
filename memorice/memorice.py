import random
def crear_lista(cartas):
    numero = cartas
    #lista visual
    visual =[]
    for i in range(2):
        visual.append([])
        for j in range(numero):
            visual[i].append("#")
    for a in range(2):
        print(visual[a])
    #Mezclador de listas   
    mezclar = []
    for i in range(numero+1):
        if i > 0:
            mezclar.append(i)
            mezclar.append(i)
    random.shuffle(mezclar)
    print(mezclar)
    #lista real
    Real = []
    for i in range(2):
        Real.append([])
        for j in range(numero):
            Real[i].append(mezclar[0])
            mezclar.pop(0)
    for a in range(2):
        print(Real[a])
    return [visual,Real]

def imprimir(tablero):
    tabla= tablero
    for a in zip(*tabla):         #Zip() fue sacado de Stackoverflow
        print(" ".join(map(str, a)))
    return

def dar_vuelta(lista,posicion):
    real = lista[1]
    censura = lista[0]
    print(real)
    x = int(posicion.split(sep=',')[0])
    y = int(posicion.split(sep=',')[1])
    censura[y-1][x-1] = real[y-1][x-1]
    imprimir(censura)
    

crear = crear_lista(int(input("cuantas cartas quieres: ")))
pos= str(input("ingrese la cordenada en el Formato x,y (Ej. 1,2):"))
dar_vuelta(crear,pos)