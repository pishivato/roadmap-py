import json 


with open("equipos.json", encoding="utf-8") as f:
    dispositivos = json.load(f)

#SW01, SW02, AP01 y MDF

print(f"---------------- inventario de red ---------------\n")
for d in dispositivos:
    estado = "\u2705" if d["activo"] else "\u274C"
    print(f"{d["nombre"]:15} | {d["tipo"]:15} | {d["ip"]:15} | {d["ubicacion"]:10} | {estado}")
    

#lineas = [f"{d['nombre']:15} | {d['tipo']:15} | {d['ip']:15} | {d['ubicacion']:10} | {d['activo']}" for d in dispositivos]
#print("\n".join(lineas))