import os 

linea_ = "===================================="
os.system('clear')
def linea():
    print(linea_)
linea();print("LISTAS");linea()
#LISTAS
jedis = ["Yoda", "Obi Wan", "Anakin", "Luke"]
jedis1 = ["Yoda", 1, "Darth Vader", 0, "Obi Wan", 1]
sith = ["Darth Vader", "Palpatine"]
fuerza = [["Yoda", "Obi Wan", "Anakin", "Luke"],["Darth Vader", "Palpatine"]]
print(fuerza)
jedis += ["Qui-Yong"] # sin los corchetes añade una lista con cada letra
print(jedis)
print(fuerza[1][1])
nuevafuerza=jedis+jedis1
print(nuevafuerza)
jedis = jedis + ["Pinocho"]
print(jedis)
print(jedis[1:4])
#jedis[1:4]=["Pepito"]
print(jedis)
for jedi in range(len(jedis)):
    print(jedi)
a = range(20)
print(list(a))

linea()
# DICCIONARIOS
os.system("clear")
linea();print("DICCIONARIS");linea()
la_Fuerza = {
    "Yoda":"Jedi",
    "Darth_Sidious":"Lord Sith",
    "Conde_Dooku": "Lord Sith",
    "Qui_Gon_Jinn": "Jedi",
    "Darth_Maul": "Lord Sith",
    "Obi_Wan_Kenobi": "Jedi",
    "Luke_Skywalker": "Jedi"
}
print(la_Fuerza)
print(f'Obi-Wan Kenobi es un {la_Fuerza.get("Obi_Wan_Kenobi")}')
print(la_Fuerza.get("Anakin_Skywaker", "No existe aún"))
la_Fuerza["Anakin_Skywalker"]="Jedi" #Añadir una nueva clave-valor
print(f'Anakin Stywalker aun es un {la_Fuerza.get("Anakin_Skywalker")}')
print("Anakin se pasa al lado oscuro")
la_Fuerza["Anakin_Skywalker"] = "Lord Sith"
print(f'Anakin Stywalker ahora es un {la_Fuerza.get("Anakin_Skywalker")}')
jedi_malo = la_Fuerza.pop("Anakin_Skywalker")
print(la_Fuerza)
nueva_Cosa = la_Fuerza.copy()
print(la_Fuerza)
print(nueva_Cosa)
print(id(la_Fuerza), " ---", id(nueva_Cosa))
la_Fuerza.setdefault("Darth Vader","Lord Sith")
print("LLEGÖ EL MEJOR")
print(la_Fuerza)

for nombre, bando in la_Fuerza.items():
    print(f'{nombre} es un {bando}')
print("Ahora sólo las claves")
for nombre in la_Fuerza.keys(): # solo las claves
    print(f'- {nombre}')
print(sorted(la_Fuerza.items()))