#Tipo de dato String/cadena de texto/str
"Esto es un string"
#Tipo de dato Ineger/Entero/int
105
#Listas
[] #Lista Vacia 
["Ibrahim", 18, "Student"] # Lista de 3 elementos
#Variables 
nombre = "Ibrahim"
edad = 9*2
variable_lista = ["Hola", nombre, edad]
# Acceder a un elemento de a lista 
print(variable_lista[0], edad, variable_lista[2])
#Acciones/operaciones sobre listas 
variable_lista.append("Leer libros") #agrega elemento a la lista 
variable_lista.pop()
variable_lista[1]
print(variable_lista[1])
print(variable_lista)
variable_lista[1] = "No me importa"
print(variable_lista[1])
#Bucles / Loop / Ciclos
print(len(variable_lista))

for whatever in variable_lista:
    print(whatever,variable_lista )

for whatever in variable_lista:
    print(variable_lista, whatever)

for x in variable_lista:
    print("Nevermind",x)

#Imprimir los numeros del 1 al 10

for w in range(1,11):
    print(w)

otra_lista = [4, "no", 45, "si"]

dim_de_lista = len(otra_lista)
print("La dimension de otra_lista", dim_de_lista)
indice_del_ultimo = dim_de_lista -1 
print(" El indice de ultimo elemento es", indice_del_ultimo)
print(otra_lista[indice_del_ultimo])

# Solucion una linea 
print(otra_lista[len(otra_lista)-1])

sum_x = 0
for x in range(1, 11):
    sum_x = x + sum_x
print(sum_x)

# esto es equivalente 
for numero in range(1,11):
    print(numero)
# a esto 
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print(numero)
# imprimir hola 10 veces 
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print ("hola", numero) #imprimir numero es opcional 


####### FUNCIONES ########

# def nombre_de_la_funcion(argumentos)

def greeting(arguments):
    print("Hello", arguments)

greeting("Ibrahim")
greeting("Mohamad")

def addition(num1, num2):
    result = num1 + num2
    print(result)
addition(45,8)

def subtraction(num1, num2):
    result = num1 - num2
    print(result)
subtraction(5,2)

def addition(num1, num2):
    result = num1 + num2 
    return result 

print(addition(3, 6))

# Crear una funcion resta, que reciba como parametro dos numeros 
# y retorne la resta de esos numeros 
# luego llamaar a la funcion e imprimir e resultado 

def subtraction( num1, num2):
    result = num1 - num2
    print("The subtraction between", num1, "-", num2, "is equal to", result)
subtraction(5,3)

def subtraction(num1, num2):
    result = num1 - num2 
    print(result)

(subtraction(4,3))

def subtraction(num1, num2):
    result = num1 - num2 
    return result 
print(subtraction(2,1))

# Crear una funcion saludo que reciba como parametro nombre y edad 
# e imprimir "Hola soy ____ y tengo_____ years old"
# llamar varias veces a la funcion con distintos valores 
# Nota: retornar algo es opcional 

def saludo(name, age):
    print( "Hello, my name is", name, "and Im", age, "years old")

saludo("Ibrahim", 18)

###########################################
def suma2(num1, num2):
    return num1 + num2 
print(suma2(2,3))
print("---------------------------------------------------------------")

#Ej. Crear una funcion suma_lista que reciba como argumento una lista de numeros 
# y retorne la suma de sus elementos 
# Pista: Usar for y una variable acumulador 

listita = [1,2,3,4,5] # 1+2+3+4+5
listota = [100, 5, 5] #el valor de retorno seria 110


# Pista 2, la llamada deberia ser:
# suma_lista(listita)
# suma_lista(listota)
# def suma_lista(listita):

def suma_lista(listita):
    sum_x = 0
    for x in listita  :
        sum_x = x + sum_x
    return sum_x
print(sum_x)

       # return result



#Ej2. Lista al cuadrado
# Crear una funcion que reciba una lista de numero como parametro
# y retorne una lista con los numeros al cuadrado
# lista_cuadrado(listita)--> [1,4,9,14,25]

def multiplicacion(lista):
    lista_cuadrado = []
    for x in lista:
        lista_cuadrado.append(x*x)
    return lista_cuadrado

print(multiplicacion(listita))
print(multiplicacion(listota))

listita_cuad = multiplicacion(listita)
print("El cuadrado del ultimo elemento es", listita_cuad[len(listita_cuad)-1])

# Ej.: Eliminar todos los elementos de una lista utilizando "for"

grupo5 = ["N", "F1", "F2","A"]
print(grupo5)
for J in grupo5:
    print("Hola",J)
for J in range(len(grupo5)):
    print(grupo5)
    grupo5.pop()
print(grupo5)
grupo5.append("P")
print(grupo5)

#Crear una funcion suma_cuadrado que reciba una lista de nunmeros 
# y retorner el valor de la suma de cada numero al cuadrado 
# [1,2,3,4,5] --> 1+4+9+16-->30 

print("------------------------------------")

numbers = [1,2,3,4]
def opera(numbers):
    sum_x = 0
    for x in numbers  :
        sum_x = x*x + sum_x
    return sum_x
op = opera(numbers)
print(op)


    

    