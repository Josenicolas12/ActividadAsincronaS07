# Defininiendo variables
variable1 = 4
variable2 = 8
variable3 = 2

var_division1 = 12
var_division2 = 4

#Enteros (int)
#multiplicacion de numeros enteros
multiplicacion = variable1 * variable2 * variable3
#Divison  con numeros enteros
division_entera = int(var_division1 // var_division2) 
resultado_suma = multiplicacion + division_entera
print("El resultado de la multiplicación es:", multiplicacion)
print("El resultado de la división entera es:", division_entera)
print("El resultado de la suma es:", resultado_suma)

# Definir variables de tipo flotante (Float)
var_exponecial1 = 5
var_exponecial2 = 2

var_modul1 = 2 
var_modul2 = 4 

exponencial = var_exponecial1 ** var_exponecial2
#Operando modulo
modulo = var_modul1 % var_modul2
resultado_flotante = exponencial - modulo
division = resultado_suma / resultado_flotante
print("El resultado del exponencial es:", exponencial)
print("El resultado del módulo es:", modulo)
print("El resultado de la resta es:", resultado_flotante)
print("El resultado de la división es:", division)

# Definir variables de tipo complejo (Complex)
complejo1 = 2 + 3j
complejo2 = 4 + 2j
complejo3 = 1 - 1j
complejo4 = -3 + 4j
numeroComplejo = complejo1 + complejo2 + complejo3 + complejo4
print("El numero complejo es:", numeroComplejo)

# Definir variables de tipo carácter (String)
fruta1 = "Sandia"
fruta2 = "Mango"
fruta3 = "Manzana"
fruta4 = "Pera"
fruta5 = "Piña"

# Definir variable de tipo booleano (Bool)
nombre_fruta = input("Ingrese el nombre de una fruta: ")
if nombre_fruta == fruta1:
    print(fruta1 + " es la fruta favorita de Gerardo.")
elif nombre_fruta == fruta2:
    print(fruta2 + " es la fruta favorita de Nicolas.")
elif nombre_fruta == fruta3:
    print(fruta3 + " es la fruta favorita de Bryan.")
elif nombre_fruta == fruta4:
    print(fruta4 + " es la fruta favorita de Rolando.")
elif nombre_fruta == fruta5:
    print(fruta5 + " es la fruta favorita de Aaron.")
else:
    print("La fruta ingresada no está en la lista.")
    
# Mensaje de finalización del programa
print("La ejecución del programa ha terminado.")