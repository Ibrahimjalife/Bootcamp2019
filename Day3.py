
gente_ausentes = [ "Alex", "Pedro", "Iris", "Steven"]

def ausentes(listaaus): # listaaus representa a gente ausentes 
    for aus in listaaus: # aus representa a los elementos de la lista gente ausentes  # listaaus a listaaus 
        print(aus)     # imprime todos los elementos de la lista 
ausentes(gente_ausentes) # gente_ausentes representa a listaaus 
print("------------------------")


ing_pan = ["harina", "levadura","sal", "azucar", "agua"] # Creamos la lista con los elementos 

def imprimir_lista(ingredientes, nombre_producto): # definimos la funcion, con los parametros que deseamos 

    print("Lista de compras de", nombre_producto)
    print("--------------------") 
    for producto in ingredientes:
        print(producto)

imprimir_lista(ing_pan, "pan")
print("---------------------------------")

ing_salsa = ["tomate", "azucar", "sal", "cebolla"]
imprimir_lista(ing_salsa, "salsa de pizza")

print( "-----------------------------------")

################## CONDICIONALES ###################

# == es igual a 
# > mayor que 
# < menor que 
# >= mayor o igual que 
# <= menor o igual que 
# ! = distinto o no igual 



a = 3 

if  a > 3:
    print("Si, a es mayor a 3")
    print("Chau!")
else:
    print("No, a no es mayor a 3")

if a == 3:
    print(" a es igual a 3")

nota = 60 
if nota >= 60:
    print("Pasaste!")
else:
    print("Hule ya")

score = 75
if score < 75:
    print( "Thank u, next semester")
else:
    print(" You might graduate")

# Ej.: Crear una funcion que reciba como parametro una 
# nota del 1 al 100 e imprima si pasaste o te aplazaste 
print("-----------------------------------")
score2 = 67
def grades(scores):
    print("The student did" , scores)
    if scores > 75:
        print("Might fail later, but enjoy the moment")
    else:
        print("Damn, gotta see u again")
grades(score2)

a = 7 
if a > 5 and a < 10 :
    print("a es mayor a 5 y menor que 10")
else: 
    print("a no esta en el rango, alguna de las 2 condiciones no se cumplieron")

if a > 5 or a < 10:
    print("a es mayor que 5 o menor que 10")
else: 
    print(" a no es mayor que 5 ni menor que 10")

print(5>3)
print(5==3)

edad = 8 

if edad > 18:
    print("Deberia estar en la universidad")
elif edad > 13:
    print("Deberia estar en la secundaria")
elif edad > 6:
    print("Deberia estar en la primaria")
else:
    print("Deberia estar en su casa bbdlc")

print("-------------------------------")

# Ej.: Crear una funcion puntaje que reciba como parametro una nota 
# del 1 al 100 e imprima que nota sacaste
# nota < 60 -------> 1
# nota entre 60 y 70 ---> 2 
# nota entre 71 y 75 -----> 3
# nota entre 76 y 85 -------> 4
# nota mayor que 85 -----------> 5

score3 = 898
def grades(scores, name):
    if scores >= 0 and scores <= 100:
        if scores < 60:
            print("Sacaste 1",",", name)
        elif scores >= 60 and scores <=70:
            print("Sacaste 2",",", name)
        elif scores >= 71 and scores <= 75:
            print("Sacaste 3",",", name)
        elif scores >= 76 and scores <= 85:
            print("Sacaste 4",",", name)
        elif scores > 85:
            print("Sacaste 5",",", name)
    else:
        print("Error: Nota fuera de rango", ",", name)

    
grades(score3, "Rafael")

print("-----------------------------")
# nombre = input("Ingresa tu nombre: ")
# print("Hola", nombre)

# num1 = input("Ingresa el primer numero para sumar: ")   
# num2 = input("Ingresa el segundo numero para sumar: ") 
# print("El resultado es: ", int(num1)+ int(num2))

print("-----------------------------")

# edad = 33 
# saludo = ("Tenes", + str(edad))
# print(saludo)

# Ej.: Pedir al usuario que ingrese tres numeros y multiplicarlos 
# entre si, imprimir el resultado
#nombre = input("Ingrese tu nombre:")
#num1 = input("Ingresa el primer numero a multiplicar: ")
#num2 = input("Ingresa el segundo numero a multiplicar:")
#num3 = input("Ingresa el tercer numero a multiplicar:")
#print("El resultado es:", int(num1)* int(num2)* int(num3))

print("---------------------------------------")


#Ej2: Pedir al usuario un numero del 1 al 100 y llamar a la 
# funcion que retornaba la nota que creamos hace rato 
# utilizando el valor ingresado por el usuario 

#nombre = input("Ingrese tu nombre:")
#calif = input("Ingrese su puntaje:")
#grades(int(calif),  nombre)

print("----------------------------------------")

#year = int(input("Year:"))
#f year%4==0 and year%100!=0:
 #   print("It is a leap-year.")
#else:
 #   print("It is not a leap-year.")


print("---------------------------------------")
nombre = ["Jose", "Raul"]
nota =[64, 89]

if len(nombre)==len(nota):   # Verificar que el numero de elementos sea igual en cada lista 
    for x in range(len(nombre)): 
        print(nombre[x],nota[x])

############# Bucle while == Mientras ###########

# x = 0
# while x != 5:
#     print("Hola esto es un blucle while")
#     x = int(input("Ingresa un numero:"))
#     print("El valor de x ahora es", x)
# print("Termino!!")

# # Contador

# contador = 0
# while contador < 10:
#     print("Sigo en el bucle while")
#     contador = contador + 1
#     print("Se repitio", contador, "veces.")    
# print("Ahora termina.")


# # Contador Inverso 
# contador = 10 
# while contador > 0:
#     print("Sigo en el bucle while")
#     contador = contador - 1 
#     print("Te quedan", contador, "oportunidades.")
# print("Se termino.")




# Usando while pedir al usuario ingredientes para hacer una pizza
# y agregar a una lista, al final imprimir la lista 
 
# conta = 0   # iniciamos el contador en 0
# ingredients =[] # creamos una lista 
# print("Los ingredientes para la pizza:")
# while conta < 5: # se va a repetir 
#     ingredients.append(input("Ingrediente:")) 
#     conta = conta + 1
# print("Los ingredientes de la lista son:", ingredients)



# Ej. Crear un juego de adivinar el numero como ell de arriba y 
# darle pistas si el numero que ingreso es mayor o menor 
# al numero a adivinar 
# pista usar elif 

secret = 67
adivino = False
from random import randint

while adivino == False:
    apuesta = int(input("Adivina el numero secreto del 1 al 100:"))
    if apuesta > secret:
        print("Intenta un numero menor.")
    elif apuesta < secret:
        print("Intenta un numero mayor.")
    
    if apuesta == secret:
        print("GANASTE!!")
        adivino = True 
    
    else:
        print("Segui participando ndeitavya.")


# Ej2 Buscar como generar un numero aleatorio para secret 





    



