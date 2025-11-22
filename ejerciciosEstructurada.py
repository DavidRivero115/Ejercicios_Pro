"""Escribir un programa que calcule la media de cinco valores numéricos reales (tipo float)
introducidos por teclado.
"""

#x = 0
#l = []
#while x < 3:
#    n = float(input("Dime un numero: "))
#    l.append(n)
#    x +=1
#print (sum(l)/3)

"""Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
luego las muestre en orden inverso a como se han introducido, desde la última cadena
introducida hasta la primera."""

#n = 0
#v = []
#while n < 10:
#    c = input("Introduce la cadena: ") 
#    v.append(c)
#    n +=1
#print(v[::-1])

""" Escribir un programa que determine si un número entero introducido por teclado es
primo o compuesto.
Indicación: Un número primo es aquel que sólo puede dividirse exactamente por sí
mismo y por 1.
"""
""" Escribir un programa que gestione datos almacenados en una lista, de forma que muestre
un menú con las siguientes opciones:
1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.
El programa deberá pedir la información necesaria para cada opción elegida por el
usuario."""

#lista = []
#while True:
#    print("1. Añadir un elemento a la lista")
#    print("2. Cambiar el valor de un elemento de la lista.")
#    print("3. Eliminar un elemento de la lista.")
#    print("4. Eliminar todos los elementos de la lista.")
#    print("5. Mostrar los elementos de la lista.")
#    print("0. Salir del programa.")
#    x = int(input("Introduce la opcion: "))
#
#    if x == 1:
#        lista.append(input("Introduce el elemento que quieras meter: "))
#    elif x == 2:
#        viejo = input("Introduce el valor que quieras cambiar: ")
#        lista[lista.index(viejo)] = input("Introduce el valor nuevo")
#    elif x == 3:
#        lista.remove(input("Introduce el valor a eliminar: "))
#    elif x == 4:
#        lista.clear()
#    elif x == 5:
#        print(lista)
#    else:
#        break

"""Los datos de los empleados de una empresa se almacenan en una lista de tuplas, donde
cada tupla representa a un empleado de la siguiente forma:

(nombre, apellidos, salario)
En el programa, los cuatro empleados que tiene la empresa se almacenan en la siguiente
lista:
empleados = [('María', 'González', 1800.23),
('Javier', 'Ruiz', 1630.50),
('Jesús', 'Pérez', 2100.42),
('Rosa', 'Muñoz', 2240.78)]

Se pide escribir un programa que modifique la lista de empleados incrementando en un
10 % el salario de cada empleado y muestre por pantalla el salario total de los empleados
de la empresa.
"""

#empleados = [
#    ('María', 'González', 1800.23),
#    ('Javier', 'Ruiz', 1630.50),
#    ('Jesús', 'Pérez', 2100.42),
#    ('Rosa', 'Muñoz', 2240.78)]
#x = 0
#while x < len(empleados):
#    empleados = list(empleados[x])
#    print(empleados[2]) # *= 0.10
#    x +=1
#print(empleados)

"""14. Convertir una cantidad de tiempo (en segundos, Z) en la correspondiente en horas,
minutos y segundos, con arreglo al siguiente formato:

3817 segundos = 1 horas, 3 minutos y 37 segundos
"""

#def tiempo(n):
#    Hora = n//3600
#    Minutos = (n % 3600) // 60
#    Segundos = n % 60
#
#    return Hora, Minutos, Segundos
#print(tiempo(3817))

#def polinomio(a1,a2,a3):

#def consecutiva(t):
#    return t == tuple(range(min(t), max(t) +1))
#print(consecutiva((3,4,5,6,7)))

#print(123 // 10)
#print(123 % 10)
#
#suma = lambda n: n if n < 10 else n % 10 + suma(n // 10)
#print(suma(123))

"""Dado un string, crea una función que elimine las repeticiones consecutivas.
Ejemplo:
"aaabbccccd" → "abcd"""

#def sin_repetidos(s):
#    l = []
#    x = 0
#    while x < len(s):
#        if s[x] not in l:
#            l.append(s[x])
#        x +=1
#    return "".join(l)
#
#print(sin_repetidos("aabbbcddd"))

#def palindromo(s):
#    l = ""
#    x = -1
#    while abs(x) <= len(s):
#        l += s[x]
#        x -=1
#    return l == s
#
#print(palindromo("radar"))

#def mayor_en_matriz(x,matriz):
#    lista = []
#    i = 0
#    while i < len(matriz):
#        j = 0
#        while j < len(matriz[i]):
#            if matriz[i][j] > x:
#                lista.append(matriz[i][j])
#            j +=1
#        i +=1
#    return(len(lista))
#print(mayor_en_matriz(7,[[1,2,3],[4,5,6],[7,8,8,9]]))

#def traspuesta(matriz):
#    nueva = []
#    while len(nueva) < len(matriz):
#        nueva.append([0] * len(matriz))
#    i = 0
#    while i < len(matriz):
#        j = 0
#        while j < len(matriz):    
#            nueva[i][j] = matriz[j][i]
#            j +=1
#        i +=1
#    return nueva
#
#print(traspuesta([[1,2,3],[4,5,6],[7,8,9]]))

