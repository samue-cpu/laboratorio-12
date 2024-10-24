
#ejercicio 1
nombre = ["emerson", "barzola", "navarro", "jamil", "dayner"]
ordenar = sorted(nombre, key = len)
print(ordenar)
#ejercicio 2
numeros=[1,2,3,4,5,6,7,8,9,10]
numeros.sort(reverse=True)
print(numeros)
#ejercicio 3
datos = [("samuel", 21), ("diana",12), ("rolando",10), ("raysa", 16)]
ordenando = sorted(datos, key=lambda edad:edad[1])
print(ordenando)
#ejercicio 4
productos = [{"nombre": "manzan", "precio":20},
             {"nombre": "pera", "precio":15},
             {"nombre": "papaya", "precio":10}]
productos.sort(key=lambda productos: productos["precio"], reverse= False)
print(productos)

#ejercicio 5
def lista_palabras (lista):
    lista =[]
    for i in range(5):
        palabras= input("ingresa:")
        lista.append(palabras)
    return sorted (lista, key =lambda lista: lista[0], )
print ( lista_palabras([]))
#ejercici 6

def ordenar_numeros(numero):
    
    
    return sorted(numero, key=lambda x:(x%2, -x if x%2 else x))
numero = [1,2,3,4,5,6,7,8,9,10]
ordenar = ordenar_numeros(numero)
print(ordenar )

#ejercicio 7
def contar_vocales(cadena):
    vocal = "aeiuoAEIUO"
    contador = 0
    for i in cadena :
        if i in vocal:
            contador +=1
    return contador
lista = ["mango", "programa", "ingles", "sistemas"]
lista.sort(key=contar_vocales, reverse=True)
print(lista)
#ejercicio 8
def ordenar_por_años (fechas):
    fechas = ["13/05/2020", "12/03/2019", "9/10/2021"]
    return sorted(fechas, key =lambda fechas: (fechas.split("/")[2]))

print(ordenar_por_años("fechas"))
 #ejercicio 9
nombre_notas = [("diana", 12), ("pamela", 10), ("samuel",16),("dante", 17)]
nombre_notas. sort(key =lambda nombre:len(nombre[0]), reverse=True)
print(nombre_notas)

