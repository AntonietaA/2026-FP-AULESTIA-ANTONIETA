#Calcular el promedio de 3 notas

def calificaciones (nota_1, nota_2, nota_3):
    media=(nota_1+nota_2+nota_3)/3
    return media

nota_1=float(input("Ingrese la nota 1:"))
nota_2=float(input("Ingrese la nota 2:"))
nota_3=float(input("Ingrese la nota 3:"))

promedio=calificaciones(nota_1,nota_2,nota_3)
print("Promedio",promedio)
