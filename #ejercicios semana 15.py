#ejercicios semana 15

#1 lista de tareas (lista)
tareas=[]
tareas.append ("Estudiar")
tareas.append ("Ejercicio")
tareas.append ("Leer")

print(tareas)

#eliminar el segundo elemento
tareas.pop(1)
print(tareas)

#eliminar duplicados (set)

nombres =["Ana", "Luis","Ana"]

unicos=set(nombres)
print(unicos)

#Agenda telefónica (diccionario)

agenda={}

agenda["Ana"]="097"
agenda["Luis"]="099"
print(agenda["Luis"])

#Contador de palabras (diccionario)

palabras={"sol","luna","sol"}

contador={}
for p in palabras:
    contador[p]=contador.get(p,0)+1

print(contador)    

#Contador de palabras (set y diccionario)

estudiantes ={"Ana","Luis","Ana"}

notas= {
    "Ana":9.0,
    "Luis":8.5
    }
for e in estudiantes:
    print(e, ":",notas[e])