import json
import subprocess
from datetime import datetime
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def PING(IP):
    resultado = subprocess.run(
        ["ping", "-n", "1", "-w", "100", IP],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if resultado.returncode == 0:
        return "\u2705 -active"
    else:
        return "\u274C -inactive"
    
    
try:

    with open("equipos.json", encoding="utf-8") as f:
        dispositivos = json.load(f)

    with open("reporte.txt", "w", encoding="utf-8") as f:
        f.write(f"=== REPORTE DE RED FECHA: {date} ===\n")
        for d in dispositivos:
            lineas = f"{d['nombre']:15} | {d['ip']:15} | {PING(d['ip'])}"
            print(lineas)
            f.write(lineas + "\n")

except FileNotFoundError:
    print("Error: no se encontró equipos.json\n")
    exit(1)
except subprocess.SubprocessError:
    print("No se pudo hacer ping\n")
    exit(1)