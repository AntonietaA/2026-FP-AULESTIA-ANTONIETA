#Tarea semana 15

#Guardar frutas sin repetir usando conjunto
frutas={"manzana", "pera","uva","manzana","pera"}
total_frutas=set(frutas)
print(total_frutas)

nueva_fruta=input("Nueva fruta: ")
frutas.add(nueva_fruta)
print(frutas)

buscar=input("\n¿Qué fruta busca? ")

if buscar in frutas:
    print("Fruta", buscar, "si se encuentra")
else:
    print("Fruta", buscar, "no se encuentra")

print("\n Listado de frutas")
for fruta in frutas:
    print(fruta)