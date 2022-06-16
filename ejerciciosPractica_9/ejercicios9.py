# # Ejercicio 1 (Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.)

# numeros=int(input("ingrese un numero entero positivo, para realizar el conteo regresivo: "))
# if(numeros>0):
#     while numeros > 0:
#         print(numeros,end=",")
#         numeros=numeros-1
#         numcadena=(numeros)
    
#     print("Se acabó")
# else:
#     print("Ingresa un numero POSITIVO!")

############################# Ejercicio 2 ############################

#Media piramide con valor ingresado de input

# tamaño=int(input("ingrese tamaño de la mitad de la piramide: "))
# escalon=1
# while tamaño >0 :
    
#     for x in range(0, escalon):
#         print("*",end="")
#     print("")
#     escalon+= 1
#     tamaño-=1
# print("ejercicio finalizado")


############################# Ejercicio 3 ############################
 
# imprimir la misma "piramide" de arriba pero con numeros impares


tamaño=int(input("ingrese tamaño de la mitad de la piramide: "))
escalon=1
num=1
nume=1
while tamaño >0 :
    
    for x in range(0, escalon):
        for y in range(0,nume):
            print(nume,end="")
    nume=nume+1  
    print("")
    escalon+= 1
    tamaño-=1
print("ejercicio finalizado")

#probando para subir
