import os 

linea = "===================================="
os.system('clear')
def linea():
    print(linea)

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
diccVehiculos = {"Barco":"mar", "Coche": "tierra", "Avion": "aire"}
print(diccVehiculos["Barco"])
print(diccVehiculos.get("Satelita","no existe"))
print(diccVehiculos, id(diccVehiculos))