#def fibonazi(n):
#    l = []
#    a = 1
#    b = 0
#    i = 0
#    while i < n:
#        if b > n:
#            break
#        l.append(b)
#        b, a = b + a, b
#        i +=1
#    print(l)
#    
#fibonazi(30)

"""Una funcion que reciba un numero y devuelva una matriz de n * n con los numeros del 1 al n"""

#def matriz(n):
#    lista = list(range(1, n +1 ))
#    res = [lista]
#    x = n -1
#    while len(res) < n:
#        res.append((lista[x:] + lista[:x]))    
#        x -=1
#    return res
#
#print(matriz(4))

#def traspuesta(matriz):
#    res = []
#    z = 0
#    x = 0
#    y = 0
#    while len(res)  < (len(matriz) +1 or len(res)  < len(matriz) ):
#        while z < len(matriz):
#            lista = []
#            lista.append(matriz[x][y])
#            x +=1
#            z +=1
#        res.append(lista)
#        z = 0
#        y +=1
#    return res
#
#print(traspuesta([[1,2,3],[4,5,6],[7,8,9]]))

def traspuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Crear matriz vacía para la traspuesta
    resultado = []
    i = 0
    while i < columnas:
        resultado.append([0] * filas)
        i += 1
    print(resultado)

    # Rellenar la traspuesta
    i = 0
    while i < filas:
        j = 0
        while j < columnas:
            resultado[j][i] = matriz[i][j]
            j += 1
        i += 1

    return resultado

print(traspuesta([[1,2,3],[4,5,6]]))


def suma_matriz(matriz):
    x = 0
    z = 0
    while z < len(matriz):
        x += sum(matriz[z])
        z +=1
    return x

print(suma_matriz([[1,2,3],[4,5,6]]))

def contar_elementos(matriz):
    x = 0
    i = 0
    while i < len(matriz):
        x += len(matriz[i])
        i +=1
    return x

print(contar_elementos([[1,2,3],[4,5,6]]))

def suma_columnas(matriz):
    lista = []
    i = 0
    while i < len(matriz):
        j = 0
        suma = 0
        while j < len(matriz):
           suma += matriz[j][i]
           j += 1
        lista.append(suma)
        i +=1
    return lista

print(suma_columnas([[1,2,3],[4,5,6],[7,8,9]]))

def es_cuadrada(matriz):
    if len(matriz) == 0:
        return matriz
    i = 0
    while i < len(matriz):
        if (len(matriz) == len(matriz[i])) == False:
            return False
        i += 1
    return True

print(es_cuadrada([]))

def columna(matriz,n):
    l = []
    i = 0
    while i < len(matriz):
        l.append(matriz[i][n])
        i += 1
    return l

print(columna([[1,2,3],[4,5,6],[7,8,9]], 2))

def pin_valido(s):
    if len(s) != 4 and len(s) != 6:
        return False
    i = 0
    while i < len(s):
        try:
            int(s[i])
        except ValueError:
            return False
        i += 1
    return True
    
print(pin_valido("127464"))

def swap(cadena, a, b):
    return cadena.translate(str.maketrans(a+b,b+a))

print(swap("aabbccc", "a", "b"))

def harshad(n):
    l = map(int,list(str(n)))
    return n % sum(l) == 0 

print(harshad(171))

def words(letras, indices):
    l = [""]  * len(letras)
    i = 0
    while i < len(letras):
        l[indices[i]] = letras[i]
        i +=1
    return "".join(l)

print(words(["h","l","o","a"],[0,2,1,3]))

def burla(frase):
    return frase.translate(str.maketrans("aeiou", "eeeee"))

print(burla("Hola que tal como estan todos"))

#l = list("hola buenas tardes")
#print(l)
#m = []
#i = 0
#while i < len(l):
#    if l[i] == "a" or "e":
        

def triangulo(a,b,c):
    from math import sqrt
    l = [a,b,c]
    x = ((a + b + c) / 2)
    s = x
    i = 0
    while i < 3:
        s *= x - l[i]
        i += 1
    return sqrt(s)

print(triangulo(5,5,5))

def navidad(n): 
    i = 1
    while i <= n:
        print(" " * (n -i)  + "*" * (2*i - 1) )
        i +=1
    print(" " * (n-1) + "*")

navidad(4)


def factorial(n):
    f = 1
    x = 1
    while x <= n:
        f *= x
        x +=1
    return f 

def nk(n,k):
    """"""
    return factorial(n) / (factorial(n-k) * factorial(k))

print(nk(8,8))

def ordenar_numeros(lista):
    nueva = lista
    i = 0
    while i < len(lista):
        nueva[i] = int("".join((sorted(str(lista[i])))))
        i += 1
    return nueva
print(ordenar_numeros([515,755,929]))

def intercambiar(persona):
    i = 1
    fin = ""
    while i > 0:
        fin += str(list(persona[i]))
        i -= 1
    return fin

print(intercambiar("Paco Sanz")) 

#Hola xd