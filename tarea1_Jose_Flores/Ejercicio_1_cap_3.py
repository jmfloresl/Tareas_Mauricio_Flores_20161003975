#capitulo 3.11

#Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
#1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

horas= int(input("Introduzca las Horas: "))
tarifa= float(input("Intruduzca Tarifa por hora: "))

if horas > 40:
    calculo = (horas - 40) * 1.5 * tarifa
    salario = (40 * tarifa) + calculo 
    
else : salario= horas*tarifa 


print("Salario: ", salario )