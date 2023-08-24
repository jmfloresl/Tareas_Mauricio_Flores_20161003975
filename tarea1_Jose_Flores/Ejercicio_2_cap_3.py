# capitulo 3.11

#Reescribe el programa del salario usando try y except, de modo que el
#programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
#un mensaje y saliendo del programa.

try:
    horas= int(input("Introduzca las Horas: "))
    tarifa= float(input("Intruduzca Tarifa por hora: "))
    
    if horas > 40:
     calculo = (horas - 40) * 1.5 * tarifa
     salario = (40 * tarifa) + calculo 
    
    else : salario= horas*tarifa 

    print("Salario: ", salario )
     
except: 
    print("Error, por favor Introduzca un numero")    


