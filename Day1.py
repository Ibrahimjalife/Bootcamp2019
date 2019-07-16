print(3245+564) #Suma de enteros 
print(3*5)
print(7/9)
print(90-4)
print ("Hola " * 10) #Print "Hola" 10 times 
print ("At the end of the day you just need a cup of coffee                                      " * 100)
print("GET FUCKED" + "3")
#Lo siguiente es una concatenacion de strings/ str concatenacion
###################################################3
x = 3
c = 10
print (x+c)
x = 3
t = 9
print(x*t)
a = 7
b = -3 + a
c = 3*b
print(a+c) #These are variables 
print(a, b, )
#########################
#Ej. 1 Crear una variable nombre y una variable edad con sus nombres y edades e imprimir:
# Hola, me llamo _____ y tengo _____ years old
name = "Ibrahim"
age = 2*9
print("Hello, my name is", name,  "Im", age, "years old")

# Ej. 1.1 Crear una variable hobby con tu pasatiempo 
# e imprimir 
name = "Ibrahim"
age = 2*9
hobby = "to do volunteer work I guess"
print( "Hello, my name is", name, "and Im", age,". Also, something important about me is that I love", hobby, ".")
################################

lista_vacia = [] #con los corchetes se crea una lista vacia
listax = [1,2,6,7] #lista con 4 elementos de tipo anterior 
print(lista_vacia) # se imprime la lista vacia
print(listax) #se imprime la listax
datos = ("Marce") # Se crea una lista de datos con un elemento string
print(datos) # Imprimimos la lista anterior
alumnos = ["Jose", "Ramoncito", name, "Maria"] #lista de alumnos
print(alumnos)
nro_alumnos = 3
print(alumnos[2], alumnos [0])

#Ej. Crear una lista datos que en el primer lugar este tu nombre 
# y en la segunda posicion este tu edad
# Imprimir "Hola me llamo___, y tengo ___ years"
list = [ "Ibrahim", 18] 
print("Hola, me llamo", list[0], ", y tengo", list[1], "years old")
print(list)
list.append("Student")
print(list)
print(list[2])

# Ej. Agregar una profesion y un hobby a la lista "list"
# previamente creada (usar append ())
# imprimir lista

list.append("dancing")
print(list)
list.pop()
print(list)
list.pop(1)
print(list)

# Funcion len() = lenght

print(list)
print(len(list))

# Ej. Obtener la dimension de la lista datos e imprimir:
# "La lista datos tiene _____ elementos

data_length = len(list)
print("La lista de datos tiene",data_length, "elementos")

comment = "I dont care"
print(len(comment)) 
# Imprimir el ultimo elemento de una lista sin saber cuantos elementos tiene
# Pista usar len()
print("-------------------------")
numbers = [5,6,3,5,6,3,5,7,4,3,5,7,4,3,5,7,4,3,5,6,3,5]
print(numbers)
print(numbers[len(numbers)-1])
print(len(numbers))
print(numbers[21])
print(numbers[0])
####################

serie = ["Ibrahim", 24, 23, 23, 45, "Student"]
print(serie[5])
print(serie[len(serie)-1])

################### Bucles/Loops/Ciclos/Iteraciones 

lista_temas = ["variables", "listas", "tipos de datos"]

for concepts in lista_temas:
    print("Today I learned", concepts)
    print("Fun!")
print("What an awesome day!")

#Recorrer una lista imprimir en cada ciclo 
#El valor del elemento con 3 signos de admiracion y al fina fuera del bucle "FIN!!!"

for instagram in serie:
    print(instagram, "!!!")
print("FIN!!!")

DSA = ["ISA", "BELLA", "TROCHE"]
ASD = ["NOTA", "CARA", "PABLO"]
AYQ = ["MESA", "ROJO", "COSA"]

for google in DSA:
    for yahoo in ASD:
        for explorer in AYQ:
            print(google, yahoo, explorer)

for x in range(10):
    print("HI!")

for x in range(10):
    print("Nevermind",x)

for x in range(10):
    print(x, "Dont care")

#Ej. Imprimir los numeros del 1 al 100 unsando for y range
#Imprimir el resultado de la suma de los numeros del 1 al 100

for x in range(1,101):
    print(x)


sum_x = 0
for x in range(1,11):
    sum_x = x + sum_x
print(sum_x)

   