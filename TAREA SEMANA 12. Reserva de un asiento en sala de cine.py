#asientos en el cine
asientos= [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

while True:

    fila=int(input("Ingrese la ubicación de la fila del asiento: "))
    columna=int(input("Ingrese la columna del asiento: "))

    asientos[fila][columna]=1

    print("Reserva exitosa")

    print("Estado de sala: ")

    for fila_nueva in asientos:
       for asiento in fila_nueva:
            print(asiento, end=" ")
       print()


    nueva_reserva=input("¿Nueva reserva? (si/no): ")

    if nueva_reserva== "no":
        break

print("Estado de reservas de la sala")

for fila in asientos:
    for asiento in fila:
        print(asiento, end=" ")
    print()