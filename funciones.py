import pickle
import os
import random
from registro import*

NOMBRE_ARCHIVO = "medicamentos.dat"

def generar_nombre():
    nombres = "producto1", "producto2", "producto3", "producto4"
    mas = "por10", "ndio34", "mfop903", "02nu9" 
    res = random.choice(nombres) + " " + random.choice(mas)
    return res


def carga_automatica():
    cod = random.randint(1, 20)
    nombre = generar_nombre()
    tipo = random.randint(1, 40)
    almacenamiento = random.randint(0, 9)
    costo = random.randint(1000, 5000)
    linea = MEDICAMENTO(cod, nombre, tipo, almacenamiento,costo)
    return linea 



def add_in_order(vec, x):
    n = len(vec)
    pos = n
    izq = 0
    der = n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].codigo == x.codigo:
            pos = c
            break
        if x.codigo < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [x] 


def crear_arreglo(n):
    vec = []
    for i in range(n):
        linea = carga_automatica()
        add_in_order(vec, linea)
    return vec

def calcular_costo_promedio(vec):
    cant = 0
    total = len(vec)
    for i in range(total):
        cant += vec[i].costo
    promedio = 0
    if total != 0:
        promedio = cant // total
    else:
        print("error divide por cero")
    return promedio  


def mostrar_vec(vec, promedio):
    titulos = get_titulos() 
    print(titulos)
    for i in range(len(vec)):
        if vec[i].costo > promedio:
            print(vec[i])


def mostrar_v(vec):
    titulos = get_titulos()
    print(titulos)
    for i in range(len(vec)):
        print(vec[i])


def generar_matriz(vec):
    mat = [0] * 10
    for i in range(len(mat)):
        mat[i] = [0] * 41

    for med in vec:
        f = med.almacenamiento
        c = med.tipo
        mat[f][c] += 1
    return mat


def mostrar_matriz(mat, t):
    for j in range(len(mat[t])):
        print('hay', mat[t][j], 'medicamentos de tipo', t ,'y modo', j)

def crear_archivo(vec):
    arch = open(NOMBRE_ARCHIVO, "wb")
    for i in range(len(vec)):
        if vec[i].almacenamiento == 2 or vec[i].almacenamiento == 5 or vec[i].almacenamiento == 9:
            pickle.dump(vec[i], arch)

    arch.close()


def es_vocal(car):
    return car.lower() in "aeiouáéíóúü"


def es_digito(car):
    return car in "0123456789"


def cargar_texto(mensaje='Ingrese un texto (finaliza con punto):'):
    texto = input(mensaje)
    while len(texto) == 0 or texto[-1] != '.':
        print("Error en el texto ingresado.")
        texto = input(mensaje)
    return texto


def procesar_cadena(cadena):
    cont_voc = clet = cant_pal = 0
    hay_digito = False
    for car in cadena:
        if car != " " and car != ".":
            clet += 1
            if clet == 1 and es_vocal(car):
                cont_voc += 1
            if es_digito(car):
                hay_digito = True
        else:
            if cont_voc and hay_digito:
                cant_pal += 1
            #reset 
            cont_voc = clet = 0
            hay_digito = False
    return cant_pal
    

def mostrar_archivo(titulos, x):
    cont = 0
    print(titulos)
    archivo = open(NOMBRE_ARCHIVO, 'rb')
    size = os.path.getsize(NOMBRE_ARCHIVO)
    while archivo.tell() < size:
        med = pickle.load(archivo)
        print(med)
        if med.tipo == x:
            cont += 1
    archivo.close()
    print("la cantidad de medicamentos del tipo ", x, "es: ", cont)

