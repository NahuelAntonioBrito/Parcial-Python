'''Enunciado:

Una compañía famacéutica necesita un programa para procesar los datos de los medicamentos que fabrica. Por cada medicamento,
 se tienen los siguientes datos: código de identificación (un entero), nombre del medicamento (una cadena),
  el tipo de medicamento (un entero entre 1 y 40 para indicar, por ejemplo: 1: pedíátrico, 2: analgésico, etc.), 
  el modo de almacenamiento (otro entero, entre 0 y 9 para indicar por ejemplo: 0: en frío, 1: a temperatura ambiente, 
  2: sin exposición  a la luz, etc.) y el costo de fabricación (un flotante).  Se pide definir en un módulo separado el tipo de registro
   Medicamento con los campos pedidos, y desarrollar en un segundo módulo un programa en Python controlado por menú de opciones que permita 
   gestionar las siguientes tareas:

Requerimientos comunes a todos los alumnos que recuperan para REGULARIZAR o para APROBAR/PROMOCIONAR:

Cargar un arreglo de registros con los datos de n medicamentos de manera que en todo momento se mantenga ordenado por código de identificación,
 de menor a mayor. Para esto debe utilizar el algoritmo de inserción ordenada con búsqueda binaria (se considerará directamente incorrecta
  la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada, pero con búsqueda 
  secuencial). Puede hacer la carga en forma manual (en cuyo caso realice las validaciones que sean necesarias), o puede generar los datos 
  en forma automática (con valores aleatorios generados en el rango correcto). Pero si hace carga manual, TODA la carga debe ser manual, 
  y si la hace automática entonces TODA debe ser automática.
Mostrar los datos de los medicamentos (a razón de uno por por línea de pantalla) cuyo costo sea mayor al costo promedio de todos los registros del arreglo.
Usando el arreglo creado en el punto 1, determine la cantidad de medicamentos por cada combinación posible de tipo y modo de almacenamiento (o sea, 400 contadores: cantidad de medicamentos tipo 1 con modo de almacenamiento 0,  tipo 1 con modo 2, etc.). Genere TODOS los contadores, pero muestre sólo los resultados que correspondan al tipo de medicamento t que se carga por teclado.
Usando el arreglo creado en el punto 1, generar un archivo con todos los medicamentos cuyo modo de almacenamiento sea  2, 5 o 9. Si el archivo ya existía, eliminar su contenido y comenzar desde cero.
Mostrar por pantalla el contenido del archivo creado en el punto anterior. Pero al final del listado, muestre una línea adicional indicando la cantidad de registros que se mostraron que eran del tipo de medicamento x, cargando x por teclado.

Requerimiento EXTRA solo para los alumnos que recuperan para APROBAR/PROMOCIONAR:


6. (Además de todos los ítems del 1 al 5 planteados para los alumnos que rinden para regularizar, los alumnos que rindan para aprobar en forma directa deben agregar una solución para el ítem que sigue): 
En el menú de opciones del programa, incluya una opción que permita cargar una cadena de caracteres,
 y luego pase esa cadena como parámetro a una función que determine cuántas palabras de la cadena comenzaban con una vocal 
 y tenían al menos un dígito en cualquier posición.'''

from funciones import *
from registro import *

def cargar_mayor_que(valor, mensaje="Ingrese un valor:"):
    num = int(input(mensaje))
    while num <= valor:
        print('Error, debe ingresar un valor mayor que', valor)
        num = int(input(mensaje))
    return num


def menu():
    print("\n", "*" * 100)
    print("Crear arreglo de registro ingrese 1")
    print("Mostrar arreglo ingrese 2")
    print("determinar cantidad de medicamentos ingrese 3")
    print("generar un archivo ingrese 4")
    print("Mostrar archivo ingrese 5")
    print("procesar cadena de caracteres ingrese 6")
    print("*" * 100)
    op = int(input("ingrese la opcion deseada: "))
    return op


def pirncipal():
    titulos = get_titulos()
    medicamentos = []
    op = -1
    n = cargar_mayor_que(0, "ingrese la cantidad de medicamentos: ")
    while op != 0:
        op = menu()
        if op == 1:
            medicamentos = crear_arreglo(n)
        elif op == 2:

            if len(medicamentos) > 0:
                promedio = calcular_costo_promedio(medicamentos)
                mostrar_v(medicamentos)
                mostrar_vec(medicamentos, promedio)
                print("el promedio es: ", promedio)
            else:
                print("Eroor, primero debe ejecutar la opcion 1")
        elif op == 3:
            if len(medicamentos) > 0:
                t = int(input("ingrese el tipo de producto: "))
                mat = generar_matriz(medicamentos)
                mostrar_matriz(mat, t)
            else:
                print("Eroor, primero debe ejecutar la opcion 1")
        
        elif op == 4:
            if len(medicamentos) > 0:
                crear_archivo(medicamentos)
                print("archivo creado")
            else:
                print("Eroor, primero debe ejecutar la opcion 1")
        
        elif op == 5:
            if len(medicamentos) > 0:
                x = int(input("ingrese el tipo de medicamento: "))
                mostrar_archivo(titulos, x)
            else:
                print("Eroor, primero debe ejecutar la opcion 1")
        
        elif op == 6:
            cadena = input("ingrese una cadena de caracteres: ")
            cant_pal = procesar_cadena(cadena)
            print("la cantidad de palabras que comienzan con vocal y tienen digitos es: ", cant_pal)
        

if __name__ == "__main__":
    pirncipal()



